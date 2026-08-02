# Build Plan — WeeBee

**Status:** Draft 1.6 — under founder review · 2026-08-02 *(1.0 of 2026-07-08 updated same day for SPEC v1.5 name rules: steps 2.3, 3.1, 8.4, 13.3. 1.1: Phase 4 clarified during review — Step 4.1 explicitly defines the bare content/contact data models the engine tests need, tables only; Step 9.1 accordingly becomes UI-only. Engine-first ordering approved by founder 2026-07-13. 1.2: rule-5 enforcement made mechanical — Step 2.4 grows tool deny rules, a pre-commit hook, and a constants tripwire test; §0.2 rules 3 and 5 updated to match. Also approved by founder 2026-07-13: early deploy (Phase 5) and the Cloudflare no-proxy warning (Step 1.3); Step 5.1 geography recorded (US + Canada → Hetzner Ashburn VA). ARCHITECTURE bumped to v1.3 same day, §13 scaling path recorded. The §0.2 working rhythm approved by founder 2026-07-13 — all five flagged judgment calls now ruled in favor. 1.3, synced to SPEC v1.8 / ARCHITECTURE v1.4 (2026-07-21): authentication security folded into existing phases — Step 2.5 gains the `credentials`/`credential_codes`/`login_attempts` tables, codes-not-links reset, the "we never email login links" promise, and Argon2id; Step 3.1 gains the breach-password check and code-based email verification; Step 5.5 gains SPF/DMARC `p=reject`; Step 13.4 gains login backoff; Step 16.1 gains the auth-security checks; Appendix rule 6 notes the one approved new dependency. 1.4, synced to SPEC v1.10 / ARCHITECTURE v1.5 (2026-07-21): **accessibility (WCAG 2.1 AA) folded into the existing phases rather than bolted on at the end** — Step 2.5 builds the base-template foundations and the shared accessible partials every later step composes, plus a keyboard/VoiceOver check in its verification; Step 6.1 adds image alt text and Step 6.2's verification the composer's deliberate-choice rule; Step 8.2 adds the automated `THEME_SET` contrast gate; Step 13.2 adds the "accessibility problem" request category; new Step 15.2 is the accessibility statement; new Step 16.5 is the five-pass pre-launch audit; Appendix gains rule 9. 1.5, synced to SPEC v1.12 / ARCHITECTURE v1.6 (2026-07-26): the **URL allowlist becomes a validator, not a domain list** — Step 6.2 now builds one shared link validator with the mandatory **open-redirector rejection** and the contact-card rejection message, and its verification adds the redirector and look-alike-host attack cases; Step 13.3's admin editor gains the category and redirector-pattern fields plus the add-inactive-by-default rule; Step 16.1's security pass confirms the validator. Folded into existing phases; no new phase, no renumbering. 1.6, synced to SPEC v1.13–v1.15 / ARCHITECTURE v1.7 (2026-08-02): **notifications, editing, relative timestamps and the bio fields folded into existing phases.** Step 2.3 gains the **shared time-rendering helper** alongside the name helper, built before any surface can print a date, with its boundary-table test; Step 6.2 gains `POST_MIN_INTERVAL_MINUTES` spacing; new Step **6.6** builds editing for posts and comments, with its verification written as the **attack case** — publish clean, edit in a disallowed link, confirm refusal — because a validator wired only into the create path is the failure this step exists to prevent; Step 6.5's "visible timestamps" becomes the relative ladder plus the absolute expiry countdown; Step 7.1 gains comment editing and the author-cannot-edit rule; Step 8.1 gains the two bio fields with screening, the no-links rule on the short bio, and the change cooldown; Phase 12 is rewritten from two steps to four (per-field profile triggers, the two coalescing modes, following a post, and the live-render/no-counts rules); Step 13.4 records that three §13.6 controls are timestamp-based rather than day counters; Step 16.1 confirms edit-path revalidation; Appendix gains rules 10 and 11. Folded into existing phases; one new step (6.6), no renumbering of existing steps.)*
**Companion to:** SPEC.md v1.15 (§7.5.1, §7.8, §9.4, §12) and ARCHITECTURE.md v1.7 (§3.8, §4, §7). This is deliverable (c) per SPEC §18. The actual AI-coding prompts are deliverable (d); every `[AI]` step below will have a matching numbered prompt there.
**Audience:** The founder, and the AI coding models that will execute the `[AI]` steps.

---

## 0. How to Read and Use This Plan

### 0.1 Step labels

- **[FOUNDER]** — you do this yourself, outside any AI chat: account signups, DNS settings, running commands on the server, plugging in credit cards. Exact instructions are given inline.
- **[AI]** — an AI coding model does this, driven by the matching prompt from deliverable (d). Your job on these steps is to run the prompt, skim the result, run the verification, and commit.
- **[FOUNDER+AI]** — collaborative: the AI drafts, you decide (e.g., the privacy policy, the reaction phrases).

### 0.2 The working rhythm (read this twice — it is the plan's real safety mechanism)

1. **One step at a time, in order.** Steps are sequenced so that everything a step needs already exists. Skipping ahead is how AI-built projects rot.
2. **Every step ends with a verification.** Do it. If it fails, do not proceed — tell the AI model what you saw and let it fix the step. "It probably works" is not a state this project recognizes.
3. **Commit to git after every completed step**, with the step number in the message (e.g., `Step 6.2: feed post composer`). This makes every AI mistake reversible with one command, which is your insurance against a less capable model damaging working code. **Before committing, glance at the changed-file names** (`git status`) — SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md, and `constants.py` must never appear in that list unless you personally ordered the change. You are reading filenames, not code; it takes five seconds and no law file can change without leaving its name there.
4. **Fresh chat per step (or small group of related steps).** Long AI chats degrade; the prompts in deliverable (d) are written to be self-contained so a new chat loses nothing.
5. **The AI never edits SPEC.md, ARCHITECTURE.md, this file, or the values in `constants.py`.** If a step seems to require changing any of those, stop — that's a design conversation, not a coding task. This rule is enforced by mechanism, not obedience: Step 2.4 installs tool-level deny rules, a git pre-commit hook, and a constants tripwire test, and rule 3's filename glance is the human backstop. A prompt is a request; those are locks. If an AI ever *reports* it couldn't edit one of these files, that is the system working — it means the model wanted to move a goalpost, which is your cue for a design conversation.
6. **When stuck:** paste the exact error text and what you did into the chat. If two fix attempts fail, revert to the last commit (`git checkout .`) and re-run the step's prompt in a fresh chat, telling it what failed last time. This recovers from most AI dead ends.

### 0.3 Rough effort expectations

Phases 1–5 (skeleton to first deploy) are the steep part — expect several sessions of evenings/weekends. Phases 6–14 are repetitive feature work at a rhythm you'll have learned. There is no calendar deadline; the sequence protects you, not a schedule.

---

## Phase 1 — Your Machine [FOUNDER]

Everything here happens on your Mac.

**1.1 [FOUNDER] Install the tools.**
1. Install **Docker Desktop for Mac** from docker.com (the free Personal tier). Launch it once so it finishes setup.
2. Verify **git** is present: open Terminal, run `git --version`. If macOS offers to install command-line developer tools, accept.
3. Install your AI coding tool (e.g., **Claude Code**: `npm install -g @anthropic-ai/claude-code` after installing Node.js from nodejs.org, or the desktop app). Any capable coding agent works with the deliverable-(d) prompts.
✅ *Done when:* `docker --version` and `git --version` both print versions in Terminal.

**1.2 [FOUNDER] Create the project folder and repository.**
1. In Terminal: `mkdir ~/thenetwork && cd ~/thenetwork && git init`
2. Copy SPEC.md, ARCHITECTURE.md, and this file into it (they are the project's law and must travel with the code).
3. On github.com, create a **private** repository named `thenetwork`. Follow GitHub's shown commands to connect and push. (Code only, ever — never data, never secrets. Step 2.4's `.gitignore` enforces this.)
✅ *Done when:* the three documents are visible in the private GitHub repo.

**1.3 [FOUNDER] Register the domain. — ✅ DONE (2026-07-25)**
The domain is **`weebee.social`**, registered at **Porkbun**. The platform name is **WeeBee** (SPEC §2). No defensive/typo domains are being registered — this is a settled decision (SPEC §4.6.1). Remaining reminder for the DNS steps below (Phase 5):
- **Do not put the domain behind Cloudflare's proxy service** now or later. Cloudflare-the-registrar/DNS is fine, but its orange-cloud "proxy" mode would terminate HTTPS at Cloudflare, meaning a third party decrypts all user traffic — a violation of the privacy architecture (ARCHITECTURE §2, Decision 2). DNS-only, always. (Porkbun's own DNS is DNS-only by default, so simply using Porkbun's nameservers satisfies this.)
✅ *Done when:* ~~you own the domain and can see its DNS management page.~~ **Met — `weebee.social` owned, Porkbun DNS panel accessible.**

---

## Phase 2 — Skeleton Application [AI]

Goal: an empty but *running* Django site in Docker on your Mac.

**2.1 [AI] Project scaffold.** Django (current LTS) project + Docker Compose with three services (`app` via Gunicorn, `db` PostgreSQL 16, `caddy`), per ARCHITECTURE §3.4. A single placeholder page.
✅ `docker compose up` then http://localhost shows the placeholder.

**2.2 [AI] `constants.py`.** Every SPEC §14 constant, named exactly as in SPEC, each with a comment citing its SPEC section and the raise-only rule.
✅ You read the file side-by-side with SPEC §14 and every row matches.

**2.3 [AI] Custom user model.** UUID primary key; login email as unique credential; display name plus previous-name and name-changed-date fields (SPEC §4.5.1); the lifecycle fields from ARCHITECTURE §4 (last-login, deactivation state, invite budget fields). Includes the **single shared name-render helper** ("Name" or "Name (formerly Old)" during a transition) that every later template must use — names are never rendered any other way. Done **before anything else touches the database** — retrofitting a Django user model later is notoriously painful.

Build the **shared time-rendering helper** here too (SPEC §7.5.1, ARCHITECTURE §4), for the same reason the name helper is built here: it must exist before any surface can print a date, or surfaces will each grow their own. It takes a timestamp and returns one phrase from the 40-row ladder — "Just now", "A few hours ago", "Over a week ago" — and it **returns the phrase and nothing else**: no `title` attribute, no `<time datetime="…">`, no data attribute carrying the real timestamp. The two absolute-time cases (the expiry countdown, and account/security events) are separate formatters, not options on this one.
✅ AI-written model tests pass (including the helper's formerly-window arithmetic); you can create a user via Django admin. **The time helper's boundary table test passes**: one case per ladder row at its boundary and one unit either side, plus a totality test sweeping a wide range of ages and asserting every one returns a non-empty phrase. That totality test is the point — a gap between two bounds renders an empty string, which no feature test would ever catch and no user would report as anything more useful than "sometimes there's no date."

**2.4 [AI] Housekeeping files and the law-file guards.** `.gitignore` (secrets, environment files, images, database volumes — with comments saying why), an environment-file template, a README pointing at the three law documents. Plus the three mechanical guards enforcing §0.2 rule 5 (the AI never edits the law files), layered so a violation is blocked, loud, or both:
1. **Tool deny rules** — the AI coding tool's permission settings file (e.g., Claude Code's `.claude/settings.json`) refusing edits to SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md, and `constants.py`. The harness blocks the edit regardless of what the model decides.
2. **A git pre-commit hook** — a small script git runs before accepting any commit, refusing any commit that touches a law file; overriding it requires a deliberate founder act, so "forgot to look" cannot happen.
3. **A tripwire test** — a tiny test file asserting every SPEC §14 constant's exact value (`FRIEND_CAP` is 300, `CONTENT_TTL_DAYS` is 90, …). Tests run at every step, so a quietly changed constant fails loudly by name.
(Layer 4 is free: the authoritative document copies live outside the repo, and GitHub keeps every committed version — any tampering is diffable and reversible.)
✅ `git status` shows no secret or data files as committable; an attempted edit to SPEC.md via the AI tool is refused; a commit touching a law file is rejected by the hook; temporarily change one constant → the tripwire test fails naming it (then revert).

**2.5 [AI] Authentication pages and the credential layer.** Login, logout, and password reset, base page template + the single CSS file, mobile-first (ARCHITECTURE §3.5). Logged-out users can reach exactly: login, password reset, invite redemption (stub) — nothing else (SPEC §2, §9.3). The authentication specifics of SPEC §4.6.1 land here:
- **Credential tables** (ARCHITECTURE §4): a `credentials` table (type = password | passkey; only password rows in v1, so passkeys need no later user-model change), a `credential_codes` table (hashed, short-lived, single-use, attempt-capped), and a `login_attempts` table (per-account and per-source-address).
- **Argon2id** as the password hasher (SPEC §4.6.1) — Django's `argon2` hasher; add the `argon2-cffi` dependency (the one approved addition, Appendix rule 6).
- **Codes, not links, for reset.** Password reset emails a numeric code (`RESET_CODE_TTL_MINUTES`, `RESET_CODE_LENGTH`) the user types into the reset page they opened themselves — **no login link is ever emailed.** Codes print to the console locally for now. Show the user-facing promise ("we will never email you a link to log in or reset your password — only a code you type in yourself") on the login and reset pages.
- **Login throttling** (SPEC §4.6.1, §13.6): exponential backoff and temporary lockout keyed on both account and source address (`LOGIN_ATTEMPT_LIMIT`, `LOGIN_LOCKOUT_MINUTES`).
- **The accessibility foundations (SPEC §16, ARCHITECTURE §3.8) — built here, once, and inherited by every later page.** This step is where WCAG 2.1 AA is cheap; retrofitting it in Phase 16 is where it is expensive. Specifically: the base template's `lang`, per-page `<title>`, landmark regions, and skip link; visible focus styling that no theme may remove; and the **shared partials** every later step must compose rather than reinvent — `_field.html` (label + error wiring), `_errors.html`, `_modal.html` (focus trap, Escape, focus restore), `_expandable.html` (`aria-expanded`), `_status.html` (polite live region). The login, reset, and lockout messages are the first users of them.
✅ On your Mac **and on your phone's browser** (same Wi-Fi, using your Mac's local address): log in, log out, reset your password by typing the console-printed **code** (confirm no login link is sent); the reset page shows the "only a code, never a link" promise; hammer a wrong password past the limit and get a clear temporary lockout. Try any other URL logged-out — always redirected to login. **Then unplug your mouse:** reach and operate every control on the login and reset pages with Tab/Shift-Tab/Enter alone, and see where the focus ring is at all times. Turn on VoiceOver (⌘F5) and log in with your eyes closed once — it will be slow and strange; that is the point, and it takes ten minutes on a two-page site.

