---
session_id: {YYYY-MM-DD}-bug-fix-{short-description}
type: bug-fix
status: active
priority: critical|high|medium|low
started: YYYY-MM-DD HH:MM CET
completed: YYYY-MM-DD HH:MM CET (if completed)
ai_agent: Cursor AI
epic_id: {epic-id} (if epic session)
epic_session: {N} of {M} (if epic session)
epic_file: .ai-workflow/workplace/epics/{active|completed}/{epic-id}/epic-breakdown.md (if epic session)
ai_model_settings:
  temperature: 0.1-0.2
  top_p: 0.9
  frequency_penalty: 0.3-0.5
---

# 🐛 Bug Fix: {Title}

## 📂 Struktura souboru

**Obsah tohoto session file:**
- Objective - cíl opravy
- Discovery - symptom, expected behavior, current behavior
- Investigation Steps - checklist a investigation log
- Solution - root cause, proposed fix, changes made, code snippet
- Testing - test plan a test results
- Impact - before/after metrics
- Documentation Updates - seznam aktualizovaných docs
- References - related issues, PRs, documentation, sessions, commits
- AI Session Log - timeline akcí a rozhodnutí
- Completion Checklist - pre-completion a session closure
- Next Steps - pro human review a AI

**Related Files:**
- Epic breakdown: `.ai-workflow/workplace/epics/{active|completed}/{epic-id}/epic-breakdown.md` (if epic)
- Session log: `.ai-workflow/workplace/session-log.md`
- Templates: `.ai-workflow/templates/session-bug-fix.md`
- Workflow: `.ai-workflow/instructions/workflows/bug-fix.md`

---

## 🤖 AI Model Settings (Recommended)

**Pro tuto bug fix session doporučujeme:**
- **Temperature:** 0.1-0.2 (nízká pro maximální přesnost a determinismus)
- **Top-P:** 0.9 (omezuje na nejpravděpodobnější tokeny)
- **Frequency Penalty:** 0.3-0.5 (střední - zabraňuje opakování, ale zachovává konzistenci)

**Proč:**
- Bug fixy vyžadují přesnost a determinismus - chceme konzistentní, opakovatelné řešení
- Nízká temperature zajišťuje, že stejný bug bude opraven stejně
- Střední frequency penalty zabraňuje opakování frází, ale ne příliš agresivně

**Alternativa pro komplexní debugging:**
- Temperature: 0.3 (pokud potřebuješ více kreativity při hledání root cause)

**Reference:** `.ai-workflow/instructions/core/ai-model-settings.md`

---

> **💡 Multi-Session Work?** If this bug fix requires 3+ sessions or involves multiple interdependent changes, consider creating an **Epic Breakdown** first using `.ai-workflow/templates/epic-breakdown.md` before starting individual session files.

## 🎯 Objective
> One-sentence description of what needs to be fixed

## 📊 Discovery
**Reported:** {Date}  
**Discovered In:** {Environment - dev/staging/prod}  
**Affected Features:** {List components affected}  
**Severity:** 🔴 CRITICAL / 🟡 HIGH / 🟢 MEDIUM / 🔵 LOW

