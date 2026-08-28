# Mockup session M5 — friendship and contact flows

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** `mockups/pages/` (friend requests, introductions, contact cards, unfriend/block), `mockups/CRIB.md`, `mockups/NOTES.md`, `mockups/pages/index.html`. **No design document is edited.**
> **Depends on:** M1 (harness, crib sheet), M4 (the request card is previewed there; this session builds the received one).
> **Expected outcome:** every surface on which one person reaches another exists — all of them free-text-free, all of them consent-based.

---

You are working in the WeeBee design-document repository — a small, private, deliberately
anti-viral social network whose design documents exist but whose platform has not been built.
Read `README.md`, then `prompts/mockups/README.md`, `mockups/NOTES.md` and `mockups/CRIB.md`.

This is session M5 of eight building **browser-viewable mockups of the design exactly as
`SPEC.md` and `ARCHITECTURE.md` already describe it.**

The unifying rule of this session, from §13.1: the platform has **no free-text messaging
channel** — friend requests, introductions and reactions carry no composed text, and there is
no DM system at all. Every surface below is shaped by that, and the one honest qualification
(§13.1, §5.2: the request card does push the sender's own photo and short bio at someone who
never asked) is what several of the controls exist to answer.

## Standing constraints

- **Build only what the documents describe.** No invented features, no fixes. Contradictions
  go in `mockups/NOTES.md`; build on regardless.
- **Never edit** `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md` or
  anything in `prompts/`. Write inside `mockups/` only.
- **SPEC leads** where ARCHITECTURE lags it (prompt 09 has not been run).
- **Neutral, layout-true fidelity**; the existing `styles.css`; no invented brand palette.
- **Static pages, no scripts**; **nothing fetched from anywhere**; compose the M1 partials —
  ARCHITECTURE §3.8 is explicit that no page hand-rolls a form control or a status message.

## What to read

| Document | Sections | Lines (v1.27) |
|---|---|---|
| SPEC | §5.1 The friend cap | 161–165 |
| SPEC | §5.2 Friend requests | 165–176 |
| SPEC | §5.3 Unfriending | 176–181 |
| SPEC | §5.4 Blocking | 181–190 |
| SPEC | §5.5 Introductions | 190–201 |
| SPEC | §9.1 — the **frozen/live field table** for the request card | 498–542 |
| SPEC | §9.2 Visibility tiers (the basic tier) | 554–564 |
| SPEC | §10.1–§10.5 Contact cards | 632–661 |
| SPEC | §13.2 Reporting (**where the action lives**) | 792–812 |
| SPEC | §13.6 Rate limits (the friend-request send hold) | 876–898 |
| SPEC | §16.3, §16.4 | 1027–1089 |
| ARCHITECTURE | §3.8 (the contact-card toggles are named there) | 175–191 |

## What to build

### 1. `pages/friend-request-received.html`

The card as its recipient sees it. §5.2: *"Requests carry no composed text: there is no message
field, no note, no subject line."* The recipient sees the requester's basic-tier profile, the
mutual friends they share, and shared profile hashtags — **the system generates this context;
the requester writes nothing into the request.**

Follow **§9.1's field table exactly**, and put a short visible note on the page saying which
fields are frozen and which are live, because §9.1 calls the split *"a security boundary, not
a rendering detail"*:

| Field | Source |
|---|---|
| Profile photo | **Frozen** at send time |
| Short bio | **Frozen** at send time |
| Display name | **Live**, through the shared helper |
| Shared profile hashtags | **Live** |
| The mutual friends they share | **Live** |
| The report action | **Live** — it targets the requester's profile |

- **The card carries the report action** (§5.2, §13.2), a real `<button>` with visible text,
  never an unlabelled icon. §13.2 calls this placement load-bearing: the profile photo is the
  one author-controlled thing that cannot be screened, and this card pushes it at someone who
  never asked for it.
- Accept and decline. **Declines are silent** — *"the requester is never notified; the request
  simply never resolves for them"* (§5.2). Show nothing that would tell the requester.
- §9.1's basic-tier invariant: the header plus the About tab minus the extended bio is
  **exactly** what this card shows. Render it from the same markup you used in M4's
  `profile-fof-basic.html` — if the two drift apart on screen, that is itself worth a NOTES.md
  entry.

### 2. `pages/friend-requests-sent.html`

The sender's side, and the two limits that show up there:

- **The send hold.** §5.2 and §13.6: a user may not send new friend requests for
  `REQUEST_HOLD_AFTER_PROFILE_CHANGE_HOURS` = 12 after changing their profile photo or short
  bio, *"with the usual honest message stating the reason and the remaining time"* — §5.2's
  own form is *"you can send friend requests again in N hours."* Render that message.
