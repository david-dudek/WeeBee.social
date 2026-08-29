# Mockup session M2 — the composer, and the single-post views

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** `mockups/pages/` (composer + three post views), `mockups/CRIB.md`, `mockups/NOTES.md`, `mockups/pages/index.html`. **No design document is edited.**
> **Depends on:** M1 (the harness, the stylesheet and the crib sheet must exist).
> **Expected outcome:** the one composer of §7.1 and the only surface reactions ever render on both exist in the browser, with every state SPEC gives them.

---

You are working in the WeeBee design-document repository — a small, private, deliberately
anti-viral social network whose design documents exist but whose platform has not been built.
Read `README.md`, then `prompts/mockups/README.md` and `mockups/NOTES.md`, then
`mockups/CRIB.md` (written in session M1: it carries the constants, the sample cast and the
verbatim interface strings, so you do not re-derive them).

This is session M2 of eight building **browser-viewable mockups of the design exactly as
`SPEC.md` and `ARCHITECTURE.md` already describe it.**

## Standing constraints

- **Build only what the documents describe.** No invented features, no fixes for problems you
  notice. Contradictions go in `mockups/NOTES.md`; you build on regardless.
- **Never edit** `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md` or
  anything in `prompts/`. Write inside `mockups/` only. No CHANGELOG entry, no version bump.
- **SPEC leads** where ARCHITECTURE lags it (prompt 09 has not been run).
- **Neutral, layout-true fidelity.** Real semantic HTML, the existing `styles.css`, no invented
  brand palette, no logo.
- **Static pages, no scripts** — show a state rather than implement behaviour, and show both
  states where both matter. `<details>`/`<summary>` is the exception: SPEC §8.2.2 names it as
  the actual mechanism.
- **Nothing fetched from anywhere** (SPEC §15.2; ARCHITECTURE §3.5).
- **Compose the M1 partials** (`_base`, `_nav`, `_post`, `_field`, `_errors`, `_status`). Per
  ARCHITECTURE §3.8, no page hand-rolls a form control, dialog or status message.
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

Do not read SPEC.md whole. Line ranges are correct as of v1.27; the section number is
authoritative if the file has moved.

| Document | Sections | Lines (v1.27) |
|---|---|---|
| SPEC | §7.1 The two post types (the composer rules) | 212–228 |
| SPEC | §7.2 Content rules, §7.2.1 Text formatting, §7.2.3 URL allowlist | 228–271 |
| SPEC | §7.3 Audience selection | 271–275 |
| SPEC | §7.9 Stated visibility | 378–411 |
| SPEC | §8.1 Comments | 413–427 |
| SPEC | §8.2, §8.2.1, §8.2.2, §8.2.3 Reactions | 427–496 |
| SPEC | §11.2 Hashtags, §11.2.1 The vocabulary, §11.3 Hashtag-gated FoF visibility | 666–706 |
| SPEC | §6 Groups (the audience-save suggestion only) | 201–210 |
| SPEC | §16.3, §16.4 | 1027–1089 |
| ARCHITECTURE | §3.5, §3.8 | 155–191 |

## What to build

### 1. `pages/composer.html` — the one composer

SPEC §7.1: *"There is a single composer, reached from the main navigation."* One page, showing
the composer with both destination branches visible (side by side, or as two pages —
`composer-feed.html` / `composer-blog.html` — if one page becomes unreadable).

- **Destination is a required choice with no default, in real text**, both strings verbatim
  from §7.1: *"Send to a few friends — appears in their feed"* and *"Post to my blog — all your
  friends can find it."*
- **A missing choice produces an honest text error naming the fix, never a silently disabled
  button** (§7.1, §16.3 3.3.1/3.3.3). Show that error state.
- **Feed branch: the audience picker** (§7.3) with its live count against
  `POST_AUDIENCE_MAX` = 30, announced in a **polite live region** (§16.3, 4.1.3) — and note
  ARCHITECTURE §3.8's rule that the count is *also* rendered server-side so it is never
  JS-only. Exceeding 30 produces a clear warning requiring narrowing; **recipients are never
  silently dropped** (§7.3).
- **Blog branch: the hashtag picker** (§11.2 — a searchable picker over the curated
  vocabulary; hashtags are **never free-typed**) with §7.9's audience line beneath it.
- **The visibility line updates live** in the composer through a polite live region (§7.9). It
  is derived from the post's own type and tags, **never from the viewer**; every tag is named
  and the word is *"any of"*; **never a number**.
- **The preformatted toggle** (§7.2.1) with its **explainer linked directly from the
  composer**, stating what the mode is for and its shortcomings: exact spacing, no wrapping,
  horizontal scrolling on narrow screens.
- **Image upload with the alt-text prompt**: §16.3 requires a **deliberate choice every
  time** — write a description (up to `ALT_TEXT_MAX` = 1,000) **or** tick "this image is
  decorative". Never silently skipped, never auto-filled.
- **Character count on cap overrun** — honest, and text is never silently truncated (§7.2.1).
- **A rejected URL**, with §7.2.3's message: that the link is not permitted here, briefly what
  the allowlist is for, and that anything else can be shared through the contact card.
