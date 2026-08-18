# TODO — WeeBee design work

Tracker for the design conversations still to be held. Each numbered item has a
self-contained prompt file in `prompts/`, written to be pasted into a **fresh**
session (BUILD_PLAN §0.2 rule 4: long chats degrade; prompts carry their own context).

**This file was written at project version 1.16; the project is now at 1.23.** Under the
scheme prompt 01 introduced, the version number belongs to the whole project, not to
individual files.

---

## How to use this file

1. Pick the next prompt whose dependencies are met.
2. Open a fresh session in this repo and paste the prompt file's contents.
3. When the conversation ends, update the **Status** and **Landed in** columns below,
   and confirm the session wrote its CHANGELOG.md entry.
4. A prompt that ends in "no change" is still *done* — record the decision and its
   reasons in-document, per README's rule that rejected suggestions keep their reasons.
5. **This file and `prompts/` are working files, outside the versioned record** (CHANGELOG's
   preamble, v1.23). They get no row in an entry's status table; a session says in prose
   what it did to them. Changing them is not a version bump.
6. **The queue has a second inlet now (v1.23):** a *stop note* from a build session that hit
   a wall. It lands in the stopped-steps table below rather than in `prompts/`, and it is
   already self-contained enough to open a design session with — BUILD_PLAN §0.7.

Status values: `not run` · `in progress` · `done` · `deferred` · `dropped`

---

## The queue

| # | Prompt | Touches | Depends on | Status | Landed in |
|---|---|---|---|---|---|
| 01 | [Changelog & project-wide versioning](prompts/01-changelog-and-versioning.md) | all four docs, new CHANGELOG.md | — | done | 1.17 |
| 02 | [Small corrections & open items](prompts/02-small-corrections.md) | SPEC, ARCHITECTURE, BUILD_PLAN, README | 01 | done | 1.18 |
| 03 | [Visibility engine performance](prompts/03-visibility-engine-performance.md) | ARCHITECTURE §5, §9 | 01 | done | 1.19 |
| 04 | [Availability & DDoS posture](prompts/04-availability-and-ddos.md) | ARCHITECTURE §4, §6, §7, §8, §10, §11, §13, §14, §15; BUILD_PLAN §5, §15, §16, §17 | 01 | done | 1.20 |
| 05 | [Hashtag vocabulary operations](prompts/05-hashtag-vocabulary-operations.md) | SPEC §11.2, §13.5, §13.2, §7.9, §14, §17; ARCHITECTURE §4; BUILD_PLAN §10, §13.1, §17.3 | 01 | done | 1.21 |
| 06 | [Accessibility: regression & the admin](prompts/06-accessibility-regression.md) | SPEC §16.1, §16.5, §17; ARCHITECTURE §3.8, §9, §15; BUILD_PLAN §0.1, §0.3, §0.5, §2.5, §8.2, §15.2, §15.3, §16.5, §17.3, Appendix | 01 | done | 1.22 |
| 07 | [How documents change during the build](prompts/07-design-review-mode.md) | BUILD_PLAN §0.2 + §2.4, all four headers, CHANGELOG | 01 | done | 1.23 |
| 08 | [Document boundaries: SPEC vs ARCHITECTURE](prompts/08-document-boundaries.md) | SPEC, ARCHITECTURE | 01 | not run | |
| 10 | [Reactions: look, lifecycle, expiry](prompts/10-reactions.md) | SPEC §8.2, §7.6, §9.7, §14; ARCHITECTURE §4, §6 | 01 | not run | |
| 11 | [Three internal contradictions in SPEC](prompts/11-spec-contradictions.md) | SPEC §9.1/§5.2, §8.1/§5.4, §4.6.1/§12.3; ARCHITECTURE §5 | 01 | not run | |
| 12 | [What a ban actually does](prompts/12-moderation-outcomes.md) | SPEC §13.2, §4.7, §12 | 01 | not run | |
| 09 | [The sync: ARCHITECTURE + BUILD_PLAN to current SPEC](prompts/09-sync-arch-and-buildplan.md) | ARCHITECTURE, BUILD_PLAN | **02–08, 10–12** | not run | |

