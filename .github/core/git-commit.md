---
applyTo: "**/*"
---

# 🔀 Git Commit Protocol

**Version:** 3.0.0  
**Last Updated:** 2026-01-24

---

## 🎯 Overview

**Problem:** AI commitne více změn najednou → těžký review a rollback

**Solution:** **ATOMIC COMMITS** - jedna logická změna = jeden commit

**Proč:**
- Snadnější review
- Snadnější rollback
- Lepší git historie
- Lepší debugging (git bisect)

---

## 🚨 MANDATORY Rules

### Rule #1: Commit Po PM Schválení

**VŽDY až PO schválení PM, ne před!**

```
1. Implementuj změnu
2. PM otestuje/schválí
3. TEPRVE TEĎ commitni
4. Pokračuj na další
```

### Rule #2: Atomic Commits

**Jeden commit = jedna logická změna**

**Je logická změna:**
- ✅ Jeden bug fix
- ✅ Jeden feature (i více souborů)
- ✅ Jeden refactoring krok
- ✅ Jedna docs aktualizace

**NENÍ logická změna:**
- ❌ Bug fix + feature v jednom
- ❌ Více nezávislých bug fixů
- ❌ Kód + docs (pokud docs není součást změny)

**Exception:** Docs přímo součástí změny (API endpoint + jeho docs) = OK v jednom commitu

### Rule #3: Commit Message Format

```
type(scope): description (YYYY-MM-DD HH:MM CET)
```

**Types:**
```
feat fix docs refactor test chore style perf ci
```

**Rules:**
```markdown
□ Imperativ ("add" not "added")
□ No period at end
□ Lowercase
□ Max 72 znaků (first line)
□ Timestamp VŽDY
```

**Examples:**
```bash
# ✅ GOOD
feat(api): add legal_domains endpoint (2026-01-23 14:30 CET)
fix(parser): resolve merged cell duplication (2026-01-23 15:00 CET)

# ❌ BAD
Added feature  # Missing type, scope, timestamp
Fixed bug      # Vague
WIP           # Not descriptive
```

### Rule #4: Include Side-Effects

**Commit MUSÍ obsahovat všechny side-effects:**
- ✅ Docs updates
- ✅ Test updates
- ✅ Migration files
- ✅ Config changes

```bash
# ❌ WRONG - separate commits
git commit -m "feat(api): add endpoint"
git commit -m "docs(api): update docs"  # Separate!

# ✅ RIGHT - all together
git commit -m "feat(api): add legal_domains endpoint (2026-01-23 14:30 CET)

- Add GET /api/v1/legal-domains
- Update API docs
- Update ERD
- Add tests"
```

---

## 📋 Commit Workflow

### Step 1: Implement
```bash
vim backend/app/api/legal_domains.py
vim docs/api-reference/legal-domains.md
vim backend/tests/test_legal_domains.py
```

### Step 2: PM Approval
```
AI: "Feature implementován. Můžeš otestovat?"
PM: "OK, funguje"
→ Pokračuj Step 3
```

### Step 3: Commit
```bash
git add backend/app/api/legal_domains.py \
        docs/api-reference/legal-domains.md \
        backend/tests/test_legal_domains.py

git commit -m "feat(api): add legal_domains endpoint ($(date '+%Y-%m-%d %H:%M CET'))

- Add GET /api/v1/legal-domains endpoint
- Update API documentation
- Add integration tests"
```

### Step 4: Update Session File
```markdown
## ✅ Completed Tasks

### Task 1: Legal Domains API
- Status: ✅ Completed
- Commit: a1b2c3d - feat(api): add legal_domains endpoint
- Files: backend/app/api/legal_domains.py, docs/..., tests/...
```

---

## ⚠️ Common Mistakes

**❌ WRONG:**
- Commitneš bez PM schválení
- Více logických změn v jednom
- Commit bez side-effects
- Message bez timestampu
- Minulý čas ("added" instead of "add")

**✅ RIGHT:**
- Čekáš na PM schválení
- Jeden commit = jedna změna
- Obsahuje side-effects
- Message s timestampem
- Imperativ

---

## 🎯 Examples

Viz [examples/git-commit-examples.md](../examples/git-commit-examples.md)

---

## 📚 Related

- [coding-standards.md](coding-standards.md) - Rule #0.3
- [quality-gates.md](quality-gates.md) - Pre-commit checks
- [session-management.md](session-management.md) - Session workflow

---

**Remember:** Commit = PM schválil + jedna změna + všechny side-effects!
