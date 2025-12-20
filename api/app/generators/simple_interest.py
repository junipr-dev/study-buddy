"""Simple interest question generator (I = PRT)."""

import random
from typing import Dict, Any, List


def generate_simple_interest(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a simple interest problem using I = PRT.

    Args:
        difficulty: 1 (find interest), 2 (find P or R), 3 (find T or word problems)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps: List[str] = []

    if difficulty == 1:
        # Find interest: I = PRT
        principal = random.randint(5, 50) * 100  # 500-5000 in increments of 100
        rate = random.choice([3, 4, 5, 6, 7, 8])  # percentage
        time = random.randint(2, 10)  # years

        interest = (principal * rate * time) / 100

        question = (
            f"Calculate the simple interest on ${principal} "
            f"at {rate}% per year for {time} years."
        )

        steps.append("Use the simple interest formula: $I = PRT$")
        steps.append("Where:")
        steps.append(f"- P = ${principal} (principal)")
        steps.append(f"- R = {rate}% = {rate/100} (rate as decimal)")
        steps.append(f"- T = {time} years (time)")
        steps.append("Substitute values:")
        steps.append(f"$I = {principal} \\times {rate/100} \\times {time}$")
        steps.append(f"$I = {principal * rate * time / 100}$")
        steps.append(f"**Final Answer:** ${interest:.2f}")

        answer = interest

    elif difficulty == 2:
        # Find principal or rate
        find_what = random.choice(["principal", "rate"])

        if find_what == "principal":
            # Find P: P = I / (RT)
            interest = random.randint(1, 8) * 100  # 100-800 in increments of 100
            rate = random.choice([4, 5, 6, 8, 10])
            time = random.randint(2, 5)

            principal = (interest * 100) / (rate * time)

            question = (
                f"What principal will earn ${interest} simple interest "
                f"at {rate}% per year for {time} years?"
            )

            steps.append("Use the simple interest formula: $I = PRT$")
            steps.append("Solve for P: $P = \\frac{I}{RT}$")
            steps.append(f"Given: I = ${interest}, R = {rate}% = {rate/100}, T = {time} years")
            steps.append("Substitute values:")
            steps.append(f"$P = \\frac{{{interest}}}{{{rate/100} \\times {time}}}$")
            steps.append(f"$P = \\frac{{{interest}}}{{{rate * time / 100}}}$")
            steps.append(f"**Final Answer:** ${principal:.2f}")

            answer = principal

        else:
            # Find R: R = I / (PT)
            principal = random.randint(5, 30) * 100  # 500-3000 in increments of 100
            time = random.randint(2, 6)
            rate = random.choice([4, 5, 6, 8])

            interest = (principal * rate * time) / 100

            question = (
                f"At what annual interest rate will ${principal} earn ${interest:.0f} "
                f"simple interest in {time} years?"
            )

            steps.append("Use the simple interest formula: $I = PRT$")
            steps.append("Solve for R: $R = \\frac{I}{PT}$")
            steps.append(f"Given: I = ${interest:.0f}, P = ${principal}, T = {time} years")
            steps.append("Substitute values:")
            steps.append(f"$R = \\frac{{{interest:.0f}}}{{{principal} \\times {time}}}$")
            steps.append(f"$R = \\frac{{{interest:.0f}}}{{{principal * time}}}$")
            steps.append(f"$R = {rate/100}$")
            steps.append(f"Convert to percentage: R = {rate/100} × 100% = {rate}%")
            steps.append(f"**Final Answer:** {rate}%")

            answer = rate

    else:
        # Find time or word problem
        problem_type = random.choice(["time", "word"])

        if problem_type == "time":
            # Find T: T = I / (PR)
            principal = random.randint(8, 40) * 100  # 800-4000 in increments of 100
            rate = random.choice([4, 5, 6, 8, 10])
            time = random.randint(3, 8)

            interest = (principal * rate * time) / 100

            question = (
                f"How many years will it take for ${principal} to earn ${interest:.0f} "
                f"simple interest at {rate}% per year?"
            )

            steps.append("Use the simple interest formula: $I = PRT$")
            steps.append("Solve for T: $T = \\frac{I}{PR}$")
            steps.append(f"Given: I = ${interest:.0f}, P = ${principal}, R = {rate}% = {rate/100}")
            steps.append("Substitute values:")
            steps.append(f"$T = \\frac{{{interest:.0f}}}{{{principal} \\times {rate/100}}}$")
            steps.append(f"$T = \\frac{{{interest:.0f}}}{{{principal * rate / 100}}}$")
            steps.append(f"**Final Answer:** {time} years")

            answer = time

        else:
            # Word problem: find total amount (Principal + Interest)
            principal = random.randint(10, 50) * 100  # 1000-5000 in increments of 100
            rate = random.choice([4, 5, 6, 7, 8])
            time = random.randint(3, 10)

            interest = (principal * rate * time) / 100
            total = principal + interest

            question = (
                f"You deposit ${principal} in a savings account that earns "
                f"{rate}% simple interest per year. What will be the total "
                f"amount in the account after {time} years?"
            )

            steps.append("First, calculate the simple interest using $I = PRT$")
            steps.append(f"P = ${principal}, R = {rate}% = {rate/100}, T = {time} years")
            steps.append(f"$I = {principal} \\times {rate/100} \\times {time}$")
            steps.append(f"$I = {interest:.0f}$")
            steps.append("Total amount = Principal + Interest")
            steps.append(f"Total = ${principal} + ${interest:.0f}")
            steps.append(f"**Final Answer:** ${total:.2f}")

            answer = total

    # Determine answer format
    if difficulty == 2 and find_what == "rate":
        answer_str = str(int(answer))
    elif difficulty == 3 and problem_type == "time":
        answer_str = str(int(answer))
    else:
        answer_str = f"{answer:.2f}"

    return {
        "question": question,
        "answer": answer_str,
        "answer_numeric": round(answer, 2),
        "steps": steps,
        "difficulty": difficulty,
    }
