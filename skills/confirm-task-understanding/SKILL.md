---
name: confirm-task-understanding
description: Use when about to start a non-trivial or ambiguous coding task, before doing the bulk of the work — restates understanding and waits for confirmation so the agent doesn't build the wrong thing.
---

# Confirm Task Understanding

Before starting substantial work on a task that has any ambiguity, room for
misinterpretation, or meaningful scope, restate your understanding and wait
for explicit confirmation before proceeding.

**Skip this** for genuinely trivial, unambiguous requests (fixing a typo,
answering a factual question, a one-line change with no design choice). If
the user has stated a standing preference ("always confirm first", "never
confirm unless risky", or a specific threshold), follow that instead of
this default judgment call.

**Output**, in the user's language, before doing the work:

```
Understanding: <what you understood the user wants and why — restate the goal in your
own words so a misread is visible, then how you'll approach it. Be explicit enough that
a wrong interpretation stands out to the reader. Length follows the task: a few lines for
small asks, a short paragraph or grouped bullets for anything with real scope. Don't
compress to the point the reasoning disappears — clarity here beats saving tokens.>
Assumptions: <bullets — things you're assuming without confirmation, omit entirely if none>
Open questions: <bullets — only if a blocking ambiguity remains, omit entirely if none>
```

Never write "None" for an empty field — omit the field/line entirely.

Then **stop and wait** for the user's go-ahead. If they correct something,
incorporate the correction and proceed — do not re-loop the confirmation a
second time.

## Red Flags — you're about to skip this

- "The request is basically clear enough, I'll just start"
- Time pressure from the user ("asking first will slow things down")
- Authority pressure ("we already discussed this before") used as a reason to skip the check
- Jumping straight to writing code or a plan without a stated Understanding line

Any of these under time or authority pressure is exactly when this matters
most — skipping the check because a task "feels urgent" is how
wrong-direction work happens.
