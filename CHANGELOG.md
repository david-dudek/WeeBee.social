# Changelog — WeeBee

WeeBee has **one version number for the whole project**, not a version number per
document. It is currently **1.17**, inherited from SPEC.md because SPEC is the spine.
A version bump covers whatever changed in that round: if a change touches SPEC.md and
README.md only, the project still goes to the next number, and the other documents are
"at" that version too — identical in content to their previous selves, and said so here
explicitly. Every entry below names the status of **every** file, including the
untouched ones: "unchanged" is a real status, and stating it is what makes an unsynced
document visible instead of invisible. The version number lives in each document's
header (`**Project version:**`) and must match the newest entry in this file.

Entries before 1.17 were reconstructed from the version-history blocks that used to sit
in the four document headers; the prose is moved verbatim. Where the source text did not
record something — a date, a file's status in a given round — this file says
"not recorded" rather than guessing. See the mapping appendix at the bottom for the
translation between the old per-file version numbers and these project versions.

---

## 1.17 — 2026-08-03

| File | Status |
|---|---|
| README.md | changed — version header added; feedback section now names CHANGELOG.md |
| SPEC.md | changed — history moved to this file |
| ARCHITECTURE.md | changed — history moved to this file |
| BUILD_PLAN.md | changed — history moved to this file |
| CHANGELOG.md | new |

Structural only. No project content changed in this version: no requirement, constant,
decision or build step was added, removed or reworded. Version history was moved out of
the four document headers into this file, and the project moved to a single
whole-project version number.

**Note carried forward:** ARCHITECTURE.md and BUILD_PLAN.md were last synced to SPEC
v1.15 and remain unsynced to the v1.16 spec changes. See `TODO.md` prompt 09.

---

## 1.16 — 2026-08-03

| File | Status |
|---|---|
| README.md | not recorded — README carried no version number before 1.17 |
| SPEC.md | changed (file v1.16) |
| ARCHITECTURE.md | **unchanged since 1.15 (file v1.7) — not yet synced** |
| BUILD_PLAN.md | **unchanged since 1.15 (file v1.6) — not yet synced** |

### SPEC.md

