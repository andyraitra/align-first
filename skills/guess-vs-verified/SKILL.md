---
name: guess-vs-verified
description: Use when concluding a non-trivial investigation, claiming something is fixed or done, or committing — separates which claims were actually checked with a tool from which were assumed.
---

# Guess vs Verified

Before concluding an investigation, claiming a bug is fixed, or stating a
technical fact you're about to act on, produce a short grouped summary that
separates what you actually checked (read the file, ran the command,
grepped for the reference) from what you're assuming.

**Output**, in the user's language, once — right before the conclusion:

```
Verified: <claims confirmed via tool/read/run — brief>
Assumed: <claims not confirmed, omit entirely if none>
```

Never write "None" for an empty field — omit the field/line entirely. Don't
repeat this after every individual claim — once, at the checkpoint right
before concluding, is enough.

## Red Flags — you're about to skip this

- Concluding "this is fixed" / "this works" without having run anything
- "I'm confident this is how it behaves" with no read/grep/run behind it
- Time pressure ("just tell me it's fixed") pushing you to assert instead of check
- A confident final answer that, if you're honest, mixes things you checked with things you inferred

Stating something as fact because it's *probably* true is exactly the gap
this closes — if you didn't check it this session, it's Assumed, not
Verified.
