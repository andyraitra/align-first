# align-first

Two lightweight, portable AI-coding-agent skills that keep the agent aligned
with you — on what's being asked, and on what's actually been verified —
before and during non-trivial work. Both are token-frugal by design: short
templates, fields omitted when empty, no filler.

Works with any harness that supports the [Agent Skills](https://agentskills.io/specification)
open format: Claude Code, Cursor, Codex, GitHub Copilot, Windsurf, and more.

## The skills

- **`confirm-task-understanding`** — before starting the bulk of a
  non-trivial or ambiguous task, the agent restates what it understood and
  what it's assuming, then waits for your go-ahead. Stops wrong-direction
  work before it happens.
- **`guess-vs-verified`** — before concluding an investigation, claiming
  something is fixed or done, or committing, the agent separates what it
  actually checked with a tool from what it's assuming. Stops
  confident-sounding guesses from passing as fact.

## How this fits with other skills

| If you use | align-first adds |
|---|---|
| A full brainstorming/design process | A fast, standalone check for the small asks that never reach that process |
| A staged dev workflow (understand → plan → implement) | The same understanding-check, usable outside a full workflow session |
| A plan-vs-docs consistency check | A check that runs *before* a plan exists |
| A "verify before claiming done" discipline | The human-facing summary of what was checked vs assumed, not just the internal discipline of checking |

## Install

**1. npx (recommended, works across harnesses):**
```bash
npx skills add andyraitra/align-first
# or target specific agents:
npx skills add andyraitra/align-first -a claude-code -a cursor -a copilot
```

**2. Manual:**
```bash
git clone https://github.com/andyraitra/align-first
# then copy the skill folder(s) you want into your harness's skills directory, e.g. for confirm-task-understanding:
cp -r align-first/skills/confirm-task-understanding ~/.claude/skills/            # Claude Code
cp -r align-first/skills/confirm-task-understanding ~/.cursor/skills/            # Cursor
cp -r align-first/skills/confirm-task-understanding ~/.agents/skills/            # Codex
cp -r align-first/skills/confirm-task-understanding .github/copilot/skills/      # Copilot (project-level)
# same pattern for guess-vs-verified — just swap the folder name in the source path
```

## License

MIT — see [LICENSE](LICENSE).
