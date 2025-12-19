# Function Composition

## What is Function Composition?

Function composition is the process of applying one function to the result of another function. It's like a chain of operations where the output of one function becomes the input of the next.

**Notation:** (f ∘ g)(x) = f(g(x))

This reads as "f composed with g of x" or "f of g of x."

**How it works:**
1. Start with input x
2. Apply function g to get g(x)
3. Apply function f to that result to get f(g(x))

**Order matters!** f(g(x)) is usually different from g(f(x)).

Examples:
- If f(x) = x² and g(x) = x + 1, then f(g(x)) = (x + 1)²
- If f(x) = 2x and g(x) = x + 3, then f(g(x)) = 2(x + 3) = 2x + 6

## How to Compose Functions

### Finding f(g(x))
1. **Identify the inner function** - This is g(x)
2. **Substitute g(x) into f** - Replace every x in f with g(x)
3. **Simplify** - Expand and combine like terms
4. **Write the result** - As a single expression

### Evaluating at a specific value
1. **Work from inside out** - Evaluate g(x) first
2. **Use that result** - Plug it into f
3. **Calculate the final answer**

## Step-by-Step Example

**Find (f ∘ g)(x):** If f(x) = 2x - 1 and g(x) = x²

### Step 1: Set up the composition
Write f(g(x)), which means "replace x in f with g(x)":
```
f(g(x)) = f(x²)
```

### Step 2: Substitute g(x) into f
Take the formula for f and replace every x with x²:
```
f(x) = 2x - 1
f(x²) = 2(x²) - 1
```

### Step 3: Simplify
Expand if needed:
```
f(g(x)) = 2x² - 1
```

### Step 4: Check your answer
Try a test value, like x = 2:
```
g(2) = 2² = 4
f(4) = 2(4) - 1 = 7
Using composition: f(g(2)) = 2(2²) - 1 = 2(4) - 1 = 7 ✓
```

## More Examples

### Example 2: Reverse composition
**Find (g ∘ f)(x):** If f(x) = 2x - 1 and g(x) = x²

```
g(f(x)) = g(2x - 1)
        = (2x - 1)²
        = 4x² - 4x + 1
```

**Check:** This is different from f(g(x)) = 2x² - 1 ✓ (order matters!)

### Example 3: Evaluate at a point
**Find f(g(3)):** If f(x) = x + 5 and g(x) = 2x

```
Method 1 (work inside out):
g(3) = 2(3) = 6
f(6) = 6 + 5 = 11

Method 2 (find composition first):
f(g(x)) = f(2x) = 2x + 5
f(g(3)) = 2(3) + 5 = 11
```

**Check:** Both methods give 11 ✓

### Example 4: Three function composition
**Find f(g(h(x))):** If f(x) = x², g(x) = x + 1, h(x) = 2x

```
Work from inside out:
h(x) = 2x
g(h(x)) = g(2x) = 2x + 1
f(g(h(x))) = f(2x + 1) = (2x + 1)²
           = 4x² + 4x + 1
```

**Check:** With x = 1: h(1) = 2, g(2) = 3, f(3) = 9, and 4(1)² + 4(1) + 1 = 9 ✓

## Key Points to Remember

✓ **Inside out** - Always work from the innermost function outward
✓ **Order matters** - f(g(x)) ≠ g(f(x)) in general
✓ **Substitute completely** - Replace every instance of x
✓ **Simplify after substituting** - Expand and combine like terms
✓ **Check domains** - The composition might have a different domain
✓ **Notation clarity** - (f ∘ g)(x) is the same as f(g(x))
✓ **Not multiplication** - f(g(x)) doesn't mean f times g

## Common Mistakes to Avoid

❌ **Wrong order** - f(g(x)) means g first, then f (inside out)
❌ **Incomplete substitution** - Must replace all x's with the entire function g(x)
❌ **Treating as multiplication** - f(g(x)) ≠ f(x) · g(x)
❌ **Not simplifying** - Always expand and combine terms

## Practice More

[Khan Academy: Function Composition](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:composite/x9e81a4f98389efdf:composing/v/function-composition)

---

**Next Skills:**
- Inverse Functions
- Decomposing Functions
- Domain of Composite Functions
