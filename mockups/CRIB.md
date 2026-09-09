# CRIB.md — shared reference for the mockup track

Built in session M1. Sessions M2–M8 read this instead of re-deriving constants, verbatim
strings, the sample cast, and the relative-age ladder from SPEC.md each time. Add to it as
later sessions need more of any of these — do not remove or renumber existing entries.

All citations are to SPEC.md at project version 1.30 unless marked ARCHITECTURE.

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
| `REQUEST_HOLD_AFTER_PROFILE_CHANGE_HOURS` | 12 (friend requests held after a photo/short-bio change; picker selections, clearing to empty, screening rejections and the extended bio are exempt) | §5.2, §13.6 |
| Pending friend-request expiry | 90 days (matches `CONTENT_TTL_DAYS`; destroys the frozen card with it) | §5.2 |
| Re-request cooldown after a declined friend request | 90 days | §5.2 |
| Daily rate limits, suggested | 20 friend requests, 10 introductions (per account per day) | §13.6, §14 |
| `CARD_ITEM_LABEL_MAX` | 40 characters (v1.29; the label on a contact-card item — new free text on a surface that had none, so it is capped hard *and* screened against `NAME_BLOCKLIST` at every save) | §10.2, §14 |
| URL allowlist | operator-curated; each row carries an **admitting category** and a **surface scope** — posts and comments, contact cards, or both (v1.29). Messenger domains are **card-only** | §7.2.3, §14 |
| URL blocklist | operator-curated, **new in v1.29** — domains refused outright, in any form, on every surface. Checked by the same shared validator as the allowlist, on **every save path, create and edit alike**. Retired by deactivating, never deleting; **no appeal channel** | §7.2.3, §7.2.4 |

Full table: SPEC §14 (lines 1082–1141 at v1.30). Pull in more rows here as later sessions need
them rather than re-reading §14 whole.

**The last three rows were added in the 1.27 → 1.30 re-sync (session R1).** Two of them are not
constants at all: the **URL allowlist and URL blocklist are operator-maintained tables**, kept in
the operator console beside each other, and §7.2.3 says of the blocklist in terms that it is *"a
table, maintained by the operator in the console alongside the allowlist … never a constant in
code."* §14 marks both ✎, as it marks `CARD_ITEM_LABEL_MAX`. They carry no backticks in the rows
above for that reason, and **a page must never render either as a code-style constant** — no
`URL_BLOCKLIST`, no monospace, no invented constant name. `CARD_ITEM_LABEL_MAX` is an ordinary
code constant and keeps its backticks.

**M7 adds:**

| Constant | Value | Ref |
|---|---|---|
| `RESET_CODE_LENGTH` | 6 digits | §4.6.1 |
| `RESET_CODE_TTL_MINUTES` | 15 | §4.6.1 |
| `LOGIN_ATTEMPT_LIMIT` | ≈ 5 failures before backoff begins, per account and per source address | §4.6.1, §13.6 |
| `LOGIN_LOCKOUT_MINUTES` | ≈ 15, base lockout, escalating with exponential backoff | §4.6.1, §13.6 |
| `INVITE_EXPIRY_DAYS` | 14; expired invites return to the sender's budget | §4.1 |
| `DELETE_GRACE_DAYS` | 30 | §4.7 |
| `BACKUP_RETENTION_DAYS` | 30 days after live erasure | §7.5, §4.7 |
| `POST_MIN_INTERVAL_MINUTES` | ≈ 10 (suggested default) | §7.3, §13.6 |

**M8 adds:**

| Constant | Value | Ref |
|---|---|---|
| `INACTIVITY_DELETE_DAYS` | 730 (two years since last login) | §4.8 |
| `INACTIVITY_WARN_DAYS` | 180, 365, 670, 700 days since last login | §4.8 |

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

### §5.2 — The friend-request send hold

*"you can send friend requests again in N hours"* — SPEC's own quoted form, stating the reason
(a photo or short-bio change) alongside the remaining time. Used on M5's
`friend-requests-sent.html`.

### §5.3 — Block framing

