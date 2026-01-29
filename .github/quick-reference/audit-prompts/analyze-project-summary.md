# 📊 Analyze Project & Generate Summary

**Version:** 1.0.0  
**Purpose:** Generate concise project summary for AI context  
**Output:** Markdown summary for docs + meta-prompt

---

## 🎯 Task

Analyze the entire project and generate a **concise 2-3 sentence summary** about:
1. **What the project does** (business value, domain)
2. **Key features** (main capabilities)
3. **Core tech stack** (languages, frameworks, key libraries)
4. **Architecture type** (monolithic, microservices, RAG, etc.)

Output will be used in:
- **docs/docs/overview/project-summary.md** - Available to all users
- **meta-prompt.md** - Auto-loaded for AI context

---

## 📋 Analysis Steps

### Step 1: Scan Project Root
```bash
# Examine these files (in order of priority):
1. README.md - Main project description
2. CHANGELOG.md - Version history + features
3. .gitlab-ci.yml or similar - CI/CD
4. docker-compose.yml - Architecture overview
5. package.json or requirements.txt - Dependencies
```

**Extract:**
- 🎯 Project name & tagline
- 📝 3-5 sentence description (from README intro)
- 🏗️ Architecture diagram/description (if exists)

### Step 2: Identify Tech Stack
```markdown
Frontend:
- Check: package.json main "dependencies"
- Look for: React, Vue, Angular, Next.js, etc.
- TypeScript? Yes/No

Backend:
- Check: requirements.txt, pom.xml, go.mod, etc.
- Look for: FastAPI, Django, Express, Go, etc.
- Database: PostgreSQL, MongoDB, etc.

Infrastructure:
- Check: docker-compose.yml, k8s files
- Deployment: Docker, Kubernetes, serverless, etc.

Key Libraries:
- AI/ML: OpenAI, LangChain, Hugging Face, etc.
- Vector DB: Qdrant, Pinecone, Weaviate, etc.
- ORM: SQLAlchemy, TypeORM, etc.
```

**Extract:**
```
Frontend: [name] [version] ([features])
Backend: [name] [version] ([features])
Database: [type]
Infrastructure: [type]
Key Libraries: [list with versions]
```

### Step 3: Identify Key Features
```markdown
From README, CHANGELOG, or docs/:

Look for:
- "Features" section
- "Key capabilities" section
- "What you can do" section
- Numbered lists of main features
- Project maturity (v1.0, beta, POC, etc.)

Extract TOP 3-5 features (most important first)
```

**Extract:**
```
✨ Feature 1: [Description]
✨ Feature 2: [Description]
✨ Feature 3: [Description]
```

### Step 4: Understand Architecture
```markdown
Look for patterns:

Monolithic:
- Single repo + folder structure
- One backend language
- Shared database

Microservices:
- Multiple docker-compose services
- Separate backend/frontend folders
- Message queues (RabbitMQ, Redis)
- Service discovery or API gateway

RAG System:
- Vector DB (Qdrant, Pinecone)
- LLM integration (OpenAI, Hugging Face)
- Embedding generation
- Retrieval logic

Check: README section, architecture file, docker-compose.yml
```

**Extract:**
```
Architecture Type: [monolithic|microservices|RAG|hybrid|other]
Primary Pattern: [description]
Data Flow: [brief overview]
```

### Step 5: Check for Special Characteristics
```markdown
Look for:
- Domain specialization (legal, medical, fintech, etc.)
- Real-time processing
- Batch processing
- Learning/feedback loops
- Multi-language support
- High security/compliance requirements

These help understand project constraints & priorities
```

**Extract:**
```
Domain: [industry/use-case]
Special Requirements: [list]
```

---

## 📝 Generate Summary

### Format 1: Short (For AI meta-prompt)
```markdown
## Project Context

**{Project Name}** - {1-2 sentence description of what it does}

Key capabilities:
- {Feature 1}
- {Feature 2}
- {Feature 3}

**Tech Stack:**
- Frontend: {stack}
- Backend: {stack}
- Infrastructure: {stack}
```

