# CRIB.md — shared reference for the mockup track

Built in session M1. Sessions M2–M8 read this instead of re-deriving constants, verbatim
strings, the sample cast, and the relative-age ladder from SPEC.md each time. Add to it as
later sessions need more of any of these — do not remove or renumber existing entries.

All citations are to SPEC.md at project version 1.27 unless marked ARCHITECTURE.

---

## 1. Configuration constants in use (SPEC §14)

| Constant | Value | Ref |
|---|---|---|
| `FEED_FOLD_CHARS` | 500 characters (feed, and profile Pinned tab) | §7.7, §7.6 |
| `BLOG_FOLD_CHARS` | 2,000 characters (profile Blog tab) | §7.7, §9.1 |
| `COMMENT_FOLD_CHARS` | 300 characters (comments, every surface) | §8.1, §7.7 |
| `POSTS_PER_PAGE_DEFAULT` | 20 | §7.7.1 |
| `POSTS_PER_PAGE_OPTIONS` | 20 / 40 / 60 (viewer-chosen) | §7.7.1 |
| `EXPIRY_COUNTDOWN_DAYS` | 14 | §7.5 |
| `CONTENT_TTL_DAYS` | 90 | §7.5 |
| `FRIEND_CAP` | 300 | §5.1 |
| `POST_AUDIENCE_MAX` | 30 | §7.1 |
| `GALLERY_MAX` | 8 | §9.4, §14 |
| `PIN_LIMIT` | 10 | §7.6 |
| `PROFILE_HASHTAG_MAX` | 10 | §11.2 |
| `CONTACT_ITEMS_MAX` | 12 | §10.2 |
| `BIO_SHORT_MAX` | 200 characters | §9.4 |
| `BIO_EXTENDED_MAX` | 2,000 characters | §9.4 |
| `POST_LENGTH_MAX` | 10,000 characters | §7.2.1 |
| `COMMENT_LENGTH_MAX` | 2,000 characters | §7.2.1, §8.1 |
| `NAME_CHANGE_COOLDOWN_DAYS` | 90 (must stay ≥ `NAME_TRANSITION_DAYS`) | §4.5.1 |
| `NAME_TRANSITION_DAYS` | 90 (dual "formerly" display) | §4.5.1 |
| `ALT_TEXT_MAX` | 1,000 characters (image alternative text) | §16.3 |
| `GROUP_SIZE_MAX` | 30 (matches `POST_AUDIENCE_MAX`, so any group is a valid post audience) | §6 |

Full table: SPEC §14 (lines ~898–953 at v1.27). Pull in more rows here as later sessions need
them rather than re-reading §14 whole.

---

## 2. Verbatim interface strings

Use these exact strings wherever the governing section applies. Do not paraphrase.

### §7.9 — Stated visibility (three lines + comment-box line)

| Post type | Line |
|---|---|
| Feed post | *"Visible to: the friends {author} sent this to."* |
| Profile post, untagged | *"Visible to: all of {author}'s friends."* |
| Profile post, tagged | *"Visible to: all of {author}'s friends, and friends-of-friends with **any of** #hiking, #jazz."* (tag names are §7.9's own example) |

Comment box, every post: *"Your comment will be visible to the same people."*

SPEC's own table uses "David" as the illustrative author in all three rows. **M1 substitutes
the real post's author name** (Alice, Tom, Mom, Priya) on feed.html, since feed.html mocks
David's own feed and every post shown there was authored by one of his friends, not by David —
see NOTES.md's entry on this. Only the "feed post" row is actually used on feed.html; the two
profile-post rows are reserved for profile/single-post views (M2, M3), since profile posts
never appear as content in the feed itself (§7.7, §9.1 — only a notification about them does).

### §9.1 — Non-friend profile view

*"You and David are not friends. Friends see his posts, photos and about section."*

### §7.1 — Composer destination choice (no default; both required text)

- *"Send to a few friends — appears in their feed"*
- *"Post to my blog — all your friends can find it."*

### §5.3 — Unfriend confirmation

*"They'll no longer see your posts or your about section. If you have friends in common, they
can still see your name, photo and short bio — and any blog post tagged with an interest you
both share."*

### §11.6 — Friends page filter box label

*"Filter your friends"* — a visible label, never placeholder text. Never "Search".

### §4.6.1 — The checkable anti-phishing promise

*"WeeBee will never email you a link to log in or reset your password — only a code you type
in yourself."*

### §12.2 — Notification wordings (names, never numbers; real text, never an icon)

- *"David posted to his blog"*
- *"David changed his profile photo"*
- *"David added 3 photos to his gallery"*
- *"Alice and Tom commented on your post"*
- Overflow form: *"and others"* (never "3 new comments")

### §12.3 — Coalesced notification

*"David posted twice to his blog"* — links to the blog tab, not to either individual post.

### §6 — Groups, the audience-save suggestion

*"Save this selection as a group?"* — offered by the composer, never automatic (M2,
composer.html).

### §8.2.2 — Reaction line and react-control accessible names (M2)

- The reaction list's own accessible name: *"Reactions to your post"*, *"Reactions to your
  comment"*.
- The react control's own text: *"React"* (not yet reacted) or *"Reacted: Love it!"* (reacted,
  phrase named), and a **distinct accessible name** per control via visually hidden text —
  SPEC's own worked examples are *"React to David's post"*, *"React to Alice's comment"*.
- Per-phrase button accessible name — SPEC's own worked example: *"Love it! — react to Alice's
  comment"*.
