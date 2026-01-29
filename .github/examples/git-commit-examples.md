# Git Commit Examples

**Version:** 3.0.0  
**Last Updated:** 2026-01-24

---

## 🎯 Overview

Detailed examples for [git-commit-protocol.md](../core/git-commit-protocol.md)

---

## ✅ Good Commit Examples

### Example 1: Bug Fix (Single File)

**Scenario:** Fixed merged cell duplication in parser

```bash
git add backend/app/parsers/document_parser.py

git commit -m "fix(parser): resolve merged cell duplication (2026-01-23 14:30 CET)

- Skip already processed merged cells
- Add cell tracking set
- Update parsing logic"
```

**Why good:**
- ✅ One logical change (bug fix)
- ✅ Descriptive message
- ✅ Timestamp included
- ✅ Imperative mood

---

### Example 2: New Feature (Multiple Files)

**Scenario:** Add legal domains API endpoint

```bash
git add backend/app/api/v1/endpoints/legal_domains.py \
        backend/app/services/legal_domains_service.py \
        backend/tests/integration/test_legal_domains.py \
        docs/api-reference/legal-domains.md

git commit -m "feat(api): add legal_domains endpoint (2026-01-23 15:00 CET)

- Add GET /api/v1/legal-domains endpoint
- Implement service layer with caching
- Add integration tests (happy path + edge cases)
- Update API documentation"
```

**Why good:**
- ✅ One logical change (new feature)
- ✅ Multiple files OK (all part of feature)
- ✅ Includes side-effects (tests, docs)
- ✅ Descriptive commit message

---

### Example 3: Refactoring

**Scenario:** Extract legal domain logic to service

```bash
git add backend/app/api/v1/endpoints/legal_domains.py \
        backend/app/services/legal_domains_service.py \
        backend/tests/integration/test_legal_domains.py

git commit -m "refactor(api): extract legal domain logic to service (2026-01-23 16:00 CET)

- Move business logic from endpoint to service
- Update tests to test service directly
- No behavior changes"
```

**Why good:**
- ✅ One logical change (refactoring)
- ✅ Clear "no behavior changes"
- ✅ Tests updated

---

### Example 4: Docs Update (Standalone)

**Scenario:** Update API docs only (no code changes)

```bash
git add docs/api-reference/legal-domains.md

git commit -m "docs(api): clarify legal_domains response format (2026-01-23 17:00 CET)

- Add response schema examples
- Clarify error codes"
```

**Why good:**
- ✅ Standalone docs change
- ✅ Type: docs

---

### Example 5: Test Addition (Regression)

**Scenario:** Add regression test for bug fix

```bash
git add backend/app/parsers/document_parser.py \
        backend/tests/unit/test_document_parser.py

git commit -m "fix(parser): prevent merged cell duplication (2026-01-23 18:00 CET)

- Add regression test (proves bug exists)
- Fix merged cell handling
- Test now passes"
```

**Why good:**
- ✅ Test + fix together
- ✅ Mentions regression test

---

## ❌ Bad Commit Examples

### Example 1: Multiple Unrelated Changes

```bash
# ❌ BAD
git commit -m "fix(parser): fix merged cells and add legal domains endpoint"
```

**Why bad:**
- ❌ Two unrelated changes (bug fix + feature)
- ❌ Should be 2 separate commits

**Fix:**
```bash
# Commit 1
git commit -m "fix(parser): resolve merged cell duplication (2026-01-23 14:30 CET)"

# Commit 2 (later)
git commit -m "feat(api): add legal_domains endpoint (2026-01-23 15:00 CET)"
```

---

### Example 2: Missing Side-Effects

```bash
# ❌ BAD - Code only, missing docs
git add backend/app/api/legal_domains.py
git commit -m "feat(api): add legal domains endpoint"

# Separate commit for docs
git add docs/api-reference/legal-domains.md
git commit -m "docs: update api docs"
```

**Why bad:**
- ❌ Docs are part of feature, should be together
- ❌ Missing timestamp

**Fix:**
```bash
# ✅ GOOD - All together
git add backend/app/api/legal_domains.py \
        docs/api-reference/legal-domains.md \
        backend/tests/integration/test_legal_domains.py

git commit -m "feat(api): add legal_domains endpoint (2026-01-23 15:00 CET)

- Add GET /api/v1/legal-domains
- Update API documentation
- Add integration tests"
```

---

### Example 3: Vague Message

```bash
# ❌ BAD
git commit -m "Fixed bug"
git commit -m "WIP"
git commit -m "Updates"
```

**Why bad:**
- ❌ Not descriptive
- ❌ Missing type/scope
- ❌ Missing timestamp
- ❌ "WIP" never acceptable

**Fix:**
```bash
# ✅ GOOD
git commit -m "fix(parser): resolve merged cell duplication (2026-01-23 14:30 CET)"
```

---

### Example 4: Wrong Tense

```bash
# ❌ BAD
git commit -m "feat(api): added legal domains endpoint"
```

**Why bad:**
- ❌ Past tense ("added" instead of "add")
- ❌ Missing timestamp

**Fix:**
```bash
# ✅ GOOD
git commit -m "feat(api): add legal_domains endpoint (2026-01-23 15:00 CET)"
```

---

### Example 5: Commit Before PM Approval

```bash
# ❌ BAD - Committing without testing
git commit -m "feat(api): add endpoint"
# PM hasn't tested yet!
```

**Why bad:**
- ❌ PM hasn't approved
- ❌ Might need changes

**Fix:**
```bash
# ✅ GOOD
1. Implement feature
2. PM tests: "OK, funguje"
3. THEN commit
```

---

## 🎯 Real-World Workflow Example

### Scenario: Add Legal Domains API

**Step 1: Implement**
```bash
vim backend/app/api/v1/endpoints/legal_domains.py
vim backend/app/services/legal_domains_service.py
vim backend/tests/integration/test_legal_domains.py
vim docs/api-reference/legal-domains.md
```

**Step 2: Self-Test**
```bash
pytest backend/tests/integration/test_legal_domains.py
curl http://localhost:8000/api/v1/legal-domains
```

**Step 3: PM Approval**
```
AI: "Feature implementován. Můžeš otestovat endpoint?"
PM: "Zkouším... OK, funguje správně"
```

**Step 4: Commit**
```bash
git add backend/app/api/v1/endpoints/legal_domains.py \
        backend/app/services/legal_domains_service.py \
        backend/tests/integration/test_legal_domains.py \
        docs/api-reference/legal-domains.md

git commit -m "feat(api): add legal_domains endpoint ($(date '+%Y-%m-%d %H:%M CET'))

- Add GET /api/v1/legal-domains endpoint
- Implement service layer with caching
- Add integration tests (happy path + error cases)
- Update API documentation with examples"
```

**Step 5: Update Session File**
```markdown
## ✅ Completed Tasks

### Task 1: Legal Domains API
- Status: ✅ Completed
- Commit: a1b2c3d - feat(api): add legal_domains endpoint
- Files: 
  - backend/app/api/v1/endpoints/legal_domains.py
  - backend/app/services/legal_domains_service.py
  - backend/tests/integration/test_legal_domains.py
  - docs/api-reference/legal-domains.md
- PM Approved: 2026-01-23 15:00 CET
```

---

## 📚 Related

- [git-commit-protocol.md](../core/git-commit-protocol.md) - Full protocol
- [coding-standards.md](../core/coding-standards.md) - Rule #0.3
- [quality-gates.md](../core/quality-gates.md) - Pre-commit checks

---

**Remember:** One commit = One logical change + All side-effects + PM approved!
