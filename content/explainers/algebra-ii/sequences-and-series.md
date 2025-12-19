# Sequences and Series

## What are Sequences and Series?

A **sequence** is an ordered list of numbers following a pattern. Each number in the sequence is called a **term**.

A **series** is the sum of the terms in a sequence.

**Types of sequences:**
- **Arithmetic sequence** - Add the same number each time (common difference)
- **Geometric sequence** - Multiply by the same number each time (common ratio)

Examples:
- Arithmetic: 2, 5, 8, 11, 14 (add 3 each time)
- Geometric: 3, 6, 12, 24, 48 (multiply by 2 each time)
- Series: 2 + 5 + 8 + 11 + 14 = 40

## Arithmetic Sequences

**General form:** aₙ = a₁ + (n - 1)d

Where:
- aₙ = the nth term
- a₁ = first term
- n = term number
- d = common difference

**Sum formula:** Sₙ = (n/2)(a₁ + aₙ)

## Geometric Sequences

**General form:** aₙ = a₁ · r^(n-1)

Where:
- aₙ = the nth term
- a₁ = first term
- n = term number
- r = common ratio

**Sum formula:** Sₙ = a₁(1 - r^n)/(1 - r) when r ≠ 1

## Step-by-Step Example

**Find the 10th term:** Arithmetic sequence 3, 7, 11, 15...

### Step 1: Identify the pattern
Find the common difference:
```
7 - 3 = 4
11 - 7 = 4
15 - 11 = 4
d = 4 (adding 4 each time)
```

### Step 2: Identify the first term
The first term is given:
```
a₁ = 3
```

### Step 3: Use the formula
Apply aₙ = a₁ + (n - 1)d with n = 10:
```
a₁₀ = 3 + (10 - 1) · 4
```

### Step 4: Calculate
Simplify step by step:
```
a₁₀ = 3 + 9 · 4
a₁₀ = 3 + 36
a₁₀ = 39
```

### Step 5: Check your answer
Count the pattern forward: 3, 7, 11, 15, 19, 23, 27, 31, 35, 39
```
The 10th term is 39 ✓
```

## More Examples

### Example 2: Geometric sequence
**Find the 6th term:** 2, 6, 18, 54...

```
Find common ratio: 6/2 = 3, 18/6 = 3
r = 3, a₁ = 2

Use formula: aₙ = a₁ · r^(n-1)
a₆ = 2 · 3^(6-1)
a₆ = 2 · 3⁵
a₆ = 2 · 243
a₆ = 486
```

**Check:** 2, 6, 18, 54, 162, 486 (multiply by 3 each time) ✓

### Example 3: Sum of arithmetic series
**Find the sum:** First 10 terms of 5, 8, 11, 14...

```
First term: a₁ = 5
Common difference: d = 3
10th term: a₁₀ = 5 + (10-1)·3 = 5 + 27 = 32

Sum formula: Sₙ = (n/2)(a₁ + aₙ)
S₁₀ = (10/2)(5 + 32)
S₁₀ = 5 · 37
S₁₀ = 185
```

**Check:** Add first few: 5 + 8 + 11 + 14 + 17 + 20 + 23 + 26 + 29 + 32 = 185 ✓

### Example 4: Geometric series
**Find the sum:** First 5 terms of 1, 2, 4, 8...

```
First term: a₁ = 1
Common ratio: r = 2
Number of terms: n = 5

Sum formula: Sₙ = a₁(1 - r^n)/(1 - r)
S₅ = 1(1 - 2⁵)/(1 - 2)
S₅ = (1 - 32)/(-1)
S₅ = -31/(-1)
S₅ = 31
```

**Check:** 1 + 2 + 4 + 8 + 16 = 31 ✓

## Key Points to Remember

✓ **Arithmetic: constant difference** - Add the same amount each time
✓ **Geometric: constant ratio** - Multiply by the same factor each time
✓ **Sequence vs series** - Sequence is the list, series is the sum
✓ **Check the pattern** - Always verify the common difference or ratio
✓ **Formula shortcuts** - Use formulas instead of counting all terms
✓ **Sum formulas save time** - Especially for large numbers of terms
✓ **Index carefully** - First term is a₁, not a₀

## Common Mistakes to Avoid

❌ **Wrong formula** - Use arithmetic formula for arithmetic sequences, geometric for geometric
❌ **Off-by-one errors** - Remember n = 1 for the first term
❌ **Confusing d and r** - d is difference (add), r is ratio (multiply)
❌ **Forgetting the pattern** - Always check multiple terms to confirm the pattern

## Practice More

[Khan Academy: Sequences and Series](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:seq/x2ec2f6f830c9fb89:seq-intro/v/introduction-to-arithmetic-sequences)

---

**Next Skills:**
- Infinite Geometric Series
- Sigma Notation
- Recursive Sequences
