---
applyTo: "**/*"
---

# 🧪 Testing Protocol

**Version:** 3.0.0  
**Last Updated:** 2026-01-24

---

## 🎯 Overview

**When to test:**
- **Regression:** Fixing bug → Run regression tests
- **New Feature:** Adding feature → Write + run new tests
- **Manual UAC:** PM approval critical → Manual walkthrough
- **Performance:** Optimization → Run performance tests

---

## 🚨 MANDATORY Rules

### Rule #1: Regression Tests for Bug Fixes

**Každý bug fix MUSÍ mít regression test!**

**Process:**
```markdown
1. Reproduce bug
2. Write test that FAILS (proves bug exists)
3. Fix bug
4. Test now PASSES
5. Commit test + fix together
```

**Example:** [examples/testing-examples.md#regression](../examples/testing-examples.md#regression)

### Rule #2: Tests for New Features

**Každý nový feature MUSÍ mít tests!**

**Coverage:**
- ✅ Happy path
- ✅ Edge cases
- ✅ Error handling
- ✅ Integration points

**Example:** [examples/testing-examples.md#new-feature](../examples/testing-examples.md#new-feature)

### Rule #3: Manual UAC When Required

**When:**
- Critical business logic
- User-facing feature
- Complex workflow
- PM explicitly requests

**Process:**
```markdown
1. Create test scenario
2. Step-by-step walkthrough
3. Document expected vs actual
4. PM confirms behavior
```

---

## 🧪 Test Types

### Unit Tests
**What:** Test individual functions/methods  
**When:** Complex logic, edge cases, algorithms  
**Tool:** pytest, jest  
**Location:** `tests/unit/`

### Integration Tests
**What:** Test multiple components together  
**When:** API endpoints, database operations  
**Tool:** pytest with test database, supertest  
**Location:** `tests/integration/`

### End-to-End Tests
**What:** Test complete user workflows  
**When:** Critical user journeys  
**Tool:** Playwright, Cypress  
**Location:** `tests/e2e/`

### Performance Tests
**What:** Test speed, load, resource usage  
**When:** Optimization tasks, scalability  
**Tool:** pytest-benchmark, k6  
**Location:** `tests/performance/`

---

## 📋 Decision Tree

**Should I write automated tests?**

```
Q: Is this a bug fix?
├─ YES → Regression test MANDATORY
└─ NO → Continue

Q: Is this a new feature?
├─ YES → Unit + integration tests MANDATORY
└─ NO → Continue

Q: Is this a refactoring?
├─ YES → Existing tests should still pass
└─ NO → Continue

Q: Is this docs/config only?
└─ NO → No tests needed (unless docs contain code examples)
```

**Should I do manual UAC?**

```
Q: Did PM explicitly request manual testing?
├─ YES → Do manual UAC
└─ NO → Continue

Q: Is this critical business logic?
├─ YES → Do manual UAC
└─ NO → Continue

Q: Is this user-facing feature?
├─ YES → Do manual UAC
└─ NO → Automated tests sufficient
```

---

## 🚀 Running Tests

### Python (Backend)
```bash
# All tests
pytest

# Specific file
pytest tests/integration/test_legal_domains.py

# With coverage
pytest --cov=app --cov-report=html

# Specific test
pytest tests/test_parser.py::test_merged_cells
```

### TypeScript (Frontend)
```bash
# All tests
npm test

# Watch mode
npm test -- --watch

# Coverage
npm test -- --coverage

# Specific test
npm test -- Header.test.tsx
```

### E2E Tests
```bash
# Playwright
npx playwright test

# Cypress
npx cypress run
```

---

## 📊 Test Quality Checklist

```markdown
□ Test names descriptive (test_should_return_legal_domains_for_valid_query)
□ Arrange-Act-Assert pattern
□ Independent (no dependencies between tests)
□ Fast (avoid sleep/delays when possible)
□ Reliable (no flaky tests)
□ Clean test data
```

---

## 🎯 Examples

Detailed test examples: [examples/testing-examples.md](../examples/testing-examples.md)

**Quick Examples:**

**Regression Test:**
```python
def test_merged_cells_not_duplicated():
    # Arrange: Create merged cell scenario
    # Act: Parse document
    # Assert: No duplicates
```

**New Feature Test:**
```python
def test_legal_domains_endpoint():
    # Happy path
    # Edge cases
    # Error handling
```

---

## 📚 Related

- [coding-standards.md](coding-standards.md) - Test structure
- [quality-gates.md](quality-gates.md) - Gate #6 (Tests)
- [examples/testing-examples.md](../examples/testing-examples.md) - Full examples

---

**Remember:** Bug fix = regression test, New feature = full test coverage!
