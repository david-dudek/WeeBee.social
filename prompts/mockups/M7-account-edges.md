# Mockup session M7 — the account edges: logged-out, locked-out, banned, gone

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** `mockups/pages/` (login, reset, invite redemption, invites, banned, deactivated, export, errors, maintenance), `mockups/CRIB.md`, `mockups/NOTES.md`, `mockups/pages/index.html`. **No design document is edited.**
> **Depends on:** M1 (harness, crib sheet). Independent of M2–M6, so it can run out of order if convenient.
> **Expected outcome:** every state an account can be in has a page, including the three the platform hopes nobody sees.

---

You are working in the WeeBee design-document repository — a small, private, deliberately
anti-viral social network whose design documents exist but whose platform has not been built.
Read `README.md`, then `prompts/mockups/README.md`, `mockups/NOTES.md` and `mockups/CRIB.md`.

This is session M7 of eight building **browser-viewable mockups of the design exactly as
`SPEC.md` and `ARCHITECTURE.md` already describe it.** These are the pages SPEC §16.1 names as
*"logged-out pages (login, password reset, invite redemption) … error and empty states"*, plus
the account states §4.7 and §13.2.1 define.

**If M6 ran smoothly and this session runs short, M8 (emails) may be folded in.** Decide at the
time; do not assume it.

## Standing constraints

- **Build only what the documents describe.** No invented features, no fixes. Contradictions
  go in `mockups/NOTES.md`; build on regardless.
- **Never edit** `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md` or
  anything in `prompts/`. Write inside `mockups/` only.
- **SPEC leads** where ARCHITECTURE lags it (prompt 09 has not been run).
- **Neutral, layout-true fidelity**; the existing `styles.css`; no invented brand palette.
- **Static pages, no scripts**; **nothing fetched from anywhere**; compose the M1 partials.
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
| SPEC | §4.1 Registration, §4.2 Invite budgets | 68–80 |
| SPEC | §4.4 Age, §4.5 Names and identity | 85–95 |
| SPEC | §4.6 Authentication and recovery, §4.6.1 Credential security and anti-phishing | 102–135 |
| SPEC | §4.7 Account deletion, §4.8 Inactivity deletion, §4.9 Data export | 135–153 |
| SPEC | §9.3 Access rules | 564–571 |
| SPEC | §13.2.1 The three outcomes, defined — **point 3 especially** | 812–855 |
| SPEC | §13.6 Rate limits | 876–898 |
| SPEC | §16.1 The commitment (the scope sentence), §16.3, §16.4 | 999–1004, 1027–1089 |
| ARCHITECTURE | §7.2 — *"Planned downtime, and the maintenance page"* | 430–491 |

## What to build

### 1. `pages/login.html`

- Password login; login is **by email address** (§4.5, §4.6).
- **The checkable promise, verbatim** (§4.6.1), shown at this touchpoint: *"WeeBee will never
  email you a link to log in or reset your password — only a code you type in yourself."*
  §4.6.1 explains its value — it makes any look-alike "click here to log in" email
  self-evidently fake — so it goes on the page as prominent real text, not fine print.
- A link to the reset page, since §4.6.1 requires the user to open it **from the login screen**
  rather than from an email.
- **No CAPTCHA of any kind** (§4.6.1, §16.4, §17). Nothing resembling one.

### 2. `pages/reset-request.html` and `pages/reset-code.html`

§4.6.1: password reset is completed with **a short, single-use, time-limited numeric code**
that the platform emails and the user types into a page they reached **by navigating to the
site themselves**. `RESET_CODE_LENGTH` = 6 digits, `RESET_CODE_TTL_MINUTES` = 15.

- **The time limit is told to the user in text**, and they can always request a new code
  (§16.3, "Time limits and motion"). Render that.
- **The lockout state**: login attempts are rate-limited per account *and* per source address
  with exponential backoff and temporary lockout (`LOGIN_ATTEMPT_LIMIT` ≈ 5,
  `LOGIN_LOCKOUT_MINUTES` ≈ 15). §16.3 requires lockout messages to use **polite live
  regions**; the message itself is honest and names the fix.

### 3. `pages/invite-redeem.html`

§4.1 — **the only way to create an account.** Redeeming requires: a working email address
verified by a numeric code, a password, a display name, and **an attestation of being 18 or
older** (§4.4). **Registration collects nothing else — no phone number, no legal name, no
address.** Nothing on the page may ask for more.

Show three rejection states, all as text tied to their field and describing the fix
(§16.3 3.3.1/3.3.3):

- a **known-breached password**, refused with an honest explanation (§4.6.1)
- a **display name rejected by `NAME_BLOCKLIST`** at save time, with an honest message (§4.5)
- the invite itself expired — `INVITE_EXPIRY_DAYS` = 14, and expired invites return to the
  sender's budget (§4.1)

State on the page that **inviter and invitee automatically become friends** (§4.1).

### 4. `pages/invites.html` — **inferred, not specified**