### Format 2: Medium (For docs/overview)
```markdown
---
title: "Project Summary"
sidebar_label: "Summary"
sidebar_position: 1
last_updated: {YYYY-MM-DD}
status: current
audience:
  primary: [stakeholder, ai-developer]
  secondary: [developer]
complexity: beginner
read_frequency: onboarding
---

# {Project Name}

{1-2 sentence tagline}

## What It Does

{2-3 sentences explaining business value + domain}

## Key Features

- ✨ {Feature 1}: {Description}
- ✨ {Feature 2}: {Description}
- ✨ {Feature 3}: {Description}

## Architecture

**Type:** {Architecture}
**Pattern:** {Pattern description}

{1-2 sentences explaining how components work together}

## Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| Frontend | {Frontend} | {version} |
| Backend | {Backend} | {version} |
| Database | {Database} | {version} |
| Infrastructure | {Infrastructure} | - |

## Key Libraries

- {Library 1}: {Purpose}
- {Library 2}: {Purpose}
- {Library 3}: {Purpose}

## Current Phase

**Version:** {version}
**Status:** {beta|production|POC|in-development}
**Last Updated:** {date}

---

### Quick Links
- [Full Documentation](../index.md)
- [Architecture Guide](../architecture/)
- [Getting Started](../development/quick-start.md)
```

---

## ✅ Validation Checklist

### Generated Summary Should:
- [ ] Be 1-3 sentences maximum (~100 words)
- [ ] Explain WHAT the project does (not HOW)
- [ ] Include domain/industry context
- [ ] Mention 3+ main features
- [ ] List tech stack components
- [ ] Be understandable to non-technical stakeholders
- [ ] NOT include implementation details
- [ ] Include project version/status

### Format Should:
- [ ] Use Markdown
- [ ] Include YAML frontmatter (for docs)
- [ ] Have clear sections
- [ ] Include tables for structured data
- [ ] Have proper links

---

## 🔍 Common Patterns by Project Type

### SaaS Application
```
{Project} is a cloud-based {domain} platform that {main-feature}.
It enables {benefit} through:
- {Feature 1}
- {Feature 2}
- {Feature 3}

Built with {tech-stack}
```

### AI/ML System
```
{Project} is a {type} system for {domain} that {capability}.
Key components:
- {Component 1}: {Purpose}
- {Component 2}: {Purpose}
- {Component 3}: {Purpose}

Tech: {AI-Framework}, {Vector-DB}, {Backend}
```

### Tool/Library
```
{Project} is a {type} library for {domain}.
It provides:
- {Capability 1}
- {Capability 2}
- {Capability 3}

Built with: {Tech}
```

### Specialized System (RAG, Legal, etc.)
```
{Project} is a {specialized-type} platform for {domain}.
Unlike generic solutions, it features:
- {Unique-Feature-1}
- {Unique-Feature-2}
- {Domain-Specific-Feature}

Powered by: {Tech-Stack}
```

---

## 🚀 Usage in Meta-Prompt

Once summary is generated and saved to docs/docs/overview/project-summary.md:

**In meta-prompt.md, add:**
```markdown
## Project Overview

**Auto-load:** 
```bash
cat docs/docs/overview/project-summary.md
```

This will ensure:
1. AI always knows project context on session start
2. Summary updated only when project changes significantly
3. Documentation stays DRY (single source of truth)
```

---

## 📚 Related

- [documentation-protocol.md](../../core/documentation-protocol.md) - Docusaurus standards
- [project-guide.md](../../core/project-guide.md) - Technical details
- [meta-prompt.md](../../core/meta-prompt.md) - AI context loading

---

## 💡 Tips

1. **Don't overthink:** Summary should take 2-3 minutes to read
2. **Use examples:** Reference specific features, not abstract concepts
3. **Match audience:** Different versions for stakeholders vs developers
4. **Keep it fresh:** Update every 3-6 months or after major releases
5. **Link everything:** Make sure it connects to detailed docs

---

**Remember:** The goal is for AI to understand project without reading 100+ pages of docs!
