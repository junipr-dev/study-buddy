"""Law of Cosines question generator."""

import random
import math
from typing import Dict, Any


def generate_law_of_cosines(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate Law of Cosines problems.

    Args:
        difficulty: 1 (find side, SAS case), 2 (find angle, SSS case), 3 (word problems)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Find the third side given two sides and included angle (SAS)
        side_a = random.choice([8, 10, 12, 15])
        side_b = random.choice([10, 12, 15, 18])
        angle_C = random.choice([60, 90, 120])

        # Calculate side c using Law of Cosines: c² = a² + b² - 2ab*cos(C)
        cos_C = math.cos(math.radians(angle_C))
        side_c_squared = side_a**2 + side_b**2 - 2*side_a*side_b*cos_C
        side_c = math.sqrt(side_c_squared)

        question = f"In triangle $ABC$, side $a = {side_a}$, side $b = {side_b}$, and angle $C = {angle_C}°$. Find side $c$."

        steps = [
            "Use the Law of Cosines: $c^2 = a^2 + b^2 - 2ab\\cos(C)$",
            f"Substitute the known values:",
            f"$c^2 = {side_a}^2 + {side_b}^2 - 2({side_a})({side_b})\\cos({angle_C}°)$",
            f"Calculate each term:",
            f"$c^2 = {side_a**2} + {side_b**2} - {2*side_a*side_b}\\cos({angle_C}°)$",
            f"$\\cos({angle_C}°) = {round(cos_C, 4)}$",
            f"$c^2 = {side_a**2} + {side_b**2} - {2*side_a*side_b} \\cdot {round(cos_C, 4)}$",
            f"$c^2 = {side_a**2} + {side_b**2} - {round(2*side_a*side_b*cos_C, 2)}$",
            f"$c^2 = {round(side_c_squared, 2)}$",
            f"Take the square root: $c = \\sqrt{{{round(side_c_squared, 2)}}}$",
            f"$c \\approx {round(side_c, 2)}$",
            f"**Final Answer:** $c \\approx {round(side_c, 2)}$"
        ]

        answer_numeric = round(side_c, 2)

    elif difficulty == 2:
        # Medium: Find an angle given three sides (SSS)
        # Use a Pythagorean triple or near-triple for cleaner numbers
        triples = [
            (5, 12, 13),
            (8, 15, 17),
            (7, 24, 25),
            (6, 8, 10),
            (9, 12, 15)
        ]

        side_a, side_b, side_c = random.choice(triples)

        # Find angle C (opposite to side c) using Law of Cosines
        # cos(C) = (a² + b² - c²) / (2ab)
        cos_C = (side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)
        angle_C = math.degrees(math.acos(cos_C))

        question = f"In triangle $ABC$, side $a = {side_a}$, side $b = {side_b}$, and side $c = {side_c}$. Find angle $C$ (opposite to side $c$)."

        steps = [
            "Use the Law of Cosines to find the angle:",
            "$\\cos(C) = \\frac{a^2 + b^2 - c^2}{2ab}$",
            f"Substitute the known values:",
            f"$\\cos(C) = \\frac{{{side_a}^2 + {side_b}^2 - {side_c}^2}}{{2({side_a})({side_b})}}$",
            f"Calculate:",
            f"$\\cos(C) = \\frac{{{side_a**2} + {side_b**2} - {side_c**2}}}{{{2*side_a*side_b}}}$",
            f"$\\cos(C) = \\frac{{{side_a**2 + side_b**2 - side_c**2}}}{{{2*side_a*side_b}}}$",
            f"$\\cos(C) = {round(cos_C, 4)}$",
            f"Take the inverse cosine: $C = \\arccos({round(cos_C, 4)})$",
            f"$C \\approx {round(angle_C, 2)}°$",
            f"**Final Answer:** $C \\approx {round(angle_C, 2)}°$"
        ]

        answer_numeric = round(angle_C, 2)

    else:
        # Hard: Word problems involving Law of Cosines
        problem_types = ["navigation", "distance", "surveying"]
        problem_type = random.choice(problem_types)

        if problem_type == "navigation":
            # Boat or plane navigation problem
            dist1 = random.choice([100, 120, 150])
            dist2 = random.choice([80, 100, 120])
            angle = random.choice([60, 75, 90, 120])

            # Calculate direct distance using Law of Cosines
            cos_angle = math.cos(math.radians(angle))
            distance_squared = dist1**2 + dist2**2 - 2*dist1*dist2*cos_angle
            distance = math.sqrt(distance_squared)

            question = f"A plane flies ${dist1}$ km north, then turns and flies ${dist2}$ km in a direction ${angle}°$ from its original path. How far is the plane from its starting point?"

            steps = [
                "This forms a triangle where:",
                f"- First leg: ${dist1}$ km",
                f"- Second leg: ${dist2}$ km",
                f"- Angle between the two legs: ${angle}°$",
                "Use the Law of Cosines to find the direct distance $d$:",
                f"$d^2 = {dist1}^2 + {dist2}^2 - 2({dist1})({dist2})\\cos({angle}°)$",
                f"Calculate:",
                f"$d^2 = {dist1**2} + {dist2**2} - {2*dist1*dist2} \\cdot {round(cos_angle, 4)}$",
                f"$d^2 = {dist1**2} + {dist2**2} - {round(2*dist1*dist2*cos_angle, 2)}$",
                f"$d^2 = {round(distance_squared, 2)}$",
                f"$d = \\sqrt{{{round(distance_squared, 2)}}} \\approx {round(distance, 2)}$ km",
                f"**Final Answer:** ${round(distance, 2)}$ km"
            ]

            answer_numeric = round(distance, 2)

        elif problem_type == "distance":
            # Distance between two points problem
            dist_A = random.choice([40, 50, 60])
            dist_B = random.choice([30, 40, 50])
            angle = random.choice([45, 60, 90])

            cos_angle = math.cos(math.radians(angle))
            distance_squared = dist_A**2 + dist_B**2 - 2*dist_A*dist_B*cos_angle
            distance = math.sqrt(distance_squared)

            question = f"Two hikers start from the same point. One walks ${dist_A}$ meters in one direction, and the other walks ${dist_B}$ meters in a direction ${angle}°$ from the first. How far apart are they?"

            steps = [
                "This creates a triangle with:",
                f"- Side 1: ${dist_A}$ meters",
                f"- Side 2: ${dist_B}$ meters",
                f"- Included angle: ${angle}°$",
                "Use the Law of Cosines:",
                f"$d^2 = {dist_A}^2 + {dist_B}^2 - 2({dist_A})({dist_B})\\cos({angle}°)$",
                f"$d^2 = {dist_A**2} + {dist_B**2} - {2*dist_A*dist_B} \\cdot {round(cos_angle, 4)}$",
                f"$d^2 \\approx {round(distance_squared, 2)}$",
                f"$d \\approx {round(distance, 2)}$ meters",
                f"**Final Answer:** ${round(distance, 2)}$ meters"
            ]

            answer_numeric = round(distance, 2)

        else:  # surveying
            # Baseball diamond problem (or similar)
            side1 = 90  # feet (like a baseball diamond)
            side2 = 90
            angle = 90

            # For a square, diagonal = side * sqrt(2)
            distance = side1 * math.sqrt(2)

            question = f"A baseball diamond is a square with sides of ${side1}$ feet. What is the distance from home plate to second base (diagonally across)?"

            steps = [
                "This forms a right triangle (actually, an isosceles right triangle)",
                f"- Two sides: ${side1}$ feet each",
                f"- Included angle: ${angle}°$",
                "Use the Law of Cosines:",
                f"$d^2 = {side1}^2 + {side2}^2 - 2({side1})({side2})\\cos({angle}°)$",
                f"Since $\\cos(90°) = 0$:",
                f"$d^2 = {side1**2} + {side2**2} - 0$",
                f"$d^2 = {side1**2 + side2**2}$",
                f"$d = \\sqrt{{{side1**2 + side2**2}}} = {side1}\\sqrt{{2}} \\approx {round(distance, 2)}$ feet",
                f"**Final Answer:** ${round(distance, 2)}$ feet"
            ]

            answer_numeric = round(distance, 2)

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
