# WeeBee — Platform Specification

**Project version:** 1.21 · 2026-08-17 · DRAFT pending founder review
**This file last changed in:** 1.21 (the hashtag vocabulary given an operational posture — aliases, batching, the accepted single-point-of-failure — and every report given a reason)
**History:** see [CHANGELOG.md](CHANGELOG.md)
**Purpose of this document:** The single authoritative description of what the platform is and how every feature behaves. It is written to be self-contained: a developer or an AI coding model with no access to prior conversations must be able to build from this document alone. Architecture, technology choices, and build steps live in separate documents (see §18).

---

## 1. Mission and Design Philosophy

### 1.1 Purpose
A digital tool for maintaining and creating positive real-life social relationships:
1. Help people stay in touch with existing friends and family.
2. Help people form new friendships through mutual friends and shared interests.
3. Be structurally resistant to commercial and political manipulation — by design, not by moderation.

**The measure of success is offline.** WeeBee exists for the times people *cannot* be together in person — distance, schedules, life. Its job is to carry a relationship across those gaps and, wherever possible, to help close them. The platform is working when it puts people in the same room; it is not working merely because someone is looking at it. This is the reason features that help people convene are privileged in the link policy (§7.2.3), and the reason nothing here competes for a user's attention or tries to extend a visit.

### 1.2 The core thesis: no concept of reach
The reshare/repost button is the "original sin" of social media. Once content can propagate beyond its author's chosen audience, virality exists, and virality is the mechanism that manipulation exploits. **This platform has no concept of reach. Nothing can go viral.**

**The No-Reach Test (apply to every current and future feature):** *Can this feature cause content to travel beyond the audience its author deliberately chose, or let a person be seen by people with no real social connection to them?* If yes, the feature is wrong for this platform.

**What the guarantee covers — stated honestly (v1.12).** No-reach is a guarantee about **mechanical** propagation: the platform offers no reshare button, no ranking, no global search, no hashtag browsing, and no measurement that could move content past its chosen audience. It is *not* a claim that an idea can never travel. A person can always read something here and retype it in their own post, paste in an outside link, or run a "copy this into your feed" chain letter. **That path is deliberately not designed against**, because it is indistinguishable from a friend telling a friend about something — the exact behavior the platform exists to support.

What keeps it self-limiting rather than exploitable is that every hop must pay full price: a deliberate human act of copying and composing, a fan-out capped at 30 hand-picked people (§7.1), a landing zone that heavily overlaps the cluster it came from (a bounded graph has no long tail of weak ties), a daily posting rate limit (§13.6), and — decisively — **no number that would ever tell anyone it is working.** Reactions and comments do return real social feedback, as they should between friends, but they are names and fixed phrases, private to the author, not comparable across posts, and invisible to any third party (§8.2). An outside campaign cannot measure its own reach here at all, and a campaign that cannot be measured cannot be optimized. Social cost does the rest: on a network with no strangers (§1.3), chain letters annoy people who know you. Persistent offenders are reportable (§13.2) and traceable through the invite tree (§4.3).

### 1.3 Supporting principles
- **Pull over push.** Broad audiences must come to you (profile visits); push is reserved for small, hand-picked audiences.
- **Bounded everything.** Friends, audiences, groups, images, invites, hashtags — every quantity has a hard cap, implemented as a named configuration constant (§14). Caps may be raised later; they are never lowered (lowering strands users above the new limit).
- **Data minimalism.** The platform is a communication tool, not an archive and not a data harvester. Content self-destructs (§7.5); collection is minimal; tracking is banned absolutely (§15.2).
- **Humans, vouched.** Every account enters through a personal invitation from an existing member. There are no strangers; every user is at most one trusted hop from someone who vouched for them.
- **Not a walled garden.** The platform does not try to own a relationship. Where a need is already well served by open, established channels — person-to-person messaging above all (§10.1) — WeeBee delegates rather than rebuilds, and makes the handoff cleanly. It aims to be one useful tool among many, never the place a user cannot leave (see also credible exit, §4.9).
- **The platform never infers.** No behavioral profiling, no algorithmic ranking, no machine guesses about who matters to you. Users state their intent; the platform obeys it.
- **Usable by everyone it invites.** Every surface conforms to WCAG 2.1 Level AA (§16). On an invite-only network of real friends and family, an inaccessible page does not inconvenience a user — it excludes a specific person from the specific people who vouched for them.

---

## 2. Project Context

- **Name:** The platform is **WeeBee**, at `weebee.social` (registered 2026-07-25). The name reads as *wee* (small) + *bee* (a member of a close, busy hive) — a fit for a deliberately small, private network. It is used verbatim in user-facing copy; "the platform" is retained in this document only as the generic descriptor.
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
- Replenishment: +1 every `INVITE_REPLENISH_DAYS` = **30 days** since the last replenishment, never exceeding the bank max. (In days, not calendar months, for the reason given in §4.8.)
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
- **The checkable promise.** Because recovery never uses a login link, the platform makes a plain, memorable commitment: *"WeeBee will never email you a link to log in or reset your password — only a code you type in yourself,"* shown at the relevant touchpoints (login, reset, help). Its value is that it makes **any** look-alike "click here to log in" email self-evidently fake, no matter how convincing the sending domain — a defense that does not depend on the user scrutinizing a URL.

**More than one kind of credential (capability now, passkeys later).**
- v1 ships **password login only.** But the credential data model is built from the start to hold **more than one credential type per account**, so a phishing-resistant second type can be added later without reworking the auth layer (per §2: architecture must not need discarding).
- The intended second type is **passkeys (WebAuthn)**, cryptographically bound to the site's origin: a passkey registered on the real domain does not function on a look-alike, and the browser will not even offer it. This is the only measure here that structurally defeats a **real-time proxy phish** (an attacker relaying the live login page). For the record: **ordinary TOTP two-factor codes do _not_ defeat that attack** — a proxy relays a 6-digit code as readily as a password; this is why passkeys, not TOTP, are the chosen structural fix. Passkeys are **deferred as a feature** for the solo prototype (device-loss recovery and cross-device UX are real work); only the capability is required in v1.
- **Password managers** are encouraged at onboarding: they refuse to autofill on the wrong origin, giving the user a free, silent phishing signal.

**Login-endpoint defense (brute force and credential stuffing).** These are attacks on our own server, so they are ours to fix directly:
- **Throttling with lockout.** Login attempts are rate-limited **per account _and_ per source address**, with exponential backoff and temporary lockout (`LOGIN_ATTEMPT_LIMIT`, `LOGIN_LOCKOUT_MINUTES`), extending the rate-limit framework of §13.6. A failed-login flood is slowed to uselessness without ever challenging a human.
- **Slow password hashing.** Passwords are stored with a deliberately slow, memory-hard hash (**Argon2id**), so an attacker who ever obtained the database cannot cheaply brute-force the stored hashes.
- **Breach-password rejection** at registration and at every password change: the chosen password is checked against the public corpus of known-breached passwords via a **k-anonymity range query** — only the first five characters of the password's hash leave our server; the full password and the user's identity never do. It is a server-to-server call, not a browser script, so it is fully compatible with the tracking ban (§15.2). A known-breached password is refused with an honest explanation. (That hash prefix is a lookup index only; passwords are never stored this way — see the Argon2id rule above.)

**Email domain authentication.** The sending domain publishes **SPF, DKIM, and DMARC at `p=reject`** from day one. This does not stop look-alike domains, but it stops anyone spoofing the platform's *real* domain in email — a free, standard baseline. (Mechanics: ARCHITECTURE §7, build-plan Step 5.5.)

**Security-event emails.** New-device login, password change, and email change generate account/security notifications (§12); these shrink the window in which a compromise goes unnoticed. They mitigate, not prevent. **These events carry absolute timestamps wherever they appear** — one of the two narrow exceptions to the relative-time rule of §7.5.1, because *"was that login me?"* is not a question anyone can answer with "several hours ago."

**CAPTCHA — considered and rejected (2026-07-21).** No CAPTCHA (or reCAPTCHA / hCaptcha / Turnstile) is adopted, for three reasons: (1) it does nothing against phishing — it is an anti-automation control on our own server, not a defense against a deceptive site elsewhere; (2) the mainstream options conflict with the absolute ban on third-party scripts and behavioral profiling (§15.2) — reCAPTCHA v3 in particular scores users on browsing behavior; (3) the problem CAPTCHA usually solves — signup spam and content scraping — does not exist here (no public signup, no public content). The login-endpoint threats it is sometimes stretched to cover are better handled by the throttling, hashing, and breach-check measures above. **If** a human-challenge mechanism is ever genuinely needed, the only kind compatible with this platform's privacy principles is a **self-hosted proof-of-work** challenge (e.g., Altcha, mCaptcha): first-party, no tracking, no third-party scripts, accessible.

**Defensive domain registrations — settled: none (2026-07-25).** Buying look-alike/typo variants of `weebee.social` is harm-reduction aimed at a *public* brand worth impersonating, and it is an unwinnable, open-ended expense (a brand can be misspelled in unbounded ways across unbounded TLDs). The founder has decided **not** to pursue it — not as a v1 deferral but as a standing decision — and to invest no effort in "domain hygiene." The structural anti-phishing defenses (codes-not-links, the checkable promise, passkey capability, SPF/DKIM/DMARC at `p=reject`) do not depend on owning the neighboring namespace. **Certificate-transparency monitoring is kept as the one lightweight recommendation:** a free crt.sh alert on the brand string costs nothing and gives early warning of a look-alike certificate being issued; it is worth enabling before any public phase (§15.1) but requires no registrations.

### 4.7 Account deletion (user-initiated)
- Deletion request → account immediately deactivates (invisible to all users) → **30-day grace period** (`DELETE_GRACE_DAYS`) during which the user can log in to cancel → after grace, **full erasure** of all data: posts, comments, reactions, images, contact card, groups, friendships, profile.
- **What "full erasure" means precisely, and its one honest caveat (v1.18).** Erasure from the live system is immediate and permanent at the end of the grace period. As with every deletion here, an encrypted off-server backup may still hold a copy until it ages out at `BACKUP_RETENTION_DAYS` = 30 days, and is then destroyed (§7.5, ARCHITECTURE §10). Backups are encrypted, never queried, and never used to restore an individual account — only the whole system after a disaster. The promise is therefore: **erased from the platform at once, and gone from the last encrypted backup within 30 days after that.** This is stated here rather than left to §7.5 because account deletion is the one place a user is most likely to rely on the promise being literal.
- Sole exception: the anonymized invite-tree stub (§4.3) and content-free moderation counters (§13.4).
- Deletion of a user removes their comments and reactions everywhere.
- **What "deactivates" means (v1.16).** The account **and all of its content** become invisible everywhere, reversibly: profile, blog, gallery, and the user's comments and reactions on other people's posts. Nobody is notified — the silent precedent of §5.3. Notifications naming them drop out on their own, because §12.2 renders from current state rather than from event-time state. A visitor gets the response of §9.3, indistinguishable from a profile that never existed. The user's own view keeps working so they can cancel, carrying a banner with the **absolute** erasure date — an account event, and therefore one of §7.5.1's two narrow exceptions to relative time.

### 4.8 Inactivity deletion
- Accounts with no login for `INACTIVITY_DELETE_DAYS` = **730 days** (two years) are deleted (full erasure as §4.7).
- Warning emails at `INACTIVITY_WARN_DAYS` = **180, 365, 670 and 700 days** since last login. The first two are gentle "your account is dormant" notes; the final two — 60 and 30 days before deletion — are explicit deletion warnings.
- **Every interval here is a count of days, never calendar months (v1.18).** The sweep is a daily job (ARCHITECTURE §6) and every other time quantity in this document is a count of days; "six months" would leave a builder to choose between 180 days and six calendar months, which do not agree.

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
- Requests carry **no composed text**: there is no message field, no note, no subject line. The recipient sees: the requester's basic-tier profile (§9.2), the mutual friends they share, and shared profile hashtags. The system generates this context; the requester writes nothing *into the request*.
- **The qualification this needs, and the controls that answer it (v1.15).** The basic-tier profile shown here contains the requester's own **short bio and profile photo** — both author-controlled. A friend request therefore does place text and imagery of the sender's choosing in front of someone who never asked for it, up to `20` requests a day (§13.6), whether or not the recipient accepts. That is a message channel wearing a profile field's clothes, and it is answered four ways (amended v1.16): the short bio is **screened against `NAME_BLOCKLIST` at every save**, exactly as display names are (§4.5); **sending further requests is held for `REQUEST_HOLD_AFTER_PROFILE_CHANGE_HOURS` after either the photo or the short bio changes** (§13.6), so the surface cannot be rewritten between batches of requests, and the card itself is frozen at send time so a later change cannot rewrite one already delivered; the short bio **never renders clickable links and rejects disallowed URLs at save** (§9.4), so no link can be delivered this way; and the card **carries the report action** (§13.2), so the person the push lands on can act on it. What a blocklist cannot catch is left to the report system and invite ancestry (§4.3) — the same honest posture §4.5 takes for names. §13.1 records the qualification rather than continuing to claim the surface does not exist.
- **The card is a snapshot, not a live view (v1.16).** The requester's **profile photo and short bio are frozen into the request at the moment it is sent**; a later change never alters a card already delivered. Without this, any limit on changing them is defeated by the obvious move — send twenty clean requests, then change the photo, and every unanswered card shows the new image. (The requester's *display name* still renders live through the shared helper, per §4.5.1's rule that names are never stored on content.)
- **The card carries the report action** (§13.2), targeting the requester's profile. This surface is where an unscreened profile photo (§13.6) reaches someone who never asked for it, so it is exactly where reporting must be reachable; the defence of this surface is screening, the send hold below, and reports, and a report the recipient cannot reach is not a defence.
- **Sending is held after a profile change (v1.16).** A user may not send new friend requests for `REQUEST_HOLD_AFTER_PROFILE_CHANGE_HOURS` after changing their profile photo or short bio (§13.6). Hitting it produces the honest "you can send friend requests again in N hours" message, stating the reason.
- Recipient accepts or declines. **Declines are silent** — the requester is never notified; the request simply never resolves for them.
- Asserted default: after a decline, the same requester cannot re-request the same person for 90 days.
- **Pending requests expire after 90 days (v1.16)**, matching `CONTENT_TTL_DAYS`, and their frozen card is destroyed with them. A request that never resolves would otherwise hold a copy of an image indefinitely.

