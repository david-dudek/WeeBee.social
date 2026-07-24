# Platform Specification — Working Title: "The Network"

**Status:** 1.10 — DRAFT pending founder review · 2026-07-21
*(1.2.1: clarified login-email change flow in §4.6 and contact-item self-management in §10.2. 1.3, founder-initiated: commenter names link to profiles with visibility-aware rule (§8.1); clickable hashtags as viewer-scoped discover filter (§11.2, §11.4); visible timestamps and expiry countdown (§7.5); `CONTENT_TTL_DAYS` = 90 reconfirmed. 1.4, founder-initiated: theming generalized — spaces-not-content principle plus viewer override (§9.1). 1.5, founder-initiated: display-name lifecycle — blocklist screening at every name set, 90-day change cooldown, 90-day "formerly" dual display, names always rendered live from the account (§4.5, §4.5.1); global name uniqueness considered and rejected. 1.6, founder-initiated: text formatting — whitespace preservation with abuse bounds, per-post preformatted/monospace toggle with composer explainer, `POST_LENGTH_MAX` = 10,000, long-post folding at `FEED_FOLD_CHARS` = 500 in the feed and `BLOG_FOLD_CHARS` = 2,000 on profile blogs (§7.2.1, §7.7, §8.1, §9.1); `COMMENT_LENGTH_MAX` = 2,000 asserted, not yet discussed. 1.7, founder-initiated: image sizing and display — proportional scale-to-fit with click-to-expand overlay, stored images capped at a 3840 px long edge with server-side downscaling, `IMAGE_UPLOAD_MAX_MB` = 20 (§7.2.2). 1.8, founder-initiated: new §4.6.1 consolidates authentication security — codes-not-links for password reset and email change with a checkable "we never email login links" promise, multi-credential capability built in from day one with passkeys deferred as a feature, per-account/per-IP login throttling, Argon2id password hashing, breach-password rejection at registration and password change, SPF/DKIM/DMARC at `p=reject`; CAPTCHA and defensive domain hygiene both considered and declined for v1; §4.1, §4.6, §12, §13.6, §16 cross-referenced; constants `RESET_CODE_TTL_MINUTES`, `RESET_CODE_LENGTH`, `LOGIN_ATTEMPT_LIMIT`, `LOGIN_LOCKOUT_MINUTES` added (§14). 1.9, founder-initiated: new §15.5 records the end-to-end-encryption and content-signing question — full E2EE and per-post signing considered and deferred for v1 (web-app delivery trust, password-reset incompatibility, and the break of server-side moderation/EXIF-stripping/allowlist enforcement), encryption-at-rest adopted instead, and the honest trust model stated; §16 Non-Goals and §13.1 cross-referenced. 1.10, founder-initiated: **accessibility — new §16 makes WCAG 2.1 Level AA conformance a requirement of the same rank as the tracking ban**, with per-area requirements (semantics, keyboard, contrast, reflow, images and alt text, forms/errors/status messages, time limits, motion, targets), the preformatted-post reflow exemption documented honestly, accessibility overlays and separate "accessible versions" banned outright, and verification plus an accessibility statement and a report channel required; supporting principle added (§1.3); §7.2.1, §7.2.2, §9.1, §13.5 cross-referenced; constant `ALT_TEXT_MAX` = 1,000 added (§14); former §16 Non-Goals → §17 and former §17 Downstream Documents → §18, with all cross-references updated.)*
**Purpose of this document:** The single authoritative description of what the platform is and how every feature behaves. It is written to be self-contained: a developer or an AI coding model with no access to prior conversations must be able to build from this document alone. Architecture, technology choices, and build steps live in separate documents (see §18).

---

## 1. Mission and Design Philosophy

### 1.1 Purpose
A digital tool for maintaining and creating positive real-life social relationships:
1. Help people stay in touch with existing friends and family.
2. Help people form new friendships through mutual friends and shared interests.
3. Be structurally resistant to commercial and political manipulation — by design, not by moderation.

### 1.2 The core thesis: no concept of reach
The reshare/repost button is the "original sin" of social media. Once content can propagate beyond its author's chosen audience, virality exists, and virality is the mechanism that manipulation exploits. **This platform has no concept of reach. Nothing can go viral.**

**The No-Reach Test (apply to every current and future feature):** *Can this feature cause content to travel beyond the audience its author deliberately chose, or let a person be seen by people with no real social connection to them?* If yes, the feature is wrong for this platform.

### 1.3 Supporting principles
- **Pull over push.** Broad audiences must come to you (profile visits); push is reserved for small, hand-picked audiences.
- **Bounded everything.** Friends, audiences, groups, images, invites, hashtags — every quantity has a hard cap, implemented as a named configuration constant (§14). Caps may be raised later; they are never lowered (lowering strands users above the new limit).
- **Data minimalism.** The platform is a communication tool, not an archive and not a data harvester. Content self-destructs (§7.5); collection is minimal; tracking is banned absolutely (§15.2).
- **Humans, vouched.** Every account enters through a personal invitation from an existing member. There are no strangers; every user is at most one trusted hop from someone who vouched for them.
- **The platform never infers.** No behavioral profiling, no algorithmic ranking, no machine guesses about who matters to you. Users state their intent; the platform obeys it.
- **Usable by everyone it invites.** Every surface conforms to WCAG 2.1 Level AA (§16). On an invite-only network of real friends and family, an inaccessible page does not inconvenience a user — it excludes a specific person from the specific people who vouched for them.

---

## 2. Project Context

- **Stage:** "Prototype now, public later." First target: a working platform for the founder and a small circle of real users. Architecture decisions must not need discarding if the platform later grows.
- **Team:** Solo founder (IT professional, not a professional developer) building with AI assistance. All documents downstream of this spec must be explicit enough for less capable AI models to execute.
- **First interface:** A simple, mobile-friendly **web application**. No native mobile app in v1. No public (logged-out) pages except login/registration/invite-acceptance.
- **Explicitly rejected:** the AT Protocol and all blockchain/decentralized hosting (incompatible with the fully-private design and guaranteed deletion; infeasible solo). Portability is provided by data export (§4.9) instead.

---

## 3. Definitions

| Term | Meaning |
|---|---|
| **Friend** | A user with whom a mutual, accepted friendship link exists. All friendships are symmetric. |
| **Mutual friend (of A and B)** | A user who is a friend of both A and B. |
| **Friend-of-friend (FoF)** | A user who shares at least one mutual friend with you but is not your friend. Exactly one hop; never more. |
| **Group** | A named, user-created list of that user's friends, used for audience selection. |
| **Feed post** | A post pushed to a hand-picked audience of ≤ `POST_AUDIENCE_MAX` friends; appears in those friends' feeds. |
| **Profile post** | A post visible to all the author's friends, living only on the author's profile page ("the blog"); friends receive only a notification. |
| **Basic tier (profile)** | The subset of profile information visible to FoFs as well as friends (§9.2). |
| **Contact card** | A user's collection of contact methods, shared under a per-viewer visibility cascade (§10). |
| **Invite tree** | The permanent record of which account invited which. |

---

## 4. Accounts and Identity

### 4.1 Registration — invite-only, permanently
- The **only** way to create an account is by redeeming a personal invitation from an existing user. This is a permanent identity principle, not a launch-phase gate. Slow growth is accepted and intended.
- An invite is a single-use link/code sent by email. Asserted default: invites expire after 14 days (`INVITE_EXPIRY_DAYS`); expired invites return to the sender's budget.
- Redeeming an invite requires: a working email address (verified by a numeric code, §4.6.1), a password (screened against known-breached passwords, §4.6.1), a display name, and an attestation of being 18 or older.
- **Registration collects nothing else.** No phone number, no legal name, no address.
- When an invite is accepted, inviter and invitee automatically become friends.

### 4.2 Invite budgets
- Maximum banked invites per user: `INVITE_BANK_MAX` = 5.
- Replenishment: +1 per month, never exceeding the bank max.
- New accounts start with `INVITE_NEW_ACCOUNT` = 2 (prevents a newly-invited bad actor from immediately chain-inviting).