- **The type-switch notices as text, not modal interruptions** (§7.1): switching to a blog post
  clears any picked audience; switching to a feed post states that hashtags stop gating
  visibility and become decorative.
- **"Save this selection as a group?"** (§6) — memory of the user's explicit choices, offered,
  never automatic.

### 2. `pages/post-feed.html` — a feed post, single-post view

This is the **only surface reactions ever render on** (§8.2, v1.16 rule: never on the Blog tab,
the Pinned tab, or the feed).

- The post, with its §7.9 visibility line: *"Visible to: the friends David sent this to."*
- **The reaction line**, per §8.2.2: directly **beneath the content and above that content's
  comments**; a **real list in the markup** with an accessible name — *"Reactions to your
  post"* — whose items read *"Alice: Love it!"*; **complete, never truncated, never folded,
  never summarised**; and **when nothing has been given, nothing is rendered** — no empty
  state. Show a comment carrying its own reaction line too (accessible name *"Reactions to
  your comment"*).
- **The react control** as a native `<details>`/`<summary>` disclosure. Its **own text says
  whether this viewer has already reacted and with what** — *"React"* or *"Reacted: Love it!"*
  — in real text, never a colour. Inside: one real `<button>` per `REACTION_SET` phrase in
  curated order, plus **"Remove reaction"** where one is set, the current phrase marked in
  text. **Distinct accessible names** per §16.3 — *"React to David's post"*, *"React to
  Alice's comment"*, and per phrase *"Love it! — react to Alice's comment"*. At 320 px the
  phrase buttons **wrap onto as many rows as they need**; nothing scrolls sideways.
- **No react control on your own post or your own comment** (§8.2).
- **Comments: flat, one linear list, no nested replies** (§8.1). Each carries its author's
  display name and its age. **Long comments fold at `COMMENT_FOLD_CHARS` = 300**, with a
  distinct accessible name — §8.1's own example is *"Read more of Alice's comment"*.
- **The comment box repeats the visibility line**: *"Your comment will be visible to the same
  people."* (§7.9)

**Use §8.2's placeholder phrase set as written** — "Agreed!", "Love it!", "So proud!",
"Thinking of you", "Congrats!", "Ha!" — and **record in NOTES.md** that §8.2.3 recommends
retiring "Ha!" in favour of "Thank you!" and that this recommendation has not been adopted in
the document. Do not adopt it here.

### 3. `pages/post-profile-tagged.html` — a hashtag-gated profile post

The same view for a tagged profile post, seen by a friend-of-friend who matched on a tag
(§11.3). What differs, and why this page exists:

- The visibility line, verbatim from §7.9: *"Visible to: all of David's friends, and
  friends-of-friends with **any of** #hiking, #jazz."*
- **The report action sits with the visibility line** on a tagged profile post (§7.9, v1.21),
  carrying a reason for exactly this case — *"the tags don't match this post"*.
- **At least one commenter name rendered as plain text rather than a link** (§8.1). This is
  the only situation in which that arises: two viewers of a hashtag-gated post may be
  strangers to each other, and the name links only where the viewer has at least basic-tier
  access to that commenter.
- A reaction from someone the viewer has no connection to likewise renders as plain text
  (§8.2.2).

### 4. `pages/post-preformatted.html` — the reflow exemption

A preformatted post (§7.2.1), on a single-post view. This is **the platform's one documented
exception** to the reflow requirement, and the obligations that come with it are the point of
the page:

- Monospace, runs of spaces preserved **exactly**, long lines **never soft-wrap**; the post
  scrolls horizontally instead.
- The scrolling region is **keyboard-scrollable, focusable and named** — ARCHITECTURE §3.8:
  `tabindex="0"`, an accessible name, and a visible focus ring, *"because a horizontally
  scrollable region that only a mouse can pan fails 2.1.1."*
- **The horizontal scroll is confined to the post's own container and must never cause the
  page itself to scroll sideways** (§16.3, v1.16). Verify this at 320 px — it is the single
  most important check on this page.
- Monospace here is **structural, not theming** (§9.1.1): it survives every theme, including
  the viewer override. Only the monospace-ness is exempt.

## Before you finish

Check every page you built, exactly as M1 did — this is ARCHITECTURE §9's template smoke tests
applied by hand:

- one `<h1>` and a unique descriptive `<title>`; skip link first focusable; `lang` set
- landmarks present; every `<img>` has an `alt`; every input has an associated **visible
  label** (placeholders are never labels)
- no `tabindex` above 0 **except** the preformatted scroll container, which §16.3 requires
- no `title` attribute anywhere; no timestamp in any markup attribute (§7.5.1)
- reflow at **320 px** with no horizontal page scroll — the preformatted post's own container
  is the only thing allowed to scroll sideways

Then: add this session's verbatim strings to `CRIB.md`, add its pages to `pages/index.html`,
update `NOTES.md`, and **print the contents of NOTES.md**. Do not touch `TODO.md` or
`CHANGELOG.md`.
