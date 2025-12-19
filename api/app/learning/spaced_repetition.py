"""Spaced repetition algorithm (modified SM-2)."""

from datetime import datetime, timedelta


def calculate_next_review(mastery_score: float, last_practiced: datetime) -> datetime:
    """
    Calculate when to review a skill next based on mastery.

    Uses a simplified spaced repetition algorithm:
    - Mastery 90-100: Review in 7 days
    - Mastery 70-89:  Review in 3 days
    - Mastery 50-69:  Review in 1 day
    - Mastery < 50:   Review immediately

    Args:
        mastery_score: Current mastery score (0-100)
        last_practiced: When the skill was last practiced

    Returns:
        Datetime when skill should be reviewed next
    """
    if mastery_score >= 90:
        interval_days = 7
    elif mastery_score >= 70:
        interval_days = 3
    elif mastery_score >= 50:
        interval_days = 1
    else:
        # Immediate review needed
        return datetime.utcnow()

    return last_practiced + timedelta(days=interval_days)


def is_due_for_review(next_review: datetime) -> bool:
    """Check if a skill is due for spaced repetition review."""
    if next_review is None:
        return False
    return datetime.utcnow() >= next_review
