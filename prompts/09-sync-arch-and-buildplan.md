# Prompt 09 — Sync ARCHITECTURE and BUILD_PLAN to the current SPEC

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** ARCHITECTURE.md, BUILD_PLAN.md
> **Depends on:** prompts 02–08. **Run this last.**
> **Expected outcome:** the three documents describe the same platform again, and Phase 2
> of the build can safely begin.
> **This is the largest prompt in the queue.** Expect to split it across two sessions —
> ARCHITECTURE first, BUILD_PLAN second. That is fine; record the split in TODO.md.

---

You are working in the WeeBee design-document repository. Read `README.md`, then `SPEC.md`
in full, then `ARCHITECTURE.md` and `BUILD_PLAN.md` in full, then `CHANGELOG.md` for every
version from 1.16 onward. This is a **founder-directed design session**; you may edit
ARCHITECTURE.md and BUILD_PLAN.md.

## Why this session exists

**ARCHITECTURE.md and BUILD_PLAN.md were never synced to SPEC v1.16.** ARCHITECTURE was
last synced at SPEC v1.15, BUILD_PLAN at v1.13–v1.15. Two external reviewers each found a
fragment of the consequence and reported it as a spec inconsistency; it is not — it is one
overdue sync, and everything they found falls out of it.

Two consequences are live errors rather than omissions, and they are why Phase 2 of the
build has not started:

- **BUILD_PLAN §8.1 instructs the builder to implement `BIO_CHANGE_COOLDOWN_HOURS` and
  `BIO_EDIT_GRACE_MINUTES`.** SPEC §14 marks both **retired v1.16**. A builder following
  BUILD_PLAN today would write a mechanism the spec deliberately removed, and the §2.4
  tripwire test — which asserts every SPEC §14 constant — would fail on constants that no
  longer exist.
- **ARCHITECTURE §7 makes the same reference**, inside a security argument that concludes
  "the cooldown is the only control that covers the profile photo." That conclusion is no
  longer true: v1.16 replaced the cooldown with a send-hold *and* added a snapshot of the
  photo and short bio at request-send time. The argument needs rewriting, not
  find-and-replacing.

Since prompts 02–08 will have amended SPEC and ARCHITECTURE further, **work from the
documents as they stand, not from the inventory below.** The inventory is a checklist to
make sure nothing is missed, not a description of the current state.

## Method

Follow the pattern every previous sync used, which is recorded in CHANGELOG.md and works:

1. **Fold into existing phases wherever possible.** Prior syncs added exactly one new step
   (6.6) across five spec versions and renumbered nothing. Renumbering breaks every
   reference in every document and both reviews.
2. **New steps get letters** (6.2a) when they must be inserted mid-phase.
3. **Each phase's ✅ verification is part of the change.** A folded-in requirement with an
   unchanged verification is not actually in the plan — the verification is the only
   quality gate the founder has.
4. **Work ARCHITECTURE first, then BUILD_PLAN.** BUILD_PLAN cites ARCHITECTURE throughout.
5. **Report each item before editing.** For each, state: what SPEC now requires, what the
   target document says today, and the proposed change. Batch these — do not ask about
   each of twenty items separately, but do not make twenty silent edits either.

---

## Inventory — SPEC v1.16 changes and where they land

Verify each against the current SPEC before acting; several may already have been handled
by prompts 02–08.

### A. The retired constants (do these first — they are errors, not gaps)

- BUILD_PLAN §8.1: remove `BIO_CHANGE_COOLDOWN_HOURS` and `BIO_EDIT_GRACE_MINUTES` and
  their three carve-outs and verification steps.
- The replacement, `REQUEST_HOLD_AFTER_PROFILE_CHANGE_HOURS` = 12, is **not a Phase 8
  concern** — it holds *friend-request sending*, so it belongs where friend requests are
  built (§4.3) or where rate limits land (§13.4). SPEC §5.2, §9.4 and §13.6 all describe
  it; place it once and cross-reference. Its exemptions — picker selections, clearing to
  empty, screening rejections, the extended bio — are part of the requirement.
- ARCHITECTURE §7: rewrite the friend-request-surface paragraph. The three controls are
  now screening, the **send hold**, and the **snapshot**, and the "cooldown is the only
  control that covers the photo" sentence is obsolete — the snapshot is what actually
  covers it now.
