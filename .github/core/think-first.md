---
applyTo: "**/*"
---

# 🧠 Think-First Approach

**Version:** 3.0.0  
**Last Updated:** 2026-01-24

---

## 🎯 Overview

**Problem:** AI implementuje bez konzultace → špatné přístupy

**Solution:** **VŽDY PLÁN PRVNÍ** - navrhni plán, čekej na schválení

**Proč:**
- Prevents bad implementations
- Fixes approach before work starts
- Saves time
- Ensures alignment

---

## 🚨 MANDATORY Process

### 1. STOP
Když dostaneš task → **IHNED ZASTAV**, neim implementuj!

### 2. ANALYZE
```
- Co user chce?
- Jaký context?
- Jaké constraints?
- Které soubory?
```

### 3. PROPOSE
Navrhni plán (formát viz níže)

### 4. ASK
"Můžu pokračovat s tímto plánem?"

### 5. WAIT
**ČEKEJ** na odpověď. **NIKDY** nepokračuj bez schválení!

### 6. EXECUTE (Po schválení)

**A. Create session file:**
```bash
mkdir -p .ai-workflow/workplace/sessions/active
# Vytvoř session file podle templates/
# Fill: session_id, type, status, priority, started date
```

**B. Create git branch:**
```bash
git checkout -b session/$(date +%Y-%m-%d)-{topic}
```

**C. Confirm to user:**
```
✅ Session file created
✅ Branch created
✅ Starting implementation
```

**D. Implement** podle plánu

**E. Update session file** s results

---

## 📋 Plan Format

```markdown
## Navrhovaný Plán

Úkol: {co PM chce}
Role: {Detective/Architect/...}
Mindset: {priorita}

Analýza: {co jsem pochopil}
Přístup: {konkrétní kroky}
Soubory: {seznam + co udělám}
Docs: {preliminary assessment}
Rizika: {co může selhat}

Alternativy (pokud relevantní):
- A: {popis} - Pro/Con
- B: {popis} - Pro/Con

Můžu pokračovat?
```

---

## ⚠️ Exceptions (Kdy můžeš přeskočit)

**Skip planning POUZE když:**

1. PM explicitně říká: "Just do it" / "Go ahead" / "Proceed"
2. Triviální task: "Fix typo" / "Add comment"
3. Už schválený plán: pokračuješ v approved session
4. Continuous work: další krok z approved plánu

**Když nejistý → VŽDY navrhni plán!**

---

## 🚫 Common Mistakes

**❌ WRONG:**
```
User: "Fix bug"
AI: *Immediately starts changing files*
```

**✅ RIGHT:**
```
User: "Fix bug"
AI: "## Navrhovaný Plán
...
Můžu pokračovat?"
```

---

## 📚 Examples

Viz [examples/think-first-examples.md](../examples/think-first-examples.md)

---

## 🔗 Related

- meta-prompt.md - Rule #0.1
- session-management.md - Session lifecycle
- git-commit-protocol.md - Branch workflow

---

**Key:** Plan → Wait → Implement → Document. Never skip.
