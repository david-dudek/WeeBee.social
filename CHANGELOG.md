# Changelog — WeeBee

WeeBee has **one version number for the whole project**, not a version number per
document. **The current number is always the newest entry below**; the scheme began at
**1.17**, inheriting SPEC.md's number because SPEC is the spine.
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

## 1.19 — 2026-08-06

| File | Status |
|---|---|
| README.md | unchanged — version header only |
| SPEC.md | **unchanged — version header only, and deliberately so** |
| ARCHITECTURE.md | changed — Decision 4, §5 (rewritten and subdivided), §6, §7, §9, §13.2, §14, §15 |
| BUILD_PLAN.md | unchanged — version header only; the build steps this implies are handed to prompt 09 |
| CHANGELOG.md | changed — this entry, and the opening paragraph that still said "currently 1.17" |
| TODO.md | changed — prompt 03 marked done; prompt 09's inventory gains a section |

One finding, from prompt 03: **the visibility engine had no performance rules at all.** ChatGPT's review of 1.16 (finding 3) raised it, and the founder judged it the strongest technical point in the external reviews — everything routes through one engine, which is architecturally right, and §5 stated that rule in absolute terms while saying nothing about how often the engine runs or what a run costs.

**Why this was worth a version.** The load is real and the recent spec versions increased it: a reader on `POSTS_PER_PAGE_OPTIONS` = 60 is ordinary (SPEC §7.7.1), v1.16 extended SPEC §8.1's link-or-plain-text rule from commenters to post authors, mutual-friend context and reaction lists, and SPEC §11.5 renders mutual friends by name. A sixty-post page therefore asks the engine several hundred questions, most of them the same three questions about the same handful of people, whose answers cannot change while the page is being built.

**And the reason it is an architecture change rather than a tuning note:** the failure mode is not a crash but a four-second feed, and a four-second feed gets repaired by inlining a query into a template — which is precisely what Decision 4 exists to forbid, in a list, where a permission bug is least visible. **The performance gap was a threat to the architectural rule before it was a threat to speed.** Left unstated, the rule would have been broken in the field by someone doing an obviously sensible thing.

**SPEC was not touched, on purpose.** Caching is invisible to users; a wish to edit SPEC here would have been drift (prompt 08). **No new infrastructure either**: a request-scoped dictionary needs no Redis, and Redis is now recorded as rejected for this purpose at every scale, including the one where §13.2 eventually admits it for other things.

**The judgment call of the session — put to the founder and approved 2026-08-06.** Prompt 03 flagged the bulk-query question as possibly a redesign deserving its own prompt, and instructed that it be split rather than decided tired. It was adopted here instead, on an argument that turned out not to be about performance at all: **a queryset filter is a visibility decision**, so a list that builds its own filter has already broken Decision 4 — and before this version the engine offered no way to build a list any other way. The plural forms are what make the rule obeyable for lists, not merely faster. They cost one thing honestly: a rule expressed twice, in SQL and in Python, which is the drift this document warns about in five other places. That cost is paid by one equivalence test rather than waved away. The founder was given the reversal's consequence before deciding — pulling §5.4 would take the shape test with it, since that test's assertion (a 60-item page costs what a 20-item page costs) holds only if the bulk form exists — and confirmed it stays.

### ARCHITECTURE.md

(a) **§5 is rewritten and subdivided** into §5.1 the rule (unchanged text, now a named subsection), §5.2 what the rule costs, §5.3 request-scoped memoization, §5.4 the plural forms, §5.5 what is never cached. Nothing in the original rule was weakened; the four new subsections are all *inside* the module, and a caller that knows a cache or a batch exists is stated to be the wrong design.

