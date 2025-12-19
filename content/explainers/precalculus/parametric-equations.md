# Parametric Equations

## What are Parametric Equations?

Parametric equations express coordinates (x and y) as separate functions of a third variable, usually called t (the parameter). Instead of y as a function of x, both x and y are functions of t.

**Standard form:**
```
x = f(t)
y = g(t)
```

Where t is the parameter (often representing time).

**Why use parametric equations?**
- Describe motion and paths (time-dependent)
- Represent curves that fail the vertical line test
- Model real-world motion (projectiles, planets, etc.)
- Easier to work with for certain curves

**Examples:**
- Circle: x = cos(t), y = sin(t)
- Line: x = 2t, y = 3t + 1
- Projectile: x = v₀t, y = h₀ - 16t²

## How to Work with Parametric Equations

### Plotting points
1. **Choose t values** - Select several values
2. **Calculate x and y** - For each t value
3. **Plot points** - (x, y) coordinates
4. **Connect** - Draw the curve
5. **Show direction** - Arrow shows increasing t

### Converting to rectangular form
1. **Solve one equation for t** - Usually the simpler one
2. **Substitute into other equation** - Replace t
3. **Simplify** - Get y in terms of x (or vice versa)

### Finding derivatives
1. **Find dx/dt and dy/dt** - Derivatives with respect to t
2. **Use chain rule** - dy/dx = (dy/dt)/(dx/dt)

## Step-by-Step Example

**Graph:** x = t + 1, y = 2t - 3, for -2 ≤ t ≤ 2

### Step 1: Create a table of values
```
t  | x = t + 1 | y = 2t - 3 | Point (x, y)
---|-----------|------------|-------------
-2 |    -1     |    -7      |   (-1, -7)
-1 |     0     |    -5      |   (0, -5)
 0 |     1     |    -3      |   (1, -3)
 1 |     2     |    -1      |   (2, -1)
 2 |     3     |     1      |   (3, 1)
```

### Step 2: Plot the points
Mark each (x, y) point on the coordinate plane:
```
Points: (-1, -7), (0, -5), (1, -3), (2, -1), (3, 1)
```

### Step 3: Connect and show direction
Draw a line through the points with arrow showing t increasing:
```
Line from (-1, -7) to (3, 1) with arrow →
```

### Step 4: Convert to rectangular form
Solve for t from x equation:
```
x = t + 1
t = x - 1

Substitute into y equation:
y = 2(x - 1) - 3
y = 2x - 2 - 3
y = 2x - 5
```

### Step 5: Check your answer
Verify with a point, say t = 0:
```
Parametric: (1, -3)
Rectangular: y = 2(1) - 5 = -3 ✓
```

## More Examples

### Example 2: Circle
**Graph:** x = 3cos(t), y = 3sin(t), 0 ≤ t ≤ 2π

```
Key points:
t = 0: (3, 0)
t = π/2: (0, 3)
t = π: (-3, 0)
t = 3π/2: (0, -3)
t = 2π: (3, 0)

Rectangular form:
x² + y² = (3cos(t))² + (3sin(t))²
x² + y² = 9(cos²(t) + sin²(t))
x² + y² = 9

Circle with radius 3, center at origin
```

**Check:** All points are distance 3 from origin ✓

### Example 3: Parabola
**Convert to rectangular:** x = t², y = 2t

```
Solve y for t:
y = 2t
t = y/2

Substitute into x:
x = (y/2)²
x = y²/4
y² = 4x

Parabola opening to the right
```

**Check:** Point t = 2 gives (4, 4), and 4² = 4(4) ✓

### Example 4: Finding slope
**Find dy/dx at t = 1:** x = t³, y = t²

```
Find derivatives:
dx/dt = 3t²
dy/dt = 2t

Apply formula:
dy/dx = (dy/dt)/(dx/dt) = 2t/(3t²) = 2/(3t)

At t = 1:
dy/dx = 2/(3·1) = 2/3
```

**Check:** Slope at point (1, 1) is 2/3 ✓

## Key Points to Remember

✓ **Parameter is independent** - Both x and y depend on t
✓ **Direction matters** - Curves have orientation as t increases
✓ **Not always functions** - Can go backwards or loop
✓ **Eliminate parameter** - To convert to rectangular form
✓ **Time-based** - Often t represents time in applications
✓ **Multiple representations** - Same curve can have different parametric forms
✓ **Derivatives need chain rule** - dy/dx = (dy/dt)/(dx/dt)
✓ **Table helps** - Plot several points to see the curve

## Common Mistakes to Avoid

❌ **Forgetting direction** - The parameter gives the curve orientation
❌ **Wrong elimination** - Check your algebra when removing the parameter
❌ **Missing domain** - Pay attention to the range of t values
❌ **Dividing by zero** - In dy/dx, check that dx/dt ≠ 0

## Practice More

[Khan Academy: Parametric Equations](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:parametric/x9e81a4f98389efdf:parametric-intro/v/parametric-equations-1)

---

**Next Skills:**
- Polar Coordinates
- Vectors
- Calculus with Parametric Equations
