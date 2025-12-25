"""Factoring polynomials question generator."""

import random
from typing import Dict, Any
import math

# Word problems for polynomial factoring
POLYNOMIAL_WORD_PROBLEMS = [
    {
        "context": "Volume of a box with cut corners: V = 2x³ + 8x² (cubic inches)",
        "question": "Factor to find the base dimensions",
        "domain": "geometry"
    },
    {
        "context": "Growth model for bacteria: N(t) = 3t³ - 12t (population in thousands)",
        "question": "Factor to find when population changes",
        "domain": "biology"
    },
    {
        "context": "Profit function: P(x) = 4x³ - 16x (in thousands of dollars)",
        "question": "Factor to analyze profit at different production levels",
        "domain": "finance"
    },
    {
        "context": "Motion equation: s(t) = 5t³ - 20t (distance in meters)",
        "question": "Factor to find when object returns to starting position",
        "domain": "physics"
    },
]


def generate_factoring_polynomials(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a factoring polynomials problem.

    Args:
        difficulty: 1 (GCF), 2 (grouping), 3 (complex)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        return _generate_gcf_factoring()
    elif difficulty == 2:
        return _generate_grouping_factoring()
    else:
        return _generate_complex_factoring()


def _generate_gcf_factoring() -> Dict[str, Any]:
    """Generate a GCF factoring problem (e.g., 6x² + 9x)."""
    # Choose GCF
    gcf = random.choice([2, 3, 4, 5, 6])

    # Generate two terms with the GCF
    coeff1 = gcf * random.randint(1, 5)
    coeff2 = gcf * random.randint(1, 5)

    # Powers (first term has higher power)
    power1 = random.randint(2, 4)
    power2 = random.randint(1, power1 - 1)

    # Build the polynomial
    term1 = f"{coeff1}x^{{{power1}}}" if power1 > 1 else f"{coeff1}x"
    term2 = f"{coeff2}x^{{{power2}}}" if power2 > 1 else f"{coeff2}x"

    polynomial = f"{term1} + {term2}"

    # Calculate factored form
    factor1_coeff = coeff1 // gcf
    factor2_coeff = coeff2 // gcf
    factor_power = power2  # GCF includes x^(min power)

    gcf_term = f"{gcf}x^{{{factor_power}}}" if factor_power > 1 else f"{gcf}x"

    remaining_power1 = power1 - factor_power
    remaining_power2 = power2 - factor_power

    if remaining_power1 > 1:
        remaining_term1 = f"{factor1_coeff}x^{{{remaining_power1}}}"
    elif remaining_power1 == 1:
        remaining_term1 = f"{factor1_coeff}x"
    else:
        remaining_term1 = str(factor1_coeff)

    if remaining_power2 > 1:
        remaining_term2 = f"{factor2_coeff}x^{{{remaining_power2}}}"
    elif remaining_power2 == 1:
        remaining_term2 = f"{factor2_coeff}x"
    else:
        remaining_term2 = str(factor2_coeff)

    if remaining_term1 == "1":
        remaining_term1 = "1"
    if remaining_term2 == "1":
        remaining_expr = f"{remaining_term1} + 1"
    else:
        remaining_expr = f"{remaining_term1} + {remaining_term2}"

    answer = f"{gcf_term}({remaining_expr})"

    # Generate solution steps
    steps = [
        f"Start with the polynomial: ${polynomial}$",
        f"Find the GCF of the coefficients: $\\text{{GCF}}({coeff1}, {coeff2}) = {gcf}$",
        f"Find the GCF of the variable terms: $x^{{{factor_power}}}$ (lowest power)",
        f"Factor out ${gcf_term}$",
        f"${polynomial} = {gcf_term}({remaining_expr})$",
        f"**Final Answer:** ${answer}$"
    ]

    return {
        "question": f"Factor completely: ${polynomial}$",
        "answer": answer,
        "answer_numeric": None,  # No numeric answer for factoring
        "steps": steps,
        "difficulty": 1,
    }


def _generate_grouping_factoring() -> Dict[str, Any]:
    """Generate a factor by grouping problem (e.g., x³ + 2x² + 3x + 6)."""
    # Choose common factor for first two terms
    a = random.randint(1, 4)
    b = random.randint(1, 4)

    # Build polynomial: ax³ + bax² + cx + bc
    # This factors to: ax²(x + b) + c(x + b) = (ax² + c)(x + b)
    c = random.randint(2, 5)

    coeff1 = a
    coeff2 = a * b
    coeff3 = c
    coeff4 = b * c

    # Build the polynomial string
    terms = []
    if coeff1 == 1:
        terms.append("x^3")
    else:
        terms.append(f"{coeff1}x^3")

    if coeff2 == 1:
        terms.append("x^2")
    else:
        terms.append(f"{coeff2}x^2")

    if coeff3 == 1:
        terms.append("x")
    else:
        terms.append(f"{coeff3}x")

    terms.append(str(coeff4))

    polynomial = " + ".join(terms)

    # Build answer
    if a == 1:
        first_factor = f"x^2 + {c}"
    else:
        first_factor = f"{a}x^2 + {c}"

    second_factor = f"x + {b}"
    answer = f"({first_factor})({second_factor})"

    # Generate solution steps
    group1 = f"{terms[0]} + {terms[1]}"
    group2 = f"{terms[2]} + {terms[3]}"

    if a == 1:
        factor_group1 = f"x^2(x + {b})"
    else:
        factor_group1 = f"{a}x^2(x + {b})"

    factor_group2 = f"{c}(x + {b})"

    steps = [
        f"Start with the polynomial: ${polynomial}$",
        f"Group terms in pairs: $({group1}) + ({group2})$",
        f"Factor out GCF from first group: ${factor_group1}$",
        f"Factor out GCF from second group: ${factor_group2}$",
        f"Combine: ${factor_group1} + {factor_group2}$",
        f"Factor out common binomial $(x + {b})$",
        f"**Final Answer:** ${answer}$"
    ]

    return {
        "question": f"Factor by grouping: ${polynomial}$",
        "answer": answer,
        "answer_numeric": None,
        "steps": steps,
        "difficulty": 2,
    }


def _generate_complex_factoring() -> Dict[str, Any]:
    """Generate a complex factoring problem (e.g., 4x³ - 16x)."""
    # GCF with complete factoring
    gcf = random.choice([2, 3, 4])

    # Generate polynomial of form: gcf·x(x² - k²) = gcf·x(x-k)(x+k)
    k = random.randint(2, 5)
    k_squared = k * k

    # Coefficients
    coeff1 = gcf
    coeff2 = gcf * k_squared

    # Build polynomial: coeff1·x³ - coeff2·x
    term1 = f"{coeff1}x^3" if coeff1 > 1 else "x^3"
    term2 = f"{coeff2}x"

    polynomial = f"{term1} - {term2}"

    # Build answer: gcf·x(x - k)(x + k)
    gcf_term = f"{gcf}x" if gcf > 1 else "x"
    answer = f"{gcf_term}(x - {k})(x + {k})"

    # Alternative form for validation
    answer_alt = f"{gcf_term}(x + {k})(x - {k})"

    # Generate solution steps
    steps = [
        f"Start with the polynomial: ${polynomial}$",
        f"Factor out the GCF: ${gcf_term}$",
        f"${polynomial} = {gcf_term}(x^2 - {k_squared})$",
        f"Recognize difference of squares: $x^2 - {k_squared} = x^2 - {k}^2$",
        f"Factor using $a^2 - b^2 = (a-b)(a+b)$",
        f"$x^2 - {k}^2 = (x - {k})(x + {k})$",
        f"**Final Answer:** ${answer}$"
    ]

    return {
        "question": f"Factor completely: ${polynomial}$",
        "answer": answer,
        "answer_numeric": None,
        "steps": steps,
        "difficulty": 3,
    }