### 5.3 Unfriending
Silent. The unfriended party receives no notification. Effects are immediate: each loses access to the other's friends-only content, feeds stop receiving the other's posts, and each disappears from the other's audience lists (see snapshot rules, §7.4).

**Unfriending is not invisibility, and the confirmation must say so (v1.16).** A former friend does not vanish; they fall to whatever tier they still qualify for. If any mutual friend remains they are a FoF, and therefore keep the basic tier — name, photo, short bio, hashtags — **plus any profile post carrying a hashtag they also carry**, including pinned ones, under the live gate of §11.3 that §7.4 already names as an exception. This is surprising enough, and consequential enough, that the confirmation states it plainly rather than leaving the user to derive it: *"They'll no longer see your posts or your about section. If you have friends in common, they can still see your name, photo and short bio — and any blog post tagged with an interest you both share."* A user who wants the stronger outcome wants a block (§5.4). The former friend's own past comments on the user's posts remain where they are; only account deletion removes those (§4.7).

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
| Delivery | **Push**: appears in each recipient's feed | **Pull**: lives only on the author's profile blog; friends receive only a notification, never the content (§12.1, §12.2) |
| Hashtags | Ranking signals only (§11.2) | Gate FoF visibility (§11.3) |
| Pinnable | No | Yes (§7.6) |
| Where it can be read | The recipients' feeds, **and its author's Blog tab** (§9.1) | Its author's Blog tab, and the Pinned tab if pinned |

**One composer for both types (v1.16).** There is a single composer, reached from the main navigation — not a separate composer on the profile page, which would make the destination implicit in where the author happened to be standing rather than something they chose. One composer is also the only way the shared rules stay shared: length caps, whitespace normalization, the preformatted toggle, the URL allowlist and its open-redirector check, the image-plus-alt-text prompt, and the hashtag picker are all written in this document as rules for *both* types (§7.2, §7.2.1, §7.8), and two implementations are how §7.8's security-critical invariant 4 quietly stops running on one path.

- **Destination is a required choice with no default**, in real text (§16.4): *"Send to a few friends — appears in their feed"* / *"Post to my blog — all your friends can find it."* Choosing the first opens the audience picker (§7.3); choosing the second opens the hashtag picker with the audience line of §7.9 beneath it.
- Per §16.3's error rule, a missing choice produces an **honest text error naming the fix**, never a silently disabled button.
- **A draft may switch type freely.** Switching to a blog post clears any picked audience, which has become meaningless; switching to a feed post states that hashtags stop gating visibility and become decorative (§11.2). Both are text notices, not modal interruptions.
- **A published post can never change type.** Not primarily a No-Reach question — an author widening their own audience is manual re-propagation, which §17 places out of scope — but because §7.8 invariant 1 forbids re-snapshotting an audience, and above all because of **the comments**: converting a feed post would expose words written to ≤30 hand-picked people to all the author's friends and to hashtag-matched FoFs, which is the same disposal of other people's words that §7.6 refuses. Delete-and-repost remains available at its honest cost.

### 7.2 Content rules (both types)
- Plain text, plus **at most one image** per post.
- URLs are permitted **only** from an operator-curated allowlist of trusted service domains. Any other URL is rejected at composition time with an honest explanation that names the alternative. The allowlist is a maintained operational artifact, not user-configurable. **What the allowlist admits and why — including the mandatory open-redirector rule — is §7.2.3.** The allowlist governs posts and comments; the profile's bio fields carry their own rule (§9.4), under which the FoF-visible **short bio renders no links at all** and only the friends-only extended bio may carry allowlisted ones.
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
- **Length caps.** A post may contain at most `POST_LENGTH_MAX` = **10,000 characters** (roughly 1,500–2,000 words — genuine long-form writing is welcome; the cap is an abuse bound required by the bounded-everything principle (§1.3), not a style nudge). A comment may contain at most `COMMENT_LENGTH_MAX` = 2,000 characters — roughly 300 words, **confirmed by the founder 2026-08-04**, having stood as an undiscussed assertion since v1.6; long enough that comments need a fold of their own (§8.1). Exceeding a cap produces an honest character count in the composer; text is never silently truncated.

### 7.2.2 Images: size and display (v1.7)
Applies to **every uploaded image** — post images, gallery images (§9.4), and the profile photo — and extends the existing upload pipeline of §7.2 (EXIF stripping, server-side re-encoding).

- **Upload and storage.** Uploads are accepted up to `IMAGE_UPLOAD_MAX_MB` = 20 (rejected above that with an honest message). The server **downscales** any image whose long edge exceeds `IMAGE_MAX_PX` = **3,840 pixels** to that size, preserving aspect ratio — full 4K-wallpaper quality is kept; nothing larger is stored. Normal phone photos (12–48 MP, larger than 4K) are therefore never rejected for their dimensions — they are accepted and scaled down. The server may additionally store smaller derived renditions of the same image for efficient display; the 3,840 px version is the canonical "full size."
- **Display: scale to fit, click to expand.** On every reading surface (feed, profile blog, gallery, discover), an image is **proportionally scaled** — never cropped, never stretched — to fit within the surface's layout (in the feed, also within a bounded height, so one tall portrait photo cannot dominate the screen the way long-post folding prevents for text, §7.7). Clicking/tapping an image opens the **full-size version in an in-app overlay** (dismissable, with zoom/pan when the image is larger than the screen) — a proper modal dialog per §16.3: keyboard-openable, focus-trapped, Escape-dismissable, focus restored on close. Every image carries uploader-authored alternative text or an explicit "decorative" mark (§16.3). The overlay is an in-app view, not a raw file URL — image access follows the same no-deep-links, permission-checked rule as everything else (§9.3).

### 7.2.3 The URL allowlist: what it admits and why (v1.12)

The allowlist does **two jobs at once**, and both are deliberate. The first is **anti-phishing**: it is the control that closes the in-platform link-delivery vector §4.6.1 depends on. The second is to **state what the platform is for** — WeeBee carries the links that serve the mission of §1.1 and delegates everything else to the channels of §10.1. The list is a purpose filter, not merely a security whitelist that happens to contain map services.

**Three admitting categories.** A domain is a candidate only if it falls into one of these **and** independently clears the anti-phishing bar below.

1. **Convening — services that help people be together in person.** Maps (Google Maps, Apple Maps), invitations and RSVPs (Evite and equivalents), calendars, ticketing, venue and restaurant pages. This category is the platform's purpose expressed as a data table, and it is why WeeBee needs no events system of its own (§17).
2. **Hosting what WeeBee cannot host.** Video and audio platforms (e.g. YouTube, Vimeo, SoundCloud, Bandcamp). WeeBee hosts no video or audio (§7.2, §17) — hosting them is out of scope for a solo operator — so these services are where a user's **own** recording lives. The stated purpose in composer and help copy is exactly that: *"WeeBee doesn't host video or audio. This is where your own recording lives."*
3. **Handoff — official messenger link domains** (WhatsApp, Signal, Telegram and equivalents). These move a conversation to a channel WeeBee deliberately does not provide (§10.1) — the "not a walled garden" principle (§1.3) made concrete. The same domains serve the contact card (§10.2).

**Original content: an aspiration, honestly not an enforceable rule.** The founding preference is that what people post here is their own, and category 2 largely serves it — the link is a prosthetic for a capability the platform lacks, not a channel for someone else's work. But **a link to one's own upload and a link to someone else's are identical at the URL level.** The difference is intent, and no domain rule can read intent. The platform therefore states the preference in its copy and does not pretend to enforce it.

Nor should it. Sharing something you did not make in order to *talk about it* with people you know is ordinary friendship and long predates the internet, and the structure of §1.2 already guarantees it cannot become amplification: there is no reshare, no ranking, no search, no counter, and nothing an outside campaign could measure. Virality is defeated structurally, which is precisely what frees the allowlist from having to police authorship.

**The anti-phishing bar (every candidate, every category).**
- Official domains of large, stable, non-deceptive services only. **A URL shortener is never allowlistable** — it makes the destination unknowable, which defeats the entire control.
- **Host matching is not sufficient.** Several otherwise-allowlistable services operate **open redirectors** — `youtube.com/redirect?q=…` and `google.com/url?q=…` are the well-known cases — which would bounce a reader from an allowed host to an arbitrary attacker page. The validator must match on **host *and* reject known redirector paths and query parameters**, and every newly added domain must be checked for a redirector before it goes live. This is a requirement of the allowlist, not an optimization; a host-only check is a defective implementation of this section.

**The rejection message.** When a URL is refused, the message is honest and states the fix (§16.3): that the link is not permitted here, briefly what the allowlist is for, and that **anything else can be shared through the contact methods on the user's contact card** (§10) — email, phone, or messenger, where nothing is restricted. This is the standing answer to "you are restricting what I can share": WeeBee limits what **it** carries, never what a user may say, and it always names the door out. Users may propose a domain through the operator request channel (§13.5).

### 7.3 Audience selection (feed posts)
- The composer lets the author pick individual friends and/or groups; the resolved recipient set must be ≤ 30. Exceeding it produces a clear warning and requires narrowing — recipients are never silently dropped.
- Feed posts by the same author are additionally spaced at least `POST_MIN_INTERVAL_MINUTES` apart, closing the batch-and-repost workaround for reaching more than 30 people via push (§13.6).

### 7.4 Audience semantics (both types)
- The audience is **snapshotted at posting time**, and access additionally requires **current friendship** at viewing time. Formally: viewer may see a post iff (viewer ∈ posting-time audience) AND (viewer is currently the author's friend) — plus the FoF hashtag exception in §11.3. Unfriending or blocking therefore removes access to all past posts. Friends added *after* a post never see that feed post; new friends *do* see existing profile posts (profile posts' audience is "all current friends").

### 7.5 Expiry — nothing outlives 3 months
- **Every post and every comment is permanently deleted `CONTENT_TTL_DAYS` = 90 days after creation, with one exception: posts that are currently pinned (§7.6).** No archive, no soft-delete, no operator copy (sole exception: frozen moderation copies, §13.3). The exception is stated here, and not only in §7.6, because an expiry job written from this bullet alone would delete pinned posts. **Comments have no such exception** — a comment on a pinned post expires at its own 90 days regardless of the pin.
- **And in the backups, for up to 30 days more (v1.18).** Deletion — by expiry, by its author, or by account erasure (§4.7) — is immediate and permanent in the live system. The encrypted off-server backups (ARCHITECTURE §10) still hold a copy until they age out at `BACKUP_RETENTION_DAYS` = 30 days, and are then destroyed. They are encrypted, never queried, and never serve a page. The honest form of the promise, used in all user-facing and project-facing copy: **deleted at 90 days, and purged from the last encrypted backup within 30 days after that.** Deliberately not "gone by day 120": that figure invites a reader to compute an exact date which in truth depends on when the last backup happened to run.
- **What this rule does not govern.** Expiry applies to posts and comments. The profile photo, the gallery, both bio fields, profile hashtags, the contact card, groups and the friend list are **account state**, not statements, and do not expire — see §9.7.
- Deletion includes attached images and all comments/reactions on the expired post.
- Authors can delete their own posts at any time before expiry (immediate, permanent).
- **Visible timestamps and countdown:** every post and comment displays its age, as a **relative, approximate phrase** rather than an absolute date and time (§7.5.1, amended in v1.15). When an unpinned post has `EXPIRY_COUNTDOWN_DAYS` = 14 or fewer days left, a countdown to deletion is shown to everyone who can see it, in **absolute days** ("deletes in 6 days") — ephemerality made visible, the anti-archive stance as interface. Pinned posts show a "pinned" marker instead.

### 7.5.1 Displayed time: relative, not absolute (v1.15)

**Every timestamp a normal user sees on a social surface is relative and approximate**, drawn from the fixed ladder below, growing vaguer as the content ages. This amends §7.5, which formerly required the absolute posting date and time.

**Why.** Precision about the past is archival, and this is not an archive (§1.3). Exact times also carry a specific anxiety — *"posted three minutes ago, why has nobody replied"* — which is scorekeeping wearing a clock's face (§8.2). Stated as a principle: **WeeBee is deliberately vague about how old something is and exactly precise about when it will be destroyed.** The absolute-days expiry countdown of §7.5 is not an inconsistency with this rule; it is the other half of the same idea.

**The ladder.** Exhaustive and non-overlapping by construction: each row is an upper bound on elapsed time, evaluated in order, first match wins. It is rendered by **one shared helper**, as display names are (§4.5.1) — every surface calls it, none reimplements it.

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

Notes on three of the choices, so they are not "corrected" later by someone who assumes they were sloppy. **"Just now" deliberately covers everything under 75 seconds**: pages are server-rendered and never live-tick (§16.3), so a finer bucket would be visibly stale on a page left open — worse than saying nothing precise at all. **"About a day ago" is used rather than "Yesterday"**, because "yesterday" is a calendar word in an elapsed-time ladder: at 10 a.m., something posted at 11 a.m. the previous day is 23 hours old and *was* yesterday, while something posted at 11 p.m. two nights ago is 35 hours old and was not. Getting that right would require storing each viewer's timezone, which §1.3 has no appetite for. **The long tail below 90 days is for pinned posts alone** — unpinned content is deleted at `CONTENT_TTL_DAYS`, so nothing ordinary can ever read older than "Over a couple of months ago"; the tail exists because pinned posts (§7.6) are exempt from expiry and may genuinely be years old.