**2.6 [AI] Seed-data command.** A management command creating ~20 fake users with a realistic friendship web (once friendships exist in Phase 3, it grows with each phase). This is how you test everything without real people.
✅ Command runs; you can log in as any fake user (documented shared password).

---

## Phase 3 — Invitations and the Social Graph [AI]

Goal: the data structures everything else stands on. Mostly models + minimal pages; the polished flows come after the visibility engine exists.

**3.1 [AI] Invites and the invite tree.** Invite creation (budget-checked: bank max 5, new accounts start with 2), single-use emailed code, 14-day expiry returning to budget, redemption flow (email verification **by numeric code, not a link — SPEC §4.6.1**; password **screened against known-breached passwords via the HIBP k-anonymity range API, server-to-server, fail-open on outage — SPEC §4.6.1**; display name — screened against `NAME_BLOCKLIST` with an honest rejection message (SPEC §4.5) — 18+ attestation, per SPEC §4.1), auto-friendship inviter↔invitee, permanent invite-tree record (SPEC §4.3).
✅ As a seeded user, invite a new fake address; redeem it (console code, not a link); a deliberately breached password (e.g., `password123`) is refused with an honest message while a strong one is accepted; the two accounts are friends; the tree row exists; the budget decremented.

**3.2 [AI] Friendships, friend requests, blocks — models and rules.** Symmetric friendships; 300-cap enforced with honest errors (SPEC §5.1); request records with the 90-day declined cooldown (§5.2); block records (§5.4). UI minimal for now.
✅ Model tests pass, including: cap at exactly 300, cooldown arithmetic, block ends friendship.

