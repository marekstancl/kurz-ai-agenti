# 🎯 EPIC BREAKDOWN: [Epic Name]

## 📂 Struktura souboru

**Obsah tohoto epic breakdown file:**
- Executive Summary - cíl, scope, out of scope
- Session Overview - tabulka všech sessions s dependencies
- Session 1-N - detailní breakdown každé session (objectives, deliverables, documentation checklist, UAC testing, acceptance criteria, technical notes, end-of-session checklist)
- Architecture Decisions - context, decision, consequences
- Testing Strategy - unit tests, integration tests, manual UAC tests, performance requirements
- Documentation Deliverables - API docs, architecture docs, developer docs, user docs, Docusaurus sidebars, blog post
- Deployment Plan - pre-deployment checklist, deployment steps, rollback plan
- Success Metrics - functional, quality, performance metrics
- Related Resources - epic planning, dependencies
- Session Log - timeline všech sessions

**Related Files:**
- Session templates: `.ai-workflow/templates/session-*.md`
- Session management: `.ai-workflow/instructions/core/session-management.md`
- Meta-prompt: `.ai-workflow/instructions/core/meta-prompt.md`

---

**CRITICAL!! Related Documentation: Always read all linked documents below and related documents linked in these documents !**
- **Meta-Prompt:** `.ai-workflow/instructions/core/meta-prompt.md` - AI operating system
- **Session Management:** `.ai-workflow/instructions/core/session-management.md` - Session workflow
- **Coding Standards:** `.ai-workflow/instructions/core/coding-standards.md` - Coding standards
- **Docusaurus Guide:** `.github/ai-prompts/guides/DOCUSAURUS-GUIDE.md` - Documentation system (MANDATORY reading)
- **Workflow Docs:** `docs/docs/workflows/` - Session management, prompts database, CI/CD
- **Architecture Docs:** `docs/docs/architecture/` - System design, ERD, ADRs

---

**Epic ID:** {epic-id} (e.g., epic-2026-01-05-documentation)  
**Created:** YYYY-MM-DD HH:MM CET  
**Epic Type:** [Feature Implementation | Bug Fix | Refactoring | Documentation]  
**Priority:** [HIGH | MEDIUM | LOW]  
**Estimated Duration:** X sessions (~Y-Z hours)  
**Complexity:** [Low | Medium | High]

---

## 📋 Executive Summary

**Cíl:** [Jednořádkový popis hlavního cíle epic]

**Scope:**
- [Co je součástí této epic]
- [Hlavní deliverables]
- [Klíčové funkcionality]

**Out of Scope:**
- [Co není součástí této epic]
- [Future features]
- [Deferred items]

---

## 📊 Session Overview

| # | Session Name | Duration | Dependencies | Status |
|---|-------------|----------|--------------|--------|
| 1 | [Session 1 Name] | Xh | None | Not Started |
| 2 | [Session 2 Name] | Xh | Session 1 | Not Started |
| 3 | [Session 3 Name] | Xh | Session 1, 2 | Not Started |

**Total Estimated Time:** X-Y hours  
**Completed:** 0 hours  
**Remaining:** X-Y hours

---

## 🔄 Session 1: [Session Name]

**Type:** [feature | bugfix | refactor | docs]  
**Priority:** [CRITICAL | HIGH | MEDIUM | LOW]  
**Estimated Duration:** X-Y hours  
**Dependencies:** [None | Session N]  
**Session File:** `.ai-workflow/sessions/active/{epic-id}-session1-{short-description}.md`

### 🎯 Objectives

1. **[Objective 1 Name]**
   - [Specific task]
   - [Specific task]
   - [Specific task]

2. **[Objective 2 Name]**
   - [Specific task]
   - [Specific task]

### 📦 Deliverables

- [ ] [Deliverable 1]
- [ ] [Deliverable 2]
- [ ] [Deliverable 3]
- [ ] Unit tests for [feature]
- [ ] **Documentation updated** (see checklist below)