**Run 09 last.** Prompts 02–08 and 10–12 may each amend SPEC and ARCHITECTURE; syncing
BUILD_PLAN once against a settled SPEC means writing those build steps a single time.

**Prompt 03 handed BUILD_PLAN work to 09 rather than doing it (1.19).** ARCHITECTURE §5 now
specifies a larger engine than BUILD_PLAN describes — plural forms, a request-scoped memo,
four new tests. No new phase or step is needed; five existing places need updating, and they
are itemized as a new **§N** in `prompts/09-sync-arch-and-buildplan.md` so the sync session
does not have to reconstruct them from CHANGELOG.

**Prompt 03's one open call is settled.** The bulk (plural) engine API was adopted rather than
split into a later prompt — **approved by founder 2026-08-06**, recorded with its reasoning in
ARCHITECTURE §15 item 5. Prompt 09 writes the Phase 4 and Phase 6 steps from it without
re-opening the question.

**Prompt 04 handed BUILD_PLAN work to nobody — it wrote its own steps (1.20).** Unlike prompt 03,
04's build steps were unambiguous and land in existing phases (5.2, 5.4, 5.6, new 5.7, 15.1,
new 16.6, 17.3, Appendix rule 7). Prompt 09 inherits **one** item from it, below.

**New for prompt 08 (from 1.20).** ARCHITECTURE §7.3 adds an unauthenticated route, `/healthz`,
and argues it is not a *page* and therefore does not contradict SPEC §2's "no public pages
except login/registration/invite-acceptance." That argument is written down in ARCHITECTURE
rather than acted on in SPEC. **08 decides whether SPEC §2 should name the route**, which is a
boundary question of exactly the kind 08 owns. Note while you are there that §2's list is
already slightly narrower than the built system: the privacy policy and accessibility
statement are linked from login (BUILD_PLAN §15.1, §15.2) and are therefore also reachable
logged out.

**New for prompt 09 (from 1.20) — nothing to decide, one thing to leave alone.** External
uptime/heartbeat monitoring is **deferred with intent to build**: the founder's position is
email alerts for launch and the watchdog built out if the platform actually gets used
(ARCHITECTURE §15 item 6). It has deliberately **no numbered build step**, because its trigger
is the platform being used rather than a phase being reached; it lives instead as section 11
of the operator runbook (BUILD_PLAN §17.3), alongside the yearly restore rehearsal, which is
the same shape of standing item. **09 should not relocate it into a phase.** Everything it will
need in the application — `/healthz`, `job_runs`, `check_health` — is already built at Step
5.7, so the future work is a signup and two monitors, not code.

**New for prompt 09 (from 1.21) — one small sync gap, noticed in passing.** SPEC §13.2 has
required a **short free-text note to the operator** on profile reports since v1.16, and v1.21
extends the same form to posts and comments. ARCHITECTURE §4's `reports` row lists *reporter,
target, category, frozen copy, status, purge-by date* — **no note column**. The `category`
column was already there (which is why v1.21 needed no schema change for report reasons); the
note appears to have been missed when §13.2 was written a version later. Check it and add it.

**New for prompt 09 (from 1.22) — one page-list sync, and one thing to leave alone.** Step 2.5
now builds the **template smoke tests**, whose page list must grow with every phase that adds a
page (Appendix rule 9). When 09 syncs BUILD_PLAN against a settled SPEC, check that the phases
it touches say so where a new page type appears — the feed, the composers, the four profile
tabs, discover, the contact card, settings, and the error and empty states. **Leave the
accessibility tester where it is:** Step 15.3 is a `[FOUNDER]` booking step deliberately placed
in Phase 15 and told to start during Phase 13, and the re-audit rule it serves lives in the
operator runbook (§17.3 section 13) rather than in a phase — the same shape as the watchdog,
and for the same reason: its trigger is the platform changing, not a step being reached.