*"A user who wants the stronger outcome wants a block"* — SPEC's own framing for when unfriending
isn't enough. Used on M5's `unfriend-confirm.html` alongside the §5.3 unfriend quote already
registered above.

### §5.5 — Introduction wordings (both flows free-text-free)

- Broker-initiated, to each candidate: *"M wants to introduce you to [other party]"* — M5's
  `introduction-broker.html` renders this literally as *"David wants to introduce you to
  Grace."*
- **No verbatim wording exists anywhere in SPEC for flow (b)'s ask** — what M sees when a friend
  requests an introduction. M5's `introduction-requested.html` invents *"Alice asks you to
  introduce her to Henry"* for this; flagged in NOTES.md rather than presented as a SPEC quote.

### §10.3 — The contact-card cascade's own reasoning

*"Accidental under-sharing is recoverable (see request flags); accidental over-sharing is not."*
Used as real page text, not commentary, on M5's `contact-card-editor.html`.

### §7.8 — Editing hashtags: the widening notice (M6)

*"This post has comments. Widening who can see it also shows those comments to the people it
reaches."* Verbatim, rendered on `post-editor.html` when a tag is added to a profile post that
already has comments. Removing a tag narrows the audience and shows no notice at all — see the
same page's section 4.

### §4.6.1 — The checkable promise, reused (M7)

Same string already registered above, rendered as prominent real text (not fine print) on
`login.html`, and referenced (not repeated) on `reset-request.html` and `settings.html`'s email
change section.

### §4.7 — The honest erasure-plus-backup promise (M7)

*"Erased from the platform at once, and gone from the last encrypted backup within
`BACKUP_RETENTION_DAYS` = 30 days after that."* Rendered on `deactivated.html` as two separate
sentences (immediate live erasure; a separate, later backup window) rather than added together
into one deadline — §4.7 and §7.5 both explicitly refuse a combined "gone by day 120" phrasing.

### §13.6 — The feed-post spacing message, verbatim pattern (M7)

*"Slow down, you can post again in N minutes."* Rendered on `errors.html` as *"Slow down — you
can post again in 8 minutes."*

### §4.8 — The absolute deletion-date example (M8)

*"your account will be deleted on 12 March"* — SPEC's own worked example, missing only a year
(this mockup track adds one, 2027, for concreteness — see `mockups/NOTES.md`). Rendered on
`emails/inactivity-deletion.html`, and never as a relative phrase like "in a couple of months,"
which §4.8 explicitly rules out.

### §4.6.1 and §12.2, reused across the email set (M8)

The checkable promise (registered above) is repeated verbatim on `emails/reset-code.html`,
`emails/email-change-notice.html` and both scenarios of `emails/security-event.html` — every
touchpoint where a recipient might reasonably worry "was that me?" *"Alice and Tom commented on
your post"* (registered above under §12.2) is reused verbatim on `emails/social-notification.html`
as the one worked example of the optional emailed copy of an in-feed notification.

### §9.3 and §4.5 — two messages with no SPEC-given wording (M7)

Neither the single response a viewer gets when they may not see a profile (§9.3) nor the honest
message a blocked display name is rejected with (§4.5) is given verbatim anywhere in either
document. Both are this session's own invented wording — *"This page isn't here, or you don't
have permission to see it"* (`errors.html`) and *"That name isn't allowed on WeeBee. Please choose
a different one"* (`invite-redeem.html`) — flagged as invented rather than quoted, in
`mockups/NOTES.md`.

### §9.4 — The gallery reorder controls' naming pattern (M6)

*"Move '[alternative text]' up"* / *"Move '[alternative text]' down"* — SPEC's own worked
example is *"Move 'Me on a beach in Cornwall' up."* Rendered literally, per image, on M6's
`gallery-manage.html`; a control at either end of the list that has nothing to move toward is
shown disabled rather than omitted, so its presence in the tab order stays predictable.

### §13.2 — Report reasons, verbatim (M6)

Post and comment reports: *harassment or abuse · unwanted or commercial content · someone else's
private information · **the tags don't match this post** (profile posts only) · something
else.* The tag-mismatch reason only ever appears on a tagged profile post. Profile reports:
*the photo · the name · the short bio · the about section · the gallery · this person's
behaviour.* Both rendered on M6's `report-post.html` and `report-profile.html`.

