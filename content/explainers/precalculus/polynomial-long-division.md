# Polynomial Long Division

## What is Polynomial Long Division?

Polynomial long division is a method for dividing one polynomial by another, similar to long division with numbers. It's used to simplify rational expressions, find factors, and solve polynomial equations.

**When to use it:**
- Dividing one polynomial by another
- Simplifying rational expressions
- Finding remainders
- Factoring polynomials
- Solving polynomial equations

**The result:** When dividing P(x) by D(x):
```
P(x)/D(x) = Q(x) + R(x)/D(x)
```

Where:
- P(x) = dividend (what you're dividing)
- D(x) = divisor (what you're dividing by)
- Q(x) = quotient (the answer)
- R(x) = remainder (what's left over)

## How to Do Polynomial Long Division

### The process
1. **Set up** - Write in long division format
2. **Divide leading terms** - First term of dividend ÷ first term of divisor
3. **Multiply** - Multiply divisor by that result
4. **Subtract** - Subtract from dividend
5. **Bring down** - Bring down the next term
6. **Repeat** - Continue until degree of remainder < degree of divisor

## Step-by-Step Example

**Divide:** (2x³ + 3x² - 5x + 6) ÷ (x + 2)

### Step 1: Set up the division
```
         _______________
x + 2 ) 2x³ + 3x² - 5x + 6
```

### Step 2: Divide leading terms
2x³ ÷ x = 2x²
```
         2x²
         _______________
x + 2 ) 2x³ + 3x² - 5x + 6
```

### Step 3: Multiply back
2x²(x + 2) = 2x³ + 4x²
```
         2x²
         _______________
x + 2 ) 2x³ + 3x² - 5x + 6
        2x³ + 4x²
```

### Step 4: Subtract
```
         2x²
         _______________
x + 2 ) 2x³ + 3x² - 5x + 6
       -(2x³ + 4x²)
        ___________
             -x² - 5x
```

### Step 5: Bring down next term and repeat
```
         2x² - x
         _______________
x + 2 ) 2x³ + 3x² - 5x + 6
       -(2x³ + 4x²)
        ___________
             -x² - 5x
            -(-x² - 2x)
             __________
                  -3x + 6
```

### Step 6: Continue
```
         2x² - x - 3
         _______________
x + 2 ) 2x³ + 3x² - 5x + 6
       -(2x³ + 4x²)
        ___________
             -x² - 5x
            -(-x² - 2x)
             __________
                  -3x + 6
                 -(-3x - 6)
                  _________
                       12
```

### Step 7: Write the answer
```
Quotient: 2x² - x - 3
Remainder: 12
Answer: 2x² - x - 3 + 12/(x + 2)
```

### Step 8: Check your answer
Multiply back: (x + 2)(2x² - x - 3) + 12 should equal original
```
= 2x³ - x² - 3x + 4x² - 2x - 6 + 12
= 2x³ + 3x² - 5x + 6 ✓
```

## More Examples

### Example 2: Simple division with no remainder
**Divide:** (x² + 5x + 6) ÷ (x + 2)

```
         x + 3
         ___________
x + 2 ) x² + 5x + 6
       -(x² + 2x)
        _________
            3x + 6
           -(3x + 6)
            ________
                 0

Answer: x + 3 (no remainder)
```

**Check:** (x + 2)(x + 3) = x² + 5x + 6 ✓

### Example 3: With missing terms
**Divide:** (x³ + 8) ÷ (x + 2)

```
Fill in missing terms with 0:
x³ + 0x² + 0x + 8

         x² - 2x + 4
         ______________
x + 2 ) x³ + 0x² + 0x + 8
       -(x³ + 2x²)
        __________
            -2x² + 0x
           -(-2x² - 4x)
            ___________
                 4x + 8
                -(4x + 8)
                 ________
                     0

Answer: x² - 2x + 4
```

**Check:** (x + 2)(x² - 2x + 4) = x³ + 8 ✓

## Key Points to Remember

✓ **Like number division** - Same process, different notation
✓ **Divide leading terms** - Focus on the first term at each step
✓ **Subtract carefully** - Watch your signs
✓ **Stop when remainder degree < divisor degree** - Can't divide further
✓ **Fill in missing terms** - Use 0 coefficients for missing powers
✓ **Check your work** - Multiply quotient by divisor and add remainder
✓ **Organize your work** - Line up like terms vertically
✓ **Degree decreases** - Quotient degree = dividend degree - divisor degree

## Common Mistakes to Avoid

❌ **Sign errors** - Be careful when subtracting (double negative)
❌ **Forgetting terms** - Include 0x² if the x² term is missing
❌ **Wrong alignment** - Keep like terms (same powers) lined up
❌ **Stopping too soon** - Continue until remainder degree < divisor degree

## Practice More

[Khan Academy: Polynomial Long Division](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:polynomials/x9e81a4f98389efdf:poly-div/v/polynomial-division)

---

**Next Skills:**
- Synthetic Division
- Remainder Theorem
- Factor Theorem