**Two exceptions, both narrow.** The **expiry countdown** (§7.5) shows absolute days remaining. **Account and security events** (§4.6.1) carry absolute timestamps wherever they appear — they are security notices, not social content.

**Rules that keep this from leaking into the machinery.**
- **Display only.** Ordering, expiry, coalescing (§12.3), rate limits (§13.6), and data export (§4.9) always use the stored absolute timestamp. Two posts a second apart may read identically and still order correctly — the same posture as long-post folding, which never changes what is stored (§7.7).
- **The exact time appears nowhere in the interface.** No tooltip, no `title` attribute, no `datetime` attribute in the markup. Precise timestamps live in the user's data export (§4.9) and the operator's database, and nowhere else. This is a **substantive** choice rather than a presentational one, and it is load-bearing in two directions: a hover tooltip would fail §16.4's ban on meaning that depends on hover — touchscreens have no hover state at all and `title` is unreliably announced by screen readers — and a `datetime` attribute would quietly ship in the page source the very precision this section exists to withhold.
- **Computed per page load, never live-ticking** (§16.3, WCAG 2.2.2).
- **Emails carry no timestamp at all** (§12.3): a relative time is computed when mail is sent and read whenever the recipient opens it, so it would simply be false by then.

### 7.6 Pinning
- A user may **pin up to `PIN_LIMIT` = 10 of their own profile posts**. Pinned posts are exempt from expiry for as long as they remain pinned; unpinning a post older than 90 days deletes it. Feed posts can never be pinned. Pinning is the deliberate, editorial act of preservation — the only one on the platform.
- **Where pinned posts appear (v1.16).** On the **Pinned tab** of the author's profile (§9.1), folded at `FEED_FOLD_CHARS` rather than `BLOG_FOLD_CHARS` — that tab is a shelf, not a reading surface, and `PIN_LIMIT` posts of up to `POST_LENGTH_MAX` characters must not become the page. A pinned post **also** keeps its chronological place on the **Blog tab**, so the timeline is not full of holes; the two tabs are never on screen together, so nothing is duplicated in view. Unpinning a post under 90 days old simply returns it to ordinary status — it still expires 90 days from creation (§7.8, invariant 2).
- **A pinned post displays its age** under the ordinary relative-time rule (§7.5.1). Only the *expiry countdown* is replaced by the "pinned" marker (§7.5), never the age. The long tail of §7.5.1's ladder exists for this case and for no other. The age is not decoration: without it, a first-time visitor cannot tell whether *"we're moving to Lisbon next month"* is news or history, and the pinned tab is precisely where first-time visitors land.
- **A pinned post stays open for new comments**, which expire on their own 90-day clock like any others (§8.1). Its older comments are gone, and **nothing marks that they ever existed** — no tombstone, no "this post had comments." Two reasons: such a marker is a count in disguise, a signal about how much attention a post once drew, which §17 refuses everywhere else; and it is a permanent trace of an interaction whose whole point was to be impermanent.
- **The governing principle, stated because it will be needed again: an author may preserve their own words indefinitely, and may never preserve anyone else's.** Keeping comments alive for as long as a pin would let one person's editorial decision make another person's words permanent inside a 300-person group, without asking. That is the same refusal §7.8 makes when it lets a host delete a comment but never edit one.

### 7.7 The feed
- A user's feed contains, in **strict reverse-chronological order**: feed posts they are in the audience of, profile-update notifications from friends, and system notifications (friend requests, introductions, contact-card events, warnings).
- **No algorithmic ranking, ever. No suggested content, no inserted people, no ads, nothing the user did not subscribe to by friendship.** The feed is a mailbox, not a machine.
- **Long-post folding (v1.6):** a post longer than the surface's threshold is shown folded — the first characters up to that threshold (cut at a whitespace boundary) plus a "read more" control that expands the post **in place** — so one essay does not push everything else off the screen. Thresholds per reading surface: **`FEED_FOLD_CHARS` = 500** in the feed (a shared space where many authors compete for the screen) **and on the Pinned tab** (§7.6, §9.1), **`BLOG_FOLD_CHARS` = 2,000** on the Blog tab of a profile (§9.1; the reader deliberately visited this author's own space). Folding is display-only: it never changes what is stored or who can see it. A post opened directly (e.g., from a notification) is always shown in full. **Comments fold on a threshold of their own**, `COMMENT_FOLD_CHARS`, on every surface they appear on (§8.1).

### 7.7.1 Paging long lists (v1.16)

The feed and the Blog tab (§9.1) are both unbounded lists — 90 days of posts, and for a heavy poster that can run to hundreds. Neither had a navigation rule before v1.16.

- **Prev/next page links, and nothing cleverer.** A list shows the reader's chosen number of items; if more exist, a single **"Older posts →"** link at the foot loads a **new page**, which carries "← Newer posts" in turn. Ordinary page loads, ordinary back button, no script.
- **No page numbers and no total.** "Page 3 of 7" is a post count wearing different clothes, and counts do not exist here (§17).
- **No date-based archive.** This is foreclosed by rule rather than taste: a "March 2026" navigation requires absolute dates in the interface, which §7.5.1 forbids outright.
- **No infinite scroll and no "load more."** Both need JavaScript, which the architecture deliberately does without (§16.2); both lose the reader's place on back-navigation; both push the end of the document permanently out of reach of a keyboard user, stranding anything below the list. And infinite scroll in particular exists to remove stopping cues, which is the opposite of §1.1's commitment that nothing here tries to extend a visit.
- **The reader chooses the page size**, not the page author: `POSTS_PER_PAGE_DEFAULT` = 20, selectable from `POSTS_PER_PAGE_OPTIONS` = 20 / 40 / 60. It is one setting in the viewer's own preferences and applies to the feed and to every profile they visit. Per §16.3 it takes effect on an explicit **Apply**, never on the change of a dropdown (a control that reloads the page the instant it is touched is a 3.2.2 failure).
- On a normal profile the list fits one page and **no navigation is rendered at all**.

### 7.8 Editing posts and comments (v1.15)

Editing was unspecified before v1.15 — this document defined only deletion (§7.5). Silence was the wrong default and pointed the wrong way: because deleting a post destroys every comment and reaction on it (§7.5), an author with a typo was pushed toward delete-and-repost, which is the *more* destructive path and re-notifies everyone. Authors may edit.

- **What may be edited.** A post's text, its image (replacing an image re-prompts for alternative text — §16.3 requires a deliberate choice every time), its preformatted toggle (§7.2.1), and its hashtags. A comment's text. Nothing else.
- **The "edited" marker.** An edited post or comment permanently displays **"edited"** with the relative time of the most recent edit (§7.5.1), as real text beside its age. There is **no version history and no diff** — this is not an archive (§1.3), and honesty here needs only the fact and the approximate time.
- **No notification on edit** (§12.1). Re-notifying would make fixing a typo socially expensive, so people would stop fixing typos. Friends who already read a post may never learn it changed; the permanent marker is what keeps that honest.
- **Comments may be edited only by their author.** The post's author can delete any comment on their post (§8.1) but may never edit one: deleting someone's words is a host's prerogative, rewriting them is ventriloquism.
- **Bios are not covered by this section** — see §9.4. A bio is a current description of a person, not a statement made at a moment to a snapshotted audience with responses attached to it, so it carries no marker.

**Five invariants.** An edit:

1. **never re-snapshots the audience** (§7.4). The posting-time audience is fixed; an edit cannot add recipients. *One deliberate exception:* a profile post's hashtags are the FoF visibility gate, and §11.3 already evaluates that gate **live** — so adding or removing a tag does change which FoFs can see the post, by design. The *friend* audience is immutable either way, and newly-matched FoFs are never notified (§11.4 forbids discovery reaching the feed).
2. **never resets the expiry clock.** `CONTENT_TTL_DAYS` runs from creation (§7.5). Otherwise editing would confer immortality and pinning would stop being the only deliberate act of preservation on the platform (§7.6).
3. **never re-orders the post.** The feed is strictly reverse-chronological by creation time (§7.7). If an edit bumped a post, editing would be a reach trick.
4. **always re-runs every content validation** — URL allowlist including the open-redirector rule (§7.2, §7.2.3), length caps, whitespace normalization (§7.2.1), hashtag vocabulary (§11.2), and EXIF stripping and downscaling on a replaced image (§7.2.2). **This invariant is security-critical:** a save path that validates only on creation would let an author publish clean text and then edit a disallowed link into it, defeating the control §4.6.1 relies on to close the in-platform link-delivery vector. Validating only on create is a defective implementation of this section, exactly as a host-only allowlist check is a defective implementation of §7.2.3.
5. **is subject to the ordinary rate limits** (§13.6), so an edit loop cannot become an unbounded write channel. Editing does **not** consume `POST_MIN_INTERVAL_MINUTES`, which governs the spacing of *new* feed posts only (§7.3).

**Editing hashtags is an audience change, and is treated as one (v1.16).** Invariant 1's deliberate exception makes tag editing **the only audience-changing operation available after posting**, so it carries the same obligations as the composer:

- The editor shows the same live audience line as the composer (§7.9), updating as tags change. It is not a warning that appears only on "dangerous" choices — a notice people can learn to click through is worth nothing.
- Adding a tag to a post that **already has comments** re-exposes *those comments* to everyone the widening reaches. The commenters wrote to a stated audience and cannot have known. The editor therefore says so — *"This post has comments. Widening who can see it also shows those comments to the people it reaches."* — and **every existing commenter is notified** (§12.1). No new machinery is needed: commenting already turns following on (§12.3), so the delivery path exists, access is already re-checked at delivery, and the notification carries no excerpt (§12.2). By the test of §12 this is not invented bait but notice that a decision the recipient already made has changed underneath them, so that they may delete their comment if they wish.
- Removing a tag narrows the audience and notifies nobody; narrowing needs no consent from anyone.

**Accepted cost, recorded rather than solved.** With relative timestamps (§7.5.1), a reader can no longer tell from the display which comments predated an edit — so the "comments visibly older than the edit" check that would otherwise blunt a bait-and-switch is gone. On a bounded network of at most 300 vouched humans with no reach and no measurement, the permanent marker is judged sufficient; version history is not worth building to close the remainder.

### 7.9 Stated visibility — every post says who can see it (v1.16)

**Every post displays its audience, in plain text, to everyone who can see it**, on every surface — feed, Blog tab, Pinned tab, single-post view — and the comment box repeats it.

| Post | Line shown |
|---|---|
| Feed post | *"Visible to: the friends David sent this to."* |
| Profile post, untagged | *"Visible to: all of David's friends."* |
| Profile post, tagged | *"Visible to: all of David's friends, and friends-of-friends with **any of** #hiking, #jazz."* |

At the comment box: *"Your comment will be visible to the same people."*

**Why this exists.** §8.1 records that a commenter's words on a hashtag-gated post are readable by people who are strangers to them, and calls the consequence consciously accepted. It was accepted by **this document**, not by the commenter, who until now had no way to know. Disclosure is what makes that sentence true.

**Rules.**
- **The line is derived from the post's own type and tags, never from the viewer** — one string per post, not a per-viewer computation.
- **Every tag on the post is named, and the word is "any of" (v1.18).** One shared tag satisfies the gate (§11.3), so the line lists all of the post's tags and says so. A line naming one tag on a post carrying three would understate the audience to the one person who most needs it stated correctly — the author, at the moment they can still change it.
- **Never a number.** A live count of matching friends-of-friends would be a visible count (§17) and, worse, a **privacy oracle**: added one tag at a time and watched, it would enumerate how many of the author's FoFs carry each interest. §1.2's own argument is that a campaign which cannot be measured cannot be optimized; a match counter is a measuring instrument. Naming the rule reveals nothing; naming the number reveals the graph.
- **Never the audience itself** on a feed post. Naming or numbering the recipients would expose the author's audience choices to every recipient — a real disclosure and a social minefield. The fixed phrase says only what the model already guarantees.
- It is **real text**, not an icon or a colour (§16.4), and updates in the composer and editor through a polite live region (§16.3, 4.1.3).

**No-Reach Test and "never infers."** The line widens no audience and creates no new access; it states a rule the platform mechanically enforces, computed from the post's own stored fields. It passes both by construction.

**Reporting a tag that does not belong (v1.21).** §11.3's gate is satisfied by **any** shared tag, which makes tagging an audience control and makes **irrelevance the abuse that is actually available** — a post tagged #jazz with nothing to do with jazz, carried to every friend-of-friend who declared an interest in jazz. Note how narrow the vocabulary makes that: tags are never free-typed (§11.2), so nobody can invent a tag or coin a coded one, and over-tagging with real interests is the whole of what is left. The person best placed to notice is the friend-of-friend who received the post *because* of the match — and this line is precisely what tells them the match is why. **The affordance therefore goes where the explanation already is: on a tagged profile post, the report action (§13.2) sits with the visibility line**, carrying a reason for exactly this case (*"the tags don't match this post"*). Three things it deliberately does not become:

- **The line itself is unchanged.** No new words in the table above, no per-viewer computation, and never a number — the rules above are not relaxed to make room for this.
- **No per-tag report count is surfaced anywhere** — not to users, and not as a flag or a ranking on the tag in the operator console. A tag is not a thing that can be in trouble; a post is, and a person is.
- **Nothing detects irrelevant tagging automatically.** §13.2 declined automated content-similarity detection on cost/benefit grounds rather than principle, and every word of that reasoning applies here with more force: relevance has no threshold, and any detector would misfire on the legitimately eclectic post — which, on a platform for friends, is most of the good ones.

**§17's parked "per-post friends-only comments" switch stays parked**, and the reason is recorded so it is not re-proposed as new. The parked name is ambiguous between *only friends may write* and *only friends may see comments*, and only the second would actually help — a FoF barred from commenting still reads the comments, so the commenter's exposure is unchanged. The second version breaks §8.1's single-line invariant (*a comment is visible to exactly the people who can see the post — never more*) and would require a second visibility model layered over §11.3. Disclosure is the smaller change with the larger effect. The coherent stronger alternative — hiding comments from hashtag-matched FoFs entirely, making their view read-only — is recorded as considered: it would restore a one-line rule and strengthen §1.1's telos (discovery shows you the person; friendship gets you the conversation), but it reverses §11.3's grant of comment rights and removes what §8.1 calls a deliberate surface where people meet through mutual friends, which is a founding purpose. Not adopted for v1.