**Contact-card reports (v1.30, added in R1):** *the label · the address or number · the card as
a whole · this person's behaviour.* **"The card as a whole" is reachable from any item's button**
— it is the category for the case where no single item is the complaint — and *"this person's
behaviour"* is the same last entry the profile list carries, for a card that is a symptom rather
than the thing wrong. Plus the same optional short note to the operator every report already
carries. To be rendered on the new `report-card.html`, which R3 builds; not built here. **The two
lists above are unchanged** — 1.30 added a fourth report target, it did not alter the existing
three.

### §13.5 — Operator request categories, verbatim (M6)

*Hashtag suggestion · External service request · Bug report · Accessibility problem · General
feedback / feature request.* Rendered on M6's `operator-request.html` and reused, pre-selected to
"Hashtag suggestion," on `hashtag-suggest.html`. Accessibility problems are stated as triaged
ahead of feature requests, per §13.5's own note.

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

### §7.2.3 — Composer and help copy for the two hosting categories (v1.29, R1)

SPEC says the stated purpose in composer and help copy *"stays exactly that"*, so these two are
quotations rather than paraphrases. Copy them character for character:

> *"WeeBee doesn't host video or audio. This is where your own recording lives."*

> *"WeeBee holds one photo per post. If you have sixty, they live somewhere else — link to them
> here."*

The first belongs wherever the composer explains video and audio; the second wherever it explains
the one-photo-per-post limit (`GALLERY_MAX` = 8 on a profile).

### §7.2.4 — The three link outcomes, and the rule that only one of them is an error (v1.29, R1)

SPEC's own table, copied:

| The link | What happens |
|---|---|
| On the **allowlist**, in scope for this surface (§7.2.3) | Renders as a **clickable hyperlink** |
| **On neither list** | Renders as an inert **copy box** — the address in full, with a copy control, no hyperlink |
| On the **blocklist** | **Refused.** The post, comment or card item cannot be saved |

One rule, identical on posts, comments and contact-card items (§10.2).

**A copy box is not an error, and this constrains every string in the four entries below.**
§7.2.4: a copy box is *"a different rendering, not a refusal"* — *no warning, no apology, no
error styling, no "this link is not approved" note beside it.* Only the blocklisted case is an
error. **If a string written for a copy box reads as a telling-off, it is wrong.**

### §7.2.4 — The blocklisted-link refusal — **INVENTED; SPEC gives no wording**

§7.2.4 states what this message must do and gives no words for it: it *"says plainly that this
address cannot be posted here and that the fix is to remove it"*, and *"**It names no appeal**,
because there is none"*. §16.3's rule that an error states its fix is the constraint. This
session's own wording, to be used as-is:

> *"This address can't be posted on WeeBee. Remove the link to save your post."*

The last clause names the thing being saved, so the same string on the other two surfaces reads
*"… to save your comment."* and *"… to save this item."* (a contact-card item, §10.2).

**Invented, not quoted** — recorded in `mockups/NOTES.md`. Two things must not be added to it:
**no appeal route** of any kind (no "contact the operator", no "request a review" — §7.2.3 rules
the channel out, and an error gesturing at a door that does not open is worse than one that names
no door), and **no explanation of why the domain is blocked**, which SPEC does not offer and the
operator's table does not publish. It is a field error on the offending field (§16.3, 3.3.1 /
3.3.3), shown at composition and again at save, on the create and edit paths alike.

### §7.2.4 and §16.3 — The copy control: visible text and accessible name — **INVENTED pattern**

§16.3 names the copy control among the repeated controls that must carry a distinct accessible
name, and requires that name to say **which address it copies** — *"a single feed page may carry
many"*, and an element list reading "Copy" twelve times is the dead end the rule exists to
prevent. SPEC requires only that the control be a real `<button>` and not a bare icon; it gives
no wording for either the visible text or the name. Both below are this session's own, written in
the shape of §16.3's existing worked example *"Read more of David's post from a few days ago"*:

