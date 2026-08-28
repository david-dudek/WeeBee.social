# Mockup session M8 — every email the platform sends

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** `mockups/pages/emails/` (nine templates, each HTML + plain-text), `mockups/CRIB.md`, `mockups/NOTES.md`, `mockups/pages/index.html`. **No design document is edited.**
> **Depends on:** M1 (harness, crib sheet). Independent of M2–M7; **may be folded into M7** if that session runs short.
> **Expected outcome:** SPEC §16.1's *"every email the platform sends"* is in scope and now exists, each with the plain-text alternative §16.3 requires.

---

You are working in the WeeBee design-document repository — a small, private, deliberately
anti-viral social network whose design documents exist but whose platform has not been built.
Read `README.md`, then `prompts/mockups/README.md`, `mockups/NOTES.md` and `mockups/CRIB.md`.

This is session M8, the last of eight building **browser-viewable mockups of the design exactly
as `SPEC.md` and `ARCHITECTURE.md` already describe it.** SPEC §16.1 puts every platform email
inside the accessibility commitment, so they are mockup material like any page.

**Email is the one channel where the platform legitimately sends links** (§4.6.1), which is why
the rules below about links and timestamps are unusually specific. They are the whole point of
this session.

## Standing constraints

- **Build only what the documents describe.** No invented features, no fixes. Contradictions
  go in `mockups/NOTES.md`; build on regardless.
- **Never edit** `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md` or
  anything in `prompts/`. Write inside `mockups/` only.
- **SPEC leads** where ARCHITECTURE lags it (prompt 09 has not been run).
- **Neutral fidelity**, and here that is a requirement rather than a preference: §16.3 says
  every platform email must be **legible without images or CSS**. No images, no web fonts,
  no layout that depends on a stylesheet.
- **Every email gets two files**: `name.html` and `name.txt` — §16.3: *"Every platform email is
  sent with a plain-text alternative and is legible without images or CSS."* The `.txt` is not
  a stripped copy made carelessly; it is the version many people will actually read.
- Render each in the browser as an ordinary page (a simple wrapper showing From / To / Subject
  above the body is fine, and useful — the subject line is part of the design).

## What to read

| Document | Sections | Lines (v1.27) |
|---|---|---|
| SPEC | §4.1 Registration (the invite email) | 68–75 |
| SPEC | §4.6 Authentication and recovery, §4.6.1 Credential security and anti-phishing | 102–135 |
| SPEC | §4.7 Account deletion, §4.8 Inactivity deletion | 135–150 |
| SPEC | §12 opening, §12.1, §12.2, §12.3 | 728–777 |
| SPEC | §13.2.1 The three outcomes — the **Warn** subsection | 812–855 |
| SPEC | §7.5.1 Displayed time (the two exceptions) | 286–328 |
| SPEC | §16.1, §16.3 (the **Email** bullet) | 999–1004, 1027–1083 |
| ARCHITECTURE | §3.6 Email: the one outside service | 162–171 |

## The three rules that govern all nine

1. **Codes, not links — with exactly one exception.** §4.6.1: password reset, login-email
   change and registration verification are completed with **a short, single-use, time-limited
   numeric code** the user types into a page they reached by navigating to the site themselves.
   *"Invitations remain links (§4.1), and only invitations"* — a brand-new user has no session
   and no page open. **Every other action email either carries no link or uses a code.**
2. **No relative ages, ever; absolute timestamps where §7.5.1's two exceptions apply.**
   §12.3, narrowed in v1.26: a relative age is computed when mail is sent and read whenever the
   recipient opens it, so it would be false by then. But *"an absolute timestamp has none of
   that problem, and is not banned here"* — a **security-event mail carries an absolute time**
   (§4.6.1) and an **inactivity warning states the absolute deletion date** (§4.8).
3. **Names, never numbers, and never an excerpt.** §12.2 governs notification content wherever
   it appears: the actor's name, the event type in specific plain text, and a link — **never an
   excerpt of post or comment body text**, and multiple actors listed by name overflowing to
   *"and others"*, never *"3 new comments"*.

## What to build

`mockups/pages/emails/`, nine templates, each `.html` + `.txt`:

