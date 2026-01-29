---
applyTo: "**/*"
---

# 📤 Handoff Quick Reference

**Version:** 3.0.0  
**Last Updated:** 2026-01-24

---

## 🎯 Purpose

**What:** Transfer work between chats or complete session

**When:** Token limit, session complete, end of day, PM request

**Key:** Handoff must be self-contained for next AI

---

## 🧭 Decision Tree

```
Session complete (all tasks done)?
├─ YES → Full Handoff
│   ├─ Merge branch to main
│   ├─ Delete branch
│   └─ Archive session file
│
└─ NO → Mini Handoff
    ├─ Update session file
    ├─ Keep branch active
    └─ Session stays in active/
```

---

## 🔄 Common Steps (Both Types)

### Step 0: Pre-Handoff Verification
```markdown
□ All changes committed
□ Quality gates passed
□ Documentation updated
□ Session file current
□ Git status clean
```

### Step 1: Session File Final Update
```markdown
## 📤 HANDOFF - {Mini|Full} ({YYYY-MM-DD HH:MM CET})

**Session Type:** {bug-fix|new-feature|refactoring|exploration|hotfix}
**Handoff Type:** {Mini|Full}
**Reason:** {reason}

### Session Summary
- Started: {date}
- Duration: {time}
- Tasks: {N/M} complete
- Commits: {list}
- Files changed: {list}

### Next Steps
{For Mini: Next task}
{For Full: "Session complete"}

### Known Issues
{Any warnings}
```

---

## 🔹 Mini Handoff (Session Continues)

**When:**
- Task done, more tasks remain
- Token limit approaching
- End of day, resume tomorrow

**Process:**
```markdown
1. Update session file (status: active)
2. Generate UNIFIED HANDOFF blok
3. Confirm to PM

Branch: STAYS ACTIVE
File: STAYS in active/
```

**UNIFIED HANDOFF Blok:**
```markdown
## 📦 UNIFIED HANDOFF - NEW CHAT
```markdown
Pokračujeme v session.

Načti:
1. .ai-agent-framework/core/meta-prompt.md
2. .ai-agent-framework/core/project-guide.md
3. .ai-agent-framework/sessions/active/{YYYY-MM-DD}-{type}-{topic}.md

Session: {date}-{type}-{topic}
Branch: session/{date}-{topic}

Dokončeno: {N/M} tasks
Poslední: {task} (commit: {hash})
Aktuální: Task {N+1}: {name}

Další krok:
1. Verify branch
2. Review last task
3. Continue with Task {N+1}
4. Think-First approach

Komunikuj v češtině.
```
```

---

## 🔹 Full Handoff (Session Complete)

**When:**
- All session tasks complete
- Session goal achieved

**Process:**
```markdown
1. Final quality gates
2. Update session file (status: completed)
3. Git merge session → main (MANDATORY)
4. Delete session branch (MANDATORY)
5. Archive session file (MANDATORY)
6. Update session log (workspace/session-log.md - přidej nahoru + statistiky)
7. Generate handoff summary
```

### Merge & Delete Branch
```bash
# Current branch
BRANCH=$(git branch --show-current)

# Merge to main
git checkout main
git merge "$BRANCH" --no-ff -m "Merge $BRANCH into main"
git push origin main 2>/dev/null || true

# Delete branch
git branch -d "$BRANCH"
git push origin --delete "$BRANCH" 2>/dev/null || true
```

### Archive Session File
```bash
# Move to completed
mv sessions/active/{YYYY-MM-DD}-{type}-{topic}.md sessions/completed/{YYYY-MM-DD}-{type}-{topic}.md

# Commit
git add sessions/
git commit -m "docs(session): archive {YYYY-MM-DD}-{type}-{topic} ($(date '+%Y-%m-%d %H:%M CET'))"
```

### Update Session Log
```markdown
| Date | Session File | Session Type | Status | Achievement |
|------|-----------|------|--------|-------------|
| {date} | {YYYY-MM-DD}-{type}-{topic}.md | bug-fix\|new-feature\|refactoring\|exploration\|hotfix | ✅ Complete | {summary} |
```

---

## ✅ Validation

### Mini Handoff
```markdown
□ Session file updated
□ UNIFIED HANDOFF generated
□ Branch active
□ File in active/
□ PM notified
```

### Full Handoff
```markdown
□ Quality gates passed
□ Session status: completed
□ Branch merged to main
□ Branch deleted
□ File archived to completed/
□ File NOT in active/
□ Session log updated (workspace/session-log.md - záznam nahoru + statistiky)
□ Git status clean
```

---

## 🚨 Common Mistakes

**❌ NEVER:**
- Skip git merge for full handoff
- Skip branch deletion for full handoff
- Leave file in active/ after full handoff
- Forget session log update

**✅ ALWAYS:**
- Merge + delete for full handoff
- Archive file for full handoff
- Generate UNIFIED HANDOFF blok
- Verify git status clean

---

## 📚 Related

- [session-management.md](../core/session-management.md) - Session lifecycle
- [task-complete.md](task-complete.md) - Task completion
- [quality-gates.md](../core/quality-gates.md) - Pre-handoff checks

---

**Remember:** Mini = Continue, Full = Merge + Archive + Complete!
