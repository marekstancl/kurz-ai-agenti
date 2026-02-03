---
applyTo: "**/*"
---

# 🎯 Session Management

**Version:** 3.0.0  
**Last Updated:** 2026-01-24

---

## 🎯 Overview

**Session = jednotka práce AI s jasným začátkem, průběhem a koncem.**

**Typy sessions:**
- **Single Session:** Jeden task, dokončen za 1 chat
- **Epic Session:** Velký task, více sub-sessions
- **Handoff Session:** Přebírání práce od jiné AI

---

## 📋 Session Lifecycle

### Session Templates

**Available templates in `.github/templates/`:**
- `session-bug-fix.md` - Bug fix sessions with investigation log
- `session-new-feature.md` - Feature development with design docs
- `session-refactoring.md` - Refactoring sessions with before/after
- `session-exploration.md` - Codebase exploration sessions
- `epic-breakdown.md` - Multi-session epic planning

**Usage:** Copy appropriate template to `workspace/sessions/active/YYYY-MM-DD-{type}-{topic}.md`

**Session File Naming Convention:**
```
{YYYY-MM-DD}-{type}-{descriptive-name}.md

Examples:
- 2026-01-28-bug-fix-login-validation.md
- 2026-01-28-new-feature-user-profile.md
- 2026-01-28-refactoring-database-layer.md
- 2026-01-28-exploration-api-structure.md
- 2026-01-28-hotfix-payment-processing.md
```

**Types:**
- `bug-fix` - Fix existing bug/issue
- `new-feature` - Implement new feature
- `refactoring` - Code cleanup/restructuring
- `exploration` - Investigation/research
- `hotfix` - Emergency production fix

### 1. Session Initialization

**Command:**
```markdown
Přečti si [new-chat.md](../quick-reference/new-chat.md) a inicializuj session.
```

**AI actions:**
```markdown
1. Čti new-chat.md (MANDATORY)
2. Identifikuj typ session (bug-fix, new-feature, refactoring, exploration)
3. Vytvořit `YYYY-MM-DD-{type}-{topic}.md` (viz naming convention výše)
4. Generate AI name
5. PM vyplní task description
6. Analyze:
   □ Project structure
   □ Dependencies
   □ Related files
   □ Risk faktory
7. Create Think-First Plan (see think-first.md)
```

**Session File Structure:**
```markdown
# Session: [Task Name]
- **AI Name:** [name]
- **Created:** YYYY-MM-DD HH:MM CET
- **PM:** [name]
- **Status:** 🔵 In Progress

## 🎯 Objective
[What to accomplish]

## 📋 Think-First Plan
[6-step plan from think-first.md]

## 📊 Progress Tracking
- [ ] Task 1
- [ ] Task 2

## ✅ Completed Tasks
[After PM approval]

## 🔄 Handoff Notes
[For next AI if needed]
```

### 2. Work Loop

**Standard Work Pattern:**
```markdown
Loop:
   1. Implement change
   2. PM tests/approves
   3. Update documentation per documentation-protocol.md (if affected)
   4. Commit (see git-commit-protocol.md)
   5. Update session file
   6. Next task or finish
```

**Quality Gates:**
- Every commit → Run quality gates ([quality-gates.md](quality-gates.md))
- Before PM approval → Self-test

### 3. Session Completion

**Command:**
```markdown
Přečti si [task-complete.md](../quick-reference/task-complete.md) a ukonči session.
```

**AI actions:**
```markdown
1. Čti task-complete.md (MANDATORY)
2. Run final quality gates
3. Update documentation per documentation-protocol.md (if affected)
4. Update session file:
   - Status: ✅ Completed
   - All commits listed
   - All files changed
5. Generate completion summary
6. Ask PM: Close or continue?
7. Update `workspace/session-log.md` (přidej záznam nahoru + statistiky)
```

**Completion Checklist:**
```markdown
□ All tasks completed
□ All commits done
□ Quality gates pass
□ Session file updated
□ Session log updated (workspace/session-log.md)
□ PM confirmed done
```

### 4. Handoff (Optional)

**When:**
- Session unfinished (PM busy, context too large, etc.)
- Complex epic spanning multiple chats

**Command:**
```markdown
Přečti si [handoff.md](../quick-reference/handoff.md) a vytvoř handoff.
```

**Handoff Structure:**
```markdown
## 🔄 Handoff Notes

**From AI:** [current AI name]
**Date:** YYYY-MM-DD HH:MM CET

### ✅ Completed
- [x] Task 1 (Commit: a1b2c3d)
- [x] Task 2 (Commit: e4f5g6h)

### 🔜 Next Steps
1. [Next task]
2. [Considerations]

### ⚠️ Important Context
- [Critical info]
- [Gotchas]
- [Dependencies]

### 🗺️ Where to Find Things
- Logs: [location]
- Config: [location]
- Tests: [location]
```

---

## 🏔️ Epic Sessions

**Epic = velký task requiring multiple sub-sessions**

### Epic Structure

**Main Epic File:** `EPIC-[name].md`
```markdown
# Epic: [Name]
- **Created:** YYYY-MM-DD
- **PM:** [name]
- **Status:** 🔵 In Progress

## 🎯 Epic Objective
[High-level goal]

## 📋 Sub-Sessions
1. [SESSION-2026-01-23.md] - ✅ Create database schema
2. [SESSION-2026-01-24.md] - 🔵 API endpoints
3. [SESSION-TBD.md] - ⏸️ Frontend integration

## 🎯 Progress
25% complete (1/4 sub-sessions)
```

**Sub-Session Files:** `YYYY-MM-DD-{type}-{topic}.md` (normal structure, one per sub-session)

**Cross-References:**
- Sub-session → Epic file (link in objective)
- Epic file → All sub-sessions (listed)

### Epic Workflow

```markdown
1. Create epic file
2. Break down into sub-sessions (in epic file)
3. Execute sub-sessions:
   - New chat → new session → link to epic
   - Complete → update epic file
4. Epic complete when all sub-sessions done
```

---

## 🚨 Common Mistakes

**❌ WRONG:**
- Začneš kódit bez Think-First Plan
- Session file neaktualizuješ
- Commitneš bez PM schválení
- Zapomeneš quality gates
- Handoff bez context

**✅ RIGHT:**
- new-chat.md → Think-First → Implement
- Session file aktuální
- Commit po PM schválení
- Quality gates vždy
- Handoff s full context

---

## 📚 Related

- [new-chat.md](../quick-reference/new-chat.md) - Session start
- [task-complete.md](../quick-reference/task-complete.md) - Session end
- [handoff.md](../quick-reference/handoff.md) - Handoff process
- [think-first.md](think-first.md) - Planning
- [git-commit-protocol.md](git-commit-protocol.md) - Commits
- [quality-gates.md](quality-gates.md) - Pre-commit checks

---

**Remember:** Session = Think-First → Work Loop → Quality Gates → Complete!
