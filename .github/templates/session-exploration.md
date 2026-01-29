---
session_id: {YYYY-MM-DD}-exploration-{short-description}
type: exploration
status: active
priority: critical|high|medium|low
started: YYYY-MM-DD HH:MM CET
completed: YYYY-MM-DD HH:MM CET (if completed)
ai_agent: Cursor AI
epic_id: {epic-id} (if epic session)
epic_session: {N} of {M} (if epic session)
epic_file: .ai-workflow/workplace/epics/{active|completed}/{epic-id}/epic-breakdown.md (if epic session)
ai_model_settings:
  temperature: 0.5-0.7
  top_p: 0.95-1.0
  frequency_penalty: 0.1-0.3
---

# 🔬 Exploration: {Title}

## 📂 Struktura souboru

**Obsah tohoto session file:**
- Research Question - jasná otázka k zodpovězení
- Time Budget & Scope - budget, in scope, out of scope
- Success Criteria - co musí být splněno
- Research Phase - existing knowledge, external sources, key learnings
- Options Analysis - Option 0 (do nothing), Option 1-N s pros/cons
- Prototype (If Needed) - goals, implementation, results, limitations
- Recommendations - recommended approach, rationale, implementation plan, next steps
- Documentation Updates - created research docs, architecture decisions
- References - external sources, related sessions, commits
- AI Session Log - timeline akcí a rozhodnutí
- Completion Checklist - pre-completion a session closure
- Next Steps - pro human review a AI

**Related Files:**
- Epic breakdown: `.ai-workflow/workplace/epics/{active|completed}/{epic-id}/epic-breakdown.md` (if epic)
- Session log: `.ai-workflow/workplace/session-log.md`
- Templates: `.ai-workflow/templates/session-exploration.md`
- Workflow: `.ai-workflow/instructions/workflows/exploration.md`

---

## 🤖 AI Model Settings (Recommended)

**Pro tuto exploration session doporučujeme:**
- **Temperature:** 0.5-0.7 (vyšší pro kreativitu při generování možností)
- **Top-P:** 0.95-1.0 (široký výběr tokenů)
- **Frequency Penalty:** 0.1-0.3 (nízká - exploration může zahrnovat opakování konceptů)

**Proč:**
- Exploration potřebuje kreativitu při generování možností a návrhů řešení
- Vyšší temperature umožňuje prozkoumat různé přístupy, ale ne příliš vysoká (aby zůstala faktická)
- Široký Top-P umožňuje prozkoumat různé možnosti
- Nízká frequency penalty umožňuje důkladné prozkoumání konceptů

**Fázové nastavení:**
- **Research fáze:** Temperature 0.7, Top-P 1.0 (maximální kreativita při hledání řešení)
- **Analysis fáze:** Temperature 0.5, Top-P 0.95 (vyvážené pro analýzu)
- **Recommendation fáze:** Temperature 0.4, Top-P 0.9 (konzervativnější pro finální doporučení)

**Reference:** `.ai-workflow/instructions/core/ai-model-settings.md`

---

> **💡 Multi-Session Work?** If exploration findings suggest this will require 3+ sessions for implementation, consider creating an **Epic Breakdown** using `.ai-workflow/templates/epic-breakdown.md` to plan the multi-session implementation strategy.

## 🎯 Research Question
> Clear, answerable question this exploration aims to resolve

**Example:**
- "What's the best vector database for our TM search? Qdrant vs Pinecone vs Weaviate?"
- "Is it feasible to add real-time collaboration using CRDTs?"
- "How should we structure the frontend state management?"

## ⏱️ Time Budget & Scope

**Budget:**
| Phase | Planned | Actual |
|-------|---------|--------|
| Research | 1h | - |
| Options Analysis | 30m | - |
| Prototype (if needed) | 1.5h | - |
| Documentation | 30m | - |
| **Total** | 3.5h | - |

**In Scope:**
- [ ] {Specific thing to investigate}
- [ ] {Specific thing to investigate}