**New for prompt 09 (from 1.23) — two sentences to carry into ARCHITECTURE, and two things
to leave alone.** BUILD_PLAN Appendix rule 4 now requires **every test to cite the SPEC or
ARCHITECTURE section it enforces**, by number, somewhere a plain text search will find it —
that is what makes the new §0.6 conformance check possible, and **ARCHITECTURE §9 should say
it too**, since §9 is where this project describes what its tests are for. While there,
§9 may want one line acknowledging §0.6's stated limit: none of these tests catches an
assertion that is weaker than the rule it cites. **Leave two things where they are.** SPEC
Appendix A's "reviewed and confirmed by the founder on 2026-07-07" stays as written — it is
a record of a specific act on ten specific defaults, not a status line, and the v1.23
approval scheme does not replace it. And the **stopped-steps table above stays in this file**
rather than moving into BUILD_PLAN: BUILD_PLAN is a law file locked during build sessions,
and a queue that cannot be written to during a build is not a queue.

**Do not start Phase 2 of BUILD_PLAN until 09 is done.** `BIO_CHANGE_COOLDOWN_HOURS` and
`BIO_EDIT_GRACE_MINUTES`, which SPEC §14 marks **retired v1.16**, are still live
instructions in **five** places: ARCHITECTURE §4 (`profiles`, where they are *columns*),
ARCHITECTURE §4 (`rate_counters`), ARCHITECTURE **§7.1** (inside a security argument — §7 was subdivided in 1.20, and the retired constants are in the first subsection),
BUILD_PLAN §8.1, and BUILD_PLAN §13.4. A build session following those files today would
write the wrong mechanism. This file previously named only two of the five.

---

## Stopped build steps

Empty until the build starts, and it should stay short. When an `[AI]` build step cannot be
done as written, the session prints a **stop note** (BUILD_PLAN §0.7) and stops; paste it
into a row here with the date. That is the whole of the founder's part — thirty seconds,
and it turns "the AI stopped" into a queued design conversation instead of a dead end.

Before queuing one, run §0.7's thirty-second check: search the document for the quoted
sentence. Not found → the model guessed; that is not a stop, and the fix is to re-run the
step in a fresh chat (BUILD_PLAN §0.2 rule 6) rather than to open a design session.

| Date | Step | The sentence in the way | Resolved into | Status |
|---|---|---|---|---|
| — | — | — | — | *(none yet)* |

**Resolved into** is one of: a SPEC/ARCHITECTURE change (name the version), a new build step
(name it — Step 6.2a and so on), a corrected prompt in deliverable (d), or nothing (the
model was confused). Then re-run the step from its prompt and mark the row done.

---

## Appendix A — Where the queue came from

Version 1.16 of README.md, SPEC.md, ARCHITECTURE.md and BUILD_PLAN.md was reviewed by
ChatGPT (`1.16_ChatGPT_review.md`, 8 findings), DeepSeek (`1.16_DeepSeek_review.md`,
27 findings) and Kimi (`1.16_Kimi_review.md`, 12 findings — see Appendix B). Every finding
was checked against the actual documents. The triage below records what happened to each
one, so no finding is silently dropped and none needs re-litigating.

### Findings that became prompts

