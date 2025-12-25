"""Main FastAPI application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import get_settings, engine, Base
from app.routes import auth, questions, progress, skills, evaluation, admin, badges

# Create database tables
Base.metadata.create_all(bind=engine)

settings = get_settings()

# Initialize FastAPI app
app = FastAPI(
    title="Study Buddy API",
    description="Adaptive math quiz platform API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
origins = settings.cors_origins.split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix=settings.api_prefix)
app.include_router(questions.router, prefix=settings.api_prefix)
app.include_router(progress.router, prefix=settings.api_prefix)
app.include_router(skills.router, prefix=settings.api_prefix)
app.include_router(evaluation.router, prefix=settings.api_prefix)
app.include_router(admin.router, prefix=settings.api_prefix)
app.include_router(badges.router, prefix=settings.api_prefix)


@app.get("/")
def root():
    """Root endpoint."""
    return {
        "message": "Study Buddy API",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get(f"{settings.api_prefix}/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "study-buddy-api"}
