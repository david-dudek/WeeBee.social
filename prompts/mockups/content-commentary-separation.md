# Mockup fix — separating simulated content from build commentary

Not one of the numbered M1–M8 sessions — a cross-cutting retrofit, written after M5, that
applies to everything already built and amends M1–M8's own prompt text so future sessions
produce compliant pages from the start.

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** `prompts/mockups/README.md`, `prompts/mockups/M1.md` through `M8.md` (the
> standing-constraints bullets only), `mockups/partials/_base.html`, `mockups/styles.css`,
> `mockups/CRIB.md`, `mockups/NOTES.md`, and every already-built page in `mockups/pages/` (M1–M5's
> output). **No SPEC/ARCHITECTURE/BUILD_PLAN/CHANGELOG/TODO document is edited.**
> **Depends on:** M1–M5 already built. **Expected outcome:** every existing mockup page cleanly
> separates simulated product copy from build commentary, with commentary in a distinct visual
> style and a per-page, no-script toggle to hide it.

---

You are retrofitting the WeeBee browser-mockup track (`mockups/`). Read `README.md`,
`prompts/mockups/README.md`, `mockups/NOTES.md`, and `mockups/CRIB.md` first.

## Why this is needed

Every page so far mixes two audiences in one stream of text: copy a real WeeBee user would see,
and commentary explaining a build decision to the founder (SPEC citations, "this is invented,"
cross-references to other pages). The `.session-note` class was meant to mark the second kind,
but it was applied inconsistently — a lot of commentary is sitting in plain paragraphs with no
visual distinction at all, including SPEC section numbers and phrases like "§5.3, verbatim:"
inside what's meant to be product copy.

## The fix has three parts: a rule, a style, and a toggle

### 1. The rule — the grandma test

For every sentence on every page, decide: *would WeeBee actually say this to a user who has never
read a design document?* If not, it's commentary, full stop — no exceptions for "just a little
context." Concretely, commentary includes:
- Any SPEC/ARCHITECTURE section reference (`§5.2`, `§9.1`, etc.)
- Any named constant in its code form (`FRIEND_CAP`, `CONTACT_ITEMS_MAX`) — the human-readable
  fact it encodes ("up to 12 items," "a 300-friend limit") can stay in real copy; the shouty
  constant name cannot
- Anything explaining *why* a page was built a certain way, what's invented vs. established, or
  referencing another mockup file, NOTES.md, or CRIB.md
- Anything using words like "verbatim," "this session," "this track," "worked example,"
  "placeholder"

Everything else — headings, body copy, button labels, form labels, hint text, error messages, the
actual quoted SPEC user-facing strings (e.g. the unfriend confirmation's *"They'll no longer see
your posts..."* — that one **is** real product copy, SPEC just happens to mandate its exact
wording) — is simulated content and must read in plain, warm, non-technical language.

**Worked example of the fix, from `unfriend-confirm.html`:**
- Before: *"Unfriending is not invisibility. Sofia doesn't vanish; she falls to whatever tier she
  still qualifies for. §5.3, verbatim:"* followed by the blockquote.
- After: the blockquote's own text already says everything a real user needs ("They'll no longer
  see your posts... If you have friends in common, they can still see...") — drop the redundant
  lead-in sentence from simulated copy entirely, or fold its non-jargon half into plain framing
  ("Here's what happens:"), and move "§5.3, verbatim" into a commentary note explaining that the
  quoted text below is SPEC's own mandated wording.

Do this same audit on **every paragraph of every already-built page** — not just ones already
wrapped in `.session-note`.

### 2. The style — commentary must be unmistakable

Give commentary a distinct, consistent treatment: **italic monospace**
(`font-family: var(--font-mono); font-style: italic;`), in the existing muted secondary color, at
the existing smaller size. This is a bigger visual break than the current grey-and-small
treatment alone — it should read unmistakably as "build notes," never mistakable for product
copy, even skimming. Decide whether to keep the class name `.session-note` or rename it to
something clearer (e.g. `.commentary`) — if renamed, update every page that uses it. Verify the
new treatment stays legible against the page background (it doesn't need to clear the platform's
own WCAG AA bar, since it isn't part of the simulated product, but it must be readable).

### 3. The toggle — CSS-only, no scripts

The track's standing rule is static pages, no scripts — so this has to be a checkbox-driven CSS
toggle (the well-known "checkbox hack"), not JavaScript. Add one real, visibly labelled
`<input type="checkbox">` (e.g. "Show build commentary and SPEC citations") to the shared header
in `partials/_base.html`, structured so a CSS sibling selector can hide every commentary block on
the page when it's unchecked. Requirements:
- Real native checkbox, not a div — keyboard-operable, visible focus ring, same as every other
  control in this track.
- Default state is your call, but default to **visible** (matches current behavior; hiding is the
  deliberate action).
- Note plainly in NOTES.md that this toggle can't persist across page loads without scripts or
  cookies, neither of which this track uses — each page resets to the default. This is an
  accepted limitation, not a bug to chase.
- One shared implementation in `_base.html` + `styles.css` — not hand-rolled per page.

## Scope of the retrofit

1. **`prompts/mockups/README.md`** — add this as a third standing rule alongside "build only what's
   described" and "never edit the design documents," so every future session inherits it
   automatically.
2. **`prompts/mockups/M1.md` through `M8.md`** — each repeats the standing constraints verbatim in
   its own "Standing constraints" section; add the same new bullet to each, so a session pasted in
   isolation (without separately reading README.md) still sees the rule. M6–M8 haven't been run
   yet, so this is the only change they need — they'll produce compliant pages from the start once
   run.
3. **`mockups/partials/_base.html`** — add the toggle control.
4. **`mockups/styles.css`** — add the commentary styling and the toggle CSS.
5. **`mockups/pages/*.html`** (everything M1–M5 built, ~26 pages) — full audit per the grandma test
   above: reclassify every sentence, rewrite any simulated copy that leaked jargon, wrap every
   genuine commentary block in the new class.
6. **`mockups/CRIB.md`** — register the new class name and the toggle mechanism as a shared
   convention so M6–M8 don't reinvent it.
7. **`mockups/NOTES.md`** — log this as a track-wide convention change: what triggered it, what
   changed, and the toggle's no-persistence limitation.

## Before you finish

- Rebuild (`python3 mockups/build.py`) and spot-check a page from each earlier session (at least
  one from M1–M5) with the toggle both on and off.
- Confirm the toggle is operable by keyboard alone and its label is real, visible text.
- Confirm that with commentary hidden, **no page shows a SPEC section number, a shouted constant
  name, or any phrase like "this session" or "verbatim"** anywhere in the remaining visible text.
- Re-run the standing accessibility checklist (single `<h1>`, unique titles, 320px reflow, no
  `title` attributes, labelled inputs) on every page you touched, since this retrofit rewrites a
  lot of copy.
- Update `CRIB.md` and `NOTES.md`, and print the new NOTES.md entry.
