# Mockup session M4 — the visibility set: who sees what

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** `mockups/pages/` (two non-friend profile views, discover ×2, friends page, preview-as ×4), `mockups/CRIB.md`, `mockups/NOTES.md`, `mockups/pages/index.html`. **No design document is edited.**
> **Depends on:** M1 (harness, crib sheet), M3 (the friend view these are the counterparts to).
> **Expected outcome:** the same profile rendered at each visibility tier, the two pull-only discovery surfaces, the friends page, and all four preview-as modes — the set that makes §9.2's table visible.

---

You are working in the WeeBee design-document repository — a small, private, deliberately
anti-viral social network whose design documents exist but whose platform has not been built.
Read `README.md`, then `prompts/mockups/README.md`, `mockups/NOTES.md` and `mockups/CRIB.md`.

This is session M4 of eight building **browser-viewable mockups of the design exactly as
`SPEC.md` and `ARCHITECTURE.md` already describe it.** It is the session where the platform's
central mechanism — who can see what, and what an absence looks like — becomes visible, so
the negative requirements below matter as much as the positive ones.

## Standing constraints

- **Build only what the documents describe.** No invented features, no fixes. Contradictions
  go in `mockups/NOTES.md`; build on regardless.
- **Never edit** `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md` or
  anything in `prompts/`. Write inside `mockups/` only.
- **SPEC leads** where ARCHITECTURE lags it (prompt 09 has not been run).
- **Neutral, layout-true fidelity**; the existing `styles.css`; no invented brand palette.
- **Static pages, no scripts**; **nothing fetched from anywhere**; compose the M1 partials.

## What to read

| Document | Sections | Lines (v1.27) |
|---|---|---|
| SPEC | §9.1 (the *"What a non-friend sees"* paragraph especially) | 498–542 |
| SPEC | §9.2 Visibility tiers — the whole table | 554–564 |
| SPEC | §9.3 Access rules | 564–571 |
| SPEC | §9.5 Preview-as | 597–607 |
| SPEC | §11.2 Hashtags, §11.3 Hashtag-gated FoF visibility | 666–706 |
| SPEC | §11.4 The discover page | 706–713 |
| SPEC | §11.5 Friend-list visibility | 713–718 |
| SPEC | §11.6 Reaching a profile | 718–728 |
| SPEC | §5.2 Friend requests (for preview-as mode 4) | 165–176 |
| SPEC | §5.4 Blocking | 181–190 |
| SPEC | §8.1 Comments (the link-or-plain-text rule) | 413–427 |
| SPEC | §17 Non-Goals | 1122–1130 |
| SPEC | §16.3 | 1027–1083 |

## What to build

### 1. `pages/profile-fof-basic.html` — a plain friend-of-friend's view

§9.2: a FoF with any mutual friend sees the **basic tier only** — display name, profile photo,
short bio, profile hashtags, and the specific mutual friends they share — and **About only**.

Three things this page exists to show, all easy to get wrong:

- **No tab strip is drawn at all.** §9.1: *"A tab is rendered only where this viewer has
  something in it, and when only one tab qualifies, no tab strip is drawn at all — a lone tab
  reads as a broken interface."*
- **The line goes below the content, never above it**, verbatim: *"You and David are not
  friends. Friends see his posts, photos and about section."* §9.1 gives the reason —
  *"leading with it makes the page read as a refusal rather than a profile."*
- **The line is unconditional**, shown whether or not the owner has ever posted. §9.1: a line
  that appeared only when content existed *"would tell a non-friend whether there is anything
  to miss."*

No extended bio, no gallery (§9.2). The report action is still in the header — §13.2 calls
that placement load-bearing.

### 2. `pages/profile-fof-tagged.html` — a hashtag-matched friend-of-friend's view

§9.2's third row: basic tier **plus** the owner's profile posts carrying a tag the viewer also
carries, under all three live conditions of §11.3.

- **About, plus Blog and Pinned filtered to matching posts**; each tab omitted if nothing
  matches. So here a tab strip *is* drawn, and it has three tabs, not four.
- **Non-matching posts are absent with no placeholder.** §9.2: *"no 'some posts are hidden,'
  which would be an oracle telling a non-friend how much they are missing."* Draw nothing.
- **Feed posts never appear** — §11.3 gates profile posts only (§9.1, §9.2).
- The gallery and the extended bio remain invisible.
- Comments on a visible post are visible, **with commenter names rendering as plain text where
  this viewer has no connection to the commenter** (§8.1) — the same rule M2 exercised.

