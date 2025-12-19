# Study Buddy - Project Status & Tracking

**Last Updated:** 2024-12-19 (Session 1 Complete)

---

## 📋 Project Overview

**Goal:** Adaptive math quiz platform for college prep (pre-algebra → precalculus)

**Tech Stack:**
- Backend: FastAPI + PostgreSQL + SQLAlchemy
- Web: React 18 + TypeScript + Vite + Tailwind + KaTeX
- Mobile: React Native (Android)
- Deployment: study.junipr.io (VPS)

**Key Features:**
- Programmatic question generation (unlimited, free)
- Adaptive learning (spaced repetition + difficulty scaling)
- Smart prerequisite gap detection
- Pre-written explainers + Khan Academy links
- Cross-platform (web + mobile)

---

## ✅ Completed (Phase 1: Backend Foundation)

### Backend Infrastructure
- [x] Project structure (monorepo: api/, web/, mobile/, content/, docs/)
- [x] Git repository initialized with proper .gitignore
- [x] PostgreSQL database schema
- [x] SQLAlchemy models (User, Skill, QuestionTemplate, UserMastery, QuestionHistory)
- [x] Pydantic schemas for request/response validation
- [x] Environment configuration (Settings, .env)

### Authentication System
- [x] JWT token generation (24h access, 30d refresh)
- [x] Password hashing (bcrypt)
- [x] Auth endpoints (register, login, refresh, me)
- [x] Protected route dependencies

### Adaptive Learning Engine
- [x] Mastery score calculation (0-100 with recency bias)
- [x] Spaced repetition algorithm (7/3/1 day intervals)
- [x] Difficulty scaling (1-5 based on performance)
- [x] Adaptive question selection (due reviews → weak prerequisites → new skills → weighted random)
- [x] Prerequisite gap detection

### API Endpoints
- [x] Authentication routes (`/study/auth/*`)
- [x] Questions routes (`/study/questions/*`) - next, answer, practice
- [x] Progress routes (`/study/progress/*`) - summary, skill detail, weak areas, next reviews
- [x] Skills routes (`/study/skills/*`) - list, by subject, explainer

### Question Generators
- [x] Linear equations (ax + b = c) - 3 difficulty levels
- [x] Fraction addition (a/b + c/d) - 3 difficulty levels
- [x] Generator registry system

### Initial Content
- [x] Seed script with 5 skills
- [x] 3 prerequisite relationships
- [x] 6 question templates
- [x] Setup documentation (SETUP.md)

### Documentation
- [x] Main README.md
- [x] API README.md
- [x] API SETUP.md with testing instructions
- [x] .gitignore properly configured

### Git Management
- [x] 4 commits with proper messages and co-authorship
- [x] Clean commit history

**Backend Status:** ✅ COMPLETE (27 files, 2,400+ LOC)

---

## 🔄 In Progress (Phase 2: Content Creation - Started)

### Content Structure
- [x] Content directory structure created
- [x] README and template created
- [x] Initial skills.json (5 skills)
- [x] 2 example explainers written
- [ ] **Remaining: 45-95 more skills and explainers**

**Delegation Note:** Content writing (explainers) is perfect for Codex/Gemini agents. Template and examples provided.

---

## 📝 TODO - Phase 2: Content Creation

### Skills Mapping (50-100 skills total)
- [ ] Map Khan Academy curriculum structure
- [ ] Define all skills from pre-algebra → precalculus
- [ ] Create skills hierarchy with prerequisites

### Content Files
- [ ] Create `content/skills.json` with all skill metadata
- [ ] Create `content/khan-links.json` with Khan Academy URLs
- [ ] Write explainers for each skill (Markdown format):
  - [ ] Pre-Algebra (15-20 skills)
  - [ ] Algebra Basics (10-15 skills)
  - [ ] Algebra I (15-20 skills)
  - [ ] Algebra II (15-20 skills)
  - [ ] Trigonometry (10-15 skills)
  - [ ] Precalculus (10-15 skills)

### Question Templates
- [ ] Create template definitions for each skill type
- [ ] Implement generators:
  - [ ] Pre-Algebra: percentages, decimals, exponents
  - [ ] Algebra: multi-step equations, inequalities, systems
  - [ ] Algebra II: quadratics, polynomials, exponentials
  - [ ] Trig: unit circle, identities, right triangles
  - [ ] Precalculus: functions, logs, conics

**Estimated:** 2-3 weeks (can be delegated to Codex/Gemini for explainer writing)

---

## 📝 TODO - Phase 3: Web Application

