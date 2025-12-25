"""Inverse functions question generator."""

import random
from typing import Dict, Any

# Real-world applications of inverse functions
INVERSE_FUNCTION_CONTEXTS = [
    {
        "context": "Decryption: encode/decode messages using inverse cipher functions",
        "domain": "cryptography"
    },
    {
        "context": "Temperature conversion: F = 9C/5 + 32, find C given F (inverse)",
        "domain": "physics"
    },
    {
        "context": "Loan interest: compound interest forward, find principal inverse",
        "domain": "finance"
    },
    {
        "context": "Sound waves: frequency to wavelength and back (inverse relationship)",
        "domain": "acoustics"
    },
    {
        "context": "Medical imaging: CT scan reconstruction uses inverse transforms",
        "domain": "medicine"
    },
]


def generate_inverse_functions(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate an inverse function problem.

    Args:
        difficulty: 1 (linear inverses), 2 (verify inverses), 3 (composition verification)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Find inverse of linear function f(x) = ax + b
        a = random.choice([2, 3, 4, 5])
        b = random.randint(-5, 5)

        # Inverse: f^(-1)(x) = (x - b) / a
        # Evaluate at a specific point
        x_val = random.randint(1, 10)
        inverse_result = (x_val - b) / a

        # Check if result is integer
        if inverse_result == int(inverse_result):
            inverse_result = int(inverse_result)
            answer_numeric = inverse_result
        else:
            answer_numeric = round(inverse_result, 2)

        question = f"Given $f(x) = {a}x {b:+d}$, find the inverse function $f^{{-1}}(x)$ and evaluate $f^{{-1}}({x_val})$."

        steps = [
            "To find the inverse, replace $f(x)$ with $y$:",
            f"$y = {a}x {b:+d}$",
            "",
            "Swap $x$ and $y$:",
            f"$x = {a}y {b:+d}$",
            "",
            "Solve for $y$:",
            f"$x {-b:+d} = {a}y$",
            f"$y = \\frac{{x {-b:+d}}}{{{a}}}$",
            "",
            f"Therefore, $f^{{-1}}(x) = \\frac{{x {-b:+d}}}{{{a}}}$",
            "",
            f"Now evaluate $f^{{-1}}({x_val})$:",
            f"$f^{{-1}}({x_val}) = \\frac{{{x_val} {-b:+d}}}{{{a}}}$",
            f"$f^{{-1}}({x_val}) = \\frac{{{x_val - b}}}{{{a}}}$",
            f"$f^{{-1}}({x_val}) = {answer_numeric}$",
            "",
            f"**Final Answer:** ${answer_numeric}$"
        ]

    elif difficulty == 2:
        # Medium: Find inverse and verify with composition
        a = random.choice([2, 3, 4])
        b = random.randint(-4, 4)

        question = f"Find the inverse of $f(x) = {a}x {b:+d}$ and verify that $f(f^{{-1}}(x)) = x$ for $x = {a * 2 + b}$."

        # Pick x_val such that f^(-1)(x_val) is an integer
        x_val = a * 2 + b
        inverse_at_x = 2

        steps = [
            "**Step 1: Find the inverse function**",
            f"Start with $y = {a}x {b:+d}$",
            f"Swap $x$ and $y$: $x = {a}y {b:+d}$",
            f"Solve for $y$: $y = \\frac{{x {-b:+d}}}{{{a}}}$",
            f"So $f^{{-1}}(x) = \\frac{{x {-b:+d}}}{{{a}}}$",
            "",
            "**Step 2: Verify with composition**",
            f"Calculate $f^{{-1}}({x_val})$:",
            f"$f^{{-1}}({x_val}) = \\frac{{{x_val} {-b:+d}}}{{{a}}} = \\frac{{{x_val - b}}}{{{a}}} = {inverse_at_x}$",
            "",
            f"Now calculate $f(f^{{-1}}({x_val})) = f({inverse_at_x})$:",
            f"$f({inverse_at_x}) = {a}({inverse_at_x}) {b:+d}$",
            f"$f({inverse_at_x}) = {a * inverse_at_x} {b:+d}$",
            f"$f({inverse_at_x}) = {x_val}$",
            "",
            f"Since $f(f^{{-1}}({x_val})) = {x_val}$, the functions are inverses.",
            "",
            f"**Final Answer:** ${x_val}$"
        ]

        answer_numeric = x_val

    else:
        # Hard: Inverse of simple quadratic (restricted domain)
        # f(x) = x² + a for x ≥ 0, find f^(-1)(b) where b > a
        a = random.randint(1, 4)
        x_val = random.randint(2, 4)
        b = x_val ** 2 + a  # This ensures the answer is x_val

        question = f"Given $f(x) = x^2 + {a}$ for $x \\geq 0$, find $f^{{-1}}({b})$."

        steps = [
            "To find the inverse:",
            f"Start with $y = x^2 + {a}$",
            f"Swap variables: $x = y^2 + {a}$",
            f"Solve for $y$: $y^2 = x - {a}$",
            f"$y = \\sqrt{{x - {a}}}$ (positive root since $x \\geq 0$)",
            "",
            f"So $f^{{-1}}(x) = \\sqrt{{x - {a}}}$",
            "",
            f"Evaluate $f^{{-1}}({b})$:",
            f"$f^{{-1}}({b}) = \\sqrt{{{b} - {a}}}$",
            f"$f^{{-1}}({b}) = \\sqrt{{{b - a}}}$",
            f"$f^{{-1}}({b}) = {x_val}$",
            "",
            f"**Final Answer:** ${x_val}$"
        ]

        answer_numeric = x_val

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
