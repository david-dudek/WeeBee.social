# Mockup session M1 — the harness, and the feed

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** creates `mockups/` (build script, partials, stylesheet, crib sheet, notes, index, feed). **No design document is edited.**
> **Depends on:** nothing. This is the first session of the track.
> **Expected outcome:** `mockups/site/index.html` opens in a browser and the feed page renders every state SPEC gives it.

---

You are working in the WeeBee design-document repository. WeeBee is a small, private,
deliberately anti-viral social network; the repository holds its complete design documents and
the platform has not been built yet. Read `README.md` first for the shape of the project.

This session is the first of eight that build **browser-viewable mockups of the design exactly
as `SPEC.md` and `ARCHITECTURE.md` already describe it**. The founder has not yet reviewed and
approved those documents; the mockups exist so he can look at the platform before he does.
Read `prompts/mockups/README.md` for how the track is organised.

## Standing constraints — these hold in every session of this track

- **Build only what the documents describe.** No invented features. No fixes for problems you
  notice along the way. If you spot a contradiction, **record it in `mockups/NOTES.md` and
  build on regardless** — resolving it is the founder's review, not this task.
- **Never edit** `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md`, or
  anything in `prompts/`. This track writes inside `mockups/` and nowhere else. It gets no
  CHANGELOG entry and no version bump (`TODO.md` "How to use this file", rule 5).
- **SPEC leads.** Prompt `prompts/09-sync-arch-and-buildplan.md` has not been run, so
  ARCHITECTURE.md lags SPEC.md. Where they disagree about a user-facing surface, follow SPEC
  and note the disagreement.
- **Fidelity: neutral and layout-true.** Real semantic HTML, one hand-written stylesheet,
  system font stack, neutral greys. **No invented brand palette, no logo, no illustration** —
  WeeBee has no documented visual style (`THEME_SET` is operator-curated and has no members
  named anywhere), so anything beyond neutral would be inventing a design decision the founder
  has not made.
- **Static pages, no scripts.** A mockup shows a *state*; it does not implement behaviour.
  Where both states of a control matter, show both — side by side, or as two pages. The one
  exception is `<details>`/`<summary>`, which SPEC §8.2.2 names as the actual mechanism and
  which needs no script.
- **Nothing is fetched from anywhere.** No CDN, no web fonts, no remote images (SPEC §15.2;
  ARCHITECTURE §3.5: *"nothing loaded from a CDN, ever"*). Use inline SVG placeholders for
  photographs.
- **Use SPEC's own words wherever it supplies them.** Where SPEC quotes an interface string,
  that exact string goes on the page. `mockups/CRIB.md` is the register of them.

## What to read

Do **not** read SPEC.md whole — it is 223 KB. Read these sections. Line ranges are a hint for
locating them quickly and are correct as of project version 1.27; **the section number is
authoritative** if the file has moved since.

| Document | Sections | Lines (v1.27) |
|---|---|---|
| SPEC | §7.5 Expiry, §7.5.1 Displayed time | 278–328 |
| SPEC | §7.7 The feed, §7.7.1 Paging long lists | 336–352 |
| SPEC | §7.8 Editing (the "edited" marker only) | 352–378 |
| SPEC | §7.9 Stated visibility | 378–411 |
| SPEC | §7.2.2 Images: size and display | 245–251 |
| SPEC | §12.1, §12.2, §12.3 Notifications | 732–777 |
| SPEC | §4.5.1 Changing a display name | 95–102 |
| SPEC | §16.3 Requirements by area, §16.4 Banned measures | 1027–1089 |
| SPEC | §14 Configuration Constants | 898–956 |
| ARCHITECTURE | §3.5 Frontend, §3.8 Accessibility | 155–191 |
| ARCHITECTURE | §9 Testing (the template smoke tests) | 659–689 |

## What to build

### 1. The harness