1.16, founder-initiated: **the profile page is restructured as a persistent header plus four tabs, and the permanence question is settled.** (a) *Structure* — §9.1 replaces the single stacked page (identity header → pinned posts → about → gallery → blog) with a persistent header carrying only the profile photo, display name and report action, above four tabbed views reached as **separate URLs, not a scripted widget**: **Blog** (every post the viewer may see, newest first), **Pinned**, **Photos**, and **About** (both bios, hashtags, mutual friends). A tab is rendered only where the viewer has content, and no tab strip is drawn when only one qualifies. The header plus the About tab minus the extended bio becomes a **stated invariant**: it is exactly §9.2's basic tier and exactly §5.2's friend-request card, built from one component, because three surfaces that drift apart would silently falsify the screening arguments of §5.2 and §13.1. (b) *Feed posts appear on their author's profile* — no audience widens (§7.4's snapshot-plus-current-friendship rule is untouched and a FoF never sees a feed post at all); what changes is that a feed post is retrievable by pull for its 90 days instead of only by scrolling a feed. (c) **Permanence is settled and named** — new §9.7: *statements expire; descriptions do not.* The 90-day rule governs posts and comments; the profile photo, gallery, both bios, hashtags, contact card, groups and friend list are **account state** and persist until changed, erased (§4.7), or dormant (§4.8). Expiring the gallery was considered and rejected — it would force re-uploading the same photographs four times a year and leave the least frequent visitor with the emptiest profile. Public copy stops claiming that everything is deleted at 90 days. (d) *Pinned posts* — §7.5's absolute "every post and every comment" wording is corrected to name the §7.6 exemption a builder would otherwise not implement; a pinned post **displays its age** (the long tail of §7.5.1's ladder exists for it and nothing else) and **stays open for new comments**, which expire on their own 90-day clock; its expired comments leave **no trace at all**, on the principle that **an author may preserve their own words indefinitely and never anyone else's**, and because a "this once had comments" marker is a count in disguise (§17). (e) **Stated visibility** — new §7.9 puts a plain-text audience line on **every post**, shown to everyone who can see it and repeated at the comment box, because §8.1's "consciously accepted consequence" had been accepted by this document and never disclosed to the commenter who bears it. **Never a number:** a live match count would be a visible count (§17) and, worse, a privacy oracle enumerable one tag at a time. §17's parked per-post friends-only-comments switch **stays parked**, with reasons now recorded. (f) *Tag edits change an audience after the fact* — §7.8 invariant 1's deliberate exception also re-exposes **comments already written**, so the editor warns the author and **every existing commenter is notified** through the follow channel they already have (§12.3). (g) *Navigation* — long lists get **prev/next page links**, never page numbers (a post count in disguise), never a date archive (§7.5.1 forbids absolute dates in the interface), and never infinite scroll or "load more"; `POSTS_PER_PAGE_DEFAULT` = 20 with a viewer-chosen 20/40/60, applying to the blog and the feed alike. New §11.6 adds the **friends page** — the commonest route to a profile, absent from every prior version — with a filter over one's own list, which is not the global search §17 forbids. (h) *The profile photo becomes a picker* — an operator-curated `DEFAULT_AVATAR_SET` of original, non-human artwork, one member assigned at account creation; picker selections notify nobody, uploads notify friends coalesced. **The change cooldown moves off the edit and onto the push:** `BIO_CHANGE_COOLDOWN_HOURS` and `BIO_EDIT_GRACE_MINUTES` are retired in favour of `REQUEST_HOLD_AFTER_PROFILE_CHANGE_HOURS` = 12, which blocks **sending friend requests** after a photo or short-bio change. The attacker's edit-and-blast cycle meets the identical delay; the ordinary user — who tries three photos in week one and sends a request once a month — never meets the limit at all. Swapping *to* a picker image, and editing alternative text, trigger nothing. The friend-request card **snapshots** the photo and short bio at send time, without which any cooldown, old or new, is defeated by changing the photo after the requests are out; and **pending requests now expire at 90 days**, since each one holds a frozen image. (i) *A friend-list disclosure is removed* — §11.5's "hashtag-matched non-mutual friends" clause was the only place the platform revealed a friendship the viewer is not part of, gated on a criterion unrelated to it, and enumerable by rotating one's own profile hashtags, which nothing rate-limits and §12.1 deliberately keeps silent. Deleted; profiles show mutual friends only. This also resolves the §11.4/§11.5 inconsistency under which the same class of information carried two different gates. (j) *Smaller corrections*: §9.4's claim that "a field with no links is a field that cannot deliver one" was overstated — the short bio now **rejects** disallowed URLs at save rather than merely de-linking them; both bios acquire the whitespace rules they never had (§7.2.1's normal-post rules for the extended bio, all line breaks collapsed in the short bio, and no preformatted toggle for either); the gallery gets author-arranged order with keyboard-operable controls and **no caption field — the alternative text is the caption**, shown in the expand overlay; §13.2 states what a **profile** report captures, given that a profile has no frozen content, and the **friend-request card gains a report action**, the one surface where an unscreened photo lands on someone who never asked for it having previously had none; §4.7 states that deactivation hides an account's content everywhere, reversibly; §5.3 requires the unfriend confirmation to say plainly that unfriending is not invisibility; §8.1's name-linking rule extends to post authors, mutual-friend names and reaction lists; **reactions never render in a list view** (§8.2), a column of one's own posts with names under some and nothing under others being precisely the scoreboard that section exists to refuse; and §16.3 gains three specifics — distinct accessible names for repeated "read more" controls, containment of a preformatted post's horizontal scroll inside the post, and server-side application of the viewer's theme override.

---

## 1.15 — 2026-08-02

| File | Status |
|---|---|
| README.md | not recorded — README carried no version number before 1.17 |
| SPEC.md | changed (file v1.15) |
| ARCHITECTURE.md | changed (file v1.7) |
| BUILD_PLAN.md | changed (file v1.6) |

### SPEC.md

