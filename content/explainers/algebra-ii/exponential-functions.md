# Exponential Functions

## What are Exponential Functions?

An exponential function is a function where the variable appears in the exponent. Unlike polynomial functions where x is the base, exponential functions have x as the power.

Exponential functions model rapid growth or decay, like population growth, radioactive decay, compound interest, and viral spread.

**General form:** f(x) = a · b^x

Where:
- a is the initial value (y-intercept)
- b is the base (growth/decay factor)
- x is the exponent (independent variable)

**Growth vs Decay:**
- If b > 1: exponential growth (increases rapidly)
- If 0 < b < 1: exponential decay (decreases rapidly)

Examples:
- f(x) = 2^x (growth, base 2)
- f(x) = 3 · 2^x (growth, starting at 3)
- f(x) = (1/2)^x (decay, base 1/2)
- f(x) = 100 · (0.8)^x (decay from 100)

## How to Work with Exponential Functions

### Evaluating
1. **Identify a and b** - Find the initial value and base
2. **Substitute x** - Replace x with the given value
3. **Calculate the power** - Evaluate b^x
4. **Multiply by a** - Get the final result

### Graphing
1. **Find the y-intercept** - When x = 0, y = a
2. **Plot key points** - Calculate f(-1), f(0), f(1), f(2)
3. **Draw the curve** - Smooth curve through points
4. **Note the asymptote** - Horizontal line at y = 0 (x-axis)

### Solving Equations
1. **Isolate the exponential term** - Get b^x alone
2. **Use logarithms** - Take log of both sides
3. **Solve for x** - Apply log properties

## Step-by-Step Example

**Evaluate:** f(x) = 3 · 2^x when x = 4

### Step 1: Identify the function components
Initial value a = 3, base b = 2, exponent x = 4
```
f(x) = 3 · 2^x
```

### Step 2: Substitute x = 4
Replace x with 4:
```
f(4) = 3 · 2^4
```

### Step 3: Calculate the power
Evaluate 2^4:
```
2^4 = 2 · 2 · 2 · 2 = 16
```

### Step 4: Multiply by the coefficient
Multiply 3 × 16:
```
f(4) = 3 · 16 = 48
```

### Step 5: Check your answer
Verify the calculation:
```
f(4) = 3 · 2^4 = 3 · 16 = 48 ✓
```

## More Examples

### Example 2: Exponential decay
**Evaluate:** f(x) = 100 · (0.5)^x when x = 3

```
f(3) = 100 · (0.5)^3
     = 100 · (0.5 · 0.5 · 0.5)
     = 100 · 0.125
     = 12.5
```

**Check:** Starting at 100, halving three times: 100 → 50 → 25 → 12.5 ✓

### Example 3: Solve for x
**Solve:** 2^x = 32

```
Recognize that 32 = 2^5:
2^x = 2^5

If bases are equal, exponents are equal:
x = 5
```

**Check:** 2^5 = 32 ✓

### Example 4: Growth problem
**Problem:** A bacteria population doubles every hour. Starting with 50 bacteria, how many after 5 hours?

```
f(x) = 50 · 2^x, where x = hours
f(5) = 50 · 2^5
     = 50 · 32
     = 1,600 bacteria
```

**Check:** 50 → 100 → 200 → 400 → 800 → 1,600 ✓

## Key Points to Remember

✓ **Variable is in the exponent** - That's what makes it exponential
✓ **Base b must be positive** - b > 0 and b ≠ 1
✓ **Growth when b > 1** - Function increases as x increases
✓ **Decay when 0 < b < 1** - Function decreases as x increases
✓ **Y-intercept is always a** - When x = 0, b^0 = 1, so f(0) = a
✓ **Never touches x-axis** - Horizontal asymptote at y = 0
✓ **Domain is all real numbers** - Can plug in any x value
✓ **Range is y > 0** - Output is always positive (if a > 0)

## Common Mistakes to Avoid

❌ **Confusing with power functions** - x^2 is power, 2^x is exponential
❌ **Wrong order of operations** - Calculate exponent before multiplying by a
❌ **Negative outputs** - With positive a and b, exponentials are always positive
❌ **Forgetting the y-intercept** - f(0) = a, not 0

## Practice More

[Khan Academy: Exponential Functions](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:exp/x2ec2f6f830c9fb89:exp-intro/v/exponential-growth-functions)

---

**Next Skills:**
- Logarithmic Functions (inverse of exponentials)
- Solving Exponential Equations
- Applications of Exponential Growth and Decay
