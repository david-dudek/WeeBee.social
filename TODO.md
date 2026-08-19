# TODO — WeeBee design work

Tracker for the design conversations still to be held. Each numbered item has a
self-contained prompt file in `prompts/`, written to be pasted into a **fresh**
session (BUILD_PLAN §0.2 rule 4: long chats degrade; prompts carry their own context).

**This file was written at project version 1.16; the project is now at 1.26.** Under the
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
| 08 | [Document boundaries: SPEC vs ARCHITECTURE](prompts/08-document-boundaries.md) | SPEC, ARCHITECTURE, BUILD_PLAN | 01 | done | 1.24 |
| 10 | [Reactions: look, lifecycle, expiry](prompts/10-reactions.md) | SPEC §8.2, §7.6, §9.7, §14; ARCHITECTURE §4, §6 | 01 | done | 1.25 |
| 11 | [Three internal contradictions in SPEC](prompts/11-spec-contradictions.md) | SPEC §9.1/§5.2, §7.9, §8.1, §8.2, §12.3, §7.5.1, §4.8; ARCHITECTURE Decision 4, §5, §9, §15 | 01 | done | 1.26 |
| 12 | [What a ban actually does](prompts/12-moderation-outcomes.md) | SPEC §13.2 (new §13.2.1), §4.7, §4.8, §9.3, §12.1, §13.4 | 01 | done | 1.27 |
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

**Prompt 08's `/healthz` question is answered (1.24) — founder decision 2026-08-18: SPEC §2
does not name the route.** §2's rule is about *pages*, and an endpoint returning the literal
body `ok` — no HTML, no template, no theme, nothing about any user — is not one. SPEC §2 gained
a **pointer** to ARCHITECTURE §7.3 rather than a restatement of the argument, which is the
citation convention (SPEC §18) applied to the first case that arose under it. ARCHITECTURE §7.3
and §15 item 6 now record the question as closed, and §7.3 states the test a *future*
unauthenticated route has to meet rather than leaving this one as a precedent.

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

**New for prompt 09 (from 1.27) — one new prompt section, and the answer to the question
prompt 12 was told to settle.** Prompt 12 defined the three moderation outcomes in a new
SPEC §13.2.1 and **wrote nothing to ARCHITECTURE or BUILD_PLAN**, on the 1.19/1.25/1.26
precedent. Everything it hands over is written out as **§Q of
`prompts/09-sync-arch-and-buildplan.md`**.

- **Yes, ARCHITECTURE needs an account-state column** — this was the open question the prompt
  asked to have settled here. ARCHITECTURE §4's `users` row lists *"deactivation/deletion-grace
  state"* and nothing else; it needs a **banned flag with the date of each ban and each
  reversal**. The constraint that matters is not the column but where it is read: **a banned
  account is invisible by the same route a deactivated one is**, so this is one more input to
  the visibility engine (§5), never a second hiding path. A builder who writes a parallel
  "hide banned users" filter has defeated Decision 4 in exactly the way 1.26's missing
  `can_see_comment` did.
- **A `warnings` table does not exist and SPEC §13.4 now requires one** — date, account,
  operator text, originating report. This is the **second** thing 09 must add to a moderation
  table; the missing `note` column on `reports` (from 1.21, above) is the other, and they
  should land together.
- **Four BUILD_PLAN places, one of which has no step at all.** Step 13.3 (the console's
  ban/warn actions, per-account and never a bulk list action), Step 14.2 (`inactivity_sweep`
  gains two branches for a banned account), Step 14.4 (export stays reachable from a banned
  session — the reason the login is not refused), and **the banned-session middleware, which
  no step anywhere describes.** That last one is the likely miss: everything else on the list
  is a column or a form.
- **One rule that is not about banning.** SPEC §4.7 now states that an outstanding invitation
  cannot be redeemed while the sending account is invisible. That has always been true of
  deactivation and was never written down; invite redemption and Step 14.1 both need it.