1.15, founder-initiated: **the notification model, content editing, and the profile's bio fields are specified together.** (a) *Profile-update notifications become per-event and coalesced* — §9.3's undifferentiated "changed bio / new gallery image" trigger and §7.1's single generic string ("David updated his profile") are replaced by the per-field table of §12.1: new blog posts and profile-photo changes notify friends, gallery additions notify coalesced, and bio, about-section, hashtag and theme changes are **silent and self-announcing on the next visit** (the §4.5.1 name-change precedent — the display *is* the announcement). New constant `PROFILE_NOTIFY_WINDOW_HOURS` = 6. Notifications carry **no excerpt of body text**, because a notification with content in it turns a pull-model profile post into a push-model feed post with an audience of up to 300 and erases the distinction §7.1 is built on. (b) *Comment and reaction notifications are added* — §12 previously generated none, so an author learned of a conversation on their own post only by revisiting it. Coalesced **by unread state rather than by clock**, rendered as **names, never numbers** (reusing §8.2's reaction idiom), and rendered live from current state so deleted comments and removed reactions drop out. **Commenters may follow a post**; following is private, has no count, and is re-checked at delivery so unfriending, blocking, or a lapsed hashtag gate silently ends it. (c) *Relative timestamps* — new §7.5.1 replaces the absolute posting date and time §7.5 formerly required with a fixed 40-step ladder that grows vaguer as content ages, on the stated principle that **WeeBee is deliberately vague about how old something is and exactly precise about when it will be destroyed**. The expiry countdown and account/security events (§4.6.1) keep absolute time; the exact timestamp appears **nowhere in the interface** — no tooltip, no `datetime` attribute — living only in the data export (§4.9) and the operator's database; emails carry no timestamp at all. (d) *Editing posts and comments* — new §7.8, previously unspecified anywhere in this document, which perversely pushed an author with a typo toward delete-and-repost, the more destructive path. Editable until expiry with a permanent "edited" marker, no version history, no notification, and five invariants — of which the security-critical one is that **an edit re-runs full content validation**, since an edit path that skipped the URL allowlist would let an author publish clean text and then edit a disallowed link into it, defeating the control §4.6.1 depends on. (e) *Two bio fields, both capped for the first time* — `BIO_SHORT_MAX` = 200 (basic tier, FoF-visible) and `BIO_EXTENDED_MAX` = 2,000 (friends only, matching `COMMENT_LENGTH_MAX`); the term "one-line bio" is retired, since 200 characters is not one line. The short bio never renders links; the friends-only extended bio may carry allowlisted ones. (f) **A free-text vector is closed and an incorrect claim corrected**: §5.2 promised friend requests "carry no free text" while showing up to 20 FoFs a day the requester's own attacker-controlled short bio and profile photo. Both are now screened at every save (as names are, §4.5) and rate-limited by `BIO_CHANGE_COOLDOWN_HOURS` = 12 with `BIO_EDIT_GRACE_MINUTES` = 15, with clearing-to-empty never rate-limited; §13.1's "no free-text vectors" wording is corrected to say what is actually true. (g) **Structured profile fields — considered and rejected** (new §9.6, §17): no relationship status, location, birthday or employer, on data-minimalism and engagement-bait grounds. (h) §13.6's parenthetical asserting that comparing post text for similarity would be §1.3 behavioral inference is corrected — v1.14 (§13.2) had already recorded it as a *mechanical* check declined on cost/benefit, and the two statements contradicted each other.

### ARCHITECTURE.md

1.7, synced to SPEC v1.13–v1.15: **three features that were previously unmodelled acquire architecture.** (a) *Editing* (SPEC §7.8) — `posts` and `comments` gain a nullable `edited_at`; §7 records the security-critical rule that **the URL validator and every other content check run on save, create and edit alike**, since a validator wired only into the create path would let an author publish clean text and edit a disallowed link into it, silently defeating the control §4.6.1 leans on. Ordering and expiry continue to read `created_at` and never `edited_at`. (b) *Notifications* (SPEC §12) — the one-line `notifications` entry is expanded into a real model with an event kind, a **coalescing key**, live-rendered actors, and read state; a new `post_follows` table carries per-post following, with the permission re-check pushed through the visibility engine at delivery rather than trusted from write time. A new `expire_notifications` cron job (§6) stops notifications outliving the content they point at. (c) *Relative timestamps* (SPEC §7.5.1) — a **single shared time-rendering helper**, added to §4's new "single-source rendering helpers" rule alongside the existing name helper, with the boundary-table test in §9 and the template prohibition on `title`/`datetime` attributes in §3.5 and §3.8. Also recorded: bio fields, screening and the change cooldown (§4, §7), `POST_MIN_INTERVAL_MINUTES` needing a last-post timestamp rather than a day counter (§4), and content-similarity detection declined so that no such table, job, or dependency exists (§14). Additive; no existing section changes meaning and no section is renumbered.

