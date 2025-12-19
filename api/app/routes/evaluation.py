"""Evaluation mode endpoints for quick skill assessment."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Dict, Any
import uuid

from app.database import get_db
from app.models import User, Skill, QuestionTemplate
from app.schemas import QuestionResponse, AnswerSubmit
from app.auth import get_current_user
from app.generators import get_generator
from app.utils.answer_validation import answers_are_equivalent

router = APIRouter(prefix="/evaluation", tags=["Evaluation"])

# In-memory storage for evaluation sessions (in production, use Redis)
evaluation_sessions: Dict[str, Dict[str, Any]] = {}


@router.post("/start")
def start_evaluation(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Start a new evaluation session.

    Returns list of skills in chronological order and creates session.
    """
    # Get all skills ordered by ID (chronological)
    skills = db.query(Skill).order_by(Skill.id).all()

    # Filter to only skills with question templates
    skills_with_templates = []
    for skill in skills:
        has_template = db.query(QuestionTemplate).filter(
            QuestionTemplate.skill_id == skill.id
        ).first()
        if has_template:
            skills_with_templates.append(skill)

    if not skills_with_templates:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No skills with templates available for evaluation",
        )

    # Create evaluation session
    session_id = str(uuid.uuid4())
    evaluation_sessions[session_id] = {
        "user_id": current_user.id,
        "skills": [s.id for s in skills_with_templates],
        "current_index": 0,
        "results": [],  # {skill_id, skill_name, is_correct, question_id}
        "active_question": None,
        "completed": False,
        "failed_at": None,
        "started_at": datetime.utcnow(),
    }

    return {
        "session_id": session_id,
        "total_skills": len(skills_with_templates),
        "skills": [{"id": s.id, "name": s.name, "subject": s.subject} for s in skills_with_templates],
    }


@router.get("/next/{session_id}", response_model=QuestionResponse)
def get_next_evaluation_question(
    session_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get the next question in the evaluation sequence."""
    session = evaluation_sessions.get(session_id)
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Evaluation session not found or expired",
        )

    if session["user_id"] != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized for this evaluation session",
        )

    if session["completed"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Evaluation already completed",
        )

    # Get current skill
    current_index = session["current_index"]
    if current_index >= len(session["skills"]):
        session["completed"] = True
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No more skills to evaluate",
        )

    skill_id = session["skills"][current_index]
    skill = db.query(Skill).filter(Skill.id == skill_id).first()

    if not skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Skill {skill_id} not found",
        )

    # Get a template for this skill (difficulty 2 for fair evaluation)
    template = db.query(QuestionTemplate).filter(
        QuestionTemplate.skill_id == skill_id,
        QuestionTemplate.difficulty == 2,
    ).first()

    if not template:
        # Fallback to any difficulty
        template = db.query(QuestionTemplate).filter(
            QuestionTemplate.skill_id == skill_id
        ).first()

    if not template:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No templates found for skill {skill_id}",
        )

    # Generate question
    generator = get_generator(template.template_type)
    question_data = generator(template.difficulty)

    question_id = str(uuid.uuid4())

    # Store active question
    session["active_question"] = {
        "question_id": question_id,
        "skill_id": skill_id,
        "skill_name": skill.name,
        "correct_answer": question_data["answer"],
        "answer_numeric": question_data.get("answer_numeric"),
        "steps": question_data.get("steps", []),
        "created_at": datetime.utcnow(),
    }

    return {
        "question_id": question_id,
        "skill_id": skill_id,
        "skill_name": skill.name,
        "question": question_data["question"],
        "difficulty": template.difficulty,
        "template_id": template.id,
    }


@router.post("/answer/{session_id}")
def submit_evaluation_answer(
    session_id: str,
    answer_data: AnswerSubmit,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Submit an answer for the current evaluation question."""
    session = evaluation_sessions.get(session_id)
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Evaluation session not found",
        )

    if session["user_id"] != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized",
        )

    question = session.get("active_question")
    if not question or question["question_id"] != answer_data.question_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found or mismatched",
        )

    # Validate answer
    is_correct = answers_are_equivalent(answer_data.answer, question["correct_answer"])

    # Record result
    session["results"].append({
        "skill_id": question["skill_id"],
        "skill_name": question["skill_name"],
        "is_correct": is_correct,
        "user_answer": answer_data.answer,
        "correct_answer": question["correct_answer"],
    })

    # If incorrect, mark where they failed and complete evaluation
    if not is_correct:
        session["failed_at"] = session["current_index"]
        session["completed"] = True

        return {
            "is_correct": False,
            "evaluation_complete": True,
            "failed_at_skill": question["skill_name"],
            "correct_answer": question["correct_answer"],
            "steps": question.get("steps"),
        }

    # If correct, move to next skill
    session["current_index"] += 1
    session["active_question"] = None

    # Check if evaluation complete (all skills passed)
    if session["current_index"] >= len(session["skills"]):
        session["completed"] = True

        return {
            "is_correct": True,
            "evaluation_complete": True,
            "all_passed": True,
        }

    return {
        "is_correct": True,
        "evaluation_complete": False,
        "skills_remaining": len(session["skills"]) - session["current_index"],
    }


@router.get("/report/{session_id}")
def get_evaluation_report(
    session_id: str,
    current_user: User = Depends(get_current_user),
):
    """Get the final evaluation report card."""
    session = evaluation_sessions.get(session_id)
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Evaluation session not found",
        )

    if session["user_id"] != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized",
        )

    if not session["completed"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Evaluation not yet completed",
        )

    total_skills = len(session["skills"])
    passed_count = sum(1 for r in session["results"] if r["is_correct"])
    failed_skill = None

    if session["failed_at"] is not None:
        # Find the failed skill
        failed_result = session["results"][session["failed_at"]]
        failed_skill = {
            "skill_id": failed_result["skill_id"],
            "skill_name": failed_result["skill_name"],
            "user_answer": failed_result["user_answer"],
            "correct_answer": failed_result["correct_answer"],
        }

    return {
        "session_id": session_id,
        "total_skills": total_skills,
        "skills_tested": len(session["results"]),
        "skills_passed": passed_count,
        "all_passed": session["failed_at"] is None,
        "failed_skill": failed_skill,
        "passed_skills": [
            {"skill_id": r["skill_id"], "skill_name": r["skill_name"]}
            for r in session["results"] if r["is_correct"]
        ],
        "completion_percentage": (passed_count / total_skills * 100) if total_skills > 0 else 0,
        "started_at": session["started_at"],
    }
