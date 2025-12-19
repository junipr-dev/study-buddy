# Matrices

## What are Matrices?

A matrix is a rectangular array of numbers arranged in rows and columns. Matrices are used to organize data, solve systems of equations, and represent transformations.

**Notation:** A matrix is written in brackets with rows and columns:
```
A = [a₁₁  a₁₂  a₁₃]
    [a₂₁  a₂₂  a₂₃]
```

**Dimensions:** An m × n matrix has m rows and n columns.

**Types of matrices:**
- **Square matrix:** Same number of rows and columns (n × n)
- **Row matrix:** 1 × n matrix (one row)
- **Column matrix:** m × 1 matrix (one column)
- **Identity matrix (I):** Square matrix with 1's on diagonal, 0's elsewhere
- **Zero matrix:** All entries are 0

**Applications:**
- Solving systems of equations
- Computer graphics and transformations
- Data organization and statistics
- Network analysis and graphs

Examples:
```
2×3 matrix: [1  2  3]
            [4  5  6]

Identity:   [1  0  0]
            [0  1  0]
            [0  0  1]
```

## How to Work with Matrices

### Matrix addition
Add corresponding entries: (A + B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ
- **Requirement:** Same dimensions

### Scalar multiplication
Multiply each entry by the scalar: (kA)ᵢⱼ = k·Aᵢⱼ

### Matrix multiplication
For A (m × n) and B (n × p):
- **Result:** C is m × p
- **Entry:** Cᵢⱼ = sum of (row i of A) × (column j of B)
- **Requirement:** Columns of A = Rows of B

## Step-by-Step Example

**Add matrices:** A = [1  2] and B = [5  6]
                      [3  4]         [7  8]

### Step 1: Check dimensions
Both are 2×2 matrices:
```
A is 2×2 ✓
B is 2×2 ✓
Same dimensions, can add
```

### Step 2: Add corresponding entries
Row 1: Add first row of A to first row of B:
```
[1+5  2+6] = [6  8]
```

Row 2: Add second row of A to second row of B:
```
[3+7  4+8] = [10  12]
```

### Step 3: Write the result
```
A + B = [6   8]
        [10  12]
```

### Step 4: Check your answer
Verify a few entries:
```
Top-left: 1 + 5 = 6 ✓
Bottom-right: 4 + 8 = 12 ✓
```

## More Examples

### Example 2: Scalar multiplication
**Multiply:** 3·[2  -1]
               [0   4]

```
Multiply each entry by 3:
3·[2  -1] = [3·2   3·(-1)] = [6  -3]
  [0   4]   [3·0   3·4]     [0  12]
```

**Check:** Each entry is 3 times the original ✓

### Example 3: Matrix multiplication
**Multiply:** [1  2] · [5  6]
              [3  4]   [7  8]

```
Result will be 2×2

Entry (1,1): 1·5 + 2·7 = 5 + 14 = 19
Entry (1,2): 1·6 + 2·8 = 6 + 16 = 22
Entry (2,1): 3·5 + 4·7 = 15 + 28 = 43
Entry (2,2): 3·6 + 4·8 = 18 + 32 = 50

Result: [19  22]
        [43  50]
```

**Check:** Dimensions work: 2×2 · 2×2 = 2×2 ✓

### Example 4: Identity matrix property
**Multiply by identity:** [2  3] · [1  0]
                         [4  5]   [0  1]

```
Entry (1,1): 2·1 + 3·0 = 2
Entry (1,2): 2·0 + 3·1 = 3
Entry (2,1): 4·1 + 5·0 = 4
Entry (2,2): 4·0 + 5·1 = 5

Result: [2  3] (unchanged)
        [4  5]
```

**Check:** A·I = A ✓ (identity property works)

## Key Points to Remember

✓ **Dimensions must match for addition** - Can't add different sizes
✓ **Matrix multiplication is not commutative** - AB ≠ BA in general
✓ **Row × Column** - Multiply row entries by column entries and sum
✓ **Dimensions rule for multiplication** - (m×n)(n×p) = (m×p)
✓ **Identity matrix is like 1** - A·I = I·A = A
✓ **Order matters** - Position of rows and columns is crucial
✓ **Scalar multiplies all entries** - Every entry gets multiplied
✓ **Add entry by entry** - Corresponding positions

## Common Mistakes to Avoid

❌ **Adding different dimensions** - Must be same size
❌ **Wrong multiplication order** - AB and BA can be different or one undefined
❌ **Incorrect row × column** - Must sum all products, not just multiply corresponding entries
❌ **Forgetting dimension check** - For AB, columns of A must equal rows of B

## Practice More

[Khan Academy: Matrices](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:mat-intro/v/introduction-to-matrices)

---

**Next Skills:**
- Determinants
- Inverse Matrices
- Solving Systems with Matrices
- Matrix Transformations
