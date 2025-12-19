"""SQLAlchemy database models."""

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class User(Base):
    """User account model."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    first_name = Column(String(50), nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    mastery = relationship("UserMastery", back_populates="user")
    question_history = relationship("QuestionHistory", back_populates="user")
    evaluations = relationship("Evaluation", back_populates="user", order_by="desc(Evaluation.completed_at)")


class Skill(Base):
    """Math skill/topic model."""

    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(100), unique=True, nullable=False, index=True)
    name = Column(String(200), nullable=False)
    subject = Column(String(50), nullable=False, index=True)
    description = Column(Text)
    khan_url = Column(String(500))
    explanation = Column(Text)
    difficulty_base = Column(Integer, default=1)

    # Relationships
    templates = relationship("QuestionTemplate", back_populates="skill")
    mastery = relationship("UserMastery", back_populates="skill")
    question_history = relationship("QuestionHistory", back_populates="skill")


class SkillPrerequisite(Base):
    """Skill prerequisite relationships."""

    __tablename__ = "skill_prerequisites"

    skill_id = Column(Integer, ForeignKey("skills.id"), primary_key=True)
    prerequisite_id = Column(Integer, ForeignKey("skills.id"), primary_key=True)


class QuestionTemplate(Base):
    """Question generation template model."""

    __tablename__ = "question_templates"

    id = Column(Integer, primary_key=True, index=True)
    skill_id = Column(Integer, ForeignKey("skills.id"), nullable=False)
    template_type = Column(String(50), nullable=False, index=True)
    template_data = Column(JSON, nullable=False)
    difficulty = Column(Integer, default=1)

    # Relationships
    skill = relationship("Skill", back_populates="templates")
    question_history = relationship("QuestionHistory", back_populates="template")


class UserMastery(Base):
    """User progress and mastery tracking."""

    __tablename__ = "user_mastery"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    skill_id = Column(Integer, ForeignKey("skills.id"), nullable=False)
    mastery_score = Column(Float, default=0.0)
    last_practiced = Column(DateTime(timezone=True))
    next_review = Column(DateTime(timezone=True))
    total_attempts = Column(Integer, default=0)
    correct_attempts = Column(Integer, default=0)

    # Relationships
    user = relationship("User", back_populates="mastery")
    skill = relationship("Skill", back_populates="mastery")


class QuestionHistory(Base):
    """Question attempt history."""

    __tablename__ = "question_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    skill_id = Column(Integer, ForeignKey("skills.id"), nullable=False)
    template_id = Column(Integer, ForeignKey("question_templates.id"), nullable=False)
    is_correct = Column(Boolean, nullable=False)
    time_taken_seconds = Column(Integer)
    difficulty = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="question_history")
    skill = relationship("Skill", back_populates="question_history")
    template = relationship("QuestionTemplate", back_populates="question_history")


class Evaluation(Base):
    """Saved evaluation/assessment results."""

    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    started_at = Column(DateTime(timezone=True), nullable=False)
    completed_at = Column(DateTime(timezone=True), server_default=func.now())
    overall_score = Column(Float, nullable=False)
    total_questions = Column(Integer, nullable=False)
    total_correct = Column(Integer, nullable=False)
    skills_mastered = Column(Integer, nullable=False, default=0)
    skills_review = Column(Integer, nullable=False, default=0)
    skills_study = Column(Integer, nullable=False, default=0)

    # Relationships
    user = relationship("User", back_populates="evaluations")
    skill_results = relationship("EvaluationSkillResult", back_populates="evaluation", cascade="all, delete-orphan")


class EvaluationSkillResult(Base):
    """Individual skill results within an evaluation."""

    __tablename__ = "evaluation_skill_results"

    id = Column(Integer, primary_key=True, index=True)
    evaluation_id = Column(Integer, ForeignKey("evaluations.id"), nullable=False)
    skill_id = Column(Integer, ForeignKey("skills.id"), nullable=False)
    skill_name = Column(String(200), nullable=False)
    subject = Column(String(50), nullable=False)
    proficiency_score = Column(Float, nullable=False)
    proficiency_level = Column(String(20), nullable=False)  # mastered, review, study
    questions_correct = Column(Integer, nullable=False)
    questions_total = Column(Integer, nullable=False)

    # Relationships
    evaluation = relationship("Evaluation", back_populates="skill_results")
    skill = relationship("Skill")