- **The friend cap.** §5.1: any action that would push either party past `FRIEND_CAP` = 300
  fails with **a clear, honest error message — never silently**. Render that too.
- **Pending requests expire after 90 days** (§5.2). Show how a pending request reads; do not
  invent a countdown for it, since §7.5's countdown rule is about posts.

### 3. `pages/introduction-broker.html` and `pages/introduction-requested.html`

§5.5's two flows, *"both free-text-free, both requiring consent, both silent on decline"*:

- **Broker-initiated.** M selects two friends A and C who are not friends with each other.
  Each receives *"M wants to introduce you to [other party]"* plus the other's basic-tier
  profile and auto-generated context (shared hashtags, mutual friends). **Both must accept;
  mutual acceptance creates the friendship.** If either declines: *"the other candidate is
  never told an introduction was attempted or declined; M sees only that it did not complete,
  not who declined."* Render M's view of an incomplete introduction — it must not name who
  declined.
- **Requested.** A asks mutual friend M for an introduction to M's friend C. **M's decline is
  silent.**
- No free-text field on either page.

### 4. `pages/contact-card-editor.html`

§10.2 and §10.3 — the owner's own card:

- Up to `CONTACT_ITEMS_MAX` = 12 items, drawn from **phone numbers, email addresses, and
  messenger links** (links only from allowlisted official messenger domains). **The card starts
  empty**; items are added, edited and removed at any time.
- **The three-level visibility cascade, per item:** default on/off for all friends → **group
  override** → **individual override, which always wins, in either direction**. Among multiple
  groups containing the same friend, **the more restrictive setting wins: deny beats allow.**
  §10.3 gives the reason and it belongs on the page as real text: *"Accidental under-sharing is
  recoverable (see request flags); accidental over-sharing is not."*
- **Real `<input type="checkbox">` elements, styled — never `<div>`s with click handlers**
  (ARCHITECTURE §3.8, SPEC §16.3 2.1.1). Every toggle keyboard-operable, every one with an
  associated visible label.
- **The login email is separate** and appears on the card only if the user deliberately adds it
  as an item (§10.2).

### 5. `pages/contact-card-received.html`

§10.4: a friend requests the card **via a picker (no text)**, and the system **auto-replies
with exactly the version of the card that requester is permitted to see — possibly empty.**
Render the empty case too; it is a real state, not an error.

Include §10.5's request-more-access flags — "phone", "email", "other", a **one-time**
notification then a small passive flag visible to the owner only, turn-off-able by the
requester, mutable by the owner — and **label the section clearly with §10.5's own hedge:
*"may ship in v1.1"***. Do not present it as settled v1.

### 6. `pages/unfriend-confirm.html`

§5.3. Unfriending is **silent** — the unfriended party receives no notification — and the
confirmation must say what it does *not* do. Use §5.3's wording verbatim:

> *"They'll no longer see your posts or your about section. If you have friends in common, they
> can still see your name, photo and short bio — and any blog post tagged with an interest you
> both share."*

On the same page, the **block** action (§5.4): silent and **fully mutually invisible** —
friendship ends silently, neither appears in the other's discovery, suggestions, hashtag
matches, mutual-friend lists or introduction flows, neither can see the other's comments or
reactions anywhere, **neither is shown the other's existence in any list or count**, and
**block lists are private**. State plainly on the page that a user who wants the stronger
outcome wants a block — that is §5.3's own framing.

## Before you finish

Check every page, as in the earlier sessions, plus three specific to this set:

- **no free-text field on the friend-request or introduction pages** (§13.1, §5.2, §5.5)
- **every contact-card toggle is a real `<input type="checkbox">` with a visible label**, and
  the whole cascade is operable by keyboard (§16.3 2.1.1; ARCHITECTURE §3.8)
- **nothing on the sender's or broker's side reveals a decline** (§5.2, §5.5)

Plus the standing list: one `<h1>` and a unique `<title>` per page; skip link first focusable;
`lang` set; landmarks present; every `<img>` has an `alt`; every input has an associated
visible label, placeholders never labels; error messages are text, associated with their
field, and describe the fix (§16.3 3.3.1/3.3.3); no `tabindex` above 0; no `title` attribute;
no timestamp in any markup attribute; reflow at **320 px** with no horizontal page scroll.

Then: add this session's strings to `CRIB.md`, add its pages to `pages/index.html`, update
`NOTES.md`, and **print the contents of NOTES.md**. Do not touch `TODO.md` or `CHANGELOG.md`.