§4.2 gives the mechanics — `INVITE_BANK_MAX` = 5, +1 every `INVITE_REPLENISH_DAYS` = 30 days,
new accounts start with 2 — but **no section of either document describes a surface where a
user sees their budget or sends an invite.** Build the minimum the mechanics imply, **label the
page visibly as inferred**, and record it in NOTES.md.

An invite is *"a single-use link/code sent by email"* (§4.1). Show the budget as **words, not a
progress bar or a badge** — §17 bans visible counts, and it is worth a NOTES.md line that a
literal invite count is arguably the one number a user must be shown.

### 5. `pages/banned.html`

§13.2.1 point 3 — the single page a banned person reaches. Authentication succeeds and
authorization is empty.

- It *"states plainly that the account has been suspended by the operator and that their
  content is hidden from other members."*
- **It names no reason.** §13.2.1: *"reasons are the deferred policy question, and a generated
  reason line would promise a consistency the v1 workflow cannot keep."* Do not write one.
- **From that page exactly two things work: data export (§4.9) and account deletion (§4.7).**
  *"Everything else — feed, composers, comment boxes, requests, discovery, the report action,
  the rest of settings — is that page."* Draw no navigation to anything else. **This means the
  page does not use the standard `_nav.html`** — note that decision in NOTES.md.
- The register is *"the platform's ordinary honest register"* — plain, not punitive.

### 6. `pages/deactivated.html`

§4.7 — the user's own view during the deletion grace period, which keeps working so they can
cancel. It carries **a banner with the absolute erasure date** — *"an account event, and
therefore one of §7.5.1's two narrow exceptions to relative time."* Use an absolute date here
and nowhere else in the mockups except the security and inactivity emails.

`DELETE_GRACE_DAYS` = 30. State §4.7's honest promise in the platform's own words: **erased
from the platform at once, and gone from the last encrypted backup within
`BACKUP_RETENTION_DAYS` = 30 days after that.** Do not soften it and do not write "gone by day
120" — §4.7 and §7.5 both refuse that phrasing.

### 7. `pages/export.html`

§4.9: a complete, well-structured copy of profile, posts, comments authored, friend list,
groups, contact card and images, in **JSON plus image files**. §7.5.1 notes this is where exact
timestamps live, since they appear nowhere in the interface — say so on the page.

### 8. `pages/errors.html`

A single page collecting the error and empty states §16.1 puts in scope. At minimum:

- **§9.3's single response**, and the fact that it is single. *"A viewer who may not see a
  profile gets one response, identical for a block (§5.4), no mutual friend, a deactivated
  account (§4.7), a **banned** account (§13.2.1) and a profile that never existed. Any
  variation between those cases is an oracle."* Render it once, and list beneath it — as page
  text for the founder's benefit — the five cases it covers.
- **A rate-limit "slow down" message** (§13.6), honest, naming when the action becomes
  available again.
- **The feed-post spacing message**: *"slow down, you can post again in N minutes"*
  (`POST_MIN_INTERVAL_MINUTES` ≈ 10, §13.6).
- A genuine **empty state** — a feed with nothing in it — and a note that §8.2.2 forbids empty
  states for reactions specifically (*"no 'no reactions yet', which is a count of zero written
  out in words"*), so the two are not the same rule.

### 9. `pages/maintenance.html`

ARCHITECTURE §7.2. Caddy is the front door and stays up when the app is down, so this page
lives in Caddy: *"one static, first-party page, served with **HTTP 503 and a `Retry-After`
header** — never 200."* Put the status and header in an HTML comment at the top, since a static
mockup cannot send them.

*"It is a user-facing surface, so SPEC §16 applies to it as much as to any other: `lang`, a page
title, one `<h1>`, contrast that does not depend on a theme being loaded, and — per §7.1 —
nothing fetched from anywhere."* That last clause is a real constraint on this page: **it must
not link to `styles.css` either.** Inline whatever it needs, and say so on the page.

## Before you finish

Check every page, as in the earlier sessions, plus four specific to this set:

- **`banned.html` carries no navigation and no reason**, and offers only export and deletion
- **`maintenance.html` fetches nothing at all**, `styles.css` included
- **the only absolute dates in the whole mockup set are on `deactivated.html`** (§4.7's banner)
  — everywhere else, relative phrases from §7.5.1's ladder
- **no CAPTCHA, no third-party human-challenge, anywhere** (§4.6.1, §16.4, §17)

Plus the standing list: one `<h1>` and a unique `<title>` per page; skip link first focusable;
`lang` set; landmarks present; every `<img>` has an `alt`; every input has an associated
visible label, placeholders never labels; errors are text tied to their field and describe the
fix; no `tabindex` above 0; no `title` attribute; no timestamp in any markup attribute; reflow
at **320 px** with no horizontal page scroll.

Then: add this session's strings to `CRIB.md`, add its pages to `pages/index.html`, update
`NOTES.md`, and **print the contents of NOTES.md**. Do not touch `TODO.md` or `CHANGELOG.md`.