(b) **§5.3 — memoization, scoped hard.** One HTTP request, populated on first use, discarded when the response is sent, never written to disk, never shared between requests or users. A table names what may be remembered and what it costs: the viewer's friend set (one query, ≤ `FRIEND_CAP` = 300 ids), their block set in both directions, their own profile hashtags (≤ `PROFILE_HASHTAG_MAX` = 10) — all per-viewer — plus per-pair connection status, mutual friends, profile tier and resolved contact card, plus the five answers themselves keyed on the full argument tuple. The per-viewer rows are the ones that do the work: the viewer's whole social position fits in three small queries, after which most of a page's questions are set membership and touch the database not at all. Three further rules, each closing a specific failure: the store is a `contextvars.ContextVar` set by middleware and cleared in a `finally` (a thread-local would break on async workers; an uncleared dictionary would leak into the next request on that thread); **every key begins with the viewer, and it is the viewer the engine was *called with*** — SPEC §9.5's preview-as substitutes a different viewer inside one request, so a key on the object alone would serve the owner's answers to the preview or the reverse, in the one feature built to show the owner somebody else's view; and **any write to a relation the engine reads discards the whole dictionary**, bluntly rather than selectively, because selective invalidation is how one gets a privacy bug nobody can reproduce. Finally, **no request, no memo**: cron jobs (§6) run uncached, deliberately, because a job runs for minutes and `post_follows` delivery re-asks the engine per recipient precisely so a mid-run block takes effect at once.

(c) **§5.4 — the plural forms.** Two shapes and no third: **one queryset per list**, owned by the engine (the feed, the Blog and Pinned tabs, discover, the friends page), with the caller owning ordering, folding and paging and nothing else; and **`profile_tiers(viewer, people)`**, one batch call over every name that will appear on the page. The batch call has a pleasing property worth recording: the single query that resolves FoF status for the non-friends also returns *which* mutual friends they share, which is exactly what SPEC §11.5's "knows Alice and Tom" and SPEC §9.2's basic tier need to render — one result, two requirements, neither computed twice. The singular functions of Decision 4 remain the item-level API (single-post view, notification delivery, the permission-checked image view, the data export) and, where possible, are implemented *as* the plural form over a set of one, so each rule has one implementation.

(d) **§5.5 — what is never cached, and the three ways it will be tried.** Cross-request caching of a visibility answer is forbidden, on SPEC's authority rather than preference: §11.3 requires the hashtag gate be evaluated live, §7.4 pairs a snapshot audience with *current* friendship, §5.4 makes blocks immediate. In each case a stale "yes" is a person seeing something the platform promised they could not, with nothing in any log. Three mechanisms are named so they are not proposed as obvious improvements — a module-level `functools.lru_cache` (the smallest-looking change and the worst: it lives for the life of the worker process), Django's cache framework on permission-checked pages or fragments, and a precomputed `visible_to` table. The third gets an explicit disambiguation: **`post_audience` is not an instance of it**, because SPEC §7.4 defines the posting-time snapshot as a stored fact and the engine still applies the live tests on top of it every read. Two clarifications keep the ban from being read too wide: it concerns visibility answers, not sessions or rate counters, and `select_related`/`prefetch_related` on an engine-supplied queryset are ordinary good practice.

(e) **Four tests in §9.** The first asserts a cost rather than a behaviour — the only place in the project that does — and it earns that under v1.18's own blast-radius rule, because what it protects is Decision 4 rather than the page's speed; the other three are ordinary correctness tests whose failures happen to be privacy failures. **The shape test**: render the same seeded feed at 20 and at 60 and assert the query counts are **equal**, and both under a stated ceiling. The equality is the durable assertion — it says cost does not grow with item count — and it is recorded that **the ceiling may be revised with a changelog line while the equality may not**. **The equivalence test**: the posts a list queryset returns are exactly the posts for which `can_see_post` returns true, over a fixture seeded with blocks, lapsed friendships, snapshot mismatches and live gates — this is the test that pays for having a plural form at all. **The viewer-in-the-key test** and **the flush-on-write test** guard §5.3's two failure modes. All four use `assertNumQueries` and the test client; no new dependency, and deliberately no wall-clock assertion, which would measure the machine rather than the code.

(f) **Decision 4 gains a paragraph** — the "one engine" principle is argued there, so the cost of that principle is named there too, with the point that a slow feed is Decision 4 failing in the field rather than losing an argument. A stale cross-reference in the same paragraph is corrected in passing: the engine's tests are in §9, not §11.