### 4.3 Invite tree
- The platform permanently records which account invited which.
- **v1 attaches no consequences** to the tree. It exists for forensics and future analysis (e.g., detecting clusters of abusive accounts). Any future accountability mechanism (e.g., reducing invite budgets of users whose invitees are banned) is a separate, later decision.
- When an account is deleted, its node in the tree is replaced by an **anonymized stub** ("deleted account #N invited X, Y"). No personal data survives; the tree's shape does. This prevents delete-and-rejoin laundering of invite history.

### 4.4 Age
Minimum age is **18**. Enforced by attestation at signup (no ID collection). Rationale: minors impose duty-of-care and verification obligations a solo operator cannot meet. May be lowered later; the reverse would be hard.

### 4.5 Names and identity
- Users choose a **display name**: freely chosen, **no uniqueness requirement**, changeable under the rules of §4.5.1. Login is by email address.
- There is **no real-name mandate**. Vouched entry makes names socially self-policing. For moderation purposes, identity is the account and its invite ancestry — never the name.
- There is **no global user search by name.** People are found through mutual friends and hashtag matches only (§11).
- **Screening (v1.5):** every time a name is set — at registration and at every later change — it is checked against an operator-curated blocklist (`NAME_BLOCKLIST`: slurs and obviously abusive strings) and rejected at save time with an honest message. There is **no human pre-approval** of names; the report system (§13.2) and invite ancestry are the backstop for what a list cannot catch.
- **Global name uniqueness: considered and rejected (2026-07-08).** Uniqueness would create a global namespace on a platform that deliberately has none (no search, no handles, no mentions), force real-name collisions ("the fifth John Smith") into unrecognizable handles, act as a privacy oracle (any member could probe whether a name exists anywhere on the network, beyond their FoF bubble), and open an impersonation window via recycled old names after changes. Anti-impersonation is provided instead by the graph: requests only from FoFs, always with mutual-friend context, and moderation identity tied to the account, never the name.

### 4.5.1 Changing a display name (v1.5)
- A display name may be changed only when at least `NAME_CHANGE_COOLDOWN_DAYS` = 90 days have passed since **account creation or the last name change**, whichever is later. Uniform clock, no exceptions (a signup typo waits out the same cooldown, or is worn honestly under the dual display below).
- **Dual display:** for `NAME_TRANSITION_DAYS` = 90 days after a change, the user's name renders **everywhere it appears** — posts, comments, profile header, reaction name-lists, mutual-friend context, discovery, requests, introductions, notifications — as "**NewName** (formerly OldName)". After the window, the old name disappears entirely.
- **Names are never stored on content.** Content records only the author's account; every surface renders the name live through one shared helper (which appends the "formerly" tag during the transition window). Old posts therefore show the new name immediately, tagged — content never shows a stale name.
- **Invariant:** `NAME_CHANGE_COOLDOWN_DAYS` must always be ≥ `NAME_TRANSITION_DAYS`, so a previous transition has fully finished displaying before the next can begin — at most two names (current + one previous) ever exist on screen, and no "formerly"-chains can occur.
- There is **no separate name-change notification**: the dual display *is* the announcement, shown exactly where the person appears, for longer than any of their pre-change content survives (`NAME_TRANSITION_DAYS` ≥ `CONTENT_TTL_DAYS` window relationship: every post ever seen under the old name expires before the tag comes off).

### 4.6 Authentication and recovery
- Password login; email-based password reset completed with a numeric **code, not a login link** (§4.6.1).
- Every account has **exactly one login email address** at all times (it is required for password reset and the lifecycle emails of §4.8/§4.7). It can be **changed but never removed**: the user enters a new address, verifies it via a numeric code sent to that new address (§4.6.1), and only then does it replace the old one (a notice is sent to the old address). The login email is a credential, not an identifier: internally, accounts are identified by a permanent internal ID, so changing email affects nothing else.
- (Parked idea, not v1: "social recovery" via friends vouching.)

### 4.6.1 Credential security and anti-phishing (v1.8)
Authentication is the one place where the platform's structural anti-abuse design (§13.1) does not by itself protect users: a password can be phished on a look-alike domain or guessed by machines, entirely off-platform. The measures here defend the login and recovery flows specifically. They address two separate problems with two separate answers — **anti-phishing** (deception on someone else's domain) and **login-endpoint defense** (brute force and credential stuffing against our own server).

**Why most phishing vectors are already closed.** The platform gives an attacker almost no in-platform way to deliver a deceptive link: no direct messages (§10.1); no free text in friend requests, introductions, or reactions; a URL allowlist on every post and comment (§7.2); and no public registration (§4.1) — an unsolicited "click to join" is inherently suspicious. The realistic remaining vector is **email**, the one channel where the platform legitimately sends links (invites, verification, recovery, inactivity notices).

**Codes, not links, for recovery and email changes.**
- Password reset and login-email change (§4.6) are completed with a **short, single-use, time-limited numeric code** (`RESET_CODE_TTL_MINUTES`, `RESET_CODE_LENGTH`) that the platform emails and the user types into a page they reached **by navigating to the site themselves** — never by clicking a link in the email. For a password reset, the user opens the reset page from the login screen and enters the code there; for an email change, the code is sent to the new address and entered back into the already-open settings page (which also verifies the new address). Email verification at registration works the same way (§4.1).
- **Invitations remain links (§4.1), and only invitations** — a brand-new user has no session and no page open, so a link is unavoidable there. Every *other* action email either carries no link or uses a code.
- **The checkable promise.** Because recovery never uses a login link, the platform makes a plain, memorable commitment: *"[Platform] will never email you a link to log in or reset your password — only a code you type in yourself,"* shown at the relevant touchpoints (login, reset, help). Its value is that it makes **any** look-alike "click here to log in" email self-evidently fake, no matter how convincing the sending domain — a defense that does not depend on the user scrutinizing a URL.

**More than one kind of credential (capability now, passkeys later).**
- v1 ships **password login only.** But the credential data model is built from the start to hold **more than one credential type per account**, so a phishing-resistant second type can be added later without reworking the auth layer (per §2: architecture must not need discarding).
- The intended second type is **passkeys (WebAuthn)**, cryptographically bound to the site's origin: a passkey registered on the real domain does not function on a look-alike, and the browser will not even offer it. This is the only measure here that structurally defeats a **real-time proxy phish** (an attacker relaying the live login page). For the record: **ordinary TOTP two-factor codes do _not_ defeat that attack** — a proxy relays a 6-digit code as readily as a password; this is why passkeys, not TOTP, are the chosen structural fix. Passkeys are **deferred as a feature** for the solo prototype (device-loss recovery and cross-device UX are real work); only the capability is required in v1.
- **Password managers** are encouraged at onboarding: they refuse to autofill on the wrong origin, giving the user a free, silent phishing signal.

**Login-endpoint defense (brute force and credential stuffing).** These are attacks on our own server, so they are ours to fix directly:
- **Throttling with lockout.** Login attempts are rate-limited **per account _and_ per source address**, with exponential backoff and temporary lockout (`LOGIN_ATTEMPT_LIMIT`, `LOGIN_LOCKOUT_MINUTES`), extending the rate-limit framework of §13.6. A failed-login flood is slowed to uselessness without ever challenging a human.
- **Slow password hashing.** Passwords are stored with a deliberately slow, memory-hard hash (**Argon2id**), so an attacker who ever obtained the database cannot cheaply brute-force the stored hashes.
- **Breach-password rejection** at registration and at every password change: the chosen password is checked against the public corpus of known-breached passwords via a **k-anonymity range query** — only the first five characters of the password's hash leave our server; the full password and the user's identity never do. It is a server-to-server call, not a browser script, so it is fully compatible with the tracking ban (§15.2). A known-breached password is refused with an honest explanation. (That hash prefix is a lookup index only; passwords are never stored this way — see the Argon2id rule above.)

