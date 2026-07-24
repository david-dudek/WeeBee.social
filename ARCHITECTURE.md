# Architecture & Technology Stack — "The Network"

**Status:** 1.5 — accessibility sync, DRAFT pending founder review · 2026-07-21 *(1.3 and earlier **approved as a whole by founder 2026-07-08**)*
*(1.1: synced to SPEC v1.4 — v1.3/v1.4 spec additions checked against this architecture; none require structural change. Explicit notes added for theming (§3.5, §4) and comment-name linking (§5). No section reviewed in Draft 1.0 changes meaning. 1.2: synced to SPEC v1.5 — display-name lifecycle (§4.5.1): name fields on users, blocklist table, single name-render helper; additive, no structural change. 1.3, founder-requested 2026-07-13: §13 expanded to record the full scaling path discussed in build-plan review — staged promotions, sharding locality, and the TLS-terminates-only-on-our-machines principle generalizing the Cloudflare-proxy ban; additive, changes nothing about v1. 1.4, synced to SPEC v1.8: authentication-security mechanisms recorded in §7 (codes-not-links reset via a hashed short-lived code table, a `credentials` table holding multiple credential types so passkeys drop in later, Argon2id hashing with its one added dependency, per-account/per-IP login backoff, server-to-server breach-password check, SPF/DKIM/DMARC `p=reject`); data-model additions in §4; DMARC note in §3.6; CAPTCHA row added to §14; additive, no change to any existing structure. 1.5, synced to SPEC v1.10 (accessibility): new §3.8 records how WCAG 2.1 AA is built in — shared accessible template partials as the single source of each pattern, base-template landmarks/skip link/focus styling, an automated `THEME_SET` contrast test, per-island ARIA requirements with no-JavaScript fallbacks, keyboard-scrollable preformatted blocks, and the permanent ban on accessibility overlays; Decision 1 gains reason 6 (server rendering is the accessible default); `images` gains `alt_text` and `is_decorative` (§4); §9 gains the accessibility test set and the human-audit note; §14 gains overlay and separate-site rejection rows; additive, no existing section changes meaning and no section is renumbered.)*
**Companion to:** SPEC.md v1.10 (deliverable b per SPEC §18)
**Audience:** The founder (an IT professional, not a professional developer) and the AI coding models that will build the platform. Written in plain language; every technology choice is justified. Where a term of art is unavoidable, it is explained the first time it appears.

---

## 1. The Shape of the System in One Paragraph

The platform is **one web application running on one rented server**, talking to **one database on that same server**, with images stored on that server's disk. Users reach it through their phone or computer browser over an encrypted connection. A small set of scheduled housekeeping jobs runs on the same machine (deleting expired posts, topping up invite budgets, sending inactivity warnings). The only outside service involved is an email-sending provider, because a home-grown server cannot reliably deliver email. That's the whole system. This shape is called a **monolith** — one program that does everything — and for this project it is not a compromise; it is the correct design, argued below.

```
  [ User's browser (phone or computer) ]
                  |
             HTTPS (encrypted)
                  |
  +--------------- one rented server (VPS) ---------------+
  |                                                        |
  |  Caddy (web server: HTTPS, passes requests inward)     |
  |       |                                                |
  |  Django application (all the logic and pages)          |
  |       |                    |                           |
  |  PostgreSQL (database)   image files (on disk)         |
  |                                                        |
  |  cron (the server's alarm clock) -> housekeeping jobs  |
  +--------------------------------------------------------+
                  |
        [ Email provider (outbound only) ]
```

---

## 2. The Five Decisions That Shape Everything

Before naming products, here are the architectural decisions, each with its reasoning. Every technology in §3 follows from these.

### Decision 1 — A server-rendered web app, not a JavaScript app

There are two mainstream ways to build a web app today:

- **Server-rendered:** the server builds each page as finished HTML and sends it to the browser. Every click that changes something is a normal page request. This is how the web worked when you studied CS, and it never stopped working.
- **Single-page application (SPA):** the browser downloads a large JavaScript program (usually React) which then builds the interface itself and talks to the server through a separate data API. Two codebases, two deployments, twice the surface for bugs.

**We choose server-rendered.** Reasons:

1. **It halves the system.** No separate frontend project, no API versioning, no duplicated permission logic ("does the API check what the interface checks?"). For a solo non-developer with AI assistance, every halving matters.
2. **Our pages are simple.** A feed, a profile, a composer, some pickers. Nothing here needs the interactivity budget of a Google Docs. The few genuinely dynamic pieces (audience picker, hashtag picker) need only a sprinkle of JavaScript, not a framework.
3. **It is inherently tracking-clean.** The SPA ecosystem is soaked in third-party scripts, CDNs, and analytics hooks; SPEC §15.2 bans all of that. A server-rendered app ships zero third-party JavaScript by default.
4. **AI coding models make fewer mistakes with it.** Less coordination between moving parts means less room for a sub-Fable model to wire something wrong. This matters given SPEC §2's requirement that all documents be executable by less capable models.
5. **Permission checks happen in exactly one place** — on the server, before HTML is built. There is no client-side copy of the rules to drift out of sync (see §5, the visibility engine).
6. **It is the accessible default.** Semantic HTML delivered whole, with no client-side routing to break focus management and no framework widget layer between the user and the DOM, is the cheapest path to SPEC §16's WCAG 2.1 AA requirement. The SPA alternative would mean re-implementing focus, announcements, and page titles by hand on every route change (see §3.8).

