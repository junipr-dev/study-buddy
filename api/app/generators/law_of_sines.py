"""Law of Sines question generator."""

import random
import math
from typing import Dict, Any

# Real-world contexts for Law of Sines problems
WORD_PROBLEMS = [
    {
        "context": "Navigation and surveying: Finding distances between landmarks or waypoints.",
        "application": "Calculating distances in land surveying using angle measurements"
    },
    {
        "context": "Aviation: Flight path calculations and distance determinations.",
        "application": "Navigation between waypoints and distance calculations for flight planning"
    },
    {
        "context": "Rescue operations: Determining distances in search and rescue scenarios.",
        "application": "Calculating distances to locate missing persons or objects"
    },
    {
        "context": "Astronomy and celestial mechanics: Determining distances to celestial objects.",
        "application": "Parallax method for measuring astronomical distances"
    },
    {
        "context": "Construction and engineering: Layout and distance calculations for structures.",
        "application": "Calculating support structure dimensions and placements"
    },
]


def generate_law_of_sines(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate Law of Sines problems.

    Args:
        difficulty: 1 (find side, AAS case), 2 (find angle), 3 (ASA or ambiguous case)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Find a side using Law of Sines (AAS case)
        # Two angles and one side known
        use_word_problem = random.random() < 0.4
        angle_A = random.choice([30, 45, 60])
        angle_B = random.choice([30, 45, 60, 75])

        # Make sure angles sum to less than 180
        if angle_A + angle_B >= 180:
            angle_B = random.choice([30, 45])

        angle_C = 180 - angle_A - angle_B

        # Known side opposite to angle A
        side_a = random.choice([10, 12, 15, 20])

        # Calculate side b using Law of Sines
        side_b = side_a * math.sin(math.radians(angle_B)) / math.sin(math.radians(angle_A))

        if use_word_problem:
            question = f"**Land Surveying:** A surveyor measures two angles in a triangular land plot: angle $A = {angle_A}°$ and angle $B = {angle_B}°$. The distance along one side is $a = {side_a}$ meters. Find the length of side $b$ opposite to angle $B$."
        else:
            question = f"In triangle $ABC$, angle $A = {angle_A}°$, angle $B = {angle_B}°$, and side $a = {side_a}$. Find side $b$."

        steps = [
            f"**Step 1 - Recall the Law of Sines:**",
            f"This law states: $\\frac{{a}}{{\\sin(A)}} = \\frac{{b}}{{\\sin(B)}} = \\frac{{c}}{{\\sin(C)}}$",
            f"It relates sides and their opposite angles in ANY triangle.",
            "",
            f"**Step 2 - Identify what we know:**",
            f"- Angle $A = {angle_A}°$ (opposite to side $a$)",
            f"- Angle $B = {angle_B}°$ (opposite to side $b$, which we're finding)",
            f"- Side $a = {side_a}$ units",
            "",
            f"**Step 3 - Set up the equation using Law of Sines:**",
            f"$\\frac{{{side_a}}}{{\\sin({angle_A}°)}} = \\frac{{b}}{{\\sin({angle_B}°)}}$",
            "",
            f"**Step 4 - Solve for $b$ by multiplying both sides:**",
            f"$b = \\frac{{{side_a} \\cdot \\sin({angle_B}°)}}{{\\sin({angle_A}°)}}$",
            "",
            f"**Step 5 - Calculate using angle values:**",
            f"$\\sin({angle_A}°) \\approx {round(math.sin(math.radians(angle_A)), 4)}$",
            f"$\\sin({angle_B}°) \\approx {round(math.sin(math.radians(angle_B)), 4)}$",
            f"",
            f"$b = \\frac{{{side_a} \\times {round(math.sin(math.radians(angle_B)), 4)}}}{{{round(math.sin(math.radians(angle_A)), 4)}}} \\approx {round(side_b, 2)}$",
            "",
            f"**Final Answer:** $b \\approx {round(side_b, 2)}$ units"
        ]

        answer_numeric = round(side_b, 2)

    elif difficulty == 2:
        # Medium: Find an angle using Law of Sines
        angle_A = random.choice([30, 45, 60])
        side_a = random.choice([10, 12, 15])
        side_b = random.choice([8, 10, 12])

        # Make sure side_b < side_a to avoid ambiguous case for simplicity
        if side_b >= side_a:
            side_b = side_a - 3

        # Calculate angle B using Law of Sines
        sin_B = side_b * math.sin(math.radians(angle_A)) / side_a
        angle_B = math.degrees(math.asin(sin_B))

        question = f"In triangle $ABC$, angle $A = {angle_A}°$, side $a = {side_a}$, and side $b = {side_b}$. Find angle $B$."

        steps = [
            "Use the Law of Sines: $\\frac{a}{\\sin(A)} = \\frac{b}{\\sin(B)}$",
            f"We have: $A = {angle_A}°$, $a = {side_a}$, $b = {side_b}$",
            f"Set up the equation: $\\frac{{{side_a}}}{{\\sin({angle_A}°)}} = \\frac{{{side_b}}}{{\\sin(B)}}$",
            f"Solve for $\\sin(B)$: $\\sin(B) = \\frac{{{side_b} \\cdot \\sin({angle_A}°)}}{{{side_a}}}$",
            f"Calculate: $\\sin(B) = \\frac{{{side_b} \\cdot {round(math.sin(math.radians(angle_A)), 4)}}}{{{side_a}}}$",
            f"$\\sin(B) \\approx {round(sin_B, 4)}$",
            f"Take the inverse sine: $B = \\arcsin({round(sin_B, 4)})$",
            f"$B \\approx {round(angle_B, 2)}°$",
            f"**Final Answer:** $B \\approx {round(angle_B, 2)}°$"
        ]

        answer_numeric = round(angle_B, 2)

    else:
        # Hard: ASA case or word problem
        problem_type = random.choice(["ASA", "word_problem"])

        if problem_type == "ASA":
            # Two angles and the included side
            angle_A = random.choice([40, 50, 60])
            angle_C = random.choice([50, 60, 70])

            # Make sure angles sum to less than 180
            if angle_A + angle_C >= 150:
                angle_C = 60

            angle_B = 180 - angle_A - angle_C

            # Side between angles A and C (this is side b)
            side_b = random.choice([15, 18, 20, 25])

            # Find side a using Law of Sines
            side_a = side_b * math.sin(math.radians(angle_A)) / math.sin(math.radians(angle_B))

            question = f"In triangle $ABC$, angle $A = {angle_A}°$, angle $C = {angle_C}°$, and side $b = {side_b}$ (the side opposite to angle $B$). Find side $a$."

            steps = [
                f"First, find angle $B$: $B = 180° - A - C = 180° - {angle_A}° - {angle_C}° = {angle_B}°$",
                "Use the Law of Sines: $\\frac{a}{\\sin(A)} = \\frac{b}{\\sin(B)}$",
                f"Set up the equation: $\\frac{{a}}{{\\sin({angle_A}°)}} = \\frac{{{side_b}}}{{\\sin({angle_B}°)}}$",
                f"Solve for $a$: $a = \\frac{{{side_b} \\cdot \\sin({angle_A}°)}}{{\\sin({angle_B}°)}}$",
                f"Calculate: $a = \\frac{{{side_b} \\cdot {round(math.sin(math.radians(angle_A)), 4)}}}{{{round(math.sin(math.radians(angle_B)), 4)}}}$",
                f"$a \\approx {round(side_a, 2)}$",
                f"**Final Answer:** $a \\approx {round(side_a, 2)}$"
            ]

            answer_numeric = round(side_a, 2)

        else:  # word_problem
            # Surveying or navigation problem
            angle_A = 65
            angle_B = 48
            angle_C = 180 - angle_A - angle_B
            distance = 200  # meters

            # Distance is opposite to angle C, find distance opposite to angle A
            side_a = distance * math.sin(math.radians(angle_A)) / math.sin(math.radians(angle_C))

            question = f"A surveyor stands at point $C$ and measures angles to two landmarks $A$ and $B$. The angle at $A$ is ${angle_A}°$, the angle at $B$ is ${angle_B}°$, and the distance from $A$ to $B$ is ${distance}$ meters. How far is point $C$ from point $A$?"

            steps = [
                "First, find the angle at $C$:",
                f"$C = 180° - {angle_A}° - {angle_B}° = {angle_C}°$",
                f"The distance from $A$ to $B$ (side $c$) is ${distance}$ meters",
                "We need to find the distance from $C$ to $A$ (side $b$)",
                "Use the Law of Sines: $\\frac{b}{\\sin(B)} = \\frac{c}{\\sin(C)}$",
                f"Set up: $\\frac{{b}}{{\\sin({angle_B}°)}} = \\frac{{{distance}}}{{\\sin({angle_C}°)}}$",
                f"Solve for $b$: $b = \\frac{{{distance} \\cdot \\sin({angle_B}°)}}{{\\sin({angle_C}°)}}$",
                f"Calculate: $b \\approx {round(side_a, 2)}$ meters",
                f"**Final Answer:** ${round(side_a, 2)}$ meters"
            ]

            answer_numeric = round(side_a, 2)

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