### 📚 Documentation Checklist (MANDATORY)

**BEFORE committing code, verify:**
- [ ] **API docs updated** (if new/changed endpoints): `/docs/docs/api-reference/`
- [ ] **Architecture docs updated** (if architectural changes): `/docs/docs/architecture/`
- [ ] **Database ERD updated** (if DB schema changes): `/docs/docs/architecture/database-erd.md`
- [ ] **Developer guides updated** (if new patterns/components): `/docs/docs/developers/`
- [ ] **Docusaurus sidebar updated** (if new doc pages): `/docs/sidebars.ts`
- [ ] **Docusaurus builds without errors**: `cd docs && npm start` (verify no MDX errors)

**MDX Syntax Prevention:**
- [ ] No `<number` patterns (e.g., `<100ms` → use "pod 100ms" or "less than 100ms")
- [ ] No unescaped `{{` or `}}` in text (use `\{\{` or wrap in code blocks)
- [ ] No markdown links to `.github/` files (use plain text paths instead)
- [ ] No paths starting with numbers (e.g., `00-overview`, `06-workflows`)

**See:** `.ai-workflow/instructions/core/coding-standards.md` for documentation dependency tables

### 🧪 UAC Testing (if user-facing changes)

- [ ] **Manual UAC test performed** (describe test scenario)
- [ ] **Frontend integration verified** (if API changes)
- [ ] **Test results documented** in session file
- [ ] **Edge cases tested** (error handling, validation)

### 🔍 Acceptance Criteria

- [Measurable success criterion 1]
- [Measurable success criterion 2]
- [Measurable success criterion 3]
- All unit tests passing
- Documentation updated and Docusaurus builds successfully
- UAC tests performed (if applicable)

### 📝 Technical Notes

**Files to modify:**
- `path/to/file1.py`
- `path/to/file2.ts`

**New files to create:**
- `path/to/new_file.py`

**Dependencies:**
- [External library/service if needed]

**API Changes:**
- [If any API endpoints are added/modified]

### ✅ End-of-Session Checklist

**Before completing session, verify:**
- [ ] All code committed with proper Conventional Commits format
- [ ] Tests written and passing (>80% coverage for new code)
- [ ] Documentation updated (API, architecture, developer guides)
- [ ] Session file updated with commits, duration, notes
- [ ] No broken links in Docusaurus (run `npm start` to verify)
- [ ] Changes pushed to repository (if required)
- [ ] CHANGELOG.md updated (for feat:/fix: commits)
- [ ] `.ai-workflow/sessions/session-log.md` entry added
- [ ] Automation scripts run (git-change-checker, session-validator)
- [ ] Session archived to `.ai-workflow/epics/{epic-id}/sessions/completed/`

**See:** `.ai-workflow/instructions/core/session-management.md` for detailed handoff protocol

---

## 🔄 Session 2: [Session Name]

[Repeat structure from Session 1]

---

## 📐 Architecture Decisions

### Decision 1: [Decision Title]
**Context:** [Why this decision is needed]  
**Decision:** [What was decided]  
**Consequences:** [Impact of this decision]  
**Location:** `docs/docs/architecture/design-decisions.md`

### Decision 2: [Decision Title]
**Context:** [Why this decision is needed]  
**Decision:** [What was decided]  
**Consequences:** [Impact of this decision]  
**Location:** `docs/docs/architecture/design-decisions.md`

---

## 🧪 Testing Strategy

### Unit Tests
- [Component 1]: X% coverage target
- [Component 2]: X% coverage target
- [Critical paths]: 95% coverage minimum

### Integration Tests
- [Integration point 1]
- [Integration point 2]

### Manual UAC Tests
- [ ] [User acceptance test 1]
- [ ] [User acceptance test 2]
- [ ] [User acceptance test 3]

### Performance Requirements
- [Metric 1]: target value
- [Metric 2]: target value

