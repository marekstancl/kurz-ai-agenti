---
applyTo: "**/*"
---

# ✅ Task Complete Quick Reference

**Version:** 3.0.0  
**Last Updated:** 2026-01-24

---

## 🎯 Purpose

**What:** Complete workflow after PM approves task

**When:** PM says "task done" or "commit this"

**Key:** One task = atomic commit with all side-effects

---

## 📋 Workflow (Sequential - DO NOT SKIP!)

### Step 1: Quality Gates (MANDATORY)
```markdown
□ Gate 1: Logs clean
□ Gate 2: Docs updated
□ Gate 3: Code cleanup
□ Gate 4: Git status OK
□ Gate 5: Commit message ready
□ Gate 6: Tests passing

See: quality-gates.md
```

### Step 2: Documentation Impact
```markdown
What changed? → Which docs affected? → Update docs → Stage docs
```

**See:** [documentation-protocol.md](../core/documentation-protocol.md) for Docusaurus standards:
- MDX escaping (curly braces, `<` symbols)
- Sidebar IDs (no numeric prefixes)
- YAML frontmatter (required fields)
- Test: `cd docs && npm run build`

### Step 3: Update Session File
```markdown
## ✅ Task Completed: {Name}

**Date:** {YYYY-MM-DD HH:MM CET}
**Commit:** {hash} (add in Step 5)
**Duration:** {time}

### Summary
{Brief technical description}

### Changed Files
- {file1} - {what changed}

### Documentation Updated
- {doc1} - {what updated}

### Tests
- Unit: {status}
- Integration: {status}

### Quality Gates
All gates: ✅ PASS

### Next Task
{Next OR "Session complete"}
```

### Step 4: Atomic Commit
```bash
git add {all-files}
git commit -m "type(scope): description ($(date '+%Y-%m-%d %H:%M CET'))"
```

**Format:**
- `feat(api): add legal_domains endpoint`
- `fix(parser): resolve merged cell duplication`
- `docs(api): update endpoint documentation`

**See:** [git-commit-protocol.md](../core/git-commit-protocol.md)

### Step 5: Update Commit Hash
```bash
# Get hash
HASH=$(git log -1 --format="%H")

# Update session file with hash
# Commit update
git add sessions/active/{file}.md
git commit -m "docs(session): add commit hash ($(date '+%Y-%m-%d %H:%M CET'))"
```

### Step 6: Update Session Log (if task completes session)
```markdown
Pokud je to poslední task v session:
1. Otevři workspace/session-log.md
2. Přidej záznam NAHORU (reverse chrono)
3. Aktualizuj statistiky
4. Přidej do commit
```

### Step 7: Confirm to PM
```markdown
✅ Task Complete: {Name}

**Commit:** {hash} - {message}
**Files:** {count} changed
**Docs:** {list}
**Tests:** {status}
**Quality Gates:** ✅ All passed

**Next:** {Next task OR "Session complete - ready for handoff"}
**Progress:** {N/M} tasks complete
```

---

## ✅ Checklist
```markdown
### Pre-Commit
- [ ] Quality gates passed
- [ ] Docs updated
- [ ] Session file updated
- [ ] All changes staged

### Commit
- [ ] Commit message follows format
- [ ] Timestamp included
- [ ] Commit executed

### Post-Commit
- [ ] Hash obtained
- [ ] Session file updated with hash
- [ ] Hash update committed
- [ ] Session log updated (if last task - workspace/session-log.md)
- [ ] PM notified
```

---

## 🚨 Common Mistakes

**❌ NEVER:**
- Commit without quality gates
- Forget documentation
- Missing commit timestamp
- Forget to update session file

**✅ ALWAYS:**
- Run quality gates first
- Update all docs
- Include timestamp
- Update session file with hash
- Confirm to PM

---

## 📚 Related

- [quality-gates.md](../core/quality-gates.md) - Pre-commit checks
- [git-commit-protocol.md](../core/git-commit-protocol.md) - Commit format
- [handoff.md](handoff.md) - Session completion

---

**Remember:** Quality Gates → Docs → Session File → Commit → Confirm!