Add a NOTES.md entry: a static mockup shows one viewer, so §5.4's mutually-invisible blocked
pair — a comment present for one viewer and absent for another on the same page — **cannot be
shown as a page**. Caption it on this page instead of faking it.

### 3. `pages/discover.html` and `pages/discover-tag.html` — the discover page

§11.4: *"One dedicated page the user must deliberately visit."* Pull-only.

- **People suggestions:** FoFs, each shown with auto-context. §11.4's own example is *"knows
  Alice and Tom · shares #hiking"*.
- **Matched posts:** hashtag-gated FoF profile posts per §11.3.
- **The tag filter** (`discover-tag.html`), reached by clicking that tag anywhere (§11.2).
  The filtered view shows connected people carrying the tag on their profile, and
  already-visible tagged profile posts.
- **Nothing from discovery ever appears in the feed.** No push, no notification, **no "someone
  viewed you"** (§11.4). Nothing on either page suggests otherwise.
- **No global hashtag browsing** — there is no "see all posts tagged #x" anywhere (§11.2,
  §17). The tag view is viewer-scoped and only that.
- No counts of any kind (§17).

### 4. `pages/friends.html` — the friends page

§11.6, *"the commonest route to a profile"*:

- The user's own friend list, **listed alphabetically by display name — no other sort order**,
  since *"any other ordering would be the platform inferring who matters."*
- **A filter box over that list, labelled "Filter your friends"** — a **visible label, never
  placeholder text** (§11.6, §16.3). §11.6 makes this a requirement rather than a copy
  suggestion: *"a box labelled 'Search' on this page tells the user the platform has a search,
  on a platform whose central promise is that it has none."* The exact string may change; that
  it says *filter*, and says *your friends*, may not.
- No count of friends anywhere on the page (§17).

### 5. Preview-as — four pages

§9.5 makes preview-as a **required feature**. The owner previews their profile page, their
contact card, and the card their friend requests display, exactly as another person would see
them. Four modes, four pages:

| Page | Mode |
|---|---|
| `preview-as-friend.html` | **As a specific friend** — a picker over the friend list. Required because the contact card is per-friend (§10.3) and the mutual-friend block is per-viewer |
| `preview-as-fof.html` | **As a generic friend-of-friend** — the basic tier, with the mutual-friend block shown as **a placeholder**, since the actual names depend on which FoF |
| `preview-as-fof-tagged.html` | **As a FoF carrying a chosen hashtag** — a picker over *"the tags present on the owner's own profile and pinned posts"*, showing Blog and Pinned filtered exactly as §11.3 filters them |
| `preview-as-request-card.html` | **As it appears in a friend request** (§5.2) — not a profile view, but the highest-consequence view of the short bio and photo |

Common to all four (§9.5): preview-as is **read-only, changes no state, sends no notification,
marks itself with persistent real text, and is exitable by keyboard.** Draw that marker as
real text, not a colour or a badge (§16.4).

**There is deliberately no "as a specific friend-of-friend" mode** — §9.5: *"the owner cannot
enumerate their FoFs, and offering that picker would leak a friend list in the opposite
direction."* Do not add one, and say on the page that its absence is deliberate.

For mode 4, follow §9.1's field table exactly — the profile photo and short bio are **frozen**
at send time, while the display name, shared hashtags, mutual friends and report action are
**live**. §9.1 calls that split *"a security boundary, not a rendering detail"*. Session M5
builds the received card itself; this page is the owner's preview of it.

## Before you finish

Check every page, as in the earlier sessions — plus three specific to this set:

- **`profile-fof-basic.html` has no tab strip at all**, and its "not friends" line is below
  the content
- **no placeholder anywhere for content the viewer cannot see** (§9.2) — no "hidden posts", no
  greyed rows, no counts
- **no number appears on any of these pages** — not a friend count, not a suggestion count,
  not a match count (§17; §7.9 explains why a match count in particular is a privacy oracle)

Plus the standing list: one `<h1>` and a unique `<title>` per page; skip link first focusable;
`lang` set; landmarks present; every `<img>` has an `alt`; every input has an associated
**visible label** (the filter box especially); no `tabindex` above 0; no `title` attribute; no
timestamp in any markup attribute; reflow at **320 px** with no horizontal page scroll.

Then: add this session's strings to `CRIB.md`, add its pages to `pages/index.html`, update
`NOTES.md`, and **print the contents of NOTES.md**. Do not touch `TODO.md` or `CHANGELOG.md`.