**Email domain authentication.** The sending domain publishes **SPF, DKIM, and DMARC at `p=reject`** from day one. This does not stop look-alike domains, but it stops anyone spoofing the platform's *real* domain in email — a free, standard baseline. (Mechanics: ARCHITECTURE §7, build-plan Step 5.5.)

**Security-event emails.** New-device login, password change, and email change generate account/security notifications (§12); these shrink the window in which a compromise goes unnoticed. They mitigate, not prevent.

**CAPTCHA — considered and rejected (2026-07-21).** No CAPTCHA (or reCAPTCHA / hCaptcha / Turnstile) is adopted, for three reasons: (1) it does nothing against phishing — it is an anti-automation control on our own server, not a defense against a deceptive site elsewhere; (2) the mainstream options conflict with the absolute ban on third-party scripts and behavioral profiling (§15.2) — reCAPTCHA v3 in particular scores users on browsing behavior; (3) the problem CAPTCHA usually solves — signup spam and content scraping — does not exist here (no public signup, no public content). The login-endpoint threats it is sometimes stretched to cover are better handled by the throttling, hashing, and breach-check measures above. **If** a human-challenge mechanism is ever genuinely needed, the only kind compatible with this platform's privacy principles is a **self-hosted proof-of-work** challenge (e.g., Altcha, mCaptcha): first-party, no tracking, no third-party scripts, accessible.

**Defensive domain registrations and certificate-transparency monitoring — not in v1 (2026-07-21).** Buying look-alike/typo domains and watching public certificate-transparency logs for the brand string are harm-reduction measures aimed at a *public* brand worth impersonating. With the network limited to the founder's vouched circle there is nothing yet to phish against, so v1 does neither. Both — the free crt.sh certificate-transparency alert in particular — are to be reconsidered before any public phase (§15.1), where the calculus changes.

### 4.7 Account deletion (user-initiated)
- Deletion request → account immediately deactivates (invisible to all users) → **30-day grace period** (`DELETE_GRACE_DAYS`) during which the user can log in to cancel → after grace, **full erasure** of all data: posts, comments, reactions, images, contact card, groups, friendships, profile.
- Sole exception: the anonymized invite-tree stub (§4.3) and content-free moderation counters (§13.4).
- Deletion of a user removes their comments and reactions everywhere.

### 4.8 Inactivity deletion
- Accounts with no login for **24 months** are deleted (full erasure as §4.7).
- Warning emails at 6, 12, 22, and 23 months of inactivity. The early ones are gentle "your account is dormant" notes; the final two are explicit deletion warnings.

### 4.9 Data export
Every user can download a complete, well-structured copy of their data (profile, posts, comments they authored, friend list, groups, contact card, images) in an open format (JSON + image files). This serves three purposes: GDPR compliance, "credible exit" (users are never hostage), and any future migration.

### 4.10 Death and third-party requests
- No memorialized state. A third party (e.g., family member) may request deletion of a deceased user's account through the report/contact channel; the operator verifies plausibility manually and deletes.
- Inactivity deletion (§4.8) eventually covers unreported cases.

---

## 5. Friendship

### 5.1 The friend cap
- Hard ceiling: `FRIEND_CAP` = **300 friends** per user.
- Any action that would push either party past the cap (request, introduction, invite acceptance) fails with a clear, honest error message — never silently.

### 5.2 Friend requests
- Only a **FoF** (shares ≥ 1 mutual friend) can send a friend request. Strangers cannot; their path is a real-world meeting or an introduction (§5.5).
- Requests carry **no free text**. The recipient sees: the requester's basic-tier profile (§9.2), the mutual friends they share, and shared profile hashtags. The system generates this context; the requester writes nothing.
- Recipient accepts or declines. **Declines are silent** — the requester is never notified; the request simply never resolves for them.
- Asserted default: after a decline, the same requester cannot re-request the same person for 90 days.

### 5.3 Unfriending
Silent. The unfriended party receives no notification. Effects are immediate: each loses access to the other's friends-only content, feeds stop receiving the other's posts, and each disappears from the other's audience lists (see snapshot rules, §7.4).

### 5.4 Blocking
Silent and **fully mutually invisible**. When A blocks B (order irrelevant to effect):
- Any friendship between them ends (silently).
- Neither appears in the other's discovery, suggestions, hashtag matches, mutual-friend lists, or introduction flows.
- Neither can see the other's comments or reactions anywhere, including on shared friends' posts. (Others still see those comments; invisibility is only between the pair.)
- Neither can send the other a friend request, introduction, or contact-card request.
- Neither is shown the other's existence in any list or count.
Block lists are private. Unblocking is possible by the blocker only.

### 5.5 Introductions
Two flows, both free-text-free, both requiring consent, both silent on decline:

**(a) Broker-initiated.** User M selects two of their friends, A and C, who are not friends with each other and neither of whom blocks the other. A and C each receive: "M wants to introduce you to [other party]" plus the other's basic-tier profile and auto-generated context (shared hashtags, mutual friends). **Both must accept; mutual acceptance creates the friendship.** If either declines: the other candidate is never told an introduction was attempted or declined; M sees only that it did not complete, not who declined.

**(b) Requested.** User A asks mutual friend M for an introduction to M's friend C. A can only point at a C that A can see (in practice: hashtag-matched FoFs, §11.3, or people A knows offline who appear as M's mutual friends with A — by definition already A's friends, so effectively: hashtag matches). If M agrees, flow (a) runs with A's side pre-accepted; only C decides. M's decline is silent.

(Parked idea, not v1: an opt-in "friends may show my name for introduction purposes" toggle to widen flow (b).)

---

## 6. Groups

- A user organizes friends into named **groups**. A friend can be in zero, one, or many of that user's groups. Groups are private to their owner; members never know they are in one.
- Max members per group: `GROUP_SIZE_MAX` = **30** (matches the feed-post audience cap, so any group is always a valid post audience).
- The UI warns when an edit would exceed the cap and refuses it.
- **Audience-save suggestion (the demoted "close friends" idea):** if a user repeatedly hand-picks the same audience for feed posts, the composer may offer "Save this selection as a group?" This is *memory of the user's explicit choices*, never behavioral inference about relationship strength. The platform must not auto-create, auto-populate, or auto-modify groups.

---

## 7. Posts

### 7.1 The two post types
| | **Feed post** | **Profile post** |
|---|---|---|
| Audience | Hand-picked friends and/or groups, max `POST_AUDIENCE_MAX` = **30** recipients | All the author's friends (up to 300) |
| Delivery | **Push**: appears in each recipient's feed | **Pull**: lives only on the author's profile blog; friends receive only a notification ("David updated his profile") |
| Hashtags | Ranking signals only (§11.2) | Gate FoF visibility (§11.3) |
| Pinnable | No | Yes (§7.6) |

### 7.2 Content rules (both types)
- Plain text, plus **at most one image** per post.
- URLs are permitted **only** from an operator-curated allowlist of trusted service domains (e.g., Google Maps, Evite, YouTube, SoundCloud, and official messenger link domains). Any other URL is rejected at composition time with an explanation. The allowlist is a maintained operational artifact, not user-configurable.
- Images: EXIF metadata (including GPS location) is **stripped on upload, always**. Uploads are re-encoded/resized server-side.
- No video or audio **hosting**, no polls. Links to allowlisted media services (YouTube, SoundCloud, etc.) are permitted **as plain clickable links only** — never auto-embedded as players or preview cards, because third-party embeds load the external service's scripts and trackers into the page, violating the tracking ban (§15.2). (Parked: privacy-safe "click-to-load" embeds — a placeholder that connects to the external service only after the viewer explicitly clicks it.)

### 7.2.1 Text formatting, whitespace, and length (v1.6)
Browsers collapse whitespace by default; the behaviors below are therefore explicit requirements, not defaults to rely on.

