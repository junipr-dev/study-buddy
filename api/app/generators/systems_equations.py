"""Systems of equations question generator with real-world contexts."""

import random
from fractions import Fraction
from typing import Dict, Any, Tuple

# Real-world contexts for systems of equations
SYSTEMS_CONTEXTS = [
    {"context": "tickets", "template": "Adult tickets cost ${a1} and child tickets cost ${b1}. {x_sol} adults and {y_sol} children spent ${c1} total. Verify this and find if {x2_adj} adults and {y2_adj} children would spend ${c2}.", "var1": "adults", "var2": "children"},
    {"context": "coins", "template": "You have nickels (5¢) and dimes (10¢). If you have {sum_coins} coins worth ${total_cents/100}, how many of each?", "var1": "nickels", "var2": "dimes"},
    {"context": "mixture", "template": "A store mixes nuts at ${a1}/lb with raisins at ${b1}/lb. They make a {sum_lbs}lb mix worth ${c1}. How much of each?", "var1": "lbs of nuts", "var2": "lbs of raisins"},
    {"context": "age", "template": "The sum of two ages is {age_sum}. In {years} years, one person will be twice as old as the other. What are their ages now?", "var1": "age1", "var2": "age2"},
]


def generate_system_of_equations(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a system of two linear equations in two variables.

    Args:
        difficulty:
            1 (easy - simple substitution, integer solutions)
            2 (medium - elimination or substitution, may have fraction solutions)
            3 (medium-hard - requires multiplication before elimination)
            4 (hard - larger coefficients, fraction solutions likely)
            5 (very hard - no solution or infinite solutions)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []

    # Special case: inconsistent or dependent systems
    if difficulty == 5 and random.random() < 0.3:
        return _generate_special_system(steps)

    # Choose solution first (working backwards)
    if difficulty == 1:
        x_sol = random.randint(-5, 5)
        y_sol = random.randint(-5, 5)
        coeff_range = (1, 5)
    elif difficulty == 2:
        x_sol = random.randint(-8, 8)
        y_sol = random.randint(-8, 8)
        coeff_range = (1, 6)
    elif difficulty == 3:
        x_sol = random.randint(-10, 10)
        y_sol = random.randint(-10, 10)
        coeff_range = (2, 8)
    else:  # difficulty >= 4
        x_sol = random.randint(-15, 15)
        y_sol = random.randint(-15, 15)
        coeff_range = (2, 12)

    # Generate two equations that have this solution
    # Equation 1: a₁x + b₁y = c₁
    a1 = random.randint(coeff_range[0], coeff_range[1])
    b1 = random.randint(coeff_range[0], coeff_range[1])
    c1 = a1 * x_sol + b1 * y_sol

    # Equation 2: a₂x + b₂y = c₂
    # Make sure not parallel (avoid a₂/a₁ = b₂/b₁)
    a2 = random.randint(coeff_range[0], coeff_range[1])
    b2 = random.randint(coeff_range[0], coeff_range[1])

    # Ensure not parallel
    max_attempts = 10
    attempts = 0
    while attempts < max_attempts and a1 * b2 == a2 * b1:
        a2 = random.randint(coeff_range[0], coeff_range[1])
        b2 = random.randint(coeff_range[0], coeff_range[1])
        attempts += 1

    c2 = a2 * x_sol + b2 * y_sol

    # Format equations
    eq1 = _format_linear_equation(a1, b1, c1, "x", "y")
    eq2 = _format_linear_equation(a2, b2, c2, "x", "y")

    question = f"Solve the system:\n\n${eq1}$\n\n${eq2}$"

    steps.append(f"Given system of equations:")
    steps.append(f"${eq1}$")
    steps.append(f"${eq2}$")

    # Choose solution method based on difficulty and coefficients
    if difficulty <= 2:
        method = "substitution"
    else:
        # For higher difficulties, prefer elimination
        method = "elimination"

    if method == "substitution":
        answer_str = _solve_by_substitution(a1, b1, c1, a2, b2, c2, x_sol, y_sol, steps)
    else:
        answer_str = _solve_by_elimination(a1, b1, c1, a2, b2, c2, x_sol, y_sol, steps)

    return {
        "question": question,
        "answer": answer_str,
        "steps": steps,
        "difficulty": difficulty,
    }


def _generate_special_system(steps: list) -> Dict[str, Any]:
    """Generate a system with no solution or infinite solutions."""

    if random.random() < 0.5:
        # No solution (parallel lines)
        a = random.randint(2, 6)
        b = random.randint(2, 6)
        c1 = random.randint(-10, 10)
        c2 = random.randint(-10, 10)

        # Make sure c1 ≠ c2
        while c1 == c2:
            c2 = random.randint(-10, 10)

        # Both equations have same coefficients but different constants
        eq1 = _format_linear_equation(a, b, c1, "x", "y")
        eq2 = _format_linear_equation(a, b, c2, "x", "y")

        question = f"Solve the system:\n\n${eq1}$\n\n${eq2}$"

        steps.append(f"Given system of equations:")
        steps.append(f"${eq1}$")
        steps.append(f"${eq2}$")
        steps.append("Notice that both equations have the same coefficients for $x$ and $y$")
        steps.append(f"The left sides are identical, but ${c1} \\neq {c2}$")
        steps.append("This means the lines are parallel and never intersect")
        steps.append("**Final Answer:** No solution (inconsistent system)")

        answer_str = "no solution"

    else:
        # Infinite solutions (same line)
        a = random.randint(2, 6)
        b = random.randint(2, 6)
        c = random.randint(-10, 10)

        # Second equation is just a multiple of the first
        multiplier = random.choice([2, 3, -1, -2])

        eq1 = _format_linear_equation(a, b, c, "x", "y")
        eq2 = _format_linear_equation(multiplier * a, multiplier * b, multiplier * c, "x", "y")

        question = f"Solve the system:\n\n${eq1}$\n\n${eq2}$"

        steps.append(f"Given system of equations:")
        steps.append(f"${eq1}$")
        steps.append(f"${eq2}$")
        steps.append(f"Notice that the second equation is just {multiplier} times the first equation")
        steps.append("Both equations represent the same line")
        steps.append("Every point on the line is a solution")
        steps.append("**Final Answer:** Infinite solutions (dependent system)")

        answer_str = "infinite solutions"

    return {
        "question": question,
        "answer": answer_str,
        "steps": steps,
        "difficulty": 5,
    }


def _format_linear_equation(a: int, b: int, c: int, var1: str, var2: str) -> str:
    """Format a linear equation as LaTeX."""
    terms = []

    # First term
    if a == 1:
        terms.append(var1)
    elif a == -1:
        terms.append(f"-{var1}")
    else:
        terms.append(f"{a}{var1}")

    # Second term
    if b != 0:
        if b == 1:
            terms.append(f"+ {var2}")
        elif b == -1:
            terms.append(f"- {var2}")
        elif b > 0:
            terms.append(f"+ {b}{var2}")
        else:
            terms.append(f"- {abs(b)}{var2}")

    equation = " ".join(terms) + f" = {c}"
    return equation


def _solve_by_substitution(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int,
                           x_sol: int, y_sol: int, steps: list) -> str:
    """Solve system using substitution method."""

    steps.append("**Method: Substitution**")
    steps.append(f"Solve the first equation for $x$:")

    # Solve equation 1 for x: x = (c1 - b1*y) / a1
    steps.append(f"${a1}x = {c1} - {b1}y$")

    if a1 == 1:
        steps.append(f"$x = {c1} - {b1}y$")
        expr = f"{c1} - {b1}y"
    else:
        steps.append(f"$x = \\frac{{{c1} - {b1}y}}{{{a1}}}$")
        expr = f"\\frac{{{c1} - {b1}y}}{{{a1}}}"

    steps.append(f"Substitute into the second equation:")
    steps.append(f"${a2}({expr}) + {b2}y = {c2}$")

    # Solve for y
    # a2(c1 - b1*y)/a1 + b2*y = c2
    # a2*c1/a1 - a2*b1*y/a1 + b2*y = c2
    # y(b2 - a2*b1/a1) = c2 - a2*c1/a1

    steps.append("Simplify and solve for $y$:")

    # Calculate y
    if y_sol == int(y_sol):
        steps.append(f"$y = {int(y_sol)}$")
    else:
        steps.append(f"$y = {y_sol:.2f}$")

    steps.append(f"Substitute $y = {int(y_sol) if y_sol == int(y_sol) else f'{y_sol:.2f}'}$ back into the first equation:")

    # Calculate x
    if x_sol == int(x_sol):
        steps.append(f"$x = {int(x_sol)}$")
    else:
        steps.append(f"$x = {x_sol:.2f}$")

    # Format answer
    if x_sol == int(x_sol) and y_sol == int(y_sol):
        steps.append(f"**Final Answer:** $x = {int(x_sol)}, y = {int(y_sol)}$")
        answer_str = f"({int(x_sol)}, {int(y_sol)})"
    else:
        steps.append(f"**Final Answer:** $x = {x_sol:.2f}, y = {y_sol:.2f}$")
        answer_str = f"({x_sol:.2f}, {y_sol:.2f})"

    return answer_str


def _solve_by_elimination(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int,
                          x_sol: int, y_sol: int, steps: list) -> str:
    """Solve system using elimination method."""

    steps.append("**Method: Elimination**")

    # Decide which variable to eliminate
    # Check if we can eliminate directly or need to multiply
    eliminate_x = True  # Default to eliminating x

    # Check if coefficients are already opposites or equal
    if a1 == -a2:
        steps.append("The coefficients of $x$ are opposites, so add the equations:")
        mult1, mult2 = 1, 1
    elif a1 == a2:
        steps.append("The coefficients of $x$ are equal, so subtract the equations:")
        mult1, mult2 = 1, -1
    elif b1 == -b2:
        steps.append("The coefficients of $y$ are opposites, so add the equations:")
        eliminate_x = False
        mult1, mult2 = 1, 1
    elif b1 == b2:
        steps.append("The coefficients of $y$ are equal, so subtract the equations:")
        eliminate_x = False
        mult1, mult2 = 1, -1
    else:
        # Need to multiply to make coefficients match
        if eliminate_x:
            mult1 = a2
            mult2 = -a1
            steps.append(f"Multiply the first equation by ${a2}$ and the second by ${-a1}$ to eliminate $x$:")
        else:
            mult1 = b2
            mult2 = -b1
            steps.append(f"Multiply the first equation by ${b2}$ and the second by ${-b1}$ to eliminate $y$:")

    # Show multiplied equations if needed
    if abs(mult1) > 1 or abs(mult2) > 1:
        new_a1, new_b1, new_c1 = mult1 * a1, mult1 * b1, mult1 * c1
        new_a2, new_b2, new_c2 = mult2 * a2, mult2 * b2, mult2 * c2

        eq1_mult = _format_linear_equation(new_a1, new_b1, new_c1, "x", "y")
        eq2_mult = _format_linear_equation(new_a2, new_b2, new_c2, "x", "y")

        steps.append(f"${eq1_mult}$")
        steps.append(f"${eq2_mult}$")
    else:
        new_a1, new_b1, new_c1 = a1, b1, c1
        new_a2, new_b2, new_c2 = mult2 * a2, mult2 * b2, mult2 * c2

    # Add equations
    steps.append("Add the equations:")
    result_a = new_a1 + new_a2
    result_b = new_b1 + new_b2
    result_c = new_c1 + new_c2

    if result_a == 0:
        # Eliminated x
        steps.append(f"${result_b}y = {result_c}$")
        if y_sol == int(y_sol):
            steps.append(f"$y = {int(y_sol)}$")
        else:
            steps.append(f"$y = {y_sol:.2f}$")

        steps.append(f"Substitute $y = {int(y_sol) if y_sol == int(y_sol) else f'{y_sol:.2f}'}$ into the first equation:")
        if x_sol == int(x_sol):
            steps.append(f"$x = {int(x_sol)}$")
        else:
            steps.append(f"$x = {x_sol:.2f}$")
    else:
        # Eliminated y
        steps.append(f"${result_a}x = {result_c}$")
        if x_sol == int(x_sol):
            steps.append(f"$x = {int(x_sol)}$")
        else:
            steps.append(f"$x = {x_sol:.2f}$")

        steps.append(f"Substitute $x = {int(x_sol) if x_sol == int(x_sol) else f'{x_sol:.2f}'}$ into the first equation:")
        if y_sol == int(y_sol):
            steps.append(f"$y = {int(y_sol)}$")
        else:
            steps.append(f"$y = {y_sol:.2f}$")

    # Format answer
    if x_sol == int(x_sol) and y_sol == int(y_sol):
        steps.append(f"**Final Answer:** $x = {int(x_sol)}, y = {int(y_sol)}$")
        answer_str = f"({int(x_sol)}, {int(y_sol)})"
    else:
        steps.append(f"**Final Answer:** $x = {x_sol:.2f}, y = {y_sol:.2f}$")
        answer_str = f"({x_sol:.2f}, {y_sol:.2f})"

    return answer_str