**Out of Scope:**
- {What we're NOT investigating}
- {What we're deferring}

## ✅ Success Criteria
- [ ] Understand tradeoffs between at least 2-3 options
- [ ] Have clear recommendation with reasoning
- [ ] Document findings for future reference
- [ ] Know estimated effort for implementation (if proceeding)

---

## 📚 Research Phase

### Existing Knowledge
{What do we already know? Check previous sessions, docs, code}

```bash
# Commands run to gather context:
grep -r "{keyword}" docs/
ls .ai-workflow/sessions/completed/ | grep -i "{topic}"
```

### External Sources
| Source | Key Insight | Relevance |
|--------|-------------|-----------|
| [Link](url) | {Main takeaway} | High/Medium/Low |
| [Link](url) | {Main takeaway} | High/Medium/Low |

### Key Learnings from Research
1. {Learning 1}
2. {Learning 2}
3. {Learning 3}

---

## ⚖️ Options Analysis

### Option 0: Do Nothing (Baseline)
**What:** Keep current approach unchanged
**Pros:**
- No effort required
- No risk of regression

**Cons:**
- {Cons}

### Option 1: {Option Name}
**What:** {Description}

**Pros:**
- {Pro 1}
- {Pro 2}

**Cons:**
- {Con 1}
- {Con 2}

**Effort:** {X hours/days}
**Risk:** {Low/Medium/High}

### Option 2: {Option Name}
{Repeat structure from Option 1}

---

## 🧪 Prototype (If Needed)

### Prototype Goals
- {Goal 1}
- {Goal 2}

### Prototype Implementation
```python
# Show prototype code here
```

### Prototype Results
**Findings:**
- {Finding 1}
- {Finding 2}

**Performance:**
- {Metrics}

**Limitations:**
- {Limitation 1}
- {Limitation 2}

---

## 💡 Recommendations

### Recommended Approach
**Option:** {Option Name}

**Rationale:**
- {Reason 1}
- {Reason 2}
- {Reason 3}

### Implementation Plan (If Proceeding)
1. {Step 1}
2. {Step 2}
3. {Step 3}

**Estimated Effort:** {X hours/days}
**Estimated Sessions:** {N sessions}

### Next Steps
- [ ] {Next step 1}
- [ ] {Next step 2}

---

## 📝 Documentation Updates

**Created:**
- [ ] Research document: `docs/docs/development/{research-doc}.md`
- [ ] Architecture decision: `docs/docs/architecture/design-decisions.md` (if applicable)

**See:** `.ai-workflow/instructions/core/coding-standards.md` for documentation dependency tables

---

## 🔗 References

**External Sources:**
- [Source 1](url)
- [Source 2](url)

**Related Sessions:**
- [Previous session](../completed/{session-id}.md)

**Commits:**
- `{hash}` - {message} (if prototype created)

---

## 💬 AI Session Log

**{Timestamp}** - {Action/Decision}

**Example:**
- **10:00 CET** - Started research, reviewed existing docs
- **10:30 CET** - Analyzed 3 options
- **11:00 CET** - Created prototype
- **11:30 CET** - Documented findings and recommendations

---

## ✅ Completion Checklist

### Pre-Completion:
- [ ] Research question answered
- [ ] Options analyzed
- [ ] Recommendations provided
- [ ] Findings documented
- [ ] Prototype tested (if applicable)

### Session Closure:
- [ ] Commit messages follow conventions
- [ ] Session file archived to completed/
- [ ] **Handoff protocol executed** (MANDATORY)
  - See: `.ai-workflow/instructions/core/session-management.md` § Handoff Protocol
- [ ] All documentation commits created
- [ ] Automation scripts run (git-change-checker, session-validator)

---

## 🎬 Next Steps

**For Human Review:**
- Review recommendations
- Decide on implementation approach
- Create epic breakdown (if proceeding)

**For AI (if session continues):**
- Implement recommended approach
- Create epic breakdown for implementation

---

**Status:** {active|blocked|completed}  
**Last Updated:** {YYYY-MM-DD HH:MM CET}  
**Completion:** {%}

