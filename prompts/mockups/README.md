# prompts/mockups/ — the browser mockup track

A **separate, unnumbered track**, deliberately outside `../../TODO.md`'s queue.

The numbered prompts in `../` are design conversations: they edit the law files, land in a
version bump, and get a CHANGELOG entry. This track does none of that. It builds
browser-viewable mockups of the design **exactly as SPEC.md and ARCHITECTURE.md already
describe it**, so the founder can look at the platform before approving the documents.
It produces no version bump, no CHANGELOG entry, and no row in the queue.

**Started against project version 1.27.** Prompt `../09-sync-arch-and-buildplan.md` had not
been run when this track was written, so ARCHITECTURE.md and BUILD_PLAN.md are known to lag
SPEC.md (see `../../TODO.md`, row 09 and Appendix A). These mockups are therefore **SPEC-led**:
where the two documents disagree about a user-facing surface, SPEC wins, and the disagreement
goes in `mockups/NOTES.md`.

## The sessions

Run in order. Each is self-contained — paste the file from the `---` divider down into a
fresh session in this repository.

| # | File | Builds |
|---|---|---|
| M1 | [M1-scaffold-and-feed.md](M1-scaffold-and-feed.md) | The harness (build script, base partials, CSS, crib sheet, index) + the feed |
| M2 | [M2-composer-and-post-views.md](M2-composer-and-post-views.md) | The composer + three single-post views |
| M3 | [M3-profile-friend-view.md](M3-profile-friend-view.md) | The four profile tabs as a friend sees them + the image overlay |
| M4 | [M4-visibility-set.md](M4-visibility-set.md) | Non-friend profile views, discover, friends page, preview-as |
| M5 | [M5-friendship-and-contact-flows.md](M5-friendship-and-contact-flows.md) | Friend requests, introductions, contact cards, unfriend/block |
| M6 | [M6-authoring-and-forms.md](M6-authoring-and-forms.md) | Post editor, gallery management, report and operator forms, settings, groups |
| M7 | [M7-account-edges.md](M7-account-edges.md) | Login, reset, invite redemption, banned, deactivated, errors, maintenance |
| M8 | [M8-emails.md](M8-emails.md) | Every email SPEC §16.1 puts in scope, HTML + plain-text |

M7 and M8 may be merged into one session if the pattern is well established by M6.

## The three rules that hold across all eight

1. **Build only what the documents describe.** No invented features, no fixes for problems
   noticed along the way. Where a surface needs something neither document specifies, render
   the simplest thing that satisfies the surrounding rules and **record it in
   `mockups/NOTES.md`** — do not resolve the gap and do not edit the design documents.
2. **Never edit `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md`, or
   anything in `prompts/`.** This track writes inside `mockups/` and nowhere else.
3. **Separate simulated content from build commentary.** Every sentence on a page is either
   something WeeBee would actually say to a user who has never read a design document
   (simulated content — plain, warm, non-technical language) or a note to the founder about how
   the page was built (commentary — SPEC/ARCHITECTURE citations, invented-vs-established calls,
   cross-references to another mockup file, NOTES.md or CRIB.md). Never mix the two in one
   sentence or paragraph. Wrap every commentary block in `.commentary` (a distinct
   italic-monospace style in `styles.css`) so the shared header's build-commentary checkbox in
   `_base.html` can hide it. See
   [content-commentary-separation.md](content-commentary-separation.md) for the full rule,
   worked examples, and the toggle mechanism.

## Where the gaps go

`mockups/NOTES.md` is the running log of every place the documents were silent and something
had to be drawn anyway. It is the by-product most worth reading after the mockups themselves,
and it is **notes for the founder's review, not a to-do list** — nothing in it gets fixed by
this track.