- **The retired constants are in five places, not two.** A third reviewer of v1.16 found
  them in the data model, which neither earlier review nor `TODO.md` recorded. Work the
  full list mechanically — a grep for both names is the check:
  - `ARCHITECTURE.md` §4 `profiles` — defines **`short_bio_changed_at` and
    `photo_changed_at` as columns**, with the grace-window semantics spelled out. These are
    storage for a retired mechanism; decide whether the new send-hold needs its own
    timestamp columns or reuses these renamed, and do not leave both.
  - `ARCHITECTURE.md` §4 `rate_counters` — names `BIO_CHANGE_COOLDOWN_HOURS` in the list of
    controls that are elapsed-time checks rather than day tallies. Still true of the
    replacement; the constant name is wrong.
  - `ARCHITECTURE.md` §7 — the security argument above.
  - `BUILD_PLAN.md` §8.1 — the build instruction and its three carve-outs.
  - `BUILD_PLAN.md` §13.4 — the "confirm the three non-counter controls are wired" check,
    which names the retired constant and would have the builder verify a mechanism that no
    longer exists.

### B. The profile page is a different page (SPEC §9.1, v1.16 (a) and (b))

- BUILD_PLAN §8.1 says "SPEC §9.1 section order," describing the stacked page that v1.16
  replaced. The profile is now a **persistent header** (photo, display name, report
  action) above **four tabs reached as separate URLs, not a scripted widget**: Blog,
  Pinned, Photos, About. A tab renders only where the viewer has content; no tab strip is
  drawn when only one qualifies.
- **The stated invariant is the important part and needs its own build instruction:** the
  header plus the About tab minus the extended bio is *exactly* §9.2's basic tier and
  *exactly* §5.2's friend-request card, **built from one component**. SPEC says three
  surfaces that drift apart would silently falsify the screening arguments of §5.2 and
  §13.1. That is an architectural instruction — check whether ARCHITECTURE should carry it
  alongside the visibility engine's single-source rule.
- Feed posts now appear on their author's profile Blog tab (§9.1 (b)). No audience widens;
  §7.4's snapshot-plus-current-friendship rule is untouched. Confirm the Blog tab query
  goes through the visibility engine and that a FoF still sees no feed post at all.

### C. Stated visibility on every post (SPEC §7.9)

Every post displays its audience in plain text on every surface — feed, Blog, Pinned,
single-post view — and the comment box repeats it. Derived from the post's own type and
tags, **never from the viewer**; never a number; never the audience itself on a feed post;
real text, not an icon or colour; updates in the composer and editor through a polite live
region. Lands in Phase 6 (composer, feed) and Phase 7 (comment box), with the live-region
behaviour composing Step 2.5's `_status.html` partial.

### D. Paging (SPEC §7.7.1)

Prev/next links, never page numbers (a post count in disguise), never a date archive
(§7.5.1 forbids absolute dates), never infinite scroll or "load more."
`POSTS_PER_PAGE_DEFAULT` = 20 with a viewer-chosen `POSTS_PER_PAGE_OPTIONS` of 20/40/60 —
**one setting applying everywhere**, so it is a user preference field, not a per-page
control. Lands in Phase 6 (feed) and Phase 8 (Blog tab); the setting itself lands wherever
user preferences live.

### E. The friends page (SPEC §11.6)

A user's own friend list, **alphabetical by display name and no other sort order** (any
other ordering would be the platform inferring who matters, §1.3), with a filter box over
it. SPEC §11.6 calls it "the commonest route to a profile, absent from every prior
version" — and it is absent from BUILD_PLAN too. Decide where it lands: Phase 4.3 builds
the friendship flows, Phase 8 builds profiles. Prompt 02 may already have added the
required label wording; check before specifying it.

### F. The profile photo becomes a picker (SPEC §9.4, §14)

`DEFAULT_AVATAR_SET` — operator-curated original artwork, never photographs of people, one
member designated as the account-creation default. Picker selections notify nobody and are
exempt from the send hold; uploads notify friends, coalesced. Needs a Phase 8 step, an
operator-console editor in Phase 13 (alongside `HASHTAG_VOCAB`, `REACTION_SET` and the URL
allowlist), and an account-creation assignment in Phase 3.