| Finding | Source | Prompt |
|---|---|---|
| Version history hard to navigate → CHANGELOG.md | ChatGPT 8 | 01 |
| `argon2-cffi` framed as an exception, not part of the stack | DeepSeek 13 | 02 |
| "Months" in the inactivity sweep is undefined | DeepSeek 20 | 02 |
| Email provider free tier is thinner than the launch needs | DeepSeek 21 | 02 |
| SPF/DKIM verification steps (DMARC's are already there) | DeepSeek 11 (partly) | 02 |
| Browser / viewport test matrix is one phone | DeepSeek 19 | 02 |
| Accessibility-overlay ban is stated but never tested | DeepSeek 26 | 02 |
| Pre-commit hook is bypassable with `--no-verify` | DeepSeek 16 | 02 |
| Profile URLs use UUID — true, but SPEC never says so | DeepSeek 2 | 02 |
| Friends-list filter will read as "search" | DeepSeek 7 | 02 |
| Restore rehearsed twice, never again | DeepSeek 18 | 02 |
| Shared helpers are single points of correctness | ChatGPT 6 | 02 |
| Visibility engine may issue N×M queries; needs request-scoped caching | ChatGPT 3 | 03 |
| Cloudflare proxy ban leaves no DDoS mitigation | DeepSeek 9 | 04 — **done in 1.20**; the finding itself was wrong (§13.3 already answered it) but checking it exposed that §7 said nothing about availability at all |
| Hashtag vocabulary makes the operator a single point of failure | DeepSeek 3 | 05 — **done in 1.21**; the finding was right and **both** proposed fixes were wrong, and both are now recorded as rejected in SPEC §11.2.1 so they do not return as new. The real answers were a good starter list and **search aliases**, which turn a declined synonym into a permanent fix |
| Accessibility is audited once, never regression-tested | DeepSeek 22 | 06 — **done in 1.22**; the finding was right, and checking it found a defect the reviewer had missed: ARCHITECTURE §9's **template smoke tests had no build step at all** and existed only inside the pre-launch audit. Conformance now runs on three clocks (SPEC §16.5), the scan moves to a milestone cadence, and the ongoing duty lives in the runbook |
| Django admin WCAG exception is a hedge, not a decision | DeepSeek 12 | 06 — **done in 1.22**; "a cop-out" was too strong, but the sentence stated no obligation and could be satisfied by doing nothing. Settled as a **bounded commitment** (SPEC §16.1.1): a named subset over §13's four weekly surfaces, everything else out of scope with the §3.1-leg-2 reason stated, and the future-operator remedy named |
| AI cannot even *propose* a document correction | ChatGPT 2 | 07 — **done in 1.23**; the finding was right about the gap and wrong about its shape. The locks were stronger than the reviewer credited; what was missing was that **nothing existed on the other side of the stop**. Answered by the **stop note** (BUILD_PLAN §0.7), not by the proposed "Design Review Mode" — design sessions have run here for twenty-two versions and needed a route in, not a switch |
| No "discovery loop" for steps found missing mid-build | DeepSeek 14 | 07 — **done in 1.23**; granted. Insert with a letter at the point of need (Step 6.2a), **never renumber** — renumbering falsifies git commit messages, CHANGELOG references and prompt filenames, which are history. The founder writes the step, it gets its own ✅, and the preceding verification is re-run. It is one of the four things a stop note resolves into, not a separate mechanism |
| AI won't recognize when it needs to change a law file | DeepSeek 15 | 07 — **done in 1.23**, and it is the finding this session could least fully answer. The half that is answerable is coverage: **new BUILD_PLAN §0.6** has the founder read two columns of section numbers at each phase milestone, which catches a SPEC clause that got no code and therefore no test. The half that is not is stated in the document rather than papered over — **a test that cites the right section and asserts the wrong thing is caught by nothing here** |
| SPEC is absorbing architectural concerns | ChatGPT 1 | 08 |
| Decisions justified as "easier for AI" will age badly | ChatGPT 4 | 08 |
| Missing build step for the friends page | DeepSeek 24 | 09 |
| `REQUEST_HOLD_AFTER_PROFILE_CHANGE_HOURS` unimplemented | DeepSeek 25 | 09 |

### Findings assessed and closed — no prompt needed

Each was checked against the document text; the reviewer's concern is already answered
where noted. Recorded here so they are not raised again as new.

- **No-reach has a "weasel clause"** (DeepSeek 5). SPEC §1.2 already states this at
  length, unprompted — the retyping path is named, and the paragraph explains why it
  stays self-limiting (full price per hop, 30-person fan-out, no measurement). The
  reviewer restated the document's own argument as an objection to it.
- **`COMMENT_LENGTH_MAX` not set in BUILD_PLAN** (DeepSeek 23). Wrong: BUILD_PLAN §2.2
  is "every SPEC §14 constant, named exactly as in SPEC," and SPEC §14 carries the
  value 2,000. *Residual, folded into prompt 02:* SPEC's own history records the value
  as "asserted, not yet discussed."
- **Preformatted posts can force horizontal scroll on every reader** (DeepSeek 4).
  Already closed in v1.16(j): §16.3 requires the scroll be contained inside the post.
  Abusive ASCII shapes are a moderation matter (§13.2), not a spec hole.
- **Widening a post's audience exposes existing comments** (DeepSeek 6). SPEC §7.8
  already warns the author in the editor *and* notifies every existing commenter
  through the follow channel, explicitly so they may delete. The extra "remove my
  comment" button is a marginal convenience; noted, not adopted.
- **One-server assumption is fragile** (DeepSeek 8). ARCHITECTURE §13 exists precisely
  to answer this and was written deliberately. Moving it to an appendix is a
  presentation preference, not a defect.
- **Backup retention conflicts with GDPR** (DeepSeek 10). ARCHITECTURE §10 already
  adopts the standard resolution — encrypted, off-server, 30 days, stated in the
  privacy policy. *Residual, folded into prompt 02:* §10 flags its own amendment as
  awaiting founder approval into SPEC, and that approval has never been given.
- **Accessibility is manual only, with no automated scanning** (DeepSeek 17). Wrong:
  BUILD_PLAN §16.5 pass 1 runs an axe/`pa11y` scan, ARCHITECTURE §9 specifies template
  smoke tests and a contrast test over every theme, and passes 2–4 are the keyboard,
  screen-reader and zoom checks the reviewer said were absent. *Residual, and it was
  DeepSeek 22's point rather than 17's — **closed in 1.22**:* all of it ran once, as a
  pre-launch gate. One correction to the record while closing it: of the two automated
  tests, only the contrast test was genuinely continuous. **The smoke tests were specified
  and never built**, which is why 1.22 gave them Step 2.5 rather than merely "saying so".
- **DMARC should start at `p=none` and be verified with a lookup tool** (DeepSeek 11).
  BUILD_PLAN §5.5 already says both, including the MXToolbox check. *Residual, minor:*
  SPF and DKIM get no independent verification step.
- **Nothing stops a query computing an unread count** (DeepSeek 27). Conflates a
  per-row `read` boolean (needed to render a notification list at all) with a badge.
  BUILD_PLAN Appendix rule 12 already bans every counter by name.
- **BUILD_PLAN is so prescriptive it constrains better models** (ChatGPT 7). The
  reviewer says it is a conscious tradeoff. It is. Prescription is what makes a
  non-developer able to verify each step.
- **Long critical path before anything is demonstrable** (ChatGPT 5). Phase 5 already
  is that milestone — a real domain, real HTTPS, real email, deliberately placed before
  fourteen phases of feature work.
- **Feedback mechanism is awkward for a GitHub repo** (DeepSeek 1). README already
  states this is not an open review process and that pull requests are unwanted. A
  CONTRIBUTING.md would advertise a process that does not exist.

### Open questions parked for later

- **`HASHTAG_VOCAB` seed content — still parked, now with a brief (1.21).** Prompt 05
  settled the workflow; the vocabulary itself still has to be written, and it remains
  content work rather than design work. It is now a numbered build step, **BUILD_PLAN
  §10.1a [FOUNDER]**, with the founder's decisions attached: **~300 tags, hand-written
  (not imported from a public taxonomy), across roughly twenty areas of life, every entry
  weighted toward things people do with other people offline**, and **each tag's search
  aliases written at the same desk sitting** — a rejected synonym becomes an alias rather
  than being lost. SPEC deliberately states no size target (§11.2.1); this is the only
  place the number lives. Do it during Phase 10.
- **Can an LLM help draft the vocabulary? (new, parked 2026-08-17.)** The founder's
  question on adopting aliases. Worth trying: drafting ~300 tags and their synonym sets
  by hand is the single largest piece of content work in the project. It is **not blocked
  by SPEC §1.3's "the platform never infers"** — that rule governs what the running
  platform does with user data, and this is an operator writing a static word list at a
  desk, with no user, no user data and no inference about anybody. The conditions, so the
  trial stays honest: **the founder approves every entry**, nothing is loaded unread, and
  §10.1a's "done when" is the acceptance bar (search ten interests the way five different
  people would phrase them; land on a tag every time). Recorded in BUILD_PLAN §10.1a.
