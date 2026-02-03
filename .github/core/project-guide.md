---
applyTo: "**/*"
---

# 📘 Project Guide

**Version:** 3.0.0  
**Last Updated:** 2026-01-24

> **Auto-Generated:** This file is auto-generated when AI starts new session.

---

## 🎯 Overview

**Project Guide = project-specific quick reference**

**Contains:**
- Architecture overview
- Quick start commands
- Testing commands
- Log locations
- Database operations
- Common troubleshooting

**Generate:** AI auto-generates when starting new session (reads codebase)

---

## 📋 Template Structure

### 1. Architecture

```markdown
## 🏗️ Architecture

**Type:** [Detected: FastAPI + React / Next.js / etc.]

**Structure:**
- Backend: [language, framework, location]
- Frontend: [language, framework, location]
- Database: [type, location]
- Infrastructure: [Docker, Kubernetes, etc.]

**Key Files:**
- Config: [locations]
- Entry points: [main files]
- Migrations: [location]
```

### 2. Quick Start

```markdown
## 🚀 Quick Start

### Development
```bash
# Backend
cd backend && uvicorn app.main:app --reload

# Frontend
cd frontend && npm run dev
```

### Production
```bash
docker-compose up -d
```

### Testing
```bash
# Unit tests
pytest

# E2E tests
npx playwright test
```
```

### 3. Logs & Debugging

```markdown
## 🔍 Logs & Debugging

**Log Locations:**
- Backend: `backend/logs/app.log`
- Frontend: Browser console
- Docker: `docker logs <container>`

**Enable Debug Mode:**
```bash
# Backend
export LOG_LEVEL=DEBUG

# Frontend
export VITE_DEBUG=true
```

**Common Issues:**
- [Issue 1]: [Solution]
- [Issue 2]: [Solution]
```

### 4. Database

```markdown
## 🗄️ Database

**Connection:**
```python
# Location: backend/app/core/database.py
DATABASE_URL = "postgresql://..."
```

**Migrations:**
```bash
# Check project-specific approach:
# - Alembic: alembic revision --autogenerate -m "message"
# - Raw SQL: Create numbered .sql files in migrations/
# - Flyway: Use V{version}__{description}.sql format

# Example (Alembic):
alembic revision --autogenerate -m "add users table"

# Apply
alembic upgrade head

# Rollback (if supported)
alembic downgrade -1
```

**Common Queries:**
```sql
-- See data
SELECT * FROM legal_domains;

-- Reset
TRUNCATE TABLE legal_domains CASCADE;
```
```

### 5. API Reference

```markdown
## 🌐 API Endpoints

**Base URL:** `http://localhost:8000`

**Key Endpoints:**
- `GET /api/v1/health` - Health check
- `GET /api/v1/legal-domains` - Legal domains
- `POST /api/v1/upload` - File upload

**Docs:** http://localhost:8000/docs
```

### 6. Testing

```markdown
## 🧪 Testing

**Run All Tests:**
```bash
pytest
```

**Run Specific:**
```bash
# File
pytest tests/test_legal_domains.py

# Function
pytest tests/test_legal_domains.py::test_endpoint
```

**Coverage:**
```bash
pytest --cov=app --cov-report=html
open htmlcov/index.html
```
```

---

## 🤖 AI Generation Process

**When:** Start of every new session

**Steps:**
```markdown
1. Detect architecture:
   - Check for backend/ (FastAPI/Django/Express)
   - Check for frontend/ (React/Vue/Next.js)
   - Check for docker-compose.yml
   - Check for package.json, requirements.txt

2. Find key files:
   - Entry points (main.py, index.ts)
   - Config files (.env, config.py)
   - Migration directories

3. Determine commands:
   - Start commands (from package.json, README)
   - Test commands (pytest, npm test)
   - Build commands (docker-compose up)

4. Locate logs:
   - Check logs/ directory
   - Check docker-compose.yml volumes

5. Database info:
   - Find connection strings
   - Locate migrations
   - Common queries

6. Generate project-guide.md
7. Save to session file
```

---

## 📚 Related

- [session-management.md](session-management.md) - Session initialization
- [new-chat.md](../quick-reference/new-chat.md) - Session start

---

**Remember:** AI auto-generates this per project when starting new session!
