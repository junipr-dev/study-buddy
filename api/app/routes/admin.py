"""Admin dashboard API endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from typing import List, Optional
from datetime import datetime, timedelta

from app.database import get_db
from app.models import User, Evaluation, EvaluationSkillResult, QuestionHistory, Skill
from app.auth import get_current_user

router = APIRouter(prefix="/admin", tags=["Admin"])


def require_admin(current_user: User = Depends(get_current_user)) -> User:
    """Dependency to require any admin access (full or readonly)."""
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )
    return current_user


def require_full_admin(current_user: User = Depends(get_current_user)) -> User:
    """Dependency to require full admin access (not readonly)."""
    if not current_user.is_admin or current_user.admin_level != 'full':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Full admin access required",
        )
    return current_user


@router.get("/check")
def check_admin_status(current_user: User = Depends(get_current_user)):
    """Check if current user has admin access."""
    return {
        "is_admin": current_user.is_admin,
        "admin_level": current_user.admin_level,
        "is_readonly": current_user.admin_level == 'readonly',
    }


@router.get("/stats")
def get_dashboard_stats(
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Get overall dashboard statistics."""
    # Total users
    total_users = db.query(func.count(User.id)).scalar()

    # Total evaluations
    total_evaluations = db.query(func.count(Evaluation.id)).scalar()

    # Users active in last 7 days (have evaluations)
    week_ago = datetime.utcnow() - timedelta(days=7)
    active_users = db.query(func.count(func.distinct(Evaluation.user_id))).filter(
        Evaluation.completed_at >= week_ago
    ).scalar()

    # Average score
    avg_score = db.query(func.avg(Evaluation.overall_score)).scalar() or 0

    # Total questions answered
    total_questions = db.query(func.count(QuestionHistory.id)).scalar()

    # Evaluations today
    today = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    evals_today = db.query(func.count(Evaluation.id)).filter(
        Evaluation.completed_at >= today
    ).scalar()

    return {
        "total_users": total_users,
        "total_evaluations": total_evaluations,
        "active_users_7d": active_users,
        "average_score": round(avg_score, 1),
        "total_questions_answered": total_questions,
        "evaluations_today": evals_today,
    }


@router.get("/users")
def get_all_users(
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db),
    limit: int = 50,
    offset: int = 0,
):
    """Get all users with their stats."""
    users = db.query(User).order_by(desc(User.created_at)).offset(offset).limit(limit).all()

    user_data = []
    for user in users:
        # Get latest evaluation
        latest_eval = db.query(Evaluation).filter(
            Evaluation.user_id == user.id
        ).order_by(desc(Evaluation.completed_at)).first()

        # Count evaluations
        eval_count = db.query(func.count(Evaluation.id)).filter(
            Evaluation.user_id == user.id
        ).scalar()

        # Count questions answered
        questions_count = db.query(func.count(QuestionHistory.id)).filter(
            QuestionHistory.user_id == user.id
        ).scalar()

        user_data.append({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "is_admin": user.is_admin,
            "created_at": user.created_at,
            "evaluation_count": eval_count,
            "questions_answered": questions_count,
            "latest_score": latest_eval.overall_score if latest_eval else None,
            "latest_eval_date": latest_eval.completed_at if latest_eval else None,
        })

    total = db.query(func.count(User.id)).scalar()

    return {
        "users": user_data,
        "total": total,
        "limit": limit,
        "offset": offset,
    }


