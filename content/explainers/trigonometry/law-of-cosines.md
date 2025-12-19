# Law of Cosines

## What is the Law of Cosines?

The Law of Cosines is a formula that relates all three sides of a triangle to one of its angles. It's a generalization of the Pythagorean theorem that works for any triangle, not just right triangles.

**Formula:** c² = a² + b² - 2ab·cos(C)

You can also write it for the other sides:
- a² = b² + c² - 2bc·cos(A)
- b² = a² + c² - 2ac·cos(B)

**When to use it:**
- When you know three sides and need an angle (SSS)
- When you know two sides and the included angle (SAS)
- When the Law of Sines doesn't work

**Connection to Pythagorean theorem:** When C = 90°, cos(90°) = 0, so the formula becomes c² = a² + b², which is the Pythagorean theorem!

## How to Use the Law of Cosines

### Finding a side (SAS)
1. **Identify the known parts** - Two sides and the included angle
2. **Choose the right formula** - The unknown side should be on the left
3. **Substitute values** - Plug in the knowns
4. **Calculate** - Evaluate and take square root

### Finding an angle (SSS)
1. **Choose a formula** - Pick the angle you want to find
2. **Rearrange to solve for cos** - Isolate cos(angle)
3. **Substitute** - Plug in all three sides
4. **Use inverse cosine** - Apply cos⁻¹ to find the angle

## Step-by-Step Example

**Find side c:** Triangle with a = 7, b = 10, and C = 50°

### Step 1: Identify the formula needed
We have two sides and the included angle (SAS), need the opposite side:
```
c² = a² + b² - 2ab·cos(C)
```

### Step 2: Substitute the values
Plug in a = 7, b = 10, C = 50°:
```
c² = 7² + 10² - 2(7)(10)·cos(50°)
```

### Step 3: Calculate step by step
Evaluate each part:
```
c² = 49 + 100 - 140·cos(50°)
c² = 149 - 140(0.6428)
c² = 149 - 89.99
c² = 59.01
```

### Step 4: Take the square root
Find c:
```
c = √59.01
c ≈ 7.68
```

### Step 5: Check your answer
Verify with approximate values:
```
c² ≈ 59 ✓
This makes sense: c is between a and b
```

## More Examples

### Example 2: Finding an angle (SSS)
**Find angle A:** Triangle with a = 5, b = 7, c = 9

```
Use formula: a² = b² + c² - 2bc·cos(A)
Rearrange: cos(A) = (b² + c² - a²)/(2bc)

Substitute:
cos(A) = (7² + 9² - 5²)/(2·7·9)
cos(A) = (49 + 81 - 25)/126
cos(A) = 105/126
cos(A) ≈ 0.833

Find A:
A = cos⁻¹(0.833)
A ≈ 33.6°
```

**Check:** cos(33.6°) ≈ 0.833 ✓

### Example 3: Verify Pythagorean theorem
**Check:** Right triangle with a = 3, b = 4, C = 90°

```
c² = a² + b² - 2ab·cos(90°)
c² = 9 + 16 - 2(3)(4)·cos(90°)
c² = 25 - 24(0)
c² = 25
c = 5
```

**Check:** This is the famous 3-4-5 right triangle ✓

### Example 4: Two sides and included angle
**Find c:** a = 12, b = 15, C = 60°

```
c² = 12² + 15² - 2(12)(15)·cos(60°)
c² = 144 + 225 - 360·cos(60°)
c² = 369 - 360(0.5)
c² = 369 - 180
c² = 189
c ≈ 13.7
```

**Check:** c is between the two given sides ✓

## Key Points to Remember

✓ **Works for any triangle** - Right, acute, or obtuse
✓ **Generalizes Pythagorean theorem** - Special case when angle is 90°
✓ **Use with SAS or SSS** - Two sides + included angle, or all three sides
✓ **Choose the right formula** - Pick the one with your unknown
✓ **Included angle** - The angle between the two known sides
✓ **Always gives one solution** - Unlike Law of Sines (no ambiguous case)
✓ **Rearrange to find angles** - Isolate cos(angle) first
✓ **Calculator needed** - For cosine values and square roots

## Common Mistakes to Avoid

❌ **Using wrong formula** - Make sure the angle matches the opposite side
❌ **Forgetting the 2ab term** - The formula is NOT just a² + b²
❌ **Sign errors** - It's minus 2ab·cos(C), not plus
❌ **Wrong rearrangement** - To find angle: cos(A) = (b² + c² - a²)/(2bc)

## Practice More

[Khan Academy: Law of Cosines](https://www.khanacademy.org/math/trigonometry/trig-with-general-triangles/law-of-cosines/v/law-of-cosines)

---

**Next Skills:**
- Law of Sines
- Area of Triangle Using Trig (Heron's Formula)
- Solving Any Triangle