```
mockups/
  build.py          stdlib only, no dependencies. Expands {{include partials/_x.html}}
                    and simple {{var}} substitution. Roughly 60 lines. No watch mode,
                    no live reload, no package manager.
  partials/
    _base.html      landmarks (banner / navigation / main / contentinfo), skip link as
                    the first focusable element, lang, per-page <title>, focus-visible
                    styling that no theme may remove  (ARCHITECTURE §3.8)
    _nav.html       the main navigation
    _post.html      the most-repeated block: age, visibility line, fold, countdown or
                    pinned marker, edited marker
    _field.html _errors.html _status.html
                    named in ARCHITECTURE §3.8 as the accessibility unit — a form field
                    with its label association, an error summary with aria-describedby
                    wiring, a polite live region. Pages compose these; no page
                    hand-rolls a form control or a status message.
  styles.css        one file, mobile-first, neutral greys at >=4.5:1 body text and
                    >=3:1 for UI boundaries and focus rings (SPEC §16.3), 44x44 CSS px
                    touch targets, reflows at 320 px
  CRIB.md           see below
  NOTES.md          see below
  pages/*.html      body content only; build.py wraps them
  site/             generated output, opened via file://
  README.md         one paragraph: what this folder is, how to rebuild it
```

`mockups/site/` is generated — add it to `.gitignore` if the repo's existing `.gitignore`
does not already cover it.

**`_nav.html` needs a warning in NOTES.md.** SPEC names the main navigation exactly once —
§7.1: the composer is *"reached from the main navigation"* — and never says what else is in
it. Whatever you draw propagates through roughly forty mockups. Draw the minimum the other
sections imply, and record plainly that its contents are not specified.

### 2. `CRIB.md` — the register every later session reads

The point is that sessions M2–M8 do not re-derive these. Include at minimum:

- Every constant from **SPEC §14** that appears on a page: `FEED_FOLD_CHARS` 500,
  `BLOG_FOLD_CHARS` 2,000, `COMMENT_FOLD_CHARS` 300, `POSTS_PER_PAGE_DEFAULT` 20,
  `POSTS_PER_PAGE_OPTIONS` 20/40/60, `EXPIRY_COUNTDOWN_DAYS` 14, `CONTENT_TTL_DAYS` 90,
  `FRIEND_CAP` 300, `POST_AUDIENCE_MAX` 30, `GALLERY_MAX` 8, `PIN_LIMIT` 10,
  `PROFILE_HASHTAG_MAX` 10, `CONTACT_ITEMS_MAX` 12, `BIO_SHORT_MAX` 200,
  `BIO_EXTENDED_MAX` 2,000, `POST_LENGTH_MAX` 10,000, `COMMENT_LENGTH_MAX` 2,000.
- **The verbatim interface strings SPEC supplies**, each with its section number. Start with
  §7.9's three visibility lines and its comment-box line, §9.1's "not friends" line, §7.1's
  two destination strings, §5.3's unfriend confirmation, §11.6's "Filter your friends",
  §4.6.1's never-a-link promise, §12.2's notification wordings. Later sessions add to it.
- **The sample cast, taken from SPEC's own examples** so nothing is invented: David (the
  account whose view we are mocking up), Alice, Tom, Mom — from §8.2's
  *"Alice: Love it! · Mom: So proud!"*, §11.5's *"knows Alice, Tom and others"*, §12.2's
  *"Alice and Tom commented on your post"*, §16.3's page title *"David Dudek — Posts"*.
  Add a fourth and fifth name only where a page needs one, and say in CRIB.md that you did.
- **The relative-age phrases in use**, quoted from §7.5.1's ladder. Mockups are static, so
  these are literal strings — the ladder's 39 rows do not need implementing.

### 3. `NOTES.md` — the running gap log

One entry per place the documents were silent and something had to be drawn anyway: what the
surface needed, what the documents say, what you drew, and the section you looked in. This
file is **notes for the founder's review, not a to-do list.** Nothing in it gets fixed here.
Two entries are already known and should be written in this session: the unspecified
navigation above, and the fact that ARCHITECTURE lags SPEC pending prompt 09.