- **Whitespace preservation (normal posts).** Authors' deliberate spacing survives, bounded against abuse. Normalization happens **once, silently, at save time** — what is stored is exactly what every viewer sees, and the composer never nags about whitespace:
  - Line breaks are preserved as typed.
  - Up to **one blank line** between paragraphs is preserved; longer runs of blank lines collapse to one.
  - Up to **two consecutive spaces** are preserved (sentence spacing survives); longer runs collapse to two.
  - Leading and trailing whitespace on the post as a whole is trimmed.
- **Preformatted posts (per-post toggle).** The composer offers a per-post **"preformatted" toggle** for text tables, diagrams, and ASCII art. A preformatted post renders in a **monospace font** and preserves runs of spaces **exactly** (the space-collapsing rule above does not apply; blank-line runs still collapse, at a looser bound of **three**). Long lines **never soft-wrap** — on screens narrower than the content (a phone shows ~40 monospace characters) the post scrolls horizontally instead, because wrapping would destroy the artwork. (This is the platform's single documented exception to the reflow requirement of §16.3, permitted by WCAG 1.4.10's two-dimensional-layout exemption; the scrolling region must be keyboard-scrollable and named, and the explainer must say so.) The toggle is accompanied by a **brief explainer, linked directly from the composer**, stating what the mode is for and its shortcomings (exact spacing, no wrapping, horizontal scrolling on narrow screens). Monospace here is **structural, not decorative** — it is part of the content, like the one-image allowance, not part of any theme; see §9.1 for the interaction with viewer theming. Comments have no preformatted toggle (§8.1).
- **Length caps.** A post may contain at most `POST_LENGTH_MAX` = **10,000 characters** (roughly 1,500–2,000 words — genuine long-form writing is welcome; the cap is an abuse bound required by the bounded-everything principle (§1.3), not a style nudge). A comment may contain at most `COMMENT_LENGTH_MAX` = 2,000 characters (asserted default, operator-tunable). Exceeding a cap produces an honest character count in the composer; text is never silently truncated.

### 7.2.2 Images: size and display (v1.7)
Applies to **every uploaded image** — post images, gallery images (§9.4), and the profile photo — and extends the existing upload pipeline of §7.2 (EXIF stripping, server-side re-encoding).

- **Upload and storage.** Uploads are accepted up to `IMAGE_UPLOAD_MAX_MB` = 20 (rejected above that with an honest message). The server **downscales** any image whose long edge exceeds `IMAGE_MAX_PX` = **3,840 pixels** to that size, preserving aspect ratio — full 4K-wallpaper quality is kept; nothing larger is stored. Normal phone photos (12–48 MP, larger than 4K) are therefore never rejected for their dimensions — they are accepted and scaled down. The server may additionally store smaller derived renditions of the same image for efficient display; the 3,840 px version is the canonical "full size."
- **Display: scale to fit, click to expand.** On every reading surface (feed, profile blog, gallery, discover), an image is **proportionally scaled** — never cropped, never stretched — to fit within the surface's layout (in the feed, also within a bounded height, so one tall portrait photo cannot dominate the screen the way long-post folding prevents for text, §7.7). Clicking/tapping an image opens the **full-size version in an in-app overlay** (dismissable, with zoom/pan when the image is larger than the screen) — a proper modal dialog per §16.3: keyboard-openable, focus-trapped, Escape-dismissable, focus restored on close. Every image carries uploader-authored alternative text or an explicit "decorative" mark (§16.3). The overlay is an in-app view, not a raw file URL — image access follows the same no-deep-links, permission-checked rule as everything else (§9.3).

### 7.3 Audience selection (feed posts)
- The composer lets the author pick individual friends and/or groups; the resolved recipient set must be ≤ 30. Exceeding it produces a clear warning and requires narrowing — recipients are never silently dropped.

### 7.4 Audience semantics (both types)
- The audience is **snapshotted at posting time**, and access additionally requires **current friendship** at viewing time. Formally: viewer may see a post iff (viewer ∈ posting-time audience) AND (viewer is currently the author's friend) — plus the FoF hashtag exception in §11.3. Unfriending or blocking therefore removes access to all past posts. Friends added *after* a post never see that feed post; new friends *do* see existing profile posts (profile posts' audience is "all current friends").

### 7.5 Expiry — nothing outlives 3 months
- **Every post and every comment is permanently deleted `CONTENT_TTL_DAYS` = 90 days after creation.** No archive, no soft-delete, no operator copy (sole exception: frozen moderation copies, §13.3).
- Deletion includes attached images and all comments/reactions on the expired post.
- Authors can delete their own posts at any time before expiry (immediate, permanent).
- **Visible timestamps and countdown:** every post and comment displays its posting date and time. When an unpinned post has `EXPIRY_COUNTDOWN_DAYS` = 14 or fewer days left, a countdown to deletion is shown to everyone who can see it (ephemerality made visible — the anti-archive stance as interface). Pinned posts show a "pinned" marker instead.

### 7.6 Pinning
- A user may **pin up to `PIN_LIMIT` = 10 of their own profile posts**. Pinned posts are exempt from expiry for as long as they remain pinned; unpinning a post older than 90 days deletes it. Feed posts can never be pinned. Pinning is the deliberate, editorial act of preservation — the only one on the platform.

### 7.7 The feed
- A user's feed contains, in **strict reverse-chronological order**: feed posts they are in the audience of, profile-update notifications from friends, and system notifications (friend requests, introductions, contact-card events, warnings).
- **No algorithmic ranking, ever. No suggested content, no inserted people, no ads, nothing the user did not subscribe to by friendship.** The feed is a mailbox, not a machine.
- **Long-post folding (v1.6):** a post longer than the surface's threshold is shown folded — the first characters up to that threshold (cut at a whitespace boundary) plus a "read more" control that expands the post **in place** — so one essay does not push everything else off the screen. Thresholds per reading surface: **`FEED_FOLD_CHARS` = 500** in the feed (a shared space where many authors compete for the screen), **`BLOG_FOLD_CHARS` = 2,000** on a profile blog (§9.1; the reader deliberately visited this author's own space). Folding is display-only: it never changes what is stored or who can see it. A post opened directly (e.g., from a notification) is always shown in full.

---

## 8. Comments and Reactions

### 8.1 Comments
- Who can comment = who can see the post (§7.4, §11.3). **A comment is visible to exactly the people who can see the post — never more.** Nothing about commenting propagates content anywhere.
- Consciously accepted consequence: on a profile post, a commenter's words are readable by the author's other friends, who may be strangers to the commenter (bounded: ≤ 300 vouched humans; this is also a deliberate surface where people meet through mutual friends).
- **Attribution:** every comment displays its author's display name and timestamp. The name **links to the commenter's profile when the viewer has at least basic-tier access to that commenter** (friend or FoF, §9.2); for a viewer with no connection to the commenter (possible on hashtag-gated posts, §11.3, where two viewers of the same post may be strangers to each other) the name renders as plain text, not a link.
- **Flat** — one linear list per post; no nested replies in v1.
- Same content rules as posts (§7.2, §7.2.1) except: no images in comments, no preformatted toggle, and the smaller `COMMENT_LENGTH_MAX` = 2,000 length cap. Whitespace normalization applies as for normal posts.
- Comment authors can delete their own comments. **The post's author can delete any comment on their post** (host's rules — the cheapest moderation tool).
- Comments expire with their post, or at their own 90 days, whichever comes first.

### 8.2 Reactions (no likes)
- There are **no like buttons, no counters, no public reaction displays of any kind.**
- A user may attach **one reaction per post or comment**, chosen from a fixed, operator-curated picker of ~6 warm phrases (`REACTION_SET`; e.g., "Agreed!", "Love it!", "So proud!", "Thinking of you", "Congrats!", "Ha!"). Changeable or removable at any time. No free text, no arbitrary emoji.
- **Reactions are visible only to the author of the reacted-to content, shown as names, never as numbers** ("Alice: Love it! · Mom: So proud!"). Other viewers see nothing — no counts, no indicators. This is deliberate: warmth without scorekeeping; no validation economy.

