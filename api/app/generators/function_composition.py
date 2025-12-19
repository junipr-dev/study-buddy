"""Function composition question generator."""

import random
from typing import Dict, Any


def generate_function_composition(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a function composition problem.

    Args:
        difficulty: 1 (linear compositions), 2 (quadratic compositions), 3 (triple compositions)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Linear function compositions
        # f(x) = ax + b, g(x) = cx + d
        a = random.randint(2, 5)
        b = random.randint(-5, 5)
        c = random.randint(2, 4)
        d = random.randint(-5, 5)
        x_val = random.randint(1, 5)

        # Calculate f(g(x_val))
        g_result = c * x_val + d
        fg_result = a * g_result + b

        question = f"Given $f(x) = {a}x {b:+d}$ and $g(x) = {c}x {d:+d}$, find $f(g({x_val}))$."

        steps = [
            f"First, find $g({x_val})$:",
            f"$g({x_val}) = {c}({x_val}) {d:+d}$",
            f"$g({x_val}) = {c * x_val} {d:+d}$",
            f"$g({x_val}) = {g_result}$",
            "",
            f"Now, find $f(g({x_val})) = f({g_result})$:",
            f"$f({g_result}) = {a}({g_result}) {b:+d}$",
            f"$f({g_result}) = {a * g_result} {b:+d}$",
            f"$f({g_result}) = {fg_result}$",
            "",
            f"**Final Answer:** $f(g({x_val})) = {fg_result}$"
        ]

        answer_numeric = fg_result

    elif difficulty == 2:
        # Medium: Quadratic and linear compositions
        # f(x) = x², g(x) = ax + b
        a = random.randint(2, 4)
        b = random.randint(-4, 4)
        x_val = random.randint(1, 4)

        # Calculate f(g(x_val)) where f(x) = x²
        g_result = a * x_val + b
        fg_result = g_result ** 2

        question = f"Given $f(x) = x^2$ and $g(x) = {a}x {b:+d}$, find $f(g({x_val}))$."

        steps = [
            f"First, find $g({x_val})$:",
            f"$g({x_val}) = {a}({x_val}) {b:+d}$",
            f"$g({x_val}) = {a * x_val} {b:+d}$",
            f"$g({x_val}) = {g_result}$",
            "",
            f"Now, find $f(g({x_val})) = f({g_result})$:",
            f"$f({g_result}) = ({g_result})^2$",
            f"$f({g_result}) = {fg_result}$",
            "",
            f"**Final Answer:** $f(g({x_val})) = {fg_result}$"
        ]

        answer_numeric = fg_result

    else:
        # Hard: Triple composition or g(f(x))
        if random.choice([True, False]):
            # g(f(x)) with f(x) = x², g(x) = ax + b
            a = random.randint(2, 4)
            b = random.randint(-4, 4)
            x_val = random.randint(2, 4)

            # Calculate g(f(x_val))
            f_result = x_val ** 2
            gf_result = a * f_result + b

            question = f"Given $f(x) = x^2$ and $g(x) = {a}x {b:+d}$, find $g(f({x_val}))$."

            steps = [
                f"First, find $f({x_val})$:",
                f"$f({x_val}) = ({x_val})^2$",
                f"$f({x_val}) = {f_result}$",
                "",
                f"Now, find $g(f({x_val})) = g({f_result})$:",
                f"$g({f_result}) = {a}({f_result}) {b:+d}$",
                f"$g({f_result}) = {a * f_result} {b:+d}$",
                f"$g({f_result}) = {gf_result}$",
                "",
                f"**Final Answer:** $g(f({x_val})) = {gf_result}$"
            ]

            answer_numeric = gf_result
        else:
            # Triple composition: f(g(h(x)))
            # f(x) = 2x, g(x) = x + a, h(x) = x + b
            a = random.randint(1, 3)
            b = random.randint(1, 3)
            x_val = random.randint(1, 3)

            # Calculate f(g(h(x_val)))
            h_result = x_val + b
            g_result = h_result + a
            fgh_result = 2 * g_result

            question = f"Given $f(x) = 2x$, $g(x) = x + {a}$, and $h(x) = x + {b}$, find $f(g(h({x_val})))$."

            steps = [
                f"First, find $h({x_val})$:",
                f"$h({x_val}) = {x_val} + {b} = {h_result}$",
                "",
                f"Next, find $g(h({x_val})) = g({h_result})$:",
                f"$g({h_result}) = {h_result} + {a} = {g_result}$",
                "",
                f"Finally, find $f(g(h({x_val}))) = f({g_result})$:",
                f"$f({g_result}) = 2({g_result}) = {fgh_result}$",
                "",
                f"**Final Answer:** $f(g(h({x_val}))) = {fgh_result}$"
            ]

            answer_numeric = fgh_result

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
