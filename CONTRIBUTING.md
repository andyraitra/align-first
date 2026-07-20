# Contributing to align-first

Thanks for wanting to improve align-first. This project ships small, portable
agent skills, so contributions stay focused: keep them token-frugal, portable
across harnesses, and grounded in a real failure the skill prevents.

## Ground rules

- **Nobody pushes to `main` directly** — including maintainers. All changes go
  through a pull request from a branch or fork, and CI must pass before merge.
- Keep skills harness-agnostic. Don't hardcode one tool's paths or commands in
  a `SKILL.md` unless the skill is explicitly tool-specific.
- Prefer editing an existing skill over adding a near-duplicate.

## Workflow

1. **Fork** the repo (or create a branch if you're a maintainer).
2. Create a topic branch: `git checkout -b feat/short-description`.
3. Make your change. For skill changes, follow the guidance in
   [`skills/`](skills/) — restate the failure the skill prevents.
4. Commit using [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat(skill-name): ...` — new behavior
   - `fix(skill-name): ...` — corrected behavior
   - `docs: ...`, `chore: ...`, `ci: ...`
   - No AI attribution / `Co-Authored-By` trailers.
5. Push and open a **pull request** against `main`. Fill in the PR template.
6. Wait for CI (skill validation) to pass. A maintainer merges.

## Adding or changing a skill

Each skill lives in `skills/<skill-name>/SKILL.md` with YAML frontmatter:

```yaml
---
name: skill-name-with-hyphens
description: Use when <specific triggering conditions> — <what it keeps aligned>.
---
```

- `name`: letters, numbers, hyphens only.
- `description`: third person, starts with "Use when…", states *when* to use
  the skill (not a summary of its steps).
- Body: the rule, a skip clause for trivial cases, and a "Red Flags" section.

Before proposing a skill change, confirm it prevents a failure an agent
actually makes without it — that's the bar for this repo.

## Reporting bugs / ideas

Open an issue using the templates. Include the harness (Claude Code, Cursor,
Codex, …) and a concrete before/after of the agent behavior.
