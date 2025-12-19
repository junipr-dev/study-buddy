# Study Buddy API

FastAPI backend for Study Buddy adaptive math quiz platform.

## Setup

### 1. Create Virtual Environment

```bash
cd api
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
cp .env.example .env
# Edit .env with your database credentials and JWT secret
```

### 4. Set Up Database

```bash
# Install PostgreSQL if not already installed
sudo apt install postgresql postgresql-contrib

# Create database and user
sudo -u postgres psql
```

```sql
CREATE DATABASE study_buddy;
CREATE USER study_api WITH PASSWORD 'your_password_here';
GRANT ALL PRIVILEGES ON DATABASE study_buddy TO study_api;
\q
```

### 5. Run Migrations

```bash
alembic upgrade head
```

### 6. Run Development Server

```bash
uvicorn app.main:app --reload --port 8001
```

API will be available at: http://localhost:8001

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8001/docs
- ReDoc: http://localhost:8001/redoc

## Testing

```bash
pytest
```

## Deployment

See main README.md for deployment instructions to VPS.
