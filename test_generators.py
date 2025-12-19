#!/usr/bin/env python3
"""Test script to verify all generators work correctly."""

import sys
sys.path.insert(0, '/home/jesse/school/study-buddy/api')

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

def test_generator(name, generator_func, difficulty=1):
    """Test a single generator."""
    print(f"\n{'='*60}")
    print(f"Testing: {name} (difficulty {difficulty})")
    print('='*60)
    try:
        result = generator_func(difficulty)
        print(f"Question: {result['question']}")
        print(f"Answer: {result['answer']}")
        print(f"\nSolution steps:")
        for i, step in enumerate(result['steps'], 1):
            print(f"  {i}. {step}")
        print("\n✓ PASSED")
        return True
    except Exception as e:
        print(f"\n✗ FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all generator tests."""
    generators = [
        ("Order of Operations", generate_order_of_operations),
        ("Distributive Property", generate_distributive_property),
        ("Combining Like Terms", generate_combining_like_terms),
        ("Evaluating Expressions", generate_evaluating_expressions),
        ("Inequalities", generate_inequality),
        ("Exponent Rules", generate_exponent_rules),
        ("Slope-Intercept Form", generate_slope_intercept),
        ("Integer Operations", generate_integers_operations),
        ("Absolute Value", generate_absolute_value),
        ("Fractions Multiplication", generate_fractions_multiplication),
        ("Fractions Division", generate_fractions_division),
        ("Percentages", generate_percentages),
    ]

    results = []
    for name, func in generators:
        # Test difficulty 1 for each
        passed = test_generator(name, func, difficulty=1)
        results.append((name, passed))

    # Summary
    print(f"\n\n{'='*60}")
    print("TEST SUMMARY")
    print('='*60)
    passed_count = sum(1 for _, passed in results if passed)
    total_count = len(results)

    for name, passed in results:
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{name}: {status}")

    print(f"\nTotal: {passed_count}/{total_count} passed")

    if passed_count == total_count:
        print("\n🎉 All generators working correctly!")
        return 0
    else:
        print(f"\n⚠️  {total_count - passed_count} generator(s) failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