> Visible text: *"Copy"*
> Accessible name: *"Copy the address {the full address, verbatim}"* — e.g. *"Copy the address
> https://photos.example.com/cornwall-2026"*

The naming text is visually hidden, exactly as the "read more" folds do it. The accessible name
**begins with the visible word "Copy"**, which is what keeps §16.3's *"Visible label text matches
accessible names"* (2.5.3) true. The address in the example is illustrative, not registered cast
content. **Invented, not quoted** — recorded in `mockups/NOTES.md`.

### §7.2.4 — The copy confirmation — **INVENTED wording; the live region itself is not invented**

§7.2.4 requires that the copy be *"confirmed in a polite live region"* (4.1.3), *"composing the
existing status partial"*. That partial is **`partials/_status.html`, which is already correct** —
`<p class="status-message" role="status" aria-live="polite">`. Compose it; **do not write a second
one**. SPEC gives no wording for the message. This session's:

> *"Address copied."*

**Invented, not quoted** — recorded in `mockups/NOTES.md`. It is a confirmation and nothing else:
no apology, no instruction, and nothing about approval or safety, per the no-scolding rule above.

### §13.2 — The contact-card report button (v1.30, R1)

**Visible text, given verbatim by SPEC:** *"Report this item"*. A real `<button>`, never an
unlabelled icon (§16.4). One action per item.

Its accessible name must name its own item, and SPEC gives both forms verbatim:

> *"Report the item labelled 'My photos'"* — taken from the item's label.
> *"Report the third item, a phone number."* — for an item whose label is empty, named by kind
> and position instead.

Placement and availability, all from §13.2: the action lives on the **card page** (§10.4); it is
available to anyone that page is available to — a current friend whose request has been answered
— and **not to the card's owner**, exactly as the profile report is not. **An empty card carries
no report action at all**, because there is nothing on it to report and a complaint about the
person rather than the card is a profile report. In preview-as (§9.5) *"the action renders and
does nothing."*

### §16.3 — Worked accessibility examples

- Repeated-control accessible name: *"Read more of David's post from a few days ago"*
- Profile tab page title example: *"David Dudek — Posts"* — **note:** this conflicts with
  §9.1, which names the same landing tab "Blog," not "Posts." Recorded as a contradiction in
  NOTES.md; not resolved here per the standing instruction to log and build on regardless.
- Post `<article>` accessible label pattern: *"Post by David, a few days ago"*
- **Copy control on a link's copy box** (§7.2.4, v1.29) — §16.3 names it explicitly as a repeated
  control, *"of which a single feed page may carry many"*, whose accessible name *"has to say which
  address it copies"*, with the copy confirmed in a polite live region. SPEC gives the requirement
  and no wording; the invented pattern is registered in this section's copy-control entry above.
- **Per-item report action on a contact card** (§13.2, v1.30) — §16.3 names this one explicitly
  too, *"of which one page may carry `CONTACT_ITEMS_MAX` = 12"*, named from the item's own label
  and, where there is none, from its kind and position. Here SPEC does give the wording; both
  forms are quoted in the §13.2 report-button entry above.

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

**M3 gives David his own name-change pair, "David Dudek (formerly Dave Dudek)"**, shown in the
persistent header on all four profile-tab pages — the first time the dual-name display renders
for the account whose view this track otherwise always shows. This is not reconciled against
David's plain "David" byline on M1/M2's already-built pages (feed.html, post-feed.html,
post-profile-tagged.html); per the standing fidelity choice already recorded for Priya's case
(NOTES.md entries 5 and 7), each mockup illustrates the pattern it was built to show, not one
fully self-consistent fictional timeline.

**M3 chooses Alice as the friend whose view of David's profile the four tabs render** (SPEC
§9.1 requires a friend's view; every earlier mockup rendered David's own). David and Alice's
mutual friends for the About tab's §11.5 line are Tom, Mom and Priya (three, so the idiom's
"and others" form applies). Later sessions building another friend's view of a profile should
either reuse Alice or record their own choice here.

