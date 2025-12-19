"""Question generator modules."""

from typing import Dict, Callable, Any
from app.generators.linear_equation import generate_linear_equation
from app.generators.fraction_operations import generate_fraction_addition
from app.generators.quadratic_equation import generate_quadratic_equation
from app.generators.systems_equations import generate_system_of_equations
from app.generators.polynomial_operations import generate_polynomial_operation

# Registry of generator functions by template type
GENERATORS: Dict[str, Callable[[int], Dict[str, Any]]] = {
    "linear_equation": generate_linear_equation,
    "fraction_addition": generate_fraction_addition,
    "quadratic_equation": generate_quadratic_equation,
    "system_of_equations": generate_system_of_equations,
    "polynomial_operation": generate_polynomial_operation,
}


def get_generator(template_type: str) -> Callable[[int], Dict[str, Any]]:
    """Get generator function for a template type."""
    if template_type not in GENERATORS:
        raise ValueError(f"Unknown template type: {template_type}")
    return GENERATORS[template_type]
