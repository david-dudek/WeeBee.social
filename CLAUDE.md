# Claude Code Guidelines for WeeBee Project

## Working Mode

### Discussion vs. Edit Mode
When a request says "discuss", "review", "analyze", or asks a question, do NOT edit, create, or write any files. Present findings and wait for explicit approval before touching the repo. Ask "shall I apply this?" instead of applying.

## Git / Branch Preflight

Before any edit: run `git status && git branch --show-current && git log --oneline -3` and confirm the target file is writable on this branch. TODO.md and prompt files are canonical on `main` only — never edit them from a feature/archetype branch. If uncommitted changes must move branches, spell out the full stash/cherry-pick sequence, not a single command.

## Mockups / Frontend

### Verifying Mockups
Never verify HTML/CSS over `file://` URLs or data-URL snapshots — the stylesheet silently fails to load and screenshots give false positives. Always start a local HTTP server (`python3 -m http.server 8000`) and verify at `http://localhost:8000/...`, including the 320px reflow check.

## Documentation Process

### Sourcing Rules
When triaging external reviews or judging whether a finding is new, read the primary review file directly — never infer from TODO.md summaries or secondhand notes. Quote the source line in your triage. If a source file is empty or unreadable, say so immediately rather than proceeding.

## Style

### Output Discipline
Respect stated word/length budgets: draft to the budget, run a word count before presenting, and stay silent about already-settled items. Define any coined term on first use.
