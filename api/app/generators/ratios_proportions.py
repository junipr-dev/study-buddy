"""Ratios and proportions question generator with engaging contexts."""

import random
from typing import Dict, Any, List

# Engaging word problem contexts for proportions
PROPORTION_CONTEXTS = {
    "recipe": [
        {"setup": "A recipe uses {a} cups of flour for every {b} cups of sugar.", "ask": "If you use {new_a} cups of flour, how many cups of sugar do you need?"},
        {"setup": "A smoothie needs {a} bananas for every {b} cups of milk.", "ask": "If you use {new_a} bananas, how many cups of milk do you need?"},
    ],
    "gaming": [
        {"setup": "In a video game, you earn {a} coins for every {b} enemies defeated.", "ask": "If you want {new_a} coins, how many enemies must you defeat?"},
        {"setup": "A player scores {a} points for every {b} levels completed.", "ask": "How many points for completing {new_a} levels?"},
    ],
    "social_media": [
        {"setup": "A post gets {a} likes for every {b} shares.", "ask": "If a post has {new_a} shares, how many likes would you expect?"},
        {"setup": "An influencer gains {a} followers for every {b} posts.", "ask": "How many posts to gain {new_a} followers?"},
    ],
    "map": [
        {"setup": "On a map, {a} inches represents {b} miles.", "ask": "How many miles does {new_a} inches represent?"},
        {"setup": "A model uses a scale of {a} cm to {b} meters.", "ask": "If the model is {new_a} cm, what's the real size in meters?"},
    ],
    "sports": [
        {"setup": "A basketball player makes {a} shots out of every {b} attempts.", "ask": "Out of {new_a} attempts, how many shots would they make?"},
        {"setup": "A runner covers {a} miles in {b} hours.", "ask": "At this rate, how many miles in {new_a} hours?"},
    ],
}

# Three-part ratio contexts
THREE_RATIO_CONTEXTS = [
    {"context": "sharing_money", "template": "Three friends split ${total} in the ratio {a}:{b}:{c}. What does the person with the largest share get?"},
    {"context": "mixing_paint", "template": "To make a color, mix red, blue, and yellow in the ratio {a}:{b}:{c}. If you use {total} ml total, how much of the most-used color do you need?"},
    {"context": "team_points", "template": "Three players scored points in the ratio {a}:{b}:{c}. If the team scored {total} total points, what did the top scorer get?"},
]


def generate_ratios_proportions(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a ratios and proportions problem.

    Args:
        difficulty: 1 (simple ratios), 2 (word problems), 3 (complex proportions)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps: List[str] = []

    if difficulty == 1:
        # Simple ratio: a:b = x:d, find x
        a = random.randint(2, 8)
        b = random.randint(2, 8)
        multiplier = random.randint(2, 5)
        d = b * multiplier
        x = a * multiplier

        question = f"If ${a}:{b} = x:{d}$, find $x$"

        steps.append(f"Set up the proportion: $\\frac{{{a}}}{{{b}}} = \\frac{{x}}{{{d}}}$")
        steps.append("Cross multiply:")
        steps.append(f"${a} \\times {d} = {b} \\times x$")
        steps.append(f"${a * d} = {b}x$")
        steps.append(f"Divide both sides by ${b}$:")
        steps.append(f"$x = \\frac{{{a * d}}}{{{b}}} = {x}$")

        answer = x

    elif difficulty == 2:
        # Word problem with engaging context
        category = random.choice(list(PROPORTION_CONTEXTS.keys()))
        context = random.choice(PROPORTION_CONTEXTS[category])

        a = random.randint(2, 6)
        b = random.randint(2, 6)
        multiplier = random.randint(2, 5)
        new_a = a * multiplier
        answer = b * multiplier

        setup = context["setup"].format(a=a, b=b)
        ask = context["ask"].format(new_a=new_a)
        question = f"{setup} {ask}"

        steps.append(f"**Problem:** {question}")
        steps.append(f"**Set up a proportion:**")
        steps.append(f"$\\frac{{{a}}}{{{b}}} = \\frac{{{new_a}}}{{x}}$")
        steps.append("**Cross multiply:**")
        steps.append(f"${a} \\times x = {b} \\times {new_a}$")
        steps.append(f"${a}x = {b * new_a}$")
        steps.append(f"**Divide both sides by ${a}$:**")
        steps.append(f"$x = \\frac{{{b * new_a}}}{{{a}}} = {answer}$")

    else:
        # Complex proportion with 3 quantities and engaging context
        # a:b:c ratio, given total, find each part
        a = random.randint(1, 4)
        b = random.randint(2, 5)
        c = random.randint(2, 6)
        sum_parts = a + b + c
        total = sum_parts * random.randint(3, 8)

        part_a = (total * a) // sum_parts
        part_b = (total * b) // sum_parts
        part_c = (total * c) // sum_parts

        # Use engaging context
        context = random.choice(THREE_RATIO_CONTEXTS)
        question = context["template"].format(a=a, b=b, c=c, total=total)

        steps.append(f"**Problem:** {question}")
        steps.append(f"**The ratio is** ${a}:{b}:{c}$")
        steps.append(f"**Let the parts be** ${a}x$, ${b}x$, and ${c}x$")
        steps.append(f"**Their sum equals** ${total}$:")
        steps.append(f"${a}x + {b}x + {c}x = {total}$")
        steps.append(f"${sum_parts}x = {total}$")
        steps.append(f"$x = \\frac{{{total}}}{{{sum_parts}}} = {total // sum_parts}$")
        steps.append(f"**Calculate each part:**")
        steps.append(f"First part: ${a} \\times {total // sum_parts} = {part_a}$")
        steps.append(f"Second part: ${b} \\times {total // sum_parts} = {part_b}$")
        steps.append(f"Third part: ${c} \\times {total // sum_parts} = {part_c}$")
        steps.append(f"**The largest is** ${max(part_a, part_b, part_c)}$")

        answer = max(part_a, part_b, part_c)

    steps.append(f"**Final Answer:** ${answer}$")

    return {
        "question": question,
        "answer": str(answer),
        "answer_numeric": answer,
        "steps": steps,
        "difficulty": difficulty,
    }
