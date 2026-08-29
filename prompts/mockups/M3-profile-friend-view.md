# Mockup session M3 — the profile, as a friend sees it

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** `mockups/pages/` (four profile tabs + two image-overlay states), `mockups/CRIB.md`, `mockups/NOTES.md`, `mockups/pages/index.html`. **No design document is edited.**
> **Depends on:** M1 (harness, crib sheet), M2 (the `_post` block is exercised there first).
> **Expected outcome:** the persistent header and four tabs of §9.1 exist as four separate URLs, and the click-to-expand overlay exists in both its variants.

---

You are working in the WeeBee design-document repository — a small, private, deliberately
anti-viral social network whose design documents exist but whose platform has not been built.
Read `README.md`, then `prompts/mockups/README.md`, `mockups/NOTES.md` and `mockups/CRIB.md`
(the crib sheet carries the constants, the sample cast and the verbatim interface strings).

This is session M3 of eight building **browser-viewable mockups of the design exactly as
`SPEC.md` and `ARCHITECTURE.md` already describe it.**

## Standing constraints

- **Build only what the documents describe.** No invented features, no fixes. Contradictions
  go in `mockups/NOTES.md`; build on regardless.
- **Never edit** `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md` or
  anything in `prompts/`. Write inside `mockups/` only.
- **SPEC leads** where ARCHITECTURE lags it (prompt 09 has not been run).
- **Neutral, layout-true fidelity**; the existing `styles.css`; no invented brand palette.
- **Static pages, no scripts**; show both states where both matter.
- **Nothing fetched from anywhere** (SPEC §15.2; ARCHITECTURE §3.5). Inline SVG placeholders
  for photographs.
- **Compose the M1 partials**; no page hand-rolls a form control, dialog or status message
  (ARCHITECTURE §3.8).
- **Separate simulated content from build commentary.** Every sentence on a page is either
  something WeeBee would actually say to a user who has never read a design document
  (simulated content — plain, warm, non-technical language) or a note to the founder about how
  the page was built (commentary — SPEC/ARCHITECTURE citations, invented-vs-established calls,
  cross-references to another mockup file, NOTES.md or CRIB.md). Never mix the two in one
  sentence or paragraph. Wrap every commentary block in `.commentary` (a distinct
  italic-monospace style in `styles.css`) so the shared header's build-commentary checkbox in
  `_base.html` can hide it. See `prompts/mockups/content-commentary-separation.md` for the full
  rule, worked examples, and the toggle mechanism.

## What to read

| Document | Sections | Lines (v1.27) |
|---|---|---|
| SPEC | §9.1 Structure: a persistent header and four tabs | 498–542 |
| SPEC | §9.1.1 Theming | 542–554 |
| SPEC | §9.2 Visibility tiers (the **Friends** row) | 554–564 |
| SPEC | §9.4 Limits, the two bio fields, the gallery, and the photo | 571–597 |
| SPEC | §9.7 Permanence | 614–632 |
| SPEC | §7.6 Pinning | 328–336 |
| SPEC | §7.7 The feed (the fold thresholds), §7.7.1 Paging | 336–352 |
| SPEC | §7.2.2 Images: size and display | 245–251 |
| SPEC | §11.5 Friend-list visibility | 713–718 |
| SPEC | §13.2 Reporting (**where the action lives** only) | 792–812 |
| SPEC | §16.3 — especially *"The profile page, concretely (v1.16)"* | 1027–1083 |
| SPEC | §4.5.1 Changing a display name | 95–102 |
| ARCHITECTURE | §3.5, §3.8 | 155–191 |

## What to build

All four tabs, as a **friend** of the owner sees them. Non-friend views are session M4 — do
not build them here.

### The structure every one of these four pages shares

§9.1 and §16.3 specify this precisely; follow it literally.

- **A persistent header above every tab**, carrying the owner's **profile photo**, their
  **display name**, and the **report action** — *"Nothing else."* It **scrolls with the page
  and is never sticky**, which §9.1 says would cost screen height on a phone and complicate the
  320 px reflow requirement.
- `<h1>` is the owner's display name, **once**, in that header — rendered so that §4.5.1's
  *"NewName (formerly OldName)"* is **real text inside it**. Show that state on at least one
  page.
- **Tabs are links to separate URLs**, server-rendered and **styled as tabs — never a scripted
  tab widget**. The tab strip is a `<nav>` with an accessible name, its links carrying
  `aria-current="page"`. Each tab is its own page with its own descriptive `<title>` —
  §16.3's own example is *"David Dudek — Posts"*.
- `<h2>` names the tab's content.
- **Individual posts carry no heading** — §16.3: *"a post has no title, and inventing one from
  its opening words would truncate content and fight the fold."* Each post is an `<article>`
  inside an `<ol>`, labelled *"Post by David, a few days ago"*.
- **Posts on the Blog and Pinned tabs do not repeat the author's name** (§9.1, §8.1) — every
  post there belongs to the owner, whose name is in the header above. **Comment authors are
  still named.**
- **Reactions never render on these tabs** (§8.2, v1.16). Only the single-post view of M2 has
  them. This is a rule about a layout decision, and it is easy to break by accident.
- The report action is a real `<button>` with visible text, **never an unlabelled icon**
  (§13.2, §16.4).

Tab order, with **Blog as the landing tab**: Blog · Pinned · Photos · About.