**New for prompt 09 (from 1.26) — three items, all itemized in the prompt file.** Prompt 11
resolved three SPEC contradictions and amended ARCHITECTURE §5 where one of them required it;
**BUILD_PLAN was deliberately left alone**, on the 1.19 and 1.25 precedent. Two of the three
are **errors rather than gaps**, in the sense §A uses — a build session following BUILD_PLAN
today writes the wrong thing:

- **Step 12.5** repeats *"Emails carry no timestamp at all"*. SPEC §12.3 was narrowed to
  **relative** ages, because the old wording collided with SPEC §4.6.1 and would have stripped
  the deletion date out of an inactivity warning. Written out as a new **§P** in the prompt file.
- **Step 4.1** names *"the five functions of ARCHITECTURE Decision 4"* and lists them. There
  are now **six** — `can_see_comment` joined them, because a block makes the comment audience a
  strict subset of the post audience. **§L** of the prompt file, which was written expecting
  exactly this handover, now carries the decision instead of the question. Step 4.2 gains the
  test case and Step 7.1 gains the engine-owned comment queryset.
- **§G is narrowed rather than changed.** The `friend_requests` snapshot columns are for the
  **photo and the short bio only** — SPEC §9.1 now carries the frozen/live field table and
  calls it a security boundary, and snapshotting the name or the mutual friends would break
  SPEC §4.5.1 and §5.4.

**New for prompt 09 (from 1.25) — six items, all itemized in the prompt file.** Prompt 10
amended SPEC §8.2–§8.2.3 and ARCHITECTURE §4 and §6 and **deliberately left BUILD_PLAN
alone**, on the 1.19 precedent: the build work lands in existing steps and is written once,
by 09. The six are written out as **§O of `prompts/09-sync-arch-and-buildplan.md`** so the
sync session does not have to reconstruct them — Step 7.2 (which is two lines describing
three subsections), the `expire_content` sweep by a reaction's own timestamp, `REACTION_SET`
being a **table** and not a `constants.py` entry, the admin editor's retire-never-delete
rule, one clause in Step 12.4, and a numbered content step for the phrases that has never
existed. **Two of them are errors rather than gaps**, in the sense §A uses: a constants step
that puts `REACTION_SET` in `constants.py` and an `expire_content` written from the cascade
alone are both wrong today, and the second fails only on the pinned post, which ordinary seed
data will never contain.

**Found while there, flagged and not fixed (1.25).** `THEME_SET` and `DEFAULT_AVATAR_SET` are
operator-curated and both get an admin editor at BUILD_PLAN Step 13.3, but ARCHITECTURE §4
gives neither a table and §3.5 describes a theme as a named set of CSS variables. **Whether a
theme is a database row or a file the operator deploys is a real question**, and answering it
was outside prompt 10. ARCHITECTURE §4's new carve-out paragraph flags it; 09 should either
answer it or hand it on, so that a builder reaching Step 13.3 does not resolve it by guessing.

**Carried with item 6 above, for the founder rather than for the sync.** SPEC §8.2.3 states
six criteria a reaction phrase must pass and deliberately does **not** freeze the list —
same division as `HASHTAG_VOCAB` (§11.2.1), where the criteria are spec and the writing is
content work. The recommendation on the current six is recorded in §8.2.3 with its reasoning:
**drop "Ha!"** (laughing *with* and laughing *at* are the same three characters, and the
recipient cannot tell which they were sent) and **add "Thank you!"**. It needs no decision
now; it needs to be in front of the founder at the moment the list is actually written.

**One error in prompt 10 itself, recorded so nobody hunts for it.** It twice asks for enough
detail "for Phase 8 to be built." Reactions are **Phase 7**, Step 7.2; Phase 8 is Profile
Pages and Theming. Harmless — the work landed against Phase 7 — but the prompt file was not
edited, since `prompts/` records what a session was asked.

