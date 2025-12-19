# Content Writing Delegation Brief

**For:** Codex or Gemini Agent
**Task:** Write educational explainers for math skills (pre-algebra → precalculus)
**Format:** Markdown files following template
**Quantity:** 45-95 skill explainers
**Timeline:** Async (can be done in batches)

---

## Instructions for Codex/Gemini

### What to Do

Write clear, educational explainers for math skills covering:
- Pre-Algebra (15-20 skills)
- Algebra Basics (10-15 skills)
- Algebra I (15-20 skills)
- Algebra II (15-20 skills)
- Trigonometry (10-15 skills)
- Precalculus (10-15 skills)

### Template Location

**Template:** `/home/jesse/school/study-buddy/content/EXPLAINER-TEMPLATE.md`

### Examples to Follow

**Example 1:** `content/explainers/algebra-basics/solving-linear-equations.md`
**Example 2:** `content/explainers/pre-algebra/fraction-addition.md`

### Format Requirements

Each explainer must include:
1. **What is [Concept]?** - Clear definition (1-2 sentences)
2. **How to Solve** - Step-by-step method (numbered list)
3. **Step-by-Step Example** - Full worked example with explanation
4. **More Examples** - 2-3 additional examples
5. **Key Points to Remember** - Bullet list with ✓
6. **Common Mistakes to Avoid** - Bullet list with ❌
7. **Practice More** - Link to Khan Academy
8. **Next Skills** - Related topics

### Style Guidelines

- **Reading Level:** 8th-10th grade
- **Length:** 200-400 words (excluding examples)
- **Tone:** Clear, friendly, educational
- **Math Notation:** Use code blocks for equations
- **Formatting:** Use bold, bullets, headers
- **Language:** Simple, avoid jargon

### File Naming Convention

Save as: `content/explainers/{subject}/{skill-slug}.md`

**Subjects:**
- `pre-algebra/`
- `algebra-basics/`
- `algebra-1/`
- `algebra-2/`
- `trigonometry/`
- `precalculus/`

**Skill slugs:** Use kebab-case (e.g., `solving-quadratic-equations.md`)

---

## Skills to Cover

### Priority 1: Core Algebra Skills (Start Here)

#### Algebra Basics
- [ ] `distributive-property.md` - Distributive Property
- [ ] `order-of-operations.md` - Order of Operations (PEMDAS)
- [ ] `evaluating-expressions.md` - Evaluating Algebraic Expressions
- [ ] `combining-like-terms.md` - Combining Like Terms (already seeded in DB, need explainer)
- [ ] `equations-with-variables-both-sides.md` - Variables on Both Sides

#### Algebra I
- [ ] `solving-inequalities.md` - Solving Linear Inequalities
- [ ] `graphing-linear-equations.md` - Graphing Linear Equations
- [ ] `slope-intercept-form.md` - Slope-Intercept Form (y = mx + b)
- [ ] `point-slope-form.md` - Point-Slope Form
- [ ] `systems-of-equations.md` - Solving Systems of Equations
- [ ] `solving-quadratic-equations.md` - Solving Quadratic Equations
- [ ] `factoring-quadratics.md` - Factoring Quadratic Expressions
- [ ] `quadratic-formula.md` - The Quadratic Formula
- [ ] `exponent-rules.md` - Laws of Exponents
- [ ] `scientific-notation.md` - Scientific Notation

### Priority 2: Pre-Algebra Foundations

#### Pre-Algebra
- [ ] `integers-operations.md` - Operations with Integers
- [ ] `absolute-value.md` - Absolute Value
- [ ] `fractions-multiplication.md` - Multiplying Fractions
- [ ] `fractions-division.md` - Dividing Fractions
- [ ] `decimals-operations.md` - Operations with Decimals
- [ ] `percentages.md` - Percentages and Applications
- [ ] `ratios-proportions.md` - Ratios and Proportions
- [ ] `unit-conversions.md` - Unit Conversions
- [ ] `simple-interest.md` - Simple Interest
- [ ] `pythagorean-theorem.md` - Pythagorean Theorem

### Priority 3: Algebra II

