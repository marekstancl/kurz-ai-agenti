---
applyTo: "**/*"
---

# 🔧 Refactoring Workflow

**Version:** 3.0.0  
**Last Updated:** 2026-01-23  
**Template:** .github/templates/session-refactoring.md

---

## 🎯 Purpose

Restructure code WITHOUT changing functionality. Tests must pass before AND after.

**✅ Use when:** Code duplication, tight coupling, poor naming, long functions, hard to test

**❌ Don't use:** Adding features (→ new-feature.md), fixing bugs (→ bug-fix.md)

**⚠️ CRITICAL:** Zero behavior change. Tests fail = you broke something!

---

## 🎭 Role: Safety Officer

**Mindset:** Safety FIRST > Code Quality > Speed

**Rules:**
- Tests pass BEFORE refactoring (baseline)
- Small incremental changes
- Test after EACH step
- Rollback if breaks
- Zero behavior changes

**Decision:** Will behavior change? YES → Not refactoring! NO → Proceed ✅

---

## 🔄 Process (9 Steps)

```
Step 0: Think-First Plan (MANDATORY) → Wait for PM approval
Step 1: Create Session + Branch
Step 2: Establish Baseline (all tests MUST PASS)
Step 3: Analyze Architecture
Step 4: Design Solution
Step 5: Add Tests (if coverage <80%)
Step 6: Refactor Incrementally (test after EACH step)
Step 7: Verify No Regressions
Step 8: Clean Up & Document
Step 9: Commit
```

---

## STEP 0: Think-First Plan

**See:** `think-first.md` for template

**Key sections:**
- Current problems
- Refactoring strategy (Extract Method/Class/etc)
- Incremental steps (test after each)
- Safety measures
- Rollback plan

**Wait for PM approval (GO/REVISE)!**

---

## STEP 1: Session + Branch

```bash
# Create session
cp .ai-workflow/templates/session-refactoring.md \
   .ai-workflow/workplace/sessions/active/$(date +%Y-%m-%d)-{topic}.md

# Create branch
git checkout -b session/$(date +%Y-%m-%d)-refactor-{topic}
```

---

## STEP 2: Establish Baseline

**🚨 Tests MUST pass before refactoring!**

```bash
{test command from project-guide.md}
```

**If tests fail:** STOP. Fix failures first (bug-fix session) or ask PM.

**If tests pass:** Document baseline, proceed to Step 3.

---

## STEP 3: Analyze Architecture

Document:
- Files involved
- Key functions/classes
- Dependencies
- Current issues (location, impact)
- Metrics (lines, complexity, coverage)

---

## STEP 4: Design Solution

Choose pattern:
- Extract Method/Class
- Rename
- Remove Duplication
- Simplify Conditional
- etc.

Document before/after structure.

---

## STEP 5: Add Tests

Check coverage:
```bash
{coverage command from project-guide.md}
```

**If <80%:** Write missing tests BEFORE refactoring.

---

## STEP 6: Refactor Incrementally

**🚨 CRITICAL:** Small steps, test after EACH!

For each step:
1. Make change
2. Run tests → Must PASS
3. Commit
4. Next step

**If tests fail:** Review → Fix OR Rollback (`git reset --hard HEAD~1`)

---

## STEP 7: Verify No Regressions

Run full test suite:
```bash
{test command}
```

Compare with baseline:
- Same tests passing? ✅
- Coverage maintained? ✅
- Performance OK? ✅

---

## STEP 8: Clean Up

- Remove commented code
- Update docstrings
- Format code
- Run linter
- Update docs

---

## STEP 9: Commit

**See:** `git-commit-protocol.md`

Format:
```
refactor(scope): description (YYYY-MM-DD HH:MM CET)

- What was refactored
- Why (problems solved)
- Pattern used

Metrics:
- Lines: X → Y
- Complexity: X → Y
- Tests: All pass (X/X)

No behavior changes
```

---

## 🚨 Escalate If

- Baseline tests fail
- Tests fail during refactoring (after attempts)
- Behavior inadvertently changes
- Performance degrades >20%
- Scope grows
- Uncertain about safety

**Format:**
```markdown
🚨 REFACTORING ESCALATION

Issue: {what went wrong}
Step: {which step}
Problem: {what happened}
Rollback available: {Yes - commit hash}

Options:
A) Rollback and revise
B) Fix and continue
C) Stop (too risky)

Recommendation: {A/B/C} because {reason}
```

---

## 📚 Related

- `meta-prompt.md` - Role (Safety Officer)
- `think-first.md` - Planning (Step 0)
- `project-guide.md` - Test/coverage commands
- `quality-gates.md` - Pre-commit checks
- `git-commit-protocol.md` - Commit format
- `testing-protocol.md` - Coverage standards
- `coding-standards.md` - Code quality

For examples, see: `examples/` folder