**New for prompt 09 (from 1.24) — one stale citation pair, left alone on purpose.** Both
ARCHITECTURE and BUILD_PLAN still open with a **`Companion to:`** line citing *per-file* SPEC
and ARCHITECTURE version numbers — "SPEC.md v1.15", "ARCHITECTURE.md v1.7" — under a scheme that
1.17 retired in favour of one project version per document header. Prompt 08 deliberately did
**not** clear them: right now they carry honest information about how far behind those two
documents are, and deleting that before the sync would make a stale document look current.
**09 clears them when the sync is actually done**, replacing each with a plain "deliverable (b)
/ (c) per SPEC §18" and letting the version header carry the rest.

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
| SPEC is absorbing architectural concerns | ChatGPT 1 | 08 — **done in 1.24**; the finding was right that the documents repeat each other and wrong about what to do. The proposed split was tested on its own four passages and **three did not survive it**: §7.8 invariant 4 already sits on the right side of the line, §4.6.1 was partly misread (SPEC never specified hashed codes or attempt caps), and §7.9's "one string per post" is the bullet's privacy rule in implementation clothing. The remedy was **already the house convention** — ARCHITECTURE cites SPEC 148 times, SPEC's 679 references never leave SPEC unlabelled. What was actually broken was different: ARCHITECTURE's bare `§x` collided with its own section numbers and **14 references resolved into the wrong document**. Fixed by relabelling 50 references and writing the convention down (SPEC §18) |
| Decisions justified as "easier for AI" will age badly | ChatGPT 4 | 08 — **done in 1.24**; right, and smaller than it looked. **"Sub-Fable" appeared exactly twice**, both in ARCHITECTURE (Decision 1 reason 4, §3.1 leg 3); SPEC §2 already used the durable phrasing. Both now lead with the reason that holds whoever writes the code and **keep the AI reason named rather than removed** — scrubbing it would make the documents less honest, which is this project's objection to every other cosmetic tidy. README and BUILD_PLAN's tool names left alone: a description of method and an install instruction, not a justification |
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
- **Does SPEC's Purpose line promise too much? (new, parked 2026-08-18 by prompt 08.)** SPEC's
  header says *"a developer or an AI coding model with no access to prior conversations must be
  able to build from this document alone"* — and that sentence is the reason SPEC carries
  implementation-flavoured rules such as "one shared helper" (§4.5.1, §7.5.1, §8.1). It is also
  the real question underneath ChatGPT's finding 1: **the SPEC/ARCHITECTURE split cannot be drawn
  where the reviewer wants it while that promise stands**, and the promise sits oddly beside the
  next clause of the same sentence, which sends architecture to a separate document. 08 declined
  to touch it — it is a substantive decision about what SPEC is for, not a cross-reference — but
  it is the one question that would actually settle the boundary rather than manage it.
- **SPEC §7.9's "one string per post" clause reads as performance and is not (new, parked
  2026-08-18 by prompt 08.)** *"The line is derived from the post's own type and tags, never from
  the viewer — one string per post, not a per-viewer computation."* The second half is the first
  half in implementation vocabulary, in a bullet list whose other rules are *never a number* and
  *never the audience itself*; a per-viewer line would leak, which is why the rule exists. It was
  the one passage a reviewer read as an implementation instruction inside the product spec, and
  it is the wording rather than the rule that invites that. Rewording it is a content change, so
  08 left it. Small, and worth doing whenever §7.9 is next opened.
