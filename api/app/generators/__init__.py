"""Question generator modules."""

from typing import Dict, Callable, Any
from app.generators.linear_equation import generate_linear_equation
from app.generators.fraction_operations import generate_fraction_addition
from app.generators.quadratic_equation import generate_quadratic_equation
from app.generators.systems_equations import generate_system_of_equations
from app.generators.polynomial_operations import generate_polynomial_operation
from app.generators.order_of_operations import generate_order_of_operations
from app.generators.distributive_property import generate_distributive_property
from app.generators.combining_like_terms import generate_combining_like_terms
from app.generators.evaluating_expressions import generate_evaluating_expressions
from app.generators.inequalities import generate_inequality
from app.generators.exponent_rules import generate_exponent_rules
from app.generators.slope_intercept import generate_slope_intercept
from app.generators.integers_operations import generate_integers_operations
from app.generators.absolute_value import generate_absolute_value
from app.generators.fractions_multiplication import generate_fractions_multiplication
from app.generators.fractions_division import generate_fractions_division
from app.generators.percentages import generate_percentages

# Registry of generator functions by template type
GENERATORS: Dict[str, Callable[[int], Dict[str, Any]]] = {
    "linear_equation": generate_linear_equation,
    "fraction_addition": generate_fraction_addition,
    "quadratic_equation": generate_quadratic_equation,
    "system_of_equations": generate_system_of_equations,
    "polynomial_operation": generate_polynomial_operation,
    "order_of_operations": generate_order_of_operations,
    "distributive_property": generate_distributive_property,
    "combining_like_terms": generate_combining_like_terms,
    "evaluating_expressions": generate_evaluating_expressions,
    "inequality": generate_inequality,
    "exponent_rules": generate_exponent_rules,
    "slope_intercept": generate_slope_intercept,
    "integers_operations": generate_integers_operations,
    "absolute_value": generate_absolute_value,
    "fractions_multiplication": generate_fractions_multiplication,
    "fractions_division": generate_fractions_division,
    "percentages": generate_percentages,
}


def get_generator(template_type: str) -> Callable[[int], Dict[str, Any]]:
    """Get generator function for a template type."""
    if template_type not in GENERATORS:
        raise ValueError(f"Unknown template type: {template_type}")
    return GENERATORS[template_type]