Mobile-friendliness comes from **responsive CSS** (page layouts that reflow for narrow screens), not from an app. That fully satisfies SPEC §2 "simple, mobile-friendly web application."

### Decision 2 — One server, one database, boring and rented

We rent a single **VPS** (virtual private server — a slice of a machine in a data center, ~$6–15/month) and run everything on it. No cloud "platform" services, no serverless functions, no managed databases, for four reasons:

1. **Cost:** fits the SPEC §15.3 founder-funded phase (~$15/month class).
2. **Privacy sovereignty:** the data never touches a third party's product designed to analyze it. A VPS is a landlord; a "backend-as-a-service" (Firebase, Supabase cloud) is a roommate. The tracking ban and the deletion guarantees are easiest to honor when we own every byte.
3. **Comprehensibility:** one machine you can log into and inspect is something an IT professional already knows how to reason about. Twelve cloud services with separate dashboards are not.
4. **The scaling story still works** (§13): this design grows to tens of thousands of users on bigger single machines before any re-architecture is needed — and the platform's own caps (300 friends, no virality) make load unusually predictable.

### Decision 3 — Every image and page served through the application, never directly

Normally websites serve images straight from disk or a CDN for speed. **We must not.** SPEC §9.3 requires that no image or post is reachable without login and permission. Therefore *every* request — pages *and* images — passes through the application, which checks "may this logged-in viewer see this?" before responding. A leaked URL then shows a stranger nothing, exactly as the spec demands. At our scale the performance cost is irrelevant.

Corollary: **no CDN, no cloud image bucket.** Images live on the server's disk, in a folder the web server cannot serve directly.

### Decision 4 — One central "visibility engine"

The spec's hardest feature is not any page — it's the permission web: friends vs. FoFs, hashtag gates, contact-card cascades, blocks that erase people mutually, audience snapshots plus current-friendship checks. If those rules are re-implemented ad hoc on every page, they *will* diverge and leak.

So the architecture mandates **one module of code that answers all visibility questions**, and everything else must ask it. Roughly five questions cover the platform:

- `can_see_post(viewer, post)` — implements SPEC §7.4 + §11.3
- `can_see_profile_tier(viewer, owner)` — returns nothing / basic / full (§9.2)
- `visible_contact_card(viewer, owner)` — the cascade with deny-beats-allow (§10.3)
- `are_connected(a, b)` — friend / FoF / stranger, with blocks short-circuiting everything (§5.4)
- `can_act(viewer, action, target)` — may comment, react, request, introduce?

Two big payoffs:

- **Preview-as (SPEC §9.5) becomes almost free:** rendering "my profile as Alice sees it" is just calling the same functions with Alice as the viewer. No second implementation to keep honest.
- **Blocks become reliable:** because *every* list, count, suggestion, and page flows through `are_connected`, the "fully mutually invisible" rule (§5.4) is enforced in one place instead of forty.

This module gets the densest automated tests in the project (§11).

### Decision 5 — Scheduled jobs by cron, not a job-queue system

The platform runs on the calendar: content expiry at 90 days, invite +1/month, inactivity warnings at 6/12/22/23 months, deletion after the 30-day grace, moderation-copy purges. Professional stacks often add a queue system (Celery + Redis) for such work. **We refuse that complexity.** Every one of these tasks is fine running once per hour or per day; none needs to fire the instant it is due. So each is a small named command, and **cron** — the standard Unix scheduler present on every server, literally an alarm clock for programs — runs them on schedule. Two moving parts fewer (no queue, no Redis), and each job can also be run by hand for testing.

---

## 3. The Recommended Stack, Piece by Piece

| Layer | Choice | One-line role |
|---|---|---|
| Language | **Python 3.12+** | The single language of the whole project |
| Web framework | **Django (current LTS)** | Pages, database access, login, admin — batteries included |
| Database | **PostgreSQL 16+** | Stores everything except image files |
| Web server / HTTPS | **Caddy** | Encryption certificates handled automatically |
| App runner | **Gunicorn** | The standard way a Django app runs in production |
| Packaging | **Docker Compose** | The whole system described in one file; identical on Mac and server |
| Images | **Pillow** (Python library) | Re-encode, resize, and strip EXIF/GPS on upload |
| Frontend | **Django templates + one hand-written CSS file + small vanilla JavaScript** | No framework |
| Email | **A transactional email provider** (e.g., Postmark, Mailgun, or Amazon SES) | Verification, resets, warnings |
| Scheduler | **cron** | Runs the housekeeping commands |
| Backups | **Nightly encrypted off-server backup** (pg_dump + images, via restic or equivalent) | Disaster recovery, with short retention (§10) |

### 3.1 Why Python and Django (the biggest choice)

**Django** is a 20-year-old, foundation-governed web framework whose motto is "batteries included." The justification stands on five legs:

