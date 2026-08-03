# Prompt 01 — Changelog extraction and project-wide versioning

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** README.md, SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md, new CHANGELOG.md
> **Depends on:** nothing. Run this first.
> **Expected outcome:** project version 1.17, no content changes.

---

You are working in the WeeBee design-document repository. Read `README.md` first for
context, then the **top ~10 lines only** of `SPEC.md`, `ARCHITECTURE.md` and
`BUILD_PLAN.md` — you need their version headers, not their bodies.

This is a **founder-directed design session**, so the BUILD_PLAN §0.2 rule 5 prohibition
on editing SPEC.md, ARCHITECTURE.md and BUILD_PLAN.md does not apply here. It applies to
build steps. Make the edits described below.

This task is **structural only. Do not change the meaning of a single sentence of
project content.** If you believe a historical changelog entry is wrong, say so in chat;
do not fix it.

## The problem

Each of the three main documents carries its entire cumulative version history in an
italic `*( … )*` block directly under its status line. SPEC.md's is now several thousand
words and sits between the reader and §1. The history is valuable — it records why
decisions were made and what was rejected — but it has outgrown the position.

Worse, the three documents carry **independent** version numbers (SPEC 1.16,
ARCHITECTURE 1.7, BUILD_PLAN 1.6) whose relationship is only recoverable by reading
prose like "1.5, synced to SPEC v1.12 / ARCHITECTURE v1.6". This directly caused a real
failure: ARCHITECTURE and BUILD_PLAN are currently unsynced to SPEC v1.16 and both still
instruct the builder to implement two constants SPEC retired, and nothing about the
version numbers makes that visible.

## The new scheme (decided by the founder — implement, don't relitigate)

1. **One version number for the whole project.** It is currently 1.16, inherited from
   SPEC.md because SPEC is the spine.
2. **A version bump covers whatever changed.** If a change touches SPEC.md and README.md
   only, the *project* goes to 1.17. BUILD_PLAN.md is then also "at 1.17" — identical in
   content to its 1.16 self, and CHANGELOG.md says so explicitly.
3. **Every version's entry names the status of every file**, including the untouched
   ones. "Unchanged" is information, and stating it is what makes an unsynced document
   visible instead of invisible.
4. **CHANGELOG.md is the single home for history.** Document headers keep only a pointer.

## Deliverable 1 — `CHANGELOG.md` at the repository root

Structure, newest version first:

```markdown
# Changelog — WeeBee

<short section explaining the versioning rule: one number for the whole project,
every entry names every file's status, "unchanged" is a real status. Three or four
sentences. Also state that the version number lives in each document's header and
must match this file.>

---

## 1.17 — <today's date>

| File | Status |
|---|---|
| README.md | changed — version header added |
| SPEC.md | changed — history moved to this file |
| ARCHITECTURE.md | changed — history moved to this file |
| BUILD_PLAN.md | changed — history moved to this file |
| CHANGELOG.md | new |

Structural only. No project content changed in this version: no requirement, constant,
decision or build step was added, removed or reworded. Version history was moved out of
the four document headers into this file, and the project moved to a single
whole-project version number.

**Note carried forward:** ARCHITECTURE.md and BUILD_PLAN.md were last synced to SPEC
v1.15 and remain unsynced to the v1.16 spec changes. See `TODO.md` prompt 09.

---

## 1.16 — 2026-08-03

| File | Status |
|---|---|
| README.md | unchanged since 1.15 |
| SPEC.md | changed |
| ARCHITECTURE.md | **unchanged since 1.15 — not yet synced** |
| BUILD_PLAN.md | **unchanged since 1.15 — not yet synced** |

### SPEC.md
<the existing 1.16 prose, moved verbatim>

---

## 1.15 — <date>
… and so on, down to the earliest entry.
```

### Rules for reconstructing the history

- **Move the prose verbatim.** Reorganize where it sits; do not rewrite, summarize or
  "improve" it. The rejected-alternative records in particular are load-bearing — README
  says every rejected suggestion keeps its reasons.
- **SPEC's version numbers are the project spine.** Map each ARCHITECTURE and BUILD_PLAN
  entry onto the SPEC version it says it synced to. Those entries state it explicitly
  ("1.5, synced to SPEC v1.12 / ARCHITECTURE v1.6"), so the mapping is derivable rather
  than guessed.
- **Where an entry maps onto a range of SPEC versions**, put it under the highest one in
  the range and note the range in the text.
- **Where a mapping genuinely cannot be determined, stop and ask.** Do not guess. An
  invented history is worse than a gap.
- **File statuses in old entries must be honest.** If ARCHITECTURE was untouched between
  SPEC 1.9 and 1.12, three entries say "unchanged since 1.9". Do not backfill statuses
  you cannot support from the text — write "not recorded" and flag it in chat.
- **Add a mapping appendix at the bottom** — a table of historical per-file version
  numbers against project versions (SPEC 1.16 → 1.16; ARCHITECTURE 1.7 → 1.15;
  BUILD_PLAN 1.6 → 1.15; …). Old conversations and notes refer to the per-file numbers,
  so the translation must not be lost.

## Deliverable 2 — new headers on the four documents

Delete the `*( … )*` history block from SPEC.md, ARCHITECTURE.md and BUILD_PLAN.md.
Replace the whole header area with exactly this shape:

```markdown
# WeeBee — Platform Specification

**Project version:** 1.17 · <date> · DRAFT pending founder review
**This file last changed in:** 1.17 (structural only; last content change 1.16)
**History:** see [CHANGELOG.md](CHANGELOG.md)
```

Add the same three-line block to README.md, which currently carries no version at all.
Keep each document's existing status wording ("DRAFT pending founder review", "under
founder review") — that is content, and it differs per file.

Do **not** add a summary line beyond the above. The whole point is that the header stops
growing.

## Deliverable 3 — three consequential edits

1. **README.md, "How to give feedback"** says accepted changes get "a version bump and
   changelog note." That is now literally true and points somewhere. Adjust the sentence
   to name CHANGELOG.md.
2. **SPEC.md §18 (Downstream Documents)** — check whether it needs CHANGELOG.md added to
   the document set. Report what you find before editing.
3. **BUILD_PLAN.md §2.4** installs guards (tool deny rules, pre-commit hook) protecting
   SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md and `constants.py` from AI edits.
   **CHANGELOG.md is now part of the versioned record and arguably belongs in that
   list.** Do not add it unilaterally — put the question to the founder in chat with the
   tradeoff: protecting it prevents an AI quietly rewriting history, but the file must
   also be *editable* in every design session, which is exactly what the deny rules
   block. Recommend a resolution.

## Deliverable 4 — update `TODO.md`

Set prompt 01's status to `done` and its "Landed in" column to `1.17`.

## Verification before you finish

- `CHANGELOG.md` contains every sentence that was in the four headers. Confirm by
  comparing against `git show HEAD:SPEC.md` etc. — the old text is in git history, so
  nothing is lost if you slip, but check anyway.
- Every version section names all four files' statuses.
- The three-line header is identical in shape across all four documents.
- No document body was touched.
- `git diff --stat` shows changes only to the four headers plus the two README/SPEC
  sentences above.