- **The starting page list for the template smoke tests (new, parked 2026-08-18).** Not a
  design question — a five-minute build question, recorded so it is not forgotten. Step 2.5
  builds the tests against login, reset and lockout, and Appendix rule 9 says every later
  step adds its pages. Nobody has written the *list*, and the failure mode is silent: a
  suite whose page list stops growing passes forever while checking nothing. Worth one
  glance at each phase milestone (BUILD_PLAN §0.5), where the scan already runs.
- **Constant values as a whole.** README §1 invites review of every cap. No reviewer
  engaged with the numbers. Still open.
- **README §3's pager question is answered as of 1.20** — *"what does a person who has
  carried a pager know that this plan forgot? (Monitoring, alerting, failure recovery, the
  2 a.m. scenarios.)"* No reviewer answered it; prompt 04 did. ARCHITECTURE §7.2–§7.4 and
  §11.1 are the answer, and BUILD_PLAN §5.7, §16.6 and §17.3 are how it gets built. Recorded
  here so the question is not re-asked as though still open.

---

## Appendix B — the Kimi review of 1.16

`1.16_Kimi_review.md` arrived after the queue above was built. All 12 findings were checked
against the document text; **none was factually wrong**, which was not true of the other two
reviews. Eight raise something neither earlier reviewer mentioned.

