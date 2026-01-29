---
applyTo: "**/*"
---

# 🐛 Bug Report Quick Reference

**Version:** 3.0.0  
**Last Updated:** 2026-01-24

---

## 🎯 Purpose

**What:** Report and track bugs discovered during development

**When:** You discover bug/issue that needs fixing

**Key:** Document → Track → Fix (not Fix → Forget → Rediscover)

---

## 🧭 Decision Tree

```
Bug discovered
├─ Critical (blocking)? → Report AND fix now
└─ Non-critical? → Report ONLY, fix later
```

---

## 📋 For PM: Report Bug

```markdown
Bug: {popis}
- Co se děje: {detail}
- Jak reprodukovat: {kroky}
- Priorita: {critical|high|medium|low}

Přidej do bugs.md.
```

---

## 🤖 For AI: Bug Report Process

### Step 1: Generate Bug ID
```bash
BUG_ID="BUG-$(date '+%Y%m%d-%H%M')"
# Example: BUG-20260123-1430
```

### Step 2: Determine Component
```
backend | frontend | database | api | ui | parser | storage | other
```

### Step 3: Add to bugs.md

**Location:** `.ai-agent-framework/bugs.md`

**Template:**
```markdown
## 🐛 {BUG_ID} - {Krátký popis}

**Status:** 🟡 Reported  
**Priority:** {critical|high|medium|low}  
**Reported:** {YYYY-MM-DD HH:MM CET}  
**Component:** {component}

### 📝 Popis
{Detailní popis}

### 🔄 Jak Reprodukovat
1. {Krok 1}
2. {Krok 2}

### ✅ Očekávané Chování
{Co by se mělo dít}

### ❌ Aktuální Chování
{Co se děje}

### 🔗 Související Soubory
- `{file}` - {proč relevant}

### 📋 FIX INSTRUCTIONS (COPY-PASTE)
```markdown
Oprav bug {BUG_ID}.

Načti:
1. .ai-agent-framework/core/meta-prompt.md
2. .ai-agent-framework/core/project-guide.md
3. .ai-agent-framework/bugs.md#{BUG_ID}

Workflow:
1. Think-First plán
2. Regression test (must FAIL)
3. Fix
4. Test must PASS
5. Update bugs.md status: Fixed
6. Commit s referencí {BUG_ID}
```

---
```

**Commit:**
```bash
git add bugs.md
git commit -m "docs(bugs): add {BUG_ID} ($(date '+%Y-%m-%d %H:%M CET'))"
```

---

## 📊 Priority Levels

| Priority | Description | Fix Time | Examples |
|----------|-------------|----------|----------|
| 🔴 Critical | Production down, data loss | Immediately | Server crash, data corruption |
| 🟠 High | Major feature broken | This/next session | Login broken, API 500 |
| 🟡 Medium | Minor feature, workaround exists | 1-2 sessions | UI glitch, slow query |
| 🟢 Low | Cosmetic, edge case | When time permits | Typo, color issue |

---

## 🔧 Bug Fix Workflow

### Fix Immediately (Same Session)
```markdown
1. Report to bugs.md ✅
2. Think-First plan
3. Regression test (FAIL)
4. Implement fix
5. Test PASS
6. Update bugs.md: ✅ Fixed
7. Commit with bug reference
```

### Fix Later (Future Session)
```markdown
1. Report to bugs.md ✅
2. COPY-PASTE blok ready ✅
3. Continue current work
4. Later: Use COPY-PASTE blok
```

---

## ✅ Bug Fix Completion

**Update bugs.md entry:**
```markdown
**Status:** ✅ Fixed  
**Fixed:** {YYYY-MM-DD HH:MM CET}  
**Commit:** {hash} - {message}

### ✅ Solution
{How it was fixed}

### ✅ Verification
- [x] Regression test passes
- [x] Existing tests pass
- [x] Manual verification done
```

**Commit update:**
```bash
git add bugs.md
git commit -m "docs(bugs): mark {BUG_ID} as fixed ($(date '+%Y-%m-%d %H:%M CET'))"
```

---

## 🔄 Bug Status Lifecycle

```
🟡 Reported → 🔄 In Progress → ✅ Fixed
              └─ ❌ Won't Fix
              └─ 🔍 Investigating
```

---

## ✅ Checklist

```markdown
### Report
- [ ] Bug ID generated
- [ ] Priority assigned
- [ ] Component identified
- [ ] Reproduction steps clear
- [ ] COPY-PASTE blok created
- [ ] Added to bugs.md
- [ ] Committed

### Fix (when fixing)
- [ ] Think-First plan
- [ ] Regression test written (FAIL)
- [ ] Fix implemented
- [ ] Test now PASS
- [ ] bugs.md updated: Fixed
- [ ] Commit references BUG_ID
```

---

## 🚨 Common Mistakes

**❌ NEVER:**
- Fix without reporting first
- Report without reproduction steps
- Forget COPY-PASTE blok
- Fix without regression test
- Forget to update bugs.md

**✅ ALWAYS:**
- Report to bugs.md FIRST
- Include reproduction steps
- Generate COPY-PASTE blok
- Write regression test
- Update status after fix
- Reference bug ID in commit

---

## 📚 Related

- [think-first.md](../core/think-first.md) - Bug fix planning
- [testing-protocol.md](../core/testing-protocol.md) - Regression tests
- [git-commit-protocol.md](../core/git-commit-protocol.md) - Commit format

---

**Remember:** Report → Track → Fix. Every bug documented!
