# Vectors

## What are Vectors?

A vector is a quantity that has both magnitude (size) and direction. Unlike scalars (which only have magnitude), vectors point in a specific direction.

**Notation:**
- **Component form:** v = ⟨a, b⟩ or v = ai + bj
- **Position notation:** v = (a, b)
- **Magnitude:** |v| or ||v||

**Key properties:**
- **Magnitude:** Length or size of the vector
- **Direction:** Angle or orientation
- **Components:** Horizontal and vertical parts

**Examples:**
- Velocity: 50 mph northeast (has speed and direction)
- Force: 10 N at 30° angle
- Displacement: 3 units right, 4 units up = ⟨3, 4⟩

**Scalars vs Vectors:**
- Scalar: temperature, mass, time (no direction)
- Vector: velocity, force, displacement (has direction)

## How to Work with Vectors

### Finding magnitude
**Formula:** |v| = √(a² + b²) for v = ⟨a, b⟩

### Adding vectors
**Geometrically:** Place tail of second at head of first
**Algebraically:** Add components: ⟨a₁, b₁⟩ + ⟨a₂, b₂⟩ = ⟨a₁ + a₂, b₁ + b₂⟩

### Scalar multiplication
Multiply each component: k·⟨a, b⟩ = ⟨ka, kb⟩

### Finding direction
**Angle:** θ = tan⁻¹(b/a)

### Unit vectors
Divide by magnitude: u = v/|v|

## Step-by-Step Example

**Find magnitude and direction:** v = ⟨3, 4⟩

### Step 1: Identify components
```
Horizontal component: a = 3
Vertical component: b = 4
```

### Step 2: Calculate magnitude
Use the Pythagorean theorem:
```
|v| = √(a² + b²)
|v| = √(3² + 4²)
|v| = √(9 + 16)
|v| = √25
|v| = 5
```

### Step 3: Calculate direction
Use inverse tangent:
```
θ = tan⁻¹(b/a)
θ = tan⁻¹(4/3)
θ ≈ 53.13°
```

### Step 4: State the answer
```
Magnitude: 5
Direction: 53.13° from positive x-axis
```

### Step 5: Check your answer
Verify using components:
```
|v|·cos(θ) = 5·cos(53.13°) ≈ 3 ✓
|v|·sin(θ) = 5·sin(53.13°) ≈ 4 ✓
```

## More Examples

### Example 2: Vector addition
**Add:** u = ⟨2, 3⟩ and v = ⟨1, -4⟩

```
u + v = ⟨2 + 1, 3 + (-4)⟩
     = ⟨3, -1⟩

Magnitude: |u + v| = √(3² + (-1)²) = √10 ≈ 3.16
```

**Check:** Plot both vectors and their sum ✓

### Example 3: Scalar multiplication
**Multiply:** 3·⟨2, -1⟩

```
3·⟨2, -1⟩ = ⟨3·2, 3·(-1)⟩
          = ⟨6, -3⟩

Magnitude: |⟨6, -3⟩| = √(36 + 9) = √45 = 3√5
```

**Check:** Magnitude is 3 times original: √(4+1) = √5, and 3√5 ✓

### Example 4: Unit vector
**Find unit vector:** in direction of v = ⟨5, 12⟩

```
Step 1: Find magnitude
|v| = √(5² + 12²) = √(25 + 144) = √169 = 13

Step 2: Divide by magnitude
u = v/|v| = ⟨5/13, 12/13⟩

Step 3: Verify it's a unit vector
|u| = √((5/13)² + (12/13)²)
    = √(25/169 + 144/169)
    = √(169/169)
    = 1 ✓
```

**Check:** Unit vectors always have magnitude 1 ✓

## Key Points to Remember

✓ **Magnitude is distance** - Use Pythagorean theorem
✓ **Direction is angle** - Use inverse tangent
✓ **Add components separately** - Horizontal + horizontal, vertical + vertical
✓ **Scalar multiplication stretches** - Multiplies magnitude, keeps direction
✓ **Negative scalar reverses** - Changes direction by 180°
✓ **Unit vector has magnitude 1** - Shows pure direction
✓ **Zero vector** - ⟨0, 0⟩ has no direction
✓ **Resultant** - Sum of vectors shows combined effect

## Common Mistakes to Avoid

❌ **Adding magnitudes** - Must add components, not lengths
❌ **Wrong quadrant** - Check signs of components for direction
❌ **Confusing scalar and vector** - Scalars have no direction
❌ **Forgetting square root** - In magnitude formula

## Practice More

[Khan Academy: Vectors](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:vectors/x9e81a4f98389efdf:component-form/v/introduction-to-vectors-and-scalars)

---

**Next Skills:**
- Dot Product
- Vector Projections
- Applications of Vectors (physics problems)
