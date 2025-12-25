# Study Buddy - Bug Report

**Generated:** 2024-12-24
**Testing Method:** Playwright automated browser testing
**URL Tested:** https://study.junipr.io

---

## Critical Bugs

### 1. Percentages Question Generator - Empty Question
**Severity:** Critical
**Location:** `backend/app/generators/percentages.py`
**Screenshot:** `.playwright-mcp/study-buddy-07-percentage-q.png`

**Description:** The percentages question generator produces questions with incomplete text. The question displays "Calculate the percentage" with no actual numbers or values to calculate.

**Expected:** "Calculate 25% of 80" or similar complete question
**Actual:** "Calculate the percentage" (no numbers provided)

**Impact:** Users cannot answer the question - completely broken functionality

---

### 2. HTTP 500 Server Errors
**Severity:** Critical
**Location:** Backend API endpoints
**Screenshot:** `.playwright-mcp/study-buddy-10-500-error.png`, `.playwright-mcp/study-buddy-14-admin-500.png`

**Description:** Multiple API calls return HTTP 500 errors:
- During evaluation mode question submissions
- Admin dashboard data loading (overview stats, evaluations)

**Impact:** Features completely non-functional, data not loading

**Action Required:** Check server logs for stack traces, investigate database queries

---

## High Priority Bugs

### 3. KaTeX Spacing Bug in Unit Conversions
**Severity:** High
**Location:** `backend/app/generators/unit_conversions.py`
**Screenshot:** `.playwright-mcp/study-buddy-08-katex-spacing-bug.png`

**Description:** Unit conversion questions render LaTeX without proper spacing. Example: "30meterspersecond" instead of "30 meters per second"

**Expected:** `30 \text{ meters per second}` or similar with spaces
**Actual:** `30\text{meterspersecond}` - all words concatenated

**Impact:** Questions hard to read, unprofessional appearance

---

### 4. Emoji Rendering as Square Box
**Severity:** High
**Location:** Progress page, possibly other locations
**Screenshot:** `.playwright-mcp/study-buddy-09-progress-bug.png`, `.playwright-mcp/study-buddy-20-mobile-progress.png`

**Description:** The chart emoji (📊) renders as a square box instead of the actual emoji character.

**Possible Causes:**
- Missing emoji font support
- CSS font-family not including emoji fonts
- Server-side rendering issue

**Fix Suggestion:** Add emoji font fallback:
```css
font-family: ..., "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", sans-serif;
```

---

## Medium Priority Bugs

### 5. Login UI State Not Updating
**Severity:** Medium
**Location:** Frontend login flow
**Screenshot:** `.playwright-mcp/study-buddy-03-after-login.png`

**Description:** After successful login (200 response), the page URL changes to /quiz but the login form still displays briefly. Requires navigation to actually see authenticated content.

**Possible Cause:** Race condition between auth state update and route change

**Impact:** Confusing UX, user might think login failed

---

### 6. Admin Dashboard Empty States
**Severity:** Medium
**Location:** Admin dashboard tabs
**Screenshot:** `.playwright-mcp/study-buddy-15-admin-users.png`, `.playwright-mcp/study-buddy-16-admin-skills.png`

**Description:** Some admin dashboard tabs show empty or minimal data even when data should exist. The Skills tab shows 0 items but skills exist in the system.

**Impact:** Admin functionality limited

---

## User Experience Issues (Not Bugs)

### 7. No Module Progress Indicator
**Priority:** High
**Location:** Quiz/Evaluation mode

**User Feedback:** "We need some kind of brief progress shown for where they are in the modules (Pre Algebra, Trig, etc). Because even though it shows which one specifically in the progress bar, you don't know how many are left or where you are in the process, leaving you absolutely no idea how long it'll take to finish."

**Suggested Solution:**
- Show "Module 2 of 6: Pre-Algebra"
- Display estimated time remaining
- Show total questions remaining across all modules

---

### 8. Visual Appeal / Engagement
**Priority:** Medium
**Location:** Overall app

**User Feedback:** "We also need to add a bit of interest/entertainment/visual appeal/fun to study buddy. Functional or not, it's a bit dull."

**Suggested Enhancements:**
- Gamification (XP, levels, badges, streaks)
- Animations and transitions
- Theme options (dark/light/colorful)
- Mascot interactions
- Sound effects (optional)
- Celebration animations for correct answers

---

### 9. Smarter Evaluation Algorithm
**Priority:** High
**Location:** Evaluation mode logic

**User Feedback:** Evaluation needs to be both thorough AND streamlined - test all areas to some degree but as efficiently as possible. Goal is to confidently and accurately advise the user on ways to strengthen skills (specific Khan Academy links + brief advice/overview).

**Design Goals:**
1. **Thorough** - Must test ALL skill areas to understand full competency picture
2. **Efficient** - Minimize questions needed to determine skill level
3. **Accurate** - High confidence in assessment before giving recommendations
4. **Actionable** - Output specific Khan Academy links + targeted advice

**Suggested Algorithm Improvements:**
- **Adaptive question count per skill:** 2-5 questions based on answer consistency
  - 2 correct in a row = skill mastered, move on
  - 2 wrong in a row = skill gap identified, move on
  - Mixed results = ask 1-2 more to determine edge cases
- **Difficulty scaling:** Start medium, go harder if correct, easier if wrong
- **Confidence scoring:** Track certainty level per skill before finalizing
- **Breadth-first sampling:** Touch every skill category before deep-diving
- **Skip redundant skills:** If user masters "Solving Linear Equations", skip easier prerequisite skills

**Output Requirements:**
- Per-skill mastery percentage with confidence level
- Prioritized list of skills to improve (weakest first)
- Direct Khan Academy links to relevant modules
- Brief personalized advice based on error patterns

---

## Test Coverage Summary

| Page | Status | Issues Found |
|------|--------|--------------|
| Login | Tested | Minor UI state issue |
| Register | Tested | None |
| Quiz (Evaluation) | Tested | Question generators, 500 errors |
| Progress | Tested | Emoji rendering, empty state |
| Admin Dashboard | Tested | 500 errors, empty data |
| Mobile (375x812) | Tested | Responsive - working well |

---

## Next Steps

1. **Immediate:** Fix percentages question generator
2. **Immediate:** Fix KaTeX spacing in unit_conversions generator
3. **Investigate:** Server 500 errors (check logs)
4. **Quick Fix:** Add emoji font fallback CSS
5. **Enhancement:** Add module progress indicator
6. **Enhancement:** Plan gamification features
7. **Future:** Implement adaptive testing algorithm
