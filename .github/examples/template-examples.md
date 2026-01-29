---
applyTo: "**/*"
---

# 📑 Template Examples

## Example 1: Multi-session bug fix (3 sessions + PM gate)
**Context:** PM žádá rozdělit práci do 3 session files a pokračovat až po potvrzení.

**Workflow:**
1) Plan: Navrhni tři kroky (např. Repro+Root cause → Fix+Tests → Cleanup+Docs) a předlož PM ke schválení.
2) Session files: Vytvoř v `workspace/sessions/active/` tři soubory (např. `2026-01-25-bug-s1.md`, `...-s2.md`, `...-s3.md`) podle `session-bug-fix.md` šablony.
3) Branch: `git checkout -b session/2026-01-25-bug-s1` a pracuj jen v této větvi pro první session.
4) Execute Session 1: Reprodukce a root cause. Na konci update session file + žádost PM: "Hotovo S1, můžu pokračovat na S2?" → čekej na GO.
5) Session 2: Stejně vytvoř branch `session/2026-01-25-bug-s2` (nebo pokračuj v téže větvi jen pokud PM řekne) a dělej fix + testy. Po dokončení znovu PM potvrzení před S3.
6) Session 3: Cleanup, dokumentace, finální verifikace. Teprve po GO od PM: `git mv` session file do `completed/` v příslušné větvi, merge do main, smazat branch.
7) Session log: Po finálním GO update `workspace/session-log.md` + případně `bugs.md`.

**Key Gates:** PO KAŽDÉ session čekej na PM GO před dalším krokem; žádné auto-merge/commit bez schválení.

---

## Example 2: Multi-session hotfix + data cleanup (3 sessions)
**Context:** Náročný hotfix s migrací dat a rolloutem. PM chce tři fáze a každá musí projít PM review.

**Workflow:**
1) Session files: `...-hotfix-s1.md` (investigace), `...-hotfix-s2.md` (implementace + testy), `...-hotfix-s3.md` (data cleanup + rollout check).
2) Branching: Pro každou session vlastní větev (`session/YYYY-MM-DD-hotfix-s1`, ...-s2, ...-s3) kvůli čistým diffům a snadnému rollbacku.
3) Session 1: Repro + diagnostika + návrh změn. Hand-off blok pro PM s jasným plánem na S2. Čekej na GO.
4) Session 2: Implementace + nové testy. Po dokončení požádej PM o review výsledků a povolení pokračovat na S3.
5) Session 3: Datové opravy / cleanup skripty, finální verifikace, dokumentace. Po PM GO: archivuj session file ve své větvi (`git mv .../active/...s3.md .../completed/`), merge do main, smaž větev.
6) Logging: Každá session aktualizuje svůj soubor; finální session aktualizuje `session-log.md` a relevantní docs.

**Key Gates:** PM GO před vstupem do S2 a S3; finální merge a archivace pouze po PM schválení.
