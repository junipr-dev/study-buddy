# Study Buddy API Setup Guide

## Quick Start (Local Development)

### 1. Install PostgreSQL

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

### 2. Create Database

```bash
sudo -u postgres psql
```

```sql
CREATE DATABASE study_buddy;
CREATE USER study_api WITH PASSWORD 'dev_password_123';
GRANT ALL PRIVILEGES ON DATABASE study_buddy TO study_api;
\q
```

### 3. Set Up Python Environment

```bash
cd ~/school/study-buddy/api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
```

Edit `.env`:
```
DATABASE_URL=postgresql://study_api:dev_password_123@localhost/study_buddy
JWT_SECRET_KEY=your_super_secret_key_change_this_in_production
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
REFRESH_TOKEN_DAYS=30
API_PREFIX=/study
CORS_ORIGINS=http://localhost:5173,https://study.junipr.io
```

### 5. Seed Database

```bash
python seed_data.py
```

You should see:
```
✅ Database seeded successfully!
   - 5 skills
   - 3 prerequisites
   - 6 question templates
```

### 6. Run Development Server

```bash
uvicorn app.main:app --reload --port 8001
```

API will be running at: http://localhost:8001

## Testing the API

### Option 1: Swagger UI (Recommended)

Visit http://localhost:8001/docs

### Option 2: curl Commands

**Register a user:**
```bash
curl -X POST http://localhost:8001/study/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username": "jesse", "password": "testpass123"}'
```

**Login:**
```bash
curl -X POST http://localhost:8001/study/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "jesse", "password": "testpass123"}'
```

Save the `access_token` from the response.

**Get next question:**
```bash
curl -X GET http://localhost:8001/study/questions/next \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Submit answer:**
```bash
curl -X POST http://localhost:8001/study/questions/answer \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"question_id": "QUESTION_ID_FROM_PREVIOUS", "answer": "3", "time_taken_seconds": 15}'
```

**Get progress:**
```bash
curl -X GET http://localhost:8001/study/progress \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**List skills:**
```bash
curl -X GET http://localhost:8001/study/skills
```

## Troubleshooting

**Database connection error:**
- Check PostgreSQL is running: `sudo systemctl status postgresql`
- Verify credentials in `.env`
- Test connection: `psql -U study_api -d study_buddy -h localhost`

**Import errors:**
- Ensure virtual environment is activated: `source venv/bin/activate`
- Reinstall requirements: `pip install -r requirements.txt`

**Port already in use:**
- Change port: `uvicorn app.main:app --reload --port 8002`

## Next Steps

1. Test all endpoints via Swagger UI
2. Create more question generators (see `api/app/generators/`)
3. Add more skills and templates (see `api/seed_data.py`)
4. Build the web frontend