**3.3 [AI] Groups.** Named private friend lists, ≤30 members, cap warnings (SPEC §6).
✅ Create a group as a fake user; try to add a 31st member; get refused with a clear message.

---

## Phase 4 — The Visibility Engine [AI] ← the most important phase

Goal: the one module every permission decision flows through (ARCHITECTURE §5), built **before any content feature exists**, so no page is ever written that decides visibility for itself.

**4.1 [AI] The engine.** First, the **bare data models the engine reasons over** — posts, post_audience, post/profile hashtag tables, contact_items and contact_overrides: tables only, no pages, no UI (their features arrive in Phases 6–10). Then the five functions of ARCHITECTURE Decision 4 (`are_connected`, `can_see_post`, `can_see_profile_tier`, `visible_contact_card`, `can_act`), blocks checked first in both directions, plus the read-only preview-as mechanism (SPEC §9.5).
**4.2 [AI] The dense test suite.** The project's largest test file: block symmetry and total invisibility, FoF boundaries, audience-snapshot + current-friendship (§7.4), the three-condition hashtag gate (§11.3), contact-cascade conflicts with deny-beats-allow (§10.3), friend-list filtering (§11.5). Tests written from SPEC sentences, each test naming the SPEC section it enforces.
✅ *Phase milestone:* the full suite passes, and you personally read the **test names** top to bottom — they should read like SPEC's rules restated. Any rule you can't find a test for, ask the AI to add. (You are not reading code here; you are auditing coverage by name.)

