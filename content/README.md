# Study Buddy Content

Pre-written educational content for skills.

## Structure

```
content/
├── skills.json              # All skills metadata (master list)
├── khan-links.json          # Khan Academy URL mappings
├── explainers/              # Skill explanations (Markdown)
│   ├── pre-algebra/
│   ├── algebra-basics/
│   ├── algebra-1/
│   ├── algebra-2/
│   ├── trigonometry/
│   └── precalculus/
└── templates/
    └── question-templates.json  # Question template definitions
```

## Skills Structure

Each skill includes:
- **slug**: URL-friendly identifier (e.g., "solving-linear-equations")
- **name**: Display name (e.g., "Solving Linear Equations")
- **subject**: Category (e.g., "Algebra Basics")
- **description**: Brief summary
- **khan_url**: Link to Khan Academy lesson
- **prerequisites**: Array of prerequisite skill slugs
- **difficulty_base**: Base difficulty (1-5)

## Explainer Format

Each explainer is a Markdown file with:
1. What is it? (concept explanation)
2. How to solve (step-by-step method)
3. Example problem with solution
4. Key points to remember
5. Link to Khan Academy

## Content Generation Status

- **Phase 1:** Structure created ✅
- **Phase 2:** Initial examples created (2-3 skills) ✅
- **Phase 3:** Full content (50-100 skills) - **Can delegate to Codex/Gemini**

## Adding New Skills

1. Add to `skills.json` with all metadata
2. Add Khan Academy link to `khan-links.json`
3. Create explainer in appropriate subject folder
4. Update prerequisites if needed
5. Run seed script to add to database
