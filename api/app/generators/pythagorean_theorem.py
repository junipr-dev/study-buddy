"""Pythagorean theorem question generator."""

import random
import math
from typing import Dict, Any


def generate_pythagorean_theorem(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a Pythagorean theorem problem: a² + b² = c²

    Args:
        difficulty: 1 (find hypotenuse), 2 (find leg), 3 (word problems)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Find hypotenuse with Pythagorean triples
        triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (6, 8, 10)]
        a, b, c = random.choice(triples)

        question = f"A right triangle has legs of length $a = {a}$ and $b = {b}$. Find the length of the hypotenuse $c$."

        steps = [
            "Use the Pythagorean theorem: $a^2 + b^2 = c^2$",
            f"Substitute the known values: ${a}^2 + {b}^2 = c^2$",
            f"Calculate: ${a**2} + {b**2} = c^2$",
            f"Add: ${a**2 + b**2} = c^2$",
            f"Take the square root of both sides: $c = \\sqrt{{{a**2 + b**2}}}$",
            f"Simplify: $c = {c}$",
            f"**Final Answer:** The hypotenuse is $c = {c}$ units"
        ]

        answer_numeric = c

    elif difficulty == 2:
        # Medium: Find a leg with Pythagorean triples
        triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (6, 8, 10)]
        a, b, c = random.choice(triples)

        # Randomly choose which leg to find
        if random.choice([True, False]):
            known_leg, unknown_leg = b, a
            unknown_var = "a"
            known_var = "b"
        else:
            known_leg, unknown_leg = a, b
            unknown_var = "b"
            known_var = "a"

        question = f"A right triangle has hypotenuse $c = {c}$ and one leg ${known_var} = {known_leg}$. Find the length of the other leg ${unknown_var}$."

        steps = [
            "Use the Pythagorean theorem: $a^2 + b^2 = c^2$",
            f"Substitute the known values: ${unknown_var}^2 + {known_leg}^2 = {c}^2$",
            f"Calculate: ${unknown_var}^2 + {known_leg**2} = {c**2}$",
            f"Simplify: ${unknown_var}^2 + {known_leg**2} = {c**2}$",
            f"Subtract ${known_leg**2}$ from both sides: ${unknown_var}^2 = {c**2 - known_leg**2}$",
            f"Take the square root: ${unknown_var} = \\sqrt{{{c**2 - known_leg**2}}}$",
            f"Simplify: ${unknown_var} = {unknown_leg}$",
            f"**Final Answer:** The missing leg is ${unknown_var} = {unknown_leg}$ units"
        ]

        answer_numeric = unknown_leg

    else:
        # Hard: Word problems
        problem_types = ["ladder", "diagonal", "distance"]
        problem_type = random.choice(problem_types)

        triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10)]
        a, b, c = random.choice(triples)

        if problem_type == "ladder":
            question = f"A {c}-foot ladder is leaning against a wall. The base of the ladder is {a} feet from the wall. How high up the wall does the ladder reach?"

            steps = [
                "This is a right triangle problem where:",
                f"- The ladder is the hypotenuse: $c = {c}$ feet",
                f"- The distance from the wall is one leg: $a = {a}$ feet",
                "- The height up the wall is the other leg: $b = ?$",
                "Use the Pythagorean theorem: $a^2 + b^2 = c^2$",
                f"Substitute: ${a}^2 + b^2 = {c}^2$",
                f"Calculate: ${a**2} + b^2 = {c**2}$",
                f"Subtract ${a**2}$ from both sides: $b^2 = {c**2 - a**2}$",
                f"Take the square root: $b = \\sqrt{{{c**2 - a**2}}}$",
                f"Simplify: $b = {b}$",
                f"**Final Answer:** The ladder reaches ${b}$ feet up the wall"
            ]
            answer_numeric = b

        elif problem_type == "diagonal":
            question = f"A rectangular park is {a} meters wide and {b} meters long. What is the diagonal distance across the park?"

            steps = [
                "The diagonal of a rectangle forms a right triangle where:",
                f"- Width is one leg: $a = {a}$ meters",
                f"- Length is the other leg: $b = {b}$ meters",
                "- Diagonal is the hypotenuse: $c = ?$",
                "Use the Pythagorean theorem: $a^2 + b^2 = c^2$",
                f"Substitute: ${a}^2 + {b}^2 = c^2$",
                f"Calculate: ${a**2} + {b**2} = c^2$",
                f"Add: ${a**2 + b**2} = c^2$",
                f"Take the square root: $c = \\sqrt{{{a**2 + b**2}}}$",
                f"Simplify: $c = {c}$",
                f"**Final Answer:** The diagonal distance is ${c}$ meters"
            ]
            answer_numeric = c

        else:  # distance
            question = f"A boat travels {a} miles east, then {b} miles north. How far is the boat from its starting point?"

            steps = [
                "This creates a right triangle where:",
                f"- East distance is one leg: $a = {a}$ miles",
                f"- North distance is the other leg: $b = {b}$ miles",
                "- Direct distance is the hypotenuse: $c = ?$",
                "Use the Pythagorean theorem: $a^2 + b^2 = c^2$",
                f"Substitute: ${a}^2 + {b}^2 = c^2$",
                f"Calculate: ${a**2} + {b**2} = c^2$",
                f"Add: ${a**2 + b**2} = c^2$",
                f"Take the square root: $c = \\sqrt{{{a**2 + b**2}}}$",
                f"Simplify: $c = {c}$",
                f"**Final Answer:** The boat is ${c}$ miles from the starting point"
            ]
            answer_numeric = c

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }


def validate_answer(user_answer: str, correct_answer: float, tolerance: float = 0.01) -> bool:
    """Validate user's answer against correct answer."""
    try:
        user_value = float(user_answer)
        return abs(user_value - correct_answer) < tolerance
    except ValueError:
        return False
