"""Add missing question templates to database."""

from app.database import SessionLocal
from app.models import Skill, QuestionTemplate

def add_templates():
    """Add question templates for new generators."""
    db = SessionLocal()

    try:
        # Map skill slugs to generator types and difficulty ranges
        # All existing generators are mapped here
        skill_generator_map = {
            # Pre-Algebra
            'integers-operations': ('integers_operations', [1, 2, 3]),
            'absolute-value': ('absolute_value', [1, 2, 3]),
            'fraction-addition': ('fraction_addition', [1, 2, 3]),
            'fractions-multiplication': ('fractions_multiplication', [1, 2, 3]),
            'fractions-division': ('fractions_division', [1, 2, 3]),
            'decimals-operations': ('decimals_operations', [1, 2, 3]),
            'percentages': ('percentages', [1, 2, 3]),
            'ratios-proportions': ('ratios_proportions', [1, 2, 3]),
            'unit-conversions': ('unit_conversions', [1, 2, 3]),
            'simple-interest': ('simple_interest', [1, 2, 3]),
            'pythagorean-theorem': ('pythagorean_theorem', [1, 2, 3]),
            # Algebra Basics
            'order-of-operations': ('order_of_operations', [1, 2, 3]),
            'distributive-property': ('distributive_property', [1, 2, 3]),
            'evaluating-expressions': ('evaluating_expressions', [1, 2, 3]),
            'combining-like-terms': ('combining_like_terms', [1, 2, 3]),
            'solving-linear-equations': ('linear_equation', [1, 2, 3]),
            'equations-with-variables-both-sides': ('equations_variables_both_sides', [1, 2, 3]),
            # Algebra I
            'solving-inequalities': ('inequality', [1, 2, 3]),
            'graphing-linear-equations': ('graphing_linear_equations', [1, 2, 3]),
            'slope-intercept-form': ('slope_intercept', [1, 2, 3]),
            'point-slope-form': ('point_slope_form', [1, 2, 3]),
            'systems-of-equations': ('systems_equations', [1, 2, 3]),
            'solving-quadratic-equations': ('quadratic_equation', [1, 2, 3, 4, 5]),
            'factoring-quadratics': ('factoring_quadratics', [1, 2, 3]),
            'quadratic-formula': ('quadratic_formula', [1, 2, 3]),
            'exponent-rules': ('exponent_rules', [1, 2, 3]),
            'scientific-notation': ('scientific_notation', [1, 2, 3]),
            # Algebra II
            'polynomial-operations': ('polynomial_operations', [1, 2, 3]),
            'factoring-polynomials': ('factoring_polynomials', [1, 2, 3]),
            'rational-expressions': ('rational_expressions', [1, 2, 3]),
            'radical-expressions': ('radical_expressions', [1, 2, 3]),
            # Precalculus
            'function-composition': ('function_composition', [1, 2, 3]),
            'inverse-functions': ('inverse_functions', [1, 2, 3]),
            'piecewise-functions': ('piecewise_functions', [1, 2, 3]),
            'polynomial-long-division': ('polynomial_long_division', [1, 2, 3]),
            'rational-functions': ('rational_functions', [1, 2, 3]),
            'conic-sections': ('conic_sections', [1, 2, 3]),
            'parametric-equations': ('parametric_equations', [1, 2, 3]),
            'polar-coordinates': ('polar_coordinates', [1, 2, 3]),
            'vectors': ('vectors', [1, 2, 3]),
            'matrices': ('matrices', [1, 2, 3]),
            # Trigonometry
            'unit-circle-radians': ('unit_circle_radians', [1, 2, 3]),
            'sine-cosine-tangent': ('sine_cosine_tangent', [1, 2, 3]),
            'pythagorean-identities': ('pythagorean_identities', [1, 2, 3]),
            'graphing-trig-functions': ('graphing_trig_functions', [1, 2, 3]),
            'inverse-trig-functions': ('inverse_trig_functions', [1, 2, 3]),
            'law-of-sines': ('law_of_sines', [1, 2, 3]),
            'law-of-cosines': ('law_of_cosines', [1, 2, 3]),
            'trigonometric-equations': ('trigonometric_equations', [1, 2, 3]),
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