---

## 8. Comments and Reactions

### 8.1 Comments
- Who can comment = who can see the post (§7.4, §11.3). **A comment is visible to exactly the people who can see the post — never more.** Nothing about commenting propagates content anywhere.
- Consciously accepted consequence: on a profile post, a commenter's words are readable by the author's other friends, who may be strangers to the commenter (bounded: ≤ 300 vouched humans; this is also a deliberate surface where people meet through mutual friends).
- **Attribution:** every comment displays its author's display name and its age (§7.5.1). The name **links to the commenter's profile when the viewer has at least basic-tier access to that commenter** (friend or FoF, §9.2); for a viewer with no connection to the commenter (possible on hashtag-gated posts, §11.3, where two viewers of the same post may be strangers to each other) the name renders as plain text, not a link. Note the consequence, which is deliberate: on an ordinary friends-only post the name *always* links, because any two friends of the same author necessarily share that author as a mutual friend and are therefore FoFs of each other. The plain-text case arises only on hashtag-gated posts.
- **The same rule governs every rendered name, everywhere (v1.16):** post authors, mutual-friend names in "the people you both know" (§9.1, §11.5), and the names in an author's private reaction list (§8.2). One shared helper decides link-or-plain-text, as one shared helper renders the name itself (§4.5.1) and another renders its age (§7.5.1). On the Blog and Pinned tabs the post author's name is **not rendered at all** — every post there belongs to the profile's owner, whose name is in the header above it (§9.1).
- **Every post states its audience** (§7.9), and the comment box repeats it, so a commenter always knows who they are speaking to before they speak.
- **Flat** — one linear list per post; no nested replies in v1.
- Same content rules as posts (§7.2, §7.2.1) except: no images in comments, no preformatted toggle, and the smaller `COMMENT_LENGTH_MAX` = 2,000 length cap. Whitespace normalization applies as for normal posts.
- **Long comments fold (v1.18).** A comment longer than `COMMENT_FOLD_CHARS` = **300 characters** is shown folded — the first characters up to that threshold, cut at a whitespace boundary, plus a "read more" control expanding it **in place** — on every surface a comment appears on. The mechanism is §7.7's exactly, and display-only in the same way: nothing stored changes and nobody's access changes. The threshold is deliberately tighter than the feed's `FEED_FOLD_CHARS`, because a comment is a guest in the post's space and a thread is many voices competing at once: at `COMMENT_LENGTH_MAX` = 2,000 a handful of unfolded comments would bury the post they belong to, which is the same failure long-post folding exists to prevent. Each control carries its own distinct accessible name (§16.3) — *"Read more of Alice's comment"* — because a thread produces many of them.
- Comment authors can delete their own comments, and may **edit** them under §7.8. **The post's author can delete any comment on their post** (host's rules — the cheapest moderation tool) but can never edit one (§7.8).
- Comments and reactions on a post generate a coalesced notification to the post's author, and to anyone following the post (§12.1, §12.3).
- Comments expire with their post, or at their own 90 days, whichever comes first. **A pinned post is not an exception**: it is exempt from expiry itself (§7.6), but comments on it still die at 90 days and leave no trace, and the post stays open to new ones.

### 8.2 Reactions (no likes)
- There are **no like buttons, no counters, no public reaction displays of any kind.**
- A user may attach **one reaction per post or comment**, chosen from a fixed, operator-curated picker of ~6 warm phrases (`REACTION_SET`; e.g., "Agreed!", "Love it!", "So proud!", "Thinking of you", "Congrats!", "Ha!"). Changeable or removable at any time. No free text, no arbitrary emoji.
- **Reactions are visible only to the author of the reacted-to content, shown as names, never as numbers** ("Alice: Love it! · Mom: So proud!"). Other viewers see nothing — no counts, no indicators. This is deliberate: warmth without scorekeeping; no validation economy.
- **Reactions never render in a list view (v1.16).** They appear on a single-post view only — never on the Blog tab, the Pinned tab, or the feed. The reason is specific: an author's own Blog tab is a column of their own posts, and reaction names printed under each one, with nothing under others, is a comparison surface that assembles itself. That is precisely the "not comparable across posts" property this section exists to protect, and it would have been lost to a layout decision rather than to a decision.

---

## 9. The Profile Page

### 9.1 Structure: a persistent header and four tabs (v1.16)

The profile is a **persistent header** above **four tabbed views**. This replaces the single scrolling page of five stacked sections (identity header → pinned posts → about → gallery → blog) specified through v1.15, which placed up to `PIN_LIMIT` × `POST_LENGTH_MAX` characters of unchanging content between a returning friend and the one thing that had changed — a cost §1.1 does not accept ("nothing here competes for a user's attention or tries to extend a visit").

**The persistent header**, shown above every tab, carries the owner's **profile photo**, their **display name** (rendered live through the shared helper, §4.5.1), and the **report action** (§13.2). Nothing else. It scrolls with the page and is never sticky, which would cost screen height on a phone and complicate the 320 px reflow requirement (§16.3). The report action belongs here rather than inside a tab because the profile photo is the one thing on the platform that cannot be screened (§13.6), and a friend-of-friend — who has exactly one tab — is the person most likely to need it.

**The four tabs**, in this order, with **Blog** as the landing tab:

| Tab | Contents |
|---|---|
| **Blog** | Every post by the owner **that this viewer may see**, newest first: profile posts, pinned posts in their chronological place, and feed posts the viewer was in the audience of. Folded at `BLOG_FOLD_CHARS`; paged per §7.7.1. |
| **Pinned** | The owner's pinned posts (§7.6) — the author's curated shelf. Folded at `FEED_FOLD_CHARS`. |
| **Photos** | The image gallery (§9.4). |
| **About** | Short bio, extended bio (friends only), interest hashtags, and **the people you both know** (§9.2, §11.5). |

- **Tabs are links to separate URLs**, server-rendered and styled as tabs — never a scripted tab widget. The back button works, each view carries its own descriptive page title (§16.3, 2.4.2), and no ARIA tab pattern has to be implemented correctly for the page to be operable.
- **A tab is rendered only where this viewer has something in it**, and **when only one tab qualifies, no tab strip is drawn at all** — a lone tab reads as a broken interface.
- **The photo is not repeated inside About.** The header carries it.
- **Posts on the Blog and Pinned tabs do not repeat the author's name** (§8.1). Everything there is the owner's, and the header says whose page this is. Comment authors are still named.
- The two bio fields, their caps and their differing rules are §9.4; the profile carries no structured biographical fields at all (§9.6); nothing on the profile expires except posts and comments (§9.7).

**Feed posts on the profile (v1.16).** A feed post now appears on its author's Blog tab as well as in its recipients' feeds. **No audience widens.** §7.4 is untouched — the posting-time snapshot *and* current friendship both still govern, so exactly the people it was sent to can find it here, and **a friend-of-friend never sees a feed post at all**, since §11.3 gates profile posts only. What changes is retrievability: for its 90 days a feed post is findable by pull rather than only by scrolling back through a feed. Two friends therefore see substantially different Blog tabs on the same profile, and neither can tell what the other sees — accepted, and the reason §7.9's stated-visibility line does real work on this surface.

**The basic-tier invariant.** The header plus the About tab, minus the extended bio, is **exactly** §9.2's basic tier, and **exactly** what §5.2's friend-request card shows. All three render from one component with one friends-only flag. This is a requirement, not an observation: if the three surfaces drift apart, the screening arguments of §5.2 and §13.1 quietly stop being true.

**What a non-friend sees.** A friend-of-friend gets the header and the About tab, and **below that content — never above it** — one line: *"You and David are not friends. Friends see his posts, photos and about section."* Content first, then the explanation of what is missing; leading with it makes the page read as a refusal rather than a profile. The line is **unconditional**, shown whether or not the owner has ever posted: a line that appeared only when content existed would tell a non-friend whether there is anything to miss. A viewer with no mutual friend at all, and a viewer on either side of a block (§5.4), get the response of §9.3 instead — the profile does not exist for them, indistinguishably from one that never existed.

### 9.1.1 Theming

Fixed layout (no freeform customization), with limited theming: font choice and color scheme from operator-curated sets (`THEME_SET`; **every scheme must meet the WCAG 2.1 AA contrast ratios of §16.3 in every combination in which it can appear** — this is why theming is curated rather than freeform). Theming changes type and colour only, **never layout**; otherwise the reflow and 200 %-zoom guarantees of §16.3 would need re-verifying per theme, per profile.

**Theming attaches to spaces, never to content (v1.4):**
- A user themes their **own app view** — feed and all reading surfaces — for themselves only.
- A user themes their **profile page**; visitors see that theme (your living room, your wallpaper).
- Comments and feed posts **never carry their author's theme** — they render in the theme of the surface they appear on (a comment is a guest in the host's house). Rationale: sender-styled content invites an attention arms race (loudness as reach) and degrades readability; the feed is the reader's mailbox (§7.7).
- **Viewer override:** an "always use my own theme" setting renders every page, including friends' profiles, in the viewer's own theme (accessibility and consistency). It is applied **server-side at render**, never as a client-side toggle a page could defeat — §16.3 requires that a page author can never override it, and that is an implementation constraint, not only a policy.
- **Preformatted posts are exempt (v1.6):** a post's preformatted/monospace rendering (§7.2.1) is **structural content, not theming**, and survives every theme, including the viewer override — rendering ASCII art or a text table in a proportional font would destroy it. Only the monospace-ness is exempt; colors and everything else still follow the surface's theme.
- Long-post folding applies per §7.7: `BLOG_FOLD_CHARS` on the Blog tab, `FEED_FOLD_CHARS` on the Pinned tab.

### 9.2 Visibility tiers
| Viewer | Sees | Tabs |
|---|---|---|
| **Friends** | Everything: both tiers, every post they may see, gallery, and the extended bio (§9.4). | Blog · Pinned · Photos · About |
| **FoFs (any mutual friend exists)** | **Basic tier only:** display name, profile photo, **short bio** (§9.4), profile hashtags, and the specific mutual friends they share with the owner ("knows Alice and Tom"). | About only — and therefore no tab strip (§9.1) |
| FoFs with a **matching profile hashtag** | Basic tier **plus** the owner's profile posts tagged with a shared hashtag (§11.3). | About, plus Blog and Pinned filtered to matching posts; each omitted if nothing matches |
| Everyone else (no mutual friend), and either party of a block (§5.4) | Nothing. The profile does not exist for them (§9.3). | — |

**What the hashtag-matched FoF sees, exactly (v1.16).** On the Blog and Pinned tabs, only posts carrying at least one hashtag the **viewer also carries on their own profile**, under all three live conditions of §11.3 — newest first, ordinary folding, ordinary ages. **Feed posts never appear**: §11.3 gates profile posts only. Non-matching posts are **absent with no placeholder** — no "some posts are hidden," which would be an oracle telling a non-friend how much they are missing. If nothing matches, the tab is not rendered. Comments on a visible post are visible, with commenter names rendering as plain text where this viewer has no connection to the commenter (§8.1). The gallery and the extended bio remain invisible. A consequence worth stating: this viewer's entire impression of a profile can be one pinned post several years old — which is an argument for the age display of §7.6, not against it.

### 9.3 Access rules
- No profile, post, or image is ever accessible without login. **No deep links:** URLs must not function as shareable pointers to profiles or posts; internal identifiers must be non-guessable, and every request is permission-checked against the viewer (a leaked URL shows a stranger nothing).
- **An address is never built from a name (v1.18).** The address of a profile or a post derives from the account's permanent internal identifier (§4.6), never from a display name — which is neither unique (§4.5) nor stable (§4.5.1). Two people may hold the same name, so a name-derived address would collide between them; a name may change, so it would break for whoever changed theirs. Two behaviours follow, and they are the reason this belongs in the specification rather than only in the architecture: an address keeps working across a name change, and no address can be constructed by guessing at a name.
- **What "no deep links" does and does not promise (v1.16).** In-app links exist and are required — commenter and author names (§8.1), discovery (§11.4), the friends page (§11.6), notifications (§12.2). URLs are **stable and non-guessable**, and the guarantee is the permission check, not the URL: a leaked address shows a stranger nothing. It follows that an address copied out of the browser and sent to someone over another channel **does** work if that person already has permission. That is manual re-propagation, which §17 places out of scope, and it is stated here so this section is not read as promising more than it delivers.
- **A viewer who may not see a profile gets one response**, identical for a block (§5.4), no mutual friend, a deactivated account (§4.7), and a profile that never existed. Any variation between those cases is an oracle.
- Profile updates generate **only a notification**, and only for the event types listed in §12.1 — most changes are silent. Content is never pushed, and a notification never carries an excerpt (§12.2).

### 9.4 Limits, the two bio fields, the gallery, and the photo (v1.16)