- **SPEC §2's logged-out list is short by more than `/healthz` (new, parked 2026-08-18 by prompt
  08.)** §2 says "no public (logged-out) pages except login/registration/invite-acceptance." Two
  things do not fit. The **privacy policy and accessibility statement are linked from login**
  (BUILD_PLAN §15.1, §15.2) and are therefore reachable logged out. And **SPEC §16.1's own scope
  line names a different three** — "login, password reset, invite redemption" — against §2's
  "login/registration/invite-acceptance"; registration and password reset are not the same page,
  and both documents cannot be right. This is a SPEC-internal inconsistency of the kind prompt 11
  collects, and it is a content change either way, so 08 recorded it rather than fixing it.
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
| 2 | Request card: "one component" (§9.1) vs snapshot (§5.2) | new | 11 — **done in 1.26**. The invariant is over the **field set and its rendering**, never the data source: one component and one template, fed from live rows or from the snapshot. SPEC §9.1 now lists which of the card's fields freeze (photo, short bio) and which render live (name, hashtags, mutual friends, report action), and calls that list a security boundary — it is exactly the pair SPEC §13.6's send hold covers. 09 §G is constrained by it |
| 3 | §8.1 "exactly" vs §5.4 blocks; no `can_see_comment` | new | 11 — **done in 1.26**, ARCHITECTURE side included; BUILD_PLAN side is 09 §L. The failing word was **"exactly"**, not "never more": the comment audience is a strict subset of the post audience. The real finding was the consequence — a rule the spec called redundant produced no function and no test, so every comment template was either doing the block check or not doing it. `can_see_comment` added; comment lists and reaction lines are engine-owned querysets. **Reactions were checked and need no function of their own**: a block empties a one-person audience rather than narrowing it |
| 4 | Security emails: §4.6.1 timestamps vs §12.3 "no timestamp" | new | 11 — **done in 1.26**. §12.3 stated a broader rule than it argued for: every word of its justification is about a **relative** age decaying between send and open, and an absolute timestamp does not decay. Narrowed to relative ages; §4.6.1 untouched. **§4.8 was the live casualty** — the inactivity warnings are email-only and now state the absolute deletion date, since a warning that cannot say *when* is not a warning. BUILD_PLAN Step 12.5 still carries the old wording → 09 §P |
| 5 | §4.7 "full erasure" ignores the 30-day backup window | duplicate of DeepSeek 10 | 02 item 12 — sharpens the target to §4.7 |
| 6 | `friend_requests` lacks snapshot columns | new to the reviews | already covered by 09 §G |
| 7 | `images` lacks a gallery-order column | new | 09 §K |
| 8 | "Ban" (and "warn") never defined, §13.2 | new | 12 — **done in 1.27**, and the reviewer named only half of it: *warn* was undefined in the same sentence and had no delivery channel in §12 either. New SPEC **§13.2.1**: a ban is **§4.7's deactivation done to a person**, content **hidden and never deleted** (§7.6's principle read in the mirror — a judgment about one person may not destroy the other half of somebody else's conversation), **reversible but lossily** (hidden content keeps expiring), with the **session made inert rather than the login refused**, because export and erasure are data rights a moderation outcome does not cancel. A warning is an **email plus a record**; an in-feed notification type was **rejected, not deferred**. Invite tree still attaches nothing (confirmed, not re-derived). ARCHITECTURE and BUILD_PLAN side is 09 §Q |
| 9 | The founder cannot interpret a screen reader | extends DeepSeek 17, 22 | 06 item 5 — **done in 1.22**. SPEC §16.5.1 defines *qualified* (a daily screen-reader user, paid, before a professional auditor) and BUILD_PLAN §15.3 books the person from Phase 13 — the decision's real cost was scheduling, not wording |
| 10 | Tripwire paradox; guards are tool-specific | extends DeepSeek 16 | 07 item 8 — **done in 1.23**. Both halves were right. §2.4 now defines the legitimate cap-raising sequence (SPEC §14 → `constants.py` → tripwire → checksums, one founder commit, `--no-verify`) and makes a constants failure at any other time a real alarm; and it says plainly that guard 1 does not survive a change of tool, guard 2 does not survive `--no-verify` or a fresh clone, and **layer 4 is what is actually being relied on** |
| 11 | Reactions on pinned posts never expire | new | 10 — **done in 1.25**; the finding was right on every factual point. A reaction now expires 90 days after it was last set, on a clock of its own (SPEC §8.2.1), and SPEC §9.7 names reactions on the expiring side. Checking it settled the five things §8.2 had never said: where a reaction renders, what the picker is, that a reaction on a comment is invisible to the post's author, that changing one never re-notifies, and that a retired `REACTION_SET` phrase needs no migration **because** reactions expire |
| 12 | Hashtag gate ambiguous for multi-tagged posts | new | 02 item 11 — **founder ruled: any shared tag**; abuse reporting → 05 item 7 |

Two findings needed no new work: **#6** was already in prompt 09's inventory (§G asks
ARCHITECTURE §4 for the snapshot fields including a stored image copy), and most of **#1**
was too — 09's inventory was built from SPEC directly rather than from reviewer findings, so
it already covered the four-tab profile, the friends page, the stated-visibility line, the
avatar picker and the pending-request expiry.
