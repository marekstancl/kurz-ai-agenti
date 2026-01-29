---
applyTo: "**/*"
---

# 🎮 PM Commands Reference

**Version:** 3.0.0  
**For:** Project Managers  
**Read Time:** 3 minuty

> **Tip:** Toto je JEDINÝ soubor, který PM potřebuje. Všechny ostatní jsou pro AI.

---

## ⚡ Quick Start (Zkopíruj do chatu)

```markdown
Ahoj, začínáme práci.

Načti:
1. .ai-agent-framework/core/meta-prompt.md
2. .ai-agent-framework/quick-reference/pm-commands.md
3. .ai-agent-framework/core/project-guide.md (pokud existuje)

Úkol: [Popiš co potřebuješ]

Think-First: Vytvoř plán, čekej na schválení.
```

**Detaily:** [new-chat.md](new-chat.md)

---

## 🎯 Základní Příkazy

### Start New Work
```markdown
Načti meta-prompt + pm-commands. 
Úkol: [X]. 
Think-First.
```

### Approve Plan
```markdown
GO
```
nebo
```markdown
Plán schválen.
```

### Revise Plan
```markdown
Uprav krok [N]: [změna]
```

### Task Done
```markdown
Úkol hotový. Commitni to.
```

### Session Done
```markdown
Session hotová. Full handoff.
```

### Stop
```markdown
STOP. Čekej.
```

---

## 🔧 Pokročilé Příkazy

### Continue Session (nový chat)
```markdown
Pokračujeme v session.
Načti meta-prompt + sessions/active/{file}.md
Pokračuj podle plánu.
```

### Epic Session (multi-session work)
```markdown
Epic {epic-id}, session {N}.
Načti meta-prompt + epics/active/{epic-id}/*
Vytvoř session {N} file a plán.
```

### Request Tests
```markdown
Otestuj [X]:
- Unit tests (>90%)
- Integration tests
- Manual UAC
```

### Check Quality Gates
```markdown
Quality gates check před commitem.
```
**Detaily:** quality-gates.md (v core/)

### Update Docs
```markdown
Aktualizuj docs pro [X].
Documentation Impact Analysis.
```

---

## 🐛 Bug Handling

### Report
```markdown
Bug: [popis]
Jak reprodukovat: [kroky]
Priorita: [high|medium|low]
Přidej do bugs.md
```

### Fix
```markdown
Oprav bug BUG-{ID} z bugs.md.
```
**Workflow:** think-first.md (Detective role)

---

## 📊 Status & Info

### Project Status
```markdown
Zobraz stav projektu.
```

### Epic Progress
```markdown
Zobraz epic {epic-id} progress.
```

### How to X
```markdown
Jak spustím projekt?
Jak spustím testy?
Kde jsou logy?
```
**Odpovědi v:** project-guide.md

---

## 🚨 Emergency

### Stop All
```markdown
STOP
```

### Rollback Commit
```markdown
Rollback poslední commit (soft).
```

### Fix Build
```markdown
Build rozbitý. Troubleshoot.
```

---

## 💡 Best Practices

### ✅ GOOD
```markdown
# Specifický
Oprav bug: TM storage neukládá customer_id. Priorita: high.

# Review before approve
[přečti plán]
GO, ale změň krok 3: použij Redis.
```

### ❌ BAD
```markdown
# Vágní
Oprav to.

# Approve without review
OK [bez čtení plánu]
```

---

## 📋 Command Cheatsheet

> **Note:** AI rozpozná příkazy automaticky - můžeš použít libovolnou variantu níže.

| Potřebuji | Příkaz (Použij libovolnou variantu) | Detail |
|-----------|-------------------------------------|--------|
| Začít práci | "Začínáme" / "Nový úkol" / "Start" | [new-chat.md](new-chat.md) |
| Schválit plán | "GO" / "Plán schválen" | think-first.md |
| Dokončit task | "Úkol hotový" / "Task done" / "Commitni" | [task-complete.md](task-complete.md) |
| Dokončit session | "Session hotová" / "Session done" / "Handoff" | [handoff.md](handoff.md) |
| Bug report | "Bug: X" / "Chyba" / "Nefunguje X" | [bug-report.md](bug-report.md) |
| Status | "Zobraz stav" / "Status" / "Progress" | workspace/session-log.md |

---

## 🔗 Související Soubory

**Pro PM:**
- [QUICK-START.md](../QUICK-START.md) - 5-minutový úvod
- [new-chat.md](new-chat.md) - Start new work
- [handoff.md](handoff.md) - End session
- [bug-report.md](bug-report.md) - Report bugs

**Pro AI (nemusíš číst):**
- [meta-prompt.md](../core/meta-prompt.md) - AI OS
- [think-first.md](../core/think-first.md) - Planning
- [quality-gates.md](../core/quality-gates.md) - Pre-commit
- [git-commit-protocol.md](../core/git-commit-protocol.md) - Git

---

## ❓ FAQ

**Q: Co když AI nereaguje?**  
A: "STOP. Načti znovu meta-prompt."

**Q: Musím znát všechny docs?**  
A: Ne. Stačí tento soubor. AI čte zbytek.

**Q: Jak zjistím session file name?**  
A: `.ai-workflow/workplace/sessions/active/`

**Q: Co je UNIFIED HANDOFF blok?**  
A: Copy-paste text pro nový chat. Najdeš ho po handoff.

**Q: Jak dlouho první session?**  
A: +20% (AI učí framework). Druhá už fast.

---

**Remember:** Buď specifický, review plány, AI je nástroj - ty řídíš!

---

**Version:** 3.0.0 | **Updated:** 2026-01-24