*ARCHITECTURE.md's status line described this version as "notifications/editing/timestamps sync".*

### BUILD_PLAN.md

1.6, synced to SPEC v1.13–v1.15 / ARCHITECTURE v1.7 (2026-08-02): **notifications, editing, relative timestamps and the bio fields folded into existing phases.** Step 2.3 gains the **shared time-rendering helper** alongside the name helper, built before any surface can print a date, with its boundary-table test; Step 6.2 gains `POST_MIN_INTERVAL_MINUTES` spacing; new Step **6.6** builds editing for posts and comments, with its verification written as the **attack case** — publish clean, edit in a disallowed link, confirm refusal — because a validator wired only into the create path is the failure this step exists to prevent; Step 6.5's "visible timestamps" becomes the relative ladder plus the absolute expiry countdown; Step 7.1 gains comment editing and the author-cannot-edit rule; Step 8.1 gains the two bio fields with screening, the no-links rule on the short bio, and the change cooldown; Phase 12 is rewritten from two steps to four (per-field profile triggers, the two coalescing modes, following a post, and the live-render/no-counts rules); Step 13.4 records that three §13.6 controls are timestamp-based rather than day counters; Step 16.1 confirms edit-path revalidation; Appendix gains rules 10 and 11. Folded into existing phases; one new step (6.6), no renumbering of existing steps.

---

## 1.14 — date not recorded

| File | Status |
|---|---|
| README.md | not recorded — README carried no version number before 1.17 |
| SPEC.md | changed (file v1.14) |
| ARCHITECTURE.md | unchanged since 1.12 (file v1.6) |
| BUILD_PLAN.md | unchanged since 1.12 (file v1.5) |

### SPEC.md

1.14, founder-initiated: **automated content-similarity detection across an author's posts — considered and declined** (§13.2, §17). Technically easy (near-duplicate hashing needs no ML for the literal/near-literal case), but declined on cost/benefit grounds: the v1.13 interval already adds real friction, an automated flag would misfire on legitimate repeated content, and at this network's scale a human moderator reading two reported posts is cheaper and more accurate than a tuned detector. Recorded as a mechanical-check cost/benefit call, not a §1.3 "never infers" conflict.

---

## 1.13 — date not recorded

| File | Status |
|---|---|
| README.md | not recorded — README carried no version number before 1.17 |
| SPEC.md | changed (file v1.13) |
| ARCHITECTURE.md | unchanged since 1.12 (file v1.6) |
| BUILD_PLAN.md | unchanged since 1.12 (file v1.5) |

### SPEC.md

1.13, founder-initiated: a **minimum interval between an author's feed posts** is added to close a gap the daily rate limit alone leaves open — an author splitting one message across several back-to-back feed posts, each to a different ≤30-person batch of friends, to reconstruct a full-friend-list push without ever exceeding `POST_AUDIENCE_MAX` on any single post. New constant `POST_MIN_INTERVAL_MINUTES` (suggested default 10, founder's stated range 5–20, ✎) applies to feed posts only — profile posts are exempt, being pull-only and already visible to all friends regardless of posting cadence (§7.3, §13.6, §14).

---

## 1.12 — 2026-07-26

| File | Status |
|---|---|
| README.md | not recorded — README carried no version number before 1.17 |
| SPEC.md | changed (file v1.12) |
| ARCHITECTURE.md | changed (file v1.6) |
| BUILD_PLAN.md | changed (file v1.5) |

### SPEC.md

