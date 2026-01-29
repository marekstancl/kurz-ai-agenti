---
applyTo: "**/*"
---

# ⚡ Quality Gates

**Version:** 3.0.0  
**Last Updated:** 2026-01-24

---

## 🎯 Overview

**Purpose:** Zajistit, že KAŽDÝ commit je čistý, bezpečný, kompletní

**Philosophy:** Quality gates = safety net proti regresi

**When:** PŘED KAŽDÝM COMMITEM (bez výjimky!)

---

## 🚨 MANDATORY Workflow

```bash
# 1. STOP before "git commit"
# 2. Run checklist níže (v pořadí!)
# 3. Pokud FAIL → oprav → opakuj
# 4. Pokud PASS → commit
```

---

## ✅ Quality Gates (6 Steps)

### Gate 1: Log Analysis 🔴 CRITICAL

**Purpose:** Ujistit se, že změny nezlomily build

**Commands:**
```bash
# Frontend
cd frontend && npm run dev
# Běží 30s → check terminal

# Backend
cd backend && python -m uvicorn app.main:app --reload
# Běží 30s → check terminal
```

**Check:**
```markdown
□ Frontend: Žádné ERROR
□ Frontend: Žádné CRITICAL warnings
□ Backend: Žádné ERROR
□ Backend: Žádné runtime exceptions
□ Server starts bez crashes

⚠️ Pre-existing warnings: OK (dokumentuj v session file)
❌ NEW warnings: NOT OK (oprav!)
```

**If FAIL:** Oprav error → retest → Don't commit until clean!

---

### Gate 2: Documentation Impact Analysis 🔴 CRITICAL

**Purpose:** Dokumentace = synchronizovaná s kódem

**Reference:** See [documentation-protocol.md](documentation-protocol.md) for:
- MDX syntax validation (curly braces, `<` symbols)
- Docusaurus build testing (`npm run build`)
- YAML frontmatter requirements

**Process:**
```markdown
1. Co jsem změnil?
   git diff --name-only

2. Jaká docs může být dotčena?
   - DB schema změna → ERD?
   - API změna → API docs?
   - Business logika → System overview?
   - UI změna → UI guide?
   - Feature/Fix → CHANGELOG?

3. Projdi docs/ strukturu
   tree docs/ -L 3

4. Aktualizuj VŠECHNY dotčené docs

5. Stage docs do gitu
   git add docs/...
```

**Common Patterns (GUIDE, ne exhaustive!):**

| Code Change | Usually Affects |
|-------------|----------------|
| `backend/app/models/*.py` | database-erd.md |
| `backend/app/api/*.py` | api-design.md |
| `backend/app/core/*.py` | system-overview.md |
| `frontend/components/*.tsx` | components.md |
| Any `feat:`/`fix:` | CHANGELOG.md |

**⚠️ VŽDY udělej Impact Analysis! Toto jen guide.**

**If UNCERTAIN:** Eskaluj PM:
```
🤔 DOCUMENTATION UNCERTAINTY
Changed: {files}
Potentially affected: {docs list}
Question: Které docs mám aktualizovat?
```

---

### Gate 3: Code Cleanup 🟡 HIGH

**Purpose:** Odstranit temporary files a debug artifacts

**Commands:**
```bash
find . -name "*.tmp" -o -name "*.bak"
grep -r "console.log" frontend/
grep -r "print(" backend/ | grep -v "# print"
grep -r "TODO" backend/app/ frontend/src/
```

**Checklist:**
```markdown
□ Žádné .tmp, .bak soubory
□ Žádné console.log v prod
□ Žádné print() debug v prod
□ Žádné commented code (pokud není důvod)
□ Žádné TODO v prod (přesuň do bugs.md/session file)
□ Žádné hardcoded credentials
□ Žádné test data v prod
```

**DELETE:**
```python
print("DEBUG: user_id =", user_id)  # ❌
# old_function()  # ❌
# TODO: refactor  # ❌ (přesuň do session file)
API_KEY = "sk-12345"  # ❌
```

**KEEP:**
```python
logger.debug("Processing user: %s", user_id)  # ✅
# NOTE: Legacy algorithm for backwards compatibility  # ✅
```

---

### Gate 4: Git Status Check 🟡 HIGH

**Purpose:** Commitneš správné soubory

**Commands:**
```bash
git status
git diff --cached
git status | grep "Untracked"
```

**Checklist:**
```markdown
□ Všechny code changes staged
□ Všechny doc updates staged
□ Session file staged (pokud updated)
□ Epic progress staged (pokud epic)
□ .env NENÍ staged
□ node_modules/ NENÍ staged
□ __pycache__/ NENÍ staged
□ Žádné sensitive files
```

**STAGE:**
```bash
git add backend/app/api/*.py
git add docs/architecture/*.md
git add CHANGELOG.md
git add .ai-workflow/workplace/sessions/active/{file}.md
```