---

## 📚 Documentation Deliverables

### API Documentation
- [ ] OpenAPI spec updated (if applicable)
- [ ] API reference in `/docs/docs/api-reference/`
- [ ] Code examples

### Architecture Documentation
- [ ] Update `/docs/docs/architecture/system-overview.md` (if architectural changes)
- [ ] Update `/docs/docs/architecture/database-erd.md` (if DB schema changes)
- [ ] Add to `/docs/docs/architecture/design-decisions.md` (if ADRs)

### Developer Documentation
- [ ] Update `/docs/docs/developers/backend/` (if backend changes)
- [ ] Update `/docs/docs/developers/frontend/` (if frontend changes)
- [ ] Migration guides (if breaking changes)

### User Documentation
- [ ] Update UI guide (if user-facing changes)
- [ ] FAQ updates

### 📑 Docusaurus Sidebars Configuration

**When adding NEW documentation pages, update `/docs/sidebars.ts`:**

```typescript
// Example: Adding new page to sidebars
{
  type: 'category',
  label: 'Your Category',
  items: [
    'path/to/your-new-page', // Without .md extension
  ],
}
```

**CRITICAL Docusaurus Rules:**
- ⚠️ Always test build after doc changes: `cd docs && npm start`
- ⚠️ No `<number` patterns (MDX interprets as HTML tag)
- ⚠️ No markdown links to `.github/` files (external to docs tree)
- ⚠️ No numeric-prefix paths (`00-`, `06-`) in links
- ⚠️ Escape `{{` and `}}` in text: use `\{\{` or wrap in code blocks

**Verify in browser:**
- [ ] New page appears in sidebar at http://10.0.77.10:3000/
- [ ] Navigation works correctly
- [ ] No console errors

### Blog Post
- [ ] **If last session of epic:** Evaluate if blog post needed
- [ ] **If not last session:** Defer blog post evaluation to epic completion

---

## 🚀 Deployment Plan

### Pre-deployment Checklist
- [ ] All tests passing (unit + integration)
- [ ] Database migrations tested
- [ ] Documentation complete
- [ ] UAC tests performed
- [ ] Performance benchmarks met

### Deployment Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Rollback Plan
- [How to rollback if deployment fails]

---

## 📊 Success Metrics

### Functional Metrics
- ✅ [Metric 1 with target value]
- ✅ [Metric 2 with target value]

### Quality Metrics
- ✅ Test coverage: >80%
- ✅ Zero critical bugs in first week
- ✅ Méně než 5 minor bugs reported in first month
- ✅ Documentation completeness: 100%

### Performance Metrics
- ✅ [Performance metric 1]: target value
- ✅ [Performance metric 2]: target value

---

## 🔗 Related Resources

**Epic Planning:**
- Session management: `.ai-workflow/instructions/core/session-management.md`
- Session templates: `.ai-workflow/templates/`

**Dependencies:**
- [Related Epic 1] (if applicable)
- [External system/API] (if applicable)

---

## 📝 Session Log

### Session 1 - [Date] - [Status]
**Duration:** Xh Ymin  
**Commits:** [commit hash] - [commit message]  
**Notes:** [Key achievements, blockers, decisions]  
**Session File:** `.ai-workflow/epics/{epic-id}/sessions/completed/{epic-id}-session1.md`

### Session 2 - [Date] - [Status]
**Duration:** Xh Ymin  
**Commits:** [commit hash] - [commit message]  
**Notes:** [Key achievements, blockers, decisions]  
**Session File:** `.ai-workflow/epics/{epic-id}/sessions/completed/{epic-id}-session2.md`

---

**Last Updated:** [Date]  
**Next Session:** Session [N] - [Session Name]  
**Estimated Completion:** YYYY-MM-DD (assuming X-Yh sessions over Z days)

---

*This breakdown follows `.ai-workflow/instructions/core/session-management.md` Epic workflow.*