1.12, founder-initiated: **the link policy is given a stated purpose** — new §7.2.3 recasts the URL allowlist from a pure anti-phishing control into a purpose filter with three admitting categories (convening services; hosts for the video/audio WeeBee cannot host; messenger handoff domains), adds a mandatory **open-redirector rule** (host matching alone is insufficient), records "original content" as an honest aspiration rather than an enforceable rule, and points the rejection message at the user's contact card (§7.2 shortened to cross-reference it; §13.5 triage criterion added). The **no-DM rationale** is recorded as *this is a solved problem and rebuilding it would make WeeBee a walled garden* (§10.1), with the decision explicitly **kept v1-scoped** — §17 and §15.5's E2EE-reconsideration clause deliberately unchanged. The mission's **real-world-meeting telos** (§1.1) and a **"not a walled garden"** supporting principle (§1.3) are stated. **Manual re-propagation is documented as an accepted residual** of the no-reach thesis — the guarantee covers mechanical propagation, not a human retyping something — with the reasons it stays self-limiting (§1.2, §17).

### ARCHITECTURE.md

1.6, synced to SPEC v1.12 (link policy): the URL allowlist stops being a plain domain table — `url_allowlist` (§4) gains category and redirector-pattern columns, and §7 gains an explicit **link validation** control recording the rule that **host matching alone is an insufficient and defective implementation**, because allowlistable services such as `youtube.com/redirect?q=` and `google.com/url?q=` run open redirectors that would bounce a reader from an allowed host to an arbitrary page; URL shorteners are permanently unallowlistable. Additive; no existing section changes meaning and no section is renumbered.

### BUILD_PLAN.md

1.5, synced to SPEC v1.12 / ARCHITECTURE v1.6 (2026-07-26): the **URL allowlist becomes a validator, not a domain list** — Step 6.2 now builds one shared link validator with the mandatory **open-redirector rejection** and the contact-card rejection message, and its verification adds the redirector and look-alike-host attack cases; Step 13.3's admin editor gains the category and redirector-pattern fields plus the add-inactive-by-default rule; Step 16.1's security pass confirms the validator. Folded into existing phases; no new phase, no renumbering.

---

## 1.11 — date not recorded (domain registered 2026-07-25)

| File | Status |
|---|---|
| README.md | renamed only — see below; no version number |
| SPEC.md | changed (file v1.11) |
| ARCHITECTURE.md | renamed only — no version bump recorded |
| BUILD_PLAN.md | renamed only — no version bump recorded |

### SPEC.md

1.11, founder-initiated: **the platform is named WeeBee**, on the registered domain `weebee.social` (Porkbun, 2026-07-25) — the "Working Title / The Network" placeholder is retired across all documents and the checkable-promise wording in §4.6.1 now names WeeBee directly; the founder has **settled**, not merely deferred, the decision to buy **no** defensive look-alike or typo domains and to invest no effort in "domain hygiene" (§4.6.1 amended from "reconsider before public phase" to a standing decision, with free certificate-transparency monitoring kept as the one lightweight recommendation).

*Status note: SPEC 1.11 states the placeholder was retired **across all documents**, and
README.md, ARCHITECTURE.md and BUILD_PLAN.md all carry the WeeBee name today. Neither
ARCHITECTURE.md nor BUILD_PLAN.md recorded a version bump for it, so their file versions
are unchanged from 1.10 (v1.5 and v1.4 respectively).*

---

## 1.10 — 2026-07-21

| File | Status |
|---|---|
| README.md | not recorded — README carried no version number before 1.17 |
| SPEC.md | changed (file v1.10) |
| ARCHITECTURE.md | changed (file v1.5) |
| BUILD_PLAN.md | changed (file v1.4) |

### SPEC.md

1.10, founder-initiated: **accessibility — new §16 makes WCAG 2.1 Level AA conformance a requirement of the same rank as the tracking ban**, with per-area requirements (semantics, keyboard, contrast, reflow, images and alt text, forms/errors/status messages, time limits, motion, targets), the preformatted-post reflow exemption documented honestly, accessibility overlays and separate "accessible versions" banned outright, and verification plus an accessibility statement and a report channel required; supporting principle added (§1.3); §7.2.1, §7.2.2, §9.1, §13.5 cross-referenced; constant `ALT_TEXT_MAX` = 1,000 added (§14); former §16 Non-Goals → §17 and former §17 Downstream Documents → §18, with all cross-references updated.

### ARCHITECTURE.md