1. **It ships most of our platform as built-in parts.** Login/logout/password reset with correct security (SPEC §4.6) — built in. Database schema management ("migrations") — built in. Protection against the classic web attacks (CSRF, SQL injection, XSS) — built in and on by default. Page templating — built in.
2. **The Django admin is the operator console for free.** Django auto-generates a private, login-protected administration interface over the database. That is, nearly verbatim, SPEC §13's operator needs: the moderation queue, the request/suggestion queue (§13.5), the hashtag vocabulary editor (§11.2), the URL allowlist editor (§7.2), ban/warn actions. Building an operator backend by hand would otherwise be weeks of work; here it's configuration.
3. **It is the safest stack for AI-built software.** Django is among the best-represented frameworks in every coding model's training data, its conventions are strong (there is one obvious place for everything), and its defaults are secure. Sub-Fable models will make fewer and less dangerous mistakes in Django than in a stack that requires assembling ten libraries by hand (the Node.js failure mode).
4. **One language everywhere.** Pages, visibility engine, housekeeping jobs, image pipeline, data export — all Python. Nothing to context-switch.
5. **Python is the least-bad language for a lapsed programmer.** Of everything mainstream, it reads closest to pseudocode; a 1995 CS degree plus IT experience is enough to *read* it, which is what reviewing AI-written code requires.

