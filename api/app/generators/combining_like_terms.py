"""Combining like terms question generator with real-world contexts."""

import random
from typing import Dict, Any, List

# Real-world contexts for combining like terms
LIKE_TERMS_CONTEXTS = [
    {"context": "inventory", "template": "A store has {c1} boxes of item X, receives {c2} more, then {action} {c3}. Write the simplified inventory.", "vars": ["boxes"]},
    {"context": "points", "template": "In a game, you score {c1}x points, then {c2}x points, then lose {c3}x points. What's your total score expression?", "vars": ["x"]},
    {"context": "money", "template": "You have {c1} dollar bills, your friend gives you {c2} more, you spend {c3}. How many do you have?", "vars": ["bills"]},
]


def generate_combining_like_terms(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a combining like terms problem.

    Args:
        difficulty:
            1 (easy - two or three like terms)
            2 (medium - mix of like and unlike terms)
            3 (hard - multiple variables and complex expressions)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []

    if difficulty == 1:
        # Easy: Simple like terms (e.g., 3x + 5x or 2y + 7y - 3y)
        coef1 = random.randint(1, 8)
        coef2 = random.randint(1, 8)

        variable = random.choice(['x', 'y', 'a', 'b'])

        if random.choice([True, False]):
            # Two terms
            expression = f"{coef1}{variable} + {coef2}{variable}"
            steps.append(f"Start with the expression: ${coef1}{variable} + {coef2}{variable}$")
            steps.append(f"**Rule:** Like terms have the same variable and can be combined")
            steps.append(f"Both terms have the variable ${variable}$, so they are like terms")
            steps.append(f"Add the coefficients: ${coef1} + {coef2} = {coef1 + coef2}$")

            answer_coef = coef1 + coef2
            answer_str = f"{answer_coef}{variable}"
            steps.append(f"Keep the variable: ${answer_str}$")
        else:
            # Three terms
            coef3 = random.randint(1, 5)
            expression = f"{coef1}{variable} + {coef2}{variable} - {coef3}{variable}"
            steps.append(f"Start with the expression: ${coef1}{variable} + {coef2}{variable} - {coef3}{variable}$")
            steps.append(f"**Rule:** Like terms have the same variable and can be combined")
            steps.append(f"All terms have the variable ${variable}$, so they are like terms")
            steps.append(f"Combine the coefficients: ${coef1} + {coef2} - {coef3} = {coef1 + coef2 - coef3}$")

            answer_coef = coef1 + coef2 - coef3
            answer_str = f"{answer_coef}{variable}"
            steps.append(f"Keep the variable: ${answer_str}$")

    elif difficulty == 2:
        # Medium: Mix of like and unlike terms
        # Format: ax + b + cx + d or ax + by + cx + dy
        a = random.randint(1, 7)
        b = random.randint(1, 10)
        c = random.randint(1, 7)
        d = random.randint(1, 10)

        if random.choice([True, False]):
            # Same variable with constants: ax + b + cx + d
            expression = f"{a}x + {b} + {c}x + {d}"
            steps.append(f"Start with the expression: ${a}x + {b} + {c}x + {d}$")
            steps.append("**Rule:** Group and combine like terms")
            steps.append(f"Identify like terms:")
            steps.append(f"- Terms with $x$: ${a}x$ and ${c}x$")
            steps.append(f"- Constant terms: ${b}$ and ${d}$")

            x_coef = a + c
            const = b + d

            steps.append(f"Combine $x$ terms: ${a}x + {c}x = {x_coef}x$")
            steps.append(f"Combine constants: ${b} + {d} = {const}$")

            answer_str = f"{x_coef}x + {const}"
            steps.append(f"Write the simplified expression: ${answer_str}$")
        else:
            # Two different variables: ax + by + cx - dy
            b_sign = random.choice(['+', '-'])
            d_val = random.randint(1, 6)

            if b_sign == '+':
                expression = f"{a}x + {b}y + {c}x + {d}y"
                steps.append(f"Start with the expression: ${a}x + {b}y + {c}x + {d}y$")
                steps.append("**Rule:** Group and combine like terms")
                steps.append(f"Identify like terms:")
                steps.append(f"- Terms with $x$: ${a}x$ and ${c}x$")
                steps.append(f"- Terms with $y$: ${b}y$ and ${d}y$")

                x_coef = a + c
                y_coef = b + d

                steps.append(f"Combine $x$ terms: ${a}x + {c}x = {x_coef}x$")
                steps.append(f"Combine $y$ terms: ${b}y + {d}y = {y_coef}y$")

                answer_str = f"{x_coef}x + {y_coef}y"
            else:
                expression = f"{a}x + {b}y + {c}x - {d_val}y"
                steps.append(f"Start with the expression: ${a}x + {b}y + {c}x - {d_val}y$")
                steps.append("**Rule:** Group and combine like terms")
                steps.append(f"Identify like terms:")
                steps.append(f"- Terms with $x$: ${a}x$ and ${c}x$")
                steps.append(f"- Terms with $y$: ${b}y$ and ${-d_val}y$")

                x_coef = a + c
                y_coef = b - d_val

                steps.append(f"Combine $x$ terms: ${a}x + {c}x = {x_coef}x$")
                steps.append(f"Combine $y$ terms: ${b}y - {d_val}y = {y_coef}y$")

                if y_coef >= 0:
                    answer_str = f"{x_coef}x + {y_coef}y"
                else:
                    answer_str = f"{x_coef}x - {abs(y_coef)}y"

            steps.append(f"Write the simplified expression: ${answer_str}$")

    else:  # difficulty == 3
        # Hard: Multiple variables with squared terms
        # Format: ax^2 + bx + cx^2 + dx + e
        a = random.randint(1, 5)
        b = random.randint(2, 8)
        c = random.randint(1, 5)
        d = random.randint(1, 8)
        e = random.randint(1, 12)

        # Randomly add or subtract some terms
        sign1 = random.choice(['+', '-'])
        sign2 = random.choice(['+', '-'])

        if sign1 == '+' and sign2 == '+':
            expression = f"{a}x^2 + {b}x + {c}x^2 + {d}x + {e}"
            x2_coef = a + c
            x_coef = b + d
        elif sign1 == '+' and sign2 == '-':
            expression = f"{a}x^2 + {b}x + {c}x^2 - {d}x + {e}"
            x2_coef = a + c
            x_coef = b - d
        elif sign1 == '-' and sign2 == '+':
            expression = f"{a}x^2 + {b}x - {c}x^2 + {d}x + {e}"
            x2_coef = a - c
            x_coef = b + d
        else:
            expression = f"{a}x^2 + {b}x - {c}x^2 - {d}x + {e}"
            x2_coef = a - c
            x_coef = b - d

        steps.append(f"Start with the expression: ${expression}$")
        steps.append("**Rule:** Group and combine like terms")
        steps.append(f"Identify like terms:")
        steps.append(f"- Terms with $x^2$: ${a}x^2$ and {sign1} ${c}x^2$")
        steps.append(f"- Terms with $x$: ${b}x$ and {sign2} ${d}x$")
        steps.append(f"- Constant term: ${e}$")

        if sign1 == '+':
            steps.append(f"Combine $x^2$ terms: ${a}x^2 + {c}x^2 = {x2_coef}x^2$")
        else:
            steps.append(f"Combine $x^2$ terms: ${a}x^2 - {c}x^2 = {x2_coef}x^2$")

        if sign2 == '+':
            steps.append(f"Combine $x$ terms: ${b}x + {d}x = {x_coef}x$")
        else:
            steps.append(f"Combine $x$ terms: ${b}x - {d}x = {x_coef}x$")

        steps.append(f"The constant term remains: ${e}$")

        # Build answer string
        if x2_coef != 0 and x_coef >= 0:
            answer_str = f"{x2_coef}x^2 + {x_coef}x + {e}"
        elif x2_coef != 0 and x_coef < 0:
            answer_str = f"{x2_coef}x^2 - {abs(x_coef)}x + {e}"
        elif x2_coef == 0 and x_coef >= 0:
            answer_str = f"{x_coef}x + {e}"
        else:
            answer_str = f"{abs(x_coef)}x + {e}"

        steps.append(f"Write the simplified expression: ${answer_str}$")

    steps.append(f"**Final Answer:** ${answer_str}$")

    return {
        "question": f"Simplify by combining like terms: ${expression}$",
        "answer": answer_str,
        "steps": steps,
        "difficulty": difficulty,
    }
