"""Add missing question templates to database."""

from app.database import SessionLocal
from app.models import Skill, QuestionTemplate

def add_templates():
    """Add question templates for new generators."""
    db = SessionLocal()

    try:
        # Map skill slugs to generator types and difficulty ranges
        skill_generator_map = {
            'solving-linear-equations': ('linear_equation', [1, 2, 3]),
            'fraction-addition': ('fraction_addition', [1, 2, 3]),
            'order-of-operations': ('order_of_operations', [1, 2, 3]),
            'distributive-property': ('distributive_property', [1, 2, 3]),
            'combining-like-terms': ('combining_like_terms', [1, 2, 3]),
            'evaluating-expressions': ('evaluating_expressions', [1, 2, 3]),
            'solving-inequalities': ('inequality', [1, 2, 3]),
            'exponent-rules': ('exponent_rules', [1, 2, 3]),
            'slope-intercept-form': ('slope_intercept', [1, 2, 3]),
            'integers-operations': ('integers_operations', [1, 2, 3]),
            'absolute-value': ('absolute_value', [1, 2, 3]),
            'fractions-multiplication': ('fractions_multiplication', [1, 2, 3]),
            'fractions-division': ('fractions_division', [1, 2, 3]),
            'percentages': ('percentages', [1, 2, 3]),
            'decimals-operations': ('decimals_operations', [1, 2, 3]),
            'ratios-proportions': ('ratios_proportions', [1, 2, 3]),
            'unit-conversions': ('unit_conversions', [1, 2, 3]),
            'simple-interest': ('simple_interest', [1, 2, 3]),
            'pythagorean-theorem': ('pythagorean_theorem', [1, 2, 3]),
            'factoring-quadratics': ('factoring_quadratics', [1, 2, 3]),
            'factoring-polynomials': ('factoring_polynomials', [1, 2, 3]),
        }

        templates_added = 0

        for skill_slug, (generator_type, difficulties) in skill_generator_map.items():
            skill = db.query(Skill).filter(Skill.slug == skill_slug).first()
            if not skill:
                print(f"⚠️  Skill '{skill_slug}' not found")
                continue

            for difficulty in difficulties:
                # Check if template already exists
                existing = db.query(QuestionTemplate).filter(
                    QuestionTemplate.skill_id == skill.id,
                    QuestionTemplate.template_type == generator_type,
                    QuestionTemplate.difficulty == difficulty,
                ).first()

                if not existing:
                    template = QuestionTemplate(
                        skill_id=skill.id,
                        template_type=generator_type,
                        template_data={"difficulty": difficulty},
                        difficulty=difficulty,
                    )
                    db.add(template)
                    templates_added += 1

        db.commit()
        print(f"✅ Added {templates_added} new question templates!")
        print(f"   Total templates in database: {db.query(QuestionTemplate).count()}")

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    add_templates()
