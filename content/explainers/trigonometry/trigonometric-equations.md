# Trigonometric Equations

## What are Trigonometric Equations?

Trigonometric equations are equations that contain trigonometric functions like sine, cosine, or tangent. Unlike identities (which are true for all values), trig equations are only true for specific angle values.

**Key difference:**
- **Identity:** sin²(θ) + cos²(θ) = 1 (true for all θ)
- **Equation:** sin(θ) = 1/2 (only true for specific angles)

**Types of solutions:**
- **Principal solution** - The first solution in the standard range
- **General solution** - All possible solutions (often infinitely many)

**Solving strategies:**
1. Algebraic manipulation (isolate the trig function)
2. Using inverse trig functions
3. Using trig identities to simplify
4. Factoring
5. Checking for multiple solutions

## How to Solve Trigonometric Equations

### Basic equations
1. **Isolate the trig function** - Get sin(θ), cos(θ), or tan(θ) alone
2. **Use inverse function** - Apply sin⁻¹, cos⁻¹, or tan⁻¹
3. **Find principal value** - The first solution
4. **Find all solutions** - Use periodicity and symmetry
5. **Check the domain** - Ensure solutions are in the specified range

### Equations with identities
1. **Simplify using identities** - Convert to a simpler form
2. **Factor if possible** - Get zero on one side
3. **Solve each factor** - Set each factor equal to zero
4. **Find all solutions** - Consider the period

## Step-by-Step Example

**Solve:** 2sin(θ) - 1 = 0 for 0° ≤ θ < 360°

### Step 1: Isolate the trig function
Add 1 to both sides, then divide by 2:
```
2sin(θ) = 1
sin(θ) = 1/2
```

### Step 2: Find the principal value
Use inverse sine:
```
θ = sin⁻¹(1/2)
θ = 30°
```

### Step 3: Find other solutions in the range
Sine is positive in quadrants I and II:
```
Quadrant I: θ = 30°
Quadrant II: θ = 180° - 30° = 150°
```

### Step 4: Check both solutions
Verify each answer:
```
sin(30°) = 1/2 ✓
sin(150°) = 1/2 ✓
```

### Step 5: State the complete solution
```
θ = 30° or θ = 150°
```

## More Examples

### Example 2: Using identities
**Solve:** sin²(θ) - sin(θ) = 0 for 0 ≤ θ < 2π

```
Factor out sin(θ):
sin(θ)(sin(θ) - 1) = 0

Set each factor to zero:
sin(θ) = 0  OR  sin(θ) - 1 = 0

Solve first: sin(θ) = 0
θ = 0, π

Solve second: sin(θ) = 1
θ = π/2

Complete solution: θ = 0, π/2, π
```

**Check:** All values satisfy the original equation ✓

### Example 3: Pythagorean identity
**Solve:** cos²(θ) = 1 - sin(θ) for 0° ≤ θ < 360°

```
Use identity: cos²(θ) = 1 - sin²(θ)
Substitute:
1 - sin²(θ) = 1 - sin(θ)
-sin²(θ) = -sin(θ)
sin²(θ) = sin(θ)
sin²(θ) - sin(θ) = 0
sin(θ)(sin(θ) - 1) = 0

Solutions:
sin(θ) = 0: θ = 0°, 180°
sin(θ) = 1: θ = 90°

Answer: θ = 0°, 90°, 180°
```

**Check:** Each solution satisfies cos²(θ) = 1 - sin(θ) ✓

### Example 4: Double angle
**Solve:** cos(2θ) = 0 for 0 ≤ θ < 2π

```
Find when cos = 0:
2θ = π/2, 3π/2, 5π/2, 7π/2

Divide by 2:
θ = π/4, 3π/4, 5π/4, 7π/4

All four are in [0, 2π)
```

**Check:** cos(2·π/4) = cos(π/2) = 0 ✓

## Key Points to Remember

✓ **Multiple solutions are common** - Trig functions are periodic
✓ **Check all quadrants** - Use reference angles to find all solutions
✓ **Mind the domain** - Only include solutions in the specified range
✓ **Identities are your friend** - Use them to simplify equations
✓ **Factor when possible** - Easier to solve factored forms
✓ **Always verify** - Substitute back to check
✓ **Principal value isn't the only one** - Look for other solutions
✓ **Period matters** - Solutions repeat every 2π (or 360°)

## Common Mistakes to Avoid

❌ **Finding only one solution** - Check all quadrants for additional answers
❌ **Dividing by a trig function** - You might lose solutions; factor instead
❌ **Forgetting to check domain** - Solutions outside the range don't count
❌ **Not using identities** - They often simplify the equation significantly

## Practice More

[Khan Academy: Trigonometric Equations](https://www.khanacademy.org/math/trigonometry/trig-equations-and-identities/solving-trig-equations/v/solving-basic-trig-equation)

---

**Next Skills:**
- Solving Trig Equations with Multiple Angles
- Systems of Trig Equations
- Applications of Trig Equations