**The two bio fields**
- **Short bio** (About tab, and the one field that travels): `BIO_SHORT_MAX` = **200 characters**. Visible at the basic tier, to FoFs as well as friends (§9.2), and appearing in the friend-request card (§5.2) and wherever basic-tier context is rendered. Rules that follow from that exposure: it is **screened at every save** against `NAME_BLOCKLIST` as display names are (§4.5); the friend-request **send hold** of §13.6 follows a change to it; and it **never renders clickable links**, not even allowlisted ones.
- **Disallowed URLs in the short bio are rejected at save (v1.16)**, with the message of §7.2.3 — not merely rendered inert. Earlier wording claimed that "a field with no links is a field that cannot deliver one," which overstated the control: an unclickable address is still readable, and a reader can retype it. The honest claim is now what is actually true — **the short bio cannot deliver a clickable link, and recognizable disallowed URLs are refused** — while obfuscated text ("weebee dash social dot com") remains beyond any such rule, exactly as it is everywhere else.
- **Extended bio** (About tab, friends only): `BIO_EXTENDED_MAX` = **2,000 characters**, matching `COMMENT_LENGTH_MAX`. Because the cap equals `BLOG_FOLD_CHARS`, the fold can never trigger and the field needs no fold rule of its own. **Friends only** (§9.2), so it is not a push surface: no send hold follows a change to it, and allowlisted links **are** permitted (§7.2.3). Screened at save as the short bio is.
- **Whitespace (v1.16).** The extended bio follows the **normal-post whitespace rules of §7.2.1** — line breaks preserved, one blank line between paragraphs, two consecutive spaces, trimmed at the ends, normalized once at save. The **short bio additionally collapses every line break to a space**: 200 characters has no paragraphs, and a short bio full of newlines is a layout attack on the header of the friend-request card, a surface delivered unasked to up to 20 people a day. **Neither bio has a preformatted toggle.** That toggle exists to permit a documented reflow exemption for artwork (§7.2.1, §16.3), a bio is not artwork, and granting the exemption to a field that never expires (§9.7) is worse than granting it to one that dies in 90 days.
- **Neither bio carries an "edited" marker or history** (§7.8), and bio changes notify nobody (§12.1) — the change announces itself to the next visitor, as a name change does (§4.5.1). Every save nonetheless re-runs full validation, or the screening above would be decorative.
- **Clearing the short bio to empty triggers no send hold**, and a save rejected by screening never starts one (§13.6): retraction always stays free, per the §10.3 principle that the recoverable direction is the unrestricted one.
- The term **"one-line bio" is retired** as of v1.15: 200 characters is not one line, and the phrase was a layout hint that had become a specification term by accident.

**The gallery** (Photos tab)
- `GALLERY_MAX` = 8 images, separate from the profile photo. Friends only (§9.2). EXIF stripped (§7.2); sizing, scale-to-fit and the click-to-expand overlay per §7.2.2.
- **No caption field. The alternative text is the caption (v1.16)** — the uploader-authored description every image already carries (§16.3, up to `ALT_TEXT_MAX`) is **displayed visibly** in the expand overlay. One field instead of two: two fields on one image reliably produce a written caption and a blank alt, or the same string in both, which makes a screen reader announce it twice. This also turns alternative text from an accessibility tax into the thing the author wanted to write anyway. Markup: the thumbnail is `<img alt="{text}">`; the overlay is `<figure><img alt=""><figcaption>{text}</figcaption></figure>`, empty alt precisely because the caption is present and is the description. Anyone wanting to *comment* on a picture rather than describe it writes a profile post, which expires, takes comments, and does not accumulate.
- **Order is author-arranged**, new images placed first on upload and freely rearranged thereafter. This is the user stating intent, not the platform inferring it (§1.3) — the contrast is §6's ban on auto-populating groups. Reordering is performed with **"Move up" / "Move down" controls named from the image's own alternative text** ("Move 'Me on a beach in Cornwall' up"), with the result announced in a polite live region (§16.3, 4.1.3). Drag-and-drop may be offered **in addition**, never instead: a reorder only a mouse can perform is a 2.1.1 failure.
- **Replacing an image re-prompts for alternative text**, exactly as §7.8 requires when a post's image is replaced — §16.3 requires a deliberate choice every time. The same applies to the profile photo.
- Notifications: additions and replacements notify friends, coalesced; removals and reordering notify nobody (§12.1).

**The profile photo (v1.16)**
- Every account has a profile photo at all times; there is no "no photo" state. At account creation the account is given the **designated default member of `DEFAULT_AVATAR_SET`**, an operator-curated set of platform-supplied images that is also offered as a picker. A user may at any time upload their own image or choose any member of the set.
- `DEFAULT_AVATAR_SET` images are **original artwork and never photographs of people** — a stock human face reads as impersonation and defeats the recognition the photo exists for. The platform authors their alternative text, which is the one deliberate exception to §16.3's uploader-authored rule and is recorded here rather than left implied.
- Because every new account wears the same default image, that image is in practice the "hasn't chosen one yet" signal. No separate state is added on top of it.
- **Changing the photo is free and unlimited.** The limit sits on the push instead: sending friend requests is held for `REQUEST_HOLD_AFTER_PROFILE_CHANGE_HOURS` after an **upload** (§13.6). **Selecting a picker image triggers no hold and no notification** — a platform-supplied image cannot carry abuse, and swapping to one is the retraction direction, which stays free everywhere else in this section. Uploading a photo notifies friends, coalesced (§12.1).
- **Editing an image's alternative text alone changes nothing else:** no hold, no notification, on any image. The image is unchanged, and a person who realizes their description was poor must not have to wait to fix it.
- Profile hashtags: `PROFILE_HASHTAG_MAX` = 10.

### 9.5 Preview-as (required feature, v1.16)
The owner can preview **their profile page, their contact card, and the card their friend requests display** exactly as another person would see them. Four modes:

1. **As a specific friend** — a picker over the friend list. Required because the contact card is per-friend (§10.3) and the mutual-friend block is per-viewer.
2. **As a generic friend-of-friend** — the basic tier, with the mutual-friend block shown as a placeholder, since the actual names depend on which FoF.
3. **As a friend-of-friend carrying a chosen hashtag** — a picker over **the tags present on the owner's own profile and pinned posts**, which is the only set that can change the result; any other tag collapses to mode 2. Shows the Blog and Pinned tabs filtered exactly as §11.3 will filter them. This is the tier nobody can compute unaided, and it was missing from every version before v1.16.
4. **As it appears in a friend request** (§5.2) — not a profile view, but the highest-consequence view of the short bio and photo, shown to people who never asked for it, and the surface on which §5.2's and §13.1's honesty rests.

There is deliberately **no "as a specific friend-of-friend" mode**: the owner cannot enumerate their FoFs, and offering that picker would leak a friend list in the opposite direction. Preview-as is read-only, changes no state, sends no notification, marks itself with persistent real text, and is exitable by keyboard.

### 9.6 Structured profile fields — considered and rejected (2026-08-01)
The profile carries free text (the two bio fields of §9.4), a photo, a gallery, and vocabulary hashtags. It carries **no structured biographical fields** — no relationship status, location, birthday, employer, school, or equivalent — and v1 adds none.

Three reasons. **Structured fields are matchable and sortable in ways free text is not**, which is exactly the machinery a platform with no global search, no ranking and no inference has no use for (§1.3, §11.2) — the field would be built for a capability the platform refuses to have. **They enlarge the collected-data surface** against the data-minimalism principle (§1.3) and the minimal-collection posture the GDPR position of §15.1 rests on; registration deliberately collects nothing beyond an email, a name and an age attestation (§4.1), and the profile should not quietly reintroduce a dossier. And **a relationship-status field in particular invites the single most notorious engagement-bait notification in the industry's history** — precisely the category §12.2 bans by name.

Anything a person wants said about their life can be said in a bio or a post, in their own words, at whatever granularity they choose. If structured fields are ever revisited, the notification policy does not come with them: they would alter the profile **silently** (§12.1).

### 9.7 Permanence — what expires and what does not (v1.16)

**Statements expire; descriptions do not.**

§7.5's 90-day rule governs **posts and comments** — things said at a moment, to an audience, with responses attached. It does not govern **account state**: the profile photo, the gallery, both bio fields, profile hashtags, the contact card, groups, and the friend list. These persist until the user changes or removes them, and are destroyed with the account on erasure (§4.7) or after two years of inactivity (`INACTIVITY_DELETE_DAYS`, §4.8). "Permanent" here therefore means *until you change it, delete it, or go dormant for two years*.

Until v1.16 this was true only by silence, which is not a decision. The distinction itself was already half-written in §7.8: *"A bio is a current description of a person, not a statement made at a moment to a snapshotted audience with responses attached to it."* Expiry follows the same line.

**The gallery is the only member of this list that resembles content, and the cap is what makes it not content.** `GALLERY_MAX` = 8, every slot owner-replaceable and owner-deletable, so **the gallery cannot accumulate**. Expiry exists to prevent accumulation and to refuse to be an archive (§1.3); a fixed eight-slot shelf is neither. Nobody expects a friend list to empty itself every 90 days, and the gallery is in that category, not the post category.

**Expiring the gallery was considered and rejected (2026-08-03).** It would force re-uploading the same photographs four times a year, multiply trips through the alternative-text prompt, churn storage for no gain, and leave the least frequent visitor with the emptiest profile — punishing precisely the low-frequency user this platform exists for.

**Consequence for public copy.** The platform does not claim that everything is deleted after 90 days, because it is not. The honest form, which is also the better one: **everything you *say* is deleted after 90 days; what you *are* — your photo, your bio, your gallery — stays until you change it.** All user-facing and project-facing copy uses this form.

---

## 10. Contact Cards (there is no DM system)

### 10.1 Principle
The platform has **no free-text direct messaging**. Person-to-person conversation belongs on channels users already trust (phone, email, messengers). The platform's job is the *introduction and the handoff*, via a structured contact card.

**Why (v1.12): this is a solved problem, and solving it again would make WeeBee a walled garden (§1.3).** Email, SMS, the messengers people already run, other platforms' DMs, and ordinary postal mail all carry person-to-person conversation perfectly well, on channels the user already chose and already trusts. A platform that rebuilds messaging is not adding a capability — it is trying to own a relationship it did not create, and making itself harder to leave. WeeBee's contribution is the part that is genuinely *not* solved: the structured, consent-based handoff. Then it gets out of the way. (A useful side effect rather than the motive: having no in-platform message channel is what closes most phishing delivery vectors — §4.6.1.)

