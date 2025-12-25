"""Badge unlock service for tracking achievements."""

from typing import Optional, List
from sqlalchemy.orm import Session
from app.models import Badge, UserBadge, User

# Badge definitions - these will be seeded into the database
BADGE_DEFINITIONS = [
    # Milestone badges
    {
        "slug": "first-correct",
        "name": "First Steps",
        "description": "Get your first question correct",
        "icon_emoji": "🌟",
        "category": "milestone",
        "tier": "bronze",
        "unlock_criteria": {"type": "total_correct", "value": 1},
    },
    {
        "slug": "century",
        "name": "Century Club",
        "description": "Answer 100 questions",
        "icon_emoji": "💯",
        "category": "milestone",
        "tier": "silver",
        "unlock_criteria": {"type": "total_questions", "value": 100},
    },
    {
        "slug": "high-five-hundred",
        "name": "High Five Hundred",
        "description": "Answer 500 questions",
        "icon_emoji": "🖐️",
        "category": "milestone",
        "tier": "gold",
        "unlock_criteria": {"type": "total_questions", "value": 500},
    },
    # Streak badges
    {
        "slug": "streak-5",
        "name": "On Fire",
        "description": "Get 5 questions correct in a row",
        "icon_emoji": "🔥",
        "category": "streak",
        "tier": "bronze",
        "unlock_criteria": {"type": "streak", "value": 5},
    },
    {
        "slug": "streak-10",
        "name": "Unstoppable",
        "description": "Get 10 questions correct in a row",
        "icon_emoji": "⚡",
        "category": "streak",
        "tier": "silver",
        "unlock_criteria": {"type": "streak", "value": 10},
    },
    {
        "slug": "streak-25",
        "name": "Math Machine",
        "description": "Get 25 questions correct in a row",
        "icon_emoji": "🤖",
        "category": "streak",
        "tier": "gold",
        "unlock_criteria": {"type": "streak", "value": 25},
    },
    {
        "slug": "streak-50",
        "name": "Legendary",
        "description": "Get 50 questions correct in a row",
        "icon_emoji": "👑",
        "category": "streak",
        "tier": "platinum",
        "unlock_criteria": {"type": "streak", "value": 50},
    },
    # Mastery badges
    {
        "slug": "first-mastery",
        "name": "Skill Unlocked",
        "description": "Master your first skill",
        "icon_emoji": "🎯",
        "category": "mastery",
        "tier": "bronze",
        "unlock_criteria": {"type": "skills_mastered", "value": 1},
    },
    {
        "slug": "mastery-5",
        "name": "Rising Star",
        "description": "Master 5 skills",
        "icon_emoji": "⭐",
        "category": "mastery",
        "tier": "silver",
        "unlock_criteria": {"type": "skills_mastered", "value": 5},
    },
    {
        "slug": "mastery-10",
        "name": "Knowledge Keeper",
        "description": "Master 10 skills",
        "icon_emoji": "📚",
        "category": "mastery",
        "tier": "gold",
        "unlock_criteria": {"type": "skills_mastered", "value": 10},
    },
    # Evaluation badges
    {
        "slug": "first-evaluation",
        "name": "Tested",
        "description": "Complete your first evaluation",
        "icon_emoji": "📝",
        "category": "evaluation",
        "tier": "bronze",
        "unlock_criteria": {"type": "evaluations_completed", "value": 1},
    },
    {
        "slug": "perfect-section",
        "name": "Perfect Section",
        "description": "Get 100% on an evaluation section",
        "icon_emoji": "💎",
        "category": "evaluation",
        "tier": "gold",
        "unlock_criteria": {"type": "perfect_section", "value": 1},
    },
    {
        "slug": "high-scorer",
        "name": "High Scorer",
        "description": "Score 90% or higher on an evaluation",
        "icon_emoji": "🏆",
        "category": "evaluation",
        "tier": "gold",
        "unlock_criteria": {"type": "evaluation_score", "value": 90},
    },
]


def check_and_award_badges(
    db: Session,
    user: User,
    streak: int = 0,
    total_correct: int = 0,
    total_questions: int = 0,
    skills_mastered: int = 0,
    evaluations_completed: int = 0,
    evaluation_score: float = 0,
    perfect_section: bool = False,
) -> List[Badge]:
    """
    Check if user qualifies for any new badges and award them.

    Returns list of newly awarded badges.
    """
    newly_awarded = []

    # Get user's existing badge slugs
    existing_slugs = {ub.badge.slug for ub in user.badges}

    # Get all badges
    all_badges = db.query(Badge).all()

    for badge in all_badges:
        # Skip if already earned
        if badge.slug in existing_slugs:
            continue

        criteria = badge.unlock_criteria
        criteria_type = criteria.get("type")
        criteria_value = criteria.get("value")

        earned = False

        if criteria_type == "streak" and streak >= criteria_value:
            earned = True
        elif criteria_type == "total_correct" and total_correct >= criteria_value:
            earned = True
        elif criteria_type == "total_questions" and total_questions >= criteria_value:
            earned = True
        elif criteria_type == "skills_mastered" and skills_mastered >= criteria_value:
            earned = True
        elif criteria_type == "evaluations_completed" and evaluations_completed >= criteria_value:
            earned = True
        elif criteria_type == "evaluation_score" and evaluation_score >= criteria_value:
            earned = True
        elif criteria_type == "perfect_section" and perfect_section:
            earned = True

        if earned:
            user_badge = UserBadge(user_id=user.id, badge_id=badge.id)
            db.add(user_badge)
            newly_awarded.append(badge)

    if newly_awarded:
        db.commit()

    return newly_awarded


def get_user_badges(db: Session, user_id: int) -> List[dict]:
    """Get all badges with earned status for a user."""
    user_badges = db.query(UserBadge).filter(UserBadge.user_id == user_id).all()
    earned_badge_ids = {ub.badge_id for ub in user_badges}
    earned_dates = {ub.badge_id: ub.earned_at for ub in user_badges}

    all_badges = db.query(Badge).all()

    result = []
    for badge in all_badges:
        result.append({
            "id": badge.id,
            "slug": badge.slug,
            "name": badge.name,
            "description": badge.description,
            "icon_emoji": badge.icon_emoji,
            "category": badge.category,
            "tier": badge.tier,
            "earned": badge.id in earned_badge_ids,
            "earned_at": earned_dates.get(badge.id),
        })

    return result


def seed_badges(db: Session) -> int:
    """Seed badge definitions into database. Returns count of badges created."""
    existing_slugs = {b.slug for b in db.query(Badge.slug).all()}

    created = 0
    for badge_def in BADGE_DEFINITIONS:
        if badge_def["slug"] not in existing_slugs:
            badge = Badge(**badge_def)
            db.add(badge)
            created += 1

    if created > 0:
        db.commit()

    return created