*Considered and rejected:* **Node.js/Express** (assemble-it-yourself; more decisions, more drift, JavaScript's quirks); **Next.js/React** (SPA complexity per Decision 1); **Ruby on Rails** (equally good philosophically, slightly weaker AI training coverage and no admin as strong as Django's, and Ruby is a less useful second skill than Python); **PHP/Laravel** (fine, but no advantage over Django and weaker fit with the founder's background).

### 3.2 Why PostgreSQL, and from day one

PostgreSQL is the default serious open-source database — 30 years old, strict about data integrity, free. The tempting simpler alternative is **SQLite** (the database-in-a-single-file). We choose Postgres *now* anyway because:

- SPEC §2 says architecture must survive "public later." Postgres is that answer; switching databases mid-life is a well-known source of subtle breakage (the two dialects differ in details AI models trip over).
- Docker Compose (§3.4) makes running Postgres a two-line addition — the usual setup pain doesn't apply.
- Everything about our data is relational: friendships, group memberships, audience snapshots, visibility overrides. A relational database with real foreign-key enforcement catches whole categories of AI coding errors at the data layer.

*Rejected:* SQLite (above); MongoDB and other "NoSQL" stores (our data is the textbook case *for* relations, and enforced structure is a safety net we want); any managed cloud database (Decision 2).

### 3.3 Why Caddy for the front door

Every website needs a web server handling HTTPS (the encryption). The traditional choice, Nginx, requires configuring certificate renewal (Let's Encrypt, cron jobs, reload hooks). **Caddy** does all certificate work automatically — its config for us is ~5 lines. For a solo operator, "HTTPS that cannot be misconfigured or silently expire" is worth more than Nginx's extra tunability, none of which we need. Caddy passes requests to Gunicorn/Django; per Decision 3 it serves **nothing** from disk itself except the CSS file and our own JavaScript.

### 3.4 Why Docker Compose

Docker packages a program with everything it needs into a **container** (a standardized box); Docker Compose describes a small fleet of them — for us: `app`, `db`, `caddy` — in one short file. Justification:

- **The system on your Mac and the system on the server are identical.** "Works on my machine" ceases to be a failure mode.
- **Setup is reproducible.** If the VPS dies, a new one is: install Docker, copy the project, restore backup, `docker compose up`. That is the entire disaster-recovery runbook for the app itself.
- **It's the standard.** Every AI model and every tutorial speaks it; an IT professional's existing intuitions (services, ports, volumes) map straight onto it.

*Rejected:* Kubernetes and friends (industrial machinery for fleets of servers; absurd here); installing everything directly on the VPS (workable, but snowflake servers rot, and reproducibility is our insurance policy).

### 3.5 Frontend: templates, one CSS file, drops of JavaScript

- **Django templates** generate every page server-side.
- **One hand-written CSS file**, mobile-first responsive layout. The theming feature (SPEC §9.1 v1.4 — curated fonts and color schemes, attaching to *spaces*, never content) is a natural fit: each theme in `THEME_SET` is a small named set of CSS variables, and **the server decides once per page which theme's variables to emit** — the viewer's own theme for feed and app surfaces, the profile owner's theme on profile pages, or the viewer's theme everywhere when their "always use my own theme" override is on. Because pages are server-rendered, comments and feed posts *cannot* carry their author's theme even by accident: content is plain HTML dropped into whatever surface renders it. No CSS framework needed; if the builder wants a head start, a classless sheet like Pico.css (a single file, self-hosted, no JavaScript) is acceptable — but **nothing loaded from a CDN, ever** (SPEC §15.2: third-party scripts are banned; even a stylesheet fetch leaks every visitor's IP address to the CDN company).
- **Vanilla JavaScript, hand-written, self-hosted** for the handful of dynamic pieces: the audience picker with its live ≤30 count (§7.3), the searchable hashtag picker (§11.2), the contact-card visibility toggles (§10.3), image upload preview, "save this selection as a group?" (§6). Each is an island of a few dozen lines on an otherwise static page. If these grow tiresome, **htmx** (one small self-hosted file that lets HTML fetch HTML) is the approved escalation — never React/Vue (Decision 1).

### 3.6 Email: the one outside service, and why it's unavoidable

The platform must send email: verification links, password resets, invites, optional notifications, and the legally-serious inactivity warnings (§4.8) and deletion notices. Sending email directly from a VPS **does not work in practice** — the big mailbox providers distrust small servers, and messages silently vanish into spam. Everyone, including one-person projects, uses a **transactional email provider**: a service with an API and a reputation that gets mail delivered.

- **Requirements:** API access, low/free tier at our volume (hundreds of emails/month), sane privacy posture (the provider sees addresses and email contents — choose one that is a mail courier, not a marketing-analytics company; this goes in the privacy policy).
- **Candidates:** Postmark (transactional-only by design, excellent reputation), Mailgun, Amazon SES (cheapest, clunkier). The build plan will pick one and include exact setup steps; the code depends on it only through Django's email abstraction, so the provider is swappable in one settings line.
- **Domain authentication (SPEC §4.6.1):** the sending domain must publish **SPF, DKIM (from the provider), and DMARC at `p=reject`** — the anti-spoofing baseline that stops forged mail *from our own domain*. Configured as DNS records at build-plan Step 5.5.
- This is a **founder-performed setup step** (account signup, domain verification) — it will be marked as such in deliverable (c).

### 3.7 The image pipeline (SPEC §7.2, §9.3, §9.4)

Upload → size/type sanity check → **Pillow decodes and fully re-encodes** the image (this *guarantees* EXIF/GPS removal, because a re-encoded image simply has no original metadata — stronger than trying to strip fields) → resized to sane bounded dimensions → saved to disk under a **random unguessable filename** in a non-web-served folder → recorded in the database with its owner and purpose (post image / profile photo / gallery). Serving: a Django view checks the visibility engine, then streams the file. Deleting a post/account deletes its files (and the expiry job verifies orphans).

### 3.8 Accessibility: how WCAG 2.1 AA is actually built in (SPEC §16)

SPEC §16 makes Level AA conformance a requirement of the same rank as the tracking ban. Architecturally it is cheap here, because the stack chosen in §2 is the accessible one by default: server-rendered semantic HTML, no SPA route-change focus problems, no third-party widgets, no autoplaying media, no infinite scroll, no algorithmic reordering under the reader. The work is therefore mostly *discipline*, and it is organized on the same "one place only" principle as the visibility engine (§5):

- **Shared template partials are the accessibility unit.** Form fields, error summaries, modal dialogs, expandable regions, and live-region status messages each exist as **one** partial (`_field.html`, `_errors.html`, `_modal.html`, `_expandable.html`, `_status.html`) that already carries the correct label association, `aria-describedby` error wiring, focus trapping, `aria-expanded`, and `aria-live` politeness. Pages compose those partials; **no page hand-rolls a form control, dialog, or status message.** The rule mirrors §5: correct output today is not a defense for reinventing the pattern.
- **The base template** owns the landmarks, the skip link, `lang`, the per-page `<title>`, and the focus-visible styling that no theme may remove.
- **The CSS file** owns the theme variables (§3.5). Contrast is not a matter of taste here: each theme's token pairs are **verified by an automated test** (§9) that computes WCAG relative-luminance contrast ratios in plain Python — no dependency, no browser needed — and fails the build if any pair used for text or a UI boundary falls below 4.5:1 / 3:1. A theme is data; the test is the gate that lets it into `THEME_SET`.
- **The JavaScript islands** (§3.5) are the only places where accessibility can be got wrong in a way HTML wouldn't catch: the audience picker (live count → polite live region; the count is also rendered server-side so it is never JS-only), the hashtag picker (the WAI-ARIA combobox pattern, arrow keys and Escape included), the contact-card toggles (real `<input type="checkbox">` elements, styled — never `<div>`s with click handlers), the "read more" fold (a real `<button>` with `aria-expanded`, expanding in place without moving focus), and the image overlay (a real modal: focus in, trapped, Escape out, focus restored). **Every island must degrade to something usable without JavaScript**, which server-rendering makes natural: the fold is display-only (§7.7 SPEC), pickers fall back to plain multi-select forms.
- **Images carry alt text as data, not markup** (§4, `images.alt_text` + `is_decorative`), so every surface that renders an image renders its description automatically — the same discipline as the single name-render helper (§4).
- **Preformatted posts** (SPEC §7.2.1) get `tabindex="0"`, an accessible name, and a visible focus ring on their scroll container, because a horizontally scrollable region that only a mouse can pan fails 2.1.1. This is the one place the architecture knowingly accepts two-dimensional scrolling, under SPEC §16.3's documented exemption.
- **Banned outright:** accessibility overlay widgets of any kind (SPEC §16.4) — they are third-party JavaScript and would violate §15.2 twice over. There is no configuration in which one is acceptable.

---

## 4. How the Data Is Organized

Plain-language inventory of the ~20 database tables. (Exact fields are deliverable-(c)/(d) material; this is the map.) Anything whose identifier ever appears in a URL gets a **random unguessable ID** (UUID), per SPEC §9.3 — no guessable numbering anywhere a browser can see.

**People and connections**
- **users** — primary key: a permanent internal **UUID** (all other tables reference users only by this ID; it never changes and is never reused). Attributes: login email (exactly one, unique among active accounts, changeable via verified-new-address flow — SPEC §4.6; a credential, not an identifier), login credentials held in a separate **credentials** table (below) rather than a password column, display name **plus previous display name and name-changed date** (drives the 90-day "formerly" dual display and the 90-day change cooldown, SPEC §4.5.1 — one previous name suffices because the cooldown ≥ display-window invariant forbids overlapping transitions), joined date, last-login date (for §4.8), deactivation/deletion-grace state. Contact-card emails are unrelated records in **contact_items**. **Name rendering rule (SPEC §4.5.1):** names are never snapshotted onto content; every surface renders names through **one shared helper** that appends the "formerly" tag during a transition — the same one-place-only discipline as the visibility engine (§5).
- **name_blocklist** — operator-curated blocked name strings (SPEC §4.5), checked at every name set (registration and change), edited in Django admin.

**Authentication (SPEC §4.6.1)**
- **credentials** — one row per credential per user: `type` (password | passkey), the type-specific material (an Argon2id hash for password; the public-key/credential-id fields for a future passkey), created/last-used dates. v1 writes only password rows; the table exists now so passkeys need no user-model change later.
- **credential_codes** — the short-lived numeric codes for password reset, email change, and registration email-verification: purpose, target user (or pending email), **hashed** code, expiry (`RESET_CODE_TTL_MINUTES`), single-use flag, attempt count. Never a signed URL — codes only.
- **login_attempts** — failure counters keyed by account and by source address, driving the exponential backoff / lockout (`LOGIN_ATTEMPT_LIMIT`, `LOGIN_LOCKOUT_MINUTES`); a security-specific sibling of `rate_counters`, swept on the same schedule.
- **friendships** — one row per accepted pair. The 300 cap is enforced here.
- **friend_requests** — pending/declined with timestamps (drives the 90-day cooldown, §5.2).
- **blocks** — one row per blocker→blocked; the visibility engine checks it before everything.
- **groups** / **group_members** — private per owner; ≤30 members (§6).

**Invitations**
- **invites** — code, sender, expiry, redeemed-by.
- **invite_tree** — permanent parent→child records; on account deletion the child's node is replaced by an anonymized stub (§4.3, §4.7).
- Invite budgets live on **users** (count + last-replenish date).

**Content**
- **posts** — type (feed/profile), text, optional image reference, created date (drives 90-day expiry), pinned flag (profile posts only, ≤10).
- **post_audience** — the posting-time snapshot: one row per (feed post, recipient). §7.4's rule = "row exists here AND friendship currently exists."
- **comments** — flat, on posts; own 90-day clock.
- **reactions** — (user, target, phrase from `REACTION_SET`); one per user per target.
- **hashtag_vocab** — the operator-curated vocabulary (§11.2), edited in Django admin.
- **profile_hashtags** / **post_hashtags** — join tables to the vocabulary.
- **images** — file path, owner, kind, upload date, **`alt_text`** (uploader-authored description, ≤ `ALT_TEXT_MAX`) and **`is_decorative`** (the explicit "no description needed" choice). One of the two is always set — the composer requires a deliberate choice (SPEC §16.3) — and every rendering surface reads them from here, so no template invents alt text of its own.
- **profiles** — bio fields, gallery membership, **profile-page theme choice** (what visitors see, §9.1), plus the owner's **own-app-view theme** and the **"always use my own theme" viewer override flag** (SPEC §9.1 v1.4) — three small settings fields (or folded into users; builder's call).

