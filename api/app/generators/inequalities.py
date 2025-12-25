"""Linear inequalities question generator with real-world contexts."""

import random
from typing import Dict, Any

# Real-world contexts for inequalities
INEQUALITY_CONTEXTS = {
    "<": [
        {"template": "A roller coaster requires riders to be under {c} inches tall. If the height requirement is {a}x + {b} ≤ limit, what values of x work?", "context": "height"},
        {"template": "You need to spend less than ${c} on lunch. If each item costs ${a}, what's the maximum you can buy?", "context": "budget"},
    ],
    ">": [
        {"template": "You need at least ${c} in your account. If you save ${a} per week plus ${b} starting bonus, how many weeks minimum?", "context": "savings"},
        {"template": "A game requires more than {c} points to level up. If you earn {a} points per quest, how many quests minimum?", "context": "gaming"},
    ],
    ">=": [
        {"template": "You need at least a {c}% to pass. If the grade formula is {a}x + {b}, what's the minimum x?", "context": "grades"},
        {"template": "A pizza party needs at least {c} slices. If each pizza has {a} slices, how many pizzas minimum?", "context": "pizza"},
    ],
    "<=": [
        {"template": "Your data plan allows at most {c} GB. If you use {a} GB per day, how many days can you go?", "context": "data"},
        {"template": "A bag can hold at most {c} lbs. If each book weighs {a} lbs, how many can you carry?", "context": "weight"},
    ],
}


def generate_inequality(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a linear inequality problem: ax + b < c (or >, ≤, ≥).

    Args:
        difficulty:
            1 (easy - simple inequalities, positive coefficients)
            2 (medium - includes negative coefficients)
            3 (hard - requires flipping inequality sign)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []

    # Choose inequality symbol
    symbols = ['<', '>', '\\leq', '\\geq']
    symbol = random.choice(symbols)

    # Map LaTeX symbols to text for answer
    symbol_text = {
        '<': '<',
        '>': '>',
        '\\leq': '≤',
        '\\geq': '≥'
    }

    if difficulty == 1:
        # Easy: Positive coefficients, simple operations
        a = random.randint(2, 8)
        b = random.randint(1, 15)
        x_solution = random.randint(1, 12)
        c = a * x_solution + b

        equation = f"{a}x + {b} {symbol} {c}"
        steps.append(f"Solve the inequality: ${equation}$")
        steps.append("**Rule:** Solve inequalities like equations, keeping the inequality sign")

        # Subtract b from both sides
        steps.append(f"Subtract ${b}$ from both sides:")
        new_c = c - b
        steps.append(f"${a}x {symbol} {new_c}$")

        # Divide by a
        steps.append(f"Divide both sides by ${a}$:")
        steps.append(f"$x {symbol} \\frac{{{new_c}}}{{{a}}}$")

        if new_c % a == 0:
            solution = new_c // a
            steps.append(f"Simplify: $x {symbol} {solution}$")
            answer_str = f"x {symbol_text[symbol]} {solution}"
        else:
            solution = new_c / a
            steps.append(f"Simplify: $x {symbol} {solution:.2f}$")
            answer_str = f"x {symbol_text[symbol]} {solution:.2f}"

    elif difficulty == 2:
        # Medium: May include negative b
        a = random.randint(2, 10)
        b = random.randint(-20, 20)
        x_solution = random.randint(-10, 10)
        c = a * x_solution + b

        # Format equation properly
        if b >= 0:
            equation = f"{a}x + {b} {symbol} {c}"
        else:
            equation = f"{a}x - {abs(b)} {symbol} {c}"

        steps.append(f"Solve the inequality: ${equation}$")
        steps.append("**Rule:** Solve inequalities like equations, maintaining the inequality sign")

        # Isolate variable term
        if b != 0:
            operation = f"subtract ${abs(b)}$" if b > 0 else f"add ${abs(b)}$"
            steps.append(f"To isolate the variable term, {operation} from both sides:")
            new_c = c - b
            steps.append(f"${a}x {symbol} {new_c}$")
        else:
            new_c = c

        # Divide by a
        steps.append(f"Divide both sides by ${a}$:")
        steps.append(f"$x {symbol} \\frac{{{new_c}}}{{{a}}}$")

        if new_c % a == 0:
            solution = new_c // a
            steps.append(f"Simplify: $x {symbol} {solution}$")
            answer_str = f"x {symbol_text[symbol]} {solution}"
        else:
            solution = new_c / a
            steps.append(f"Simplify: $x {symbol} {solution:.2f}$")
            answer_str = f"x {symbol_text[symbol]} {solution:.2f}"

    else:  # difficulty == 3
        # Hard: Negative coefficient requires flipping the inequality
        a = random.randint(-10, -2)
        b = random.randint(-15, 15)
        x_solution = random.randint(-8, 8)
        c = a * x_solution + b

        # Format equation
        if a == -1:
            a_str = "-x"
        else:
            a_str = f"{a}x"

        if b >= 0:
            equation = f"{a_str} + {b} {symbol} {c}"
        else:
            equation = f"{a_str} - {abs(b)} {symbol} {c}"

        steps.append(f"Solve the inequality: ${equation}$")
        steps.append("**Rule:** When dividing by a negative number, flip the inequality sign")

        # Isolate variable term
        if b != 0:
            operation = f"subtract ${abs(b)}$" if b > 0 else f"add ${abs(b)}$"
            steps.append(f"First, {operation} from both sides:")
            new_c = c - b
            if a == -1:
                steps.append(f"$-x {symbol} {new_c}$")
            else:
                steps.append(f"${a}x {symbol} {new_c}$")
        else:
            new_c = c

        # Divide by negative a (flip inequality)
        steps.append(f"Divide both sides by ${a}$ (negative number):")
        steps.append("⚠️ **IMPORTANT:** Flip the inequality sign when dividing by a negative")

        # Flip the symbol
        flipped_symbol = {
            '<': '>',
            '>': '<',
            '\\leq': '\\geq',
            '\\geq': '\\leq'
        }
        new_symbol = flipped_symbol[symbol]

        steps.append(f"$x {new_symbol} \\frac{{{new_c}}}{{{a}}}$")

        if new_c % a == 0:
            solution = new_c // a
            steps.append(f"Simplify: $x {new_symbol} {solution}$")
            answer_str = f"x {symbol_text[new_symbol]} {solution}"
        else:
            solution = new_c / a
            steps.append(f"Simplify: $x {new_symbol} {solution:.2f}$")
            answer_str = f"x {symbol_text[new_symbol]} {solution:.2f}"

    steps.append(f"**Final Answer:** ${answer_str}$")

    return {
        "question": f"Solve the inequality: ${equation}$",
        "answer": answer_str,
        "steps": steps,
        "difficulty": difficulty,
    }
