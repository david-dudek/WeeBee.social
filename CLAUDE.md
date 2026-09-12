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

## Verification Scripts

The following executable scripts in `scripts/` handle recurring verification tasks and are called by hooks or manually:

### scripts/preflight.sh
Run before any session work: `./scripts/preflight.sh [expected-branch]`

Outputs:
- Current branch name
- Working tree status (clean/dirty)
- Last 3 commits
- Divergence from origin/main

Aborts if working tree has uncommitted changes or if expected branch doesn't match. Used by PreToolUse hooks to warn before edits.

### scripts/verify-mockups.sh
Run after mockup edits: `./scripts/verify-mockups.sh`

Verifies:
- Boots HTTP server on localhost:8000 (never uses file://)
- Checks HTTP 200 on all mockup/*.html files
- Captures screenshots at 320/768/1440px in light and dark modes
- Checks for horizontal overflow at 320px
- Reports failures and screenshot directory

Never verify HTML/CSS over `file://` URLs — the stylesheet silently fails to load.

## Custom Skills

### /resync
One-command re-sync of mockups/docs to SPEC version with verification and next-round queueing.

Usage: `/resync round:R2 target_branch:main next_round_name:R3`

See `.claude/skills/resync/SKILL.md` for full documentation. The skill:
1. Runs preflight checks
2. Applies edits from the round's prompt file
3. Verifies with HTTP server (320px reflow, links, overflow)
4. Bumps CHANGELOG.md
5. Writes the next round's prompt file
6. Reports verbatim diffs

Use this for moving between rounds (R1→R2→R3, etc.) rather than hand-writing each resync prompt.
