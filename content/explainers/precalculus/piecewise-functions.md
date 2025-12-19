# Piecewise Functions

## What are Piecewise Functions?

A piecewise function is a function defined by different formulas for different parts of its domain. It's like having multiple rules depending on the input value.

**General form:**
```
f(x) = { formula 1,  if condition 1
       { formula 2,  if condition 2
       { formula 3,  if condition 3
```

**Real-world examples:**
- Tax brackets (different rates for different income levels)
- Shipping costs (different rates for different weights)
- Parking fees (different rates for different time periods)

**Common example - Absolute value:**
```
|x| = { x,   if x ≥ 0
      { -x,  if x < 0
```

**Types of piecewise functions:**
- Continuous - No breaks or jumps in the graph
- Discontinuous - Has breaks, jumps, or gaps

## How to Work with Piecewise Functions

### Evaluating at a point
1. **Identify the condition** - Which piece applies to your x value?
2. **Use that formula** - Apply only the appropriate rule
3. **Calculate** - Evaluate the expression

### Graphing
1. **Graph each piece separately** - Over its specified domain
2. **Check endpoints** - Use open/closed circles correctly
3. **Look for continuity** - Check where pieces meet
4. **Combine** - Put all pieces on one graph

### Finding domain and range
1. **Domain** - Usually all real numbers (unless stated)
2. **Range** - Find the output values from each piece

## Step-by-Step Example

**Evaluate f(3) and f(-2):**
```
f(x) = { x + 1,   if x < 0
       { 2x,      if 0 ≤ x < 4
       { x²,      if x ≥ 4
```

### Step 1: Evaluate f(3)
Check which condition 3 satisfies:
```
Is 3 < 0? No
Is 0 ≤ 3 < 4? Yes ✓
Is 3 ≥ 4? No

Use the second piece: f(x) = 2x
```

### Step 2: Calculate f(3)
Apply the formula:
```
f(3) = 2(3) = 6
```

### Step 3: Evaluate f(-2)
Check which condition -2 satisfies:
```
Is -2 < 0? Yes ✓
Is 0 ≤ -2 < 4? No
Is -2 ≥ 4? No

Use the first piece: f(x) = x + 1
```

### Step 4: Calculate f(-2)
Apply the formula:
```
f(-2) = -2 + 1 = -1
```

### Step 5: Check your answers
Verify the conditions:
```
f(3) = 6 using the middle piece ✓
f(-2) = -1 using the first piece ✓
```

## More Examples

### Example 2: Absolute value
**Evaluate |5| and |-3|**

```
|x| = { x,   if x ≥ 0
      { -x,  if x < 0

For x = 5:
5 ≥ 0, so use first piece: |5| = 5

For x = -3:
-3 < 0, so use second piece: |-3| = -(-3) = 3
```

**Check:** Distance from 0 is 5 and 3 respectively ✓

### Example 3: Tax bracket example
**Find tax on $50,000:**

```
Tax(x) = { 0.10x,           if 0 ≤ x ≤ 10000
         { 1000 + 0.15(x-10000), if x > 10000

50,000 > 10,000, so use second piece:
Tax(50000) = 1000 + 0.15(50000 - 10000)
           = 1000 + 0.15(40000)
           = 1000 + 6000
           = $7,000
```

**Check:** First $10k taxed at 10% ($1,000), next $40k at 15% ($6,000) ✓

### Example 4: Continuity check
**Is this function continuous at x = 2?**

```
f(x) = { x + 1,  if x < 2
       { 2x - 1, if x ≥ 2

Check left side (approaching from below):
lim (x→2⁻) f(x) = 2 + 1 = 3

Check right side (at and approaching from above):
f(2) = 2(2) - 1 = 3

Both equal 3, so it IS continuous at x = 2
```

**Check:** No jump or break at x = 2 ✓

## Key Points to Remember

✓ **Check the condition first** - Determine which piece to use
✓ **Use only one formula** - Don't mix pieces
✓ **Pay attention to inequalities** - < vs ≤ matters at boundaries
✓ **Open vs closed circles** - < or > means open, ≤ or ≥ means closed
✓ **Domain is usually all reals** - Unless pieces have restrictions
✓ **Each piece is simpler** - Handle each part separately
✓ **Check continuity** - Look at where pieces meet
✓ **Real-world applications** - Many scenarios use piecewise functions

## Common Mistakes to Avoid

❌ **Using wrong piece** - Always check which condition applies
❌ **Ignoring boundary conditions** - Pay careful attention to < vs ≤
❌ **Mixing formulas** - Only use the appropriate piece
❌ **Graphing errors** - Use open circles for < or >, closed for ≤ or ≥

## Practice More

[Khan Academy: Piecewise Functions](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:piecewise/x9e81a4f98389efdf:piecewise-intro/v/piecewise-functions)

---

**Next Skills:**
- Continuity and Discontinuity
- Step Functions
- Absolute Value Functions
