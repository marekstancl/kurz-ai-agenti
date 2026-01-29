# Session: Reference Materials Setup
**Date:** 2026-01-29  
**Type:** Project Setup  
**Status:** ✅ Completed

## Goal
Naklonovat reference materiály z Global-Classes-CZE pro použití během kurzu AI Agenti.

## Context
- Reference repo: https://github.com/Global-Classes-CZE
- Relevantní pro kurz: `ai-chatbots`
- Potřeba jasné struktury: reference vs. vlastní kód

## Think-First Plan

### ✅ Phase 1: Structure Setup
- [x] Vytvořit `examples/` složku pro reference
- [x] Přidat `examples/` do .gitignore
- [x] Vytvořit `lectures/` složku pro kód z lekcí
- [x] Vytvořit `projects/` složku pro vlastní projekty

### ✅ Phase 2: Clone Reference
- [x] Naklonovat ai-chatbots do examples/
- [x] Dokumentovat strukturu v README
- [x] Update session tracking

## Implementation Notes

### Strategy: Direct Clone + Gitignore
- **Method:** Direct clone (ne submodule, ne fork)
- **Důvod:** Jednoduché, flexibilní, jasná separace reference vs. vlastní kód
- **Neverzováno:** examples/ je v .gitignore

### Cloned Repository
- **Source:** https://github.com/Global-Classes-CZE/ai-chatbots
- **Location:** `examples/ai-chatbots/`
- **Size:** 3.00 MiB, 414 objects
- **Content:** 
  - Lekce 1-10 (příklady kódu)
  - README dokumentace pro různé agenty:
    - Building agents
    - Financial agent
    - Interest agent
    - Interview system

### Directory Structure Created
```
kurz-ai-agenti/
├── examples/           # Reference (neverzováno)
│   └── ai-chatbots/    # Naklonováno
├── lectures/           # Vaše kód z lekcí
├── projects/           # Vaše projekty
└── workspace/          # Session tracking
```

## Quality Gates
✅ Složky vytvořeny  
✅ examples/ přidáno do .gitignore  
✅ ai-chatbots úspěšně naklonováno  
✅ README aktualizován s strukturou  
✅ .gitkeep soubory pro practices  

## Results
✅ Reference materiály dostupné lokálně  
✅ Jasná separace: examples vs. lectures vs. projects  
✅ Neverzujeme cizí kód (jen odkaz v README)  
✅ Update možný: `cd examples/ai-chatbots && git pull`  

## Update Reference (v budoucnu)
```bash
cd examples/ai-chatbots
git pull origin main
```

## Commits
d90d611: feat: add project structure and reference materials
