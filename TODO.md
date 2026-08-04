# TODO — WeeBee design work

Tracker for the design conversations still to be held. Each numbered item has a
self-contained prompt file in `prompts/`, written to be pasted into a **fresh**
session (BUILD_PLAN §0.2 rule 4: long chats degrade; prompts carry their own context).

**Project version at time of writing: 1.16.** Under the new scheme (prompt 01) the
version number belongs to the whole project, not to individual files.

---

## How to use this file

1. Pick the next prompt whose dependencies are met.
2. Open a fresh session in this repo and paste the prompt file's contents.
3. When the conversation ends, update the **Status** and **Landed in** columns below,
   and confirm the session wrote its CHANGELOG.md entry.
4. A prompt that ends in "no change" is still *done* — record the decision and its
   reasons in-document, per README's rule that rejected suggestions keep their reasons.

Status values: `not run` · `in progress` · `done` · `deferred` · `dropped`

---

## The queue

| # | Prompt | Touches | Depends on | Status | Landed in |
|---|---|---|---|---|---|
| 01 | [Changelog & project-wide versioning](prompts/01-changelog-and-versioning.md) | all four docs, new CHANGELOG.md | — | done | 1.17 |
| 02 | [Small corrections & open items](prompts/02-small-corrections.md) | SPEC, ARCHITECTURE, BUILD_PLAN | 01 | not run | |
| 03 | [Visibility engine performance](prompts/03-visibility-engine-performance.md) | ARCHITECTURE §5, §9 | 01 | not run | |
| 04 | [Availability & DDoS posture](prompts/04-availability-and-ddos.md) | ARCHITECTURE §7, §13 | 01 | not run | |
| 05 | [Hashtag vocabulary operations](prompts/05-hashtag-vocabulary-operations.md) | SPEC §11.2, §13.5, §13.2, §7.9 | 01 | not run | |
| 06 | [Accessibility: regression & the admin](prompts/06-accessibility-regression.md) | SPEC §16, ARCHITECTURE §9, BUILD_PLAN §16 | 01 | not run | |
| 07 | [How documents change during the build](prompts/07-design-review-mode.md) | BUILD_PLAN §0.2 + §2.4, all four headers, CHANGELOG | 01 | not run | |
| 08 | [Document boundaries: SPEC vs ARCHITECTURE](prompts/08-document-boundaries.md) | SPEC, ARCHITECTURE | 01 | not run | |
| 10 | [Reactions: look, lifecycle, expiry](prompts/10-reactions.md) | SPEC §8.2, §7.6, §9.7, §14; ARCHITECTURE §4, §6 | 01 | not run | |
| 11 | [Three internal contradictions in SPEC](prompts/11-spec-contradictions.md) | SPEC §9.1/§5.2, §8.1/§5.4, §4.6.1/§12.3; ARCHITECTURE §5 | 01 | not run | |
| 12 | [What a ban actually does](prompts/12-moderation-outcomes.md) | SPEC §13.2, §4.7, §12 | 01 | not run | |
| 09 | [The sync: ARCHITECTURE + BUILD_PLAN to current SPEC](prompts/09-sync-arch-and-buildplan.md) | ARCHITECTURE, BUILD_PLAN | **02–08, 10–12** | not run | |

**Run 09 last.** Prompts 02–08 and 10–12 may each amend SPEC and ARCHITECTURE; syncing
BUILD_PLAN once against a settled SPEC means writing those build steps a single time.

**Do not start Phase 2 of BUILD_PLAN until 09 is done.** `BIO_CHANGE_COOLDOWN_HOURS` and
`BIO_EDIT_GRACE_MINUTES`, which SPEC §14 marks **retired v1.16**, are still live
instructions in **five** places: ARCHITECTURE §4 (`profiles`, where they are *columns*),
ARCHITECTURE §4 (`rate_counters`), ARCHITECTURE §7 (inside a security argument),
BUILD_PLAN §8.1, and BUILD_PLAN §13.4. A build session following those files today would
write the wrong mechanism. This file previously named only two of the five.

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
| Cloudflare proxy ban leaves no DDoS mitigation | DeepSeek 9 | 04 |
| Hashtag vocabulary makes the operator a single point of failure | DeepSeek 3 | 05 |
| Accessibility is audited once, never regression-tested | DeepSeek 22 | 06 |
| Django admin WCAG exception is a hedge, not a decision | DeepSeek 12 | 06 |
| AI cannot even *propose* a document correction | ChatGPT 2 | 07 |
| No "discovery loop" for steps found missing mid-build | DeepSeek 14 | 07 |
| AI won't recognize when it needs to change a law file | DeepSeek 15 | 07 |
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
  screen-reader and zoom checks the reviewer said were absent. *Residual, and it is
  DeepSeek 22's point rather than 17's:* all of it runs once, as a pre-launch gate.
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

- **`HASHTAG_VOCAB` seed content.** Whatever prompt 05 decides about the approval
  workflow, the initial vocabulary still has to be written. That is content work, not
  design work — do it during Phase 10.
- **Constant values as a whole.** README §1 invites review of every cap. No reviewer
  engaged with the numbers. Still open.

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
| 9 | The founder cannot interpret a screen reader | extends DeepSeek 17, 22 | 06 item 5 — **founder has decided to engage a qualified tester** |
| 10 | Tripwire paradox; guards are tool-specific | extends DeepSeek 16 | 07 item 8 |
| 11 | Reactions on pinned posts never expire | new | 10 |
| 12 | Hashtag gate ambiguous for multi-tagged posts | new | 02 item 11 — **founder ruled: any shared tag**; abuse reporting → 05 item 7 |

Two findings needed no new work: **#6** was already in prompt 09's inventory (§G asks
ARCHITECTURE §4 for the snapshot fields including a stored image copy), and most of **#1**
was too — 09's inventory was built from SPEC directly rather than from reviewer findings, so
it already covered the four-tab profile, the friends page, the stated-visibility line, the
avatar picker and the pending-request expiry.
