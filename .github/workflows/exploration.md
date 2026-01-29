---
applyTo: "**/*"
---

# 🔬 Exploration Workflow

**Version:** 3.0.0  
**Type:** workflow  
**Last Updated:** 2026-01-05  
**Tier:** 1 (Ad-hoc, 2-4 hours)  
**Load after:** instructions/core/meta-prompt.md, instructions/core/coding-standards.md, instructions/core/session-management.md  
**Template:** templates/session-exploration.md

---

## 📂 Struktura souboru

**Obsah tohoto souboru:**
- When to Use - kdy použít tento workflow
- Exploration Process (6 Steps) - Define Research Question, Research & Analysis, Document Findings, Prototype (If Needed), Recommendations, Document & Archive
- Session Completion - checklist před označením jako dokončeno
- Related Documentation

**Related Files:**
- `instructions/core/meta-prompt.md` - AI operating system
- `instructions/core/coding-standards.md` - Coding standards
- `instructions/core/session-management.md` - Session workflow
- `templates/session-exploration.md` - Session file template

---

## When to Use

**Human says:** "Research: {description}" or "Explore: {description}"

**Automatically loaded when session type = `exploration`**

---

## Exploration Process (7 Steps)

### Step 0: Mandatory Think-First (Rule #0)

**🚨 STOP IMMEDIATELY!** 
1. Než začneš cokoli dělat, vytvoř plán v souladu s `.ai-workflow/instructions/core/think-first.md`.
2. Předlož plán PM a **počkej na schválení** (Go / Ano / OK / Schvaluji).
3. Bez schválení plánu NESMÍŠ pokračovat k dalším krokům (výzkum, analýza).

### Step 0.1: Create Session File and Branch (After Plan Approval)

**⚠️ MANDATORY: Po schválení plánu MUSÍŠ vytvořit session file a branch PŘED jakoukoliv implementací!**

1. **Vytvoř session file:**
   ```bash
   cp .ai-workflow/templates/session-exploration.md \
      .ai-workflow/workplace/sessions/active/$(date +%Y-%m-%d)-{topic}.md
   ```
   - Vyplň frontmatter:
     ```yaml
     session_id: exploration-YYYY-MM-DD-{topic}
     type: exploration
     status: active
     priority: {high|medium|low}
     started: YYYY-MM-DD HH:MM CET
     ai_agent: Cursor AI
     ```
   - Přidej schválený plán do session file
   - Označ task jako "in progress"

2. **Vytvoř git branch:**
   ```bash
   git checkout -b session/$(date +%Y-%m-%d)-{topic}
   ```
   - Branch name format: `session/YYYY-MM-DD-topic`
   - **VŽDY vytvoř branch před jakoukoliv změnou kódu!**

3. **Potvrdit PM:**
   ```
   ✅ Session file vytvořen: .ai-workflow/workplace/sessions/active/{filename}.md
   ✅ Git branch vytvořen: session/{date}-{topic}
   ✅ Začínám implementaci podle schváleného plánu.
   ```

### 1. Define Research Question

**Clarify:**
- What are we trying to learn?
- What are the constraints?
- What are the success criteria?
- What are the risks?

### 2. Research & Analysis

**Investigation:**
- Read relevant documentation
- Analyze existing code
- Research external solutions
- Prototype if needed

### 3. Document Findings

**Create research document:**
- Findings summary
- Pros and cons
- Recommendations
- Code examples (if applicable)

### 4. Prototype (If Needed)

**Build minimal prototype:**
- Proof of concept
- Test assumptions
- Measure performance
- Document results

### 5. Recommendations

**Provide guidance:**
- Recommended approach
- Alternative options
- Tradeoffs
- Next steps

### 6. Document & Archive

**Final documentation:**
- Research document
- Prototype code (if applicable)
- Recommendations
- Session file complete

---

## Session Completion

**Before marking exploration as complete:**
- [ ] Research question answered
- [ ] Findings documented
- [ ] Recommendations provided
- [ ] Prototype tested (if applicable)
- [ ] Session file complete

**See:** `.ai-workflow/instructions/core/session-management.md` for handoff protocol

---

## Related Documentation

- `.ai-workflow/instructions/core/meta-prompt.md` - AI operating system
- `.ai-workflow/instructions/core/coding-standards.md` - Coding standards and documentation rules
- `.ai-workflow/instructions/core/session-management.md` - Session workflow and handoff
- `.ai-workflow/templates/session-exploration.md` - Session file template

---

**Remember:** Research thoroughly. Document findings. Provide clear recommendations.