### G. The friend-request card snapshot (SPEC §5.2, §14)

The card **freezes** the photo and short bio at send time — without which any hold is
defeated by changing the photo after the requests are out. Consequently **pending requests
expire at 90 days**, destroying the frozen card with them. Two things follow:
ARCHITECTURE §4 needs the snapshot fields (including a stored copy of the image, not a
pointer to the live one), and ARCHITECTURE §6 plus BUILD_PLAN §14 need the expiry job.
This is a new cron job and a new data-retention path — treat it as such.

**Constrained by prompt 11 (1.26) — read SPEC §9.1's field table before writing the
columns.** The snapshot is **the profile photo and the short bio, and nothing else.** The
display name, the shared hashtags, the mutual friends and the report action all render
**live**, and snapshotting any of them would break SPEC §4.5.1 (names are never stored on
content) or leave a mutual-friends line SPEC §5.4 cannot empty. SPEC §9.1 now states that
list explicitly and calls it a security boundary; the same section also settles what
"render from one component" means — **one template and one field set, fed from either live
rows or the snapshot** — so the card component and the profile's basic tier stay one piece
of code without the card losing its freeze.

### H. Pinned posts (SPEC §7.6, §9.1 (d))

A pinned post displays its age, stays open for new comments, and those comments expire on
their own 90-day clock leaving **no trace at all** — no "this once had comments" marker,
which SPEC calls a count in disguise. Lands in Phase 7.

### I. Tag edits notify existing commenters (SPEC §7.8, v1.16 (f))

The editor shows the same live audience line as the composer, warns when the post already
has comments, and **every existing commenter is notified**. SPEC notes no new machinery is
needed — commenting already turns following on (§12.3), so the delivery path exists.
Touches Step 6.6 (editing) and Phase 12 (notifications); confirm both ends.

### J. The friend-list disclosure removal (SPEC §11.5)

BUILD_PLAN §10.4 says "Friend-list visibility per §11.5," which is now a materially
different rule: **mutual friends only**, as names, never a count. The hashtag-matched
non-mutual clause is deleted. The step text may survive unchanged since it cites the
section, but Phase 4.2's test suite explicitly lists "friend-list filtering (§11.5)" as a
tested rule — that test now asserts something different, and the deleted behaviour should
be tested as *absent*. This is the highest-value item in the inventory for the visibility
engine, because it removes an enumerable disclosure.

### K. The smaller v1.16 corrections (§9.4, §8.1, §8.2, §13.2, §4.7, §5.3, §16.3)

- The short bio **rejects** disallowed URLs at save rather than de-linkifying them.
  BUILD_PLAN §8.1 currently says "rendered with links disabled" — that is now only half
  the rule.
- Both bios gain whitespace rules they never had: §7.2.1's normal-post rules for the
  extended bio, all line breaks collapsed in the short bio, no preformatted toggle for
  either.
- The gallery gains author-arranged order with keyboard-operable controls, and has **no
  caption field** — the alt text is the caption, shown in the expand overlay. **The data
  model has nowhere to put that order:** ARCHITECTURE §4's `images` table has no
  `position`, `sort_order` or equivalent column, so a builder reading only that document
  produces an upload-ordered gallery with no way to rearrange it. Add the column; note that
  it makes reordering a write to every affected row, which is fine at `GALLERY_MAX` = 8.
- §8.1's name-linking rule now covers post authors, mutual-friend names and reaction
  lists, not just commenters. **Reactions never render in a list view** (§8.2).
- The friend-request card gains a report action; §13.2 states what a *profile* report
  captures.
- §4.7: deactivation hides an account's content everywhere, reversibly.
- §5.3: the unfriend confirmation must say plainly that unfriending is not invisibility.
- §16.3 gains three specifics: distinct accessible names for repeated "read more"
  controls, containment of a preformatted post's horizontal scroll inside the post, and
  **server-side** application of the viewer's theme override.

### L. The visibility engine's missing comment check (handed over from prompt 11)