### Symptom
{What's visibly broken? User-facing description}

**Example:**
- Translation Memory not saving segments to Qdrant
- Second translation of same document costs same as first ($0.044)
- Expected: $0.000 (100% TM match)

### Expected Behavior
{What should happen correctly?}

**Example:**
- Segments should save to both PostgreSQL AND Qdrant after translation
- Subsequent translations of same text should retrieve from TM (zero cost)

### Current Behavior
{What actually happens?}

**Example:**
- Segments save to PostgreSQL only
- Qdrant remains empty
- Every translation hits OpenAI API at full cost

---

## 🔍 Investigation Steps

**Checklist (update as you progress):**
- [ ] Reproduced bug locally
- [ ] Analyzed logs/errors
- [ ] Identified root cause in {file.py:line}
- [ ] Verified scope (what else is affected?)
- [ ] Checked for similar issues in codebase

### Investigation Log
**{Timestamp}** - {Finding}  
**{Timestamp}** - {Finding}

**Example:**
- **10:00 CET** - Checked `translation.py:_save_to_tm()` method
- **10:15 CET** - Found Qdrant insert commented out (line 478)
- **10:30 CET** - Root cause: Previous developer disabled for debugging, forgot to re-enable

---

## 🛠️ Solution

### Root Cause
{Technical explanation of WHY bug exists}

**Example:**
```python
# In translation.py:478 - Qdrant insert was commented:
# self.qdrant_client.insert(segments)  # FIXME: Temporarily disabled
```

### Proposed Fix
{High-level strategy}

**Example:**
1. Uncomment Qdrant insert
2. Add error handling (Qdrant could be down)
3. Add test to verify dual storage
4. Add logging for monitoring

### Changes Made
| File | Lines | Description | Commit |
|------|-------|-------------|--------|
| {path/file.py} | 123-145 | {What changed} | {hash} |

**Example:**
| File | Lines | Description | Commit |
|------|-------|-------------|--------|
| backend/app/services/translation.py | 478-485 | Uncommented Qdrant insert + error handling | abc123f |
| backend/tests/test_tm_storage.py | 1-50 | Added integration test for TM persistence | def456g |

### Code Snippet
```python
# Show key changes here
```

---

## 🧪 Testing

### Test Plan
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual QA in dev environment
- [ ] Edge cases covered
- [ ] Performance validated (if relevant)

### Test Results
**Unit Tests:**
```
pytest tests/test_tm_storage.py
✅ test_tm_saves_to_postgres - PASSED
✅ test_tm_saves_to_qdrant - PASSED
✅ test_tm_retrieval_exact_match - PASSED
```

**Manual QA:**
- ✅ Translated document A ($0.044)
- ✅ Re-translated document A ($0.000) - TM match!
- ✅ Verified Qdrant has segments (count: 657)

---

## 📈 Impact

### Before Fix:
- **TM Coverage:** 0% (no TM benefit)
- **Cost per Document:** $0.044 (every time)
- **Qdrant Storage:** 0 segments

### After Fix:
- **TM Coverage:** 100% on repeat translations
- **Cost per Document:** $0.000 (TM match) / $0.044 (new)
- **Qdrant Storage:** 657+ segments

### Performance:
- Translation time: Unchanged (~30s)
- Memory usage: +5MB (acceptable)
- Database queries: +1 (Qdrant insert)

---

## 📝 Documentation Updates

**Updated:**
- [ ] `docs/docs/developers/backend/tm-service.md` - Added TM storage flow diagram
- [ ] `docs/docs/architecture/database-erd.md` - No schema changes needed
- [ ] `docs/docs/ai-ml/cost-optimization.md` - Updated with TM savings
- [ ] `CHANGELOG.md` - Added entry

**No Updates Needed:**
- API reference (no endpoint changes)
- Frontend docs (no UI changes)

**See:** `.ai-workflow/instructions/core/coding-standards.md` for documentation dependency tables

---

## 🔗 References

**Related Issues:**
- #{issue_number} - {title}

**Related PRs:**
- #{pr_number} - {title}

**Documentation:**
- [TM Service Architecture](../../docs/docs/developers/backend/tm-service.md)
- [Cost Optimization Guide](../../docs/docs/ai-ml/cost-optimization.md)

**Related Sessions:**
- [Previous session](../completed/{session-id}.md)

**Commits:**
- `{hash}` - {message}
- `{hash}` - {message}

---

## 💬 AI Session Log

**{Timestamp}** - {Action/Decision}

**Example:**
- **10:00 CET** - Started investigation, loaded architecture docs
- **10:15 CET** - Found root cause in translation.py:478
- **10:30 CET** - Implemented fix with error handling
- **11:00 CET** - Tests passing, creating PR
- **11:15 CET** - Documentation updated, session complete

---

## ✅ Completion Checklist

### Pre-Completion:
- [ ] Bug fixed and verified
- [ ] Tests written and passing
- [ ] Documentation updated
- [ ] No TODO/FIXME left in code
- [ ] Logging added for monitoring

### Session Closure:
- [ ] Commit messages follow conventions
- [ ] Session file archived to completed/
- [ ] **Handoff protocol executed** (MANDATORY)
  - See: `.ai-workflow/instructions/core/session-management.md` § Handoff Protocol
  - Includes: session-log.md, CHANGELOG.md, database-erd.md, blog post
- [ ] All documentation commits created
- [ ] Automation scripts run (git-change-checker, session-validator)

**⚠️ CRITICAL**: Before declaring handoff ready, AI MUST execute handoff protocol SEQUENTIALLY (not mentally).

---

## 🎬 Next Steps

**For Human Review:**
- Review PR #{pr_number}
- Validate fix in staging
- Approve for production deploy

**For AI (if session continues):**
- Monitor for related issues
- Consider optimization opportunities
- Update related features

---

**Status:** {active|blocked|completed}  
**Last Updated:** {YYYY-MM-DD HH:MM CET}  
**Completion:** {%}

