# Prompt 16 — What "and nothing else" bounds on the card page

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** SPEC.md §10.4 — one clarifying addition. No other section.
> **Depends on:** prompt 01. Also depends on **15 (done)**, which wrote the "and nothing
> else" sentence this prompt clarifies. Best run **before prompt 09**, since 09 treats SPEC
> as settled going in — but harmless if 09 has already run, since §10.4 is not a section 09
> touches.
> **Expected outcome:** §10.4's "and nothing else" is worded so a builder can tell whether
> the card page's request-more-access control (§10.5) belongs there, without independently
> re-deriving the question or importing a mockup-track recommendation.

---

You are working in the WeeBee design-document repository. Read `README.md`, then `SPEC.md`
§10.1 through §10.5 in full — it is 55 lines — and §13.2's card-report paragraph (search
"Reporting a contact card"). This is a **founder-directed design session**; you may edit
SPEC.md. Nothing else needs to change for this.

## The finding, quoted

`mockups/NOTES.md` entry 51, written during the mockup re-sync's R1 session, raises this and
deliberately does not resolve it:

> "§10.4 closes the card page with 'and nothing else' — and §10.5's section is sitting on
> it. ... The question, which this session does not answer: does a v1.1 feature belong on a
> page whose own section closes with 'and nothing else'? Both readings hold up..."

`prompts/mockups/resync-3-card-cluster.md` §6a (drafted, not yet run) carries a
recommendation rather than a decision: build the request-more-access section in, keep
§10.5's "may ship in v1.1" hedge visible, and record in `NOTES.md` that "the reading was
chosen on a recommendation rather than derived from the document, and never settled by the
founder." That file explicitly defers to whatever gets decided first: "if it is answered
before this session runs, that answer wins over what follows."

This session exists to turn that recommendation into an actual document decision, so R3 —
and anything that reads §10.4 after it — doesn't have to carry the hedge forward.

## What's actually in the document

§10.4 (v1.30), the sentence in question:

> "It carries the owner's display name, rendered live through the shared helper (§4.5.1),
> the items the viewer may see, and nothing else."

The three arguments immediately beneath it — live resolution defeats a stored answer, a
stored answer would be a message, a card has no clock — are all about *not storing or
delivering a reply*. None of them are about the page's controls.

Two pieces of evidence that the closing phrase was never meant to reach controls:

1. §10.4's own next paragraph puts a **report control** (§13.2) on this exact page — a
   third thing that is neither the owner's name nor a shared item. Nobody reads that as a
   violation of "nothing else," which means the phrase is already applied, in practice, as
   a bound on *disclosed data*, not on *every element the page renders*.
2. §10.4 says of §10.5 that its flags "have always assumed this page without saying so" —
   offered as a *confirmation* of the page-based redesign, not a conflict flagged for later.
   If exclusion had been intended, this is the sentence that would have said so.

## The recommendation

Add one clarifying sentence to §10.4, right after the paragraph that mentions §10.5 (the
"have always assumed this page" paragraph). Close to:

> "'And nothing else' bounds what the page discloses — the owner's name and the items
> resolved for this viewer — not the page's controls. The §13.2 report action and §10.5's
> request-more-access flag are both controls rather than disclosed data or a reply, and
> neither is excluded by this sentence."

Match SPEC's voice; the content is what matters. A reader of §10.4 alone should be able to
tell the request-more-access flag belongs on this page without cross-referencing
`NOTES.md` or a mockup-track prompt.

**Push back if this is wrong.** If a closer read of §10.1's message ban, or of §13.1,
points the other way, say so and write the opposite clarification instead — the goal is a
settled reading, not this particular one.

## Constraints

- **This is a wording clarification, not a reopening of §10.4 or §10.5.** Do not touch the
  live-resolution decision, the three arguments beneath it, the report action, or §10.5's
  v1.1 deferral — all settled by prompt 15.
- **Don't decide whether §10.5 ships in v1.0.** That is a separate roadmap question. This
  session only settles whether the *page* may carry the control when the time comes.
- **One section changes.** If this pulls at ARCHITECTURE.md or BUILD_PLAN.md, stop —
  nothing about this is new behavior, only a reading of an existing sentence, and 09 is
  where cross-document sync happens.

## Before you finish

- CHANGELOG.md entry. This is a real SPEC change, so it takes the next project version
  (1.31), with the other four files recorded as unchanged.
- `TODO.md`: update this prompt's row to `done`, landed in 1.31.
- Say in the entry (or in prose — neither file is part of the versioned record) that this
  resolves `mockups/NOTES.md` entry 51 and lets `prompts/mockups/resync-3-card-cluster.md`
  §6a be read as a settled decision rather than a recommendation. No edit to either mockup
  file is required by this session — the mockup track's own rule keeps SPEC changes out of
  its scope, and it picks this up next time it runs.