Prompt 11 settles a SPEC contradiction with a direct consequence here: a block makes the
comment audience a **strict subset** of the post audience (§5.4), so comment visibility is
not the same question as post visibility. When this prompt was written, ARCHITECTURE §5 listed `can_see_post`,
`can_see_profile_tier` and `can_act` and **no** `can_see_comment`, which meant every
template rendering a comment was either doing the block check itself or not doing it at all.
That is exactly the "one visibility engine" rule being quietly broken.

**Settled in 1.26; ARCHITECTURE is already done, so this item is BUILD_PLAN only.** SPEC
§8.1 now reads *"visible to the people who can see the post, minus anyone blocked in either
direction with the comment's author — never more."* ARCHITECTURE Decision 4 has gained
`can_see_comment(viewer, comment)`, §5.1 explains why comments and reactions are narrower
questions than the post's, §5.4's list of engine-owned querysets now includes the comment
list and the reaction line, and §9 carries the test case. Three things follow in
BUILD_PLAN:

- **Step 4.1** lists "the five functions of ARCHITECTURE Decision 4" by name. There are
  now **six**; add `can_see_comment` to the list.
- **Step 4.2** gains the case that fails: **a comment a block hides on a post both parties
  can see.** Every post-level test passes while that comment leaks, which is why it is
  named rather than left to "blocks" in general.
- **Step 7.1** (comments) should say that the comment list's queryset comes **from the
  engine**, exactly as §N.3 says it for the feed — a template looping `post.comments.all()`
  is the defect, and it renders correctly for everyone who is not blocked.

**No `can_see_reaction`, deliberately.** A block must remove a reaction already given from
its recipient's view, but a reaction's audience is one person, so the block empties the
line rather than narrowing it. ARCHITECTURE §15 item 9 records this so it is not "fixed"
later as an oversight.

### N. The visibility engine's performance rules (handed over from prompt 03, landed in 1.19)

Prompt 03 added ARCHITECTURE §5.2–§5.5 and four tests in §9. **No new BUILD_PLAN phase or
step is needed** — Phase 4 builds the engine and Phase 6 builds the feed — but five
existing places now describe a smaller engine than the architecture does. Read
ARCHITECTURE §5 first; this list is the map, not the content.

1. **Step 4.1** currently says "the five functions of ARCHITECTURE Decision 4." The engine
   now also has **plural forms** (§5.4) — one queryset per list, plus
   `profile_tiers(viewer, people)` — and a **request-scoped memo** behind a small
   middleware (§5.3). Both are built *with* the engine in Phase 4, not retrofitted after a
   slow feed, which is the whole point of putting them in the architecture. Where a
   singular answer is a plural one over a set of one, it is implemented that way.
2. **Step 4.2** gains three of §9's four new tests — the queryset/singular equivalence
   test, the viewer-in-the-key test (preview-as inside one request), and the
   flush-on-write test. They belong beside the correctness suite because their failures
   are privacy failures, not slowness.
3. **Step 6.4** (the feed page) is where the **shape test** lands: render the same seeded
   feed at 20 and at 60 and assert the query counts are *equal* and under a ceiling. State
   the ceiling as a number in the step so the founder can check it, and state in the step
   that the equality is the assertion that may never be relaxed. Also say plainly that the
   feed's queryset comes **from the engine** — a view writing its own
   `Post.objects.filter(audience__user=viewer, …)` is the defect this step exists to
   prevent, and it fails silently because the page still looks right.
4. **Step 7.1** (comments) renders many names; its name-linking rule should be fed by one
   `profile_tiers` call over the page's cast, not one call per name.
5. **Appendix rule 2** is the natural home for a second sentence: lists take their base
   queryset from the engine, because **a queryset filter is a visibility decision**. Rule 2
   currently says "never inline," which a builder reads as being about templates.

Check also that no step tells anyone to add a cache: §5.5 bans cross-request caching of
visibility answers in three named forms, and §14 carries them as rejected rows.

### O. Reactions (handed over from prompt 10, landed in 1.25)