@router.get("/users/{user_id}")
def get_user_detail(
    user_id: int,
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Get detailed information about a specific user."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Get all evaluations
    evaluations = db.query(Evaluation).filter(
        Evaluation.user_id == user_id
    ).order_by(desc(Evaluation.completed_at)).all()

    eval_data = []
    for evaluation in evaluations:
        skill_results = db.query(EvaluationSkillResult).filter(
            EvaluationSkillResult.evaluation_id == evaluation.id
        ).all()

        eval_data.append({
            "id": evaluation.id,
            "completed_at": evaluation.completed_at,
            "overall_score": evaluation.overall_score,
            "total_questions": evaluation.total_questions,
            "total_correct": evaluation.total_correct,
            "skills_mastered": evaluation.skills_mastered,
            "skills_review": evaluation.skills_review,
            "skills_study": evaluation.skills_study,
            "skill_results": [
                {
                    "skill_name": sr.skill_name,
                    "subject": sr.subject,
                    "proficiency_score": sr.proficiency_score,
                    "proficiency_level": sr.proficiency_level,
                }
                for sr in skill_results
            ]
        })

    # Get question history stats by skill
    skill_stats = db.query(
        Skill.name,
        Skill.subject,
        func.count(QuestionHistory.id).label('attempts'),
        func.sum(func.cast(QuestionHistory.is_correct, db.bind.dialect.name == 'sqlite' and 'INTEGER' or 'INT')).label('correct'),
    ).join(QuestionHistory, QuestionHistory.skill_id == Skill.id).filter(
        QuestionHistory.user_id == user_id
    ).group_by(Skill.id).all()

    return {
        "id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "is_admin": user.is_admin,
        "created_at": user.created_at,
        "evaluations": eval_data,
        "skill_stats": [
            {
                "skill_name": s[0],
                "subject": s[1],
                "attempts": s[2],
                "correct": s[3] or 0,
                "accuracy": round((s[3] or 0) / s[2] * 100, 1) if s[2] > 0 else 0,
            }
            for s in skill_stats
        ]
    }


@router.post("/users/{user_id}/toggle-admin")
def toggle_user_admin(
    user_id: int,
    admin: User = Depends(require_full_admin),
    db: Session = Depends(get_db),
):
    """Toggle admin status for a user. Requires full admin."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Prevent removing own admin status
    if user.id == admin.id:
        raise HTTPException(status_code=400, detail="Cannot modify own admin status")

    user.is_admin = not user.is_admin
    if user.is_admin:
        user.admin_level = 'readonly'  # New admins start as readonly
    else:
        user.admin_level = None
    db.commit()

    return {"id": user.id, "is_admin": user.is_admin, "admin_level": user.admin_level}


@router.get("/evaluations")
def get_all_evaluations(
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db),
    limit: int = 50,
    offset: int = 0,
):
    """Get all evaluations across all users."""
    evaluations = db.query(Evaluation, User).join(
        User, Evaluation.user_id == User.id
    ).order_by(desc(Evaluation.completed_at)).offset(offset).limit(limit).all()

    eval_data = [
        {
            "id": e.id,
            "user_id": e.user_id,
            "username": u.username,
            "first_name": u.first_name,
            "completed_at": e.completed_at,
            "overall_score": e.overall_score,
            "total_questions": e.total_questions,
            "total_correct": e.total_correct,
            "skills_mastered": e.skills_mastered,
            "skills_review": e.skills_review,
            "skills_study": e.skills_study,
        }
        for e, u in evaluations
    ]

    total = db.query(func.count(Evaluation.id)).scalar()

    return {
        "evaluations": eval_data,
        "total": total,
        "limit": limit,
        "offset": offset,
    }


@router.get("/skills/performance")
def get_skill_performance(
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Get performance statistics for each skill across all users."""
    # Query skill performance from evaluation results
    skill_stats = db.query(
        EvaluationSkillResult.skill_name,
        EvaluationSkillResult.subject,
        func.count(EvaluationSkillResult.id).label('times_tested'),
        func.avg(EvaluationSkillResult.proficiency_score).label('avg_score'),
        func.sum(func.cast(EvaluationSkillResult.proficiency_level == 'mastered', db.bind.dialect.name == 'sqlite' and 'INTEGER' or 'INT')).label('mastery_count'),
        func.sum(func.cast(EvaluationSkillResult.proficiency_level == 'study', db.bind.dialect.name == 'sqlite' and 'INTEGER' or 'INT')).label('study_count'),
    ).group_by(EvaluationSkillResult.skill_name, EvaluationSkillResult.subject).all()

    return {
        "skills": [
            {
                "skill_name": s[0],
                "subject": s[1],
                "times_tested": s[2],
                "avg_score": round(s[3] or 0, 1),
                "mastery_count": s[4] or 0,
                "study_count": s[5] or 0,
                "mastery_rate": round((s[4] or 0) / s[2] * 100, 1) if s[2] > 0 else 0,
            }
            for s in skill_stats
        ]
    }