The calibration note worth keeping: **ChatGPT and DeepSeek both explicitly certified that no
internal contradictions existed** ("I didn't find an outright contradiction among the current
versions"; "The documents are internally consistent"). Kimi found three, all verified. A
reviewer's summary judgment is not evidence.

| # | Finding | Verdict | Routed to |
|---|---|---|---|
| 1 | BUILD_PLAN/ARCHITECTURE behind SPEC 1.16 | extends DeepSeek 24, 25 | 09 §A — the retired constants are in **five** places, not the two this file used to name |
| 2 | Request card: "one component" (§9.1) vs snapshot (§5.2) | new | 11 |
| 3 | §8.1 "exactly" vs §5.4 blocks; no `can_see_comment` | new | 11, then 09 §L |
| 4 | Security emails: §4.6.1 timestamps vs §12.3 "no timestamp" | new | 11 |
| 5 | §4.7 "full erasure" ignores the 30-day backup window | duplicate of DeepSeek 10 | 02 item 12 — sharpens the target to §4.7 |
| 6 | `friend_requests` lacks snapshot columns | new to the reviews | already covered by 09 §G |
| 7 | `images` lacks a gallery-order column | new | 09 §K |
| 8 | "Ban" (and "warn") never defined, §13.2 | new | 12 |
| 9 | The founder cannot interpret a screen reader | extends DeepSeek 17, 22 | 06 item 5 — **done in 1.22**. SPEC §16.5.1 defines *qualified* (a daily screen-reader user, paid, before a professional auditor) and BUILD_PLAN §15.3 books the person from Phase 13 — the decision's real cost was scheduling, not wording |
| 10 | Tripwire paradox; guards are tool-specific | extends DeepSeek 16 | 07 item 8 — **done in 1.23**. Both halves were right. §2.4 now defines the legitimate cap-raising sequence (SPEC §14 → `constants.py` → tripwire → checksums, one founder commit, `--no-verify`) and makes a constants failure at any other time a real alarm; and it says plainly that guard 1 does not survive a change of tool, guard 2 does not survive `--no-verify` or a fresh clone, and **layer 4 is what is actually being relied on** |
| 11 | Reactions on pinned posts never expire | new | 10 |
| 12 | Hashtag gate ambiguous for multi-tagged posts | new | 02 item 11 — **founder ruled: any shared tag**; abuse reporting → 05 item 7 |

Two findings needed no new work: **#6** was already in prompt 09's inventory (§G asks
ARCHITECTURE §4 for the snapshot fields including a stored image copy), and most of **#1**
was too — 09's inventory was built from SPEC directly rather than from reviewer findings, so
it already covered the four-tab profile, the friends page, the stated-visibility line, the
avatar picker and the pending-request expiry.
