---
applyTo: "**/*"
---

# 🆕 New Chat Quick Reference

**Version:** 3.0.0  
**Last Updated:** 2026-01-24

---

## 📋 Pro PM: Copy-Paste Bloky

### Standard Session (Nová práce)

```markdown
Ahoj, začínáme novou session.

Načti:
1. .ai-agent-framework/core/meta-prompt.md
2. .ai-agent-framework/core/project-guide.md
3. .ai-agent-framework/core/think-first.md

Úkol: [Popis úkolu]

Aplikuj Think-First protocol a čekej na schválení.
Komunikuj v češtině.
```

---

### Continuation Session (Pokračování)

```markdown
Ahoj, pokračujeme v session.

Načti:
1. .ai-agent-framework/core/meta-prompt.md
2. .ai-agent-framework/core/project-guide.md
3. .ai-agent-framework/sessions/{session-file}.md

Stav: [Kde jste skončili]
Další: [Co následuje]

Komunikuj v češtině.
```

---

## 🤖 Pro AI: Postup

### 1. Load & Verify
```markdown
□ meta-prompt.md loaded
□ project-guide.md loaded
□ Session context loaded
□ think-first.md understood
```

### 2. Identify Session Type & Naming
- **Bug Fix:** `{YYYY-MM-DD}-bug-fix-{issue-name}.md`  
  Example: `2026-01-28-bug-fix-login-validation.md`
- **New Feature:** `{YYYY-MM-DD}-new-feature-{feature-name}.md`  
  Example: `2026-01-28-new-feature-user-profile.md`
- **Refactoring:** `{YYYY-MM-DD}-refactoring-{component}.md`  
  Example: `2026-01-28-refactoring-database-layer.md`
- **Exploration:** `{YYYY-MM-DD}-exploration-{topic}.md`  
  Example: `2026-01-28-exploration-api-structure.md`
- **Hotfix:** `{YYYY-MM-DD}-hotfix-{issue}.md`  
  Example: `2026-01-28-hotfix-payment-processing.md`
- **Continuation:** Load existing file
- **Epic:** Load epic files

### 3. Identify Role
```
Bug fix → Detective
New feature → Architect
Refactoring → Safety Officer
```

### 4. Session File Naming
**Format:** `{YYYY-MM-DD}-{type}-{descriptive-name}.md`

```markdown
Bug Fix:      2026-01-28-bug-fix-login-validation.md
Feature:      2026-01-28-new-feature-user-profile.md
Refactoring:  2026-01-28-refactoring-database-layer.md
Exploration:  2026-01-28-exploration-api-structure.md
Hotfix:       2026-01-28-hotfix-payment-processing.md
```

### 5. Think-First Plan
```markdown
1. Analyze task
2. Propose plan
3. List files
4. Identify risks
5. Ask: "Můžu pokračovat?"
```

**WAIT for PM approval!**

### 5. After Approval
```bash
# Create session file
# Create git branch
# Confirm to PM
# Begin work
```

---

## ✅ Checklist
```markdown
□ Context loaded
□ Session type identified
□ Role identified
□ Plan created
□ PM approved
□ Session file created
□ Branch created
□ Ready to work
```

---

**See:** [session-management.md](../core/session-management.md) for details

**Remember:** New Chat = Fresh Start. Load context, Think First, Get Approval!
