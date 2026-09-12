---
name: resync
description: Re-sync mockups/docs to current SPEC version and queue the next round
---

# Resync Workflow

Run this skill to move from one round (R1, R2, R3, etc.) to the next. It handles preflight checks, applies spec-version edits, verifies at 320px, bumps CHANGELOG, and queues the next round's prompt.

## Required inputs

Pass these in your message when invoking `/resync`:
- **round**: The round you're completing (e.g., "R2") — the skill looks for `prompts/<round>.md` to confirm the current scope
- **target_branch**: The branch to land work on (usually "main" for canonical docs, "archetypes" or a feature branch for mockup/prototype work)
- **next_round_name**: The label for the queued prompt (e.g., "R3" or "A0b-resync")

## Execution steps

1. **Preflight**: Run `git status && git branch --show-current && git log --oneline -3`. Abort if working tree is dirty or not on target_branch.

2. **Load spec**: Read SPEC.md version header and the current round's scope from `prompts/<round>.md`.

3. **Apply edits**: Execute all edits described in the prompt file. Do NOT edit TODO.md unless on main branch.

4. **Verify**: Start HTTP server on 8000, capture screenshots at 320px and 1280px, check for horizontal overflow at 320px, verify internal links load without 404. Never use file:// URLs.

5. **Update CHANGELOG**: Add entry with new SPEC version, round identifier, and key changes. Increment version number appropriately.

6. **Queue next round**: Write `prompts/<next_round_name>.md` with a runnable prompt for the next round. Register it in `prompts/QUEUE.md` if that file exists.

7. **Report**: Show verbatim diff summary per file edited. List deliverables with file paths and confirm all exist on disk.

## When to use

Use `/resync` when you have:
- A working prompt file describing one round's changes
- Mockups or docs that need to move to the next SPEC version
- A clear next-round scope already decided or documented
- Time to wait for verification (screenshots, link checks, overflow assertions)

Do NOT use `/resync` for:
- One-off edits (use direct Edit tool)
- Discussion-phase work (use discussion mode first)
- Decisions not yet finalized (use discussion prompt instead)

## Example invocation

```
/resync round:R2 target_branch:main next_round_name:R3
```

This will:
1. Load `prompts/R2.md` to see what R2 intended
2. Check git status on main
3. Apply R2's edits
4. Verify with HTTP server
5. Bump CHANGELOG
6. Write `prompts/R3.md` with the next prompt
7. Report diff summary