1.5, synced to SPEC v1.10 (accessibility): new §3.8 records how WCAG 2.1 AA is built in — shared accessible template partials as the single source of each pattern, base-template landmarks/skip link/focus styling, an automated `THEME_SET` contrast test, per-island ARIA requirements with no-JavaScript fallbacks, keyboard-scrollable preformatted blocks, and the permanent ban on accessibility overlays; Decision 1 gains reason 6 (server rendering is the accessible default); `images` gains `alt_text` and `is_decorative` (§4); §9 gains the accessibility test set and the human-audit note; §14 gains overlay and separate-site rejection rows; additive, no existing section changes meaning and no section is renumbered.

### BUILD_PLAN.md

1.4, synced to SPEC v1.10 / ARCHITECTURE v1.5 (2026-07-21): **accessibility (WCAG 2.1 AA) folded into the existing phases rather than bolted on at the end** — Step 2.5 builds the base-template foundations and the shared accessible partials every later step composes, plus a keyboard/VoiceOver check in its verification; Step 6.1 adds image alt text and Step 6.2's verification the composer's deliberate-choice rule; Step 8.2 adds the automated `THEME_SET` contrast gate; Step 13.2 adds the "accessibility problem" request category; new Step 15.2 is the accessibility statement; new Step 16.5 is the five-pass pre-launch audit; Appendix gains rule 9.

---

## 1.9 — date not recorded

| File | Status |
|---|---|
| README.md | not recorded — README carried no version number before 1.17 |
| SPEC.md | changed (file v1.9) |
| ARCHITECTURE.md | unchanged since 1.8 (file v1.4) |
| BUILD_PLAN.md | unchanged since 1.8 (file v1.3) |

### SPEC.md

1.9, founder-initiated: new §15.5 records the end-to-end-encryption and content-signing question — full E2EE and per-post signing considered and deferred for v1 (web-app delivery trust, password-reset incompatibility, and the break of server-side moderation/EXIF-stripping/allowlist enforcement), encryption-at-rest adopted instead, and the honest trust model stated; §16 Non-Goals and §13.1 cross-referenced.

---

## 1.8 — 2026-07-21

| File | Status |
|---|---|
| README.md | not recorded — README carried no version number before 1.17 |
| SPEC.md | changed (file v1.8) |
| ARCHITECTURE.md | changed (file v1.4) |
| BUILD_PLAN.md | changed (file v1.3) |

### SPEC.md

1.8, founder-initiated: new §4.6.1 consolidates authentication security — codes-not-links for password reset and email change with a checkable "we never email login links" promise, multi-credential capability built in from day one with passkeys deferred as a feature, per-account/per-IP login throttling, Argon2id password hashing, breach-password rejection at registration and password change, SPF/DKIM/DMARC at `p=reject`; CAPTCHA and defensive domain hygiene both considered and declined for v1; §4.1, §4.6, §12, §13.6, §16 cross-referenced; constants `RESET_CODE_TTL_MINUTES`, `RESET_CODE_LENGTH`, `LOGIN_ATTEMPT_LIMIT`, `LOGIN_LOCKOUT_MINUTES` added (§14).

### ARCHITECTURE.md

1.4, synced to SPEC v1.8: authentication-security mechanisms recorded in §7 (codes-not-links reset via a hashed short-lived code table, a `credentials` table holding multiple credential types so passkeys drop in later, Argon2id hashing with its one added dependency, per-account/per-IP login backoff, server-to-server breach-password check, SPF/DKIM/DMARC `p=reject`); data-model additions in §4; DMARC note in §3.6; CAPTCHA row added to §14; additive, no change to any existing structure.

### BUILD_PLAN.md

1.3, synced to SPEC v1.8 / ARCHITECTURE v1.4 (2026-07-21): authentication security folded into existing phases — Step 2.5 gains the `credentials`/`credential_codes`/`login_attempts` tables, codes-not-links reset, the "we never email login links" promise, and Argon2id; Step 3.1 gains the breach-password check and code-based email verification; Step 5.5 gains SPF/DMARC `p=reject`; Step 13.4 gains login backoff; Step 16.1 gains the auth-security checks; Appendix rule 6 notes the one approved new dependency.

---

## 1.7 — 2026-07-13 (see placement note)

| File | Status |
|---|---|
| README.md | not recorded — README carried no version number before 1.17 |
| SPEC.md | changed (file v1.7) |
| ARCHITECTURE.md | changed (file v1.3) — placement inferred, see note |
| BUILD_PLAN.md | changed (files v1.1 and v1.2) — placement inferred, see note |

