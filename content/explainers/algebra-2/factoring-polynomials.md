# Factoring Polynomials

## What is Factoring Polynomials?

Factoring a polynomial means writing it as a product of simpler polynomials. It's the reverse of multiplying polynomials.

**Think:**
- Multiplying: (x + 2)(x + 3) = x² + 5x + 6
- Factoring: x² + 5x + 6 = (x + 2)(x + 3)

Factoring is useful for:
- Solving polynomial equations
- Simplifying expressions
- Finding roots/zeros
- Graphing functions

## Types of Factoring

1. **Greatest Common Factor (GCF)**
2. **Difference of Squares**
3. **Perfect Square Trinomials**
4. **Trinomials (quadratics)**
5. **Difference/Sum of Cubes**
6. **Grouping**

## Method 1: Greatest Common Factor (GCF)

**Always try this first!**

**Step-by-step:**
1. Find GCF of all terms
2. Factor it out
3. Write remaining polynomial inside parentheses

### Example: GCF Factoring

**Factor:** 6x³ - 9x² + 3x

```
Step 1: Find GCF
Coefficients: GCF(6, 9, 3) = 3
Variables: x (lowest power)
GCF = 3x

Step 2: Divide each term by 3x
6x³ ÷ 3x = 2x²
9x² ÷ 3x = 3x
3x ÷ 3x = 1

Step 3: Write factored form
6x³ - 9x² + 3x = 3x(2x² - 3x + 1)
```

**Check:** 3x(2x² - 3x + 1) = 6x³ - 9x² + 3x ✓

## Method 2: Difference of Squares

**Pattern:** a² - b² = (a + b)(a - b)

**Recognize:**
- Two terms
- Both perfect squares
- Subtraction between them

### Example: Difference of Squares

**Factor:** x² - 25

```
Step 1: Identify squares
x² = (x)²
25 = (5)²

Step 2: Apply pattern
x² - 25 = (x + 5)(x - 5)
```

**Check:** (x + 5)(x - 5) = x² - 5x + 5x - 25 = x² - 25 ✓

**More examples:**
```
4x² - 9 = (2x + 3)(2x - 3)
x⁴ - 16 = (x² + 4)(x² - 4) = (x² + 4)(x + 2)(x - 2)
```

## Method 3: Perfect Square Trinomials

**Patterns:**
- a² + 2ab + b² = (a + b)²
- a² - 2ab + b² = (a - b)²

**Recognize:**
- Three terms
- First and last are perfect squares
- Middle = 2 × (product of square roots)

### Example: Perfect Square Trinomial

**Factor:** x² + 6x + 9

```
Step 1: Check if perfect square
First: x² = (x)²
Last: 9 = (3)²
Middle: 6x = 2(x)(3) ✓

Step 2: Factor
x² + 6x + 9 = (x + 3)²
```

**Check:** (x + 3)² = x² + 6x + 9 ✓

## Method 4: Factoring Trinomials

**For:** ax² + bx + c

### When a = 1:
Find two numbers that multiply to c and add to b

**Example:** x² + 7x + 12

```
Need: m × n = 12, m + n = 7
Try: 3 × 4 = 12, 3 + 4 = 7 ✓

Factor: (x + 3)(x + 4)
```

### When a ≠ 1:
Use AC method or trial and error

**Example:** 2x² + 7x + 3

```
AC method:
a × c = 2 × 3 = 6
Need two numbers: multiply to 6, add to 7
6 and 1 work: 6 × 1 = 6, 6 + 1 = 7

Rewrite middle term:
2x² + 6x + x + 3

Group and factor:
2x(x + 3) + 1(x + 3)
= (2x + 1)(x + 3)
```

**Check:** (2x + 1)(x + 3) = 2x² + 7x + 3 ✓

## Method 5: Sum and Difference of Cubes

**Patterns:**
- a³ + b³ = (a + b)(a² - ab + b²)
- a³ - b³ = (a - b)(a² + ab + b²)

### Example: Difference of Cubes

**Factor:** x³ - 8

```
Step 1: Identify cubes
x³ = (x)³
8 = (2)³

Step 2: Apply pattern
a = x, b = 2
x³ - 8 = (x - 2)(x² + 2x + 4)
```

**Note:** The trinomial factor usually doesn't factor further (over real numbers)

### Example: Sum of Cubes

**Factor:** 8x³ + 27

```
8x³ = (2x)³
27 = (3)³

8x³ + 27 = (2x + 3)(4x² - 6x + 9)
```

## Method 6: Factoring by Grouping

**For:** Four terms, group in pairs

### Example: Factoring by Grouping

**Factor:** x³ + 3x² + 2x + 6

```
Step 1: Group terms
(x³ + 3x²) + (2x + 6)

Step 2: Factor GCF from each group
x²(x + 3) + 2(x + 3)

Step 3: Factor common binomial
(x + 3)(x² + 2)
```

**Check:** (x + 3)(x² + 2) = x³ + 2x + 3x² + 6 = x³ + 3x² + 2x + 6 ✓

## Complete Factoring Strategy

**Always follow this order:**

1. **GCF first** - Factor out common factors
2. **Count terms:**
   - 2 terms → Difference of squares or cubes
   - 3 terms → Perfect square or trinomial
   - 4+ terms → Grouping
3. **Check if factors can factor more** - Continue until fully factored
4. **Verify** - Multiply back to check

## Complete Example

**Factor completely:** 2x⁴ - 32

```
Step 1: GCF
GCF = 2
2(x⁴ - 16)

Step 2: Difference of squares (x⁴ - 16)
2(x² + 4)(x² - 4)

Step 3: Factor x² - 4 (another difference of squares)
2(x² + 4)(x + 2)(x - 2)

Completely factored: 2(x² + 4)(x + 2)(x - 2)
```

**Note:** x² + 4 doesn't factor over real numbers (sum of squares)

## More Examples

### Example 1: Multiple methods
**Factor:** 3x³ - 12x

```
GCF: 3x(x² - 4)
Difference of squares: 3x(x + 2)(x - 2)
```

### Example 2: Challenging trinomial
**Factor:** 6x² - 11x - 10

```
AC method: a × c = -60
Need: multiply to -60, add to -11
-15 and 4: -15 × 4 = -60, -15 + 4 = -11 ✓

6x² - 15x + 4x - 10
3x(2x - 5) + 2(2x - 5)
= (3x + 2)(2x - 5)
```

## Key Points to Remember

✓ **GCF first, always** - Makes other steps easier
✓ **Recognize patterns** - Saves time on special cases
✓ **Factor completely** - Keep going until can't factor more
✓ **Check your work** - Multiply factors back
✓ **Watch for negatives** - Sign errors are common
✓ **Some don't factor** - Not everything factors nicely (over reals)

## Common Mistakes to Avoid

❌ **Forgetting GCF** - Wrong: x² - 4x = (x - 4)x
✓ Correct: x² - 4x = x(x - 4)

❌ **Incomplete factoring** - Wrong: 2x² - 8 = 2(x² - 4)
✓ Correct: 2(x² - 4) = 2(x + 2)(x - 2)

❌ **Sign errors** - Wrong: x² - 6x + 9 = (x - 3)(x + 3)
✓ Correct: x² - 6x + 9 = (x - 3)²

❌ **Wrong pattern** - Wrong: x² + 9 = (x + 3)(x - 3)
✓ Correct: x² + 9 doesn't factor (sum of squares)

## Practice More

[Khan Academy: Factoring Polynomials](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:poly-factor)

---

**Next Skills:**
- Solving Polynomial Equations
- Polynomial Division
- Rational Expressions
