"""Seed script to populate initial skills and question templates."""

from app.database import SessionLocal
from app.models import Skill, QuestionTemplate, SkillPrerequisite

def seed_database():
    """Seed the database with initial skills and templates."""
    db = SessionLocal()

    try:
        # Check if already seeded
        existing_skills = db.query(Skill).count()
        if existing_skills > 0:
            print(f"Database already has {existing_skills} skills. Skipping seed.")
            return

        print("Seeding database with initial skills and templates...")

        # Create Pre-Algebra skills
        order_of_operations = Skill(
            slug="order-of-operations",
            name="Order of Operations",
            subject="Pre-Algebra",
            description="Apply PEMDAS/BODMAS to evaluate expressions",
            khan_url="https://www.khanacademy.org/math/pre-algebra/pre-algebra-arith-prop/pre-algebra-order-of-operations/v/introduction-to-order-of-operations",
            explanation="Order of operations (PEMDAS) tells us the correct sequence: Parentheses, Exponents, Multiplication/Division (left to right), Addition/Subtraction (left to right).",
            difficulty_base=1,
        )
        db.add(order_of_operations)

        fraction_addition = Skill(
            slug="fraction-addition",
            name="Adding Fractions",
            subject="Pre-Algebra",
            description="Add and subtract fractions with different denominators",
            khan_url="https://www.khanacademy.org/math/pre-algebra/pre-algebra-fractions/pre-algebra-add-sub-fractions/v/adding-fractions-with-unlike-denominators",
            explanation="To add fractions: 1) Find common denominator (LCD), 2) Convert fractions, 3) Add numerators, 4) Simplify if needed.",
            difficulty_base=2,
        )
        db.add(fraction_addition)

        # Create Algebra Basics skills
        combining_like_terms = Skill(
            slug="combining-like-terms",
            name="Combining Like Terms",
            subject="Algebra Basics",
            description="Simplify expressions by combining like terms",
            khan_url="https://www.khanacademy.org/math/algebra-basics/alg-basics-algebraic-expressions/alg-basics-combining-like-terms/v/combining-like-terms",
            explanation="Like terms have the same variable and exponent. Combine by adding/subtracting their coefficients. Example: 3x + 5x = 8x",
            difficulty_base=1,
        )
        db.add(combining_like_terms)

        solving_linear = Skill(
            slug="solving-linear-equations",
            name="Solving Linear Equations",
            subject="Algebra Basics",
            description="Solve equations of the form ax + b = c",
            khan_url="https://www.khanacademy.org/math/algebra-basics/alg-basics-algebraic-expressions/alg-basics-one-step-equations/v/why-we-do-the-same-thing-to-both-sides-one-step-equations",
            explanation="To solve linear equations: 1) Isolate the variable term, 2) Use inverse operations, 3) Always do the same operation to both sides.",
            difficulty_base=2,
        )
        db.add(solving_linear)

        # Create Algebra I skills
        multi_step_equations = Skill(
            slug="multi-step-equations",
            name="Multi-Step Equations",
            subject="Algebra I",
            description="Solve equations requiring multiple steps",
            khan_url="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:solve-equations/x2f8bb11595b61c86:multi-step-equations/v/multi-step-equations",
            explanation="Multi-step equations require combining like terms, using distributive property, and isolating the variable through multiple operations.",
            difficulty_base=3,
        )
        db.add(multi_step_equations)

        db.commit()
        print("Skills created successfully!")

        # Get skill IDs
        db.refresh(order_of_operations)
        db.refresh(fraction_addition)
        db.refresh(combining_like_terms)
        db.refresh(solving_linear)
        db.refresh(multi_step_equations)

        # Create skill prerequisites
        # Solving linear equations requires combining like terms
        prereq1 = SkillPrerequisite(
            skill_id=solving_linear.id,
            prerequisite_id=combining_like_terms.id,
        )
        db.add(prereq1)

        # Multi-step equations require solving linear equations
        prereq2 = SkillPrerequisite(
            skill_id=multi_step_equations.id,
            prerequisite_id=solving_linear.id,
        )
        db.add(prereq2)

        # Multi-step equations require combining like terms
        prereq3 = SkillPrerequisite(
            skill_id=multi_step_equations.id,
            prerequisite_id=combining_like_terms.id,
        )
        db.add(prereq3)

        db.commit()
        print("Prerequisites created successfully!")

        # Create question templates
        templates = [
            # Linear equation templates
            QuestionTemplate(
                skill_id=solving_linear.id,
                template_type="linear_equation",
                template_data={"difficulty": 1},
                difficulty=1,
            ),
            QuestionTemplate(
                skill_id=solving_linear.id,
                template_type="linear_equation",
                template_data={"difficulty": 2},
                difficulty=2,
            ),
            QuestionTemplate(
                skill_id=solving_linear.id,
                template_type="linear_equation",
                template_data={"difficulty": 3},
                difficulty=3,
            ),
            # Fraction templates
            QuestionTemplate(
                skill_id=fraction_addition.id,
                template_type="fraction_addition",
                template_data={"difficulty": 1},
                difficulty=1,
            ),
            QuestionTemplate(
                skill_id=fraction_addition.id,
                template_type="fraction_addition",
                template_data={"difficulty": 2},
                difficulty=2,
            ),
            QuestionTemplate(
                skill_id=fraction_addition.id,
                template_type="fraction_addition",
                template_data={"difficulty": 3},
                difficulty=3,
            ),
        ]

        for template in templates:
            db.add(template)

        db.commit()
        print(f"Created {len(templates)} question templates successfully!")

        print("\n✅ Database seeded successfully!")
        print(f"   - {db.query(Skill).count()} skills")
        print(f"   - {db.query(SkillPrerequisite).count()} prerequisites")
        print(f"   - {db.query(QuestionTemplate).count()} question templates")

    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