(g) **Smaller placements.** §6's intro states that jobs run outside any request and therefore uncached. §7 gains a security bullet, because the failure of a cached permission answer is silent and looks exactly like correct behaviour, and §7 is where a builder looks for what can leak. §13.2 records that when Redis eventually arrives on measurement, visibility answers still stay out of it. §14 gains four rejected rows (Redis for this purpose, `lru_cache`, the Django cache framework on per-viewer output, a precomputed visibility table). §15 gains item 5, recording the bulk forms as **APPROVED by founder 2026-08-06** with the reasoning that decided it, and recording "no new infrastructure" beside it as fact rather than as an open question.

(h) **Two terms are glossed in plain language where they first appear**, because this document's own header promises that "where a term of art is unavoidable, it is explained the first time it appears" and neither met it — a defect found the way such defects should be, by the founder reading the section and stopping at the word. **Memoization** (§5.3) is now defined as remembering an answer already worked out so the same question is never worked out twice; **asking in bulk** (§5.4) as handing the engine a whole set and getting all the answers back together, with the rules applied and the decision unchanged and only the number of questions differing. §5.2 also gains a paragraph on *why* several hundred queries are slow, since the intuitive answer is the wrong one: the cost is the per-query round trip, not the volume of data — which is also why the bulk form moves **less** data than the singular one, not more. That correction matters beyond readability, because "fewer requests but bigger ones" is the tradeoff a reader will assume is being made here, and it is not the tradeoff at all.

### BUILD_PLAN.md

