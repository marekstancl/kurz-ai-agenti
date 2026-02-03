# AI Agent - Překladatel EN ↔ CZ

Jednoduchý AI agent s OpenAI API, který překládá texty mezi angličtinou a češtinou pomocí function calling (tools).

## Co agent dělá

Agent automaticky rozhoduje, který nástroj použít na základě požadavku uživatele:

1. **translate_en_to_cz** - Překlad z angličtiny do češtiny
2. **translate_cz_to_en** - Překlad z češtiny do angličtiny

## Jak to funguje

1. Uživatel zadá požadavek na překlad
2. OpenAI model (GPT-4o) analyzuje požadavek
3. Model automaticky rozhodne, který nástroj použít
4. Agent zavolá příslušný nástroj
5. LLM vrátí přeložený text
6. Agent vrátí konečnou odpověď

## Instalace

### 1. Předpoklady
- Python 3.12+
- `uv` - Ultra-fast Python package installer ([instalace](https://docs.astral.sh/uv/getting-started/installation/))

### 2. Setup prostředí

```bash
# Naklonuj nebo stáhni projekt
cd /path/to/project

# Vytvoř .env soubor s OpenAI API klíčem
cp .env.example .env

# Vlož svůj OpenAI API klíč do .env
# Např.: OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
```

### 3. Instalace závislostí s `uv`

```bash
# Instalace všech dependencies
uv sync

# Případně přímo bez venv:
uv pip install openai python-dotenv
```

## Spuštění

### Pomocí uv (doporučeno)
```bash
uv run main_translator.py
```

### Alternativně - klasický Python
```bash
# Aktivuj venv (pokud je třeba)
source .venv/bin/activate

# Spusť script
python main_translator.py
```

## Příklady

```bash
# Překlad z angličtiny do češtiny
uv run main_translator.py

# Script spustí tři příklady:
# 1. "Hello, how are you today?" -> český překlad
# 2. "Ahoj, jak se máš?" -> anglický překlad
# 3. "Artificial Intelligence is revolutionizing..." -> český překlad
```

## Struktura kódu

```
main_translator.py
├── Funkce pro překlad (translate_en_to_cz, translate_cz_to_en)
├── Tools definice pro OpenAI API
├── Agent logika s function calling
└── Příklady v main sekci
```

## Klíčové koncepty

- **Function Calling** - Model automaticky volá registrované funkce
- **Tool Definitions** - JSON schéma popisující dostupné nástroje
- **LLM Routing** - Model je inteligentní, rozhoduje který tool použít
- **Message Loop** - Iterativní komunikace: uživatel → LLM → tool → LLM → odpověď

## Soubory projektu

- `main_translator.py` - Hlavní agent skript
- `pyproject.toml` - UV/pip konfigurace
- `.env.example` - Template pro API klíč
- `requirements.txt` - (legacy) pip dependencies
- `README.md` - Tato dokumentace

## Technologie

- **OpenAI API** - GPT-4o s function calling
- **Python 3.12+** - Programovací jazyk
- **python-dotenv** - Správa environment variables
- **uv** - Ultra-fast Python package manager

## Poznámky

- Agent používá `tool_choice="auto"`, model sám rozhoduje kdy použít nástroj
- Temperature je nastavena na 0.3 pro konzistentnější překlady
- Funkcí se pracuje i přímo s OpenAI API pro samotný překlad (optimalizace)