**M4 discovers, and does not resolve, a contradiction in Priya's own established status** — see
NOTES.md's new entry on this. M2 built Priya explicitly as a **friend-of-friend**, not a friend
(matched with David on #hiking through Alice); M3's About-tab mutual-friends line then listed
Priya as one of *David and Alice's* mutual friends, which can only be true if Priya is David's
direct friend. M4 needs Priya to be a FoF for its own pages to make sense (§9.2's tagged tier is
meaningless for someone who already has full friend access), so **M4 continues M2's
characterization**: Priya remains a friend-of-friend of David's, connected only through Alice,
with exactly one mutual friend (Alice) between her and David. Priya's own profile carries
#hiking, which is how she both matches David's Cornwall post (M2) and appears as a discover
suggestion and a tagged-post author (M4, <code>discover.html</code>).

**M4 adds a sixth name, Jordan**, a plain friend-of-friend of David's — knows both Alice and Tom
(two mutual friends with David, the pair SPEC's own §9.2/§11.4 worked examples use verbatim:
"knows Alice and Tom") but shares no profile hashtag with David, which is what keeps Jordan at
the basic tier rather than the tagged one. Used on <code>profile-fof-basic.html</code> and as a
no-hashtag-match discover suggestion on <code>discover.html</code>.

**M4 adds five more names purely to give <code>friends.html</code>'s alphabetical list and
filter box something real to sort and filter**: Ben, Grace, Henry, Nadia, Sofia — plain display
names with no further backstory, listed alongside Alice, Mom and Tom. Priya and Jordan are not
among them: both are friends-*of*-friends, never friends themselves, so neither belongs on
David's own friend list.

**M5 gives Priya a short bio and photo alt text for the first time** (`friend-request-received.
html`), since neither existed anywhere before this session — everything else about her (a
friend-of-friend connected to David through exactly one mutual friend, Alice, sharing #hiking)
carries forward unchanged from M2/M4. **M5 does not invent backstory for Ben, Grace, Henry,
Nadia or Sofia**, consistent with their standing "no further backstory" characterization —
where `introduction-broker.html` needs Grace's short bio or shared hashtags, it renders a
`.placeholder-field` instead of writing new content for her. **M5 adds one new group, "Book
club"** (`contact-card-editor.html`), alongside the established "Hiking crew," containing Tom,
used only to demonstrate §10.3's deny-beats-allow conflict rule when a friend belongs to two
groups with opposing overrides on the same contact-card item. Jordan (pending sent request),
Alice and Henry (the requested-introduction pair), and Sofia (unfriend/block) are all reused as
established, with no new facts added about them.

**M7's `invite-redeem.html` necessarily breaks from "every mockup renders David's view"** in the
other direction M2's Priya (entry 12) and M4's preview-as pages already established a precedent
for: nobody has an account yet at the point this page renders, so there is no "David's view" to
show. David stands in as **the inviter** instead — a role any other established friend could
equally have played — which is also what lets the page state §4.1's automatic
inviter/invitee friendship concretely ("you and David automatically become friends") rather than
abstractly.

**M8 adds a seventh name, Jamie**, a new, minimal, backstory-free placeholder used only as the
envelope recipient on `emails/invite.html` and `emails/verify-code.html` — the invitee mid
registration, continuing M7's own precedent that nobody has an account yet at this point in the
story, so there is no established cast member to name. **M8 also gives David two invented example
email addresses**, `david@example.com` (his ordinary login address, used as the recipient on
every other email in this session) and `d.dudek@example.com` (the new address in the
email-change pair) — both on the reserved documentation domain `example.com`, chosen so neither
collides with any real address. The sending address, `notifications@weebee.social`, is likewise
invented: ARCHITECTURE §3.6 requires a transactional email provider but names no specific address.

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

**Phrases used on the M3 profile tabs:** A few hours ago · About a day ago · A couple of days
ago · A few days ago · **About a year ago** — the first use in this track of a ladder rung past
"a couple of months ago," on the Pinned tab's genuinely-old post and its chronological
reappearance on the Blog tab (§7.6: "the long tail of the ladder exists for this case and for
no other").

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

**M3 builds six more pages**, per the M3 prompt's own explicit filenames: `profile-blog.html`
(the Blog tab, landing), `profile-pinned.html`, `profile-photos.html`, `profile-about.html`,
`overlay-gallery.html`, and `overlay-post.html`. These are distinct from the placeholder
`profile.html` the main nav and M1/M2 pages already link to (NOTES.md entry 8) — that link
target is left unresolved, as entry 8 anticipated; M3 did not rename or retarget it, since
`partials/_nav.html` and the already-built M1/M2 pages are outside this session's touched
files. `profile-about.html`'s hashtag links point at the plain `discover.html` target already
assumed by M1's nav (no filter query-string convention is established by any session yet — left
for M4, which builds discover.html itself).

**M4 builds nine pages** and establishes the filtered-tag-view convention `discover.html` left
open: `profile-fof-basic.html`, `profile-fof-tagged.html`, `discover.html`, `discover-tag.html`,
`friends.html`, `preview-as-friend.html`, `preview-as-fof.html`, `preview-as-fof-tagged.html`,
`preview-as-request-card.html`. **The tag-filter convention**: since a static mockup cannot
build a filtered view per tag, `discover-tag.html` is one concrete worked example, hardcoded to
`#hiking`. A hashtag link elsewhere in this session's own new pages points to
`discover-tag.html` when the tag is #hiking, and to the plain `discover.html` (same
unbuilt-placeholder treatment as ever) for #jazz, #cornwall and #baking — this session did not
retarget M3's own hashtag links, which stay on `discover.html` for every tag, since
`profile-about.html` and its siblings are outside M4's touched files (same boundary M3 drew
around M1/M2). **One more forward reference**: `profile-fof-tagged.html`'s tab strip links its
About tab to `profile-fof-tagged-about.html`, not built this session — `profile-fof-tagged.html`
itself is a single file standing in for the Blog-tab instance of the tagged friend-of-friend
view (see NOTES.md), and the About-tab instance is left as an assumed filename for whichever
session or founder decision picks it up, the same treatment M1's nav gave `friends.html` and
`discover.html` themselves before this session existed.

