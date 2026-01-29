# 📊 Session Log

**Purpose:** Krátký, chronologický log všech AI sessions. Nejnovější záznamy jsou NAHOŘE.

**Last Updated:** 2026-01-29 17:40 CET

---

## 📋 Log Format

**Každý záznam obsahuje:**
- **Date & Time:** `YYYY-MM-DD HH:MM CET` (MANDATORY format)
- **Session ID:** `{session-id}`
- **Type:** `{bug-fix|new-feature|refactoring|exploration}`
- **Status:** `{completed|active|blocked}`
- **Duration:** `{X}h {Y}m` (pokud dokončeno)
- **Summary:** Krátký popis (1-2 věty)

---

## 📊 Sessions

**⚠️ DŮLEŽITÉ: Nejnovější záznamy jsou NAHOŘE (reverse chronological order)**

### Template pro nový záznam:
```markdown
### YYYY-MM-DD HH:MM CET - {session-id}

**Type:** {bug-fix|new-feature|refactoring|exploration}  
**Status:** {completed|active|blocked}  
**Duration:** ~Xh  
**Commits:** {hash1}, {hash2}

**Summary:**
- [Hlavní úkol 1]
- [Hlavní úkol 2]
```

---

## 📈 Statistics

**Total Sessions:** 0  
**Completed:** 0  
**Active:** 0  
**Blocked:** 0

---

## 📝 Update Instructions

**AI agents MUST update this log:**
1. **After every session completion** - přidej záznam NA ZAČÁTEK sekce Sessions
2. **Format:** Použij template výše, zachovej reverse chronological order
3. **Keep it SHORT** - každý záznam max 3-4 řádky
4. **Update statistics** po každém dokončení session

**Location:** `workspace/session-log.md`
