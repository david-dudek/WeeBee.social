# Mockup track — re-sync plan after SPEC 1.28–1.30

> **Run in a fresh session.** Paste everything below the line.
> **Touches (this session):** nothing yet — it produces a **written plan** and asks the
> founder four questions. The work it plans touches `mockups/` and `prompts/mockups/`.
> **No law file is edited by this session or by the track it plans.**
> **Depends on:** prompts 14, 13 and 15 — all run, landing 1.28, 1.29 and 1.30.
> **Expected outcome:** an agreed plan, written to a file, for bringing the mockup track from
> SPEC 1.27 to SPEC 1.30 — which branch the work happens on, which pages change, which of the
> eight M sessions re-run, and what it costs.

---

**This is a discussion prompt before it is an editing prompt.** The questions in §4 belong to
the founder and several of them change the size of the job by a factor of four. Do not settle
them yourself and start editing pages. Put them to the founder, take the answers, write the
plan, and stop.

You are working in the WeeBee design-document repository — a small, private, deliberately
anti-viral social network, in design and not yet built. Read `README.md` for the shape of the
project and `prompts/mockups/README.md` for how the mockup track is organised.

## 0. How to work

- **Follow this prompt precisely.** Produce the plan it asks for — no more, no less. Do not
  start editing mockup pages, do not re-run an M session, and do not expand into design
  changes.
- **Do not fabricate.** Every constant, SPEC section number, file path, page name, branch name
  and interface string in your plan must be one you verified by reading the repository. Never
  invent a section that does not exist or a page that is not in `mockups/pages/`. If you
  cannot confirm something, leave it out or mark it explicitly as unverified.
- **Ask rather than guess.** §4 is the list of things the founder holds. If something else is
  ambiguous or you are missing information, ask in your reply instead of picking an answer.
- **State uncertainty as uncertainty.** Mark your guesses about scope, cost or founder intent
  as guesses. Do not present a judgement call as settled.
- **Verify before finishing.** Re-read your plan hunting for errors, weak points and edge
  cases: unverified citations, pages you assumed were affected without checking, steps that
  will blow the budget, instructions a cold session could misread.
- **Work economically.** This runs on a Claude Pro ($20/month) budget. Prefer targeted reads
  over whole files — `SPEC.md` is over 200 KB and reading it whole is never the right move.
  Do not re-read what you have already read. **Flag up front any step likely to consume
  significant usage**, and say so plainly rather than discovering it mid-session.

## 1. Where things stand — verified as of this writing

Confirm each of these yourself before relying on it; they were true when this prompt was
written and the repository moves.

**The numbered design queue has advanced three versions.** `TODO.md`'s queue table:

| Prompt | Landed | What it changed |
|---|---|---|
| 14 — the Gathering Test | **1.28** | New SPEC §1.4 and README. **ARCHITECTURE and BUILD_PLAN unchanged** |
| 13 — delegation principle & link policy | **1.29** | New SPEC §1.5; §7.2.3 rewritten; **new §7.2.4**; §10.2 extended; §4.6.1, §7.2, §7.5, §7.8, §9.4, §10.1, §13.1, §13.5, §14, §16.3, §17 reconciled |
| 15 — reporting a contact card | **1.30** | §13.2 gains a fourth report target; **§10.4 rewritten — an answered card is now a page**; §10.2's build gate lifted; §13.2.1, §13.1, §13.3, §9.1, §16.3 reconciled |

Project version is **1.30**. `prompts/09-sync-arch-and-buildplan.md` is the **only** numbered
prompt still unrun.

**The mockup track was built against 1.27 and has not moved.** `prompts/mockups/README.md`
says so in its own words: *"Started against project version 1.27."* The `mockups` branch's
`README.md` still reads `**Project version:** 1.27`.

**The three branches have genuinely diverged, in both directions.**

- `main` — carries SPEC 1.30, prompts 13/14/15, and an updated 09. **Has no `mockups/`
  directory at all.**
- `mockups` — carries the 67 pages in `mockups/pages/`, `CRIB.md`, `NOTES.md`, `build.py`,
  `styles.css`. Its SPEC is 1.27. It also carries things `main` does not: `MODEL-ADVISOR.md`,
  `content-commentary-separation.md`, a 12-line-longer `prompts/mockups/README.md`, and **nine
  extra lines in every one of the eight M prompts** (the simulated-content-versus-build-
  commentary rule and its `.commentary` toggle).
- `archetypes` — descends from `mockups`, so it contains the whole mockup track plus the
  archetype work. It is **missing one commit that is on `main`** (`06ef1e0`, the person-tagging
  TODO entry).

So the M prompts are not simply "behind"; `main` and `mockups` have each gained material the
other lacks. Any merge has to be reasoned about, not assumed clean.

## 2. What changed, and what it plausibly touches

**This section is a starting hypothesis, not a finding.** Verify each row against the actual
pages before putting it in the plan, and correct this table where it is wrong.

**1.28 (§1.4, the Gathering Test)** is a stated principle with no user-facing surface. The
CHANGELOG records ARCHITECTURE and BUILD_PLAN as unchanged and *"nothing owed."* Expect **no
mockup work** from it, and say so explicitly rather than leaving it unaddressed.

**1.29 is the expensive one.** SPEC §7.2.4 defines three outcomes for a link — approved
renders clickable, unapproved renders as non-clickable text (with a copy affordance), and a
blocklisted domain is refused before publication. That rule applies to posts, comments and
contact cards alike. Candidate pages, to verify: `composer.html`, `post-editor.html`,
`post-feed.html`, `post-profile-tagged.html`, `overlay-post.html`, `profile-about.html` (the
two bio fields), `contact-card-editor.html`, `contact-card-received.html`, `errors.html`.
`styles.css` likely needs a copy-box treatment. `CRIB.md` needs the new §14 constants and any
new verbatim strings — including the composer's blocklist refusal copy, which §16.3 requires to
state its fix.