**NEVER:**
```bash
# ❌ NIKDY!
git add .env
git add config/secrets.yml
git add node_modules/
```

**If wrong files staged:**
```bash
git reset HEAD <file>
echo ".env" >> .gitignore
```

---

### Gate 5: Commit Message Format 🟢 MEDIUM

**Format:**
```
type(scope): description (YYYY-MM-DD HH:MM CET)
```

**Types:**
```
feat fix docs refactor test chore style perf ci
```

**Rules:**
```markdown
□ Type validní
□ Scope jasný
□ Description v imperativu ("add" not "added")
□ Description lowercase
□ Description BEZ tečky
□ Max 72 znaků (first line)
□ Timestamp přítomen
```

**Examples:**
```bash
# ✅ GOOD
feat(api): add legal_domains endpoint (2026-01-23 14:30 CET)
fix(parser): resolve merged cell duplication (2026-01-23 15:00 CET)
docs(api): update endpoint documentation (2026-01-23 16:00 CET)

# ❌ BAD
Added feature  # Missing type, scope, timestamp
Fixed bug      # Vague
WIP           # Not descriptive
```

**Template:**
```bash
git commit -m "type(scope): description ($(date '+%Y-%m-%d %H:%M CET'))"
```

---

### Gate 6: Testing (If Applicable) 🟢 MEDIUM

**When to run:**
```markdown
✅ Změnil jsi testovaný kód
✅ Nová feature
✅ Bug fix
✅ Refactoring

⏭️ Docs-only
⏭️ UI styling (no logic)
⏭️ PM říká "skip tests"
```

**Commands:**
```bash
cd backend && pytest tests/ -v
cd frontend && npm test
```

**Checklist:**
```markdown
□ Všechny testy prošly
□ Nové testy přidány (pokud feature)
□ Regression test (pokud bug fix)
□ Coverage >80% pro nový kód
□ Žádné flaky tests
```

**If TESTS FAIL:**
```markdown
1. Identify failing test
2. Fix code OR fix test
3. Re-run
4. Pokud stále fail → eskaluj PM

DON'T COMMIT failing tests bez PM approval!
```

---

## 📋 Quick Checklist (Copy-Paste)

```markdown
## Quality Gates Pre-Commit

Date: {YYYY-MM-DD HH:MM}
Task: {task-name}

### Gate 1: Logs 🔴
- [ ] Frontend clean
- [ ] Backend clean
- [ ] No new warnings

### Gate 2: Docs 🔴
- [ ] Impact analysis done
- [ ] All docs identified
- [ ] All docs updated
- [ ] Docs staged

### Gate 3: Cleanup 🟡
- [ ] No .tmp/.bak
- [ ] No debug statements
- [ ] No TODO in prod
- [ ] No credentials

### Gate 4: Git Status 🟡
- [ ] Code staged
- [ ] Docs staged
- [ ] Session staged
- [ ] No sensitive files

### Gate 5: Message 🟢
- [ ] Valid type/scope
- [ ] Imperative description
- [ ] Timestamp present

### Gate 6: Tests 🟢
- [ ] Tests run (if applicable)
- [ ] All passed
- [ ] New tests added

---

✅ ALL PASSED → Commit!
❌ ANY FAILED → Fix → Re-run
```

---

## 🔧 Common Failures

| Problem | Solution |
|---------|----------|
| Frontend errors | Fix import/syntax → retest |
| "Nevím jakou docs" | tree docs/ → check content → eskaluj PM |
| Tests fail | pytest -vv → identify → fix code/test |
| Wrong commit message | git commit --amend |
| Staged .env | git reset HEAD .env → add to .gitignore |

---

## 📊 Metrics

Track v session file:
```markdown
## Quality Gates Summary

Total Commits: 5
Gates:
- Gate 1: 5/5 ✅
- Gate 2: 5/5 ✅
- Gate 3: 5/5 ✅
- Gate 4: 5/5 ✅
- Gate 5: 5/5 ✅
- Gate 6: 4/5 ✅ (1 skip - docs-only)

Failures: None
Avg time: ~3 min per commit
```

---

## 🎯 Summary

```
1. 🔴 Logs Clean? → Yes
2. 🔴 Docs Updated? → Yes
3. 🟡 Code Clean? → Yes
4. 🟡 Git OK? → Yes
5. 🟢 Message OK? → Yes
6. 🟢 Tests Pass? → Yes
→ COMMIT!
```

**Time:** ~5 min per commit  
**ROI:** Prevents hours debugging

---

## 📚 Related

- [meta-prompt.md](meta-prompt.md) - Rule #0.2
- [task-complete.md](../quick-reference/task-complete.md) - Uses gates
- [git-commit-protocol.md](git-commit-protocol.md) - Commit workflow

---

**Remember:** Quality gates = safety net. No shortcuts!