### 4. `pages/index.html`

Lists every mockup with a one-line description and its governing SPEC section, grouped by the
eight sessions. Each session appends its own pages. This doubles as the founder's review
index, so the citation matters as much as the link.

### 5. `pages/feed.html` — the feed

SPEC §7.7: *"in strict reverse-chronological order: feed posts they are in the audience of,
profile-update notifications from friends, and system notifications"*, and *"The feed is a
mailbox, not a machine."* Render these states, all on one page:

- **Feed posts and notification rows interleaved** in one reverse-chronological list (§7.7).
  How the two are visually distinguished is **not specified** — draw the plainest thing and
  note it.
- **One post folded at `FEED_FOLD_CHARS` = 500**, cut at a whitespace boundary, with a
  "read more" control that is a real `<button>` carrying `aria-expanded` and a **distinct
  accessible name** via visually hidden text — §16.3's own example is *"Read more of David's
  post from a few days ago"*. Show an expanded post too, so both states are visible.
- **Every post carries its stated-visibility line**, verbatim from §7.9's table.
- **Relative ages** as literal strings from §7.5.1's ladder. **No `title` attribute, no
  `<time datetime>`, no data attribute carrying a timestamp** — §7.5.1 puts the exact time
  deliberately outside the interface *and* the markup, and ARCHITECTURE §3.8 restates the ban.
- **One post inside `EXPIRY_COUNTDOWN_DAYS` = 14** showing the countdown in **absolute days**
  — §7.5's own example is *"deletes in 6 days"*. This is the one place absolute time appears
  on a social surface, and §7.5.1 explains why it is not an inconsistency.
- **One post carrying the "edited" marker** with the relative time of the edit, as real text
  beside its age; no version history, no diff (§7.8).
- **One post with an image**, proportionally scaled — never cropped, never stretched — within
  a bounded height so one tall portrait cannot dominate the screen (§7.2.2).
- **Notification rows in §12.2's idiom**: names, never numbers. Use its own wordings —
  *"David posted to his blog"*, *"David changed his profile photo"*, *"David added 3 photos to
  his gallery"*, *"Alice and Tom commented on your post"*. Include a coalesced one
  (§12.3: *"David posted twice to his blog"*, linking to the blog rather than either post).
  **No unread-count badge anywhere on the page** (§12.2, §17).
- **One name rendered as "NewName (formerly OldName)"** — real text, not decoration (§4.5.1).
- **At the foot: "Older posts →" and nothing else.** No page numbers, no total, no infinite
  scroll, no "load more" (§7.7.1). Include "← Newer posts" as a comment or a second page so
  the pairing is visible.

## Before you finish

Run `build.py`, open `site/index.html`, and check every page you built:

- one `<h1>` and a unique descriptive `<title>` per page (§16.3, WCAG 2.4.2)
- the skip link is the first focusable element (2.4.1); `lang` is set (3.1.1)
- landmark regions present: banner, navigation, main, contentinfo
- every `<img>` has an `alt` attribute — empty only where "decorative" is the specified
  behaviour (§16.3)
- every input has an associated **visible label**; placeholders are never labels (§16.3)
- no `tabindex` above 0; no `<div>` carrying the role a `<button>` should have
- no `title` attribute anywhere, and no timestamp in any markup attribute (§7.5.1)
- the page reflows at **320 px** with no horizontal scrolling of the page itself (§16.3)

This list is ARCHITECTURE §9's template smoke tests applied by hand, and it repeats in every
session of this track.

Then: update `NOTES.md`, update `pages/index.html`, and **print the contents of NOTES.md** at
the end of the session so the founder sees the gaps without opening a file. Do not update
`TODO.md` or `CHANGELOG.md` — this track is outside the versioned record.
