---
applyTo: "**/*"
---

---
template: .github/templates/session-bug-fix.md
---

## 📋 Bug Fix Completion Checklist

**Before marking bug as fixed:**
```markdown
□ Bug reproduced successfully (Step 3)
□ Root cause identified and documented (Step 4)
□ Regression test written and FAILED before fix (Step 5)
□ Fix designed to address root cause (Step 6)
□ Fix implemented following coding standards (Step 7)
□ Regression test now PASSES (Step 8)
□ All existing tests still PASS (Step 8)
□ Manual verification complete (Step 8)
□ Quality gates passed (Step 8)
□ ⚠️ PM REVIEW REQUIRED (Step 8.5) - BEFORE COMMIT
  □ AI describes what was fixed
  □ AI explains how it was fixed (code changes)
  □ AI confirms testing done (per testing-protocol.md)
  □ AI proposes PM testing steps
  □ PM approves before proceeding to commit
□ Documentation updated (Step 9)
□ Session file complete (Step 9)
□ bugs.md updated (Step 9 - if applicable)
□ Committed with proper message (Step 9)
□ Commit hash recorded (Step 9)
□ PM notified (Step 9)

All checked: ✅ Bug fix complete!
```

---

## 🚨 Escalation Triggers

**MUST escalate to PM if:**

### Critical Situations

- ❌ **Cannot reproduce** bug after 3 attempts
- ❌ **Root cause unclear** after thorough investigation
- ❌ **Fix requires breaking change** (API, database schema, etc.)
- ❌ **Security implications** (data exposure, authentication, authorization)
- ❌ **Production data affected** (need migration, data fix)
- ❌ **External dependency issue** (third-party library, API, service)
- ❌ **Performance implications** (fix might be slow)
- ❌ **Uncertain about correct behavior** (spec unclear, business logic ambiguous)

### Escalation Format
```markdown
🚨 HUMAN REVIEW REQUIRED

**Trigger:** {What triggered escalation}

**Context:**
{What you were doing when you encountered the issue}

**Investigation Done:**
- {Step 1 completed}
- {Step 2 completed}
- {Where you got stuck}

**Question:**
{Specific question that needs PM input}

**Options:**
A) {Option A}
   - Pros: {advantages}
   - Cons: {disadvantages}
   
B) {Option B}
   - Pros: {advantages}
   - Cons: {disadvantages}

C) {Option C - if applicable}
   - Pros: {advantages}
   - Cons: {disadvantages}

**Recommendation:** {A/B/C} because {reasoning}

**Need your decision to proceed.**
```

---

## 📚 Related Files

**For PM:**
- `pm-commands.md` - Quick commands for bug reporting/fixing
- `bug-report.md` - How to report bugs
- `new-chat.md` - Starting bug fix session

**For AI:**
- `meta-prompt.md` - Role & Mindset (Detective/Debugger)
- `think-first.md` - Planning bug fix approach (Step 1)
- `project-guide.md` - Project-specific commands (test, logs, start)
- `quality-gates.md` - Pre-commit verification (Step 8)
- `git-commit-protocol.md` - Commit format and workflow (Step 9)
- `testing-protocol.md` - Regression testing details (Step 5)
- `coding-standards.md` - Code quality requirements (Step 7)
- `task-complete.md` - Task completion workflow
- `handoff.md` - Session completion (if bug fix ends session)

**Tracking:**
- `workplace/bugs.md` - Bug tracking file

---

## 📝 Examples

**Multi-session patterns:** Viz [examples/template-examples.md](../examples/template-examples.md) pro rozdělení práce do 3 sessions s povinným PM GO mezi fázemi.

### Example 1: Critical Backend Bug

**Bug:** TM storage doesn't save customer_id

**PM command:**
```markdown
Oprav bug BUG-20260123-1430 z bugs.md.
```

**AI workflow:**
```markdown
✅ Loaded bug context from bugs.md

## Step 1: Think-First Plan

**Bug:** BUG-20260123-1430 - TM storage neukládá customer_id
**Component:** backend
**Priority:** high
**Role:** Detective/Debugger

Plan:
1. Reproduce (15 min)
2. Root cause analysis (30 min)
3. Regression test (30 min)
4. Design fix (15 min)
5. Implement (20 min)
6. Verify (20 min)

Můžu pokračovat?
```