**Contact cards (§10)**
- **contact_items** — up to 12 per user: kind (phone/email/messenger-link), value, default on/off.
- **contact_overrides** — per item: group-level and individual-level on/off rows. The visibility engine resolves the cascade (individual beats group; among groups, deny beats allow).
- **card_requests** — who asked whom, when, what was auto-answered.
- **access_flags** — the request-more-access flags (§10.5; may ship v1.1 — table costs nothing to design now).

**Flows and operations**
- **introductions** — broker, the two candidates, per-side accept/decline state (§5.5).
- **notifications** — the in-feed system items (§7.7, §12), each with read state.
- **reports** — reporter, target, category, **frozen copy**, status, purge-by date (§13.2–13.3); handled in Django admin.
- **operator_requests** — the §13.5 form submissions (category, text, submitter).
- **upheld_report_counters** — the content-free per-account counts that outlive everything else (§13.4).
- **rate_counters** — per user/action/day counts for §13.6 (in the database, not Redis — Decision 5's simplicity again).
- **url_allowlist** — operator-curated domains (§7.2), edited in admin.

**Configuration constants (SPEC §14)** live in **one Python file, `constants.py`**, each named exactly as in the spec (`FRIEND_CAP = 300`, …) with a comment citing its SPEC section and the raise-only rule. Code must reference the constant, never a bare number.

---

## 5. The Visibility Engine (the heart)

Restating Decision 4 as an implementation rule, because it is the single most important sentence in this document for the AI builders:

> **No template, page, list, count, notification, export, or job may decide for itself who can see something. All such decisions call the visibility module. Any code change that inlines a visibility rule elsewhere is wrong, even if it produces correct output today.**

The module implements, from SPEC: §5.4 blocks (checked first, always, both directions), §7.4 audience snapshot + current friendship, §9.2 profile tiers, §10.3 the contact cascade with deny-beats-allow, §11.3 the three-condition hashtag gate evaluated live, §11.5 friend-list filtering. "Preview-as" (§9.5) is the same code with a substituted viewer — plus one guard: preview mode must be strictly read-only.

Two smaller v1.3 features illustrate the rule in action: **comment-name linking** (§8.1 — link the commenter's name only if the viewer has basic-tier access) is just the template asking `can_see_profile_tier(viewer, commenter)`; the **discover-page tag filter** (§11.4) is just the discover queries re-run with a tag condition added — the same `can_see_post` / `are_connected` calls decide every item shown. Neither feature gets its own permission logic.

---

## 6. The Housekeeping Jobs (cron)

Each is a Django management command — runnable by hand, scheduled by cron. All must be **idempotent** (safe to run twice; a re-run finds nothing left to do), because cron sometimes double-fires or gets run manually during testing.

| Job | Schedule | Does (SPEC ref) |
|---|---|---|
| `expire_content` | hourly | Delete posts/comments > 90 days (unpinned), their images, reactions (§7.5) |
| `purge_moderation` | daily | Purge frozen copies past their date; hard cap 90 days (§13.3) |
| `replenish_invites` | daily | +1 invite to anyone a month past last replenish, cap 5 (§4.2); expire 14-day-old invites back to budget (§4.1) |
| `process_deletions` | daily | Erase accounts past 30-day grace; write anonymized invite-tree stubs (§4.7, §4.3) |
| `inactivity_sweep` | daily | Send 6/12/22/23-month warnings; delete at 24 months (§4.8) |
| `reset_rate_counters` | daily | Clear yesterday's rate-limit counts (§13.6) |
| `backup` | nightly | §10 below |

---

## 7. Security Posture (what protects what)

- **Transport:** HTTPS everywhere via Caddy; HTTP redirects to HTTPS; modern TLS only.
- **Sessions, not tokens:** Django's cookie-based login sessions (httponly, secure, sensible expiry). Logged-out users can reach exactly three pages: login, password reset, invite redemption (SPEC §2).
- **Authentication and anti-phishing (SPEC §4.6.1):**
  - *Codes, not links.* Password reset, login-email change, and registration email-verification use a short-lived numeric code (`RESET_CODE_TTL_MINUTES`, `RESET_CODE_LENGTH`), stored **hashed** in a small `credential_codes` table with a single-use flag and an attempt cap, entered on a page the user navigated to themselves — never delivered as a login link. Only invites are links (a new user has no open page). This is deliberately *not* a signed-URL/token scheme, because the whole point is that no clickable login link ever exists to imitate.
  - *Multiple credential types from day one.* Login credentials live in their own `credentials` table keyed to the user (`type` = password | passkey, plus type-specific material), so a WebAuthn/passkey credential can be added later without touching the user model. v1 creates only password rows; passkeys are deferred (SPEC §4.6.1). The password's slow hash (below) is stored here.
  - *Breach-password check.* At registration and password change, the backend makes a **server-to-server** k-anonymity range request to the Have I Been Pwned Pwned-Passwords API (send the first 5 hex characters of the password's SHA-1; match the returned suffix list locally). Only a hash prefix ever leaves the server — never the password, never any user identifier — and it is a backend HTTPS call, not a browser script, so it is §15.2-clean. Fail-open on API outage (a third party being down must never block a signup), logged.
- **The standard attacks** (CSRF, SQL injection, XSS) are covered by Django defaults; the build plan will state the few settings to verify rather than trust. **Password hashing uses Argon2id** (SPEC §4.6.1) rather than Django's PBKDF2 default — Django supports it as a first-class hasher; this pulls in one dependency (`argon2-cffi`, via `django[argon2]`), the **only** addition to the §3 stack for the security layer, flagged for founder approval per the build-plan dependency rule (Appendix rule 6).
- **No third-party anything in pages:** no CDN assets, no fonts from Google, no analytics, no embeds (SPEC §7.2, §15.2). A build-plan checklist item: load any page and confirm the browser makes **zero** requests to foreign domains.
- **Rate limits** (§13.6) enforced in the database per user/action/day. **Login attempts** get a stricter, security-specific control (SPEC §4.6.1): per-account *and* per-source-address failure counters in the database with exponential backoff and temporary lockout (`LOGIN_ATTEMPT_LIMIT`, `LOGIN_LOCKOUT_MINUTES`), complemented by OS-level fail2ban on the SSH surface. No CAPTCHA (rejected — SPEC §4.6.1, §14 below).
- **Email domain authentication:** the sending domain publishes **SPF, DKIM, and DMARC at `p=reject`** (SPEC §4.6.1) — stops spoofing of our real domain; a founder-performed DNS step at build-plan Step 5.5.
- **Unguessable IDs** in all URLs (§9.3); every request permission-checked (Decision 3).
- **Server hygiene** (founder-performed, detailed in build plan): SSH keys only, firewall allowing only 80/443/SSH, automatic OS security updates, Django admin reachable at a non-default path.
- **Logs:** operational/error logs only, IP-lean, short retention — aligned with §15.2's "minimal and short-lived."

---

## 8. Development → Production Flow

1. **Develop on the Mac.** The identical Docker Compose stack runs locally; a seeded set of fake users/posts makes every feature testable without real people.
2. **Version control with git** from day one (the coding models' work is reviewable and reversible). A private GitHub repository is acceptable as offsite code backup — *code* only; no data, no secrets ever committed. Secrets (database password, email API key) live in an environment file on the server, outside git.
3. **Deploy** = copy the new code to the VPS and restart the containers (a three-line script; later, if wanted, a git-pull-based one). No app stores, no build farms.
4. **Migrations** (database shape changes) are generated and applied by Django's built-in system — this is what makes "add a feature next month" safe.

---

## 9. Testing (right-sized, not skipped)

Full test-pyramid ceremony would drown a solo project, but SPEC's promises are exactly the kind that silent bugs break. The rule: **test depth proportional to harm.**

- **Dense automated tests on the visibility engine** — blocks, tier boundaries, cascade conflicts, hashtag-gate edge cases, snapshot-plus-current-friendship. This is where a bug = a privacy breach.
- **Automated tests on the lifecycle jobs** — expiry, deletion-with-stub, invite replenishment. A bug here breaks a promise made to users (§7.5's "nothing outlives 3 months").
- **Ordinary features** (rendering, forms): light tests plus human use. The prototype's friendly first users are the beta test.
- **Accessibility (SPEC §16)** gets two automated tests plus a human pass, because two thirds of it *is* machine-checkable and the rest genuinely isn't:
  - a **contrast test** over every `THEME_SET` combination (§3.8) — pure Python, no dependency, fails by theme name;
  - **template smoke tests** asserting the mechanical invariants on rendered HTML: every `<img>` has an `alt` attribute (possibly empty with `is_decorative`), every input has an associated label, every page has one `<h1>` and a `<title>`, no `tabindex` above 0, no `<div>` carrying a click handler where a `<button>` belongs.
  - The **human pass** — keyboard-only, VoiceOver, 200% zoom, 320px reflow — is a build-plan gate (Step 16.5), not a unit test. No automated tool catches "the focus order is bewildering"; roughly a third of WCAG failures are only findable this way.
- Optional developer tooling (an **axe** browser extension, or `pa11y`/`axe-core` run locally) is useful for the audit and is **not** an application dependency — nothing accessibility-related ships to the browser beyond our own HTML and CSS. Any use of it as a *project* dependency needs founder approval under the build-plan dependency rule.
- Deliverable (d) will instruct the coding models to write these tests *alongside* each feature, not afterward.

---

## 10. Backups — and an Honest Tension with the Deletion Promise

Nightly: database dump + image folder, **encrypted, sent off the server** (e.g., restic to a storage box or B2 bucket; exact target chosen in the build plan). Restore is rehearsed once during setup, because an untested backup is a rumor.

**The tension:** backups are copies, so a post deleted today still exists inside last week's backup. Refusing backups would honor deletion purism but risks total loss of everyone's data. The industry-standard, GDPR-accepted resolution, which this architecture adopts:

> Backups are kept **`BACKUP_RETENTION_DAYS` = 30 days**, then destroyed. Deleted content therefore fully ceases to exist within at most 30 days of its deletion (and backups are encrypted, offline-ish, and never queried). The privacy policy states this plainly.

This slightly amends the mental model of §7.5 ("deleted at 90 days" → "deleted from the live system at 90 days, gone from the last backup by day 120") — flagged here for explicit founder approval since SPEC is authoritative.

---

## 11. What This Costs (founder-funded phase, monthly)

| Item | Est. cost |
|---|---|
| VPS (e.g., Hetzner ~€6–12, DigitalOcean $8–14 class) | $7–15 |
| Backup storage (Hetzner Storage Box / Backblaze B2) | $1–4 |
| Domain name | ~$1–2 (billed yearly) |
| Email provider | $0–15 (free tiers cover prototype volume) |
| **Total** | **≈ $10–35/month**, low end realistic for the prototype |

All within SPEC §15.3's phase-1 posture. Software costs $0 — everything in the stack is free and open source.

---

## 12. What the Founder Will Do Himself (preview of deliverable c)

Steps that happen outside an AI chat, to be spelled out with exact instructions in the build plan: choose and register a domain · create VPS and backup-storage accounts · sign up with the email provider and verify the domain · run the documented server-setup commands · perform deploys · rehearse a backup restore · act as operator in the Django admin (moderation, hashtag vocabulary, URL allowlist, reaction set). Everything else — all code — is written by AI models following deliverable (d).

---

## 13. How This Survives "Public Later" (SPEC §2)

*(Expanded 2026-07-13 at the founder's request, recording the full scaling discussion from the build-plan review.)*

Nothing here needs discarding as the platform grows — it needs *promoting*. The migration is a series of promotions, not a rewrite.

### 13.1 Why this design scales unusually far in the first place

Big social networks are expensive to scale because of the very things SPEC bans. One viral post read by millions, global search, trending feeds, infinite archives — those force exotic architecture. This platform has none of them. Every user generates **bounded load**: at most 300 friends, pushes to at most 30 people, content deleted at 90 days (the database never grows old and fat), and *no query ever spans the whole network* — everything is one hop from one person. A million users here is closer to "a million small mailboxes" than "one giant town square," and mailboxes scale easily.

### 13.2 The stages (each buys roughly 10× more users)

1. **Stage 1 — a bigger single server (tens of thousands of users).** Rent a beefier VPS (e.g., 32 cores / 256 GB RAM, ~$200/month class), restore backup, repoint DNS. An afternoon.
2. **Stage 2 — split the tiers (hundreds of thousands).** PostgreSQL moves to its own machine; images to their own storage volume; several copies of the Django app run behind a **load balancer**. The most well-trodden path in web architecture; the code barely changes because it never assumed same-machine anything except through configuration. Add the deliberately-skipped cache (Redis) and job queue (Celery) when measurements — not fashion — say so.
3. **Stage 3 — millions.** Two changes:
   - **Database goes from one machine to several.** First, **read replicas** (copies handling all reads while the primary handles writes) — native to Postgres and proven at extreme scale (Instagram ran on Postgres well past a hundred million users). If that saturates, **shard** (split users across multiple databases). Sharding is where most social networks suffer, because viral posts and global search cross every shard — but the one-hop-only, capped-friends design keeps almost every query local to a user and their ≤300 friends. This design shards about as gracefully as a social network can.
   - **Run your own front door.** Multiple app servers, self-operated load balancers, serious DDoS posture (§13.3). At this stage there is no solo founder: millions of users means staff, a real entity, lawyers, and above all paid moderators.

**What is never done, at any stage:** rewrite into microservices (a team-size decision, not a technical one, if ever), multi-region active-active, AT Protocol. The monolith-on-Postgres shape is exactly what successful mid-size networks scaled.

### 13.3 The privacy rules at scale (the part most sites get wrong)

The two banned tools — CDNs and decrypting proxies (e.g., Cloudflare's orange-cloud mode) — are precisely what most sites reach for at scale. The bans survive, as one durable principle:

> **TLS may terminate only on machines this project administers.** Hardware may be rented anywhere; decrypted user traffic is never handed to a third-party *service*. At scale, you build your own front door instead of renting one. Never rent a middleman that reads the traffic; at scale, become your own middleman.

- **Global latency:** the standard fix (CDN caching near users) would be nearly useless here anyway — all content is private and per-viewer, so almost nothing is cacheable. What actually helps: regional read replicas and, eventually, self-administered points of presence. Honestly noted: a single-region site serves the world at ~150 ms for far-away users, and major services ran that way for years.
- **DDoS:** at millions of users the platform *is* a real target — this is proxy mode's strongest sales pitch. DDoS defense comes in two layers: **network-level scrubbing** (filtering junk traffic without decrypting anything — Hetzner-class providers include it, and dedicated scrubbing services operate this way), which handles the overwhelming majority of attacks and is fully compatible with this architecture; and **application-level filtering**, which requires decryption and is what orange-cloud is. Only the second is given up — knowingly, with staff, at scale; never by accident in year one.

### 13.4 The real bottleneck

The true bottleneck at scale, per prior analysis, is **human moderation time, not hardware** — and no architecture buys that.

---

## 14. Alternatives Considered — Summary Table

| Alternative | Verdict | Core reason |
|---|---|---|
| React/Next.js SPA | Rejected | Doubles system complexity; tracking-prone ecosystem; worse for AI builders (Decision 1) |
| Node.js backend | Rejected | Assembly-required culture vs. Django's batteries + free admin |
| Ruby on Rails | Close second | Philosophically ideal, but weaker admin, thinner AI training coverage than Django |
| SQLite | Rejected for v1 | Would work for prototype but violates "no re-architecture later"; Postgres is cheap to run now |
| Firebase / Supabase cloud | Rejected | Third-party custody of user data; conflicts with tracking ban & deletion guarantees |
| Serverless (Lambda etc.) | Rejected | Wrong cost/complexity shape for a stateful, tiny, always-on app |
| Celery/Redis job queue | Rejected | cron suffices; two fewer services to operate (Decision 5) |
| Kubernetes | Rejected | Fleet machinery for a one-server system |
| Self-hosted email sending | Rejected | Deliverability is a losing battle; transactional provider is the norm (§3.6) |
| CDN for images/assets | Rejected | Violates permission-checked serving (Decision 3) and leaks visitor IPs |
| CAPTCHA / reCAPTCHA / hCaptcha / Turnstile | Rejected | Doesn't touch phishing; third-party script + behavioral scoring violates the tracking ban (SPEC §15.2); no public-signup or scraping problem exists here. Login-endpoint threats handled by throttling + Argon2id + breach-check instead. Self-hosted proof-of-work (Altcha/mCaptcha) is the only acceptable fallback if ever needed (SPEC §4.6.1) |
| Accessibility overlay widget (AccessiBe/UserWay/EqualWeb class) | Rejected, permanently | Third-party JavaScript that profiles visitors — violates the tracking ban (SPEC §15.2) — and does not fix the underlying HTML it papers over; rejected by disabled users' own organizations. Conformance is built into the markup instead (SPEC §16.4, §3.8 above) |
| Separate "accessible version" of the site | Rejected | Two codebases, one of which rots; the main site is the accessible one (SPEC §16.4) |
| TOTP-only 2FA as the phishing fix | Rejected | A real-time proxy relays a 6-digit code as easily as a password; origin-bound passkeys are the structural answer (SPEC §4.6.1) — the credential schema is built to accept them |

---

## 15. Open Points — Resolution Record

1. **Backup-retention amendment** (§10): deleted content persists in encrypted backups up to 30 days. — **APPROVED by founder 2026-07-07.**
2. **Email provider** (§3.6): founder deferred the final pick to the build plan (deliverable c), 2026-07-08. Postmark remains the recommendation.
3. **VPS provider and location** (§11): founder deferred the final pick to the build plan (deliverable c), 2026-07-08. Hetzner remains the recommendation; location depends on where the first users are.
4. **The document as a whole: APPROVED by founder 2026-07-08.**

---

*Next document: deliverable (c) — BUILD_PLAN.md, the step-by-step build plan, with founder-performed steps explicitly marked.*