**1.30 adds a surface that may not exist yet.** §10.4 was rewritten so that an answered contact
card **is a page**, resolved live. Check whether `mockups/pages/` has anything that plays that
role — `contact-card-received.html` may be the wrong shape rather than merely out of date.
§13.2's fourth report target means `report-profile.html` and `report-post.html` no longer cover
the report surfaces; a card report form is likely missing entirely.

**Two documents inside the track also drift.** `CRIB.md` is the register of constants and
verbatim strings that M2–M8 read instead of re-deriving, so a stale `CRIB.md` propagates a
stale string into every session that follows. And M1's "What to read" table gives **line ranges
labelled "correct as of project version 1.27"** — those line numbers have moved. The section
numbers are authoritative and mostly still valid, but §7.2.3 was rewritten and §7.2.4 is new,
so at least one row of that table is wrong in substance, not just in line number.

## 3. The question to settle before any other

**Where does this work happen, and how does SPEC 1.30 reach the mockups?** The mockup track
cannot re-run against 1.30 while sitting on a branch whose SPEC is 1.27. Options, with the
trade-off stated rather than a recommendation dressed as a fact:

1. **Merge `main` into `mockups`,** do the work there, merge back later. Keeps the track's
   history intact. The merge brings 13/14/15 and the updated 09; the M-file changes are
   additive on one side only, so the merge is *probably* clean — verify, do not assume.
2. **Merge `mockups` into `main`** and abandon the branch split. Simpler afterwards; a larger,
   noisier merge now, and it puts 67 generated-adjacent pages on the main line.
3. **Work on `archetypes`,** which already has both the mockups and the newer work — but it is
   missing `main`'s person-tagging commit and carries archetype material irrelevant to this.

Whatever is chosen, note that `mockups/site/` is generated output and is gitignored on the
branches that carry the track, but shows as untracked on `main` because `main` lacks those
`.gitignore` lines. Do not let it get committed.

## 4. The questions for the founder — ask these before writing the plan

**Q1. Which branch, per §3?**

**Q2. Re-run all eight M sessions, or patch only what 1.29 and 1.30 broke?** This is the
factor-of-four question. A full re-run is clean, reproducible and matches the track's design —
the M prompts, not the pages, are the source of truth. A targeted patch is far cheaper but
leaves the pages and the prompts describing slightly different things unless the prompts are
updated too. Give a recommendation with a cost estimate for each; do not choose for him.

**Q3. Do the M prompt files themselves get updated, or only `mockups/`?** M1's line-range table
is stale and at least one section it cites was rewritten. If the M prompts are not updated, a
future re-run reproduces 1.27 pages. If they are, that is eight files to edit before any
session runs.

**Q4. Does this work stay outside `TODO.md`'s queue?** `prompts/mockups/README.md` is explicit
that the track is *"deliberately outside"* the queue, with no version bump and no CHANGELOG
entry. A re-sync is arguably the same kind of work — but it is now a scheduled dependency of
the founder's review, which is an argument for it being tracked somewhere. Recommend one.

Also raise, without treating it as decided: **should prompt 09 run first?** 09 syncs
ARCHITECTURE and BUILD_PLAN to SPEC. Prompts 13 and 15 already updated both documents directly,
so the lag is now partial rather than total. The track's SPEC-led rule holds either way, but
whether the mockups should wait for 09 is a real sequencing question and the founder may have a
view.

## 5. Constraints — settled, do not reopen

- **The mockup track's two standing rules**, from `prompts/mockups/README.md`, hold for
  everything this session plans: *build only what the documents describe* — no invented
  features and no fixing contradictions noticed along the way, which go in `mockups/NOTES.md`
  instead — and *never edit* `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`,
  `TODO.md`, or anything in `prompts/` outside `prompts/mockups/`.
- **SPEC leads.** Where SPEC and ARCHITECTURE disagree about a user-facing surface, SPEC wins
  and the disagreement is recorded in `mockups/NOTES.md`.
- **`NOTES.md` is notes for the founder's review, not a to-do list.** Nothing in it gets fixed
  by this track.
- **Fidelity rules are unchanged**: static HTML, no scripts beyond `<details>`/`<summary>`,
  nothing fetched from anywhere, neutral greys, no invented brand palette, real semantic
  markup, and the accessibility checklist every M session ends with.
- **The simulated-content / build-commentary separation** established on the `mockups` branch
  stays in force; see `prompts/mockups/content-commentary-separation.md`.
- **The product philosophy is decided.** This session plans mockup work; it does not argue
  about the design.

## 6. Before you finish

- **Write the plan to a file** under `prompts/mockups/`, named so it reads as part of the
  track. It should name the branch, list the affected pages with the SPEC section that governs
  each, say which M sessions re-run and in what order, say what happens to `CRIB.md` and
  `NOTES.md`, and carry the cost estimate.
- **Give a concrete budget**, not a reassurance: what one M session costs, what the whole plan
  costs, and whether it is realistic on a Claude Pro plan in one sitting or wants splitting
  across days.
- **Do not update `TODO.md` or `CHANGELOG.md`** unless Q4 is answered in a way that requires
  it — and if it is, say exactly what you wrote where.
- **Summarise the plan in your reply** so the founder can react without opening the file, and
  list anything you marked unverified.