Unchanged here by design (prompt 03's own instruction): Phase 4 already builds the engine and Phase 6 the feed, so this needs no new step. What it does need is for five existing places to stop describing a smaller engine than the architecture now specifies, and that is written up as a new **§N in `prompts/09-sync-arch-and-buildplan.md`**: Step 4.1 builds the plural forms and the memo middleware *with* the engine rather than retrofitting them after a slow feed; Step 4.2 gains three of the four new tests; Step 6.4 hosts the shape test and states that the feed's queryset comes from the engine; Step 7.1's name linking is fed by one `profile_tiers` call; and Appendix rule 2 — "all visibility decisions call the visibility engine — never inline" — gains a second sentence, because a builder reads "inline" as being about templates and the sharpest case is a view's own queryset filter.

### SPEC.md, README.md

Unchanged apart from the project-version header. SPEC's status is the deliberate one: this version added a caching rule and a bulk API, neither of which a user can observe, and prompt 03's own constraint was that wanting to edit SPEC here would be the signal of having drifted.

---

## 1.18 — 2026-08-04

| File | Status |
|---|---|
| README.md | changed — the 90-day line now states the 30-day backup window |
| SPEC.md | changed — nine sections plus §14 |
| ARCHITECTURE.md | changed — §3, §6, §7, §9, §10, §11, §15 |
| BUILD_PLAN.md | changed — §0.2, new §0.4, §2.4, §2.5, §5.1, §5.5, §5.6, §7.1, §14.2, §16.2, §17.3, Appendix rule 6 |
| CHANGELOG.md | changed — this entry |
| TODO.md | changed — prompt 02 marked done |

Thirteen items from the external reviews of 1.16 (prompt 02), eleven of them corrections and two founder decisions. **All thirteen landed; none was declined.** One was found partly already handled and is recorded as such below. The founder added a fourteenth item during the session — comments had no fold rule — and it is folded in here rather than deferred, being one constant and one clause.

**The two decisions.** (1) **The backup window is propagated into SPEC.** The reviewer reported the amendment as never approved; in fact ARCHITECTURE §15 item 1 has recorded "APPROVED by founder 2026-07-07" since that date, and what never happened was propagating it into SPEC, leaving the two documents contradicting each other on a user-facing promise. Approved again and propagated. The wording is deliberately *"deleted at 90 days, and purged from the last encrypted backup within 30 days after that"* rather than an arithmetic day-120 figure, which would invite a reader to compute an exact date that in truth depends on when the last backup ran. (2) **`COMMENT_LENGTH_MAX` is confirmed at 2,000** and loses its ✎ and its "asserted default" note — it was the only constant in §14 carrying an admission that nobody had agreed to it, and BUILD_PLAN §2.4's tripwire test will assert it.

**Two things deliberately *not* done here.** Reporting the abuse of multi-tag audience widening (a post tagged #jazz with nothing to do with jazz) is routed to prompt 05, which owns the vocabulary and §13.5. And §9.3's new address clause is written as a behavioural guarantee rather than as "UUIDs", to stay on the right side of the SPEC-versus-ARCHITECTURE boundary that prompt 08 will draw.

### SPEC.md

(a) **The deletion promise gets its honest form** (items 12, and Kimi finding 5): §7.5 gains the backup window; **§4.7's bare "full erasure" gains the caveat** — the sharpest case, because account deletion is where a user is likeliest to rely on the promise being literal, and §4.8's inactivity sweep inherits it by reference; §15.1 states that the privacy policy says so plainly; and **`BACKUP_RETENTION_DAYS` = 30 becomes a §14 constant**, on the principle that a number a user-facing promise rests on belongs in the authoritative document rather than only in the architecture. (b) **"Months" is defined out of existence** (item 2): §4.8's inactivity schedule becomes `INACTIVITY_DELETE_DAYS` = 730 and `INACTIVITY_WARN_DAYS` = 180/365/670/700, with the last two anchored 60 and 30 days before deletion so the intent survives the conversion, and a sentence stating that every interval is a count of days and never a calendar month. The same defect in §4.2's invite replenishment — "+1 per month", never noticed by any reviewer — is fixed in the same breath as `INVITE_REPLENISH_DAYS` = 30. (c) **The hashtag gate says what multiple tags mean** (item 11): §11.3 is rewritten so condition 3 is explicitly **existential** — one shared tag is enough — which corrects §11.3 to match §9.2, whose v1.16 wording already said "at least one", rather than deciding anything new. The consequence is stated in the same breath because it is a property of the design and not a side effect: **a post carrying ten tags reaches a wider FoF audience than a post carrying one**, so tagging is an audience control. §7.9's stated-visibility line, which did not cover it, now names every tag on the post and says "**any of**". (d) **Long comments fold** (founder-initiated): new `COMMENT_FOLD_CHARS` = 300 in §8.1, tighter than the feed's 500 because a comment is a guest in the post's space and a thread is many voices at once — at `COMMENT_LENGTH_MAX` = 2,000 a handful of unfolded comments would bury the post they belong to, which is the failure long-post folding already exists to prevent. Display-only, same mechanism as §7.7, with the distinct accessible names §16.3 requires for repeated controls. (e) **An address is never built from a name** (item 7): a new §9.3 bullet, stated behaviourally — an address survives a name change, and no address can be constructed by guessing a name — because display names are neither unique (§4.5) nor stable (§4.5.1), and SPEC is meant to stand on its own. Nothing was at risk in practice; ARCHITECTURE §4 and BUILD_PLAN rule 8 already said UUID. (f) **The friends-page filter gets a required label** (item 8): §11.6 requires "**Filter your friends**" as a visible label, never placeholder text, because a box labelled "Search" tells a user the platform has a search on a platform whose central promise is that it has none.

### ARCHITECTURE.md

(a) **Argon2id joins the §3 stack table** (item 1) — `Password hashing · Argon2id via django[argon2]` — and §7 stops calling it "the **only** addition … flagged for founder approval". It was never an addition anybody elected: SPEC §4.6.1 *requires* the slow memory-hard hash, and framing a mandatory dependency as an approved exception invites a later builder to treat it as optional. (b) **Test depth proportional to blast radius** (item 10): §9 gains the principle as a named second rule beside "test depth proportional to harm" — a helper that is the single source of a behaviour carries tests in proportion to how many surfaces it reaches, not to how much code it contains, which is why a thirty-line time helper carries the project's second-densest test. Two of its siblings gain named tests: the **name helper** (a boundary test on the "formerly" window) and the **theme selector** (a truth table whose point is that the viewer's override wins on someone else's profile — the contrast test proves each theme is *legible*, never that the right one was *chosen*). The **alt-text accessor was found already covered** by the existing template smoke tests and gets nothing; the reviewer's list was one item too long. (c) **The restore path is verified on two schedules** (item 9): §10 replaces "rehearsed once during setup" with a weekly automatic `verify_restore` job (new in §6 — restore into a scratch database, smoke query, email on failure, and check free disk first so a verification job can never fill it) plus a yearly manual rehearsal. Neither replaces the other, and it is recorded which one matters more: the automated job proves the server can read its own backups with credentials already in its own environment, while the scenario worth surviving is the one where the server is gone. (d) §10's approval flag is cleared and §15 item 1 records the propagation into SPEC; §6's job table and Decision 5 move to days; §11's cost table stops claiming free email tiers cover prototype volume.

### BUILD_PLAN.md

(a) **A standing browser and viewport matrix** (item 4), new **§0.4**: Safari (macOS + iOS), Chrome, Firefox; 320 / 375 / 768 / 1024 px — stated once as a rule the phase verifications refer to, rather than repeated in twenty steps. The cadence is deliberately cheap: one browser at one width per step, the full matrix at each *Phase milestone* only. 320 px was previously checked exactly once, in the Step 16.5 audit at the very end, though SPEC §16.3 requires reflow there from the first page that has a layout. Step 2.5 runs the full matrix once on its own, being where the base template and the single CSS file are born. (b) **The three law-file guards stop being presented as equivalent** (item 6): §2.4 now states each one's real strength — the tool deny rules are the lock (the harness refuses before the model's decision enters into it), the pre-commit hook **stops accidents and not determination** (`git commit --no-verify` skips it, and an agent that can run shell commands can pass that flag), and the tripwire test is the loud one. §0.2 rule 5 loses its claim that all three are locks. **The founder chose a fourth guard**, and chose the cheap one: the tripwire test also asserts the **SHA-256 checksum of each law document** against a committed `law_files.sha256`. A GitHub Actions workflow was considered and not adopted — it fires only after a push, needs branch protection plus a required status check to block anything at all, and adds a CI surface to a project that has none; the checksum test fires on the founder's own machine at the next step. Two founder-facing details are spelled out because leaving them implicit would strand a non-developer: the test's failure message **is** the reminder and prints the one `shasum` command that re-blesses the file, and the pre-commit hook will refuse that commit by design — the founder passes `--no-verify` themselves, deliberately, which is precisely the act guard 2 exists to require. (c) **Email headroom is stated honestly** (item 3): §5.1 stops implying the free 100 emails/month covers the prototype and counts what launch actually sends — two emails per new account, one per reset or security event, four per dormant account over two years, and **optional email notifications (SPEC §12.5) unbounded per user by design** — landing at roughly $15/month for 10,000 emails as the next step up. Postmark remains the recommendation; the transactional-only ethos is why it was picked, not the free tier. §5.5's verification gains what it genuinely lacked: **independent SPF and DKIM lookups** beside the existing DMARC one, and confirmation that **the provider's dashboard shows the message delivered** rather than merely that the domain verified. (d) **The overlay ban becomes mechanical** (item 5): §16.2's zero-foreign-requests check now names the vendors by domain — `accessibe.com`, `acsbapp.com`, `userway.org`, `equalweb.com`, `audioeye.com`, `reciteme.com` — plus the classic silent arrivals (Google Fonts, CDN asset hosts, analytics), so the check no longer depends on the founder recognizing a domain. A hit on the first list is worse than an ordinary tracking-ban violation: it means something installed the one class of tool this project bans three times over, in good faith. (e) Smaller: Step 5.6 builds `verify_restore` and Step 17.3's runbook gains the yearly manual rehearsal and a last-success check on both jobs; Step 7.1 gains comment folding; Step 14.2's inactivity sweep moves to days; Step 2.5 and Appendix rule 6 drop the argon2 exception clause.

### README.md

The concrete list's "every post and comment auto-deleted after 90 days" gains "(and purged from the last encrypted backup within 30 days after that)", and the "On the 90 days, precisely" paragraph gains the same caveat in prose. Claiming instantaneous total erasure while running nightly backups would be untrue, and this is the document outsiders read first.

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