---

## 9. The Profile Page

### 9.1 Structure and theming
Fixed layout (no freeform customization), with limited theming: font choice and color scheme from operator-curated sets (`THEME_SET`; **every scheme must meet the WCAG 2.1 AA contrast ratios of §16.3 in every combination in which it can appear** — this is why theming is curated rather than freeform). Sections, top to bottom: identity header (photo, display name, one-line bio, hashtags) → pinned posts → static about section (extended bio) → image gallery → the blog (the owner's profile posts, newest first, filtered per viewer).

**Theming attaches to spaces, never to content (v1.4):**
- A user themes their **own app view** — feed and all reading surfaces — for themselves only.
- A user themes their **profile page**; visitors see that theme (your living room, your wallpaper).
- Comments and feed posts **never carry their author's theme** — they render in the theme of the surface they appear on (a comment is a guest in the host's house). Rationale: sender-styled content invites an attention arms race (loudness as reach) and degrades readability; the feed is the reader's mailbox (§7.7).
- **Viewer override:** an "always use my own theme" setting renders every page, including friends' profiles, in the viewer's own theme (accessibility and consistency).
- **Preformatted posts are exempt (v1.6):** a post's preformatted/monospace rendering (§7.2.1) is **structural content, not theming**, and survives every theme, including the viewer override — rendering ASCII art or a text table in a proportional font would destroy it. Only the monospace-ness is exempt; colors and everything else still follow the surface's theme.
- The blog applies long-post folding per §7.7, at the blog threshold (`BLOG_FOLD_CHARS` = 2,000).

### 9.2 Visibility tiers
| Viewer | Sees |
|---|---|
| **Friends** | Everything: both tiers, the full blog (all profile posts), gallery, extended bio. |
| **FoFs (any mutual friend exists)** | **Basic tier only:** display name, profile photo, one-line bio, profile hashtags, and the specific mutual friends they share with the owner ("knows Alice and Tom"). |
| FoFs with a **matching profile hashtag** | Basic tier **plus** the owner's profile posts tagged with a shared hashtag (§11.3). |
| Everyone else (no mutual friend) | Nothing. The profile does not exist for them. |

### 9.3 Access rules
- No profile, post, or image is ever accessible without login. **No deep links:** URLs must not function as shareable pointers to profiles or posts; internal identifiers must be non-guessable, and every request is permission-checked against the viewer (a leaked URL shows a stranger nothing).
- Profile updates (new profile post, changed bio, new gallery image) generate **only a notification** to friends. Content is never pushed.

### 9.4 Limits
- Gallery: `GALLERY_MAX` = 8 images (plus the profile photo). EXIF stripped (§7.2); sizing and display per §7.2.2.
- Profile hashtags: `PROFILE_HASHTAG_MAX` = 10.

### 9.5 Preview-as (required feature)
The owner can view **both their profile page and their contact card** exactly as any chosen friend, or a generic FoF, would see them. With three-layer visibility rules, users must be able to verify who sees what.

---

## 10. Contact Cards (there is no DM system)

### 10.1 Principle
The platform has **no free-text direct messaging**. Person-to-person conversation belongs on channels users already trust (phone, email, messengers). The platform's job is the *introduction and the handoff*, via a structured contact card.

### 10.2 Card contents
- Up to `CONTACT_ITEMS_MAX` = 12 items total, drawn from: phone numbers, email addresses, and messenger links (links only from the allowlisted official domains of recognized messengers, e.g. WhatsApp/Signal/Telegram link domains — phishing-proofing).
- The card starts empty; users **add, edit, and remove items at any time** (the login email of §4.6 is separate and appears on the card only if the user deliberately adds it as an item).
- Every item is individually toggleable per the visibility cascade below. A card may expose different items to different friends. Non-friends never see any of it.

### 10.3 Visibility cascade (per item)
1. **Default:** each item is on or off for "all friends."
2. **Group override:** any group may override an item on or off for its members.
3. **Individual override:** a per-friend setting that **always wins**, in either direction.
Conflict rule between multiple groups containing the same friend: **the more restrictive setting wins** (deny beats allow). Accidental under-sharing is recoverable (see request flags); accidental over-sharing is not.

### 10.4 Requesting a card
- A friend requests the card via a picker (no text); the system **auto-replies** with exactly the version of the card that requester is permitted to see (possibly empty).

### 10.5 Request-more-access flags *(may ship in v1.1)*
- If the received card is insufficient, the requester can toggle a request for more: "phone," "email," or "other." The owner gets a **one-time** notification; thereafter a small passive flag appears (for the owner only) next to the requester's name/profile/comments.
- The requester can turn their flag off at any time. The owner can mute the flags in feeds/comments; the flag remains visible on the requester's profile page (to the owner) as long as the requester keeps it on. No repeat notifications, no nagging.

---

## 11. Discovery — meeting people without reach

### 11.1 The hard boundary
All discovery is limited to **friends-of-friends: exactly one mutual friend in between. This ceiling is permanent.** Two-hop visibility with a shared hashtag is qualitatively safe because every viewer shares a vouching human with the author; at three hops no such person exists and small-world math makes audiences explode toward the whole network. Any future proposal to extend the radius fails the No-Reach Test by definition.

