"""Seed script to populate initial skills and question templates from JSON."""

import json
import os
from pathlib import Path

from app.database import SessionLocal, engine, Base
from app.models import Skill, QuestionTemplate, SkillPrerequisite


def load_skills_json():
    """Load skills from content/skills.json."""
    content_dir = Path(__file__).parent.parent / "content"
    skills_file = content_dir / "skills.json"

    if not skills_file.exists():
        raise FileNotFoundError(f"Skills file not found: {skills_file}")

    with open(skills_file, 'r') as f:
        return json.load(f)


def load_explainer(skill_slug, subject):
    """Load explainer content for a skill."""
    content_dir = Path(__file__).parent.parent / "content" / "explainers"

    # Convert subject to directory name (e.g., "Algebra I" -> "algebra-1")
    subject_dir_map = {
        "Pre-Algebra": "pre-algebra",
        "Algebra Basics": "algebra-basics",
        "Algebra I": "algebra-1",
        "Algebra II": "algebra-2",
        "Trigonometry": "trigonometry",
        "Precalculus": "precalculus",
    }

    subject_dir = subject_dir_map.get(subject, subject.lower().replace(" ", "-"))
    explainer_file = content_dir / subject_dir / f"{skill_slug}.md"

    if explainer_file.exists():
        with open(explainer_file, 'r') as f:
            content = f.read()
            # Extract just the "What is..." section as a brief explanation
            lines = content.split('\n')
            explanation_lines = []
            in_what_is = False

            for line in lines:
                if line.startswith('## What is'):
                    in_what_is = True
                    continue
                elif line.startswith('##'):
                    break
                elif in_what_is and line.strip():
                    explanation_lines.append(line.strip())

            explanation = ' '.join(explanation_lines)[:500]  # Limit to 500 chars
            return explanation if explanation else f"Learn about {skill_slug.replace('-', ' ')}"

    return f"Learn about {skill_slug.replace('-', ' ')}"


def seed_database():
    """Seed the database with skills from JSON file."""
    # Create tables
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created!")

    db = SessionLocal()

    try:
        # Check if already seeded
        existing_skills = db.query(Skill).count()
        if existing_skills > 0:
            print(f"Database already has {existing_skills} skills. Skipping seed.")
            return

        print("Loading skills from skills.json...")
        data = load_skills_json()

        print(f"Found {len(data['skills'])} skills to seed")
        print("Creating skills...")

        # Create skills first (without prerequisites)
        skill_objects = {}
        for skill_data in data['skills']:
            explanation = load_explainer(skill_data['slug'], skill_data['subject'])

            skill = Skill(
                slug=skill_data['slug'],
                name=skill_data['name'],
                subject=skill_data['subject'],
                description=skill_data['description'],
                khan_url=skill_data['khan_url'],
                explanation=explanation,
                difficulty_base=skill_data['difficulty_base'],
            )
            db.add(skill)
            skill_objects[skill_data['slug']] = {
                'object': skill,
                'prerequisites': skill_data.get('prerequisites', [])
            }

        db.commit()
        print(f"✅ Created {len(skill_objects)} skills!")

        # Refresh all skills to get their IDs
        for slug, data in skill_objects.items():
            db.refresh(data['object'])

        # Create prerequisites
        print("Creating skill prerequisites...")
        prereq_count = 0
        for slug, data in skill_objects.items():
            skill = data['object']
            for prereq_slug in data['prerequisites']:
                if prereq_slug in skill_objects:
                    prereq = SkillPrerequisite(
                        skill_id=skill.id,
                        prerequisite_id=skill_objects[prereq_slug]['object'].id,
                    )
                    db.add(prereq)
                    prereq_count += 1
                else:
                    print(f"⚠️  Warning: Prerequisite '{prereq_slug}' not found for skill '{slug}'")

        db.commit()
        print(f"✅ Created {prereq_count} prerequisites!")

        # Create question templates for skills with generators
        print("Creating question templates...")
        templates = []

        # Linear equation templates (solving-linear-equations)
        if 'solving-linear-equations' in skill_objects:
            linear_skill = skill_objects['solving-linear-equations']['object']
            for difficulty in [1, 2, 3]:
                templates.append(QuestionTemplate(
                    skill_id=linear_skill.id,
                    template_type="linear_equation",
                    template_data={"difficulty": difficulty},
                    difficulty=difficulty,
                ))

        # Fraction addition templates
        if 'fraction-addition' in skill_objects:
            fraction_skill = skill_objects['fraction-addition']['object']
            for difficulty in [1, 2, 3]:
                templates.append(QuestionTemplate(
                    skill_id=fraction_skill.id,
                    template_type="fraction_addition",
                    template_data={"difficulty": difficulty},
                    difficulty=difficulty,
                ))

        for template in templates:
            db.add(template)

        db.commit()
        print(f"✅ Created {len(templates)} question templates!")

        print("\n🎉 Database seeded successfully!")
        print(f"   - {db.query(Skill).count()} skills")
        print(f"   - {db.query(SkillPrerequisite).count()} prerequisites")
        print(f"   - {db.query(QuestionTemplate).count()} question templates")

        # Show skills by subject
        print("\n📚 Skills by subject:")
        for subject_name in ["Pre-Algebra", "Algebra Basics", "Algebra I", "Algebra II", "Trigonometry", "Precalculus"]:
            count = db.query(Skill).filter(Skill.subject == subject_name).count()
            if count > 0:
                print(f"   - {subject_name}: {count} skills")

    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
