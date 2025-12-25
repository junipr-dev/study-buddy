"""Badge routes for achievement tracking."""

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime

from app.database import get_db
from app.auth import get_current_user
from app.models import User
from app.services.badges import get_user_badges, seed_badges

router = APIRouter(prefix="/badges", tags=["badges"])


class BadgeResponse(BaseModel):
    """Badge response schema."""
    id: int
    slug: str
    name: str
    description: str
    icon_emoji: str
    category: str
    tier: str
    earned: bool
    earned_at: datetime | None = None

    class Config:
        from_attributes = True


@router.get("", response_model=List[BadgeResponse])
async def list_badges(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get all badges with earned status for current user."""
    badges = get_user_badges(db, current_user.id)
    return badges


@router.get("/earned", response_model=List[BadgeResponse])
async def list_earned_badges(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get only earned badges for current user."""
    badges = get_user_badges(db, current_user.id)
    return [b for b in badges if b["earned"]]


@router.post("/seed")
async def seed_badge_definitions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Seed badge definitions (admin only)."""
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")

    count = seed_badges(db)
    return {"message": f"Seeded {count} new badges", "count": count}