**4.3 [AI] Friendship flows, now user-facing.** Friend-request send (FoF-only, auto-generated context, no free text), silent decline, unfriend (silent), block/unblock pages — all through the engine.
✅ With two browser windows logged in as two fake users: send/accept a request; block; verify the blocked pair see nothing of each other anywhere.

---

## Phase 5 — The Server: First Deploy [FOUNDER, with AI-written scripts]

Goal: the empty-but-real site running at your domain with HTTPS and real email — while the codebase is still small. Infrastructure problems are far easier to diagnose now than after fourteen more phases. From here on you develop locally and deploy occasionally.

**5.1 [FOUNDER] Decide the two deferred picks.** (Carried here from ARCHITECTURE §15 at your request.)
- **VPS:** recommendation **Hetzner**. Founder stated (2026-07-13 review): first users are in the US plus some in Canada → recommended location **Ashburn VA** (closest to both US and eastern-Canadian population centers; Hillsboro OR only if the circle turns out west-coast-heavy). A ~€6–12/month shared-vCPU instance (2 vCPU / 4 GB) is ample.
- **Email:** recommendation **Postmark** (transactional-only ethos, free 100 emails/month covers the prototype).
✅ Decisions written down; if you deviate from the recommendations, note it so the privacy policy (Step 15.1) names the right processors.