### 11.2 Hashtags
- **Hashtags are never free-typed.** All hashtags — on profiles and in posts — are chosen from a single operator-curated, platform-wide **interest vocabulary** (`HASHTAG_VOCAB`) via a searchable picker. Rationale: free-typed tags fragment the same interest across synonyms (#hiking / #hikes / #trailwalking), silently preventing the matches the feature exists to create; curation also blocks abusive or coded tags. Users may submit new-tag suggestions for operator review (§13.5).
- Users may put up to 10 vocabulary hashtags on their **profile** (interests: #hiking, #jazz) — visible at the basic tier.
- Hashtags may also be written in **posts**. On **feed posts** they are decorative/ranking signals only — they never change the audience. On **profile posts** they act as the FoF visibility gate (§11.3).
- **Hashtags are matching signals, never global navigation: there are no global hashtag feeds, no hashtag search, no network-wide "see all posts tagged #x" anywhere on the platform.** The only hashtag-driven views are the FoF-scoped ones below and the viewer-scoped tag filter of §11.4.
- **Clickable hashtags (v1.3):** clicking a hashtag anywhere opens the **discover page filtered to that tag** (§11.4). This passes the No-Reach Test because it only reorganizes what the viewer can already see — it never widens any audience and does not loosen the §11.3 gate.

### 11.3 Hashtag-gated FoF visibility (symmetric consent)
A profile post tagged #x is visible to a viewer V (beyond the author's friends) iff **all** hold:
1. V is a FoF of the author (≥ 1 mutual friend, no block between them), and
2. V has #x among their own **profile** hashtags (viewer declared the interest), and
3. the post carries #x (author declared it discoverable by tagging it).
Such viewers may also **comment** on that post (author-delete and block are the safety net). Access is evaluated live: if the tag is removed from either side, or the mutual friendship lapses, access ends.

### 11.4 The discover page (pull-only)
One dedicated page the user must deliberately visit. It contains:
- **People suggestions:** FoFs, ranked by shared mutual friends and shared profile hashtags, each shown with auto-context ("knows Alice and Tom · shares #hiking").
- **Matched posts:** hashtag-gated FoF profile posts per §11.3.
- **Tag filter (v1.3):** the discover page can be filtered to a single hashtag (reached by clicking that tag anywhere). The filtered view shows: connected people (friends and FoFs) who carry the tag on their profile, and already-visible tagged profile posts — friends' posts always; FoFs' posts only when the §11.3 conditions hold (in particular, the viewer must carry the tag too). The filter reveals nothing the unfiltered rules don't already permit; it is aggregation of the viewer's existing visibility bubble, consciously accepted as serving the friend-discovery mission.
**Nothing from discovery ever appears in the feed.** No push, no notification, no "someone viewed you."

### 11.5 Friend-list visibility
On a friend's profile, a viewer sees only: their **mutual friends** with that person, plus that person's hashtag-matched non-mutual friends (per §11.3 matching between viewer and those friends). Full friend lists are never exposed.

---

## 12. Notifications

In-feed notifications (§7.7) plus optional email for: friend requests, introduction proposals, invite acceptance, contact-card requests and one-time access-request alerts, profile-update notices from friends, inactivity warnings (email only, §4.8), and account/security events (new-device login, password change, email change — §4.6.1). No notification ever includes post content beyond what the recipient may see; no engagement-bait notifications ("you have memories!") exist.

---

## 13. Safety and Moderation

### 13.1 Layers
1. **Structural** (does most of the work): invite-only vouched entry, no reach, bounded audiences, no strangers, no free-text vectors (requests, intros, reactions are all text-free), URL allowlist.
2. **User-level:** silent unfriend (§5.3), silent full block (§5.4), author-deletes-comments (§8.1).
3. **Operator-level:** the report system below.

### 13.2 Reporting (v1 = stub)
Every post, comment, and profile has a "report" action → lands in a private operator moderation queue with reporter, target, and a frozen copy. v1 workflow is simply: the operator reviews and acts manually (delete content, warn, or ban an account). Formal policies/appeals are deferred.

### 13.3 Reported-content lifecycle
- Reported content **stays live** while the report is open (mass-report censorship is not a weapon here).
- The **frozen copy** exists only in the moderation queue, never visible to users, and survives expiry/author-deletion solely so the report can be judged.
- Purge rules: report dismissed → frozen copy purged immediately. Report upheld → live content removed; frozen copy purged 30 days later (appeal window). **Hard cap: any frozen copy is purged at 90 days** even if unreviewed.

### 13.4 What persists
Only content-free counters: "account X: N upheld reports," linked to the invite tree for forensics. Never the content itself.

### 13.5 Operator request channels
Beyond abuse reports, users need structured ways to ask the operator for things. v1 implements this as **one simple submission form with a category dropdown**, feeding the same operator queue as reports (separately categorized):
- **Hashtag suggestion** — propose a new tag for `HASHTAG_VOCAB` (§11.2).
- **External service request** — propose a domain for the URL allowlist (§7.2).
- **Bug report.**
- **Accessibility problem** — anything on the platform that is hard or impossible to use with a screen reader, keyboard, magnification, or any assistive technology (§16.5). Triaged ahead of feature requests.
- **General feedback / feature request.**
Submissions are private (submitter → operator only), rate-limited, and carry no notification machinery. The operator's decisions need no public justification.

### 13.6 Rate limits
All social actions are rate-limited per account per day (posts, comments, reactions, friend requests, introductions, card requests, invites — see §14 for suggested values). Limits are generous for humans and hostile to scripts; hitting one produces an honest "slow down" message. **Login attempts additionally get per-account _and_ per-source-address exponential backoff with temporary lockout** (§4.6.1) — a stricter, security-specific case of the same framework.

---

## 14. Configuration Constants

All caps are named constants; **raise-only** (§1.3). Suggested v1 values; those marked ✎ are operator-tunable judgment calls rather than agreed design decisions.

| Constant | Value | Ref |
|---|---|---|
| `FRIEND_CAP` | 300 | §5.1 |
| `POST_AUDIENCE_MAX` | 30 | §7.1 |
| `POST_LENGTH_MAX` | 10,000 characters | §7.2.1 |
| `COMMENT_LENGTH_MAX` ✎ | 2,000 characters (asserted default) | §7.2.1, §8.1 |
| `FEED_FOLD_CHARS` ✎ | 500 characters (display-only fold threshold, feed) | §7.7 |
| `BLOG_FOLD_CHARS` ✎ | 2,000 characters (display-only fold threshold, profile blog) | §7.7 |
| `IMAGE_MAX_PX` | 3,840 (long edge of stored images; larger uploads downscaled) | §7.2.2 |
| `IMAGE_UPLOAD_MAX_MB` ✎ | 20 | §7.2.2 |
| `ALT_TEXT_MAX` ✎ | 1,000 characters (image alternative text) | §16.3 |
| `GROUP_SIZE_MAX` | 30 | §6 |
| `PIN_LIMIT` | 10 | §7.6 |
| `GALLERY_MAX` | 8 | §9.4 |
| `PROFILE_HASHTAG_MAX` | 10 | §11.2 |
| `CONTACT_ITEMS_MAX` | 12 | §10.2 |
| `NAME_CHANGE_COOLDOWN_DAYS` | 90 (must stay ≥ `NAME_TRANSITION_DAYS`) | §4.5.1 |
| `NAME_TRANSITION_DAYS` | 90 (dual "formerly" display) | §4.5.1 |
| `NAME_BLOCKLIST` ✎ | operator-curated blocked name strings | §4.5 |
| `HASHTAG_VOCAB` ✎ | operator-curated interest vocabulary | §11.2 |
| `INVITE_BANK_MAX` / replenish / new-account start | 5 / +1 per month / 2 | §4.2 |
| `INVITE_EXPIRY_DAYS` ✎ | 14 | §4.1 |
| `CONTENT_TTL_DAYS` | 90 (reconfirmed by founder 2026-07-08; sticky in both directions once live — lowering deletes content early, raising outlives authors' expectations) | §7.5 |
| `EXPIRY_COUNTDOWN_DAYS` | 14 | §7.5 |
| `DELETE_GRACE_DAYS` | 30 | §4.7 |
| Inactivity deletion / warnings | 24 months / 6, 12, 22, 23 | §4.8 |
| Report freeze: appeal / hard cap | 30 / 90 days | §13.3 |
| Re-request cooldown after declined friend request ✎ | 90 days | §5.2 |
| `REACTION_SET` ✎ | ~6 operator-curated phrases | §8.2 |
| `THEME_SET` ✎ | operator-curated fonts + color schemes (each verified against the §16.3 contrast ratios) | §9.1, §16.3 |
| URL allowlist ✎ | operator-curated | §7.2 |
| Rate limits ✎ (per account/day) | e.g., 20 posts, 200 comments, 20 friend requests, 10 intros | §13.6 |
| `RESET_CODE_TTL_MINUTES` ✎ | 15 (lifetime of a reset / email-change / verification code) | §4.6.1 |
| `RESET_CODE_LENGTH` ✎ | 6 (digits) | §4.6.1 |
| `LOGIN_ATTEMPT_LIMIT` ✎ | e.g., 5 failures before backoff begins (per account and per source address) | §4.6.1, §13.6 |
| `LOGIN_LOCKOUT_MINUTES` ✎ | e.g., 15 (base lockout, escalating with exponential backoff) | §4.6.1, §13.6 |

---

## 15. Privacy, Legal, Money

### 15.1 Legal posture
- 18+ only (§4.4). No geo-restrictions; GDPR-compatible by design (minimal collection, guaranteed erasure and expiry, export, no profiling). Privacy policy and Terms of Service are build-plan deliverables, written plainly. A real attorney reviews before any public phase.
- Monitored risk, no v1 impact: spreading age/identity-verification laws could someday force verification machinery; nothing in this design blocks adding it.

### 15.2 Tracking — banned absolutely
No analytics trackers, no behavioral profiling, no third-party scripts, no ad targeting data, no sale or sharing of data, no "engagement" instrumentation. Operational logs (errors, security) only, minimal and short-lived.

### 15.3 Funding — phased
1. **Prototype:** founder-funded out of pocket (~$15/month hosting class). No entity.
2. **If organic growth:** donations via **fiscal sponsorship** (an established nonprofit receives donations on the project's behalf; no incorporation). Verify specific sponsor organizations when needed.
3. **Only if thriving:** consider a real nonprofit entity (charitable-status fit is a lawyer question, deferred). A **voluntary** supporter subscription (no feature gates) may accompany donations.
4. **Mandatory subscriptions: ruled out** (kills the network effect). **Ads:** philosophically permitted only as untargeted "billboards" (advertiser learns nothing about viewers); dormant and unbuilt unless ever needed.

### 15.4 Businesses and brands
Accounts are for **individual humans only**. No business, brand, organization, or bot accounts of any kind in v1.

### 15.5 End-to-end encryption and content signing — considered and deferred (2026-07-21)
The question was raised: should posts, comments, and profile pages be end-to-end encrypted (E2EE) so that even the operator cannot read them without being a friend or friend-of-friend, and should content be digitally signed?

**The cryptography is not the obstacle; audience size is a non-issue.**
- **Signing** a post costs **one signature** regardless of audience — one private-key operation by the author, verified by any number of readers with the author's public key. Thirty readers and three hundred readers are identical in cost.
- **Encrypting** for a bounded audience is also cheap via standard envelope encryption: the body is encrypted **once** with a random one-time key, and only that small key is re-wrapped per recipient public key (a 300-friend post = 1 encrypted body + 300 tiny key-wraps, a matter of milliseconds). Neither 30 nor 300 strains anything.

**Why full E2EE is nonetheless wrong for v1.** The blockers are architectural, not computational:
1. **Web-app delivery undermines the guarantee.** v1 is a browser web app (§2); the browser re-downloads the crypto code from the server on every visit, so a coerced or compromised server can serve code that exfiltrates the user's key. Browser E2EE therefore leans on trusting the very party it claims to defend against. (A native app, shipping signed code, does not have this weakness — but native is explicitly out of scope for v1, §17.)
2. **Password reset is incompatible.** The code-based password reset of §4.6/§4.6.1 cannot coexist with password-derived encryption keys: the server cannot re-encrypt data it cannot read, so a reset would mean permanent data loss — unless keys are escrowed to the server, which defeats the purpose.
3. **It breaks core server-side features — moderation above all.** The report/moderation system (§13) depends on the operator reading a frozen copy to judge it; E2EE makes the operator blind, forcing a choice between "operator can never read content" and "operator can moderate abuse." Server-side EXIF/GPS stripping and image re-encoding (§7.2.2), the URL allowlist, the name blocklist, the hashtag vocabulary, and length caps (§7.2, §4.5, §11.2, §7.2.1) all likewise require the server to see content; moved client-side they become advisory, not enforceable.
4. **It does not deliver the expected protections.** Revocation on unfriending (§7.4) is already enforced by server-side access control, not by cryptography — and cannot be enforced cryptographically, since a past reader could always have retained the key. And E2EE of content still leaves the **social graph and metadata** (who is friends with whom, timing, audience sizes, routing hashtags) visible to the server, which for a social network is often the more revealing exposure.

**What signing would buy is also low here.** Signatures matter when content crosses untrusted intermediaries (federation, forwarding, email). This platform has **no reach, no reshare, no federation** (§1.2, §2), and the server already authenticates every actor, so per-post signatures defend only the narrow case of a malicious server forging posts — a threat the web-delivery problem (point 1) reopens anyway. The value does not justify the key-management burden on a solo, non-developer operator building with AI assistance (§2).

**Adopted instead (v1):**
- **Encryption at rest.** The database/disk is encrypted, and stored content may additionally be encrypted under server-held keys. This protects against stolen backups, disk theft, and a snooping hosting provider — real threats, cheap, and breaking no feature. It explicitly does **not** hide content from the operator, and the platform will not claim otherwise.
- **An honest trust model, stated plainly.** As on every non-E2EE platform, the operator can technically read content. What users get instead is the platform's actual privacy posture: data-minimalism, a hard 90-day expiry (§7.5), guaranteed deletion (§4.7), no tracking or profiling (§15.2), and a single small trusted operator rather than an advertising business. This is consistent with the structural, trust-based safety model of §13.1.

**Where E2EE would genuinely earn its keep is one-to-one private messaging — which this platform deliberately does not have (§10.1).** Broadcast-to-your-friends content is inherently semi-public within a bounded group, so the cost/benefit is far worse than for private chat. If DMs are ever introduced, E2EE is to be reconsidered **for that channel specifically**, along with the native-app question that would make browser-delivery trust moot. Contact-card items (§10.2), the most sensitive PII, are a possible narrow candidate for stronger at-rest protection, but the per-viewer auto-reply flow (§10.4) needs the server to select items, so they too are left as at-rest-encrypted for v1.

---

## 16. Accessibility (v1.10)

### 16.1 The commitment
**Every user-facing surface of the platform conforms to the Web Content Accessibility Guidelines (WCAG) 2.1 at Level AA.** This is a requirement of the same rank as the tracking ban (§15.2) and the no-reach thesis (§1.2): a feature that cannot be made accessible is not shipped, and "we'll fix the accessibility later" is not a state this project recognizes. Level A is included by definition (AA subsumes it). Individual AAA criteria are adopted where they are free (noted below); **Level AAA is not claimed as a whole.**

Scope: the web application in every state — logged-out pages (login, password reset, invite redemption), the feed, composers, profile pages, discover, settings, contact cards, error and empty states, and every email the platform sends. The **operator console** (Django admin, §13) is held to the same standard as far as the framework allows; where it falls short, the shortfall is the operator's own, not a user's.

### 16.2 Why this is a principle here, not a checkbox
1. **An inaccessible page here excludes a person from their own family.** This is not a public site someone can route around. Membership is invite-only (§4.1), there is no API and no native app (§17), and the audience is people's real friends and relatives. The web app is the *only* door; a blind or motor-impaired invitee who cannot use it is not inconvenienced, they are excluded from the specific humans who vouched for them.
2. **The architecture already favors it.** Server-rendered HTML with no JavaScript framework, no third-party embeds, no autoplaying media, no infinite scroll, and no algorithmic reordering is the most accessible baseline the modern web offers. Most of this conformance is kept rather than built.
3. **It is legally prudent** for a service that may one day be public (§15.1) in jurisdictions with the ADA, the European Accessibility Act, and equivalents — all of which point at WCAG AA.
4. **The design's own values already point this way:** honest text error messages, no engagement animation, no scorekeeping, bounded quantities, and reader control over presentation (§9.1) are accessibility measures written in another vocabulary.

### 16.3 Requirements by area
These are the platform-specific applications of WCAG 2.1 AA. They are requirements, not suggestions; the numbered references are the WCAG success criteria they satisfy.

**Structure and semantics**
- Real semantic HTML first — headings in correct order, lists as lists, buttons as `<button>`, links as `<a>` (1.3.1). ARIA is used only where native semantics genuinely fall short, never as a substitute for them.
- Every page has landmark regions (banner / navigation / main / contentinfo), a unique descriptive page title (2.4.2), a "skip to main content" link as the first focusable element (2.4.1), and `lang` set on the document (3.1.1).

**Keyboard**
- Every function is operable by keyboard alone, with no traps (2.1.1, 2.1.2) — including the audience picker, hashtag picker, contact-card toggles, image overlay, and "read more" folds.
- A **visible focus indicator** on every focusable element, meeting contrast against its background (2.4.7). It is never removed by a theme.
- Focus order follows reading order (2.4.3). Any control that appears on hover is also reachable on focus (1.4.13).

**Contrast, color, and theming (§9.1)**
- Body text ≥ **4.5:1**, large text ≥ **3:1** (1.4.3); UI components, focus rings, and meaningful graphics ≥ **3:1** (1.4.11).
- **Every theme in `THEME_SET` must pass these ratios in every combination in which it can appear** — including a visitor's profile theme and the "always use my own theme" viewer override. This is the operational reason theming is operator-curated and not freeform: contrast can be *guaranteed* for a curated set. A candidate theme that fails is not added.
- **Color is never the only carrier of meaning** (1.4.1): expiry countdowns, pinned markers, error states, and toggle states all carry text or shape, not just hue.
- The viewer override of §9.1 is itself an accessibility feature (a user with low vision keeps their chosen high-contrast scheme everywhere) and must never be overridable by a page author.

**Text and layout**
- Text resizes to **200%** without loss of content or function (1.4.4), and the layout **reflows at 320 px** with no two-dimensional scrolling (1.4.10).
- User-applied text spacing overrides do not break layout (1.4.12).
- **Preformatted posts are the one documented exception** (§7.2.1): they legitimately require two-dimensional layout, which 1.4.10 explicitly exempts, and they intentionally scroll horizontally. The obligations that come with the exemption: the scrollable region must be **keyboard-scrollable and focusable** with an accessible name (a scrollable box that only a mouse can pan is a 2.1.1 failure), and the composer's preformatted explainer must state plainly that the mode trades reflow for exact spacing.

**Images (§7.2, §7.2.2, §9.4)**
- Every uploaded image — post image, gallery image, profile photo — carries an **alternative text description** (1.1.1), authored by the uploader, up to `ALT_TEXT_MAX` = 1,000 characters.
- The composer **prompts for it and requires a deliberate choice**: write a description, or tick "this image is decorative" (which stores an explicitly empty alt). It is never silently skipped and never auto-filled — the platform does not infer (§1.5), and machine-generated descriptions are not a v1 feature.
- The click-to-expand overlay (§7.2.2) is a **modal dialog**: focus moves into it on open, is trapped while open, Escape closes it, and focus returns to the image that opened it. Zoom/pan is operable by keyboard.

**Forms, errors, and status**
- Every input has a programmatically associated visible label (1.3.1, 3.3.2). Placeholders are never labels.
- Errors are identified in **text**, associated with the offending field, and describe the fix (3.3.1, 3.3.3) — which the spec's existing "honest error message" rule (§5.1, §7.2.1, §7.3, §13.6) already demands in prose. Character-cap overruns, breached passwords (§4.6.1), blocked names (§4.5), disallowed URLs (§7.2), and audience-size overruns all follow this rule.
- **Status messages are announced without moving focus** (4.1.3): the audience picker's live count, "post published", "code sent", rate-limit "slow down" notices, and lockout messages use polite live regions.

**Time limits and motion**
- The security-essential time limits — code TTL (`RESET_CODE_TTL_MINUTES`) and login lockout (`LOGIN_LOCKOUT_MINUTES`) — fall under 2.2.1's essential-exception, but the user is **told the limit in text** and can always request a new code. No other timed interaction exists.
- **Session expiry never destroys work in progress**: composer content survives a re-authentication.
- The expiry countdown (§7.5) renders as **static text computed per page load** ("deletes in 6 days"), never as a live-ticking timer — no moving, auto-updating, or auto-refreshing content (2.2.2). The feed updates only when the reader reloads it; nothing is ever inserted above what someone is reading.
- No flashing content (2.3.1). Any transition respects `prefers-reduced-motion`.

**Targets and pointers**
- All functionality available by pointer works with a single pointer without path-based gestures (2.5.1) and is cancellable (2.5.2). The overlay's pan/zoom has keyboard and button equivalents.
- Touch targets: **44 × 44 CSS px minimum** as a design rule. (This exceeds AA — 2.5.5 is AAA — but it is free in a mobile-first layout and adopted deliberately.)

**Names and non-visual equivalence**
- The "NewName (formerly OldName)" dual display (§4.5.1) is **real text**, not a visual decoration, so it reaches screen-reader users identically.
- Reactions (§8.2) are curated **phrases**, not emoji or colored icons, and are therefore already non-visually legible — a happy consequence of the no-scorekeeping rule.
- Visible label text matches accessible names (2.5.3).

**Email**
- Every platform email is sent with a **plain-text alternative** and is legible without images or CSS. (Outside WCAG's scope for pages, inside the spirit of this section.)

### 16.4 Explicitly banned "accessibility" measures
- **No accessibility overlay widgets** (AccessiBe, UserWay, EqualWeb and their kind), ever. They are third-party JavaScript — banned outright by §15.2 — they profile visitors, they do not fix underlying defects, and disabled users' own organizations consistently reject them. There is no exception for this ban.
- **No separate "accessible version" of the site.** One site, accessible.
- **No CAPTCHA** (already excluded by §4.6.1, §17) — an accessibility hazard as well as a privacy one. If the self-hosted proof-of-work fallback contemplated in §4.6.1 is ever adopted, it must be the **non-interactive** kind that requires nothing of the user.
- No content whose meaning depends on hover, color, sound, or an unlabelled icon.

### 16.5 Verification and feedback
- **Conformance is verified, not assumed.** The build plan carries the audit as a required gate before launch: automated scanning, a **keyboard-only pass** over every flow, a **screen-reader pass** (VoiceOver on macOS and iOS — free, already on the founder's machines), a 200%-zoom and 320px-reflow pass, and an automated contrast test over every `THEME_SET` combination. Accessibility tests live alongside feature tests, per the test-depth rule.
- An **accessibility statement page** is published alongside the privacy policy and terms (§15.1): the conformance target, known limitations honestly listed (including the preformatted-post exemption of §16.3), and how to report a problem.
- The operator request form (§13.5) gains an **"Accessibility problem"** category. Accessibility reports are triaged ahead of feature requests.
- **Honesty rule:** the platform claims exactly the conformance it has verified. A known unfixed defect is listed in the statement rather than papered over.

---

## 17. Non-Goals (explicit)

No reshare/repost/quote of any kind · no public content or logged-out visibility · no likes or visible counts (followers, reactions, views — none exist) · no algorithmic feed · no DMs · no global search (people or content) · no global hashtag browsing (the only tag view is the viewer-scoped discover filter, §11.4) · no events system (delegated to allowlisted external services) · no video/audio · no native app (v1) · no API for third parties (v1) · no AT Protocol / blockchain · no minors · no businesses · no CAPTCHA or third-party human-challenge (§4.6.1, §16.4) · no end-to-end encryption or per-post content signing in v1 (§15.5; encryption-at-rest is used instead) · **no accessibility overlay widgets and no separate "accessible version" of the site (§16.4)** · no WCAG Level AAA conformance claim (individual AAA criteria are adopted where free — §16.1) · no machine-generated image descriptions (§16.3) · defending against off-platform screenshots is out of scope.

**Parked ideas (explicitly not in v1):** request-more-access flags if trimmed to v1.1 (§10.5) · social account recovery · introduction-visibility opt-in toggle (§5.5) · per-post "friends-only comments" switch · nested comments · auto-suggesting frequent post hashtags for the profile · invite-tree accountability mechanisms · billboard ads · click-to-load media embeds (§7.2).

---

## 18. Downstream Documents

Produced in order, each pausing for founder review: **(b)** architecture + technology stack (plain-language, beginner-appropriate); **(c)** step-by-step build plan, clearly marking steps the founder performs outside AI chat, with exact instructions; **(d)** the sequence of AI-coding prompts to build it; **(e)** CLAUDE.md for the project repository.

---

## Appendix A — Defaults asserted by this spec

Decisions this document had to make that were never explicitly discussed in design sessions. **All ten were reviewed and confirmed by the founder on 2026-07-07** (item 7 after explicit discussion):

1. **Strict reverse-chronological feed, no ranking** (§7.7) — implied by the thesis, never voted on.
2. **Humans only, no business accounts** (§15.4) — discussions "leaned humans-only"; this spec commits to it for v1.
3. **Audience snapshot + current-friendship rule** (§7.4), including: unfriending revokes access to old posts; later-added friends see profile posts but not past feed posts.
4. **Inviter and invitee automatically become friends** (§4.1).
5. **Invites expire after 14 days and return to budget** (§4.1).
6. **90-day re-request cooldown** after a declined friend request (§5.2).
7. **No images in comments** (§8.1).
8. **Example reaction set and rate-limit numbers** (§14) — placeholders for operator curation.
9. **Deactivation is immediate and total during the 30-day deletion grace period** (§4.7).
10. **No "someone viewed your profile" features anywhere** — consistent with no-scorekeeping (§8.2, §11.4).