### 1. `invite`
§4.1: a single-use link/code sent by email, expiring after `INVITE_EXPIRY_DAYS` = 14, expired
invites returning to the sender's budget. **The one email that carries a link** (§4.6.1) — and
worth saying so inside it, since the platform's standing promise is that nothing else does.

### 2. `verify-code`
Registration email verification, §4.1 and §4.6.1: a numeric code, `RESET_CODE_LENGTH` = 6
digits, valid `RESET_CODE_TTL_MINUTES` = 15. **No link.**

### 3. `reset-code`
Password reset, §4.6.1. A code, typed into a page the user opens **from the login screen**.
Carry the checkable promise verbatim: *"WeeBee will never email you a link to log in or reset
your password — only a code you type in yourself."*

### 4. `email-change-code` and `email-change-notice`
§4.6: the code goes **to the new address** and is entered back into the already-open settings
page; **a notice is sent to the old address**. Two templates in one section — the notice
carries no code and no link.

### 5. `security-event`
§4.6.1: new-device login, password change, email change. *"These events carry absolute
timestamps wherever they appear"* — §4.6.1's own reason is that *"'was that login me?' is not a
question anyone can answer with 'several hours ago'."* Use an absolute time, e.g. the form
§12.3 gives: *2026-08-04 21:14 UTC*.

### 6. `inactivity-dormant`
§4.8's first two warnings, at 180 and 365 days since last login — *"gentle 'your account is
dormant' notes"*.

### 7. `inactivity-deletion`
§4.8's last two, at 670 and 700 days — **explicit deletion warnings, 60 and 30 days before
deletion**, which **state the absolute deletion date**: §4.8's own example is *"your account
will be deleted on 12 March"*, **never "in a couple of months"**. §4.8 is blunt about why: *"a
deletion warning that cannot say when is not a warning."*

### 8. `operator-warning`
§13.2.1's **Warn** outcome. Four constraints, all of them load-bearing:

- **It carries no link** (§4.6.1) and **asks for nothing back**.
- **It never identifies the reporter.** §13.2.1: *"a warning naming who complained makes
  reporting dangerous — which would cost the platform the only operator-level safety mechanism
  it has."*
- **It is not subject to §12's optional-email setting** — an account notice is not a social
  notification, and it sits alongside §4.8's inactivity warnings and §4.6.1's security mails.
- **There is no in-feed equivalent.** §13.2.1 considered and rejected one; nothing in this
  email may imply the user will also see it in the app.

The operator's text is the body; write a plausible neutral example and mark it as an example.

### 9. `social-notification`
§12's optional email delivery of an in-feed notification. Governed by §12.2 entirely:

- Actor's name (rendered live), the event type **in specific plain text**, and a link.
- **No excerpt of post or comment body text** — §12.2: a notification carrying content *"turns
  a pull-model profile post into a push-model feed post with an audience of up to 300."*
- **Names, never numbers** — *"Alice and Tom commented on your post"*, overflowing to *"and
  others"*, **never "3 new comments"**. **No unread-count badge exists anywhere.**
- **No relative age in the body** (§12.3, rule 2 above). Note in NOTES.md that this leaves the
  mail with no age at all, which §12.3 answers deliberately: *"the mail client's own
  received-time is more accurate than anything the body could assert."*
- **No engagement bait** — §12.2 bans it by name (*"you have memories!"*).

## Before you finish

Check every template:

- **each has both `.html` and `.txt`**, and the HTML is legible with CSS disabled (§16.3)
- **no images anywhere** in any email
- **no link in any email except `invite`** (§4.6.1)
- **no relative age in any email** (§12.3); **absolute times only in `security-event` and
  `inactivity-deletion`** (§4.6.1, §4.8)
- **no excerpt of any post or comment**, and **no count of anything** (§12.2, §17)
- `lang` set, one `<h1>`, a descriptive `<title>` on each HTML template
- each reflows at **320 px**

Then: add this session's strings to `CRIB.md`, add the templates to `pages/index.html`, update
`NOTES.md`, and **print the contents of NOTES.md in full** — this is the last session of the
track, so that printout is the accumulated gap log the founder reads alongside the mockups.
Finish by writing a short closing section at the top of `NOTES.md` saying how many surfaces
were built and which of them were **assembled or inferred rather than specified**
(`settings.html`, `groups.html`, `invites.html`, `_nav.html` at minimum).

Do not touch `TODO.md` or `CHANGELOG.md`.
