# Inverse Functions

## What are Inverse Functions?

An inverse function "undoes" what the original function does. If function f takes x to y, then the inverse function f⁻¹ takes y back to x.

**Notation:** f⁻¹(x) (read as "f inverse of x")

**Important:** f⁻¹ does NOT mean 1/f. It's the inverse function, not the reciprocal.

**Key relationship:** f(f⁻¹(x)) = x and f⁻¹(f(x)) = x

**How to identify:**
- If f takes a → b, then f⁻¹ takes b → a
- The graph of f⁻¹ is the reflection of f over the line y = x
- Not all functions have inverses (must be one-to-one)

**One-to-one function:** A function where each output comes from exactly one input. Use the horizontal line test - if any horizontal line crosses the graph more than once, it's not one-to-one.

Examples:
- If f(x) = 2x, then f⁻¹(x) = x/2
- If f(x) = x + 3, then f⁻¹(x) = x - 3
- If f(x) = x³, then f⁻¹(x) = ∛x

## How to Find Inverse Functions

### Method: Switch and solve
1. **Replace f(x) with y** - Write y = f(x)
2. **Switch x and y** - Swap their positions
3. **Solve for y** - Isolate y on one side
4. **Replace y with f⁻¹(x)** - Write the inverse function
5. **Verify** - Check that f(f⁻¹(x)) = x

## Step-by-Step Example

**Find the inverse:** f(x) = 3x - 5

### Step 1: Replace f(x) with y
```
y = 3x - 5
```

### Step 2: Switch x and y
Swap every x with y and every y with x:
```
x = 3y - 5
```

### Step 3: Solve for y
Add 5 to both sides:
```
x + 5 = 3y
```

Divide by 3:
```
(x + 5)/3 = y
y = (x + 5)/3
```

### Step 4: Write as inverse function
Replace y with f⁻¹(x):
```
f⁻¹(x) = (x + 5)/3
```

### Step 5: Check your answer
Verify f(f⁻¹(x)) = x:
```
f(f⁻¹(x)) = f((x + 5)/3)
          = 3((x + 5)/3) - 5
          = x + 5 - 5
          = x ✓
```

## More Examples

### Example 2: Inverse with fraction
**Find f⁻¹(x):** f(x) = (2x + 1)/3

```
Step 1: y = (2x + 1)/3
Step 2: x = (2y + 1)/3
Step 3: 3x = 2y + 1
        3x - 1 = 2y
        y = (3x - 1)/2
Step 4: f⁻¹(x) = (3x - 1)/2
```

**Check:** f(f⁻¹(x)) = (2·(3x-1)/2 + 1)/3 = (3x - 1 + 1)/3 = 3x/3 = x ✓

### Example 3: Inverse with square root
**Find f⁻¹(x):** f(x) = √(x - 2) for x ≥ 2

```
Step 1: y = √(x - 2)
Step 2: x = √(y - 2)
Step 3: x² = y - 2
        y = x² + 2
Step 4: f⁻¹(x) = x² + 2, for x ≥ 0
```

**Check:** f(f⁻¹(x)) = √((x² + 2) - 2) = √(x²) = x for x ≥ 0 ✓

### Example 4: Verifying inverses
**Verify f⁻¹(x) = (x - 4)/2 is the inverse of f(x) = 2x + 4**

```
Check f(f⁻¹(x)):
f(f⁻¹(x)) = f((x - 4)/2)
          = 2((x - 4)/2) + 4
          = x - 4 + 4
          = x ✓

Check f⁻¹(f(x)):
f⁻¹(f(x)) = f⁻¹(2x + 4)
          = ((2x + 4) - 4)/2
          = 2x/2
          = x ✓
```

**Both checks pass, so they are inverses ✓**

## Key Points to Remember

✓ **Switch and solve method** - Always works for finding inverses
✓ **f⁻¹ undoes f** - They cancel each other out
✓ **One-to-one requirement** - Use horizontal line test
✓ **Domain becomes range** - And vice versa
✓ **Reflection over y = x** - Graphs are mirror images
✓ **Verify your answer** - Check that f(f⁻¹(x)) = x
✓ **f⁻¹ ≠ 1/f** - Inverse function is NOT reciprocal
✓ **Restrict domain if needed** - Some functions need restrictions to be one-to-one

## Common Mistakes to Avoid

❌ **Confusing with reciprocal** - f⁻¹(x) is not 1/f(x)
❌ **Not switching x and y** - This step is essential
❌ **Forgetting to solve for y** - Must isolate y completely
❌ **Skipping verification** - Always check your answer

## Practice More

[Khan Academy: Inverse Functions](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:composite/x9e81a4f98389efdf:invertible/v/function-inverses-example-1)

---

**Next Skills:**
- Graphing Inverse Functions
- Restricting Domains for Inverses
- Inverse Trigonometric Functions
