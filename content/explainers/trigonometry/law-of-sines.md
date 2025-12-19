# Law of Sines

## What is the Law of Sines?

The Law of Sines is a formula that relates the sides and angles of any triangle (not just right triangles). It states that the ratio of each side to the sine of its opposite angle is constant.

**Formula:** a/sin(A) = b/sin(B) = c/sin(C)

Where:
- a, b, c are the sides of the triangle
- A, B, C are the angles opposite those sides

**When to use it:**
- When you know two angles and one side (AAS or ASA)
- When you know two sides and an angle opposite one of them (SSA)

The Law of Sines is especially useful for solving oblique triangles (triangles without a right angle).

Examples of when to apply:
- Finding a missing side when you know two angles and one side
- Finding a missing angle when you know two sides and an angle
- Navigation and surveying problems

## How to Use the Law of Sines

### Finding a side
1. **Write the formula** - a/sin(A) = b/sin(B) = c/sin(C)
2. **Choose the right ratio** - Pick two fractions with three knowns and one unknown
3. **Cross multiply** - Solve the proportion
4. **Calculate** - Use calculator for sine values

### Finding an angle
1. **Set up the proportion** - Choose the correct ratio
2. **Solve for the sine** - Isolate sin(angle)
3. **Use inverse sine** - Apply sin⁻¹ to find the angle
4. **Check for ambiguous case** - SSA might have two solutions

## Step-by-Step Example

**Find side b:** Triangle ABC where A = 40°, C = 75°, and a = 10

### Step 1: Find the missing angle
Sum of angles in a triangle = 180°:
```
A + B + C = 180°
40° + B + 75° = 180°
B = 180° - 115°
B = 65°
```

### Step 2: Set up the Law of Sines
Use the ratio with known values:
```
a/sin(A) = b/sin(B)
10/sin(40°) = b/sin(65°)
```

### Step 3: Solve for b
Cross multiply:
```
b · sin(40°) = 10 · sin(65°)
b = (10 · sin(65°))/sin(40°)
```

### Step 4: Calculate
Use calculator:
```
b = (10 · 0.9063)/0.6428
b = 9.063/0.6428
b ≈ 14.1
```

### Step 5: Check your answer
Verify the ratios are equal:
```
10/sin(40°) ≈ 15.56
14.1/sin(65°) ≈ 15.56 ✓
```

## More Examples

### Example 2: Finding an angle
**Find angle B:** Triangle where a = 8, b = 10, A = 35°

```
Set up Law of Sines:
a/sin(A) = b/sin(B)
8/sin(35°) = 10/sin(B)

Solve for sin(B):
sin(B) = (10 · sin(35°))/8
sin(B) = (10 · 0.5736)/8
sin(B) = 0.717

Find B:
B = sin⁻¹(0.717)
B ≈ 45.8°
```

**Check:** 8/sin(35°) ≈ 13.95 and 10/sin(45.8°) ≈ 13.94 ✓

### Example 3: Complete triangle
**Given:** A = 30°, B = 45°, a = 7. Find b and c.

```
Find C: C = 180° - 30° - 45° = 105°

Find b:
7/sin(30°) = b/sin(45°)
b = (7 · sin(45°))/sin(30°)
b = (7 · 0.7071)/0.5
b ≈ 9.9

Find c:
7/sin(30°) = c/sin(105°)
c = (7 · sin(105°))/sin(30°)
c = (7 · 0.9659)/0.5
c ≈ 13.5
```

**Check:** All ratios equal 14 ✓

## Key Points to Remember

✓ **Works for any triangle** - Not just right triangles
✓ **Opposite pairs** - Each side pairs with its opposite angle
✓ **Need three pieces** - To find the fourth
✓ **All ratios are equal** - You can use any two fractions
✓ **Find missing angle first** - If you need it (angles sum to 180°)
✓ **Calculator needed** - For sine values that aren't special angles
✓ **Units matter** - Make sure angles are in degrees or radians consistently
✓ **Ambiguous case (SSA)** - May have 0, 1, or 2 solutions

## Common Mistakes to Avoid

❌ **Wrong opposite pairs** - Side a is opposite angle A, not adjacent
❌ **Forgetting to find all angles first** - Sometimes you need to find angle B before finding side b
❌ **Calculator mode** - Make sure you're in degree mode (or radian if using radians)
❌ **Ignoring ambiguous case** - With SSA, check if there's a second solution

## Practice More

[Khan Academy: Law of Sines](https://www.khanacademy.org/math/trigonometry/trig-with-general-triangles/law-of-sines/v/law-of-sines)

---

**Next Skills:**
- Law of Cosines
- Ambiguous Case (SSA)
- Area of a Triangle Using Trig
