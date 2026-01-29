# AI Agent Framework v3.0.0

This project uses AI Agent Framework for structured AI-assisted development.

## 🎯 CRITICAL: Workspace Location

**ABSOLUTE PATH TO WORKSPACE:** `PROJECT_ROOT/workspace/`

All session files, bug tracking, and epic management MUST use this directory:
- **Session files:** `workspace/sessions/active/YYYY-MM-DD-topic.md`
- **Bug tracking:** `workspace/bugs.md`
- **Session log:** `workspace/session-log.md`
- **Epic tracking:** `workspace/epics/active/{epic-id}/`
- **Quick reference:** `workspace/.quick-reference/`

## Core Principles

1. **Think-First:** Always plan before coding
2. **Quality Gates:** Check before every commit
3. **Session Management:** Track all work in `workspace/sessions/active/`
4. **Clear Communication:** Short commands, full workflows

## Quick Commands for PM

See [quick-reference/pm-commands.md](quick-reference/pm-commands.md):

- **"GO"** - Approve plan and proceed
- **"REVISE"** - Request plan changes
- **"STOP"** - Halt current work
- **"STATUS"** - Show current progress

## AI Workflow

### Before Starting ANY Task:
1. Load `core/meta-prompt.md`
2. Create Think-First Plan (from `core/think-first.md`)
3. **CREATE SESSION FILE:** `workspace/sessions/active/YYYY-MM-DD-topic.md`
4. Wait for PM approval (GO/REVISE)
5. Execute with session tracking

### Before EVERY Commit:
1. Run quality gates from `core/quality-gates.md`
2. Verify all tests pass
3. Check documentation updated
4. Update `workspace/session-log.md`
5. Proper commit message format (see `core/git-commit.md`)

## Directory Structure

```
PROJECT_ROOT/
├── .github/                                 # GitHub Copilot instructions (auto-loaded)
│   ├── copilot-instructions.md              # This file (main entry point)
│   ├── core/                                # Core framework instructions
│   │   ├── meta-prompt.md      # AI role & behavior
│   │   ├── think-first.md      # Planning approach
│   │   ├── quality-gates.md    # Pre-commit checks
│   │   ├── coding-standards.md # Code quality rules
│   │   ├── git-commit.md       # Commit format
│   │   ├── session-mgmt.md     # Session tracking
│   │   ├── testing.md          # Testing standards
│   │   └── project-guide.md    # Project-specific info
│   ├── quick-reference/                     # Quick reference guides
│   │   ├── pm-commands.md      # PM command reference
│   │   ├── new-chat.md         # New chat protocol
│   │   ├── handoff.md          # Handoff protocol
│   │   ├── task-complete.md    # Task completion
│   │   └── bug-report.md       # Bug reporting
│   └── workflows/                           # Workflow templates
│       ├── bug-fix.md          # Bug fixing workflow
│       ├── new-feature.md      # Feature development
│       ├── refactoring.md      # Code refactoring
│       ├── ui-sync.md          # UI/Backend sync
│       └── exploration.md      # Codebase exploration
│
└── workspace/                               # ⚠️ WORKSPACE ROOT - ALL AI WORK HERE
    ├── bugs.md                              # Bug tracking (CRITICAL)
    ├── session-log.md                       # Session history (CRITICAL)
    ├── .quick-reference/                    # Local quick reference copies
    │   ├── pm-commands.md                   # (for easy PM access)
    │   ├── new-chat.md
    │   ├── handoff.md
    │   ├── task-complete.md
    │   └── bug-report.md
    ├── templates/                           # Session templates (CRITICAL)
    │   ├── session-bug-fix.md               # Bug fix session template
    │   ├── session-new-feature.md           # Feature session template
    │   ├── session-refactoring.md           # Refactoring session template
    │   ├── session-exploration.md           # Exploration session template
    │   └── epic-breakdown.md                # Epic planning template
    ├── automation/                          # Automation prompts & scripts
    │   ├── code-audit.md                    # Code audit automation
    │   ├── database-integrity.md            # Database checks
    │   ├── docs-integrity.md                # Documentation validation
    │   ├── frontend-audit.md                # Frontend audit
    │   ├── project-analysis-prompt.md       # Project analysis
    │   └── *.sh                             # Automation scripts
    ├── sessions/                            # Session tracking
    │   ├── active/                          # Current work (AI creates files here)
    │   │   └── YYYY-MM-DD-topic.md          # Session file format
    │   └── completed/                       # Finished sessions
    └── epics/                               # Multi-session projects
        ├── active/                          # Active epics
        │   └── {epic-id}/
        │       ├── epic-plan.md
        │       └── sessions/
        │           └── YYYY-MM-DD-*.md
        └── completed/                       # Completed epics
```

## How It Works

GitHub Copilot automatically loads instructions based on:
- **All files:** Instructions with `applyTo: "**/*"`
- **Specific paths:** Instructions with path-specific patterns
- **Current context:** Which file you're editing

All `.md` files include YAML frontmatter with `applyTo` patterns.

## For Developers

**Quick Start (5 minutes):** Read `core/meta-prompt.md`

**For AI:** 
- Always load meta-prompt at session start
- **USE TEMPLATES FROM:** `.github/templates/session-*.md`
- **CREATE SESSION FILE IN:** `workspace/sessions/active/YYYY-MM-DD-topic.md`
- Update `workspace/session-log.md` after completion
- Track bugs in `workspace/bugs.md`

**For PM:** 
- Use short commands from `workspace/.quick-reference/pm-commands.md`
- Check `workspace/session-log.md` for history
- Review `workspace/bugs.md` for known issues

**Reference docs:** Check `workspace/.quick-reference/` for human-readable versions

## Customization

Edit `core/project-guide.md` with your project specifics:
- Tech stack
- Build commands
- Project structure
- Coding conventions
- Common workflows

## Version

Framework: 3.0.0
Deployed: 2026-01-24

---

**⚠️ REMEMBER: All AI work goes to `workspace/` directory!**

GitHub Copilot loads instructions automatically based on file context.
