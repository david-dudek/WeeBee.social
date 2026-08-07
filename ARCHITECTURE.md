# Architecture & Technology Stack — WeeBee

**Project version:** 1.19 · 2026-08-06 · DRAFT pending founder review
**This file last changed in:** 1.19 (the visibility engine's performance rules: request-scoped memoization, the plural forms, and the caching that stays banned)
**History:** see [CHANGELOG.md](CHANGELOG.md)
**Companion to:** SPEC.md v1.15 (deliverable b per SPEC §18)
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

**And one cost, which must be designed for rather than discovered (v1.19).** One engine means every item on every page asks the same engine, and a page rendering sixty posts will ask it several hundred times — mostly the same few questions about the same few people. Left unanswered that becomes a slow feed, and a slow feed gets repaired by inlining a query into a template or a view, which is this decision failing in the field rather than losing an argument. **So the engine is responsible for its own performance:** it remembers within a single request what it has already worked out, and it answers in the plural as well as the singular so that a list costs a bounded number of queries rather than one per item. Both are internal to the module — no caller knows either exists, which is the only form in which they are compatible with the rule above. §5 states them, and §5.5 states the caching that stays forbidden.

This module gets the densest automated tests in the project (§9).

### Decision 5 — Scheduled jobs by cron, not a job-queue system

The platform runs on the calendar: content expiry at 90 days, invite +1 every 30 days, inactivity warnings at 180/365/670/700 days, deletion after the 30-day grace, moderation-copy purges. (All of those are **counts of days, never calendar months** — SPEC §4.8, §4.2.) Professional stacks often add a queue system (Celery + Redis) for such work. **We refuse that complexity.** Every one of these tasks is fine running once per hour or per day; none needs to fire the instant it is due. So each is a small named command, and **cron** — the standard Unix scheduler present on every server, literally an alarm clock for programs — runs them on schedule. Two moving parts fewer (no queue, no Redis), and each job can also be run by hand for testing.

---

## 3. The Recommended Stack, Piece by Piece

| Layer | Choice | One-line role |
|---|---|---|
| Language | **Python 3.12+** | The single language of the whole project |
| Web framework | **Django (current LTS)** | Pages, database access, login, admin — batteries included |
| Password hashing | **Argon2id** via `django[argon2]` | Slow, memory-hard hash — required by SPEC §4.6.1 |
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
- **Timestamps are rendered by the server, once, per page load** (SPEC §7.5.1, §16.3) — there is no clock in the browser, no script that re-renders "a few minutes ago" as the reader sits there, and no timestamp in any data attribute for such a script to read. This falls out of server rendering for free and must not be "improved" later: a live-updating age would break WCAG 2.2.2, and shipping the true timestamp to the client would defeat the point of the ladder.
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
- **Timestamps convey their meaning in visible text only** (SPEC §7.5.1, §16.4). No `title` tooltip anywhere: hover does not exist on a touchscreen, keyboard focus does not trigger `title`, and screen readers announce it inconsistently — a tooltip-only exact time would be a 1.4.13 failure and is banned outright rather than left to a template author's judgment. The relative phrase is the whole of what is communicated; there is nothing hidden behind an interaction.
- **Preformatted posts** (SPEC §7.2.1) get `tabindex="0"`, an accessible name, and a visible focus ring on their scroll container, because a horizontally scrollable region that only a mouse can pan fails 2.1.1. This is the one place the architecture knowingly accepts two-dimensional scrolling, under SPEC §16.3's documented exemption.
- **Banned outright:** accessibility overlay widgets of any kind (SPEC §16.4) — they are third-party JavaScript and would violate §15.2 twice over. There is no configuration in which one is acceptable.

---

## 4. How the Data Is Organized

Plain-language inventory of the ~20 database tables. (Exact fields are deliverable-(c)/(d) material; this is the map.) Anything whose identifier ever appears in a URL gets a **random unguessable ID** (UUID), per SPEC §9.3 — no guessable numbering anywhere a browser can see.

**People and connections**
- **users** — primary key: a permanent internal **UUID** (all other tables reference users only by this ID; it never changes and is never reused). Attributes: login email (exactly one, unique among active accounts, changeable via verified-new-address flow — SPEC §4.6; a credential, not an identifier), login credentials held in a separate **credentials** table (below) rather than a password column, display name **plus previous display name and name-changed date** (drives the 90-day "formerly" dual display and the 90-day change cooldown, SPEC §4.5.1 — one previous name suffices because the cooldown ≥ display-window invariant forbids overlapping transitions), joined date, last-login date (for §4.8), deactivation/deletion-grace state. Contact-card emails are unrelated records in **contact_items**. **Name rendering rule (SPEC §4.5.1):** names are never snapshotted onto content; every surface renders names through **one shared helper** that appends the "formerly" tag during a transition — the same one-place-only discipline as the visibility engine (§5).
- **name_blocklist** — operator-curated blocked strings (SPEC §4.5), checked at every display-name set (registration and change) **and, from SPEC v1.15, at every save of either bio field** (§9.4) — the same list, the same check, three call sites. A rejected save is refused with an honest message and persists nothing.

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
- **posts** — type (feed/profile), text, optional image reference, `created_at` (drives 90-day expiry *and* feed order), pinned flag (profile posts only, ≤10), and a nullable **`edited_at`** (SPEC §7.8). **`edited_at` is display-only:** expiry reads `created_at`, feed ordering reads `created_at`, and no query may sort or filter by `edited_at` — otherwise editing would silently become a way to bump a post or outlive the 90-day promise (SPEC §7.8 invariants 2 and 3). Feed posts also need the author's **last feed-post time** for `POST_MIN_INTERVAL_MINUTES` (SPEC §7.3) — a timestamp comparison, not a `rate_counters` day tally, because the rule is spacing rather than volume; profile posts are exempt.
- **post_audience** — the posting-time snapshot: one row per (feed post, recipient). §7.4's rule = "row exists here AND friendship currently exists." **An edit never writes to this table** (SPEC §7.8 invariant 1); the one thing an edit *can* change is a profile post's rows in `post_hashtags`, because §11.3's gate is evaluated live by design.
- **comments** — flat, on posts; own 90-day clock; nullable **`edited_at`** under the same display-only rule. Editing is author-only: the post author's delete power (§8.1) must not be wired to an update path.
- **post_follows** — one row per (post, follower) for SPEC §12.3. Written when someone comments (and removable by the per-post toggle). Two rules the model must not be trusted to enforce on its own: **following is private** — no query may expose followers to the post author, and no count of them exists anywhere — and **a row is permission-to-be-notified, not permission-to-see**. Delivery re-asks the visibility engine every time (§5), so unfriending, a block, or a lapsed hashtag gate silently stops notifications without the row needing to be found and deleted.
- **reactions** — (user, target, phrase from `REACTION_SET`); one per user per target.
- **hashtag_vocab** — the operator-curated vocabulary (§11.2), edited in Django admin.
- **profile_hashtags** / **post_hashtags** — join tables to the vocabulary.
- **images** — file path, owner, kind, upload date, **`alt_text`** (uploader-authored description, ≤ `ALT_TEXT_MAX`) and **`is_decorative`** (the explicit "no description needed" choice). One of the two is always set — the composer requires a deliberate choice (SPEC §16.3) — and every rendering surface reads them from here, so no template invents alt text of its own.
- **profiles** — the two bio fields of SPEC §9.4, which are **not interchangeable and must not be collapsed into one column with a length check**: `short_bio` (≤ `BIO_SHORT_MAX`, basic-tier/FoF-visible, **rendered with links disabled**) and `extended_bio` (≤ `BIO_EXTENDED_MAX`, friends-only, allowlisted links permitted). Also gallery membership, **profile-page theme choice** (what visitors see, §9.1), the owner's **own-app-view theme**, and the **"always use my own theme" viewer override flag** (SPEC §9.1 v1.4). Two timestamps drive the SPEC §13.6 cooldown: **`short_bio_changed_at`** and **`photo_changed_at`**, each starting a `BIO_CHANGE_COOLDOWN_HOURS` clock with a `BIO_EDIT_GRACE_MINUTES` free window measured from the *first* save in a burst — so the stored timestamp is the burst's start and is **not** rewritten by a grace-window save. Clearing `short_bio` to empty bypasses the check entirely, and a save rejected by screening writes nothing, so it cannot start a clock.

**Contact cards (§10)**
- **contact_items** — up to 12 per user: kind (phone/email/messenger-link), value, default on/off.
- **contact_overrides** — per item: group-level and individual-level on/off rows. The visibility engine resolves the cascade (individual beats group; among groups, deny beats allow).
- **card_requests** — who asked whom, when, what was auto-answered.
- **access_flags** — the request-more-access flags (§10.5; may ship v1.1 — table costs nothing to design now).

**Flows and operations**
- **introductions** — broker, the two candidates, per-side accept/decline state (§5.5).
- **notifications** — the in-feed items (SPEC §7.7, §12). Each row carries: recipient, **event kind** (blog post / photo change / gallery addition / comment activity / reaction activity / friend request / introduction / card request / security event …), a reference to the subject, read state, and a **coalescing key**. Three properties matter more than the columns:
  - **Coalescing happens on write, into an existing unread row — never by inserting a duplicate.** SPEC §12.3 uses two different keys: profile updates coalesce on (author, recipient, kind) within `PROFILE_NOTIFY_WINDOW_HOURS`, while comment and reaction activity coalesces on (post, recipient) **until read**, with no clock at all. Both are "find the open row and update it," which is why read state lives here rather than being derived.
  - **Actors are rendered live, never stored as text.** A notification stores actor *references*; the display name comes from the shared name helper (§4.5.1) and reactions/comments that were removed simply drop out at render time (SPEC §12.2). Storing "Alice and Tom commented" as a string would freeze a deleted comment into the feed and re-break the rule that names are never snapshotted onto content.
  - **No counts.** The model must not carry, and no query may compute, an unread badge count or a follower count (SPEC §12.2, §17). Names overflow to "and others"; nothing is ever tallied.
- **notification bodies never contain post or comment text** (SPEC §12.2). The template renders actor + kind + relative age + link; if a body excerpt ever appears in a notification, a profile post has become a feed post with a 300-person audience.
- **reports** — reporter, target, category, **frozen copy**, status, purge-by date (§13.2–13.3); handled in Django admin.
- **operator_requests** — the §13.5 form submissions (category, text, submitter).
- **upheld_report_counters** — the content-free per-account counts that outlive everything else (§13.4).
- **rate_counters** — per user/action/day counts for §13.6 (in the database, not Redis — Decision 5's simplicity again). Note that **three of §13.6's controls are not day counters and do not live here**: the feed-post spacing (`POST_MIN_INTERVAL_MINUTES`) and the two bio/photo cooldowns (`BIO_CHANGE_COOLDOWN_HOURS`) are *elapsed-time-since-last* checks against timestamps on `posts` and `profiles`, and login backoff has its own `login_attempts` table. A day tally cannot express "not again for 12 hours."
- **url_allowlist** — operator-curated domains (SPEC §7.2, §7.2.3), edited in admin. **Not a bare domain list.** Each row carries the host, the **admitting category** (convening / hosts-what-we-cannot-host / messenger handoff — SPEC §7.2.3, so the operator's own filter stays legible over time), and **redirector-rejection patterns**: the paths and query parameters on that host which must be refused even though the host is allowed. Rows are seeded with the known cases (`youtube.com/redirect`, `google.com/url`, and any `?q=`/`?url=`/`?redirect_uri=`-style parameter carrying an absolute URL). A row may also be marked inactive rather than deleted, so an operator can withdraw a domain without losing the reason it was added.

**Configuration constants (SPEC §14)** live in **one Python file, `constants.py`**, each named exactly as in the spec (`FRIEND_CAP = 300`, …) with a comment citing its SPEC section and the raise-only rule. Code must reference the constant, never a bare number.

**Single-source rendering helpers.** The visibility engine (§5) is the most important instance of a general rule, not the only one. Four things are rendered by **exactly one function each**, called by every surface and reimplemented by none:

| Helper | Renders | Why it must be single-source |
|---|---|---|
| Name helper | Display name, with the "(formerly …)" tag during a transition | SPEC §4.5.1 — names are never snapshotted onto content, so a second implementation would show a stale name somewhere |
| **Time helper (new, SPEC §7.5.1)** | The relative phrase for any timestamp | A 40-row ordered ladder with exact boundaries. Two implementations *will* disagree at the edges, and the gaps-and-overlaps failure mode is silent — a mis-ordered bound renders an empty string rather than an error |
| Alt-text accessor | Image description or the explicit decorative mark | SPEC §16.3 — alt text is data on `images` (§4), never invented by a template |
| Theme selector | Which theme's CSS variables a page emits | SPEC §9.1 — the viewer override must win everywhere, including on someone else's profile |

The time helper carries one prohibition the others do not: **it emits the phrase and nothing else.** No `title` attribute, no `<time datetime="…">`, no data attribute carrying the true timestamp (SPEC §7.5.1). The exact value is deliberately absent from the interface *and* the markup — a tooltip would fail §16.4's hover ban, and a `datetime` attribute would ship in page source the precision the rule exists to withhold. Its two documented exceptions — the absolute-days expiry countdown (§7.5) and account/security events (§4.6.1) — are separate call sites that format absolute time on purpose, not flags on the helper.

---

## 5. The Visibility Engine (the heart)

### 5.1 The rule

Restating Decision 4 as an implementation rule, because it is the single most important sentence in this document for the AI builders:

> **No template, page, list, count, notification, export, or job may decide for itself who can see something. All such decisions call the visibility module. Any code change that inlines a visibility rule elsewhere is wrong, even if it produces correct output today.**

The module implements, from SPEC: §5.4 blocks (checked first, always, both directions), §7.4 audience snapshot + current friendship, §9.2 profile tiers, §10.3 the contact cascade with deny-beats-allow, §11.3 the three-condition hashtag gate evaluated live, §11.5 friend-list filtering. "Preview-as" (SPEC §9.5) is the same code with a substituted viewer — plus one guard: preview mode must be strictly read-only.

Two smaller v1.3 features illustrate the rule in action: **comment-name linking** (SPEC §8.1 — link the commenter's name only if the viewer has basic-tier access) is just the template asking `can_see_profile_tier(viewer, commenter)`; the **discover-page tag filter** (SPEC §11.4) is just the discover queries re-run with a tag condition added — the same `can_see_post` / `are_connected` calls decide every item shown. Neither feature gets its own permission logic.

### 5.2 What the rule costs, and why the cost is an architectural problem (v1.19)

Everything above is about correctness, and until v1.19 this section said nothing about how often the engine runs or what each run costs. An external review of 1.16 raised that gap, and the founder judged it the strongest technical point in the external reviews: *if every item on a page independently asks `can_see_post(...)`, and each of those independently re-checks friendship, blocks, hashtags, snapshots and overrides, one accidentally creates many hundreds of repeated database lookups.*

The load is not hypothetical, and recent spec versions increased it:

- **SPEC §7.7.1** lets the reader choose `POSTS_PER_PAGE_OPTIONS` = 20 / 40 / 60. A reader on 60 is an ordinary reader, not an edge case.
- **SPEC §8.1** requires every rendered name to be a link or plain text according to `can_see_profile_tier(viewer, that person)` — and v1.16 extended that from commenters to post authors, mutual-friend context, and the author's private reaction list.
- **SPEC §11.5** renders mutual friends by name on every profile.
- **SPEC §7.9** puts an audience line on every post. That one is genuinely cheap — it is derived from the post's own type and tags and never from the viewer — but it is one more per-item computation.

So a sixty-post page carries at least sixty author names, sixty audience lines and, on any surface that renders comments inline, several commenter names each. Written naively — every item asking its own question, every question reading its own rows — that page asks the engine several hundred times and issues several hundred queries, of which the large majority are **the same question asked again about the same handful of people**: is this pair blocked, are these two connected, what tier does this viewer hold. **None of those answers can change while a single page is being built.**

What makes several hundred queries expensive is worth stating, because the intuitive answer is the wrong one. It is **not** the volume of data — every one of those answers is a handful of bytes. It is that each query is a **separate round trip**: the application sends it and waits, the database parses it, plans it and runs it, and sends back. That overhead is paid per query and is largely independent of how much comes back, so several hundred queries in sequence cost several hundred times the overhead of one. This is also why the bulk form of §5.4 moves *less* data rather than more: the repeated questions were re-reading the same rows over and over.

The failure mode is not a crash. It is a feed that takes four seconds on the €8 VPS of §11 — and the danger is not the four seconds. It is what a four-second feed makes someone do. The obvious local fix is to reach into the template or the view and fetch the friendship directly, once, for the whole list. That is a five-line change, it makes the page fast, it looks right in review because the output is right, and it quietly breaks Decision 4 in the one place — a list — where a permission bug is hardest to see and most expensive when the rules later change. **The performance gap is a threat to the architectural rule before it is a threat to speed. That is why it is answered here, in the architecture, rather than left to whoever eventually finds the page slow.**

The answer has two halves, and both live **inside** the module where no caller can see them: the engine remembers, within one request, what it has already worked out (§5.3), and it accepts questions in the plural so that a page of sixty items costs the same number of queries as a page of twenty (§5.4). Nothing a template, view, job or export does changes because of either. If a proposal ever requires a caller to know that a cache or a batch exists, it is the wrong proposal.

### 5.3 Request-scoped memoization — the only cache in this system (v1.19)

**Memoization** is remembering an answer already worked out, so that the same question is never worked out twice. Nothing more exotic than that: while one page is being built, the engine keeps a note of what it has already established about the viewer, and consults its own notes before it consults the database.

**The scope, stated first and hard, because everything else depends on it: one HTTP request. Populated on first use, discarded when the response is sent, never written to disk, never shared between requests, never shared between users.** It is a scratch pad for one page render, not a cache in the ordinary sense of the word.

**What the engine may remember.** Everything on this list is either a conclusion the engine itself reached, or the small bounded set of rows it reached that conclusion from — never a general-purpose row cache:

| Remembered | Keyed by | Cost when first needed | Why it is safe |
|---|---|---|---|
| The viewer's **friend set** (account ids of accepted friendships) | viewer | one query, at most `FRIEND_CAP` = 300 ids | Bounded by SPEC §5.1. Answers "is X a friend of the viewer" for every X on the page with no further queries |
| The viewer's **block set** (ids in *either* direction) | viewer | one query | SPEC §5.4 is symmetric in effect, so one set covers both directions and is checked first, always |
| The viewer's **own profile hashtags** | viewer | one query, at most `PROFILE_HASHTAG_MAX` = 10 | Condition 3 of SPEC §11.3, needed once per gated post and identical every time |
| **Connection status** (friend / FoF / stranger, blocks short-circuiting) | the ordered pair | free for friends and blocks (the sets above); one query for the rest, batched per §5.4 | The relation cannot change mid-render |
| **The mutual friends** between the viewer and another person | the ordered pair | falls out of the same query as FoF status | SPEC §11.5 renders those names anyway; computing them twice would be the waste, not the risk |
| **Profile tier** (nothing / basic / full) | the ordered pair | derived from connection status; no query of its own | SPEC §9.2 is a function of the row above |
| **The resolved contact card** for a viewer | the ordered pair | one or two queries per card | SPEC §10.3's cascade is deterministic given the same rows; a card renders once per page |
| **The answers themselves** — `can_see_post`, `can_see_profile_tier`, `visible_contact_card`, `are_connected`, `can_act` | the **full argument tuple, viewer first** | free after the above | The inputs cannot change mid-render (but see the write rule below) |

Note what is *per-viewer* and what is *per-pair*. The first three rows are per-viewer and are the ones that do the real work: because `FRIEND_CAP` is 300 and `PROFILE_HASHTAG_MAX` is 10, the viewer's whole social position fits in three small queries and a few kilobytes, after which most questions a page asks are answered by set membership and touch the database not at all. The block set is the one entry with no cap behind it; in practice it is bounded by human effort, each row is a pair of identifiers, and a user with enough blocks to matter here is a moderation signal (SPEC §13) rather than a performance problem.

**Where it lives, and why callers cannot see it.** A `contextvars.ContextVar` holding a plain dictionary — a Python variable whose value is private to the unit of work currently running, which is the standard mechanism for per-request state and, unlike a thread-local, stays correct if the app is ever run on asynchronous workers. A small middleware sets a fresh empty dictionary at the start of every request and clears it in a `finally` block at the end, so an exception cannot leave a populated dictionary behind for the next request that thread serves. **No caller ever creates, passes, reads, or clears it.** Views, templates, jobs and exports call the same five functions they always called; the memo is an implementation detail of the module, which is exactly what Decision 4 requires.

**The key always begins with the viewer, and it is the viewer the engine was *called with*.** SPEC §9.5's preview-as substitutes a different viewer into the same code **inside one request** — the owner's page renders as the owner, then a section of it renders as Alice. A memo keyed on the object alone would serve the owner's answers to the preview or the preview's answers to the owner, in the one feature whose entire purpose is to show the owner the truth about what someone else sees. Two rules follow, and they are small details with a bad failure mode:

1. Every key is a tuple beginning with the viewer's account id. There is no key that does not identify a viewer.
2. The engine takes its viewer as an **explicit argument** and never reads "the logged-in user" from the request, the session or a thread-local. The memo's *storage* is ambient; the viewer never is. Preview-as then needs no special case at all, which is the property Decision 4 bought in the first place.

**A write inside the request empties the whole memo.** The answers cannot change while a page is being *rendered*, but a request that writes and then renders is a different matter: accepting a friend request, blocking someone, or editing a profile post's hashtags (SPEC §7.8's one deliberate exception, which §11.3 evaluates live) all change what the engine would now answer. The rule is deliberately blunt: **any write to a relation the engine reads — `friendships`, `blocks`, `post_audience`, `profile_hashtags`, `post_hashtags`, `groups`, `group_members`, `contact_items`, `contact_overrides` — discards the entire dictionary.** Not selective invalidation. Selective invalidation is precisely the kind of cleverness that produces a privacy bug nobody can reproduce, and the blunt version costs nothing: Django's normal write flow redirects rather than rendering, so this fires rarely, and when it does the page simply re-derives three small queries.

**No request, no memo.** The cron jobs of §6 run outside any HTTP request, so the ContextVar is unset and the engine memoizes nothing; every question is answered from current state. This is deliberate and is not a performance concession. Notification delivery re-asks the engine per recipient precisely so that an unfriending, a block or a lapsed hashtag gate silently stops delivery to someone who still holds a `post_follows` row (§4) — a memo living for the length of a job that runs for minutes would defeat the re-check that rule exists to guarantee.

### 5.4 Asking in bulk — the plural forms (v1.19)

**Memoization removes repeats. It does not remove sixty separate questions.** A page that asks `can_see_post` sixty times about sixty *different* posts repeats nothing at all and still makes sixty round trips.

So the engine also answers **in bulk**: handed a whole set, it returns all the answers together. *"Which of these sixty posts may this viewer see?"* asked once, instead of *"may this viewer see this post?"* asked sixty times. The rules applied are identical, the decision still belongs entirely to the engine, and the caller learns nothing it could not have learned one question at a time — **only the number of questions changes.** Below, the two are called the **plural** and **singular** forms of the same question.

There are exactly two plural shapes and no third.

**1. One queryset per list, owned by the engine.** Every list on the platform takes its base queryset from the module: the feed (SPEC §7.7), an author's Blog tab and Pinned tab (SPEC §9.1, §9.2, §11.3), the discover page's matched posts and suggested people (SPEC §11.4), the friends page (SPEC §11.6). **The engine owns every condition that decides who sees what; the caller owns ordering, folding and paging** (SPEC §7.7.1) and may add nothing else. This also keeps paging honest — the database applies the limit, so a reader on 60 does not cause 90 days of posts to be loaded into memory and filtered.

This half is not primarily an optimization, and the reason deserves stating plainly, because it is the sharpest point in this section:

> **A queryset filter is a visibility decision.** A view that writes `Post.objects.filter(audience__user=viewer, …)` has inlined a visibility rule into a list — in the least visible place available, in the place where the rules are hardest to keep in step, and in a form that no reviewer reads as a permission check. Before v1.19 the engine offered no way to build a list correctly: a builder had either to write that filter or to load everything and check it item by item. **Providing the queryset is what makes Decision 4 obeyable for lists,** rather than a rule that lists quietly cannot follow.

**2. One batch call for tiers.** `profile_tiers(viewer, people)` takes every person whose name will appear on the page and returns each one's tier (nothing / basic / full) in a fixed number of queries. The viewer's friends and blocks are already in hand from §5.3, so friends, blocked pairs and the viewer themselves are settled with no query at all; the only people needing work are the remaining non-friends, and they are resolved **together**, by one query asking which of the viewer's friends are friends of any of them. That query also returns *which* friends — which is exactly what SPEC §11.5's "knows Alice and Tom" and SPEC §9.2's basic tier need to render. **One result, two requirements, neither computed twice.** SPEC §8.1's single link-or-plain-text helper is fed from this map rather than asking per name.

**The singular functions do not go away; they become the item-level face of the same code.** Decision 4's five questions remain the API for a single post, a single profile, a single card — the single-post view, notification delivery (§4), the permission-checked image view (Decision 3), the data export (SPEC §4.9). Where a singular answer can be expressed as a plural one over a set of one, **it is implemented that way**, so that each rule has one implementation and not two.

**The one honest cost, and the test that pays it.** A queryset expresses a rule in SQL; `can_see_post` expresses the same rule in Python. This document has argued in five other places that two expressions of one rule will drift, and it would be dishonest to exempt this one. The mitigation is a single test, specified in §9: over a seeded dataset with blocks, lapsed friendships, audience-snapshot mismatches and hashtag gates all in play, **the set of posts a list queryset returns for a viewer is exactly the set for which `can_see_post` returns true, for every viewer in the fixture.** If the two ever disagree, the next test run says so instead of a user discovering it.

### 5.5 What is never cached, and the three ways it will be tried (v1.19)

**Cross-request caching of a visibility answer is forbidden.** Not discouraged — forbidden, and the reasons are SPEC's rather than a matter of taste:

- **SPEC §11.3** requires the hashtag gate be evaluated **live**: *"if the last shared tag disappears from either side, or the mutual friendship lapses, access ends."* A cached answer means access ends when the cache says so.
- **SPEC §7.4** pairs a posting-time snapshot with **current** friendship, so unfriending removes access to every past post. A cached "yes" is that removal not happening.
- **SPEC §5.4** blocks are immediate and mutually total. A cached "yes" is a block that has not taken effect yet.

In each case the bug is not a wrong pixel. It is a person seeing something the platform promised they could not, for as long as the cache lives, with nothing in any log and no error anywhere. That is why the scope in §5.3 is stated as a hard boundary rather than a default.

Three specific mechanisms are named here, because each is a small, well-intentioned change that a later builder — or a model asked to "make the feed faster" — would reasonably propose. §14 carries them as rejected rows for the same reason.

1. **`functools.lru_cache`, or any module-level caching decorator, on an engine function.** This is the smallest possible change and the worst one: the cache lives for the life of the Gunicorn worker **process** and is shared by every request that process serves. Keyed on (viewer, post) it would serve hours-old answers to the right person; keyed on the object alone — the easy mistake §5.3 already guards against — it would serve one user's answers to another. Banned outright, in the engine and in anything it calls.
2. **Django's cache framework applied to visibility answers or to permission-checked output** — `cache.get`/`cache.set` around an engine call, `@cache_page` on a view, or template fragment caching of anything a viewer's permissions shaped. Whole-page and fragment caching of a per-viewer page is the same bug wearing HTML. (This says nothing about caching things that are the same for everybody, of which this platform has almost none — see §13.3.)
3. **A precomputed visibility table in the database** — a `visible_to` join table, a materialized audience, anything that answers "who may see this" by lookup rather than by evaluation. This is the one that will be proposed with the best intentions and would do the most damage, because it converts SPEC's live rules into a cache with no expiry and a refresh job nobody has written. **`post_audience` (§4) is not an instance of this**, and the distinction matters: it stores the *posting-time snapshot*, which SPEC §7.4 defines as a stored fact, and the engine still applies the current-friendship and block tests on top of it on every single read.

Two clarifications, so the ban is not read wider than it is. It concerns **visibility answers**, not everything in the system: sessions, `rate_counters` (§4) and `login_attempts` are unaffected, and so is ordinary query efficiency — `select_related` and `prefetch_related` on a queryset the engine handed out are the normal way to fetch authors, images and comments and are encouraged. And it survives scale: when §13.2's Stage 2 eventually adds Redis on measurement rather than fashion, **no visibility answer goes into it**.

---

## 6. The Housekeeping Jobs (cron)

Each is a Django management command — runnable by hand, scheduled by cron. All must be **idempotent** (safe to run twice; a re-run finds nothing left to do), because cron sometimes double-fires or gets run manually during testing.

They also run **outside any HTTP request**, which means the visibility engine's request-scoped memo does not exist for them and every question they ask is answered from current state (§5.3). That is deliberate rather than a concession: a job may run for minutes, and the delivery paths that re-ask the engine per recipient (§4, `post_follows`) do so precisely so that a block or an unfriending taking effect mid-run stops the very next notification.

| Job | Schedule | Does (SPEC ref) |
|---|---|---|
| `expire_content` | hourly | Delete posts/comments > 90 days (unpinned), their images, reactions (§7.5) |
| `purge_moderation` | daily | Purge frozen copies past their date; hard cap 90 days (§13.3) |
| `replenish_invites` | daily | +1 invite to anyone `INVITE_REPLENISH_DAYS` = 30 days past last replenish, cap 5 (§4.2); expire 14-day-old invites back to budget (§4.1) |
| `process_deletions` | daily | Erase accounts past 30-day grace; write anonymized invite-tree stubs (§4.7, §4.3) |
| `inactivity_sweep` | daily | Send `INACTIVITY_WARN_DAYS` warnings (180/365/670/700 days since last login); delete at `INACTIVITY_DELETE_DAYS` = 730 (§4.8). **Days, not calendar months** |
| `reset_rate_counters` | daily | Clear yesterday's rate-limit counts (§13.6). Leaves the timestamp-based controls alone — feed-post spacing and the bio/photo cooldowns are elapsed-time checks, not counters (§4) |
| `expire_notifications` | daily | Delete notifications whose subject no longer exists (expired or deleted post, deleted comment, deleted account) and any older than `CONTENT_TTL_DAYS`. Without this, the feed accumulates links to content the 90-day promise has already destroyed (§7.5, §12) |
| `backup` | nightly | §10 below |
| `verify_restore` | weekly | Restore the newest backup into a scratch database, run a smoke query, drop it, record the result; email the operator on any failure (§10). Checks free disk first and alerts rather than restoring if there is not room — a verification job that fills the disk is worse than none |

---

## 7. Security Posture (what protects what)

- **Transport:** HTTPS everywhere via Caddy; HTTP redirects to HTTPS; modern TLS only.
- **Sessions, not tokens:** Django's cookie-based login sessions (httponly, secure, sensible expiry). Logged-out users can reach exactly three pages: login, password reset, invite redemption (SPEC §2).
- **Authentication and anti-phishing (SPEC §4.6.1):**
  - *Codes, not links.* Password reset, login-email change, and registration email-verification use a short-lived numeric code (`RESET_CODE_TTL_MINUTES`, `RESET_CODE_LENGTH`), stored **hashed** in a small `credential_codes` table with a single-use flag and an attempt cap, entered on a page the user navigated to themselves — never delivered as a login link. Only invites are links (a new user has no open page). This is deliberately *not* a signed-URL/token scheme, because the whole point is that no clickable login link ever exists to imitate.
  - *Multiple credential types from day one.* Login credentials live in their own `credentials` table keyed to the user (`type` = password | passkey, plus type-specific material), so a WebAuthn/passkey credential can be added later without touching the user model. v1 creates only password rows; passkeys are deferred (SPEC §4.6.1). The password's slow hash (below) is stored here.
  - *Breach-password check.* At registration and password change, the backend makes a **server-to-server** k-anonymity range request to the Have I Been Pwned Pwned-Passwords API (send the first 5 hex characters of the password's SHA-1; match the returned suffix list locally). Only a hash prefix ever leaves the server — never the password, never any user identifier — and it is a backend HTTPS call, not a browser script, so it is §15.2-clean. Fail-open on API outage (a third party being down must never block a signup), logged.
- **The standard attacks** (CSRF, SQL injection, XSS) are covered by Django defaults; the build plan will state the few settings to verify rather than trust. **Password hashing uses Argon2id** (SPEC §4.6.1) rather than Django's PBKDF2 default — Django supports it as a first-class hasher, installed as part of the §3 stack via `django[argon2]` (which pulls in `argon2-cffi`). **It is not an addition anybody elected (v1.18):** SPEC §4.6.1 requires the slow memory-hard hash, so the dependency is implied by the specification and belongs in the stack table, which is where §3 now carries it. Framing a mandatory dependency as an approved exception invites a later builder to treat it as optional.
- **Link validation (SPEC §7.2.3):** the URL allowlist is one of the controls SPEC §4.6.1 leans on to close in-platform phishing delivery, so it is implemented as a **validator, not a substring check**. One shared function validates every URL in every post and comment — **on every save, create and edit alike** (SPEC §7.8 invariant 4). A validator wired only into the create path is a **defective implementation**, and a quiet one: it would let an author publish clean text, pass the check, and then edit a disallowed link into the stored post, defeating the entire control without ever raising an error. The same "revalidate on every save" rule governs length caps, whitespace normalization, hashtag-vocabulary membership, and image EXIF-stripping on a replaced image. Practically, this means content validation belongs to the model/form layer that both paths share, never to the create view. The validator must:
  1. Parse the URL properly (never regex-match a raw string) and require `https`.
  2. Match the **host exactly or as a subdomain of an allowlisted host** — never a substring, never a suffix test (`evil-youtube.com` and `youtube.com.attacker.net` must both fail).
  3. **Reject the row's redirector patterns** (§4). This step is not optional: `youtube.com/redirect?q=…` and `google.com/url?q=…` pass any host check yet hand the reader to an arbitrary attacker page, which would silently defeat the whole control. **A host-only implementation is a defective implementation of this section.** As a belt-and-braces rule, any allowed URL whose query string contains an absolute `http(s)://` URL is refused regardless of host.
  4. Refuse URL shorteners categorically — they make the destination unknowable, so no shortener is ever allowlistable (SPEC §7.2.3).
  Adding a domain in admin therefore carries an operator duty: check the service for a redirector before activating the row. New domains are added inactive by default.
- **No third-party anything in pages:** no CDN assets, no fonts from Google, no analytics, no embeds (SPEC §7.2, §15.2). Allowlisted links are rendered as **plain clickable links only, never embedded or preview-carded** — an embed would load the external service's scripts into our page. A build-plan checklist item: load any page and confirm the browser makes **zero** requests to foreign domains.
- **Rate limits** (§13.6) enforced in the database per user/action/day. **Login attempts** get a stricter, security-specific control (SPEC §4.6.1): per-account *and* per-source-address failure counters in the database with exponential backoff and temporary lockout (`LOGIN_ATTEMPT_LIMIT`, `LOGIN_LOCKOUT_MINUTES`), complemented by OS-level fail2ban on the SSH surface. No CAPTCHA (rejected — SPEC §4.6.1, §14 below).
- **The friend-request surface (SPEC §5.2, §13.1):** a friend request carries no composed text, but it *does* display the requester's own short bio and profile photo to up to 20 FoFs a day who never asked for either. Three controls answer that, and they are security controls rather than cosmetics: the short bio is **screened against `name_blocklist` at every save** (§4); the short bio and profile photo are held to `BIO_CHANGE_COOLDOWN_HOURS`, which is what stops the field being rewritten between batches of requests; and the short bio is **rendered with links disabled** — not merely validated, but never linkified at all, so no clickable destination can be delivered through it. Note the division of labour: screening cannot read an image, so the **cooldown is the only control that covers the profile photo**, image moderation being out of scope for a solo operator. The report queue is the backstop for the rest.
- **Email domain authentication:** the sending domain publishes **SPF, DKIM, and DMARC at `p=reject`** (SPEC §4.6.1) — stops spoofing of our real domain; a founder-performed DNS step at build-plan Step 5.5.
- **No visibility answer outlives its request (v1.19).** The engine memoizes within a single request and never beyond one (§5.3), and cross-request caching of a permission answer is banned in three named forms — a module-level `lru_cache`, a Django cache entry, a precomputed `visible_to` table (§5.5). This belongs in the security posture and not only in §5 because the failure is silent and indistinguishable from correct behaviour: a block (SPEC §5.4), an unfriending (SPEC §7.4) or a dropped hashtag (SPEC §11.3) must take effect on the very next page, and a cached answer means it takes effect when the cache happens to expire. Nothing logs that, and nobody reports it.
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

**A second rule with the same logic, stated in v1.18: test depth proportional to *blast radius*.** §4 funnels several behaviours through exactly one implementation each — the visibility engine (§5), the name helper, the time helper, the alt-text accessor, the theme selector, the URL validator (§7), and the accessible partials of §3.8. That is the right design, and its cost is that a bug in any one of them is never a bug on one page: it is the same wrong behaviour on every page at once. A single-source helper therefore earns tests in proportion to how many surfaces it reaches, **not** in proportion to how much code it contains — which is why a thirty-line time helper carries the second-densest test in this project.

- **Dense automated tests on the visibility engine** — blocks, tier boundaries, cascade conflicts, hashtag-gate edge cases, snapshot-plus-current-friendship. This is where a bug = a privacy breach.
- **Four tests on the engine's *shape*, added with the caching and bulk rules of §5 (v1.19).** The first of them asserts a **cost** rather than a behaviour, which nothing else in this project does, and it earns its place under the blast-radius rule above: what it protects is not the page's speed but Decision 4 itself. A slow feed is repaired by inlining a query, and that repair is invisible in review because the page still renders correctly. The other three are ordinary correctness tests whose failures happen to be privacy failures. All four are plain Django — `assertNumQueries` and the test client, no new dependency, no benchmark harness, and deliberately **no timing assertion**, which on a laptop would be flaky and would measure the machine rather than the code.
  - **The shape test.** Render the same seeded feed twice, at `POSTS_PER_PAGE_OPTIONS` 20 and at 60, and assert the two query counts are **equal** — and that both sit under a stated ceiling. The equality is the real assertion and the durable one: it says the page's cost does not grow with the number of items, which is the whole property §5.4 exists to create. The ceiling is a number that may be revised upward as features land, with a line in CHANGELOG saying why; **the equality may not be revised** — a change that breaks it is the regression. The same test runs on a profile Blog tab and on a single post carrying many comments.
  - **The equivalence test** (§5.4) — for every viewer in a fixture seeded with blocks, lapsed friendships, audience-snapshot mismatches and live hashtag gates, the posts a list queryset returns are **exactly** the posts for which `can_see_post` returns true. This is the one test that stops the SQL expression of a rule and the Python expression of it drifting apart, which is the price §5.4 knowingly pays for having a plural form at all.
  - **The viewer-in-the-key test** (§5.3) — inside one request, ask a question as the real viewer, then ask the same question under preview-as (SPEC §9.5) as someone whose answer differs, and assert the second answer is the second viewer's. The failure this catches is a memo keyed on the object alone, which would show the profile owner a preview of their own answers in the one feature built to show them somebody else's.
  - **The flush-on-write test** (§5.3) — inside one request, ask, then create a block, then ask again, and assert the answer changed. A memo that survives a write in the same request is a stale answer with a privacy consequence.
- **Automated tests on the lifecycle jobs** — expiry, deletion-with-stub, invite replenishment, notification expiry. A bug here breaks a promise made to users (§7.5's "nothing outlives 3 months").
- **A boundary table test on the time helper** (SPEC §7.5.1) — one case per ladder row, asserted at the boundary and one unit either side, plus a test that the ladder is **total**: for a large sweep of elapsed values, every one returns a non-empty phrase. The ladder's failure mode is a silent gap between two bounds rendering an empty string, which no feature test would notice and no user would report as anything but "the date is missing sometimes." Cheap to write once, and it is the whole reason the helper is single-source (§4).
- **A named test for the two helpers that had none (v1.18)** — the blast-radius rule applied to the time helper's siblings, and both are small:
  - **The name helper** (SPEC §4.5.1) — a boundary test on the transition window: the "(formerly …)" tag is present on the last day of `NAME_TRANSITION_DAYS`, absent on the first day after, and absent altogether for a user who has never renamed.
  - **The theme selector** (SPEC §9.1) — a truth table over its three inputs (the viewer's own theme, the page owner's theme, the viewer override on/off), asserting the rule that is easiest to get wrong: **the viewer's override wins on someone else's profile.** The `THEME_SET` contrast test below proves every theme is legible; nothing else proves the right theme was the one emitted.
  The **alt-text accessor** needs no test of its own: the template smoke tests below already assert that every rendered image carries the stored value, which is the whole of that helper's job.
- **Tests on the edit path specifically** — that editing re-runs the URL validator (post a clean body, edit in a disallowed link, assert refusal), that `edited_at` never affects feed order or expiry, that an edit writes no `post_audience` rows, and that a post author cannot reach an update path for someone else's comment. These are small tests guarding SPEC §7.8's five invariants, and invariant 4 is a security test, not a feature test.
- **Tests on notification coalescing and follow delivery** — that a second event updates the open unread row rather than inserting a duplicate, that removed reactions and deleted comments vanish from a rendered notification, that no query returns a follower list or an unread count, and that unfriending/blocking/a dropped hashtag silently ends delivery to a follower who still has a `post_follows` row. The last one is a visibility-engine test wearing a notification costume.
- **Ordinary features** (rendering, forms): light tests plus human use. The prototype's friendly first users are the beta test.
- **Accessibility (SPEC §16)** gets two automated tests plus a human pass, because two thirds of it *is* machine-checkable and the rest genuinely isn't:
  - a **contrast test** over every `THEME_SET` combination (§3.8) — pure Python, no dependency, fails by theme name;
  - **template smoke tests** asserting the mechanical invariants on rendered HTML: every `<img>` has an `alt` attribute (possibly empty with `is_decorative`), every input has an associated label, every page has one `<h1>` and a `<title>`, no `tabindex` above 0, no `<div>` carrying a click handler where a `<button>` belongs.
  - The **human pass** — keyboard-only, VoiceOver, 200% zoom, 320px reflow — is a build-plan gate (Step 16.5), not a unit test. No automated tool catches "the focus order is bewildering"; roughly a third of WCAG failures are only findable this way.
- Optional developer tooling (an **axe** browser extension, or `pa11y`/`axe-core` run locally) is useful for the audit and is **not** an application dependency — nothing accessibility-related ships to the browser beyond our own HTML and CSS. Any use of it as a *project* dependency needs founder approval under the build-plan dependency rule.
- Deliverable (d) will instruct the coding models to write these tests *alongside* each feature, not afterward.

---

## 10. Backups — and an Honest Tension with the Deletion Promise

Nightly: database dump + image folder, **encrypted, sent off the server** (e.g., restic to a storage box or B2 bucket; exact target chosen in the build plan).

**The restore path is verified on two schedules (v1.18), because an untested backup is a rumor — and the rumor restarts the day after the last test.** Backups fail loudly; restores fail silently, and what rots is the restore path (a schema that moved on, an expired storage credential, a rotated encryption key) and the runbook itself. A last-success line on the backup job reports none of that.

- **Weekly, automatically:** `verify_restore` (§6) fetches the newest backup, restores it into a scratch database on the server, runs a smoke query, drops it, and emails the operator if any step fails. This catches credential, key and schema rot within a week of its happening.
- **Yearly, by hand:** the founder restores onto their own Mac and logs into the restored copy, following the runbook (build-plan Steps 5.6, 16.4, 17.3).

Neither replaces the other, and the manual one is the one that matters most: the automated job proves the server can read its own backups using credentials already sitting in its own environment, while the scenario worth surviving is the one where the server is gone and the operator has a laptop, a runbook and nothing else.

**The tension:** backups are copies, so a post deleted today still exists inside last week's backup. Refusing backups would honor deletion purism but risks total loss of everyone's data. The industry-standard, GDPR-accepted resolution, which this architecture adopts:

> Backups are kept **`BACKUP_RETENTION_DAYS` = 30 days**, then destroyed. Deleted content therefore fully ceases to exist within at most 30 days of its deletion (and backups are encrypted, offline-ish, and never queried). The privacy policy states this plainly.

This amends the mental model of §7.5, and **SPEC now carries the amendment itself (v1.18)**: SPEC §7.5, §4.7 and §15.1 state the honest promise directly — *deleted at 90 days, and purged from the last encrypted backup within 30 days after that* — and `BACKUP_RETENTION_DAYS` is a SPEC §14 constant rather than an architecture detail, because a number a user-facing promise rests on belongs in the authoritative document. The wording is deliberately not "gone by day 120": that figure invites a reader to compute an exact date which in truth depends on when the last backup ran. The founder approved the retention policy on 2026-07-07 (§15 item 1); what had never happened, until 1.18, was propagating it into SPEC, which left the two documents contradicting each other on a promise — the kind that matters most if it is ever tested.

---

## 11. What This Costs (founder-funded phase, monthly)

| Item | Est. cost |
|---|---|
| VPS (e.g., Hetzner ~€6–12, DigitalOcean $8–14 class) | $7–15 |
| Backup storage (Hetzner Storage Box / Backblaze B2) | $1–4 |
| Domain name (`weebee.social`, renews ~$33/yr) | ~$3 (billed yearly) |
| Email provider | $0–15 — **the free tier does not cover launch volume**; budget the paid step from the launch month (build-plan §5.1) |
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
2. **Stage 2 — split the tiers (hundreds of thousands).** PostgreSQL moves to its own machine; images to their own storage volume; several copies of the Django app run behind a **load balancer**. The most well-trodden path in web architecture; the code barely changes because it never assumed same-machine anything except through configuration. Add the deliberately-skipped cache (Redis) and job queue (Celery) when measurements — not fashion — say so. **Even then, no visibility answer goes into that cache** (§5.5): it would hold sessions, rate counters and fragments that are identical for everybody, of which this platform has almost none, since all content is private and per-viewer (§13.3). The engine stays request-scoped at every stage, and the bulk forms of §5.4 are what keep it affordable there.
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
| Near-duplicate / content-similarity detection across an author's posts | Rejected for v1 | Cheap to build (SimHash-style shingling, first-party, no ML) but declined on cost/benefit: `POST_MIN_INTERVAL_MINUTES` already imposes real friction, a tuned threshold would misfire on legitimate repeated content, and a human reading two reported posts is more accurate at this scale (SPEC §13.2). **No table, job, or dependency for it exists** — recorded here so nobody adds one as an "obvious" anti-spam measure |
| Storing rendered notification text ("Alice and Tom commented") | Rejected | Freezes deleted comments and removed reactions into the feed and re-breaks the never-snapshot-names rule (SPEC §4.5.1, §12.2). Notifications store references and render live (§4) |
| Unread-count badges on the feed or notifications | Rejected | A count is a count; SPEC §17 has none anywhere, and an unread badge is the seed of the engagement loop §12.4 exists to keep closed. Names overflow to "and others" instead |
| `<time datetime="…">` for machine-readable timestamps | Rejected | Standard practice, and wrong here: it ships the exact timestamp in page source, quietly undoing SPEC §7.5.1. WeeBee has no API, no third-party consumers and no public pages, so nothing would consume it (§4) |
| **Redis (or any shared cache) for visibility answers** | Rejected | Would be new infrastructure against Decision 2, and unnecessary: the repeats all happen *within* one page render, which a request-scoped dictionary removes for free (§5.3). The remaining cost is per-item questions, which bulk queries fix without a cache at all (§5.4). If measurement ever brings Redis in at §13.2's Stage 2, visibility answers still stay out of it |
| **`functools.lru_cache` on an engine function** | Rejected, permanently | The smallest-looking change in this table and the most dangerous: a module-level cache lives for the life of the worker **process** and is shared by every request it serves — stale permission answers at best, one user's answers served to another if the key omits the viewer (§5.5) |
| **Django cache framework on permission-checked pages or fragments** (`@cache_page`, template fragment caching) | Rejected | Every page here is shaped by the viewer's permissions, so caching the output is caching the answer (§5.5). Caching genuinely viewer-independent output is not banned; there is almost none of it (§13.3) |
| **A precomputed `visible_to` table / materialized audience** | Rejected | Converts SPEC's live rules (§11.3's gate, §7.4's current-friendship test, §5.4's blocks) into a cache with no expiry and a refresh job nobody wrote. Recorded here so it is not proposed as an obvious database-level optimization. **`post_audience` is not this** — it stores the posting-time snapshot SPEC §7.4 defines as a stored fact, and the engine still applies the live tests on top of it every read (§5.5) |

---

## 15. Open Points — Resolution Record

1. **Backup-retention amendment** (§10): deleted content persists in encrypted backups up to 30 days. — **APPROVED by founder 2026-07-07**, and **propagated into SPEC §7.5, §4.7, §15.1 and §14 in project version 1.18** (2026-08-04), which is the step that had been missing: the approval was recorded here while SPEC continued to promise plain deletion.
2. **Email provider** (§3.6): founder deferred the final pick to the build plan (deliverable c), 2026-07-08. Postmark remains the recommendation.
3. **VPS provider and location** (§11): founder deferred the final pick to the build plan (deliverable c), 2026-07-08. Hetzner remains the recommendation; location depends on where the first users are.
4. **The document as a whole: APPROVED by founder 2026-07-08.**
5. **The engine's bulk (plural) forms** (§5.4): adopted in project version 1.19 rather than split into a later design session — **APPROVED by founder 2026-08-06**. The argument that decided it was not speed. A list that builds its own queryset has *already* broken Decision 4, and before 1.19 the engine offered a list no other way to be built; the bulk form is therefore what makes a list **able to obey** the rule, and the efficiency is a side effect of closing that gap properly. The cost is not speed either, and is recorded rather than waved away: one rule ends up expressed twice, in SQL and in Python, which is the drift this document warns about in five other places. §5.4 states it; the equivalence test in §9 closes it.
   Recorded beside it as fact rather than as an open question: **no new infrastructure was added.** A request-scoped dictionary needs no Redis, and §14 carries Redis as rejected for this purpose at every scale — including the one where §13.2 eventually admits it for other things. **SPEC was not touched, and should not be:** memoization and batching are invisible to users, and a wish to edit SPEC here would have been the signal of having drifted.

---

*Next document: deliverable (c) — BUILD_PLAN.md, the step-by-step build plan, with founder-performed steps explicitly marked.*