- The button that clears a set reaction: *"Remove reaction"*.
- **Where each literally renders in this track:** "React to David's post" needs a control on a
  post David authored, viewed by someone who is *not* David — impossible on David's own
  single-post view (SPEC §8.2 forbids a react control on your own content). M2 places it on
  `post-profile-tagged.html`, whose viewer is Priya, not David. See NOTES.md for why that page
  breaks from "every mockup renders David's view."

### §7.5 — Expiry countdown (absolute days, the one exception to relative time)

*"deletes in 6 days"* — SPEC's own example. M1 renders this capitalized as a standalone line,
*"Deletes in 6 days"*, on feed.html.

### §7.8 — Edited marker

The word *"edited"* plus the relative time of the most recent edit, as real text beside the
post's own age. No version history, no diff.

### §8.2 — Reaction line idiom (author-private; names, never counts)

*"Alice: Love it! · Mom: So proud!"* — the separator is presentational, not specified.
`REACTION_SET` examples given in SPEC: "Agreed!", "Love it!", "So proud!", "Thinking of you",
"Congrats!", "Ha!".

### §16.3 — Worked accessibility examples

- Repeated-control accessible name: *"Read more of David's post from a few days ago"*
- Profile tab page title example: *"David Dudek — Posts"* — **note:** this conflicts with
  §9.1, which names the same landing tab "Blog," not "Posts." Recorded as a contradiction in
  NOTES.md; not resolved here per the standing instruction to log and build on regardless.
- Post `<article>` accessible label pattern: *"Post by David, a few days ago"*

---

## 3. The sample cast

Base cast, taken directly from SPEC's own examples (see table above for citations):

| Name | Role |
|---|---|
| **David** (David Dudek) | The account whose view every mockup renders |
| **Alice** | Friend |
| **Tom** | Friend |
| **Mom** | Friend |

**M1 adds a fifth name, Priya (formerly Priyanka)**, used once on feed.html to demonstrate the
§4.5.1 "NewName (formerly OldName)" dual-name display — nothing in SPEC's own examples supplies
a name-change pair, so this one is invented for exactly this purpose and for no other. Later
sessions may reuse Priya or add a sixth name where a page needs one; note it here if you do.

---

## 4. Relative-age ladder (SPEC §7.5.1) — phrases in use

Full ladder (all 39 rows), copied here so later sessions don't re-open SPEC §7.5.1 for it.
Each row is an upper bound on elapsed time; first match wins.

| Elapsed < | Displays | | Elapsed < | Displays |
|---|---|---|---|---|
| 75 s | Just now | | 48 h | About a day ago |
| 115 s | Over a minute ago | | 72 h | A couple of days ago |
| 170 s | A couple of minutes ago | | 5 d | A few days ago |
| 5 min | A few minutes ago | | 7 d | Several days ago |
| 8.5 min | Several minutes ago | | 10 d | About a week ago |
| 13.5 min | About 10 minutes ago | | 13 d | Over a week ago |
| 17.5 min | About 15 minutes ago | | 17 d | A couple of weeks ago |
| 25 min | About 20 minutes ago | | 21 d | Over a couple of weeks ago |
| 40 min | About a half hour ago | | 28 d | A few weeks ago |
| 57 min | About 45 minutes ago | | 34 d | About a month ago |
| 70 min | About an hour ago | | 57 d | Over a month ago |
| 86 min | Over an hour ago | | 66 d | A couple of months ago |
| 101 min | About an hour and a half ago | | 100 d | Over a couple of months ago |
| 115 min | Over an hour and a half ago | | 135 d | A few months ago |
| 141 min | A couple of hours ago | | 200 d | About six months ago |
| 181 min | Over a couple of hours ago | | 300 d | Several months ago |
| 5 h | A few hours ago | | 425 d | About a year ago |
| 12 h | Several hours ago | | 550 d | Over a year ago |
| 24 h | Over 12 hours ago | | 900 d | A couple of years ago |
| | | | 1,600 d | A few years ago |
| | | | — | Several years ago |

The tail past ~90 days (from "A couple of months ago" on) is only ever reachable by a **pinned**
post, since unpinned content is deleted at `CONTENT_TTL_DAYS` = 90 (§7.5.1's own note).

**Phrases used on feed.html / feed-older.html (M1):** A few minutes ago · About an hour ago ·
A couple of hours ago · A few hours ago · Over 12 hours ago · About a day ago · A couple of
days ago · A few days ago · Several days ago · About a week ago · Over a couple of months ago
(the countdown post — a deliberately old unpinned post, elapsed ≈ 84 days, inside the 14-day
countdown window) · About a month ago · Over a month ago.

**Never in markup:** no `title` attribute, no `<time datetime>`, no data attribute carrying the
real timestamp, anywhere these phrases appear (§7.5.1, ARCHITECTURE §3.8).

---

## 5. Nav target filenames assumed by M1

`partials/_nav.html` links to `feed.html` (built), `composer.html`, `profile.html`,
`friends.html`, `discover.html`, `settings.html` (none of the latter five built yet — see
NOTES.md). Later sessions that build those surfaces should use these filenames so the M1 nav's
links resolve rather than introducing a second set of names.

**M2 adds one more assumed filename:** `post-profile-tagged.html`'s report action links to
`report.html`, not yet built — expected to land in M6 ("report and operator forms"). M2 also
built `post-feed.html`, `post-profile-tagged.html`, and `post-preformatted.html` themselves,
so composer.html's own links to `post-preformatted.html` and any future page linking to a
single-post view can now resolve.