**Scope of this decision:** the rationale above is durable, but the decision itself remains **v1-scoped**. No DMs in v1 (§17), the door is left open, and the E2EE-reconsideration clause of §15.5 stands should that ever change.

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
- **Hashtags are never free-typed.** All hashtags — on profiles and in posts — are chosen from a single operator-curated, platform-wide **interest vocabulary** (`HASHTAG_VOCAB`) via a searchable picker. Rationale: free-typed tags fragment the same interest across synonyms (#hiking / #hikes / #trailwalking), silently preventing the matches the feature exists to create; curation also blocks abusive or coded tags. Users may submit new-tag suggestions for operator review (§13.5); how those are handled, and what makes them rare, is §11.2.1.
- Users may put up to 10 vocabulary hashtags on their **profile** (interests: #hiking, #jazz) — visible at the basic tier.
- Hashtags may also be written in **posts**. On **feed posts** they are decorative/ranking signals only — they never change the audience. On **profile posts** they act as the FoF visibility gate (§11.3).
- **Hashtags are matching signals, never global navigation: there are no global hashtag feeds, no network-wide search *by* hashtag for people or posts, no "see all posts tagged #x" anywhere on the platform.** (Searching the *vocabulary itself* in the picker — a static operator-written word list naming nobody — is a different thing and is specified in §11.2.1.) The only hashtag-driven views are the FoF-scoped ones below and the viewer-scoped tag filter of §11.4.
- **Clickable hashtags (v1.3):** clicking a hashtag anywhere opens the **discover page filtered to that tag** (§11.4). This passes the No-Reach Test because it only reorganizes what the viewer can already see — it never widens any audience and does not loosen the §11.3 gate.

### 11.2.1 The vocabulary as an operational commitment (v1.21)

Curation is settled (the rationale above stands), but a curated vocabulary is a **promise the operator has to keep every week**, and until v1.21 this document made that promise and then said nothing about how it is kept. That silence mattered more here than it looks: §11.3 makes a profile hashtag one of three conditions for friend-of-friend visibility and §11.4 makes it the ranking signal on discover, so **the vocabulary is the substrate of the entire friend-discovery mission** (§1.1's second purpose). A user whose real interest has no tag is not inconvenienced — they are invisible to exactly the people this platform exists to introduce them to, with nothing telling them that is why.

**The starter vocabulary is the actual answer, and it is content work, not machinery.** The vocabulary ships **broad enough that suggesting a tag is the exception rather than the workflow**, written by hand and weighted toward *things people do with other people, offline* (§1.1: the measure of success is offline). Everything else in this section is a fallback for the cases a good starter list misses. **No size is stated here on purpose:** it is not a cap, nothing enforces it, and a number in this document would be the only content target in a specification of behaviour. The target and the method live in BUILD_PLAN Phase 10, where the writing actually happens.

**Aliases: the picker searches more words than it displays.** Every vocabulary entry carries a set of **operator-curated search aliases** — `#hiking` carries *hikes, rambling, trekking, trail walking*. Searching any of them finds `#hiking`. Aliases are **never displayed, never selectable, and are not tags**: they are search terms that route to a canonical entry, so the picker can answer a user who knows their interest by a different word than the one the vocabulary chose. This is the same anti-synonym decision as the curation rule itself, made once and stored, rather than being lost every time a synonym is declined.

**What that does to the decline path, which is the point.** The commonest suggestion is not a missing interest but a **synonym for one already present**. Without aliases, declining it teaches nobody anything and the next user types the same word into the same empty result. With them, the operator's decline *is* the fix: add the word as an alias to the canonical tag, and the miss never happens again. **A declined suggestion is therefore normally a permanent improvement to the picker rather than a dead end** — which is what stops the suggestion queue growing with repeats, and is the single largest reduction in operator load in this section.

**The empty result is honest, and it is where suggesting happens.** When a search matches no tag and no alias, the picker says so plainly and offers the suggestion form (§13.5) — it never presents a text field that would accept a tag and then silently fail to create one. **This is search over a static list, not the global search §17 forbids.** The distinction is not a technicality: §17's rule protects *people and content*, and querying `HASHTAG_VOCAB` returns neither. It reveals nothing about who is on the platform, what they are interested in, or what anyone has written — the same vocabulary is returned to every user, including one with no friends at all. (The friend-list filter of §11.6 is admitted on a different ground: it searches real people, but only the viewer's own 300.)

**What the submitter is told — and what they are not.** On submitting a suggestion the user is told, in the confirmation itself, that **suggestions are read in batches rather than one at a time, that no reply is sent, and that an accepted tag simply appears in the picker.** That is the whole of the communication, and it is deliberately compatible with §13.5: no per-suggestion reply, no status page, no "pending" state visible to anyone, no notification machinery. **A per-suggestion outcome message would be a promise about the operator's time**, and the operator is one person; the honest thing is to promise nothing and describe the rhythm. Nothing is said about *how long* — a cadence lives in the operator's runbook (BUILD_PLAN §17.3), where missing it costs an unread queue, and not in a message to a user, where missing it is a broken promise.

**Accepted cost, recorded rather than solved: the operator is a single point of failure, and stays one.** Vacation, illness, a bad month — the vocabulary is frozen for as long as the operator is away. Nothing here changes that, and no mechanism proposed so far changes it without giving up curation. It is survivable, and the reason is the shape of the load rather than optimism: **the starter vocabulary carries the ordinary cases**, **aliases absorb the synonyms**, and a frozen vocabulary is a **delay in gaining a new interest, never a loss of an existing one** — every tag already on a profile keeps working, every §11.3 gate keeps evaluating, and discovery is unaffected for everyone already tagged. Three weeks of silence costs some new users some matches they would otherwise have had, later than they would have had them. That is the cost, it is named, and it is accepted rather than engineered against.

**Two proposed fixes — considered and rejected (2026-08-17).** Both came from an external review of v1.16 that correctly identified the operator load and then proposed the two obvious remedies. They are recorded with their reasons so they are not re-proposed as new.

- **"Auto-approve a tag once three users suggest it."** Three users suggesting *#hiking*, *#hikes* and *#trail walking* are one interest arriving three times; approving all three creates precisely the synonym fragmentation curation exists to prevent, and does so *automatically*, which is worse than doing it by hand because nobody sees it happen. It also removes the abuse screen entirely, and three coordinated accounts is a low bar on a network where every member holds invites (§4.2). The count itself would additionally have to be kept off every user-facing surface (§17). **Aliases are the version of this idea that works**: repeated suggestions of a synonym are exactly the signal that an alias is missing, and the operator acts on that signal without a new tag being created.
- **"Allow free-typed tags that simply don't match anything unless they are in the vocabulary."** This is a text field that accepts input and silently does nothing — worse than a refusal, because the user believes they have tagged their post and cannot discover otherwise. It reintroduces free text on a surface that carries none (§13.1), which would then need screening (§4.5), and it would produce a class of post whose §7.9 visibility line names tags that gate nothing.

### 11.3 Hashtag-gated FoF visibility (symmetric consent)
A profile post is visible to a viewer V (beyond the author's friends) iff **all** hold:
1. V is a FoF of the author (≥ 1 mutual friend, no block between them), and
2. the post carries at least one hashtag (the author declared it discoverable by tagging it), and
3. **at least one** of the post's hashtags is also among V's own **profile** hashtags (the viewer declared the interest) — one shared tag is enough.

**One shared tag, not all of them (v1.18).** Condition 3 is existential over the post's tags, never universal: a post tagged #hiking #jazz #cornwall is visible to a FoF carrying any one of the three, not only to a FoF carrying all three. Earlier wording put the whole rule in the singular ("a post tagged #x … V has #x") and left the multi-tag case to inference. §9.2 and §11.4 both already assumed "any", so this corrects §11.3 to match the rest of the document rather than deciding anything new — and the failure it forecloses is a silent one: a builder implementing "all" would simply have hidden posts that should have appeared, with nothing anywhere raising an error.

**The consequence, stated in the same breath because it is a property of the design and not a side effect: a post carrying ten tags reaches a wider friend-of-friend audience than a post carrying one.** Tagging a profile post is therefore an **audience control**, not a filing decision. That is precisely what §7.9's stated-visibility line exists to put in front of the author while they compose, and again whenever they edit tags (§7.8).

Such viewers may also **comment** on that post (author-delete and block are the safety net). Access is evaluated live: if the last shared tag disappears from either side, or the mutual friendship lapses, access ends.

### 11.4 The discover page (pull-only)
One dedicated page the user must deliberately visit. It contains:
- **People suggestions:** FoFs, ranked by shared mutual friends and shared profile hashtags, each shown with auto-context ("knows Alice and Tom · shares #hiking").
- **Matched posts:** hashtag-gated FoF profile posts per §11.3.
- **Tag filter (v1.3):** the discover page can be filtered to a single hashtag (reached by clicking that tag anywhere). The filtered view shows: connected people (friends and FoFs) who carry the tag on their profile, and already-visible tagged profile posts — friends' posts always; FoFs' posts only when the §11.3 conditions hold (in particular, the viewer must carry the tag too). The filter reveals nothing the unfiltered rules don't already permit; it is aggregation of the viewer's existing visibility bubble, consciously accepted as serving the friend-discovery mission.
**Nothing from discovery ever appears in the feed.** No push, no notification, no "someone viewed you."

### 11.5 Friend-list visibility (amended v1.16)
On a profile, a viewer sees **only the friends they have in common with that person** — rendered as names, never as a count ("knows Alice, Tom and others", never "and 12 others"; §12.2's idiom). Full friend lists are never exposed. This appears on the About tab (§9.1).

**The hashtag-matched clause is deleted (2026-08-03).** Through v1.15 this section also showed a viewer *that person's hashtag-matched non-mutual friends*. It was removed for three reasons. It was the **only place on the platform that revealed a friendship the viewer is not part of** — discovery (§11.4) shows that a FoF exists and what they are interested in, but never whose friend they are. It gated that disclosure on a criterion unrelated to it: shared interest is not consent to have one's friendships enumerated. And it was **enumerable**: profile hashtags may be changed at will (nothing rate-limits them) and changes are deliberately silent (§12.1), so a viewer could rotate ten tags at a time through `HASHTAG_VOCAB`, revisiting a profile after each change, and map much of that person's friend list without the owner ever knowing. The exposure was bounded to FoFs and slow, but it defeated the rule a user actually believes — *people can only see the friends we have in common* — which is now simply true. Deleting it also resolves an inconsistency: §11.4's tag filter applies no symmetry requirement to *people*, while §11.5 applied one, so the same class of information carried two different gates.

### 11.6 Reaching a profile (v1.16)
The routes to a profile are enumerated here because §9.3's no-deep-links rule makes them the *only* routes, and because the commonest one was absent from every prior version.

- **The friends page.** A user's own friend list, listed alphabetically by display name — no other sort order, since any other ordering would be the platform inferring who matters (§1.3). It carries a **filter box over that list**. This is not the global search §17 forbids: global search is discovery of strangers across the network; filtering at most `FRIEND_CAP` = 300 names the user already has is navigation, and at 300 names it is necessary. **The box is labelled "Filter your friends" (v1.18)** — a visible label, never placeholder text (§16.3); any placeholder repeats the idea ("Start typing a name"). The label is a requirement, not a copy suggestion: a box labelled "Search" on this page tells the user the platform has a search, on a platform whose central promise is that it has none (§17), and nothing corrects that impression except trying it. The exact string may change; that it says *filter*, and says *your friends*, may not.
- **Names rendered anywhere else** — post authors, commenters, mutual-friend context, an author's private reaction list — under the single visibility-aware linking rule of §8.1.
- **The discover page** (§11.4), friend requests and introductions (§5.2, §5.5), and notification links (§12.2).
- **There is no in-app way to point one friend at another** besides an introduction (§5.5). That is the designed answer, not an omission; the honest residual about copied URLs is stated in §9.3.

---

## 12. Notifications

Notifications are the platform's only push mechanism, so §7.7's rule governs all of them: **the feed is a mailbox, not a machine.** The test applied to every type below is **bait invents a reason to come back; a reply is a reason that already exists.** Delivery is in-feed (§7.7), plus optional email.

### 12.1 What generates a notification (v1.15)

**Profile updates — per event type.** The undifferentiated "profile update" of earlier versions is replaced by a per-field policy. A friend's change notifies only where marked:

| Change | Notifies friends? | Why |
|---|---|---|
| New profile post (the blog) | **Yes** | The only genuinely new content; the pull model of §7.1 depends on some nudge existing |
| Profile photo **uploaded** | **Yes, coalesced** | Recognition-relevant and socially meaningful; coalesced because v1.16 removed the edit cooldown that used to space these out (§13.6) |
| Profile photo **chosen from `DEFAULT_AVATAR_SET`** | **No** | A platform-supplied image is not news, and swapping to one is the retraction direction, which is always quiet (§9.4) |
| New gallery image, or an image **replaced** | **Yes, coalesced** | Bounded at `GALLERY_MAX` = 8; a batch upload must never become eight notifications. A replacement is a picture friends have not seen |
| Gallery image **removed**, or gallery **reordered** | **No** | Nothing is new, and retraction is never announced |
| Alternative text edited on any image | **No** | The image is unchanged; a description fix must cost nothing (§9.4) |
| Short bio / extended about section | **No** | Self-announcing on the next visit; a typo fix must not cost 300 notifications |
| Profile hashtags | **No — deliberately silent** | They gate FoF visibility (§11.3); announcing a change would leak interest changes and push discovery into the feed, which §11.4 forbids |
| Theme or font | **No** | Presentation, not content (§9.1) |
| Display name | **No — already settled** | The "formerly" dual display *is* the announcement (§4.5.1) |
| Any edit to an existing post or comment | **No** | §7.8: re-notifying would make fixing a typo socially expensive |

The name-change precedent (§4.5.1) is the general principle behind the "no" rows: **where a change announces itself to the next person who looks, no notification is needed.**

**Social activity on your own content.** Comments and reactions on a post you authored, and comments on a post you follow (§12.3). Before v1.15 this document generated neither, so an author learned of a conversation on their own post only by revisiting it — an omission, not a decision.

**A widened audience, to the people it re-exposes (v1.16).** When an author edits a profile post's hashtags such that **more** viewers can now see it (§7.8), **everyone who has already commented on that post is notified**: *"David added a hashtag to a post you commented on. More people can see it now."* Commenting already turns following on (§12.3), so this uses a delivery path that exists, with access re-checked at delivery and no excerpt (§12.2). It is not an invented reason to return — it is notice that a decision the recipient already made has changed underneath them, which is the distinction §12's opening test draws. Narrowing an audience notifies nobody.

**Everything else.** Friend requests, introduction proposals, invite acceptance, contact-card requests and one-time access-request alerts (§10.5), inactivity warnings (email only, §4.8), and account/security events (new-device login, password change, email change — §4.6.1).

### 12.2 What a notification may contain

- **Never an excerpt of post or comment body text.** A notification carrying content turns a pull-model profile post into a push-model feed post with an audience of up to 300, erasing the distinction §7.1 is built on. A notification carries the actor's name (rendered live, §4.5.1), the event type in specific plain text, a relative age (§7.5.1), and a link. A post opened from a notification is always shown in full (§7.7).
- **Names, never numbers.** Multiple actors are listed by name — "Alice and Tom commented on your post" — overflowing to "and others", never "3 new comments". This is the idiom §8.2 already established for reactions, and it stops a private count becoming a score comparable across one's own posts. **There are no unread-count badges anywhere on the platform.**
- **Rendered live from current state.** Reactions are changeable and removable (§8.2) and comments are deletable (§8.1), so a notification renders from what exists at read time, not what existed at event time — the same rule as names in §4.5.1. Removed reactions and deleted comments simply drop out.
- **Wording is specific per event type,** in real text, never an icon carrying the meaning (§16.4): "David posted to his blog", "David changed his profile photo", "David added 3 photos to his gallery", "Alice and Tom commented on your post".
- No notification ever includes content beyond what the recipient may see. **No engagement-bait notifications** ("you have memories!") exist.

### 12.3 Coalescing and following

- **Profile updates coalesce on a clock.** At most one notification per author, per recipient, per event type, per `PROFILE_NOTIFY_WINDOW_HOURS` = **6** — replaced in place rather than stacked, carrying the age of the most recent event in the group. Multiple blog posts inside one window coalesce to "David posted twice to his blog", linking to the blog rather than to either post (the daily post limit of §13.6 makes a burst possible).
- **Social activity coalesces on unread state, not on a clock.** One notification per post per recipient, updating in place until it is read. Conversation is bursty: a fixed window would either flood the feed or arrive too late to join in.
- **Following a post.** Anyone who can currently see a post may follow it and be notified of further comments. Commenting turns following on; a visible per-post toggle turns it off, and a global default lives in settings. Recorded deliberately: commenting is treated as a **stated** interest rather than a behavioral inference, which is the line §1.3 draws — it is close to that line and is a decision, not an oversight.
  - **Following is private.** The author never sees who follows a post, and no follower count exists anywhere (§17).
  - **Access is re-checked at delivery, never assumed.** Unfriending (§5.3), blocking (§5.4), and a lapsed hashtag gate (§11.3, evaluated live) each silently end delivery, and must never reveal to anyone that a follow existed.
- **Email carries no timestamp at all.** A relative age is computed when mail is sent and read whenever the recipient opens it — three days later it would be false. The mail client's own received-time is more accurate than anything the body could assert (§7.5.1).

### 12.4 The honest risk, stated
Notifying on comments means the busiest threads generate the most notifications, and that is the first link of an engagement loop. What keeps the loop from closing here is structural, and is worth writing down so the reasoning survives: nothing is counted, nothing is ranked, audiences are capped at 30 and 300, following is invisible to the author, reactions remain author-private (§8.2), and every thread evaporates at 90 days (§7.5). If any of those ever weaken, this section is the first place to re-examine.

---

## 13. Safety and Moderation

### 13.1 Layers
1. **Structural** (does most of the work): invite-only vouched entry, no reach, bounded audiences, no strangers, **no free-text messaging channel** — friend requests, introductions and reactions carry no composed text (§5.2, §5.5, §8.2) and there is no DM system at all (§10.1) — and the URL allowlist (§7.2.3).
   **One honest qualification (v1.15, amended v1.16):** this layer is often summarized as "no free-text vectors," and that overstates it. A friend request displays the requester's **own short bio and profile photo** (§5.2, §9.2), both author-chosen, to someone who did not ask for them. That surface is governed not by the absence of text but by four things: screening at every save; **rejection of disallowed URLs in the short bio, not merely de-linking them** (§9.4, corrected in v1.16 — an unclickable address is still readable and retypeable); a **hold on sending further requests** after either is changed (§13.6); and a **report action on the request card itself** (§5.2), without which the only backstop for an unscreened photo was unreachable by the person it was shown to. The distinction matters because §4.6.1's anti-phishing argument leans on this layer, and an overstated claim is a weak foundation.
2. **User-level:** silent unfriend (§5.3), silent full block (§5.4), author-deletes-comments (§8.1).
3. **Operator-level:** the report system below.

### 13.2 Reporting (v1 = stub)
Every post, comment, and profile has a "report" action → lands in a private operator moderation queue with reporter, target, and a frozen copy. v1 workflow is simply: the operator reviews and acts manually (delete content, warn, or ban an account). Formal policies/appeals are deferred.

**Every report carries a reason (v1.21).** Through v1.20 a post or comment report carried only reporter, target and frozen copy, while a *profile* report — specified in v1.16, long after the stub above — carried a target category and a short note. That asymmetry was an accident of drafting order, not a decision, and it left the operator opening a queue item with no idea what they were being asked to look at. **There is one report form, and it always carries a reason category**, plus the optional short note to the operator this section already gives profile reports. For a post or a comment the reasons are: *harassment or abuse · unwanted or commercial content · someone else's private information · **the tags don't match this post** (profile posts only) · something else*. For a profile they are the target categories already listed below.

This is not new machinery: the reason is a value in a field the record already has, and the form already exists. Three notes on the tag reason specifically, which is the one this version was written for (§7.9, §11.3):

- **It is not a moderation action in waiting.** The right response to a mis-tagged post is usually a corrected tag or a word with the author, not a deletion or a ban. Recording it as a *reason* rather than routing it to a separate channel is what lets the operator see that distinction at a glance and act proportionately.
- **The frozen copy is what makes it judgeable at all.** Tags are editable after posting (§7.8) — uniquely among a post's fields, editing them changes who can see it — so a report that captured no copy could be defeated by editing the tags before the operator looks. §13.3's freeze already covers this; it is worth saying why it matters here.
- **A §13.5 form category was considered and rejected (2026-08-17)** as the venue for this. It would have needed no build at all, which was its appeal. But it requires the reporter to leave the post, find the form, and describe from memory which post they mean; it captures no frozen copy, so the evidence stays editable; and it would put one complaint into the operator's queue in two different shapes depending on how the user got there. The report action is already on every post, and giving it a reason is smaller than it looks.

**Reporting a profile (v1.16).** A profile has no single frozen "content," so this section previously assumed something that does not exist. What a profile report captures:
- **A frozen render of the profile as it appeared to the reporter** at report time — display name, short bio, extended bio if the reporter is a friend and could see it, the profile photo file, the gallery image files, and hashtags. **Not the blog:** individual posts are separately reportable, and a profile report concerns the identity surface.
- **A target category**, because the operator needs to know which of several things is wrong: *the photo · the name · the short bio · the about section · the gallery · this person's behaviour*.
- **A short free-text note to the operator.** This is not an exception to §13.1's no-free-text principle, which governs **user-to-user** surfaces; a report reaches the operator alone, exactly as §13.5's form does. The operator will frequently need it ("this is a photograph of my daughter, posted without consent").

**Where the action lives.** In the profile's persistent header, so it is reachable from every tab (§9.1), and **on the friend-request card** (§5.2). The second placement is load-bearing rather than decorative: the profile photo is the one author-controlled thing that cannot be screened (§13.6), the request card pushes it to people who never asked for it, and until v1.16 the recipient of that push had no report action anywhere. The action is a real `<button>` with visible text, never an unlabelled icon (§16.4). Available to any viewer who can see the profile at all; not to its owner.

**Content-similarity detection — considered and declined (2026-08-01).** Automatically flagging when an author's posts are textually similar (e.g., the same message split across several feed posts to different ≤30-person batches, worked around one post at a time — §13.6) is technically straightforward: shingling/SimHash-style near-duplicate hashing is cheap, fully first-party, and needs no ML model for the literal-and-near-literal cases that actually matter here. It is nonetheless declined for v1, for cost/benefit reasons rather than feasibility: **`POST_MIN_INTERVAL_MINUTES`** (§13.6, v1.13) already makes batch-and-repost cost real elapsed time; an automated similarity flag needs a tuned threshold and will misfire on legitimate repeated content (a templated thank-you note sent to two small groups, a deliberate follow-up post); and at this network's scale, a human operator reading two reported posts side by side is cheaper and more accurate than building and maintaining a detector. This is recorded as a **mechanical text-pattern check**, not the behavioral/relationship inference §1.3 rules out — declining it is a solo-operator cost/benefit call (§2), not a principled objection. If ever revisited, the manual report queue above — not an automated block — remains the intended venue.

### 13.3 Reported-content lifecycle
- Reported content **stays live** while the report is open (mass-report censorship is not a weapon here).
- The **frozen copy** exists only in the moderation queue, never visible to users, and survives expiry/author-deletion solely so the report can be judged.
- Purge rules: report dismissed → frozen copy purged immediately. Report upheld → live content removed; frozen copy purged 30 days later (appeal window). **Hard cap: any frozen copy is purged at 90 days** even if unreviewed.

### 13.4 What persists
Only content-free counters: "account X: N upheld reports," linked to the invite tree for forensics. Never the content itself.

### 13.5 Operator request channels
Beyond abuse reports, users need structured ways to ask the operator for things. v1 implements this as **one simple submission form with a category dropdown**, feeding the same operator queue as reports (separately categorized):
- **Hashtag suggestion** — propose a new tag for `HASHTAG_VOCAB` (§11.2). The commonest outcome is not a new tag but a **search alias** added to an existing one, which fixes the miss permanently for everyone (§11.2.1).
- **External service request** — propose a domain for the URL allowlist (§7.2). Judged against the three admitting categories **and** the anti-phishing bar of §7.2.3, including the open-redirector check. A domain that serves none of convening, hosting-what-WeeBee-cannot-host, or messenger handoff is declined — with the contact card named as the alternative, per the rejection wording of §7.2.3.
- **Bug report.**
- **Accessibility problem** — anything on the platform that is hard or impossible to use with a screen reader, keyboard, magnification, or any assistive technology (§16.5). Triaged ahead of feature requests.
- **General feedback / feature request.**
Submissions are private (submitter → operator only), rate-limited, and carry no notification machinery. The operator's decisions need no public justification.

**What the submitter is told (v1.21).** Because no reply is ever sent, the confirmation on submission has to do the whole job, and it does it by describing the rhythm rather than promising a time: **submissions are read in batches, no reply is sent, and an accepted change simply appears where it belongs** — a new tag in the picker, a domain in the allowlist. **No interval is stated to users**, here or anywhere: a cadence belongs in the operator's runbook (BUILD_PLAN §17.3), where missing it costs an unread queue, not in a message, where missing it breaks a promise. There is no status page, no "pending" state and no per-submission outcome; adding any of them would be the notification machinery this section exists to refuse, and would bind a solo operator's time to a queue whose length they do not control.

### 13.6 Rate limits
All social actions are rate-limited per account per day (posts, comments, reactions, friend requests, introductions, card requests, invites — see §14 for suggested values). Limits are generous for humans and hostile to scripts; hitting one produces an honest "slow down" message. **Login attempts additionally get per-account _and_ per-source-address exponential backoff with temporary lockout** (§4.6.1) — a stricter, security-specific case of the same framework.

**Minimum interval between feed posts (v1.13).** A daily count alone leaves one gap open: an author can split a single message into several near-identical feed posts, each addressed to a different ≤30-person batch of friends, fired off in quick succession, and reconstruct a full-friend-list push (up to `FRIEND_CAP` = 300) without any single post ever exceeding `POST_AUDIENCE_MAX`. This does not fail the No-Reach Test — every recipient is still the author's own friend, nobody outside the graph ever sees it — but it defeats the friction §1.3's "pull over push" principle intends for anything wider than a hand-picked audience, and floods recipients' feeds with fragments of the same message. **Feed posts by the same author must be spaced at least `POST_MIN_INTERVAL_MINUTES` apart**; hitting it produces the same honest "slow down, you can post again in N minutes" message as other rate limits. This is a minimum spacing per author, not a per-recipient or per-content check — the platform does not compare post text for similarity, which was **separately considered and declined on cost/benefit grounds** (§13.2, v1.14), not because it would constitute the behavioral inference §1.3 rules out. (Earlier wording here asserted the latter and contradicted §13.2; corrected in v1.15.) **Profile posts are exempt**: they are pull-only, already visible to all current friends regardless of when they were posted, and carry no reach-multiplication risk (§7.3).

**The friend-request send hold (v1.16, replacing the v1.15 change cooldown).** The short bio and the profile photo are the only author-controlled content the platform *pushes* toward people who are not the author's friends: both appear in the friend-request card shown to up to 20 FoFs a day (§5.2, §9.2), whether or not the recipient accepts. Without a limit the pattern is obvious — put something into the bio or the photo, send a batch of requests, change it, send another batch — and the field becomes a rotating billboard aimed at people who never opted in.

v1.15 answered this with a cooldown on **changing** the fields (`BIO_CHANGE_COOLDOWN_HOURS` = 12, with a 15-minute grace). That aimed at the wrong half of the pattern. It fell hardest on the most ordinary behaviour there is — a new user trying two or three photos on their first evening — while the attacker, who is patient by construction, simply waited. **The hold is therefore moved from the edit to the push:**

- **Changing the profile photo or the short bio is free and unlimited.**
- **Sending a friend request is blocked for `REQUEST_HOLD_AFTER_PROFILE_CHANGE_HOURS` = 12 after either changes**, with the usual honest message stating the reason and the remaining time.
- The attacker's edit-and-blast cycle meets exactly the delay it met before. The ordinary user — who fiddles with a photo in week one and sends a request once a month — never encounters the limit at all.
- **The card is snapshotted at send time** (§5.2). Without that, the hold is defeated in either form by sending clean requests and changing the photo afterwards, retroactively altering every card still unanswered.

Four carve-outs, each deliberate: **selecting an image from `DEFAULT_AVATAR_SET` triggers no hold** (a platform-supplied image cannot carry abuse, and swapping to one is retraction); **clearing the short bio to empty triggers no hold** (the §10.3 principle that the recoverable direction is the free one); a save **rejected by screening starts no hold**, since a save that never happened cannot start a clock; and the **extended bio is exempt entirely**, being friends-only with no push surface (§9.4). Editing an image's alternative text is not a change to the image and triggers nothing.

Note what this control is and is not: it needs no judgment about content, which is why it is the only measure that can cover the **profile photo** at all — screening cannot read an image, and image moderation is out of scope for a solo operator (§2). The remaining backstop for an abusive image is the report action, which §13.2 now places on the request card itself.

**`BIO_CHANGE_COOLDOWN_HOURS` and `BIO_EDIT_GRACE_MINUTES` are retired** (§14). This is not a cap being lowered against the raise-only rule of §1.3 — it is a mechanism replaced by a different one at the same strength.

---

## 14. Configuration Constants

All caps are named constants; **raise-only** (§1.3). Suggested v1 values; those marked ✎ are operator-tunable judgment calls rather than agreed design decisions.

| Constant | Value | Ref |
|---|---|---|
| `FRIEND_CAP` | 300 | §5.1 |
| `POST_AUDIENCE_MAX` | 30 | §7.1 |
| `POST_LENGTH_MAX` | 10,000 characters | §7.2.1 |
| `COMMENT_LENGTH_MAX` | 2,000 characters (**confirmed by founder 2026-08-04**, having stood as an undiscussed assertion since v1.6) | §7.2.1, §8.1 |
| `BIO_SHORT_MAX` | 200 characters (basic tier, FoF-visible; no links) | §9.4 |
| `BIO_EXTENDED_MAX` | 2,000 characters (friends only; allowlisted links permitted) | §9.4 |
| `FEED_FOLD_CHARS` ✎ | 500 characters (display-only fold threshold — the feed, and the profile's Pinned tab) | §7.7, §7.6, §9.1 |
| `BLOG_FOLD_CHARS` ✎ | 2,000 characters (display-only fold threshold, profile Blog tab) | §7.7, §9.1 |
| `COMMENT_FOLD_CHARS` ✎ | 300 characters (display-only fold threshold for comments, on every surface) | §8.1, §7.7 |
| `POSTS_PER_PAGE_DEFAULT` ✎ | 20 (items per page, feed and profile Blog tab) | §7.7.1 |
| `POSTS_PER_PAGE_OPTIONS` ✎ | 20 / 40 / 60 (viewer-chosen, one setting, applies everywhere) | §7.7.1 |
| `IMAGE_MAX_PX` | 3,840 (long edge of stored images; larger uploads downscaled) | §7.2.2 |
| `IMAGE_UPLOAD_MAX_MB` ✎ | 20 | §7.2.2 |
| `ALT_TEXT_MAX` ✎ | 1,000 characters (image alternative text) | §16.3 |
| `GROUP_SIZE_MAX` | 30 | §6 |
| `PIN_LIMIT` | 10 | §7.6 |
| `GALLERY_MAX` | 8 (separate from the profile photo; no caption field — the alt text is the caption) | §9.4 |
| `DEFAULT_AVATAR_SET` ✎ | operator-curated platform avatars; original artwork, never photographs of people; one member designated as the account-creation default | §9.4 |
| `PROFILE_HASHTAG_MAX` | 10 | §11.2 |
| `CONTACT_ITEMS_MAX` | 12 | §10.2 |
| `NAME_CHANGE_COOLDOWN_DAYS` | 90 (must stay ≥ `NAME_TRANSITION_DAYS`) | §4.5.1 |
| `NAME_TRANSITION_DAYS` | 90 (dual "formerly" display) | §4.5.1 |
| `NAME_BLOCKLIST` ✎ | operator-curated blocked name strings | §4.5 |
| `HASHTAG_VOCAB` ✎ | operator-curated interest vocabulary; each entry also carries **operator-curated search aliases** — never displayed, never selectable, never tags (§11.2.1). No size target is stated here: it is content work, and the target lives in BUILD_PLAN Phase 10 | §11.2, §11.2.1 |
| `INVITE_BANK_MAX` / new-account start | 5 / 2 | §4.2 |
| `INVITE_REPLENISH_DAYS` | 30 days since last replenish (+1 invite, capped at `INVITE_BANK_MAX`) | §4.2 |
| `INVITE_EXPIRY_DAYS` ✎ | 14 | §4.1 |
| `CONTENT_TTL_DAYS` | 90 (reconfirmed by founder 2026-07-08; sticky in both directions once live — lowering deletes content early, raising outlives authors' expectations) | §7.5 |
| `EXPIRY_COUNTDOWN_DAYS` | 14 | §7.5 |
| `DELETE_GRACE_DAYS` | 30 | §4.7 |
| `BACKUP_RETENTION_DAYS` | 30 days (encrypted off-server backups; the window in which a copy of deleted content still exists — the promise of §7.5 and §4.7 rests on this number) | §7.5, §4.7, §15.1 |
| `INACTIVITY_DELETE_DAYS` | 730 days since last login (≈ 24 months) | §4.8 |
| `INACTIVITY_WARN_DAYS` | 180 / 365 / 670 / 700 days since last login (≈ 6, 12, 22, 23 months; the last two land 60 and 30 days before deletion) | §4.8 |
| Report freeze: appeal / hard cap | 30 / 90 days | §13.3 |
| Re-request cooldown after declined friend request ✎ | 90 days | §5.2 |
| `REACTION_SET` ✎ | ~6 operator-curated phrases | §8.2 |
| `THEME_SET` ✎ | operator-curated fonts + color schemes (each verified against the §16.3 contrast ratios) | §9.1, §16.3 |
| URL allowlist ✎ | operator-curated | §7.2 |
| Rate limits ✎ (per account/day) | e.g., 20 posts, 200 comments, 20 friend requests, 10 intros | §13.6 |
| `POST_MIN_INTERVAL_MINUTES` ✎ | 10 (suggested default; minimum spacing between an author's feed posts, founder's stated range 5–20; profile posts exempt) | §7.3, §13.6 |
| `PROFILE_NOTIFY_WINDOW_HOURS` ✎ | 6 (coalescing window per author, per recipient, per event type) | §12.3 |
| `REQUEST_HOLD_AFTER_PROFILE_CHANGE_HOURS` ✎ | 12 (friend requests held after a short-bio or profile-photo change; picker selections, clearing to empty, screening rejections and the extended bio all exempt) | §5.2, §9.4, §13.6 |
| Pending friend-request expiry | 90 days (matches `CONTENT_TTL_DAYS`; destroys the frozen card with it) | §5.2 |
| ~~`BIO_CHANGE_COOLDOWN_HOURS`~~ | **retired v1.16** — mechanism replaced by `REQUEST_HOLD_AFTER_PROFILE_CHANGE_HOURS`, not weakened | §13.6 |
| ~~`BIO_EDIT_GRACE_MINUTES`~~ | **retired v1.16** — nothing left to grace once edits are free | §13.6 |
| `RESET_CODE_TTL_MINUTES` ✎ | 15 (lifetime of a reset / email-change / verification code) | §4.6.1 |
| `RESET_CODE_LENGTH` ✎ | 6 (digits) | §4.6.1 |
| `LOGIN_ATTEMPT_LIMIT` ✎ | e.g., 5 failures before backoff begins (per account and per source address) | §4.6.1, §13.6 |
| `LOGIN_LOCKOUT_MINUTES` ✎ | e.g., 15 (base lockout, escalating with exponential backoff) | §4.6.1, §13.6 |

---

## 15. Privacy, Legal, Money

### 15.1 Legal posture
- 18+ only (§4.4). No geo-restrictions; GDPR-compatible by design (minimal collection, guaranteed erasure and expiry, export, no profiling). **The privacy policy states the backup window plainly (v1.18):** deleted content leaves the live system at once and the last encrypted backup within `BACKUP_RETENTION_DAYS` = 30 days (§7.5, §4.7, ARCHITECTURE §10). This is the standard, GDPR-accepted resolution of the backup-versus-erasure tension; the alternative — claiming instantaneous and total erasure while nightly backups exist — would simply be untrue. Privacy policy and Terms of Service are build-plan deliverables, written plainly. A real attorney reviews before any public phase.
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
- **The profile page, concretely (v1.16).** `<h1>` is the owner's display name, once, in the persistent header — rendered through the shared helper, so §4.5.1's "NewName (formerly OldName)" is real text inside it. The tab strip is a `<nav>` with an accessible name, its links carrying `aria-current="page"`; each tab is a separate URL with its own page title ("David Dudek — Posts"). `<h2>` names the tab's content. **Individual posts carry no heading** — a post has no title, and inventing one from its opening words would truncate content and fight the fold. Each is an `<article>` inside an `<ol>`, labelled *"Post by David, a few days ago"*, which is the structure screen-reader users navigate a list of posts with. The gallery is a `<ul>` whose items are real `<button>`s in plain tab order; at `GALLERY_MAX` = 8 a roving-tabindex grid adds script and failure modes for nothing.

**Keyboard**
- Every function is operable by keyboard alone, with no traps (2.1.1, 2.1.2) — including the audience picker, hashtag picker, contact-card toggles, image overlay, gallery reordering (§9.4: "move up"/"move down" controls, never drag-only), and "read more" folds.
- **Repeated controls carry distinct accessible names (v1.16).** A list of posts produces many identical "read more" controls, and a screen reader's element list of twenty entries reading "Read more" is a dead end. Each is a real `<button>` (it navigates nowhere) with `aria-expanded`, a unique name — *"Read more of David's post from a few days ago"* — via visually hidden text, and focus that stays on the control as it becomes "Show less". The same rule governs the gallery's per-image controls, which take their names from the image's own alternative text (§9.4).
- A **visible focus indicator** on every focusable element, meeting contrast against its background (2.4.7). It is never removed by a theme.
- Focus order follows reading order (2.4.3). Any control that appears on hover is also reachable on focus (1.4.13).

**Contrast, color, and theming (§9.1)**
- Body text ≥ **4.5:1**, large text ≥ **3:1** (1.4.3); UI components, focus rings, and meaningful graphics ≥ **3:1** (1.4.11).
- **Every theme in `THEME_SET` must pass these ratios in every combination in which it can appear** — including a visitor's profile theme and the "always use my own theme" viewer override. This is the operational reason theming is operator-curated and not freeform: contrast can be *guaranteed* for a curated set. A candidate theme that fails is not added.
- **Color is never the only carrier of meaning** (1.4.1): expiry countdowns, pinned markers, error states, and toggle states all carry text or shape, not just hue.
- The viewer override of §9.1 is itself an accessibility feature (a user with low vision keeps their chosen high-contrast scheme everywhere) and must never be overridable by a page author. **It is applied server-side at render**, not as a client-side toggle a page could defeat — an implementation constraint, not only a policy.
- A theme may change **type and colour only, never layout** (§9.1), so the reflow and 200 %-zoom guarantees below hold without re-verification per theme.

**Text and layout**
- Text resizes to **200%** without loss of content or function (1.4.4), and the layout **reflows at 320 px** with no two-dimensional scrolling (1.4.10).
- User-applied text spacing overrides do not break layout (1.4.12).
- **Preformatted posts are the one documented exception** (§7.2.1): they legitimately require two-dimensional layout, which 1.4.10 explicitly exempts, and they intentionally scroll horizontally. The obligations that come with the exemption: the scrollable region must be **keyboard-scrollable and focusable** with an accessible name (a scrollable box that only a mouse can pan is a 2.1.1 failure); the composer's preformatted explainer must state plainly that the mode trades reflow for exact spacing; and **the horizontal scroll is confined to the post's own container and must never cause the page itself to scroll sideways** (v1.16). The exemption covers the post, not the page. This matters most on the Pinned tab (§9.1), where a preformatted post can sit for years.

**Images (§7.2, §7.2.2, §9.4)**
- Every uploaded image — post image, gallery image, profile photo — carries an **alternative text description** (1.1.1), authored by the uploader, up to `ALT_TEXT_MAX` = 1,000 characters.
- The composer **prompts for it and requires a deliberate choice**: write a description, or tick "this image is decorative" (which stores an explicitly empty alt). It is never silently skipped and never auto-filled — the platform does not infer (§1.3), and machine-generated descriptions are not a v1 feature.
- The click-to-expand overlay (§7.2.2) is a **modal dialog**: focus moves into it on open, is trapped while open, Escape closes it, and focus returns to the image that opened it. Zoom/pan is operable by keyboard. From the gallery it also carries **next/previous image controls** as real buttons, so a keyboard user need not close and reopen it eight times, and it **displays the alternative text as a visible caption** in a `<figure>`/`<figcaption>` with an empty `alt` on the image, so nothing is announced twice (§9.4).
- **One exception to uploader-authored alt text:** the platform-supplied avatars of `DEFAULT_AVATAR_SET` carry alternative text written by the operator (§9.4). It is recorded rather than left implied.

**Forms, errors, and status**
- Every input has a programmatically associated visible label (1.3.1, 3.3.2). Placeholders are never labels.
- Errors are identified in **text**, associated with the offending field, and describe the fix (3.3.1, 3.3.3) — which the spec's existing "honest error message" rule (§5.1, §7.2.1, §7.3, §13.6) already demands in prose. Character-cap overruns, breached passwords (§4.6.1), blocked names (§4.5), disallowed URLs (§7.2), and audience-size overruns all follow this rule.
- **Status messages are announced without moving focus** (4.1.3): the audience picker's live count, "post published", "code sent", rate-limit "slow down" notices, and lockout messages use polite live regions.

**Time limits and motion**
- The security-essential time limits — code TTL (`RESET_CODE_TTL_MINUTES`) and login lockout (`LOGIN_LOCKOUT_MINUTES`) — fall under 2.2.1's essential-exception, but the user is **told the limit in text** and can always request a new code. No other timed interaction exists.
- **Session expiry never destroys work in progress**: composer content survives a re-authentication.
- The expiry countdown (§7.5) renders as **static text computed per page load** ("deletes in 6 days"), never as a live-ticking timer — no moving, auto-updating, or auto-refreshing content (2.2.2). The feed updates only when the reader reloads it; nothing is ever inserted above what someone is reading.
- **Relative timestamps (§7.5.1) are computed per page load on the same rule**, and the exact underlying time is deliberately absent from the interface *and* the markup — no `title` tooltip, no `datetime` attribute. A hover-only affordance would fail 1.4.13 and §16.4 outright: touchscreens have no hover state, keyboard focus does not trigger `title`, and screen readers announce it inconsistently. The relative phrase is **real text and is the whole of what is conveyed**; anyone needing exact times gets them from their data export (§4.9).
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

No reshare/repost/quote of any kind · no public content or logged-out visibility · no likes or visible counts (followers, reactions, views, post counts, page numbers — none exist) · no algorithmic feed · no DMs · **no global search of people or content** — filtering one's *own* friend list is navigation, not search, and is provided (§11.6); searching the interest vocabulary (§11.2.1) is search over a static operator-written list that names no person and no post, and is likewise not this · no global hashtag browsing (the only tag view is the viewer-scoped discover filter, §11.4) · **no infinite scroll and no "load more"; long lists page with prev/next links (§7.7.1)** · **no date-based archive navigation** (absolute dates appear nowhere in the interface, §7.5.1) · **no gallery captions** — the alternative text is the caption (§9.4) · **no expiry of profile photo, gallery, bios, hashtags, contact card, groups or friend list**: statements expire, descriptions do not (§9.7) · no events system (delegated to allowlisted external services) · no video/audio · no native app (v1) · no API for third parties (v1) · no AT Protocol / blockchain · no minors · no businesses · no CAPTCHA or third-party human-challenge (§4.6.1, §16.4) · no automated content-similarity or duplicate-post detection (§13.2) · **no structured profile fields** — no relationship status, location, birthday, employer or equivalent (§9.6) · no unread-count badges and no follower counts (§12.2, §12.3) · no absolute timestamps in the interface (§7.5.1) · no end-to-end encryption or per-post content signing in v1 (§15.5; encryption-at-rest is used instead) · **no accessibility overlay widgets and no separate "accessible version" of the site (§16.4)** · no WCAG Level AAA conformance claim (individual AAA criteria are adopted where free — §16.1) · no machine-generated image descriptions (§16.3) · defending against off-platform screenshots is out of scope · **defending against manual re-propagation is out of scope** — a human retyping content, pasting an allowed link, or running a "copy this into your feed" chain letter is not designed against, because it is indistinguishable from a friend telling a friend; the no-reach guarantee covers mechanical propagation, and §1.2 states plainly why the manual path stays self-limiting.

**Parked ideas (explicitly not in v1):** request-more-access flags if trimmed to v1.1 (§10.5) · social account recovery · introduction-visibility opt-in toggle (§5.5) · per-post "friends-only comments" switch (**reasons for keeping it parked are recorded in §7.9**, along with the stronger alternative considered — hiding comments from hashtag-matched FoFs entirely) · nested comments · auto-suggesting frequent post hashtags for the profile · invite-tree accountability mechanisms · billboard ads · click-to-load media embeds (§7.2).

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
