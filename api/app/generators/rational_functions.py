"""Rational functions question generator."""

import random
from typing import Dict, Any

# Real-world applications of rational functions
RATIONAL_FUNCTION_CONTEXTS = [
    {
        "context": "Concentration of medicine: C(t) = 50t/(t²+1) (mg/liter over hours)",
        "domain": "pharmacology"
    },
    {
        "context": "Spread of rumors: P(t) = t/(t+2) (proportion of population at time t)",
        "domain": "sociology"
    },
    {
        "context": "Efficiency of solar panel: E(x) = (100x)/(x²+10) (efficiency vs hours of sun)",
        "domain": "engineering"
    },
    {
        "context": "Average cost per unit: C(x) = (500+2x)/x (total cost ÷ units produced)",
        "domain": "finance"
    },
    {
        "context": "Light intensity: I(d) = 1000/d² (lumens at distance d meters from source)",
        "domain": "physics"
    },
]


def generate_rational_functions(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a rational function analysis problem.

    Args:
        difficulty: 1 (vertical asymptote), 2 (horizontal asymptote), 3 (both asymptotes)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Find vertical asymptote of f(x) = 1/(x - a)
        a = random.randint(-5, 5)
        if a == 0:
            a = 1

        question = f"Find the vertical asymptote of $f(x) = \\frac{{1}}{{x {-a:+d}}}$."

        steps = [
            "A vertical asymptote occurs where the denominator equals zero.",
            "",
            f"Set the denominator equal to zero: $x {-a:+d} = 0$",
            "",
            f"Solve for $x$: $x = {a}$",
            "",
            f"The vertical asymptote is at $x = {a}$.",
            "",
            f"**Final Answer:** ${a}$"
        ]

        answer_numeric = a

    elif difficulty == 2:
        # Medium: Find horizontal asymptote
        # For f(x) = (ax + b)/(cx + d), horizontal asymptote is a/c
        a = random.randint(2, 6)
        b = random.randint(-5, 5)
        c = random.randint(2, 5)
        d = random.randint(-5, 5)

        h_asymptote = a / c
        # Round to 2 decimal places if not an integer
        if h_asymptote == int(h_asymptote):
            h_asymptote = int(h_asymptote)
            answer_numeric = h_asymptote
        else:
            answer_numeric = round(h_asymptote, 2)

        question = f"Find the horizontal asymptote of $f(x) = \\frac{{{a}x {b:+d}}}{{{c}x {d:+d}}}$."

        steps = [
            "For a rational function $\\frac{{ax + b}}{{cx + d}}$, the horizontal asymptote is found by comparing the degrees of numerator and denominator.",
            "",
            "Both numerator and denominator have degree 1.",
            "",
            "When degrees are equal, the horizontal asymptote is the ratio of leading coefficients:",
            f"$y = \\frac{{a}}{{c}} = \\frac{{{a}}}{{{c}}}$",
            "",
        ]

        if h_asymptote == int(h_asymptote):
            steps.append(f"$y = {int(h_asymptote)}$")
            steps.append("")
            steps.append(f"**Final Answer:** ${int(h_asymptote)}$")
        else:
            steps.append(f"$y = {answer_numeric}$")
            steps.append("")
            steps.append(f"**Final Answer:** ${answer_numeric}$")

    else:
        # Hard: Find both vertical and horizontal asymptotes
        # Ask for the sum of the asymptotes
        a = random.randint(-4, 4)
        if a == 0:
            a = 1

        num_coef = random.randint(2, 5)
        num_const = random.randint(-5, 5)
        denom_coef = random.randint(2, 4)

        v_asymptote = a
        h_asymptote = num_coef / denom_coef

        # Calculate sum
        asymptote_sum = v_asymptote + h_asymptote
        if asymptote_sum == int(asymptote_sum):
            asymptote_sum = int(asymptote_sum)

        answer_numeric = round(asymptote_sum, 2) if asymptote_sum != int(asymptote_sum) else asymptote_sum

        question = f"Find the vertical and horizontal asymptotes of $f(x) = \\frac{{{num_coef}x {num_const:+d}}}{{{denom_coef}(x {-a:+d})}}$. What is the sum of the vertical asymptote and horizontal asymptote values?"

        steps = [
            "**Step 1: Find the vertical asymptote**",
            "Set the denominator equal to zero:",
            f"${denom_coef}(x {-a:+d}) = 0$",
            f"$x {-a:+d} = 0$",
            f"$x = {a}$",
            f"Vertical asymptote: $x = {a}$",
            "",
            "**Step 2: Find the horizontal asymptote**",
            f"Rewrite as: $f(x) = \\frac{{{num_coef}x {num_const:+d}}}{{{denom_coef}x {-denom_coef*a:+d}}}$",
            "Both numerator and denominator have degree 1.",
            f"Horizontal asymptote: $y = \\frac{{{num_coef}}}{{{denom_coef}}}$",
        ]

        if h_asymptote == int(h_asymptote):
            h_asymptote = int(h_asymptote)
            steps.append(f"$y = {h_asymptote}$")
        else:
            h_asymptote = round(h_asymptote, 2)
            steps.append(f"$y = {h_asymptote}$")

        steps.extend([
            "",
            "**Step 3: Find the sum**",
            f"Sum $= {v_asymptote} + {h_asymptote} = {answer_numeric}$",
            "",
            f"**Final Answer:** ${answer_numeric}$"
        ])

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