#### Algebra II
- [ ] `polynomial-operations.md` - Polynomial Operations
- [ ] `factoring-polynomials.md` - Factoring Polynomials
- [ ] `rational-expressions.md` - Simplifying Rational Expressions
- [ ] `radical-expressions.md` - Simplifying Radical Expressions
- [ ] `complex-numbers.md` - Complex Numbers
- [ ] `exponential-functions.md` - Exponential Functions
- [ ] `logarithms.md` - Logarithms and Properties
- [ ] `sequences-series.md` - Sequences and Series

### Priority 4: Trigonometry

#### Trigonometry
- [ ] `unit-circle.md` - The Unit Circle
- [ ] `sine-cosine-tangent.md` - Basic Trig Ratios (SOH CAH TOA)
- [ ] `right-triangle-trig.md` - Right Triangle Trigonometry
- [ ] `trig-identities.md` - Basic Trigonometric Identities
- [ ] `graphing-trig-functions.md` - Graphing Sine and Cosine
- [ ] `inverse-trig.md` - Inverse Trig Functions
- [ ] `law-of-sines.md` - Law of Sines
- [ ] `law-of-cosines.md` - Law of Cosines

### Priority 5: Precalculus

#### Precalculus
- [ ] `function-notation.md` - Function Notation
- [ ] `function-composition.md` - Composition of Functions
- [ ] `inverse-functions.md` - Inverse Functions
- [ ] `domain-range.md` - Domain and Range
- [ ] `transformations.md` - Function Transformations
- [ ] `polynomial-division.md` - Polynomial Division
- [ ] `rational-functions.md` - Rational Functions
- [ ] `conic-sections.md` - Conic Sections
- [ ] `polar-coordinates.md` - Polar Coordinates
- [ ] `parametric-equations.md` - Parametric Equations

---

## Khan Academy URL Mapping

For each explainer, link to the corresponding Khan Academy lesson.

**Base URLs:**
- Pre-Algebra: `https://www.khanacademy.org/math/pre-algebra/`
- Algebra Basics: `https://www.khanacademy.org/math/algebra-basics/`
- Algebra I: `https://www.khanacademy.org/math/algebra/`
- Algebra II: `https://www.khanacademy.org/math/algebra2/`
- Trigonometry: `https://www.khanacademy.org/math/trigonometry/`
- Precalculus: `https://www.khanacademy.org/math/precalculus/`

Find specific lesson URLs by browsing Khan Academy curriculum.

---

## Batch Workflow

### Suggested Approach

**Batch 1 (10 skills):** Algebra Basics + Core Algebra I
- Start with fundamentals
- These are most commonly used

**Batch 2 (10 skills):** Pre-Algebra foundations
- Support skills for algebra
- Fill in gaps

**Batch 3 (10 skills):** Advanced Algebra I + Algebra II
- Quadratics, polynomials, exponents

**Batch 4 (10 skills):** Trigonometry
- Trig ratios, unit circle, identities

**Batch 5 (10 skills):** Precalculus
- Functions, advanced topics

### Quality Checklist

For each explainer, verify:
- [ ] Follows template structure exactly
- [ ] Has 2-3 worked examples with full solutions
- [ ] Includes "check your answer" steps
- [ ] Lists common mistakes (❌)
- [ ] Lists key points (✓)
- [ ] Links to Khan Academy
- [ ] Uses clear, simple language
- [ ] Shows all work step-by-step
- [ ] Proper file naming and location

---

## Delivery Format

**Option 1:** Create files directly in `/home/jesse/school/study-buddy/content/explainers/`

**Option 2:** Provide content in a batch (markdown text) and I'll create files

**Option 3:** Progressive delivery - do 5-10 at a time for review

---

## Integration Steps (I'll handle this)

Once explainers are written:
1. I'll review for quality and consistency
2. Update `content/skills.json` with all skills
3. Update database seed script
4. Link explainers to API responses
5. Commit to git

---

## Questions?

If unclear about:
- Math concepts → reference Khan Academy or ask
- Template usage → see examples
- File structure → see existing files
- Prerequisites → logical ordering

---

**Status:** Ready for delegation
**Contact:** Jesse (via Claude Code, Codex, or Gemini)
**Priority:** Medium (can be done async while React app is built)