### 1. `pages/profile-blog.html` — the Blog tab

*"Every post by the owner that this viewer may see, newest first: profile posts, pinned posts
in their chronological place, and feed posts the viewer was in the audience of."* (§9.1)

- Folded at **`BLOG_FOLD_CHARS` = 2,000** — the wider threshold, because *"the reader
  deliberately visited this author's own space"* (§7.7). Distinct accessible names on the
  "read more" controls, as in M1.
- **A pinned post keeps its chronological place here** (§7.6), so the timeline is not full of
  holes.
- **A feed post appears here as well as in its recipients' feeds** (§9.1, v1.16). No audience
  widens: the posting-time snapshot and current friendship both still govern. Show one, and
  keep its §7.9 line — *"Visible to: the friends David sent this to."*
- Paging per §7.7.1 if the list runs long: **"Older posts →" and nothing cleverer**; no page
  numbers, no total. On a normal profile the list fits one page and **no navigation is
  rendered at all** — say in a page comment which case you are showing.

### 2. `pages/profile-pinned.html` — the Pinned tab

*"The owner's pinned posts — the author's curated shelf."* (§9.1)

- Folded at **`FEED_FOLD_CHARS` = 500**, not the Blog threshold: §7.6 — *"that tab is a shelf,
  not a reading surface."*
- **A pinned post displays its age** under the ordinary relative-time rule (§7.5.1). Only the
  *expiry countdown* is replaced by the **"pinned" marker**, never the age (§7.6, §7.5). Show
  a genuinely old one — §7.6 says the long tail of the ladder exists for this case.
- A pinned post **stays open for new comments**; its older comments are gone and **nothing
  marks that they ever existed** — no tombstone, no "this post had comments" (§7.6). Draw
  nothing there, deliberately.

### 3. `pages/profile-photos.html` — the Photos tab

- `GALLERY_MAX` = 8 images, **friends only** (§9.2, §9.4).
- The gallery is a **`<ul>` whose items are real `<button>`s in plain tab order** (§16.3) — *"at
  `GALLERY_MAX` = 8 a roving-tabindex grid adds script and failure modes for nothing."*
- **No caption field: the alternative text is the caption** (§9.4). Markup exactly as §9.4
  specifies it — the thumbnail is `<img alt="{text}">`; the overlay is
  `<figure><img alt=""><figcaption>{text}</figcaption></figure>`, **empty alt precisely
  because the caption is present and is the description**.
- **Order is author-arranged.** The reorder controls belong to session M6 (gallery
  management); do not build them here.

### 4. Two overlay states — `pages/overlay-gallery.html` and `pages/overlay-post.html`

The click-to-expand overlay of §7.2.2 is *"a proper modal dialog per §16.3: keyboard-openable,
focus-trapped, Escape-dismissable, focus restored on close"*, and it is **an in-app view, not a
raw file URL**. Two variants, because they differ:

- **From the gallery** — carries **next/previous image controls as real buttons**, *"so a
  keyboard user need not close and reopen it eight times"* (§16.3), and displays the
  alternative text as a **visible caption**.
- **From a post** — the same overlay without next/previous.

Static pages, so render the overlay open, and state in visible page text or a comment which
§16.3 obligations it stands for (focus in, trapped, Escape out, focus returned; zoom/pan
operable by keyboard).

### 5. `pages/profile-about.html` — the About tab

*"Short bio, extended bio (friends only), interest hashtags, and the people you both know."*
(§9.1)

- **The photo is not repeated inside About** — the header carries it (§9.1). Easy to get wrong.
- **Short bio** at `BIO_SHORT_MAX` = 200, which **never renders clickable links, not even
  allowlisted ones** (§9.4). **Extended bio** at `BIO_EXTENDED_MAX` = 2,000, friends only,
  where allowlisted links **are** permitted. Show one of each.
- **Profile hashtags**, up to `PROFILE_HASHTAG_MAX` = 10, clickable — clicking a hashtag opens
  the discover page filtered to that tag (§11.2). That page is M4; link to it anyway.
- **"The people you both know"** — *"only the friends they have in common with that person —
  rendered as names, never as a count"* (§11.5). Use §11.5's own idiom: *"knows Alice, Tom and
  others"*, **never "and 12 others"**.
- **Neither bio carries an "edited" marker or history** (§9.4). Nothing on the profile expires
  except posts and comments (§9.7).

## Before you finish

Check every page, as in M1 and M2:

- one `<h1>` per page — and on these four it must be the **owner's display name in the
  header**, not the tab name; a unique descriptive `<title>` per tab
- the tab strip is a `<nav>` with an accessible name and `aria-current="page"` on the current
  tab
- skip link first focusable; `lang` set; landmarks present
- every `<img>` has an `alt` — and the overlay's `<img>` has an **empty** one, with the text in
  `<figcaption>`
- no `tabindex` above 0; no `title` attribute; no timestamp in any markup attribute
- reflow at **320 px** with no horizontal page scroll — check the tab strip especially, since
  four tabs at 320 px is where it will break
- **no reaction line and no react control anywhere on these four pages** (§8.2)

Then: add this session's strings to `CRIB.md`, add its pages to `pages/index.html`, update
`NOTES.md`, and **print the contents of NOTES.md**. Do not touch `TODO.md` or `CHANGELOG.md`.
