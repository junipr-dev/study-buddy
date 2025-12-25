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
            "We're using the Pythagorean theorem, which relates the sides of any right triangle: $a^2 + b^2 = c^2$",
            f"Let's plug in our known values: ${a}^2 + {b}^2 = c^2$",
            f"Now calculate the squares: ${a**2} + {b**2} = c^2$",
            f"Add the left side together: ${a**2 + b**2} = c^2$",
            f"To find $c$, take the square root of both sides: $c = \\sqrt{{{a**2 + b**2}}}$",
            f"Simplify to get: $c = {c}$",
            f"**Final Answer:** The hypotenuse measures $c = {c}$ units"
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
            "We have the hypotenuse and one leg, so we need to find the missing leg using the Pythagorean theorem: $a^2 + b^2 = c^2$",
            f"Substitute what we know: ${unknown_var}^2 + {known_leg}^2 = {c}^2$",
            f"Calculate the squares: ${unknown_var}^2 + {known_leg**2} = {c**2}$",
            f"To isolate ${unknown_var}^2$, subtract ${known_leg**2}$ from both sides: ${unknown_var}^2 = {c**2 - known_leg**2}$",
            f"Now take the square root of both sides: ${unknown_var} = \\sqrt{{{c**2 - known_leg**2}}}$",
            f"Simplify to get: ${unknown_var} = {unknown_leg}$",
            f"**Final Answer:** The missing leg is ${unknown_var} = {unknown_leg}$ units"
        ]

        answer_numeric = unknown_leg

    else:
        # Hard: Word problems with diverse real-world contexts
        use_word_problem = random.random() < 0.5

        if use_word_problem:
            # Real-world word problems with engaging contexts
            word_problems = [
                # Construction contexts
                {
                    "context": "construction_ladder",
                    "triples": [(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10)],
                    "scenario": "A construction worker places a 25-foot ladder against a building. The base of the ladder must be 7 feet away from the wall for safety. How high on the building will the ladder reach?",
                    "values": (7, 24, 25),
                    "setup": "- Ladder (hypotenuse): 25 feet\n- Distance from wall (leg): 7 feet\n- Height reached (leg): ?",
                    "solving_var": "height",
                    "answer_var": "h"
                },
                {
                    "context": "roof_pitch",
                    "scenario": "A roofer is installing shingles on a roof. The roof needs to span 12 meters across and rise 5 meters vertically. What is the length of the sloped roof that needs to be shingled?",
                    "values": (5, 12, 13),
                    "setup": "- Horizontal span (leg): 12 meters\n- Vertical rise (leg): 5 meters\n- Roof slope length (hypotenuse): ?",
                    "solving_var": "slope",
                    "answer_var": "s"
                },
                {
                    "context": "diagonal_measurement",
                    "scenario": "A carpenter is checking if a wall corner is square. He measures 6 feet along one wall and 8 feet along the other wall. The diagonal corner-to-corner should measure 10 feet if it's perfectly square. Is the wall square?",
                    "values": (6, 8, 10),
                    "setup": "- First wall length (leg): 6 feet\n- Second wall length (leg): 8 feet\n- Diagonal distance (hypotenuse): ?",
                    "solving_var": "diagonal",
                    "answer_var": "d"
                },

                # Sports contexts
                {
                    "context": "baseball_diamond",
                    "scenario": "In baseball, home plate to first base is 90 feet, and first base to second base is another 90 feet at a right angle. A baserunner wants to know the direct distance from home plate to second base. How far is that?",
                    "values": (3, 4, 5),
                    "scaled": 18,
                    "setup": "- Home to first base (leg): 90 feet\n- First to second base (leg): 90 feet\n- Home to second base directly (hypotenuse): ?",
                    "solving_var": "shortcut",
                    "answer_var": "d"
                },
                {
                    "context": "soccer_field",
                    "scenario": "A soccer player needs to run diagonally across a rectangular field that is 100 meters long and 60 meters wide. What distance must the player cover to run diagonally from one corner to the opposite corner?",
                    "values": (5, 12, 13),
                    "setup": "- Field length (leg): 100 meters\n- Field width (leg): 60 meters\n- Diagonal run (hypotenuse): ?",
                    "solving_var": "shortcut",
                    "answer_var": "d"
                },
                {
                    "context": "basketball_court",
                    "scenario": "A basketball player passes the ball diagonally across the court. The court is 94 feet long and 50 feet wide. Assuming the ball travels in a straight line, what distance does the ball travel across the diagonal?",
                    "values": (3, 4, 5),
                    "setup": "- Court length (leg): 94 feet\n- Court width (leg): 50 feet\n- Diagonal distance (hypotenuse): ?",
                    "solving_var": "pass",
                    "answer_var": "d"
                },

                # Navigation contexts
                {
                    "context": "navigation_distance",
                    "scenario": "A ship travels 9 nautical miles east, then 12 nautical miles north. Using GPS, how far is the ship from its starting point in a straight line?",
                    "values": (3, 4, 5),
                    "scaled": 3,
                    "setup": "- East distance (leg): 9 nautical miles\n- North distance (leg): 12 nautical miles\n- Direct distance (hypotenuse): ?",
                    "solving_var": "distance",
                    "answer_var": "d"
                },
                {
                    "context": "hiking_trail",
                    "scenario": "A hiker walks 5 miles north on a trail, then 12 miles east. She decides to cut directly back to the starting point. What distance does she need to walk to return directly?",
                    "values": (5, 12, 13),
                    "setup": "- North distance (leg): 5 miles\n- East distance (leg): 12 miles\n- Direct return path (hypotenuse): ?",
                    "solving_var": "shortcut",
                    "answer_var": "d"
                },

                # Architecture/Building contexts
                {
                    "context": "building_shadow",
                    "scenario": "A tall building casts a shadow 8 meters long on the ground. The distance from the top of the building to the end of the shadow (measured along a straight line) is 17 meters. How tall is the building?",
                    "values": (8, 15, 17),
                    "setup": "- Shadow length on ground (leg): 8 meters\n- Line from building top to shadow end (hypotenuse): 17 meters\n- Building height (leg): ?",
                    "solving_var": "height",
                    "answer_var": "h"
                },
                {
                    "context": "tower_height",
                    "scenario": "From a point 24 yards away from a cell tower, the straight-line distance to the top of the tower is 25 yards. What is the height of the tower?",
                    "values": (7, 24, 25),
                    "setup": "- Distance from tower base (leg): 24 yards\n- Line distance to tower top (hypotenuse): 25 yards\n- Tower height (leg): ?",
                    "solving_var": "height",
                    "answer_var": "h"
                },

                # Technology contexts
                {
                    "context": "screen_diagonal",
                    "scenario": "A computer monitor has a width of 15 inches and a height of 20 inches. Tech specs list screen size as the diagonal measurement. What is the diagonal size of this monitor?",
                    "values": (3, 4, 5),
                    "scaled": 5,
                    "setup": "- Screen width (leg): 15 inches\n- Screen height (leg): 20 inches\n- Diagonal (hypotenuse): ?",
                    "solving_var": "diagonal",
                    "answer_var": "d"
                },
                {
                    "context": "cable_length",
                    "scenario": "A cable needs to connect from the top of a building down to a ground junction box. The building is 15 meters tall and the junction box is 20 meters away from the base of the building. What length of cable is needed?",
                    "values": (3, 4, 5),
                    "scaled": 5,
                    "setup": "- Vertical distance (leg): 15 meters\n- Horizontal distance (leg): 20 meters\n- Cable length needed (hypotenuse): ?",
                    "solving_var": "cable",
                    "answer_var": "c"
                },
            ]

            problem = random.choice(word_problems)
            context = problem["context"]

            # Scale the values if specified
            if "scaled" in problem:
                scale = problem["scaled"]
                a, b, c = problem["values"][0] * scale, problem["values"][1] * scale, problem["values"][2] * scale
            else:
                a, b, c = problem["values"]

            question = problem["scenario"]

            # Build context-specific steps
            steps = [
                f"This is a real-world Pythagorean theorem problem. Let's identify the right triangle:\n{problem['setup']}",
                "We'll use the Pythagorean theorem: $a^2 + b^2 = c^2$",
            ]

            # Determine which value we're solving for based on context
            if "leg" in problem["setup"] and "?" in problem["setup"].split('\n')[-1]:
                # Solving for a leg
                if "height" in problem["setup"].split('\n')[-1].lower() or "?" in problem["setup"].split('\n')[-1]:
                    # Find the missing leg
                    steps.extend([
                        f"Substitute the known values: ${a}^2 + {problem['answer_var']}^2 = {c}^2$",
                        f"Calculate: ${a**2} + {problem['answer_var']}^2 = {c**2}$",
                        f"Subtract ${a**2}$ from both sides: ${problem['answer_var']}^2 = {c**2 - a**2}$",
                        f"Take the square root: ${problem['answer_var']} = \\sqrt{{{c**2 - a**2}}}$",
                        f"Simplify: ${problem['answer_var']} = {b}$",
                        f"**Final Answer:** The {problem['solving_var']} is {b} units"
                    ])
                    answer_numeric = b
            else:
                # Solving for hypotenuse
                steps.extend([
                    f"Substitute the known values: ${a}^2 + {b}^2 = {problem['answer_var']}^2$",
                    f"Calculate the squares: ${a**2} + {b**2} = {problem['answer_var']}^2$",
                    f"Add them up: ${a**2 + b**2} = {problem['answer_var']}^2$",
                    f"Take the square root: ${problem['answer_var']} = \\sqrt{{{a**2 + b**2}}}$",
                    f"Simplify: ${problem['answer_var']} = {c}$",
                    f"**Final Answer:** The {problem['solving_var']} is {c} units"
                ])
                answer_numeric = c

        else:
            # Traditional abstract problems (still 50% of the time)
            problem_types = ["ladder", "diagonal", "distance"]
            problem_type = random.choice(problem_types)

            triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10)]
            a, b, c = random.choice(triples)

            if problem_type == "ladder":
                question = f"A {c}-foot ladder is leaning against a wall. The base of the ladder is {a} feet from the wall. How high up the wall does the ladder reach?"

                steps = [
                    "This forms a right triangle where:",
                    f"- The ladder itself is the hypotenuse: $c = {c}$ feet",
                    f"- The distance from the wall is one leg: $a = {a}$ feet",
                    "- The height up the wall is the other leg: $b = ?$",
                    "Using the Pythagorean theorem: $a^2 + b^2 = c^2$",
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
                    "The diagonal of a rectangle creates a right triangle where:",
                    f"- The width is one leg: $a = {a}$ meters",
                    f"- The length is the other leg: $b = {b}$ meters",
                    "- The diagonal is the hypotenuse: $c = ?$",
                    "Using the Pythagorean theorem: $a^2 + b^2 = c^2$",
                    f"Substitute: ${a}^2 + {b}^2 = c^2$",
                    f"Calculate: ${a**2} + {b**2} = c^2$",
                    f"Add them up: ${a**2 + b**2} = c^2$",
                    f"Take the square root: $c = \\sqrt{{{a**2 + b**2}}}$",
                    f"Simplify: $c = {c}$",
                    f"**Final Answer:** The diagonal distance is ${c}$ meters"
                ]
                answer_numeric = c

            else:  # distance
                question = f"A boat travels {a} miles east, then {b} miles north. How far is the boat from its starting point?"

                steps = [
                    "The boat's path forms a right triangle where:",
                    f"- The eastward distance is one leg: $a = {a}$ miles",
                    f"- The northward distance is the other leg: $b = {b}$ miles",
                    "- The straight-line distance is the hypotenuse: $c = ?$",
                    "Using the Pythagorean theorem: $a^2 + b^2 = c^2$",
                    f"Substitute: ${a}^2 + {b}^2 = c^2$",
                    f"Calculate: ${a**2} + {b**2} = c^2$",
                    f"Add them up: ${a**2 + b**2} = c^2$",
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