### SPEC.md

1.7, founder-initiated: image sizing and display — proportional scale-to-fit with click-to-expand overlay, stored images capped at a 3840 px long edge with server-side downscaling, `IMAGE_UPLOAD_MAX_MB` = 20 (§7.2.2).

### ARCHITECTURE.md

1.3, founder-requested 2026-07-13: §13 expanded to record the full scaling path discussed in build-plan review — staged promotions, sharding locality, and the TLS-terminates-only-on-our-machines principle generalizing the Cloudflare-proxy ban; additive, changes nothing about v1.

*Carried from ARCHITECTURE.md's status line:* "1.3 and earlier **approved as a whole by founder 2026-07-08**".

### BUILD_PLAN.md

1.1: Phase 4 clarified during review — Step 4.1 explicitly defines the bare content/contact data models the engine tests need, tables only; Step 9.1 accordingly becomes UI-only. Engine-first ordering approved by founder 2026-07-13.

1.2: rule-5 enforcement made mechanical — Step 2.4 grows tool deny rules, a pre-commit hook, and a constants tripwire test; §0.2 rules 3 and 5 updated to match. Also approved by founder 2026-07-13: early deploy (Phase 5) and the Cloudflare no-proxy warning (Step 1.3); Step 5.1 geography recorded (US + Canada → Hetzner Ashburn VA). ARCHITECTURE bumped to v1.3 same day, §13 scaling path recorded. The §0.2 working rhythm approved by founder 2026-07-13 — all five flagged judgment calls now ruled in favor.

### Placement note

ARCHITECTURE v1.3 and BUILD_PLAN v1.1–v1.2 are the only historical entries that name no
SPEC version to sync to. All three are dated 2026-07-13, which puts them after project
1.5 (BUILD_PLAN v1.0, 2026-07-08) and before project 1.8 (2026-07-21) — a range of
project versions 1.5 to 1.7. Per the reconstruction rule they are filed under the
highest version in that range. The SPEC version current on 2026-07-13 is **not
recorded**; 1.6 and 1.7 carry no dates.

---

## 1.6 — date not recorded

| File | Status |
|---|---|
| README.md | not recorded — README carried no version number before 1.17 |
| SPEC.md | changed (file v1.6) |
| ARCHITECTURE.md | unchanged since 1.5 (file v1.2) |
| BUILD_PLAN.md | unchanged since 1.5 (file v1.0) |

### SPEC.md

1.6, founder-initiated: text formatting — whitespace preservation with abuse bounds, per-post preformatted/monospace toggle with composer explainer, `POST_LENGTH_MAX` = 10,000, long-post folding at `FEED_FOLD_CHARS` = 500 in the feed and `BLOG_FOLD_CHARS` = 2,000 on profile blogs (§7.2.1, §7.7, §8.1, §9.1); `COMMENT_LENGTH_MAX` = 2,000 asserted, not yet discussed.

---

## 1.5 — 2026-07-08

| File | Status |
|---|---|
| README.md | not recorded — README carried no version number before 1.17 |
| SPEC.md | changed (file v1.5) |
| ARCHITECTURE.md | changed (file v1.2) |
| BUILD_PLAN.md | new (file v1.0) |

### SPEC.md

1.5, founder-initiated: display-name lifecycle — blocklist screening at every name set, 90-day change cooldown, 90-day "formerly" dual display, names always rendered live from the account (§4.5, §4.5.1); global name uniqueness considered and rejected.

### ARCHITECTURE.md

1.2: synced to SPEC v1.5 — display-name lifecycle (§4.5.1): name fields on users, blocklist table, single name-render helper; additive, no structural change.

### BUILD_PLAN.md

1.0 of 2026-07-08 updated same day for SPEC v1.5 name rules: steps 2.3, 3.1, 8.4, 13.3.

---

## 1.4 — date not recorded

| File | Status |
|---|---|
| README.md | not recorded — README carried no version number before 1.17 |
| SPEC.md | changed (file v1.4) |
| ARCHITECTURE.md | changed (file v1.1) |
| BUILD_PLAN.md | not yet written — earliest recorded version is v1.0, filed under project 1.5 |

### SPEC.md

1.4, founder-initiated: theming generalized — spaces-not-content principle plus viewer override (§9.1).

