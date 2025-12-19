# Study Buddy

An adaptive learning platform for a broad range of study topics. Currently features math content (pre-algebra through precalculus), with more subjects coming.

## Features

- **Adaptive Learning**: Spaced repetition + difficulty scaling based on performance
- **Smart Gap Detection**: Identifies prerequisite weaknesses when struggling with advanced topics
- **Unlimited Questions**: Programmatic template-based generation (no AI API costs)
- **Cross-Platform**: Web app + Android mobile app
- **Progress Tracking**: Detailed mastery scores and analytics

## Architecture

- **Web**: React 18 + TypeScript + Vite + Tailwind CSS
- **Mobile**: React Native + TypeScript (Android)
- **Backend**: FastAPI + PostgreSQL + SQLAlchemy
- **Math Rendering**: KaTeX
- **Deployment**: study.junipr.io (VPS)

## Project Structure

```
study-buddy/
├── api/                # FastAPI backend
├── web/                # React web app
├── mobile/             # React Native Android app
├── content/            # Pre-written explainers + Khan Academy links
├── docs/               # Documentation
└── README.md
```

## Development

See individual README files in each directory for setup instructions.

## Deployment

- **Web**: https://study.junipr.io
- **API**: https://api.junipr.io/study

## License

Personal project for college prep.
