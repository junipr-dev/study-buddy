"""Mastery score calculation algorithms."""

from datetime import datetime, timedelta
from typing import List
from sqlalchemy.orm import Session
from app.models import QuestionHistory


def calculate_mastery(
    user_id: int,
    skill_id: int,
    db: Session,
    recent_weight: float = 0.7,
) -> float:
    """
    Calculate mastery score (0-100) with recency bias.

    Args:
        user_id: User ID
        skill_id: Skill ID
        db: Database session
        recent_weight: Weight given to recent attempts (0-1)

    Returns:
        Mastery score from 0 to 100
    """
    # Get all attempts for this skill
    all_attempts = (
        db.query(QuestionHistory)
        .filter(
            QuestionHistory.user_id == user_id,
            QuestionHistory.skill_id == skill_id,
        )
        .order_by(QuestionHistory.created_at.desc())
        .all()
    )

    if not all_attempts:
        return 0.0

    # Calculate overall accuracy
    total_correct = sum(1 for attempt in all_attempts if attempt.is_correct)
    overall_accuracy = total_correct / len(all_attempts)

    # Calculate recent accuracy (last 10 attempts)
    recent_attempts = all_attempts[:10]
    if recent_attempts:
        recent_correct = sum(1 for attempt in recent_attempts if attempt.is_correct)
        recent_accuracy = recent_correct / len(recent_attempts)
    else:
        recent_accuracy = overall_accuracy

    # Weighted average favoring recent performance
    mastery = (
        overall_accuracy * (1 - recent_weight) + recent_accuracy * recent_weight
    ) * 100

    return min(mastery, 100.0)


def get_recent_accuracy(
    user_id: int, skill_id: int, db: Session, limit: int = 10
) -> float:
    """Get accuracy for recent attempts."""
    recent_attempts = (
        db.query(QuestionHistory)
        .filter(
            QuestionHistory.user_id == user_id,
            QuestionHistory.skill_id == skill_id,
        )
        .order_by(QuestionHistory.created_at.desc())
        .limit(limit)
        .all()
    )

    if not recent_attempts:
        return 0.0

    correct = sum(1 for attempt in recent_attempts if attempt.is_correct)
    return correct / len(recent_attempts)


def get_recent_results(
    user_id: int, skill_id: int, db: Session, limit: int = 3
) -> List[bool]:
    """Get list of recent attempt results (True = correct, False = incorrect)."""
    recent_attempts = (
        db.query(QuestionHistory)
        .filter(
            QuestionHistory.user_id == user_id,
            QuestionHistory.skill_id == skill_id,
        )
        .order_by(QuestionHistory.created_at.desc())
        .limit(limit)
        .all()
    )

    return [attempt.is_correct for attempt in recent_attempts]
