# AI Agenti – Kurz

Pracovní repo pro kurz AI Agenti (29.1. - 5.3.2026).

## 🚀 Quick Start

### 1. Aktivace Python Virtual Environment

**Linux/macOS:**
```bash
source venv/bin/activate
```

**Windows:**
```cmd
venv\Scripts\activate
```

### 2. Instalace Dependencies

```bash
pip install -r requirements.txt
```

### 3. Deaktivace Venv

```bash
deactivate
```

## 📚 O Kurzu

- **Termín:** 29. ledna - 5. března 2026
- **Formát:** Live online lekce (úterý & čtvrtek, 18:00-20:00)
- **Lektor:** Lukáš Kellerstein (Microsoft, Senior Software Engineer)

### Co se naučíme:
- Volání API velkých jazykových modelů (OpenAI, Anthropic, HuggingFace, Ollama)
- Propojení AI s databázemi (SQL, NoSQL, vektorové DB)
- Vytváření vlastních AI agentů od základu
- Frameworky: LangChain, Semantic Kernel, Autogen, LangGraph, n8n
- Reinforcement learning (Gymnasium, PettingZoo, Stable-Baselines3)
- Multi-agentní systémy

## 🛠 Tech Stack

- Python 3.13.9
- LangChain, Autogen, Semantic Kernel
- OpenAI API, Anthropic
- ChromaDB, SQLAlchemy
- Gymnasium, Stable-Baselines3

## 📖 Reference

- [Global Classes CZE](https://github.com/Global-Classes-CZE)
- [AI Chatbots Examples](examples/ai-chatbots/) - Reference implementace z kurzu

## 📂 Project Structure

```
kurz-ai-agenti/
├── examples/           # Reference materiály (není verzováno)
│   └── ai-chatbots/    # Naklonováno z Global-Classes-CZE
│       ├── lekce1-10/  # Příklady kódu z lekcí
│       └── README*.md  # Dokumentace různých agentů
├── lectures/           # Vaše implementace z lekcí
│   ├── lecture01/
│   ├── lecture02/
│   └── ...
├── projects/           # Vaše vlastní projekty
│   └── final-project/
├── workspace/          # AI Agent Framework tracking
│   ├── sessions/       # Session tracking
│   ├── bugs.md
│   └── session-log.md
├── venv/               # Python virtual environment
├── requirements.txt    # Python dependencies
└── README.md
```

## 📝 Development

Projekt používá AI Agent Framework v3.0.0 pro tracking práce.  
Session tracking: `workspace/sessions/`

