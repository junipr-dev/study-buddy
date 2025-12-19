# Polar Coordinates

## What are Polar Coordinates?

Polar coordinates describe a point's location using a distance from the origin and an angle from the positive x-axis, instead of x and y coordinates.

**Notation:** (r, θ)
- r = radius (distance from origin)
- θ = angle (measured counterclockwise from positive x-axis)

**Relationship to rectangular coordinates:**
```
x = r·cos(θ)
y = r·sin(θ)

r = √(x² + y²)
θ = tan⁻¹(y/x)
```

**Why use polar coordinates?**
- Circles and spirals are simpler
- Rotational symmetry is natural
- Many physics problems (circular motion, waves)
- Navigation and radar systems

Examples:
- (3, π/4) means 3 units at 45° angle
- (2, π/2) means 2 units straight up
- (5, 0) means 5 units on positive x-axis

## How to Work with Polar Coordinates

### Plotting points
1. **Start at origin** - Begin at (0, 0)
2. **Rotate by angle θ** - Measure counterclockwise from positive x-axis
3. **Move out distance r** - Go r units in that direction
4. **Mark the point** - That's your location

### Converting to rectangular
1. **Use conversion formulas** - x = r·cos(θ), y = r·sin(θ)
2. **Calculate** - Find x and y values
3. **Write as (x, y)** - Rectangular coordinates

### Converting from rectangular
1. **Find r** - Use r = √(x² + y²)
2. **Find θ** - Use θ = tan⁻¹(y/x)
3. **Check quadrant** - Adjust θ if needed
4. **Write as (r, θ)** - Polar coordinates

## Step-by-Step Example

**Plot the point:** (4, π/3)

### Step 1: Identify r and θ
```
r = 4 (distance from origin)
θ = π/3 = 60° (angle)
```

### Step 2: Rotate to angle
Start at positive x-axis, rotate 60° counterclockwise:
```
Angle π/3 is 60° from positive x-axis
```

### Step 3: Move out distance r
From the origin, go 4 units in the π/3 direction:
```
Move 4 units at 60° angle
```

### Step 4: Convert to rectangular (to verify)
```
x = r·cos(θ) = 4·cos(π/3) = 4·(1/2) = 2
y = r·sin(θ) = 4·sin(π/3) = 4·(√3/2) = 2√3 ≈ 3.46

Rectangular: (2, 2√3)
```

### Step 5: Check your answer
Verify distance from origin:
```
r = √(2² + (2√3)²) = √(4 + 12) = √16 = 4 ✓
```

## More Examples

### Example 2: Convert to rectangular
**Convert:** (6, 3π/4)

```
x = r·cos(θ) = 6·cos(3π/4) = 6·(-√2/2) = -3√2
y = r·sin(θ) = 6·sin(3π/4) = 6·(√2/2) = 3√2

Rectangular: (-3√2, 3√2)
```

**Check:** √((-3√2)² + (3√2)²) = √(18 + 18) = √36 = 6 ✓

### Example 3: Convert to polar
**Convert:** (3, 3) to polar

```
r = √(3² + 3²) = √18 = 3√2

θ = tan⁻¹(3/3) = tan⁻¹(1) = π/4
(point in quadrant I, so angle is correct)

Polar: (3√2, π/4)
```

**Check:** 3√2·cos(π/4) = 3√2·(√2/2) = 3 ✓

### Example 4: Negative radius
**Plot:** (-2, π/6)

```
Negative r means go in opposite direction:
Instead of π/6, go to π/6 + π = 7π/6

Equivalent to: (2, 7π/6)

Rectangular:
x = -2·cos(π/6) = -2·(√3/2) = -√3
y = -2·sin(π/6) = -2·(1/2) = -1

Point: (-√3, -1)
```

**Check:** Point is in quadrant III as expected ✓

## Key Points to Remember

✓ **r is distance** - How far from origin
✓ **θ is direction** - Angle from positive x-axis
✓ **Counterclockwise is positive** - Standard angle direction
✓ **Multiple representations** - Same point has infinitely many polar forms
✓ **Negative r** - Means opposite direction
✓ **Add 2π to θ** - Gets you back to same angle
✓ **Check quadrant** - When converting from rectangular
✓ **Special angles help** - Memorize sin/cos for common angles

## Common Mistakes to Avoid

❌ **Wrong quadrant** - tan⁻¹ gives angles in [-π/2, π/2], adjust for quadrants II and III
❌ **Forgetting negative r** - Can change direction instead of distance
❌ **Wrong angle direction** - Clockwise is negative
❌ **Calculator mode** - Make sure you're in radians (or degrees if specified)

## Practice More

[Khan Academy: Polar Coordinates](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:polar/x9e81a4f98389efdf:polar-coords/v/polar-coordinates-1)

---

**Next Skills:**
- Graphing Polar Equations
- Converting Equations Between Systems
- Area in Polar Coordinates