### ARCHITECTURE.md

1.1: synced to SPEC v1.4 — v1.3/v1.4 spec additions checked against this architecture; none require structural change. Explicit notes added for theming (§3.5, §4) and comment-name linking (§5). No section reviewed in Draft 1.0 changes meaning.

---

## 1.3 — date not recorded

| File | Status |
|---|---|
| README.md | not recorded — README carried no version number before 1.17 |
| SPEC.md | changed (file v1.3) |
| ARCHITECTURE.md | unchanged (file Draft 1.0) |
| BUILD_PLAN.md | not yet written — earliest recorded version is v1.0, filed under project 1.5 |

### SPEC.md

1.3, founder-initiated: commenter names link to profiles with visibility-aware rule (§8.1); clickable hashtags as viewer-scoped discover filter (§11.2, §11.4); visible timestamps and expiry countdown (§7.5); `CONTENT_TTL_DAYS` = 90 reconfirmed.

---

## 1.2.1 — date not recorded

| File | Status |
|---|---|
| README.md | not recorded — README carried no version number before 1.17 |
| SPEC.md | changed (file v1.2.1) |
| ARCHITECTURE.md | unchanged (file Draft 1.0) |
| BUILD_PLAN.md | not yet written — earliest recorded version is v1.0, filed under project 1.5 |

### SPEC.md

1.2.1: clarified login-email change flow in §4.6 and contact-item self-management in §10.2.

### Earlier versions

SPEC.md's history block began at 1.2.1. **Versions 1.0, 1.1 and 1.2 have no recorded
entries** anywhere in the four documents, and none is reconstructed here.
ARCHITECTURE.md's "Draft 1.0" predates SPEC 1.3 (ARCHITECTURE v1.1 records checking the
"v1.3/v1.4 spec additions" against it) but its own date and contents are not recorded.

---

## Appendix — per-file version numbers mapped to project versions

Conversations and notes made before 1.17 refer to the old per-file version numbers. This
table is the translation. Every project version at which a file did not change is
omitted from that file's column; the file simply kept the version above it.

| Project version | README.md | SPEC.md | ARCHITECTURE.md | BUILD_PLAN.md |
|---|---|---|---|---|
| 1.17 | 1.17 | 1.17 | 1.17 | 1.17 |
| 1.16 | — | 1.16 | *(still 1.7)* | *(still 1.6)* |
| 1.15 | — | 1.15 | 1.7 | 1.6 |
| 1.14 | — | 1.14 | *(still 1.6)* | *(still 1.5)* |
| 1.13 | — | 1.13 | *(still 1.6)* | *(still 1.5)* |
| 1.12 | — | 1.12 | 1.6 | 1.5 |
| 1.11 | — | 1.11 | *(still 1.5, renamed)* | *(still 1.4, renamed)* |
| 1.10 | — | 1.10 | 1.5 | 1.4 |
| 1.9 | — | 1.9 | *(still 1.4)* | *(still 1.3)* |
| 1.8 | — | 1.8 | 1.4 | 1.3 |
| 1.7 | — | 1.7 | 1.3 | 1.1, 1.2 |
| 1.6 | — | 1.6 | *(still 1.2)* | *(still 1.0)* |
| 1.5 | — | 1.5 | 1.2 | 1.0 |
| 1.4 | — | 1.4 | 1.1 | — |
| 1.3 | — | 1.3 | *(still Draft 1.0)* | — |
| 1.2.1 | — | 1.2.1 | Draft 1.0 | — |

**Reading it the other way:** SPEC 1.16 → project 1.16 (SPEC's numbers are the spine and
map one-to-one). ARCHITECTURE 1.7 → project 1.15; 1.6 → 1.12; 1.5 → 1.10; 1.4 → 1.8;
1.3 → 1.7; 1.2 → 1.5; 1.1 → 1.4; Draft 1.0 → 1.2.1 or earlier. BUILD_PLAN 1.6 → project
1.15; 1.5 → 1.12; 1.4 → 1.10; 1.3 → 1.8; 1.2 and 1.1 → 1.7; 1.0 → 1.5. README.md carried
no version number before 1.17.

From 1.17 onward there are no per-file version numbers. Every file is at the project
version, and this file records which of them actually changed.
