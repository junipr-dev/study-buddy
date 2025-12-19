# Logarithmic Functions

## What are Logarithmic Functions?

A logarithmic function is the inverse of an exponential function. While exponentials ask "what's b to the x power?", logarithms ask "what power do I raise b to get x?"

**Definition:** If b^y = x, then log_b(x) = y

**General form:** f(x) = log_b(x)

Where:
- b is the base (must be positive, not equal to 1)
- x is the input (must be positive)
- The output is the exponent you need

**Special logarithms:**
- log(x) or log₁₀(x) = common logarithm (base 10)
- ln(x) = natural logarithm (base e ≈ 2.718)

Examples:
- log₂(8) = 3 because 2³ = 8
- log₁₀(100) = 2 because 10² = 100
- ln(e) = 1 because e¹ = e
- log₅(1) = 0 because 5⁰ = 1

## How to Evaluate Logarithms

### Method 1: Convert to exponential form
1. **Write as an equation** - Let log_b(x) = y
2. **Convert to exponential** - Rewrite as b^y = x
3. **Solve for y** - Find what power gives you x
4. **State the answer** - That exponent is the logarithm

### Method 2: Use log properties
1. **Product rule** - log_b(xy) = log_b(x) + log_b(y)
2. **Quotient rule** - log_b(x/y) = log_b(x) - log_b(y)
3. **Power rule** - log_b(x^n) = n · log_b(x)
4. **Change of base** - log_b(x) = log(x)/log(b)

## Step-by-Step Example

**Evaluate:** log₂(16)

### Step 1: Set up the equation
Let y = log₂(16), which asks: "2 to what power equals 16?"
```
y = log₂(16)
```

### Step 2: Convert to exponential form
Rewrite using the definition of logarithm:
```
2^y = 16
```

### Step 3: Find the exponent
Determine what power of 2 equals 16:
```
2¹ = 2
2² = 4
2³ = 8
2⁴ = 16
```

### Step 4: State the answer
Since 2⁴ = 16:
```
y = 4
log₂(16) = 4
```

### Step 5: Check your answer
Verify by computing 2⁴:
```
2⁴ = 16 ✓
```

## More Examples

### Example 2: Base 10 logarithm
**Evaluate:** log₁₀(1000)

```
Let y = log₁₀(1000)
10^y = 1000
10¹ = 10
10² = 100
10³ = 1000

Therefore: log₁₀(1000) = 3
```

**Check:** 10³ = 1000 ✓

### Example 3: Using log properties
**Simplify:** log₃(27) + log₃(3)

```
Use product rule: log_b(x) + log_b(y) = log_b(xy)
log₃(27) + log₃(3) = log₃(27 × 3)
                    = log₃(81)

Evaluate: 3^y = 81
3⁴ = 81, so y = 4

Answer: 4
```

**Check:** log₃(27) = 3 (since 3³ = 27), log₃(3) = 1 (since 3¹ = 3), and 3 + 1 = 4 ✓

### Example 4: Solving an equation
**Solve:** log₅(x) = 3

```
Convert to exponential form:
5³ = x
125 = x
```

**Check:** log₅(125) = 3 because 5³ = 125 ✓

## Key Points to Remember

✓ **Logarithms are exponents** - log_b(x) asks "what power?"
✓ **Inverse of exponential** - log_b(b^x) = x and b^(log_b(x)) = x
✓ **x must be positive** - Can't take log of negative numbers or zero
✓ **log_b(1) = 0** - Any base to the zero power equals 1
✓ **log_b(b) = 1** - The base to the first power equals itself
✓ **Product becomes sum** - log_b(xy) = log_b(x) + log_b(y)
✓ **Quotient becomes difference** - log_b(x/y) = log_b(x) - log_b(y)
✓ **Power becomes product** - log_b(x^n) = n · log_b(x)

## Common Mistakes to Avoid

❌ **Taking log of negative numbers** - Domain is only positive numbers
❌ **Forgetting to convert to exponential** - Use b^y = x to solve
❌ **Confusing log rules** - Product is addition, not multiplication
❌ **Wrong order in quotient rule** - log(x/y) = log(x) - log(y), not reversed

## Practice More

[Khan Academy: Logarithmic Functions](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs/x2ec2f6f830c9fb89:log-intro/v/logarithms)

---

**Next Skills:**
- Properties of Logarithms (expanding and condensing)
- Solving Logarithmic Equations
- Change of Base Formula
