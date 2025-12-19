"""Polynomial operations question generator."""

import random
from typing import Dict, Any, List, Tuple


def generate_polynomial_operation(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate polynomial addition, subtraction, or multiplication problems.

    Args:
        difficulty:
            1 (easy - add/subtract simple polynomials)
            2 (medium - add/subtract with more terms)
            3 (medium-hard - multiply binomials)
            4 (hard - multiply polynomial by binomial)
            5 (very hard - multiply two polynomials)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []

    if difficulty <= 2:
        # Addition or subtraction
        operation = random.choice(["add", "subtract"])
        poly1, poly1_str = _generate_polynomial(difficulty, max_degree=2)
        poly2, poly2_str = _generate_polynomial(difficulty, max_degree=2)

        if operation == "add":
            question = f"Add: $({poly1_str}) + ({poly2_str})$"
            steps.append(f"Add the polynomials: $({poly1_str}) + ({poly2_str})$")
            steps.append("Combine like terms by adding coefficients of the same power:")
            result = _add_polynomials(poly1, poly2)
        else:
            question = f"Subtract: $({poly1_str}) - ({poly2_str})$"
            steps.append(f"Subtract the polynomials: $({poly1_str}) - ({poly2_str})$")
            steps.append("Combine like terms by subtracting coefficients of the same power:")
            result = _subtract_polynomials(poly1, poly2)

        answer_str = _polynomial_to_string(result)

        # Show combining like terms
        _show_combining_steps(poly1, poly2, result, steps, operation)

        steps.append(f"**Final Answer:** ${answer_str}$")

    else:
        # Multiplication
        if difficulty == 3:
            # Multiply two binomials (ax + b)(cx + d)
            poly1, poly1_str = _generate_polynomial(1, max_degree=1, min_terms=2, max_terms=2)
            poly2, poly2_str = _generate_polynomial(1, max_degree=1, min_terms=2, max_terms=2)
            method = "FOIL"
        elif difficulty == 4:
            # Multiply binomial by trinomial
            poly1, poly1_str = _generate_polynomial(1, max_degree=1, min_terms=2, max_terms=2)
            poly2, poly2_str = _generate_polynomial(2, max_degree=2)
            method = "distributive"
        else:
            # Multiply two larger polynomials
            poly1, poly1_str = _generate_polynomial(2, max_degree=2)
            poly2, poly2_str = _generate_polynomial(2, max_degree=2)
            method = "distributive"

        question = f"Multiply: $({poly1_str})({poly2_str})$"
        steps.append(f"Multiply the polynomials: $({poly1_str})({poly2_str})$")

        if method == "FOIL":
            steps.append("Use FOIL (First, Outer, Inner, Last):")
            result, foil_steps = _multiply_polynomials_foil(poly1, poly2)
            steps.extend(foil_steps)
        else:
            steps.append("Use the distributive property:")
            result, dist_steps = _multiply_polynomials(poly1, poly2)
            steps.extend(dist_steps)

        answer_str = _polynomial_to_string(result)
        steps.append(f"**Final Answer:** ${answer_str}$")

    return {
        "question": question,
        "answer": answer_str,
        "steps": steps,
        "difficulty": difficulty,
    }


def _generate_polynomial(difficulty: int, max_degree: int = 2,
                        min_terms: int = 2, max_terms: int = 3) -> Tuple[Dict[int, int], str]:
    """
    Generate a random polynomial.

    Returns:
        (coefficients_dict, latex_string)
        coefficients_dict maps degree -> coefficient
    """
    poly = {}

    if difficulty == 1:
        coeff_range = (-5, 5)
    else:
        coeff_range = (-10, 10)

    # Decide number of terms
    num_terms = random.randint(min_terms, min(max_terms, max_degree + 1))

    # Generate terms
    degrees = random.sample(range(0, max_degree + 1), num_terms)

    for degree in degrees:
        coeff = random.randint(coeff_range[0], coeff_range[1])
        while coeff == 0:
            coeff = random.randint(coeff_range[0], coeff_range[1])
        poly[degree] = coeff

    poly_str = _polynomial_to_string(poly)
    return poly, poly_str


def _polynomial_to_string(poly: Dict[int, int]) -> str:
    """Convert polynomial dict to LaTeX string."""
    if not poly:
        return "0"

    # Sort by degree (descending)
    terms = []
    for degree in sorted(poly.keys(), reverse=True):
        coeff = poly[degree]

        if coeff == 0:
            continue

        # Format term
        if degree == 0:
            # Constant term
            term = str(abs(coeff))
        elif degree == 1:
            # Linear term
            if abs(coeff) == 1:
                term = "x"
            else:
                term = f"{abs(coeff)}x"
        else:
            # Higher degree term
            if abs(coeff) == 1:
                term = f"x^{degree}"
            else:
                term = f"{abs(coeff)}x^{degree}"

        # Add sign
        if not terms:  # First term
            if coeff < 0:
                term = "-" + term
        else:  # Subsequent terms
            if coeff > 0:
                term = "+ " + term
            else:
                term = "- " + term

        terms.append(term)

    return " ".join(terms) if terms else "0"


def _add_polynomials(poly1: Dict[int, int], poly2: Dict[int, int]) -> Dict[int, int]:
    """Add two polynomials."""
    result = poly1.copy()

    for degree, coeff in poly2.items():
        result[degree] = result.get(degree, 0) + coeff

    # Remove zero coefficients
    result = {d: c for d, c in result.items() if c != 0}

    return result


def _subtract_polynomials(poly1: Dict[int, int], poly2: Dict[int, int]) -> Dict[int, int]:
    """Subtract poly2 from poly1."""
    result = poly1.copy()

    for degree, coeff in poly2.items():
        result[degree] = result.get(degree, 0) - coeff

    # Remove zero coefficients
    result = {d: c for d, c in result.items() if c != 0}

    return result


def _multiply_polynomials(poly1: Dict[int, int], poly2: Dict[int, int]) -> Tuple[Dict[int, int], List[str]]:
    """Multiply two polynomials using distributive property."""
    steps = []
    result = {}

    # Multiply each term in poly1 by each term in poly2
    products = []

    for deg1, coeff1 in sorted(poly1.items(), reverse=True):
        for deg2, coeff2 in sorted(poly2.items(), reverse=True):
            new_degree = deg1 + deg2
            new_coeff = coeff1 * coeff2

            # Add to result
            result[new_degree] = result.get(new_degree, 0) + new_coeff

            # Track for showing work
            term1 = _format_single_term(coeff1, deg1)
            term2 = _format_single_term(coeff2, deg2)
            product_term = _format_single_term(new_coeff, new_degree)
            products.append(f"{term1} \\cdot {term2} = {product_term}")

    # Show multiplication steps
    steps.append("Multiply each term in the first polynomial by each term in the second:")
    for product in products:
        steps.append(f"${product}$")

    # Combine like terms
    steps.append("Combine like terms:")

    # Remove zero coefficients
    result = {d: c for d, c in result.items() if c != 0}

    return result, steps


def _multiply_polynomials_foil(poly1: Dict[int, int], poly2: Dict[int, int]) -> Tuple[Dict[int, int], List[str]]:
    """Multiply two binomials using FOIL method."""
    steps = []

    # Extract terms (assuming binomials)
    terms1 = sorted(poly1.items(), reverse=True)
    terms2 = sorted(poly2.items(), reverse=True)

    if len(terms1) != 2 or len(terms2) != 2:
        # Fall back to regular multiplication
        return _multiply_polynomials(poly1, poly2)

    (deg1_1, coeff1_1), (deg1_2, coeff1_2) = terms1
    (deg2_1, coeff2_1), (deg2_2, coeff2_2) = terms2

    # First
    first_deg = deg1_1 + deg2_1
    first_coeff = coeff1_1 * coeff2_1
    first_term = _format_single_term(first_coeff, first_deg)
    steps.append(f"**First:** {_format_single_term(coeff1_1, deg1_1)} \\cdot {_format_single_term(coeff2_1, deg2_1)} = {first_term}")

    # Outer
    outer_deg = deg1_1 + deg2_2
    outer_coeff = coeff1_1 * coeff2_2
    outer_term = _format_single_term(outer_coeff, outer_deg)
    steps.append(f"**Outer:** {_format_single_term(coeff1_1, deg1_1)} \\cdot {_format_single_term(coeff2_2, deg2_2)} = {outer_term}")

    # Inner
    inner_deg = deg1_2 + deg2_1
    inner_coeff = coeff1_2 * coeff2_1
    inner_term = _format_single_term(inner_coeff, inner_deg)
    steps.append(f"**Inner:** {_format_single_term(coeff1_2, deg1_2)} \\cdot {_format_single_term(coeff2_1, deg2_1)} = {inner_term}")

    # Last
    last_deg = deg1_2 + deg2_2
    last_coeff = coeff1_2 * coeff2_2
    last_term = _format_single_term(last_coeff, last_deg)
    steps.append(f"**Last:** {_format_single_term(coeff1_2, deg1_2)} \\cdot {_format_single_term(coeff2_2, deg2_2)} = {last_term}")

    # Combine
    result = {}
    result[first_deg] = result.get(first_deg, 0) + first_coeff
    result[outer_deg] = result.get(outer_deg, 0) + outer_coeff
    result[inner_deg] = result.get(inner_deg, 0) + inner_coeff
    result[last_deg] = result.get(last_deg, 0) + last_coeff

    steps.append(f"Add the terms: ${first_term} + {outer_term} + {inner_term} + {last_term}$")

    # Simplify if needed
    if outer_deg == inner_deg and (outer_coeff + inner_coeff) != 0:
        combined = outer_coeff + inner_coeff
        steps.append(f"Combine middle terms: ${outer_term} + {inner_term} = {_format_single_term(combined, outer_deg)}$")

    # Remove zero coefficients
    result = {d: c for d, c in result.items() if c != 0}

    return result, steps


def _format_single_term(coeff: int, degree: int) -> str:
    """Format a single term for display."""
    if degree == 0:
        return str(coeff)
    elif degree == 1:
        if coeff == 1:
            return "x"
        elif coeff == -1:
            return "-x"
        else:
            return f"{coeff}x"
    else:
        if coeff == 1:
            return f"x^{degree}"
        elif coeff == -1:
            return f"-x^{degree}"
        else:
            return f"{coeff}x^{degree}"


def _show_combining_steps(poly1: Dict[int, int], poly2: Dict[int, int],
                          result: Dict[int, int], steps: List[str], operation: str) -> None:
    """Show step-by-step combining of like terms."""

    # Get all unique degrees
    all_degrees = sorted(set(poly1.keys()) | set(poly2.keys()), reverse=True)

    for degree in all_degrees:
        coeff1 = poly1.get(degree, 0)
        coeff2 = poly2.get(degree, 0)
        result_coeff = result.get(degree, 0)

        if degree == 0:
            var_str = ""
        elif degree == 1:
            var_str = "x"
        else:
            var_str = f"x^{degree}"

        if operation == "add":
            if coeff1 != 0 and coeff2 != 0:
                steps.append(f"${var_str}$ terms: ${coeff1} + {coeff2} = {result_coeff}$")
        else:
            if coeff1 != 0 or coeff2 != 0:
                steps.append(f"${var_str}$ terms: ${coeff1} - {coeff2} = {result_coeff}$")