Prompt 10 rewrote SPEC §8.2 and added §8.2.1 (a reaction expires 90 days after it was last
set, on its own clock, pinned post or not), §8.2.2 (what a reaction looks like on screen) and
§8.2.3 (the curation criteria and the retire-never-repurpose rule). ARCHITECTURE §4 and §6
were amended in the same session. **BUILD_PLAN was deliberately not touched**, on the 1.19
precedent — prompt 10's build work lands in existing steps and is written once, here. Read
SPEC §8.2–§8.2.3 and ARCHITECTURE §15 item 8 first; this list is the map, not the content.

1. **Step 7.2** is two lines describing a section that is now three subsections. It needs:
   the **own-clock expiry**; **one reaction per user per target, and none on your own
   content**; the **visible-to-exactly-one-person** rule, *including that a reaction on a
   comment is invisible to the post's author*; the **`<details>`/`<summary>` picker** with
   its distinct accessible names per post and per comment (SPEC §16.3's repeated-controls
   rule) and its 320 px wrap; the **"React" / "Reacted: Love it!"** control text, which is
   how a reactor knows and is the only thing a reactor sees of their own reaction; and
   **no empty state** — nothing rendered when nothing has been given.
2. **Step 6.5** (or wherever `expire_content` is built — check) must sweep reactions **by
   their own `set_at`**, not only as a cascade from a deleted post. State the pinned-post
   case in the step, because it is the only case that fails and it will never show up in
   ordinary seed data. A backdated-91-days reaction on a **pinned** post is the milestone
   check worth adding.
3. **Step 2.2 / the constants step** must not put `REACTION_SET` in `constants.py`. It is
   the `reaction_phrases` **table** (ARCHITECTURE §4, new in 1.25), with text, display
   order and an `active` flag. While there, check the same step against `HASHTAG_VOCAB`,
   `NAME_BLOCKLIST` and the URL allowlist — ARCHITECTURE §4's new carve-out paragraph says
   the operator-curated *sets* are all tables, and the constants step may currently say
   otherwise.
4. **Step 13.3** already builds a `REACTION_SET` editor in the admin. It now has a rule to
   enforce: rows are **retired by clearing `active`, never deleted**, and a row's text may
   be corrected but never repurposed (SPEC §8.2.3). Same shape as the URL-allowlist
   editor's "deactivating beats deleting" in the same step.
5. **Step 12.4** (notification rendering) gains one clause: **a notification left with no
   actors at all is not rendered and is deleted** (SPEC §12.2, v1.25), and
   `expire_notifications` sweeps any the render path misses.
6. **The `REACTION_SET` content step.** BUILD_PLAN §0 lists "the reaction phrases" as a
   `[FOUNDER+AI]` example but no numbered step writes them. Give them one, next to the
   `HASHTAG_VOCAB` content step of Phase 10, and point it at SPEC §8.2.3's six criteria.
   Carry the recommendation with it so it reaches the founder at the moment the list is
   actually written: **drop "Ha!", add "Thank you!"** — SPEC §8.2.3 states why.

### M. Everything prompts 02–08, 10, 11 and 12 decided

Fold in whatever those sessions added — the availability and monitoring work from prompt
04 is likely the largest. Read CHANGELOG.md rather than trusting this list. (Prompts 03,
10, 11 and 12 are already itemized in §N, §O, §P and §Q; prompt 12's ban definition landed
in 1.27 and its handover is §Q, so it no longer needs reconstructing from here.)

### P. Email carries no *relative* age — the rule was narrowed (from prompt 11, landed in 1.26)

**BUILD_PLAN Step 12.5 is now wrong, and wrong in the way that matters.** It says
*"**Emails carry no timestamp at all** (SPEC §12.3) — a relative age computed at send time
is false by the time the mail is read, and the mail client already stamps it."* SPEC §12.3
was narrowed in 1.26: what email may not carry is a **relative age**. An absolute timestamp
does not decay, and SPEC §7.5.1's two exceptions hold in email exactly as they hold on a
page. A builder following Step 12.5 as written strips the absolute time out of a
security-event mail (SPEC §4.6.1) and the deletion date out of an inactivity warning
(SPEC §4.8), which makes the warning useless — the collision that forced the fix.

Rewrite the clause to say **no relative age**, and name the two things that do carry an
absolute time. Check while there that no other step repeats the old wording; a grep for
"no timestamp" over BUILD_PLAN and ARCHITECTURE is the check (ARCHITECTURE was clean at
1.26, and its §4 time-helper paragraph already states the two exceptions correctly).


