# Polynomial Operations

## What are Polynomials?

A polynomial is an expression made up of variables, constants, and exponents, combined using addition, subtraction, and multiplication. Each part is called a term.

**General form:** a_n x^n + a_(n-1) x^(n-1) + ... + a_1 x + a_0

Types by number of terms:
- **Monomial:** 1 term (3x²)
- **Binomial:** 2 terms (x² + 5)
- **Trinomial:** 3 terms (x² + 3x + 2)
- **Polynomial:** 4+ terms (x³ + 2x² - x + 7)

Types by degree (highest exponent):
- **Linear:** degree 1 (2x + 3)
- **Quadratic:** degree 2 (x² + 5x + 6)
- **Cubic:** degree 3 (x³ - 2x² + x - 1)

## Adding and Subtracting Polynomials

**Rule:** Combine like terms (same variable with same exponent)

### How to Add/Subtract:
1. **Remove parentheses** - Watch signs when subtracting
2. **Identify like terms** - Same variable and exponent
3. **Combine coefficients** - Add or subtract numbers only
4. **Write in standard form** - Descending order of exponents
5. **Check** - Substitute a value to verify

## Step-by-Step Example (Addition)

**Add:** (3x² + 2x - 5) + (x² - 4x + 7)

### Step 1: Remove parentheses
```
3x² + 2x - 5 + x² - 4x + 7
```

### Step 2: Group like terms
```
(3x² + x²) + (2x - 4x) + (-5 + 7)
```

### Step 3: Combine coefficients
```
4x² + (-2x) + 2
4x² - 2x + 2
```

### Step 4: Check
Let x = 1:
```
Original: (3 + 2 - 5) + (1 - 4 + 7) = 0 + 4 = 4
Result: 4(1) - 2(1) + 2 = 4 - 2 + 2 = 4 ✓
```

## Step-by-Step Example (Subtraction)

**Subtract:** (5x² - 3x + 2) - (2x² + x - 4)

### Step 1: Distribute negative sign
```
5x² - 3x + 2 - 2x² - x + 4
```

**Important:** Negative sign affects ALL terms in second polynomial!

### Step 2: Group like terms
```
(5x² - 2x²) + (-3x - x) + (2 + 4)
```

### Step 3: Combine
```
3x² - 4x + 6
```

### Check
Let x = 2:
```
Original: (20 - 6 + 2) - (8 + 2 - 4) = 16 - 6 = 10
Result: 3(4) - 4(2) + 6 = 12 - 8 + 6 = 10 ✓
```

## Multiplying Polynomials

### Monomial × Polynomial
**Distribute the monomial to each term**

**Example:** 3x(2x² - 5x + 4)

```
= 3x(2x²) + 3x(-5x) + 3x(4)
= 6x³ - 15x² + 12x
```

### Binomial × Binomial (FOIL)
**F**irst, **O**uter, **I**nner, **L**ast

**Example:** (x + 3)(x + 5)

```
First: x × x = x²
Outer: x × 5 = 5x
Inner: 3 × x = 3x
Last: 3 × 5 = 15

= x² + 5x + 3x + 15
= x² + 8x + 15
```

### Binomial × Trinomial
**Distribute each term of first to all terms of second**

**Example:** (x + 2)(x² - 3x + 1)

```
x(x² - 3x + 1) + 2(x² - 3x + 1)
= x³ - 3x² + x + 2x² - 6x + 2
= x³ - x² - 5x + 2
```

## More Examples

### Example 1: Three polynomials
**Add:** (2x² + x) + (x² - 3) + (-x² + 5x - 2)

```
Group like terms:
(2x² + x² - x²) + (x + 5x) + (-3 - 2)
= 2x² + 6x - 5
```

### Example 2: Special products - Difference of squares
**Multiply:** (x + 4)(x - 4)

```
Pattern: (a + b)(a - b) = a² - b²

= x² - 16
```

**Verify with FOIL:**
```
x² - 4x + 4x - 16 = x² - 16 ✓
```

### Example 3: Perfect square trinomial
**Multiply:** (x + 3)²

```
Pattern: (a + b)² = a² + 2ab + b²

= x² + 2(x)(3) + 9
= x² + 6x + 9
```

### Example 4: Three binomials
**Multiply:** (x + 1)(x + 2)(x + 3)

```
Step 1: Multiply first two
(x + 1)(x + 2) = x² + 3x + 2

Step 2: Multiply result by third
(x² + 3x + 2)(x + 3)
= x³ + 3x² + 3x² + 9x + 2x + 6
= x³ + 6x² + 11x + 6
```

## Dividing Polynomials

### By a Monomial
**Divide each term separately**

**Example:** (6x³ - 9x² + 3x) ÷ 3x

```
= (6x³/3x) - (9x²/3x) + (3x/3x)
= 2x² - 3x + 1
```

**Check:** 3x(2x² - 3x + 1) = 6x³ - 9x² + 3x ✓

### By a Binomial (Long Division)
**Example:** (x² + 5x + 6) ÷ (x + 2)

```
        x + 3
      ________
x + 2 | x² + 5x + 6
        x² + 2x
        -------
            3x + 6
            3x + 6
            ------
                0

Result: x + 3
```

**Check:** (x + 2)(x + 3) = x² + 5x + 6 ✓

## Special Polynomial Patterns

**Sum of cubes:**
```
a³ + b³ = (a + b)(a² - ab + b²)
```

**Difference of cubes:**
```
a³ - b³ = (a - b)(a² + ab + b²)
```

**Perfect square trinomials:**
```
a² + 2ab + b² = (a + b)²
a² - 2ab + b² = (a - b)²
```

## Key Points to Remember

✓ **Like terms only** - Same variable with same exponent
✓ **Distribute carefully** - Watch negative signs
✓ **Standard form** - Write in descending order of exponents
✓ **FOIL for binomials** - First, Outer, Inner, Last
✓ **Special patterns** - Recognize to save time
✓ **Check your work** - Substitute a value or multiply back

## Common Mistakes to Avoid

❌ **Combining unlike terms** - Wrong: x² + x = 2x²
✓ Correct: x² + x stays as x² + x

❌ **Sign errors in subtraction** - Wrong: (x - 2) - (x - 3) = -5
✓ Correct: x - 2 - x + 3 = 1

❌ **Forgetting middle terms** - Wrong: (x + 2)² = x² + 4
✓ Correct: (x + 2)² = x² + 4x + 4

❌ **Not simplifying** - Wrong: Leaving x² + x² as is
✓ Correct: x² + x² = 2x²

## Practice More

[Khan Academy: Polynomial Operations](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:poly-arithmetic)

---

**Next Skills:**
- Factoring Polynomials
- Polynomial Division
- Remainder Theorem