**M5 builds seven pages across the prompt's six numbered items**: `friend-request-received.html`,
`friend-requests-sent.html`, `introduction-broker.html`, `introduction-requested.html`
(item 3's two flows, one file each), `contact-card-editor.html`, `contact-card-received.html`,
and `unfriend-confirm.html` (item 6's unfriend and block, one combined file, per the prompt's own
filename). No new forward-referenced filenames are introduced; every link this session adds
either resolves to one of these seven, to an already-built page, or to the still-unbuilt
`profile.html`/`report.html`/`settings.html` placeholders carried since M1/M2.

**M6 builds eight pages**: `post-editor.html`, `gallery-manage.html`, `report-post.html`,
`report-profile.html`, `operator-request.html`, `hashtag-suggest.html`, `settings.html` (the
still-unbuilt filename M1's nav already pointed at — it now resolves), and `groups.html`.
`settings.html` links onward to one new forward-referenced filename, `account-deletion.html`,
for M7's account-edges session to build.

**Filename mismatch, not corrected here**: M2's `post-profile-tagged.html` links its
tag-mismatch report action at `report.html` (singular, unsplit). This session's own prompt
specifies two separate filenames instead — `report-post.html` and `report-profile.html` — so
`report.html` is never built and that one link now points at a filename this track will not
produce. Per the precedent M3 and M4 already set for cross-session links (neither retargeted a
link in a file outside its own touched set), `post-profile-tagged.html` is left as it is; see
`mockups/NOTES.md` for the entry recording this.

**M7 builds nine pages**: `login.html`, `reset-request.html`, `reset-code.html`,
`invite-redeem.html`, `invites.html` (inferred), `banned.html`, `deactivated.html`,
`export.html`, `errors.html`, and `maintenance.html` (a standalone file, not wrapped in
`_base.html` — see §6 below). No new forward-referenced filenames are introduced.

**Filename mismatch, not corrected here**: M6's `settings.html` links its "Delete your account"
action at `account-deletion.html`, a forward reference CRIB.md itself registered at the time.
This session's own prompt, however, names the page it builds for the deletion grace period
`deactivated.html` instead — a different filename for what is functionally the same surface
`account-deletion.html` was standing in for. `account-deletion.html` is therefore never built,
and `settings.html`'s link now points at a filename this track will not produce.
`banned.html`'s own "Delete your account" link reuses the same `account-deletion.html` forward
reference, for consistency with `settings.html`, rather than pointing at `deactivated.html`
instead — deliberately, since `deactivated.html` as built assumes deletion is already
in progress (it shows the grace-period banner), which isn't the state either linking page is in.
Per the precedent M3, M4 and M6 already set for a link in a file outside the current session's
touched set (see entries 8, 16, 20, 21, 27 in `mockups/NOTES.md`), `settings.html` is left as
found; see `mockups/NOTES.md` for the full entry.

**M8 builds ten templates in a new directory, `pages/emails/`**, each as an `.html` + `.txt`
pair: `invite`, `verify-code`, `reset-code`, `email-change-code`, `email-change-notice`,
`security-event`, `inactivity-dormant`, `inactivity-deletion`, `operator-warning`,
`social-notification`. This is ten files where the session's own prompt says "nine templates" —
see `mockups/NOTES.md` for the count mismatch, not resolved, built as ten regardless since item 4
of the prompt's own list unambiguously asks for two separate files
(`email-change-code`/`email-change-notice`). Unlike every other page in this track, none of the
ten is wrapped in `partials/_base.html` — see §6 immediately below for why and how.

---

## 6. Commentary/copy separation — the `.commentary` class and the toggle

Added by the cross-cutting retrofit run after M5 (`prompts/mockups/content-commentary-separation.md`),
which audited every page M1–M5 had built. The standing rule (now also in
`prompts/mockups/README.md` and every `M1.md`–`M8.md`'s own "Standing constraints" section): every
sentence on every page is either simulated content (what WeeBee would actually say to a user who
has never read a design document — plain, warm, non-technical) or commentary (a build note for the
founder — SPEC/ARCHITECTURE citations, invented-vs-established calls, cross-references to another
mockup file, NOTES.md or CRIB.md). Never mixed in one sentence or paragraph.

- **The class is `.commentary`**, not the earlier `.session-note` (renamed track-wide; every page
  that used the old name was updated). Styled in `styles.css` as italic monospace
  (`var(--font-mono)`, `font-style: italic`) in the existing muted secondary color and size — a
  bigger visual break than grey-and-small alone, so it reads unmistakably as a build note even
  when skimming.
- **The toggle** is one real `<input type="checkbox" id="commentary-toggle" checked>` with a
  visible `<label>` ("Show build commentary and SPEC citations"), added once in the shared
  `partials/_base.html` header — not hand-rolled per page. A CSS `body:has(#commentary-toggle
  :not(:checked)) .commentary { display: none; }` rule in `styles.css` hides every `.commentary`
  block on the page when unchecked; no scripts involved. Default is checked (visible), matching
  the track's prior behavior — hiding commentary is the deliberate action.
- **Constants in code form** (`FRIEND_CAP`, `CONTACT_ITEMS_MAX`, etc.) always belong inside
  `.commentary`; the human-readable fact they encode ("up to 12 items," "a 300-friend limit") may
  stay in real copy on its own, without the shouty name attached.
- **A genuine SPEC-mandated verbatim string stays real copy**, never commentary, even though it is
  quoted directly from SPEC — e.g. the unfriend confirmation's blockquote (§5.3) and the block
  framing ("A user who wants the stronger outcome wants a block," §5.3). Only the citation
  identifying *which* section mandates the wording, and any surrounding explanation, moves to
  commentary.
- **`pages/index.html` is exempt.** It is the founder's review index by design (M1's own
  instructions: "this doubles as the founder's review index, so the citation matters as much as
  the link") — it never pretends to be simulated product copy in the first place, so the grandma
  test does not apply to it and it carries no `.commentary` wrapping.
- **No-persistence limitation**: see `NOTES.md`. The toggle is pure CSS with no script and no
  cookie, so it cannot remember its state across a page load — every page opens with commentary
  visible, regardless of what a previous page was set to.

M6–M8 build compliant pages from the start using this convention; they do not need a follow-up
retrofit.

**M7 adds one narrow exception to the shared-harness rule, and one documented harness
limitation it did not fix:**

- **`maintenance.html` is not wrapped in `_base.html`.** Every other page in this track is built
  by `build.py` reading `pages/*.html`, substituting its front matter into the shared
  `partials/_base.html`, and writing the result to `site/`. `maintenance.html` is the one
  exception: `build.py` now special-cases this filename and copies it through to `site/`
  unchanged, because the real page it mocks up is served by Caddy, entirely outside the Django
  app (ARCHITECTURE §7.2), and must fetch nothing at all — including `styles.css`, which
  `_base.html` links unconditionally with no per-page opt-out. `pages/maintenance.html` is
  therefore a complete, standalone HTML document (its own `<style>`, own `<!DOCTYPE html>`), not
  a page body plus front matter. This is the one place in the M1–M8 track where a session edits
  `build.py` itself, rather than only `pages/`; see `mockups/NOTES.md` for the full reasoning
  and why `banned.html`'s narrower "no nav" requirement, immediately below, was handled
  differently.
- **`banned.html` cannot literally omit the shared nav within this harness.** SPEC §13.2.1
  requires the banned-account page to carry no navigation at all, "the page does not use the
  standard `_nav.html`." Unlike `maintenance.html`, this page is an ordinary page within the
  Django app in the real product, and `_base.html`'s header/nav is baked in uniformly for every
  page in `pages/`, with no per-page override — suppressing it here would mean editing
  `partials/`, outside this session's touched files. `banned.html` is left going through the
  normal pipeline, with a prominent on-page note explaining the gap, following the precedent
  M3's entry on the missing `_modal.html` partial already set (`mockups/NOTES.md`, entry 13):
  document a real harness limitation rather than extend `partials/` or `build.py` beyond what a
  single session's touched-files scope allows.

**M6 adds one more shared convention: `.page-provenance`**, for a page that is itself assembled
or inferred rather than specified (`settings.html`, `groups.html`). Unlike `.commentary`, this
label must stay visible even with the commentary toggle off, since the whole point is that the
founder can tell such a page apart from an ordinary mockup at a glance, in whatever toggle state
the page happens to be in — so it is deliberately **not** wrapped in `.commentary` and is
untouched by the `body:has(#commentary-toggle:not(:checked))` rule. Styled in `styles.css` as a
bordered, plain-weight box (not italic monospace), distinct from both `.commentary` and
`.notice`. A page carrying this label is still expected to separate its own simulated copy from
its own commentary blocks everywhere else on the page — the exemption covers only the one
top-of-page label, not the whole page the way `pages/index.html` is wholly exempt.

**M8 extends `build.py` a second time, generalizing the one-file exception M7 made for
`maintenance.html` into a whole-directory rule.** Every file directly inside `pages/emails/`
(both the `.html` and its `.txt` twin) is copied straight through to `site/emails/`, unwrapped —
no `_base.html`, no `{{include}}`, no shared header, nav or footer, and critically, no
`<link rel="stylesheet" href="styles.css">`. This is not only a build-harness workaround the way
`banned.html`'s carried-over nav was (`mockups/NOTES.md` entry 35): SPEC §16.3 itself places
email "outside WCAG's scope for pages," and this session's own instructions single out §16.3's
email requirement as "a requirement rather than a preference" — legible without images or CSS,
with no layout that depends on a stylesheet. Wrapping an email template in the shared
`_base.html` would inject the mockup site's own stylesheet into markup whose entire point is
demonstrating it doesn't need one, which would be a straightforward fidelity failure, not a
convenience skipped. Each of the ten templates therefore carries its own minimal inline `<style>`
(no external stylesheet reference at all), following the precedent `maintenance.html` already set
for a standalone document, including a locally-scoped `.commentary` class matching
`styles.css`'s own — but with **no commentary toggle**, since the checkbox-hack toggle lives in
`_base.html`'s shared header, which these pages don't include. See `mockups/NOTES.md` for this
limitation stated plainly rather than worked around.
