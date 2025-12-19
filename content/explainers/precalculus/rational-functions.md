# Rational Functions

## What are Rational Functions?

A rational function is a function that can be written as the ratio of two polynomials. It's a fraction where both the numerator and denominator are polynomials.

**General form:** f(x) = P(x)/Q(x)

Where P(x) and Q(x) are polynomials, and Q(x) ≠ 0.

**Key features:**
- **Vertical asymptotes** - Lines where the function is undefined (denominator = 0)
- **Horizontal/slant asymptotes** - Behavior as x approaches ±∞
- **Holes** - Points where factors cancel
- **Domain** - All real numbers except where denominator = 0

Examples:
- f(x) = 1/x (simplest rational function)
- f(x) = (x + 1)/(x - 2)
- f(x) = (x² - 4)/(x² - 1)

## How to Analyze Rational Functions

### Finding vertical asymptotes
1. **Factor numerator and denominator** - Simplify if possible
2. **Set denominator = 0** - Solve for x
3. **Check for cancellations** - Cancelled factors make holes, not asymptotes
4. **Write equations** - x = value is a vertical asymptote

### Finding horizontal asymptotes
1. **Compare degrees** - Look at highest power in numerator vs denominator
2. **Apply rules:**
   - If degree(numerator) < degree(denominator): y = 0
   - If degree(numerator) = degree(denominator): y = ratio of leading coefficients
   - If degree(numerator) > degree(denominator): no horizontal asymptote (may have slant)

### Finding holes
1. **Factor completely** - Both numerator and denominator
2. **Find common factors** - These create holes
3. **Calculate x-coordinate** - Set common factor = 0
4. **Calculate y-coordinate** - Plug x into simplified function

## Step-by-Step Example

**Analyze:** f(x) = (x² - 4)/(x² - 3x + 2)

### Step 1: Factor numerator and denominator
```
Numerator: x² - 4 = (x + 2)(x - 2)
Denominator: x² - 3x + 2 = (x - 1)(x - 2)

f(x) = (x + 2)(x - 2)
       ──────────────
       (x - 1)(x - 2)
```

### Step 2: Identify holes
Common factor: (x - 2)
```
Hole at x = 2

Simplified: f(x) = (x + 2)/(x - 1)

Y-coordinate: (2 + 2)/(2 - 1) = 4/1 = 4
Hole at (2, 4)
```

### Step 3: Find vertical asymptotes
Set simplified denominator = 0:
```
x - 1 = 0
x = 1

Vertical asymptote: x = 1
```

### Step 4: Find horizontal asymptote
Compare degrees of simplified function:
```
Degree of numerator: 1
Degree of denominator: 1
Same degree, so y = ratio of leading coefficients

y = 1/1 = 1
Horizontal asymptote: y = 1
```

### Step 5: Check your answer
```
Domain: all real numbers except x = 1 and x = 2
Vertical asymptote: x = 1 ✓
Hole: (2, 4) ✓
Horizontal asymptote: y = 1 ✓
```

## More Examples

### Example 2: Simple rational function
**Analyze:** f(x) = 1/(x - 3)

```
No common factors, already simplified

Vertical asymptote: x - 3 = 0 → x = 3
Horizontal asymptote: degree 0 < degree 1 → y = 0
No holes

Domain: x ≠ 3
```

**Check:** As x → ∞, 1/x approaches 0 ✓

### Example 3: Higher degree numerator
**Analyze:** f(x) = (2x² + 1)/(x - 1)

```
No common factors

Vertical asymptote: x = 1
Horizontal asymptote: degree 2 > degree 1 → none
(Has slant asymptote instead: y = 2x + 2)

Domain: x ≠ 1
```

**Check:** Use long division to find slant asymptote ✓

### Example 4: Equal degrees
**Analyze:** f(x) = (3x² + 5)/(2x² - 8)

```
Factor denominator: 2(x² - 4) = 2(x + 2)(x - 2)
No common factors

Vertical asymptotes: x = -2 and x = 2
Horizontal asymptote: y = 3/2 (ratio of leading coefficients)

Domain: x ≠ -2, 2
```

**Check:** As x → ∞, function approaches 3/2 ✓

## Key Points to Remember

✓ **Domain excludes denominator zeros** - Set Q(x) ≠ 0
✓ **Factor first** - Always simplify before analyzing
✓ **Holes vs asymptotes** - Cancelled factors make holes, remaining make asymptotes
✓ **Degree comparison** - Determines horizontal asymptote behavior
✓ **Vertical asymptote behavior** - Function approaches ±∞ near asymptotes
✓ **Horizontal asymptote** - Shows end behavior (as x → ±∞)
✓ **Graph has branches** - Separated by asymptotes
✓ **Slant asymptotes** - When numerator degree is exactly 1 more than denominator

## Common Mistakes to Avoid

❌ **Not factoring first** - Always simplify before finding asymptotes
❌ **Confusing holes and asymptotes** - Cancelled factors make holes
❌ **Wrong degree comparison** - Check highest power carefully
❌ **Forgetting domain restrictions** - Include all values where denominator = 0

## Practice More

[Khan Academy: Rational Functions](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:rational-functions/x9e81a4f98389efdf:rational-discontinuities/v/discontinuities-of-rational-functions)

---

**Next Skills:**
- Graphing Rational Functions
- Slant Asymptotes
- Solving Rational Equations