**5.2 [FOUNDER] Create the VPS.**
1. Sign up at the chosen provider; add your **SSH public key** during server creation (if you've never made one: `ssh-keygen -t ed25519` in Terminal, accept defaults, paste the contents of `~/.ssh/id_ed25519.pub`). Password SSH stays off.
2. Create the server (Ubuntu LTS, the size above).
3. In your registrar's DNS page: an **A record** pointing your domain (and `www`) at the server's IP.
✅ `ssh root@yourdomain.com` gives you a server prompt.

**5.3 [AI→FOUNDER] Server preparation script.** The AI writes a commented, idempotent setup script (firewall allowing only SSH/80/443, automatic security updates, fail2ban, Docker installation, non-root deploy user); **you** read the comments, then run it on the server per its instructions.
✅ Script's own final check passes; you can log in as the deploy user.

**5.4 [AI→FOUNDER] Deploy script + Caddy config.** The three-line-spirit deploy of ARCHITECTURE §8 (push code, run migrations, restart containers), Caddy serving your domain with automatic HTTPS. You run your first deploy.
✅ `https://yourdomain.com` shows the login page, padlock valid, plain `http://` redirects to `https://`.

**5.5 [FOUNDER] Email provider setup.**
1. Sign up (Postmark asks what you send — answer: transactional only, invitation/verification/security emails for a private social site).
2. Add the DNS records they give you (DKIM, return-path) at your registrar; wait for their dashboard to verify.
3. **Add SPF and DMARC records (SPEC §4.6.1):** an SPF record authorizing the provider to send for your domain, and a **DMARC record at `p=reject`** so mailbox providers reject anything forging your domain. (Optionally start DMARC at `p=none` for a few days to confirm your legitimate mail passes, then move to `p=reject`.)
4. Put the API key in the server's environment file (never in git).
✅ Password-reset **code** email from the live site lands in your **personal inbox** (not spam); a DMARC checker (e.g., an MXToolbox lookup) shows your domain at `p=reject`.

**5.6 [FOUNDER] Backups.**
1. Create the backup target: **Hetzner Storage Box** (if Hetzner) or **Backblaze B2** — a few dollars/month.
2. The AI writes the nightly backup job (ARCHITECTURE §10: pg_dump + images, encrypted with restic, 30-day retention `BACKUP_RETENTION_DAYS`); you install its credentials and schedule.
3. **Rehearse a restore** onto your Mac following the AI-written runbook. An untested backup is a rumor (ARCHITECTURE §10).
✅ You have personally restored a backup and logged into the restored copy locally.

---

## Phase 6 — Posts [AI]

**6.1 [AI] Image pipeline.** Pillow decode → full re-encode (guaranteed EXIF/GPS destruction) → bounded resize → random filename in a non-web-served folder → DB record; serving only through a permission-checked view (ARCHITECTURE §3.7). **Alt text (SPEC §16.3):** the `images` table gets `alt_text` (≤ `ALT_TEXT_MAX`) and `is_decorative`; every upload form requires a deliberate choice between the two — never silently skipped, never auto-generated — and every rendering surface reads the stored value.
✅ Upload a photo that has GPS EXIF (take one with your phone); download it back; inspect it (Preview → Tools → Show Inspector): no GPS, no EXIF. Copy the image URL into a logged-out window: refused.

**6.2 [AI] Feed posts.** Composer with audience picker (individuals + groups, live count, hard ≤30 with honest narrowing prompt — SPEC §7.3), one optional image, audience snapshot rows (§7.4), and URL allowlist enforcement at composition — see 6.2a, which this step, Step 6.6 (editing) and Step 7.1 (comments) all call. Also **`POST_MIN_INTERVAL_MINUTES` spacing** (SPEC §7.3, §13.6): compare against the author's last feed post's timestamp — not a daily counter — and refuse with "you can post again in N minutes." Profile posts are exempt.

**6.2a [AI] The link validator (SPEC §7.2.3, ARCHITECTURE §7).** **One shared function**, called by every composer that accepts text (feed posts, profile posts, comments) — never reimplemented per surface. It parses the URL (no regex string matching), requires `https`, matches the host **exactly or as a subdomain** of an allowlisted row, and then **rejects that row's redirector patterns**. The redirector step is the one an implementer is most likely to skip and the one that matters most: `youtube.com/redirect?q=…` and `google.com/url?q=…` pass any host check while handing the reader to an arbitrary attacker page. Belt-and-braces: refuse any otherwise-allowed URL whose query string contains an absolute `http(s)://` URL. Shorteners are never allowlistable. **The rejection message** follows SPEC §7.2.3 and the error rules of §16.3 — it says the link isn't permitted, what the allowlist is for, and that anything else can be shared through the contact methods on the user's contact card, with a pointer to the operator request form (§13.5). Links render as **plain clickable links, never embedded or preview-carded** (§7.2).
✅ Attack cases, as tests, not a manual click-through: `https://youtube.com/redirect?q=https://evil.example` → refused; `https://www.google.com/url?q=https://evil.example` → refused; `https://evil-youtube.com/watch?v=1` → refused; `https://youtube.com.attacker.net/watch?v=1` → refused; `http://` (not https) on an allowed host → refused; a plain `https://maps.google.com/…` → accepted. Each refusal names the contact card.
**6.3 [AI] Profile posts.** All-friends visibility, lives on the blog only, friends get a notification record (§7.1).
**6.4 [AI] The feed page.** Strict reverse-chronological: audience-of feed posts + profile-update notifications + system notifications; no ranking of any kind (§7.7).
**6.5 [AI] Expiry.** The `expire_content` cron job (90 days, idempotent — ARCHITECTURE §6), pinning ≤10 profile posts and "pinned" markers (§7.5–7.6). **Two kinds of time appear here and they are deliberately different** (SPEC §7.5, §7.5.1): a post's *age* renders through the Step 2.3 relative helper ("A few days ago"), while the ≤14-day deletion countdown renders as **absolute days** ("deletes in 6 days"), computed per page load, never live-ticking. Vague about the past, exact about the destruction — that contrast is the feature, not an inconsistency to tidy up.

**6.6 [AI] Editing posts and comments (SPEC §7.8).** Authors may edit their own posts (text, image, preformatted toggle, hashtags) and their own comments, until expiry. A nullable `edited_at` drives a permanent plain-text **"edited"** marker showing the *relative* time of the last edit. No version history, no diff, **no notification on edit**. Four rules that are easy to get wrong and expensive to get wrong:
- **Validation is shared with creation, not duplicated.** The edit path runs the same link validator (6.2a), length caps, whitespace normalization, hashtag-vocabulary check and image re-encode as the create path — which in practice means content validation lives in the shared model/form layer, never in the create view.
- **`edited_at` is display-only.** Feed order reads `created_at`; expiry reads `created_at`. No query sorts or filters by `edited_at`, or editing silently becomes a way to bump a post or outlive the 90-day promise.
- **An edit writes no `post_audience` rows.** The one thing an edit may legitimately change is a *profile* post's hashtags, because §11.3's FoF gate is evaluated live by design — and newly-matched FoFs are never notified.
- **The post author may delete any comment but never edit one.** Wire the author's power to the delete path only.
✅ **Written as attack cases, not a click-through:** publish a post with clean text, then edit a disallowed URL into it → **refused** (this is the whole reason this step exists — a validator wired only into the create path is the defect being prevented, and it fails silently); edit a post and confirm it does *not* move in a second account's feed; backdate a post 89 days, edit it, confirm it still expires on schedule rather than getting another 90 days; confirm no notification fires to anyone on the edit; as the post author, confirm there is no route to edit someone else's comment.
✅ Also: submit an image with neither a description nor the "decorative" tick — the composer refuses with an honest message; the audience picker's live count is reachable by keyboard and announced (SPEC §16.3); a folded long post expands with a real button that keeps focus where it was.
✅ *Phase milestone (two browser windows):* post to a hand-picked audience — the included friend sees it, the excluded one doesn't; unfriend and confirm old posts vanish; try a disallowed URL — rejected with explanation; backdate a seeded post 80 days — countdown appears; run `expire_content` against a backdated-91-days post — gone, image file too.

---

## Phase 7 — Comments and Reactions [AI]

**7.1 [AI] Comments.** Flat list; visibility = the post's exactly (via engine); attribution with the visibility-aware profile-link rule (name links only with ≥basic-tier access, plain text otherwise — SPEC §8.1 v1.3); author-delete + post-owner-delete; **author-edit only**, per Step 6.6; own 90-day clock; no images.
**7.2 [AI] Reactions.** One per user per target from `REACTION_SET`; changeable/removable; **visible only to the content's author, as names, never counts** (§8.2).
✅ *Milestone:* commenter's name links for a friend-viewer and is plain text for a stranger-viewer (use a hashtag-gated scenario from the seed data once Phase 10 lands — noted in (d) to re-verify then); reactions invisible to a third account; author sees names, no numbers anywhere.

---

## Phase 8 — Profile Pages and Theming [AI]

**8.1 [AI] The profile page.** SPEC §9.1 section order; the §9.2 tier table via `can_see_profile_tier`; gallery ≤8; the blog filtered per viewer; no deep-link value (every URL permission-checked, UUIDs only). **The two bio fields (SPEC §9.4) are separate columns with different rules, not one field with a length check:**
- `short_bio` ≤ `BIO_SHORT_MAX` — basic tier, so **FoFs see it and it rides along in every friend-request card** (§5.2). Screened against `name_blocklist` at every save (the same check as display names, Step 2.3's neighbour), and **rendered with links disabled** — URLs in it are inert text, never linkified, not even allowlisted ones.
- `extended_bio` ≤ `BIO_EXTENDED_MAX` — friends only, so it is not a push surface: allowlisted links permitted (via 6.2a), no cooldown.
- **`BIO_CHANGE_COOLDOWN_HOURS` on `short_bio` and the profile photo** (SPEC §13.6), with a `BIO_EDIT_GRACE_MINUTES` free window measured from the *first* save in a burst so the clock never restarts. Three carve-outs to implement explicitly: clearing the short bio to empty is never limited; a save rejected by screening starts no clock; the extended bio is exempt.
- Bios get **no "edited" marker** and notify nobody (SPEC §9.4, §12.1) — but every save re-runs validation, or the screening is decorative.
✅ Set a short bio, immediately fix a typo (allowed, inside the grace window), then try a third change an hour later → refused with an honest "you can change this again in N hours"; clear it to empty → allowed immediately; paste a URL into the short bio → renders as plain text with no link; paste an allowlisted URL into the extended bio → renders as a link.
**8.2 [AI] Theming.** `THEME_SET` as named CSS-variable sets; server picks the theme per surface (own view / profile owner's / viewer-override) per SPEC §9.1 v1.4 and ARCHITECTURE §3.5. **Includes the automated contrast test** (ARCHITECTURE §3.8, §9): every `THEME_SET` combination's text and UI-boundary token pairs are computed against WCAG 2.1 AA ratios (4.5:1 / 3:1) and a failing theme fails the build by name. A theme that cannot pass is not shipped — no exceptions for one that "looks nice."
**8.3 [AI] Preview-as.** Profile as any chosen friend or generic FoF sees it — same engine, substituted viewer, strictly read-only (§9.5).
**8.4 [AI] Display-name change.** The settings flow per SPEC §4.5.1: 90-day cooldown since creation/last change (honest "you can change again on [date]" message), blocklist screening, and the 90-day "formerly" dual display — which costs nothing here because every surface already renders names through the step-2.3 helper.
✅ *Milestone:* view a seeded profile as friend, as FoF (basic tier only), as stranger (nothing); set a profile theme in one account and see it from another; flip the viewer-override and see your own theme win; preview-as matches what the real second browser shows. Change a seeded user's name (test hook past the cooldown): "New (formerly Old)" appears on their old posts, comments, profile, and in a reaction list; a second change attempt is refused with the correct date.

---

## Phase 9 — Contact Cards [AI]

**9.1 [AI] Card + cascade.** ≤12 items (phone/email/messenger-link from allowlisted domains); default → group override → individual override, deny-beats-allow between groups (SPEC §10.2–10.3) — resolution lives in the engine and the tables were defined in Step 4.1 (already tested in 4.2; this step is UI only).
**9.2 [AI] Card requests.** Picker-based request; system auto-replies with exactly the permitted version (§10.4). (Request-more-access flags stay parked for v1.1, §10.5 — table may exist, no UI.)
**9.3 [AI] Preview-as for the card** (§9.5).
✅ *Milestone:* build a card with a phone number off-by-default, on for group "Close", off individually for Bob who is in "Close" — Bob's auto-reply lacks the number (individual wins); a friend in no group gets defaults only; preview-as agrees with reality.

---

## Phase 10 — Hashtags and Discovery [AI]

**10.1 [AI] Vocabulary + pickers.** `HASHTAG_VOCAB` operator-curated in Django admin; searchable picker (never free-typed — SPEC §11.2); ≤10 profile hashtags; post tagging.
**10.2 [AI] The FoF gate.** §11.3's three live-evaluated conditions (engine already tests this; wire it to real pages), including FoF commenting on gated posts.
**10.3 [AI] The discover page.** Pull-only: ranked people suggestions with auto-context, matched posts, and the clickable-hashtag tag filter (§11.4 v1.3). Nothing from here ever touches a feed.
**10.4 [AI] Friend-list visibility** per §11.5.
✅ *Phase milestone:* seed Alice–Mutual–Bob with #hiking on both Alice's and Bob's profiles; Bob sees Alice's #hiking-tagged profile post on discover and can comment; Bob removes his tag — access ends live; clicking #hiking anywhere lands on the filtered discover view; a blocked pair see nothing of each other in any of it.

---

## Phase 11 — Introductions [AI]

**11.1 [AI] Broker flow** (§5.5a): both must accept; declines silent in every direction; auto-context only.
**11.2 [AI] Requested flow** (§5.5b): pointable-Charlies rule; converts to flow (a) with requester pre-accepted.
✅ *Milestone (three browser windows):* run both flows end-to-end including a decline — verify the broker learns only "did not complete" and the other candidate learns nothing; a flow that would breach either 300-cap errors clearly.

---

## Phase 12 — Notifications and Email [AI]

**12.1 [AI] In-feed notifications** for the full SPEC §12.1 list, with read state. **Profile updates are per event type, not one generic "updated their profile"** — new blog post and profile-photo change notify; gallery additions notify, coalesced; bio, about, hashtag and theme changes are **silent**. Wording is specific per type and is real text, never an icon carrying the meaning.

**12.2 [AI] The two coalescing modes (SPEC §12.3).** These are genuinely different mechanisms and collapsing them into one will produce either a flooded feed or news that arrives too late:
- **Profile updates coalesce on a clock** — one row per (author, recipient, event type) per `PROFILE_NOTIFY_WINDOW_HOURS`, *updated in place*, carrying the most recent event's age. Two blog posts inside a window become "David posted twice to his blog", linking to the blog rather than either post.
- **Comment and reaction activity coalesces on unread state, with no clock at all** — one row per (post, recipient), updated until it is read.
Both are "find the open row and update it," never "insert another row."

**12.3 [AI] Following a post (SPEC §12.3).** A `post_follows` row per (post, follower); commenting turns it on, a visible per-post toggle turns it off, a global default lives in settings. Two rules the table cannot enforce by itself: **following is private** — nothing exposes followers to the post author and no count of them exists — and **the row is permission-to-be-notified, not permission-to-see**, so delivery re-asks the visibility engine every time rather than trusting the row.

**12.4 [AI] Rendering rules (SPEC §12.2).** **Never an excerpt of post or comment text** — actor + event type + relative age + link, nothing more; a body excerpt would turn a pull-model profile post into a push-model feed post with a 300-person audience. **Names, never numbers** ("Alice and Tom commented on your post", overflowing to "and others") — no unread badges, no counts anywhere. **Actors render live** through the Step 2.3 helpers, so deleted comments and removed reactions drop out instead of freezing into the feed. Plus the `expire_notifications` job (ARCHITECTURE §6), so notifications never outlive the content they point at.

**12.5 [AI] Optional email notifications** with per-category user settings; content-minimal (no post content beyond what the recipient may see); through Django's email abstraction. **Emails carry no timestamp at all** (SPEC §12.3) — a relative age computed at send time is false by the time the mail is read, and the mail client already stamps it.
✅ *Milestone:* each §12.1 event produces exactly its notification and (when enabled) email, and the silent ones produce **nothing** — change a bio and a theme in one account, confirm the other account's feed stays empty. Comment three times from three accounts on one post → the author has **one** notification naming them, not three. Delete one of those comments → that name disappears from the notification. Unfriend a follower → their notifications stop silently, and nothing anywhere tells the author they were following. Search the rendered feed for any digit that is a count of anything: there should be none.

---

## Phase 13 — Moderation and the Operator Console [AI]

**13.1 [AI] Reports.** Report action on every post/comment/profile → queue with frozen copy; content stays live; purge rules (dismiss→now, upheld→+30d, hard cap 90d) via the `purge_moderation` job (SPEC §13.2–13.3); content-free upheld counters (§13.4).
**13.2 [AI] Operator request form.** One form, category dropdown (hashtag / external service / bug / **accessibility problem** / feedback), rate-limited, into the same queue (§13.5). Accessibility reports sort ahead of feature requests in the queue (SPEC §16.5).
**13.3 [AI] Django admin as operator console.** Moderation queue with act-on actions (delete content / warn / ban), vocabulary editor, `NAME_BLOCKLIST` editor (SPEC §4.5), `REACTION_SET` and `THEME_SET` editors; admin at a non-default path (ARCHITECTURE §7). **URL-allowlist editor** (SPEC §7.2.3, ARCHITECTURE §4): each row carries host, **admitting category** (convening / hosts-what-we-cannot-host / messenger handoff), and **redirector-rejection patterns**; rows are **created inactive by default**, so activating one is the deliberate moment the operator confirms the service has no open redirector. Seed the known cases (`youtube.com/redirect`, `google.com/url`). Deactivating beats deleting — it keeps the record of why a domain was added.
**13.4 [AI] Rate limits.** Per-account daily counters in the database, §14's ✎ values, honest "slow down" messages (§13.6); plus the `reset_rate_counters` job. The stricter **login backoff** (per-account + per-source-address lockout) built in Step 2.5 is confirmed wired here as the security-specific case of the same framework (SPEC §4.6.1). **Confirm the three non-counter controls are wired and are *not* day tallies** (ARCHITECTURE §4): feed-post spacing (`POST_MIN_INTERVAL_MINUTES`, Step 6.2) and the two bio/photo cooldowns (`BIO_CHANGE_COOLDOWN_HOURS`, Step 8.1) are elapsed-time comparisons against stored timestamps — a daily counter cannot express "not again for 12 hours," and `reset_rate_counters` must not touch them.
✅ *Milestone:* report a seeded post; see the frozen copy in admin; dismiss → copy purged; uphold another → live content gone, counter incremented, copy purged after the (test-shortened) window; a script-speed action burst hits the limit politely.

---

## Phase 14 — Account Lifecycle and Data Export [AI]

**14.1 [AI] Deletion.** Request → immediate deactivation → 30-day grace with cancel-on-login → `process_deletions` full erasure + anonymized invite-tree stub (SPEC §4.7, §4.3); comments/reactions removed everywhere.
**14.2 [AI] Inactivity.** `inactivity_sweep`: 6/12/22/23-month warnings, 24-month deletion (§4.8).
**14.3 [AI] Login-email change** (verified-new-address flow, notice to old — §4.6).
**14.4 [AI] Data export.** One click → ZIP of JSON + images, everything §4.9 lists.
**14.5 [AI] Remaining cron wiring.** All ARCHITECTURE §6 jobs scheduled on the server; each also runnable by hand; idempotency tests.
✅ *Milestone:* delete a seeded account and fast-forward the grace (test hook) — data gone, stub present, their comments vanished from friends' posts; export your own test account and open the ZIP — it's complete and readable.

---

## Phase 15 — Legal and Public Documents [FOUNDER+AI]

**15.1 [FOUNDER+AI] Privacy policy + Terms of Service**, written plainly (SPEC §15.1): what's collected (nearly nothing), the 90-day expiry, the 30-day backup retention (ARCHITECTURE §10), the named email provider and VPS host as processors, GDPR rights (export §4.9, erasure §4.7), 18+ rule, invite-tree stub disclosure. AI drafts from SPEC; **you** read every sentence and own it. Linked from login and inside the app.
✅ *Done when:* you can honestly say every sentence is true of the system as built. (Attorney review is required before any *public* phase — SPEC §15.1; friends-only prototype proceeds without.)

**15.2 [FOUNDER+AI] Accessibility statement** (SPEC §16.5), published alongside the privacy policy and linked from login and settings: the conformance target (WCAG 2.1 Level AA), the date and method of the last audit (Step 16.5), **known limitations listed honestly** — including the preformatted-post horizontal-scroll exemption (SPEC §16.3) and anything Step 16.5 found and you have not yet fixed — and how to report a problem (the §13.5 form, plus an email address for someone who cannot use the form at all, which is the whole point).
**Sequencing:** draft it here with the rest of the public documents, but leave the conformance claim and the known-limitations list **blank until Step 16.5 fills them in** — the audit is what turns a draft into a claim.
✅ *Done when:* the statement is drafted, and (after Step 16.5) it claims **only** what the audit actually verified. A conformance claim you have not tested is the one accessibility lie that matters.

---

## Phase 16 — Hardening and the Pre-Flight Audit [AI + FOUNDER]

**16.1 [AI] Security settings pass.** The Django production checklist (`manage.py check --deploy` clean), cookie flags, header settings, upload size limits — ARCHITECTURE §7. **Confirm the auth-security layer (SPEC §4.6.1):** Argon2id is the active password hasher, reset/verification use codes with no login link anywhere, login backoff is enforced, and the breach-password check runs at registration and password change. **Confirm the link validator (SPEC §7.2.3):** the Step 6.2a attack cases still pass against the live allowlist, every composer routes through the one shared function, and no active allowlist row has an unchecked redirector. **Confirm the validator runs on the edit path too** (SPEC §7.8 invariant 4, Step 6.6): re-run the attack cases as *edits* to already-published clean content, not just as new posts. A create-only validator is the single most likely way this control gets defeated in practice, and it fails silently — nothing errors, the link simply goes live.
**16.2 [FOUNDER] The zero-foreign-requests check.** In Firefox or Chrome on the live site: open Developer Tools → Network tab, then browse every page type (feed, profile, discover, composer, settings, admin). **Every single request must go to your domain only.** One request to any foreign domain is a tracking-ban violation (SPEC §15.2) — file it as a bug.
**16.3 [FOUNDER] The stranger test.** Logged out (or as a stranger account): try saved URLs of a post, an image, a profile. All must show nothing (SPEC §9.3).
**16.4 [FOUNDER] Restore rehearsal #2** — this time from the automatic nightly backup, following the runbook.

**16.5 [AI + FOUNDER] The accessibility audit (SPEC §16.5).** The gate that turns "we built it accessibly" into a claim you can defend. Five passes over **every** page type — login, reset, invite redemption, feed, both composers, a profile (as friend, as FoF), discover, contact card, settings, every error and empty state:
1. **[AI] Automated scan.** Run an axe/`pa11y` scan over the running site (a local dev tool, not an app dependency — ARCHITECTURE §9) plus the template smoke tests (alt attributes, label associations, one `<h1>`, page titles, no positive `tabindex`). Fix everything it finds; it catches perhaps a third of real problems.
2. **[FOUNDER] Keyboard-only pass.** Unplug the mouse. Reach and operate everything with Tab / Shift-Tab / Enter / Space / arrows / Escape. Watch for: focus you cannot see, focus that jumps somewhere surprising, a control you can reach but not activate, and above all a **trap** you cannot Tab out of (the image overlay and the pickers are the likely offenders).
3. **[FOUNDER] Screen-reader pass.** VoiceOver on your Mac (⌘F5) and on your iPhone — both free, both already installed. Post something, read a profile, add a contact item, hit a validation error. You are listening for: unlabelled buttons ("button, button, button"), images announced as filenames, errors that never get announced, and the audience-picker count going silent.
4. **[FOUNDER] Zoom and reflow pass.** Browser zoom to 200% and a 320px-wide window: nothing clipped, nothing overlapping, no horizontal scrolling anywhere — **except** a preformatted post, which is the documented exemption (SPEC §16.3) and must still be scrollable by keyboard.
5. **[AI] Contrast gate.** The `THEME_SET` contrast test (Step 8.2) passes for every theme, including the viewer-override combinations.
Anything found and not fixed goes into the accessibility statement (Step 15.2) as a stated known limitation — never quietly.
✅ All five passes complete, findings either fixed or written into the statement.

✅ *Phase milestone:* all five checks pass on the production server.

---

## Phase 17 — Launch to Friends [FOUNDER]

**17.1 [FOUNDER] Reset to zero.** Wipe all seed/test data (AI provides the command), create your real account via a bootstrap invite.
**17.2 [FOUNDER] Invite your first circle.** Your invite budget is the throttle by design. Tell invitees plainly what this is (the SPEC §1 pitch, in your own words) and that it's a prototype.
**17.3 [FOUNDER] Operate.** A short recurring routine (weekly is plenty at first): moderation/request queue in admin, disk space, backup job's last-success, OS updates applied. The AI writes this one-page operator runbook as its final Phase-17 task.
**17.4 [FOUNDER] Feed reality back.** Friends' confusions and wishes go through the in-app request form (§13.5) — you'll be reading your own moderation queue as its first user. Feature ideas flow back into SPEC amendments first, never straight into code.

🏁 *The prototype is live. Everything after this is SPEC v1.16+.*

---

## Appendix — Cross-Phase Rules for the AI Coding Models

Deliverable (d) will restate these in every prompt's preamble; they live here as the master copy:

1. SPEC.md and ARCHITECTURE.md are law. On any conflict between a prompt and those documents, stop and say so.
2. All visibility decisions call the visibility engine — never inline (ARCHITECTURE §5). Any diff that inlines a permission rule is wrong even if its output is correct today.
3. Reference `constants.py` names, never bare numbers.
4. Tests are written alongside each feature, in the same step, densest where bugs equal privacy breaches (ARCHITECTURE §9).
5. No third-party requests from any page: no CDNs, no external fonts, no embeds, no analytics (SPEC §15.2).
6. No new dependencies beyond the ARCHITECTURE §3 stack without the founder's explicit approval in the chat. (The one pre-approved addition is `argon2-cffi`, for Argon2id password hashing — SPEC §4.6.1, ARCHITECTURE §7.)
7. Every scheduled job is idempotent and runnable by hand (ARCHITECTURE §6).
8. UUIDs for anything URL-visible; every request permission-checked (SPEC §9.3).
9. **Every user-facing surface meets WCAG 2.1 Level AA (SPEC §16)** — in the step that builds it, never "later." Compose the shared accessible partials from Step 2.5 (`_field`, `_errors`, `_modal`, `_expandable`, `_status`); never hand-roll a form control, dialog, or status message. Semantic HTML before ARIA; real `<button>`s and `<input>`s, never clickable `<div>`s; a visible focus indicator on everything; text errors tied to their field; images with stored alt text; nothing conveyed by color alone; no auto-updating or focus-stealing content. If a feature seems to need an inaccessible pattern, stop and say so — that is a design conversation (§0.2 rule 5), not a coding decision.
10. **Every content save re-runs every content check** (SPEC §7.8 invariant 4). Validation belongs to the shared model/form layer that both the create and the edit path call — never to a create view. A check that runs only on creation is a defective implementation, and with the URL allowlist that defect is a security hole rather than a bug: it fails silently, with nothing to notice.
11. **Four things are rendered by one shared helper each, never reimplemented** (ARCHITECTURE §4): display names, relative timestamps, image alt text, and theme selection. The time helper emits the phrase **only** — no `title` attribute, no `<time datetime="…">`, no data attribute carrying the true timestamp (SPEC §7.5.1). If a surface seems to need a date formatted some other way, stop and say so; that is a design conversation, not a coding decision.
12. **No counters.** No unread badge, no follower count, no reaction count, no post count, no view count — SPEC §17 has none anywhere, and §12.2's rule is names overflowing to "and others." If a feature seems to need a number that describes people or attention, it is the wrong feature.
