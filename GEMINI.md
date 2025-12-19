# Study Buddy - Project Context (Gemini)

## Project Overview

**Study Buddy** is an adaptive learning platform for a broad range of study topics. Currently features math content (pre-algebra through precalculus), with more subjects to come. This is a school project that demonstrates:
- Adaptive learning algorithms (spaced repetition, mastery tracking, difficulty scaling)
- Full-stack development (FastAPI backend + React frontend)
- Cost-efficient AI strategy (programmatic questions, pre-written content)

**Repository:** `/home/jesse/school/study-buddy/`

## Current Status

**Phase 3 COMPLETE** - MVP fully functional and ready for testing

### What's Done
- ✅ **Phase 1:** Complete FastAPI backend (28 files, 2,400+ LOC)
  - Database models and schemas
  - JWT authentication
  - Adaptive learning engine
  - 13 API endpoints
  - 2 question generators (linear equations, fractions)

- ✅ **Phase 2:** Content structure ready for delegation
  - 50+ skills mapped
  - Template and examples created
  - Delegation brief complete

- ✅ **Phase 3:** Complete React web app (35+ files, 5,200+ LOC)
  - Login/Register + Quiz interface + Progress dashboard
  - Full API integration with TypeScript
  - State management (Zustand)
  - Responsive Tailwind CSS design

### What's Pending
- [ ] **DELEGATED TO CODEX/GEMINI:** Write 45-95 skill explainers (see DELEGATION-BRIEF.md)
- [ ] Test full stack locally (backend + web app)
- [ ] Add more question generators (quadratics, trig, etc.)
- [ ] Deploy to study.junipr.io (Phase 4)
- [ ] Build Android mobile app (Phase 5)

## ACTIVE DELEGATION TASK

**FOR CODEX/GEMINI AGENTS:**

You have been delegated the task of writing educational explainers (currently math skills, more subjects coming).

**What to do:**
1. Read `/home/jesse/school/study-buddy/content/DELEGATION-BRIEF.md` for complete instructions
2. Follow the template at `/home/jesse/school/study-buddy/content/EXPLAINER-TEMPLATE.md`
3. Review examples:
   - `content/explainers/algebra-basics/solving-linear-equations.md`
   - `content/explainers/pre-algebra/fraction-addition.md`
4. Write explainers for skills listed in the delegation brief (45-95 total)
5. Save as: `content/explainers/{subject}/{skill-slug}.md`

**Priority:** Start with Algebra Basics (Priority 1 in delegation brief)

**Format:** Each explainer must include:
- Clear definition
- Step-by-step method
- Full worked examples (2-3)
- Key points and common mistakes
- Khan Academy link

**Delivery:** Create files directly or work in batches of 5-10 for review

**When done:** Update session notes and commit all new files to git

## Important Notes

- Session notes: `.session-notes.md` (track progress here)
- All changes must be committed to git when done
- This is a school portfolio project
- Zero ongoing AI costs is a key requirement (hence pre-written content)

## Tech Stack

**Backend:** FastAPI, SQLAlchemy, PostgreSQL, JWT, Alembic
**Frontend:** React, TypeScript, React Router, Zustand, Tailwind CSS, KaTeX
**Deployment:** Will deploy to VPS at study.junipr.io
**Mobile:** React Native (future phase)
