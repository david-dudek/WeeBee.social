---
type: handoff-summary
title: "WeeBee design-document review strategy"
detail: standard
created_utc: 2026-09-16T01:02:23Z
created_local: 2026-09-15T21:02:23-04:00
surface: claude-code
session_id: b405e408-2f2e-4b96-bfe8-e94867248786
project_dir: /Users/dudek/Documents/Claude/social network
transcript_file: 2026-09-16_0102Z_design-doc-review-strategy_transcript.md
previous_summary: none found
---

# WeeBee design-document review strategy

An advisory session, not a work session: no files in the repository were created or changed.
David said he felt overwhelmed by the volume of design documentation (~190,000 words across
SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md, CHANGELOG.md, the six external AI review files and
`mockups/NOTES.md`) and asked for strategies to understand it and move the project forward
toward founder approval and the build. Claude surveyed the repository and proposed a strategy
built around converting the document pile into a finite decision queue. **David had not yet
responded to the proposal when the handoff was requested**, so nothing here is agreed.

## Decisions

None. Every item below is a proposal awaiting David's response.

## Open questions

- **Does David want the proposed "founder's decision docket" built, and starting with the
  `mockups/NOTES.md` triage?** This was Claude's closing recommendation and the session's main
  open fork. The alternative Claude offered was something smaller first — a plain-language
  walkthrough of a single SPEC.md section, to test whether the three-pen reading method suits him.
- **Should the 49 `mockups/NOTES.md` entries be triaged and resolved before prompt 09 runs?**
  Claude argued yes and David's own stated instinct agreed, but this has not been formally
  settled or recorded in TODO.md. Prompt 09 is technically unblocked (its dependencies 02–08
  and 10–12 are all marked `done`), so the hold is a judgment call, not a dependency.
- **How should founder approval be structured?** Claude proposed approving SPEC.md section by
  section with dated in-document records, citing ARCHITECTURE.md §15 item 4 ("APPROVED by
  founder 2026-07-08") as existing precedent for a scoped, dated approval. Not discussed by David.
- **(Pre-existing, unchanged by this session)** The eight questions parked in TODO.md's "Open
  questions parked for later", including whether SPEC.md's Purpose line promises too much,
  SPEC §2's logged-out page list disagreeing with SPEC §16.1's, and the constant values as a
  whole, which TODO.md records as "Still open" because no external reviewer engaged with them.

## Next steps

1. **David: reply to the closing fork** — decision docket first, or a smaller SPEC walkthrough first.
2. **Claude (if approved): triage the 49 entries in `mockups/NOTES.md`**, sorting each into
   *needs a founder decision* / *needs a SPEC change* / *mockup-only, no action*.
3. **Claude (if approved): assemble the founder's decision docket** from four sources that
   currently live apart — the NOTES.md triage, TODO.md's eight parked questions,
   ARCHITECTURE.md §15's two deferred picks (email provider, VPS provider), and SPEC.md §14's
   23 constants marked ✎ plus the headline caps from README.md §1 (300 / 30 / 90). Each entry:
   the question in plain English, why it matters, what breaks if guessed wrong, a recommendation,
   and space for David's answer. Sorted build-blocking first.
4. **David: answer the docket in batches**, four or five items per sitting.
5. **Claude: batch the resulting SPEC changes into 2–4 new prompt files** (13, 14, 15…) in the
   established `prompts/` format, then run them.
6. **Run prompt 09** (`prompts/09-sync-arch-and-buildplan.md`) once, against a settled SPEC.
   TODO.md warns BUILD_PLAN Phase 2 must not start before 09 is done, because the retired
   constants `BIO_CHANGE_COOLDOWN_HOURS` and `BIO_EDIT_GRACE_MINUTES` remain live instructions
   in five places across ARCHITECTURE.md and BUILD_PLAN.md.
7. **Hold a constants review session** — SPEC.md §14's ✎ list and the headline numbers.
8. **David, in parallel and unblocked now: BUILD_PLAN.md Phase 1 ("Your Machine", [FOUNDER])** —
   Docker Desktop, git, the AI coding tool, and the private `thenetwork` GitHub repo. Step 1.3
   (register the domain) is already marked done, 2026-07-25. TODO.md's hold applies to Phase 2,
   not Phase 1.

## Files and references

- `README.md` — states what is and isn't up for review; §1 opens every cap value to challenge.
- `SPEC.md` (~36,000 words, 18 sections + Appendix A) — the document needing real founder
  judgment. §14 is the configuration-constants table, 23 rows marked ✎ as "operator-tunable
  judgment calls rather than agreed design decisions".
- `ARCHITECTURE.md` (~22,400 words) — §15 "Open Points — Resolution Record" holds nine items;
  item 4 records whole-document founder approval on 2026-07-08; items 2 and 3 defer the email
  provider (Postmark recommended) and VPS provider/location (Hetzner recommended).
- `BUILD_PLAN.md` (~17,700 words, Phase 0 through Phase 17 plus an Appendix) — Phase 1 is
  [FOUNDER] and unblocked; Phase 4 is flagged in-document as "the most important phase".
- `mockups/NOTES.md` (~10,200 words, 49 numbered entries) — Claude called this the
  highest-value document for David right now. Records every gap and judgment call from the
  eight-session M1–M8 mockup track, which built 56 user-facing surfaces.
- `TODO.md` — the queue. Prompts 01–08 and 10–12 are `done` (landing project versions 1.17
  through 1.27); prompt 09 is `not run`. Also holds "Stopped build steps" (empty) and the
  parked-questions list.
- `CHANGELOG.md` (~28,700 words) and the six `1.16_*`/`1.27_*` external AI review files
  (~22,000 words) — Claude advised these should never be read start-to-finish; they are
  lookup and already-triaged records respectively.
- `mockups/site/` — 56 built pages. Claude recommended promoting these from "exercise" to
  primary review surface, with SPEC.md consulted only when a page raises a question.
- Reading method proposed for the printed 1.27 PDFs in `00_scratch/`: three passes, three
  pens — green for surprise, red for disagreement, blue for incomprehension, with blue marks
  on *user-facing behaviour* treated as defects in the document (since SPEC's header promises
  it can be built from alone) and blue marks on *implementation* treated as expected and harmless.

## Since the previous handoff

No previous summary found.

## Caveats

- **The session made no repository changes.** Working tree was clean at both start and end,
  on branch `archetypes`.
- **Claude's survey of the repository was incomplete.** The initial file listing was piped
  through `head -100` and silently truncated. As a result the advice given in this session
  did not account for `CLAUDE.md`, `scripts/`, `.claude/skills/`, or — most significantly —
  the `archetypes/` track (`PLAN.md`, `BRIEF.md`, `A0-brief.md`, `A0b-resync.md`, `A7-susan.md`,
  `Social_Media_Archetypes.md`, `07-susan.md`, `PROMPT.md`), which is the active work on the
  current branch and was last re-synced to project version 1.31. **Every word count, sequencing
  claim and "what you must read" judgment in this session should be re-checked against the
  archetypes track before being acted on**; in particular, the claim that the project version
  is 1.27 comes from the document headers Claude read and conflicts with the 1.31 named in
  commit `f81ff4b`.
- `handoffs/` is inside the git repository and is not gitignored. The exporter warned that
  transcripts contain everything typed or pasted into the session, including any secrets, so
  review before committing.
- No context compaction occurred; the transcript is a complete word-for-word export.