### Q. What a ban and a warning are (from prompt 12, landed in 1.27)

SPEC gained **§13.2.1**, which defines the three moderation outcomes §13.2 had only named.
Read it before writing any of this; the summary below is a checklist, not the rule.

**The one-sentence version:** a ban is **SPEC §4.7's deactivation, done to a person rather
than chosen by them, with the session made inert and no clock running.** Content is
**hidden, never deleted**. It is **reversible**, and reversal does not restore anything that
expired while hidden.

**ARCHITECTURE §4, the `users` row.** It currently lists *"deactivation/deletion-grace
state"* and carries no moderation state. Add a **banned flag with the date of each ban and
each reversal**. The load-bearing constraint: **this is one more input to the visibility
engine (§5), not a second hiding mechanism.** A banned account is invisible by the same
route a deactivated one is, and a builder who writes a parallel "hide banned users" path
has created two places where visibility is decided, which is Decision 4 defeated exactly as
1.26's missing `can_see_comment` defeated it. No new engine function is needed — the
account-state input the engine already consults simply has one more value.

**ARCHITECTURE §4, a `warnings` table.** Date, account, the operator's text, and the report
it arose from where there was one. SPEC §13.4 now requires the record; nothing holds it
today. Note this is the **second** addition to a moderation table on this prompt's list —
the missing `note` column on `reports` (from 1.21, in the TODO notes) is the other, and both
should land in one pass.

**BUILD_PLAN, four places.**

1. **Step 13.3** already says the console has *"act-on actions (delete content / warn /
   ban)"*. It now has to say what they do. Two constraints belong **in the step**: ban is a
   **per-account action and never a bulk list action** (SPEC §13.2.1 point 10 — Django's
   admin hands you a select-rows dropdown for free and that is precisely the fat-finger),
   and the confirmation must **state what a reversal cannot restore**.
2. **Step 14.2** (`inactivity_sweep`) gains two branches for a banned account: a banned
   sign-in **does not refresh the last-login date**, and **two of the four warning emails
   are suppressed** — the 180/365 dormancy notes go, the 670/700 deletion warnings stay
   (SPEC §4.8, §13.2.1 point 8).
3. **Step 14.4** (data export) must stay **reachable from a banned session**. This is not a
   nicety: it is the reason SPEC §13.2.1 does not refuse the login at all (SPEC §4.9,
   §15.1).
4. **The banned-session check has no step anywhere, and it is one middleware.** Authentication
   succeeds; authorization is empty except for export, account deletion and the notice page;
   the check runs **per request**, so an already-open session goes inert on its next page
   load and nothing has to reach into the session table at ban time. Decide whether this
   belongs to the authentication phase or to Phase 14 and give it a step. **This is the item
   most likely to be missed**, because every other thing on this list is a column or a form.

**One rule that is not about banning at all.** SPEC §4.7 now states that **an outstanding
invitation cannot be redeemed while the account that sent it is invisible** — voided on the
existing expiry-and-return-to-budget path of SPEC §4.1. This has always been true of
deactivation and was never written down. Whichever step builds invite redemption has to
check the sender's state, and the deactivation step (14.1) has to void.

**Nothing here needs a constant.** SPEC §14 was deliberately untouched in 1.27; every
duration a ban depends on already existed.

---

## Verification before you finish

- **Every SPEC §14 constant appears somewhere in BUILD_PLAN**, or is covered by §2.2's
  blanket "every SPEC §14 constant." Check specifically that no *retired* constant is named
  anywhere in either document.
- **Every SPEC section with a v1.16 marker has a corresponding build step.** Work the list
  mechanically; this is the check that failed last time.
- **Grep both documents for stale section references.** §9.1's structure changed, so any
  citation of "§9.1 section order" is now wrong.
- **No step was renumbered.** Confirm with `git diff`.
- Write the CHANGELOG.md entry, naming every file's status. This entry is the one that
  finally lets ARCHITECTURE and BUILD_PLAN say "changed" against a SPEC version.
- Update `TODO.md`, and state plainly whether Phase 2 of the build is now clear to start.
