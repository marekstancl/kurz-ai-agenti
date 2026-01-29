---
applyTo: "**/*"
---

# 📘 Project Guide

**Version:** 3.0.0  
**Last Updated:** 2026-01-29

> **Course Setup:** This file is customized for the AI Agenti course and should be updated as the repo grows.

---

## 🎯 Overview

**Project Guide = quick reference for the AI Agenti course project**

**Purpose:** Keep course-specific context and evolving setup in one place.

**Contains:**
- Course context and goals
- Current tech stack (as it becomes known)
- Quick start commands
- Testing commands
- Log locations
- Database operations
- Common troubleshooting

**Current State:** Empty repo + AI Agent Framework installed. Code will be added during the course.

## 🧭 Course Context

**Course:** AI Agenti (29. 1. 2026 → 5. 3. 2026)

**Goal:** Build a working AI agent that connects LLMs, databases, and tools.

**Expected topics/tools (per course outline):**
- LLM APIs: OpenAI, Anthropic, HuggingFace, Ollama
- Frameworks: LangChain, Semantic Kernel, Autogen, LangGraph, n8n
- Data stores: SQL, NoSQL, vector DB (e.g., ChromaDB)
- Reinforcement learning: Gymnasium, PettingZoo, Stable-Baselines3
- Infrastructure: Docker, GitHub

**Notes:** Update this section after each lesson with new decisions or constraints.

## ✅ Current Decisions

- **Tech Stack:** TBD (decide during lessons)
- **Project Type:** Course exercises + final agent project
- **Repo Scope:** All work for the course stays in this repo

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
# Create
alembic revision --autogenerate -m "message"

# Apply
alembic upgrade head

# Rollback
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
