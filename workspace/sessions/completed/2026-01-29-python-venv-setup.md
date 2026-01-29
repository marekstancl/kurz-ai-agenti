# Session: Python Virtual Environment Setup
**Date:** 2026-01-29  
**Type:** Project Setup  
**Status:** ✅ Completed

## Goal
Nastavit Python virtuální prostředí (venv) pro izolované dependency management během kurzu AI Agenti.

## Context
- Kurz vyžaduje práci s mnoha AI/ML knihovnami (LangChain, Autogen, ChromaDB, SQLAlchemy, n8n, OpenAI API, atd.)
- Nutnost izolace dependencies od systémového Pythonu
- Best practice pro Python projekty

## Think-First Plan

### ✅ Phase 1: Environment Setup
- [x] Zjistit verzi systémového Pythonu → Python 3.13.9
- [x] Vytvořit venv v projektu
- [x] Ověřit .gitignore (již obsahuje venv excludes)
- [x] Vytvořit requirements.txt skeleton

### ✅ Phase 2: Documentation
- [x] Aktualizovat README s aktivačními instrukcemi
- [x] Testovat venv aktivaci
- [x] Dokumentovat setup proces
- [x] Update session tracking

## Implementation Notes

### Virtual Environment
- **Location:** `venv/` v project root
- **Python version:** 3.13.9
- **Pip version:** 24.2
- **Already in .gitignore:** ✅ (venv/, .venv/, ENV/, env/)

### Requirements.txt Strategy
Vytvořen skeleton se všemi dependencies z kurzu:
- Core AI/LLM (OpenAI, Anthropic, LangChain)
- Agent Frameworks (Autogen, Semantic Kernel, LangGraph)
- Databases (ChromaDB, SQLAlchemy, MongoDB)
- RL (Gymnasium, PettingZoo, Stable-Baselines3)
- Utilities & Development tools

Dependencies jsou commented out - odkomentujeme podle potřeby během kurzu.

### README Enhancements
- Přidány aktivační instrukce (Linux/macOS/Windows)
- Informace o kurzu
- Tech stack přehled
- Reference na Global-Classes-CZE

## Quality Gates
✅ Venv vytvořen a funkční  
✅ Python v venv: `/opt/_home/_kurz-ai-agenti/venv/bin/python`  
✅ Pip funkční v venv  
✅ .gitignore správně nakonfigurován  
✅ README aktualizován  
✅ requirements.txt připraven  

## Results
✅ Python venv aktivní a testován  
✅ Izolované prostředí pro kurz dependencies  
✅ README s clear instrukcemi  
✅ requirements.txt připraven pro postupnou instalaci knihoven  

## Activation Commands

```bash
# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

# Deactivate
deactivate
```

## Commits
7f98fd7: feat: add Python virtual environment setup