### React Setup
- [ ] Initialize Vite + React + TypeScript project
- [ ] Configure Tailwind CSS
- [ ] Set up React Router
- [ ] Configure Zustand stores
- [ ] Set up React Query
- [ ] Integrate KaTeX for math rendering

### Core Components
- [ ] Authentication UI (Login, Register)
- [ ] Quiz interface (QuestionCard, MathInput, AnswerFeedback)
- [ ] Progress dashboard (MasteryBar, SkillTree, WeakAreasView)
- [ ] Skill browser (SkillList, SkillDetail, Explainer)
- [ ] Navigation (Header, Sidebar, Footer)

### Pages/Routes
- [ ] Login page
- [ ] Quiz page (main practice interface)
- [ ] Progress page (overall stats)
- [ ] Weak Areas page (gap analysis)
- [ ] Skills page (browse by subject)
- [ ] Skill Detail page (explainer + practice)

### API Integration
- [ ] API client wrapper
- [ ] Auth state management (Zustand)
- [ ] Quiz state management (Zustand)
- [ ] React Query hooks for all endpoints

### Styling
- [ ] Design system (colors, typography)
- [ ] Responsive layout (mobile-first)
- [ ] Math rendering styles
- [ ] Progress visualizations

**Estimated:** 2-3 weeks

---

## 📝 TODO - Phase 4: Deployment

### VPS Setup
- [ ] Install PostgreSQL on VPS
- [ ] Create database and user
- [ ] Deploy backend to `/srv/junipr/study-api/`
- [ ] Create systemd service for API
- [ ] Test API at localhost:8001

### Caddy Configuration
- [ ] Add `study.junipr.io` block to Caddyfile
- [ ] Modify `api.junipr.io` to route `/study/*` to port 8001
- [ ] Reload Caddy

### DNS Configuration
- [ ] Add A record for `study.junipr.io` in Cloudflare

### Production Deployment
- [ ] Build web app (`npm run build`)
- [ ] Deploy to `/srv/junipr/study/`
- [ ] Test at https://study.junipr.io
- [ ] Test API at https://api.junipr.io/study

### Production Data
- [ ] Seed production database with all skills
- [ ] Create production user account

**Estimated:** 1-2 days

---

## 📝 TODO - Phase 5: Mobile App (Android)

### React Native Setup
- [ ] Initialize React Native project
- [ ] Configure TypeScript
- [ ] Set up navigation
- [ ] Configure API client (shared with web)

### Core Screens
- [ ] Login screen
- [ ] Quiz screen
- [ ] Progress screen
- [ ] Skills browser

### Mobile-Specific Features
- [ ] Token storage (React Native Keychain)
- [ ] Biometric authentication
- [ ] Offline question cache (optional)

### Build & Deploy
- [ ] Configure Android build
- [ ] Generate signed APK
- [ ] Test on physical device

**Estimated:** 2-3 weeks

---

## 🎯 Current Priority

**Next Action:** Phase 2 - Content Creation (Skills & Explainers)

**Delegation Opportunity:** Content writing (explainers) can be delegated to Codex or Gemini agents to save context/cost.

---

## 🔧 Technical Decisions Made

1. **Monorepo structure** - Easier to manage, single git repo
2. **PostgreSQL over MariaDB** - Simpler for this use case
3. **API path prefix `/study`** - Share api.junipr.io safely
4. **Question caching in-memory** - Good for MVP, can move to Redis later
5. **No AI APIs** - Programmatic generation to avoid costs
6. **KaTeX over MathJax** - Lighter weight for web app

---

## 🐛 Known Issues / Tech Debt

None currently - fresh project.

---

## 📦 Dependencies to Track

### Backend (Python)
- FastAPI 0.109.0
- PostgreSQL (psycopg2-binary 2.9.9)
- SQLAlchemy 2.0.25
- JWT (python-jose 3.3.0)
- SymPy 1.12 (math validation)

### Web (Future)
- React 18+
- Vite 5+
- TypeScript 5+
- Tailwind CSS 4+
- KaTeX (math rendering)

### Mobile (Future)
- React Native (latest stable)
- React Native Biometrics
- React Native Keychain

---

## 📚 Reference Documentation

- **Plan:** `/home/jesse/.claude/plans/smooth-conjuring-candle.md`
- **Setup:** `/home/jesse/school/study-buddy/api/SETUP.md`
- **Khan Academy Links:** Curriculum URLs in plan document

---

## 💡 Notes

- User prefers delegating to Codex/Gemini when possible (save context/cost)
- Keep this file updated as work progresses
- Track all decisions and blockers here
- Update "Last Updated" date when making changes
