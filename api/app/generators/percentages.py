"""Percentages question generator."""

import random
from typing import Dict, Any


def generate_percentages(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a percentages problem.

    Args:
        difficulty:
            1 (easy - find percentage of a number)
            2 (medium - percentage increase/decrease)
            3 (hard - reverse percentage problems)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []

    if difficulty == 1:
        # Easy: What is X% of Y?
        percent = random.choice([10, 20, 25, 30, 40, 50, 60, 75, 80, 90])
        number = random.randint(20, 200)

        # Make sure result is reasonable
        if percent == 25:
            number = random.choice([20, 40, 60, 80, 100, 120, 140, 160, 180, 200])
        elif percent == 75:
            number = random.choice([20, 40, 60, 80, 100, 120, 140, 160, 180, 200])

        steps.append(f"What is ${percent}\\%$ of ${number}$?")
        steps.append("**Rule:** To find a percentage of a number, convert the percentage to a decimal and multiply")
        steps.append(f"**Step 1:** Convert ${percent}\\%$ to a decimal:")

        decimal = percent / 100
        steps.append(f"${percent}\\% = {percent} \\div 100 = {decimal}$")

        steps.append(f"**Step 2:** Multiply by ${number}$:")
        answer = (percent * number) / 100
        steps.append(f"${decimal} \\times {number} = {answer}$")

    elif difficulty == 2:
        # Medium: Percentage increase or decrease
        operation = random.choice(['increase', 'decrease'])
        original = random.randint(50, 500)
        percent = random.choice([10, 15, 20, 25, 30, 40, 50])

        if operation == 'increase':
            steps.append(f"Increase ${original}$ by ${percent}\\%$")
            steps.append("**Rule:** For percentage increase, find the percentage amount and add it to the original")

            steps.append(f"**Step 1:** Find ${percent}\\%$ of ${original}$:")
            decimal = percent / 100
            steps.append(f"${percent}\\% = {decimal}$")
            increase_amount = (percent * original) / 100
            steps.append(f"${decimal} \\times {original} = {increase_amount}$")

            steps.append(f"**Step 2:** Add the increase to the original:")
            answer = original + increase_amount
            steps.append(f"${original} + {increase_amount} = {answer}$")

            # Alternative method
            steps.append("**Alternative method:** Multiply by $(1 + {percent}\\%)$:")
            multiplier = 1 + (percent / 100)
            steps.append(f"${original} \\times {multiplier} = {answer}$")
        else:
            steps.append(f"Decrease ${original}$ by ${percent}\\%$")
            steps.append("**Rule:** For percentage decrease, find the percentage amount and subtract it from the original")

            steps.append(f"**Step 1:** Find ${percent}\\%$ of ${original}$:")
            decimal = percent / 100
            steps.append(f"${percent}\\% = {decimal}$")
            decrease_amount = (percent * original) / 100
            steps.append(f"${decimal} \\times {original} = {decrease_amount}$")

            steps.append(f"**Step 2:** Subtract the decrease from the original:")
            answer = original - decrease_amount
            steps.append(f"${original} - {decrease_amount} = {answer}$")

            # Alternative method
            steps.append("**Alternative method:** Multiply by $(1 - {percent}\\%)$:")
            multiplier = 1 - (percent / 100)
            steps.append(f"${original} \\times {multiplier} = {answer}$")

    else:  # difficulty == 3
        # Hard: Reverse percentage problems
        problem_type = random.choice(['what_percent', 'find_original'])

        if problem_type == 'what_percent':
            # What percent of X is Y?
            whole = random.randint(20, 100)
            percent = random.choice([10, 15, 20, 25, 30, 40, 50, 60, 75, 80])
            part = (percent * whole) / 100

            steps.append(f"What percent of ${whole}$ is ${part}$?")
            steps.append("**Rule:** To find what percent, divide the part by the whole and multiply by 100")

            steps.append(f"**Step 1:** Divide the part by the whole:")
            ratio = part / whole
            steps.append(f"$\\frac{{{part}}}{{{whole}}} = {ratio}$")

            steps.append(f"**Step 2:** Convert to percentage by multiplying by 100:")
            answer = ratio * 100
            steps.append(f"${ratio} \\times 100 = {answer}\\%$")

            answer_str = f"{int(answer)}%"
            steps.append(f"**Final Answer:** ${int(answer)}\\%$")

            return {
                "question": f"What percent of ${whole}$ is ${part}$?",
                "answer": answer_str,
                "steps": steps,
                "difficulty": difficulty,
            }
        else:
            # X is Y% of what number?
            percent = random.choice([10, 20, 25, 40, 50, 80])
            original = random.randint(50, 200)
            part = (percent * original) / 100

            steps.append(f"${part}$ is ${percent}\\%$ of what number?")
            steps.append("**Rule:** To find the whole when given a part and percentage, divide the part by the percentage (as a decimal)")

            steps.append(f"**Step 1:** Convert ${percent}\\%$ to a decimal:")
            decimal = percent / 100
            steps.append(f"${percent}\\% = {decimal}$")

            steps.append(f"**Step 2:** Divide the part by the decimal:")
            answer = part / decimal
            steps.append(f"$\\frac{{{part}}}{{{decimal}}} = {answer}$")

            # Verification
            steps.append(f"**Verification:** Check that ${percent}\\%$ of ${answer}$ equals ${part}$:")
            steps.append(f"${decimal} \\times {answer} = {part}$ ✓")

    # Convert answer to int if it's a whole number
    if answer == int(answer):
        answer = int(answer)

    steps.append(f"**Final Answer:** ${answer}$")

    return {
        "question": f"Calculate the percentage" if difficulty > 1 else f"What is ${percent}\\%$ of ${number}$?",
        "answer": str(answer),
        "answer_numeric": float(answer) if isinstance(answer, (int, float)) else answer,
        "steps": steps,
        "difficulty": difficulty,
    }