**PM:** GO
```markdown
## Step 2: Session Created

✅ Session: sessions/active/2026-01-23-tm-customer-id-bug.md
✅ Branch: session/2026-01-23-tm-customer-id-bug

## Step 3: Reproduced

✅ Bug reproduced
- Created TM entry via API
- Checked DB: customer_id is NULL ✅ Bug confirmed

## Step 4: Root Cause

Root cause: tm_service.py line 52 missing customer_id parameter in model
Introduced: Commit abc123 (refactoring, 2 days ago)

## Step 5: Regression Test

✅ Test written: test_create_tm_entry_saves_customer_id
❌ Test FAILS (expected)

## Step 6: Fix Design

Add customer_id to TranslationMemory() constructor
Add validation

## Step 7: Implemented

✅ Fixed tm_service.py
✅ Added validation
✅ Added logging

## Step 8.5: PM Review (⚠️ MANDATORY GATE)

### What was fixed?
Bug BUG-20260123-1430: TranslationMemory didn't save customer_id field to database.

### How was it fixed?
**File:** backend/app/services/tm_service.py  
**Change:** Added `customer_id` parameter to `TranslationMemory()` constructor at line 52
**Details:**
- Before: `tm = TranslationMemory(text=text, language=language)`
- After: `tm = TranslationMemory(text=text, language=language, customer_id=customer_id)`
- Added validation: customer_id must be non-null UUID
- Added logging: Records customer_id for audit trail

### Testing completed (per testing-protocol.md)
✅ **Regression test:** test_create_tm_entry_saves_customer_id (PASSES)  
✅ **Unit tests:** All 45 existing tests PASS  
✅ **Manual verification:** Created TM entry via API, verified DB has customer_id  
✅ **Edge cases:** Tested with null customer_id (validation error, expected)

### How to verify (for PM)
1. **Quick check:** `curl -X POST http://localhost:8000/api/tm -d '{"text": "test", "customer_id": "<UUID>"}' | grep customer_id` → should show customer_id
2. **Database check:** `SELECT customer_id FROM translation_memory ORDER BY created_at DESC LIMIT 1;` → should NOT be NULL
3. **UI check:** Verify TM settings filters by customer work correctly
4. **Regression:** `pytest tests/test_tm.py -v` → all PASS

**Status: Ready for commit. Waiting for PM approval to proceed.**

---

**[After PM GO]**

## Step 8: Verified

✅ Regression test PASSES
✅ All tests PASS (45/45)
✅ Manual check: customer_id saved ✅

## Step 9: Committed

Commit: a1b2c3d - fix(tm): resolve customer_id not saved
bugs.md updated: ✅ Fixed

✅ Bug Fix Complete!
```

---

### Example 2: Frontend UI Bug

**Bug:** Button hover color incorrect

**PM:** "Bug: Settings page button má špatnou hover barvu. Priorita: low"

**AI workflow:**
```markdown
## Step 1: Think-First

Bug: Button hover color
Priority: low
✅ No regression in other button colors

## Step 8.5: PM Review (⚠️ MANDATORY GATE)

### What was fixed?
Button hover color on Settings page showing wrong shade of blue.

### How was it fixed?
**File:** frontend/src/pages/SettingsPage.tsx  
**Change:** Line 45, CSS class name correction
- Before: `className="hover:bg-blue-400"`
- After: `className="hover:bg-blue-600"`

### Testing completed (per testing-protocol.md)
✅ **Visual test:** Hover color now matches design spec (blue-600)  
✅ **Regression check:** Verified no other buttons use same class  
✅ **Browser check:** Tested in Chrome, Firefox (renders correctly)

### How to verify (for PM)
1. **Visual:** Go to Settings page, hover over button → color should be blue-600 (darker blue)
2. **CSS inspection:** Right-click button → inspect → check computed background-color: `rgb(37, 99, 235)` (blue-600 value)
3. **Regression:** Check other buttons still have correct hover colors
4. **Build:** `npm run build` → no errors

**Status: Ready for commit. Waiting for PM approval to proceed.**

---

**[After PM GO]**
Role: Detective/Debugger

Quick fix, estimated 30 min total

Můžu pokračovat?
```

**PM:** GO
```markdown
## Steps 2-3: Reproduce

✅ Found button in SettingsPage.tsx
✅ Hover shows blue-400, should be blue-600

## Step 4: Root Cause

Line 45: className="hover:bg-blue-400"
Should be: hover:bg-blue-600
Likely typo or copy-paste from different button

## Step 5: Regression Test

Visual test (manual verification sufficient for CSS)

## Step 6-7: Fix

Changed: hover:bg-blue-400 → hover:bg-blue-600

## Step 8: Verified

✅ Visual check: Color correct
✅ No other button affected

## Step 9: Committed

Commit: b2c3d4e - fix(ui): correct settings button hover color

✅ Complete (30 min total)
```

---

### Example 3: Intermittent Bug (Escalation)

**Bug:** API sometimes returns 500

**AI workflow:**
```markdown
## Steps 1-3: Attempted Reproduction

Tried 10 times: Bug appeared 2/10 times
Inconsistent - intermittent bug

## Step 4: Root Cause Investigation

Checked:
- Logs: No clear pattern
- Code: No obvious race condition
- Database: Connection pool seems OK

Cannot identify root cause from code inspection alone.

🚨 ESCALATION NEEDED

**Trigger:** Intermittent bug, unclear root cause

**Investigation:**
- Reproduced 2/10 times
- No consistent pattern
- Logs don't show clear error

**Options:**
A) Add extensive logging and monitor in staging
B) Review recent changes more thoroughly
C) Investigate database connection pool settings

**Recommendation:** A - Add logging to identify pattern

Need guidance on how to proceed.
```

---

**Remember: Detective mindset → Find root cause → Test → Fix → Verify → Document!**