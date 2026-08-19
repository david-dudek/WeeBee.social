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

## What the versioned record covers (v1.23)

**Five files:** README.md, SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md and this one. From
1.23 forward, every entry's status table names all five and no others.

**`TODO.md` and `prompts/` are working files, deliberately outside the record.** They get
no table row and never an "unchanged" status, and the reason is not tidiness: the table
exists to make an *unsynced* document visible, and neither of them can be unsynced with
anything. `TODO.md` records what has not been decided yet; `prompts/` records what a
session was asked. Neither is a statement about the platform, and nobody builds from
either. An entry should still say in prose what a session did to them — the parked
questions and the triage record in `TODO.md` are decisions with reasons — but that prose
is not a status. Earlier entries varied: 1.17 changed `TODO.md` without recording it and
1.22 gave it a table row. Neither is corrected, for the reason two sections below.

## Founder approval (v1.23)

Every document said "DRAFT pending founder review" for nine versions — BUILD_PLAN said
"under founder review," which was the same thing in different words and is itself the
evidence that no vocabulary existed — and no defined act ever changed it. There is one
now, and it is small.

**The record is a status field in the document's own header**, in one of exactly two
forms:

- `DRAFT — not yet founder-approved`
- `founder-approved at 1.22`

`founder-approved at N` means: *at project version N, the founder read this file end to
end and approved it.* It stays current for as long as **N is at or above that file's
"This file last changed in" number**, which sits on the very next line of the same
header. When the file next changes in substance, that number moves past N and **the
approval lapses visibly, with nobody having had to remember anything.** Two numbers,
adjacent, one comparison — the same mechanism that makes an unsynced document visible,
which is the whole reason this file exists.

Comparing against the *file's* last-changed number rather than against the project
version is what makes it work: every header carries the current project version whether
or not that file changed, so a project-version comparison would show README as stale
every time SPEC moved. For the same reason, **editing a header's status field does not
count as the file changing** — otherwise approving a file would instantly mark it
unapproved.

- **Approval is per file.** SPEC will be approved long before ARCHITECTURE is synced to
  it, and a scheme that could not say so would be describing a different project.
- **Approval bumps nothing.** This rule is load-bearing: if approving 1.22 produced 1.23,
  then 1.23 would be unapproved and the process could never converge. An approval is an
  annotation on an existing entry plus one header field, and it is the one edit in this
  project that changes files without a version bump.
- **The trigger is a sentence in chat; the record is the file.** The sentence is *"I have
  read `<FILE>` end to end and I approve it at `<version>`."* It names the file, names the
  version and asserts the reading, which are the three things the session needs; a session
  given anything vaguer asks rather than guessing, and refuses to record an approval at a
  version older than the file's last-changed number. The session then writes **exactly
  two things and stops**: the header's status field, and one annotation line on that
  version's entry here. No other edit, no tidying.
- **CHANGELOG.md carries no approval status.** It is a record of events rather than a
  statement to be approved, and it has no version header of its own — the newest entry
  *is* the version.
- **Founder approval and external review are independent facts, not two rungs of one
  ladder.** v1.16 was reviewed by three outside models while every document still said
  DRAFT, so any ladder placing external review after founder approval could not describe
  a state this project has already been in and will be in again.

**External review is an event, not a status.** "v1.16 reviewed by ChatGPT, DeepSeek and
Kimi" is something that happened to a version, and it belongs in that version's entry
below. It changes no document's authority; only the founder's approval does that. A
reviewer looking for what is open to challenge reads README's "What IS up for review,"
which exists for exactly that job.

## Entries are appended, not rewritten (v1.23)

A design session **adds a new entry at the top and leaves the existing ones alone.** The
only two permitted touches to an entry already written are *additions* rather than
rewrites: a **founder-approval annotation**, and an **external-review event** on the
version that was reviewed. Anything else that seems to require editing an old entry is a
stop, not an edit.

This is the discipline that actually protects this file. BUILD_PLAN §2.4 makes
CHANGELOG.md a law file and locks it in the build repository, but design sessions run in
the design repository, which has no lock and must write here every time. So what guards
the history is a rule and a diff: `git diff CHANGELOG.md` should show a new entry at the
top and nothing else. A changelog quietly rewritten to say ARCHITECTURE had been synced
when it had not would defeat the mechanism 1.17 was built to create, and it would leave
no other trace.

---

## 1.27 — 2026-08-18

| File | Status |
|---|---|
| README.md | changed — version header only; no content change |
| SPEC.md | changed — new §13.2.1 defines the three moderation outcomes; §4.7 gains the invisible-account invite rule; §4.8 gains the banned-account sweep adjustments; §9.3's enumeration, §12.1's "everything else" list and §13.4 follow |
| ARCHITECTURE.md | **unchanged** — version header only. §4's `users` row needs a moderation-state column and there is no `warnings` table; both are prompt 09's, itemized below |
| BUILD_PLAN.md | **unchanged** — version header only. No new phase; Steps 13.3, 14.2 and 14.4 need work and one middleware has no step at all, all of it prompt 09's, itemized below |
| CHANGELOG.md | changed — this entry |

From prompt 12, on a third external reviewer's finding against v1.16 §13.2. Verified before anything was written: §13.2's whole workflow clause is *"the operator reviews and acts manually (delete content, warn, or ban an account)"*, and of those three only the first is defined anywhere in the document. The reviewer named the ban; **the warning was undefined in the same sentence and in the same way**, with no delivery channel and no entry in §12's notification types. Both are defined here.

The reviewer's own statement of the cost is the reason this was worth a session: *"you have a button in the admin panel labeled 'Ban,' but no document tells the builder what that button is supposed to do. Different AI models will guess differently."*

### What a ban is, in one sentence

**§4.7's deactivation, done to a person rather than chosen by them, with the session made inert and no clock running.**

That is the whole of the mechanism, and it is deliberately not a new one. The platform already had four adjacent account states — deactivation, deletion, dormancy, blocking — and the question was never what to build but **which existing thing a ban reuses.** Deactivation already hides an account and all of its content everywhere, reversibly; §9.3 already answers a barred viewer with one indistinguishable response; §12.2 already renders from current state, so notifications naming a hidden person drop out on their own. A ban needed none of that written twice.

### The three decisions that were not obvious

**1. Hidden, not deleted — and the reason is §7.6's principle read in the mirror.** §7.6 says an author *"may preserve their own words indefinitely, and may never preserve anyone else's."* The ban case is its reflection: **nor may a judgment about one person destroy the other half of somebody else's conversation.** Deleting a banned account's comments would take half of every exchange they had, on the posts of up to 300 people, none of whom were judged. Hiding delivers everything a ban actually needs — the words are gone from view, no more can be added — and costs nothing, because the mechanism exists. The operator who needs one specific item *gone* still has the delete-content outcome, and the two compose. §13.2.1 also states, for the first time, that delete-content **does** destroy other people's words (a deleted post takes its comments, §7.5) and that the bounded collateral is exactly what makes it a scalpel rather than the general tool.

**2. The session is inert; the login is not refused.** This is the one place the prompt's suggested answer was argued with rather than adopted. "Blocked outright is the obvious answer" — but blocking the login is the same screen with the data rights taken out of it: a correct password already reaches a page saying the account is suspended, whether or not the platform calls that a login. The real question is whether that page also carries **export (§4.9) and account deletion (§4.7)**, and §15.1 answers it: those are data rights, and a moderation outcome does not cancel them. Refusing the login would move every future data request from a banned person to an off-platform identity check the operator is worse at than the login form is. So: authentication succeeds, authorization is empty, exactly two paths work, and the check runs per request so an open session goes inert on its next page load. The notice states the fact plainly and **names no reason** — a reason line would promise a consistency the deferred policy cannot keep.

**3. Warnings are email, and the in-feed notification type was rejected rather than deferred.** The prompt gave permission to split this out if it needed a new notification channel. It does not need one, and saying why was cheaper than deferring it. **A warning is an account notice**, in the family of §4.8's inactivity warnings and §4.6.1's security events — all system-to-user, all email, none of them in the feed. An in-feed type would make the feed a surface the operator speaks on, would need its own coalescing, read-state and wording rules, and would reach only a user who logs in, which is the wrong set. The honest residual is stated rather than engineered around: **email is not proof of reading, and v1 requires none** — a warning that must be acknowledged is a workflow, and workflows are what §13.2 defers. §12.1's list names the warning email; nothing else in §12 changes.

Three smaller things a warning needed: it **never identifies the reporter** (a warning naming who complained makes reporting dangerous, and reporting is the whole of §13.1's third layer); it **is recorded against the account** — date, text sent, originating report, because *"we warned them twice"* is the ordinary basis for a later ban and nothing stored it before; and it **is not subject to §12's optional-email setting**, which governs social notifications, on the position §4.8's and §4.6.1's mails already occupy. A warning a user can switch off is not a warning.

### The questions that had no interesting answer, answered anyway

- **Reversible, and reversal is lossy.** Lifting a ban restores everything still there; **hidden content keeps expiring on its ordinary 90-day clock**, because the expiry job does not consult visibility. A ban lifted after four months restores an account with no posts in it, and pending friend requests (90 days) and unredeemed invites (14) are gone the same way. **The operator is told this at the moment of banning**, in the confirmation, rather than discovering it at the reversal. The record survives the reversal, so a second ban reads as a second event.
- **Never a bulk list action.** Django's admin gives a select-rows-and-choose-action dropdown for free, and select-all-then-ban is the mistake one tired operator makes once. Banning lives on the account's own page, behind a confirmation that names the account and states what a reversal cannot restore.
- **Friendships, groups and the contact card are untouched** — dissolving them would make "reversible" false. One consequence written down rather than left to be discovered: a hidden friendship still occupies a slot against `FRIEND_CAP`, so a user can meet the cap while seeing fewer than 300 names. Not new (a deactivated friend has always done this), leaks nothing about who, and nobody is near the cap at this scale — but a builder needs the answer.
- **The invite tree still attaches nothing, confirmed rather than re-derived.** §4.3 records ancestry for forensics and defers accountability; §17 keeps it parked. A ban is the event that recording was for, so this was the moment to confirm: **the tree exists so a human can look, not so the system can act.** No inviter's budget moves in either direction — reducing it punishes one person for another's conduct; refunding it attaches a consequence in the generous direction, which §4.3 rules out just as firmly.
- **A ban never becomes a deletion on a clock of its own.** Content expires at 90 days, the account goes at §4.8's 730-day sweep, and that is the end. Said explicitly because a builder will otherwise wonder whether to purge sooner.
- **Nothing about a ban is visible to anyone else.** No marker, no tombstone, no explained absence — §7.6's reasoning about expired comments on a pinned post, unchanged. §9.3's enumeration now names the banned case so the identity of those five responses is a requirement rather than an inference.

### One consequence noticed here that is not about banning at all

**An outstanding invitation cannot be redeemed while the account that sent it is invisible.** §4.1 auto-friends inviter and invitee, so an invite completing under a hidden account produces a brand-new member whose only friend is invisible: no friend-of-friend path to anyone, nobody who can see them, no way to be found. That is a property of **invisibility**, not of banning — **deactivation (§4.7) has always had it and never said so.** The rule is therefore stated once in §4.7, on §4.1's existing expiry-and-return-to-budget path, and §13.2.1 inherits it. This is the session's one edit outside the moderation sections, and it is recorded as a gap that was found rather than a decision that was made.

### Constraints held

**Policies and appeals stay deferred**, and §13.2.1 says so in its first paragraph: it defines what the outcomes *do*, never what selects one. **Nothing here is a workflow, a state machine or a queue** — the ban is one reversible flag reusing an existing hiding mechanism, and the warning is an email plus a row. **The data rights survive and the export path is reachable**, which is decision 2 above and the reason the login was not refused. **No public signal**: §9.3 and §7.6 already forbade it and are cited rather than restated.

**No new constant.** §14 is untouched, and deliberately: every duration a ban depends on — 90 days of content, 14 of an invite, 30 of a deletion grace, 730 of the sweep — is one the document already had.

### What is left for prompt 09

Nothing was written to ARCHITECTURE or BUILD_PLAN here. Three items, now itemized in `prompts/09-sync-arch-and-buildplan.md`:

- **ARCHITECTURE §4, the `users` row.** It lists *"deactivation/deletion-grace state"* and has no moderation state. A **banned flag plus the dates of each ban and each reversal** is needed, and it must be a state the visibility engine reads — a banned account is invisible by the same route a deactivated one is, so this is one more input to §5, not a second hiding mechanism. **Do not let a builder invent a second one.**
- **ARCHITECTURE §4, a `warnings` table.** Date, account, operator text, originating report. It does not exist and §13.4 now requires it. Note that this is the *second* thing 09 has to add to a moderation table — the missing `note` column on `reports` (from 1.21) is already in its list.
- **BUILD_PLAN, four named places.** **Step 13.3** already says the console has *"act-on actions (delete content / warn / ban)"* and now has to say what they do, carrying two constraints that belong in the step rather than in prose: **ban is a per-account action and never a bulk list action** (SPEC §13.2.1 point 10), and its confirmation states what a reversal cannot restore. **Step 14.2** builds `inactivity_sweep`, which now has two branches for a banned account — last-login not refreshed by a banned sign-in, and two of the four warning emails suppressed. **Step 14.4** builds the export, which must stay reachable from a banned session. And the **banned-session check itself is one middleware with no step anywhere** — 09 decides whether it belongs to the authentication phase or to Phase 14, and it is the piece most likely to be missed, because every other item on this list is a column or a form.

### Working files (outside the record)

`TODO.md`: prompt 12 marked done at 1.27, and the three prompt-09 handovers above recorded in the queue notes — including the answer to the question the prompt asked to be settled here, which is **yes, ARCHITECTURE needs an account-state column.** `prompts/09-sync-arch-and-buildplan.md`: a new **§Q** carrying the three items.

---
## 1.26 — 2026-08-18

| File | Status |
|---|---|
| README.md | changed — version header only; no content change |
| SPEC.md | changed — §9.1's basic-tier invariant rewritten and given a frozen/live field table, with §5.2's snapshot bullet pointing at it; §8.1's comment audience corrected, with §7.9 and §8.2 following; §12.3's email rule narrowed to *relative* ages, with §7.5.1 and §4.8 following |
| ARCHITECTURE.md | changed — Decision 4 gains `can_see_comment`; §5.1 states why comments and reactions are narrower than their post and how lists carry the rule; §5.3's memo row and §5.4's list of engine-owned querysets follow; §4's `comments` and `reactions` entries note it; §9 gains the test case; §15 gains item 9 |
| BUILD_PLAN.md | changed — version header only; no content change. Two references are now stale and are prompt 09's, itemized below |
| CHANGELOG.md | changed — this entry |

From prompt 11, on the three internal contradictions Kimi found in v1.16. All three were verified against the document text before this session and all three are real. **The calibration note is worth keeping next to the fixes:** two capable reviewers of the same version each stated explicitly that they found none — *"I didn't find an outright contradiction among the current versions"* (ChatGPT), *"The documents are internally consistent"* (DeepSeek). None of the three is obvious, and none is a philosophy question: each is a place where two true intentions were written in a form that cannot both hold.

Two of the three were a sentence. The third was a sentence and a missing function.

### 1. The friend-request card had to be both frozen and live (§9.1, §5.2)

**The collision.** §9.1 required the friend-request card, the profile header plus About tab, and §9.2's basic tier to be *"exactly"* the same thing, rendered *"from one component"* — a requirement, it said, because if the three surfaces drift the screening arguments of §5.2 and §13.1 stop being true. §5.2 requires the card's **photo and short bio to be frozen at send time**, without which the send hold is defeated by the obvious move: send twenty clean requests, then change the photo. One rule reads current rows and the other reads a stored copy. **A builder following §9.1 to the letter rebuilds the exact attack §5.2 exists to stop.**

**The resolution, and it is the small one.** The invariant is over the **field set and its rendering**, never the data source: one component, one template, one list of fields, fed either from live rows or from the snapshot. That is what makes both arguments hold — a field added to the basic tier still appears on all three surfaces automatically, which is the drift the invariant guards against, while a delivered card stays frozen. The spec already half-knew this and said so in one place: §5.2 carves out the display name, which renders live because §4.5.1 forbids storing names on content. §9.1's "one component" predates that carve-out.

**What is new is the list, and it is new because it is a security boundary.** §9.1 now states which of the card's fields freeze and which render live: **frozen** — profile photo (a stored copy, not a pointer) and short bio; **live** — display name, shared profile hashtags, mutual friends, and the report action. **The frozen pair is exactly the pair §13.6's send hold covers**, and for the same reason: those two are the only author-controlled content the platform pushes at a non-friend. Freezing more would break §4.5.1 for the name and leave a stale mutual-friends line that §5.4 could not empty. Recorded alongside: **§9.5's preview-as mode 4 is the same component fed from live rows**, and is the standing proof that the component takes either source.

### 2. Comment visibility is smaller than post visibility, and one word denied it (§8.1, ARCHITECTURE §5)

**The collision, diagnosed one word more precisely than the review did.** §8.1 said a comment is visible to *"exactly"* the people who can see the post — *"never more."* §5.4 says neither party to a block sees the other's comments anywhere, including on a shared friend's post. So if Bob can see Charlie's post and Alice has blocked Bob, Bob sees the post and not Alice's comment on it. **"Never more" was always true. "Exactly", which asserts equality, never was.** The comment audience is a **strict subset** of the post audience.

**The finding is not the word; it is what the word prevented from being built.** ARCHITECTURE §5 exposed `can_see_post`, `can_see_profile_tier` and `can_act`, and no `can_see_comment` — because SPEC had asserted there was no separate question to ask. The consequence is that every surface rendering a comment either applied the block rule itself or did not apply it at all, **and both of those break the rule that one module makes every visibility decision.** This is Decision 4 defeated by a *gap* rather than by an inlined query, which is the harder form to catch in review: a rule the specification calls redundant produces no code and no test, and from inside either document looks exactly like a rule that is handled. ARCHITECTURE §15 item 9 records that as the shape lesson.

**The fix.** SPEC §8.1 now reads *"visible to the people who can see the post, minus anyone blocked in either direction with the comment's author — never more."* §7.9's quotation of the invariant follows it, and the parked per-post-comments switch stays parked with its argument intact and slightly sharpened: the one subtraction is platform-wide and is not the author's to configure. ARCHITECTURE gains **`can_see_comment(viewer, comment)`** in Decision 4 and §5.1, in §5.3's memo row, and — the part that actually matters for lists — **the comment list under a post joins §5.4's set of engine-owned querysets**, since a queryset filter is a visibility decision. §9 gains the case that fails: a comment a block hides on a post both parties can see, which every post-level test passes while the comment leaks.

**Reactions were checked, as the prompt asked, and the answer is "yes, but one tenth the size."** §5.4 covers "comments **or** reactions", and the case is not trivially satisfied: a block standing *after* a reaction was given must remove it from the recipient's view, and nothing said so. But a reaction's audience is exactly one person, so a block does not narrow it — it **empties** it, and the engine renders the line or renders nothing. **No `can_see_reaction` is added**, and that is recorded in ARCHITECTURE §15 so nobody adds one later believing it was overlooked. SPEC §8.2 carries the one-clause rule, on the live-rendering path §12.2 already uses for a reaction its giver removed.

**§8.1's consciously accepted consequence is untouched**, as is §11.3's grant of comment rights to hashtag-matched FoFs and §7.9's disclosure of it. This corrects a description of who sees a comment, nothing else.

### 3. Security emails had to carry a timestamp and no timestamp (§12.3, §4.6.1)

**The collision.** §4.6.1: security events *"carry absolute timestamps wherever they appear"*, because *"was that login me?"* is not a question anyone answers with "several hours ago". §12.3, restated at §7.5.1: *"Email carries no timestamp at all."* Security events are delivered by email.

**The diagnosis is inside §12.3's own reasoning.** Every word of its justification is about a **relative** age decaying between send and open — computed at send, read three days later, false by then. An absolute timestamp has no such problem: *2026-08-04 21:14 UTC* is as true on Friday as it was on Monday. §12.3 was written to ban relative times in email and **stated a broader rule than it argued for**; the over-reach is the entire collision.

**The fix is to narrow §12.3 to relative ages and leave §4.6.1 untouched.** That lands where §7.5.1's own principle already points — *deliberately vague about how old something is, exactly precise about when something will be destroyed* — with security events on the precise side by the same logic as the expiry countdown. §7.5.1's exception sentence now says *account and security* notices rather than *security* notices, since §4.7's deactivation banner was already relying on it.

**The consequence for §4.8 was real and is fixed in the same breath.** The inactivity warnings are email-only and are useless without a date; under the old wording they arguably could not carry one. §4.8 now states that **the two deletion warnings carry the absolute deletion date**, as an account event under §7.5.1's exception and on §4.7's precedent. A deletion warning that cannot say *when* is not a warning.

### What was left for prompt 09, and why

Two of the three have a downstream consequence, and 09 is written expecting the handover. **Nothing below was done here**, and each is now itemized in `prompts/09-sync-arch-and-buildplan.md` rather than left to be reconstructed from this entry:

- **§G (ARCHITECTURE §4, the `friend_requests` snapshot columns).** Unchanged in scope, but now constrained: SPEC §9.1's table says the stored snapshot is **the photo and the short bio and nothing else**. A builder who also snapshots the name, the hashtags or the mutual friends breaks §4.5.1 and §5.4. The stored image is a **copy**, not a pointer to the live one, and it is destroyed with the request at 90 days.
- **§L (BUILD_PLAN Step 4.1 and Step 4.2).** Step 4.1 names *"the five functions of ARCHITECTURE Decision 4"* and lists them; there are now six. Step 4.2's suite needs the block-hides-a-comment case, and the comment list's queryset should be named as engine-owned alongside the feed's.
- **BUILD_PLAN Step 12.5** repeats *"Emails carry no timestamp at all (SPEC §12.3)"* verbatim. That instruction is now wrong in exactly the way that matters — a builder following it strips the absolute time from a security-event mail and the deletion date from an inactivity warning. This was **not** in 09's inventory before and has been added to it.
- **Not touched, and still 09's:** ARCHITECTURE's header still reads *"Companion to: SPEC.md v1.15"*, which the sync owns.

### Scope held

No new constant, no new table, no new job, no new dependency. The no-counts rule, the snapshot mechanism, the block semantics, the relative-time ladder and the anti-scorekeeping posture were all settled before this session and none was reopened. Every change here makes a document say what it already meant.

### Working files (outside the record)

`TODO.md`: prompt 11 marked done at 1.26, and Appendix B's routing rows for findings 2, 3 and 4 annotated with what was settled. `prompts/09-sync-arch-and-buildplan.md`: §G constrained to the two frozen fields, §L given the decision it was waiting on, and a new §P added for the BUILD_PLAN Step 12.5 email-timestamp line.

---

## 1.25 — 2026-08-18

| File | Status |
|---|---|
| README.md | changed — version header only; no content change |
| SPEC.md | changed — §8.2 rewritten and extended with three new subsections (§8.2.1 lifetime, §8.2.2 rendering, §8.2.3 curation); §7.5, §7.6, §9.7, §12.1, §12.2, §12.3, §14 and §16.3 updated to name reactions |
| ARCHITECTURE.md | changed — §4 `reactions` gains its own expiry clock, new `reaction_phrases` table, a carve-out stating that operator-curated *sets* are tables rather than constants, and the empty-notification rule; §6 `expire_content` and `expire_notifications` amended; §15 gains item 8 |
| BUILD_PLAN.md | changed — version header only; no content change. Step 7.2 is now a two-line summary of a section that has grown to three subsections, and the sync is prompt 09's, per the precedent set at 1.19 |
| CHANGELOG.md | changed — this entry |

From prompt 10, on a finding from the v1.16 review by Kimi. The reviewer was right on every factual point, and the gap was in the documents rather than in the design.

**The finding.** SPEC §7.6 says at length that comments on a pinned post expire at their own 90 days and said nothing at all about reactions. SPEC §9.7's two permanence lists — the expiring side and the account-state side — named reactions on neither. ARCHITECTURE §6's `expire_content` deleted reactions only as a cascade from a deleted parent. **A pinned post is never deleted**, so reactions on one were permanent: a post standing for two years could carry every reaction it had ever received.

### The lifetime (questions 1 and 2)

**A reaction expires 90 days after it was last set, on a clock of its own, and its disappearance leaves no trace.** §7.6 had already decided this and had not said so — *"an author may preserve their own words indefinitely, and may never preserve anyone else's"* — and a reaction is another person's statement, attached to them by name, on content its author chose to keep. The reactor has even less notice than the commenter, having spoken in two words from a fixed list rather than in a paragraph they wrote. The rule is now written into §8.2.1 rather than left to be derived, and §7.5, §7.6 and §9.7 each name reactions where they previously named only posts and comments. **§9.7 puts them on the expiring side**, which is not a close call: a reaction is the shortest statement the platform permits, but it is a statement, made at a moment, about one specific piece of content.

**The clock runs from when the reaction was last set, and the apparent conflict with §7.8 invariant 2 is answered rather than ignored.** Invariant 2 forbids an edit resetting a post's clock, so that editing cannot confer immortality and pinning stays the only act of preservation. It does not transfer: a reaction is not readable content — no audience, not findable, not linkable, not followable, not countable, and exactly one person will ever see it. What §7.5 refuses is an accumulating archive, and a two-word private note re-affirmed by the person who wrote it is not one. **The consequence is stated rather than engineered against:** re-picking a phrase every eighty-nine days keeps it alive indefinitely, which is a person keeping *their own* words alive — the side of §7.6's principle that is expressly permitted.

### What a reaction looks like (question 3)

§8.2 was written almost entirely in negatives, and a builder knew what a reaction must never become without knowing where it goes on the page. §8.2.2 settles it, and every rule in it is downstream of one already in the documents.

- **The reaction line** sits under the content it belongs to and above that content's comments, on a single-post view only; it is a real list with an accessible name, its names rendered through the shared helper under §8.1's link-or-plain-text rule. **It is complete — never truncated, folded or summarized**, because "and 4 others" is a number wearing a coat, and because the audience cap and the new 90-day expiry already bound it. **When nothing has been given, nothing is rendered**: "no reactions yet" is a count of zero written out in words.
- **The picker is a native `<details>` / `<summary>` disclosure** — no script, no ARIA menu pattern to implement correctly, the same posture as §9.1's server-rendered tabs. Every post and comment carries one, shown to everyone who may see that content whether or not anyone has reacted, so its presence reveals nothing.
- **A reactor tells they have already reacted from the control's own text** — *"React"* against *"Reacted: Love it!"* — never from a colour or a highlighted button (§16.3, 1.4.1). That text is also the whole of what a reactor sees of their own reaction; the reaction line belongs to the recipient.
- **The 320 px case and the accessible names.** Phrase buttons wrap onto as many rows as they need and nothing scrolls sideways; §7.2.1's preformatted post remains the platform's only reflow exemption. A thread produces one picker per comment plus one for the post, so §16.3's repeated-controls rule applies exactly as it does to "read more": *"React to Alice's comment"*, and each phrase button *"Love it! — react to Alice's comment"*. §16.3 now names the picker alongside the read-more and gallery controls.
- **Nobody reacts to their own content**, which had never been stated either way. A reaction to yourself would put your own name in your own list, and a private tally of self-approval is scorekeeping with a sample of one.

### Reactions on comments (question 4)

**A reaction is visible to exactly one person: the author of the thing it is attached to.** On a comment that is the commenter, **and not the post's author.** The prompt's instinct was right and is now the stated reason: a post author who saw the reactions on every comment on their own post would be handed a column of reaction lines, one per commenter, down a single page — a scoreboard assembled out of other people's warmth, and the same failure the v1.16 list-view rule exists to prevent, arriving by a different door. A host's power over their own post is to **delete** a comment (§8.1); it was never to read the private replies to it.

### Changing and removing (question 5)

**§8.2 and §12.2 were consistent, and a third case fell between them.** Reactions render live, so a removed reaction drops out of every notification that named its giver — but nothing said what happens when the *last* actor drops out. A notification whose only comment was deleted, or whose only reaction was removed, would have rendered as a nameless event or an empty line: live rendering producing the one thing it exists to prevent, a notification that survives what it was about. **§12.2 now deletes it**, and `expire_notifications` sweeps any the render path misses.

Stated once, in §8.2.1, rather than in two half-places: giving notifies, **changing does not** (§7.8's reasoning about edits — a change that costs something socially is a change people stop making), removal is silent because retraction is never announced, and removing and re-giving is a new reaction that notifies as one. **The accepted cost is named:** that last path is a poke channel, bounded by the daily reaction rate limit and by unfriending, and it wins nothing measurable because there is no counter to move. Also settled while there: **a reaction carries no age and no expiry countdown** — ages beside each name would turn a warm line into a log, and a per-reaction countdown would tell the recipient how much longer each piece of warmth has left.

### `REACTION_SET` curation (question 6)

**The set is not frozen here, and the criteria are.** This follows §11.2.1's division for `HASHTAG_VOCAB`: the tests a phrase must pass are durable and belong in SPEC; writing the actual list is content work and belongs to the build plan's [FOUNDER+AI] step. Appendix A item 8 already records the six as placeholders and is unchanged. The six criteria are in §8.2.3; the first decides the list — **a phrase must be warm on the worst post it could land on**, because it can be attached to a post about a death and the only reader is the bereaved.

**One recommendation on the current six, put where the founder will see it at the curation step. "Ha!" fails criteria 1 and 3** — laughing *with* and laughing *at* are the same three characters and the recipient cannot tell which they were sent — and **"Thank you!" is recommended in its place**, gratitude being the commonest warm answer to a post about oneself and the set having no way to say it. This is a recommendation in the text, not a change to §14's row.

**What happens to existing reactions when the operator changes the set — and the answer that made it easy.** Phrases are **retired, never repurposed**: a retired phrase leaves the picker at once and existing reactions keep rendering it, unchanged, until they expire. Text may be **corrected** (a typo) and never **replaced** — turning "Ha!" into "Thank you!" in the same slot puts words in the mouths of everyone who chose it, which is the ventriloquism §7.8 forbids a host over a comment. And **because reactions now expire, a retired phrase is gone from the platform within 90 days with no migration written and no user-facing event.** Question 1's answer solved question 6's hard part; §8.2.3 names the pattern, because on this platform expiry is frequently the cheapest migration available.

**A moderation control was considered and rejected (2026-08-18).** A per-recipient "remove this reaction from my post" — §8.1's host's-rules power extended to reactions. What it defends against is a phrase that lands cruelly, and criterion 1 removes those at curation time, once, for everyone, before anyone is hurt. It also cannot be made to work cleanly: removal would have to be silent, yet the reactor sees their own reaction in the control's text and would learn of it anyway, and a removal the reactor can undo by reacting again is not a remedy. **If `REACTION_SET` is ever curated loosely enough that this control starts to look necessary, the set is the defect.**

### The architecture side

**`reactions` gains `set_at` and `expire_content` sweeps on it**, rather than only cascading from a deleted post. ARCHITECTURE §15 item 8 records it as a shape lesson rather than a bug fix: every other expiring thing in this system hangs off a parent that expires, and the reaction was the one child whose parent could outlive it — so a job written from the cascade alone is correct for every row it will ever see in testing and wrong for the only case that matters.

**`REACTION_SET` is a table, not a constant.** SPEC §8.2.3 requires that a retired phrase stop being offered while existing reactions keep rendering it, which a Python literal cannot express and an admin editor cannot edit. The new `reaction_phrases` row carries text, display order and an `active` flag, on the same "deactivating beats deleting" discipline as `url_allowlist`.

**Found while there and fixed: ARCHITECTURE's constants paragraph was wrong about more than reactions.** It said the SPEC §14 constants live in one `constants.py`, while `HASHTAG_VOCAB`, `NAME_BLOCKLIST` and the URL allowlist had had tables of their own in §4 since the first draft. §4 now states the carve-out — **the operator-curated *sets* are tables; the numbers are constants** — which is the distinction SPEC §14's ✎ mark already draws, and which is what stops a builder putting a curated list in `constants.py` and then finding the admin editor has nothing to edit. **Two more were flagged and deliberately not invented:** `THEME_SET` and `DEFAULT_AVATAR_SET` are operator-curated and both get an admin editor at BUILD_PLAN Step 13.3, and §4 gives neither a table — whether a theme is a database row or a file the operator deploys is a real question, it was outside this prompt, and it is queued rather than answered.

### What was not done, and why

**BUILD_PLAN Step 7.2 was not rewritten.** It is two lines describing a section that is now three subsections, and it is genuinely stale — but prompt 09 syncs the build plan against a settled SPEC, and TODO's "run 09 last" rule exists so those steps are written once. This is the precedent set at 1.19, where prompt 03 handed its build steps to 09 rather than doing them. The items are itemized in `prompts/09-sync-arch-and-buildplan.md` so the sync session does not have to reconstruct them from this entry.

**One error in the prompt, recorded so nobody hunts for it.** Prompt 10 twice asks for enough detail "for Phase 8 to be built." Reactions are **Phase 7**, Step 7.2; Phase 8 is Profile Pages and Theming. The work landed against Phase 7 regardless.

**Nothing was reopened that the prompt placed out of scope:** no counts anywhere, author-only visibility untouched, no free text and no arbitrary emoji, reactions still never render in a list view, and whether reactions should exist at all was not revisited.

### Working files (outside the record)

`TODO.md`: prompt 10 marked done at 1.25; one sync item added for prompt 09 covering Step 7.2, the `reaction_phrases` table and the two amended jobs; the `REACTION_SET` curation recommendation noted against the Phase 10-style content step so it reaches the founder at the moment the list is actually written.

---

## 1.24 — 2026-08-18

| File | Status |
|---|---|
| README.md | changed — version header only; no content change |
| SPEC.md | changed — §2 (the `/healthz` ruling, as a pointer), §18 (rule ownership, the citation convention, and the declined split) |
| ARCHITECTURE.md | changed — header gains a citations line; Decision 1 reason 4 and §3.1 leg 3 reworded; 50 cross-document references relabelled `SPEC §x`; §7.3 and §15 item 6 record the `/healthz` ruling |
| BUILD_PLAN.md | changed — header gains a citations line; Appendix lead-in states the document defines no rule of its own |
| CHANGELOG.md | changed — this entry |

From prompt 08, the lowest-priority item in the queue, whose expected outcome was "possibly nothing." It is close to nothing, and the reason is worth more than the edits.

**The finding.** ChatGPT called this the biggest long-term risk in the project, above any product or technical concern: SPEC specifies implementation details that are architectural decisions, those details also appear in ARCHITECTURE, and a change to one document before the other produces conflicting sources of truth. The prompt for this session went further and said it was already happening, citing four rules stated in three or four places each.

**The inventory, built before any edit, because the prompt made that the gate.** Roughly thirty to forty rule *families* are stated in more than one document — not the dozen that would have made this trivial, nor the hundred that would have made it somebody else's session. But the count is the wrong measure, and finding that out is what decided the session. **The remedy ChatGPT's finding points at is already the house convention, at scale:**

- **ARCHITECTURE cites `SPEC §x` 148 times.** BUILD_PLAN cites SPEC 121 times and ARCHITECTURE 56. Every Appendix rule already names its owner — rule 10 cites SPEC §7.8 invariant 4, rule 11 cites ARCHITECTURE §4.
- **SPEC's own discipline is perfect.** Of its 679 section references, **zero** point outside SPEC without naming the document. Where SPEC hands off, it says so ("Mechanics: ARCHITECTURE §7, build-plan Step 5.5").

So the answer to *"when the same rule is stated in three places and one of them changes, how does anyone notice?"* is that the citation already tells a reader which copy is the definition — in almost every case. What this session found was the exception, and it is a different defect from the one reported.

**The real defect: ARCHITECTURE's section numbers collide with SPEC's, and 14 of its references resolved to the wrong section.** ARCHITECTURE used a bare `§x` for both its own sections and SPEC's. The two documents' numbering overlaps across most of its range, so `§7.2` is *Content rules and the URL allowlist* in one document and *What keeps it running* in the other; `§5.4` is *Blocking* and *Asking in bulk*; `§6` is *Groups* and *The housekeeping jobs*; `§13.3` is *Reported-content lifecycle* and *The privacy rules at scale*. **179 references sat on numbers that exist in both documents**, and fourteen of them sent a reader — or a model that was handed only ARCHITECTURE — into the wrong section of the wrong subject. Four samples, all now fixed: *"the URL allowlist editor (§7.2)"*, *"≤30 members (§6)"*, *"hard cap 90 days (§13.3)"*, *"the audience picker with its live ≤30 count (§7.3)"*.

That is the "conflicting sources of truth" risk in a form nobody predicted: not two documents disagreeing, but a citation that lands in the wrong one. It is also exactly what the prompt's own recommended remedy fixes, and fixing it deletes nothing and decides nothing. **50 references in ARCHITECTURE were relabelled `SPEC §x`**, each classified individually rather than by pattern; the convention is now that a bare `§x` always means the document you are reading, and it is stated in SPEC §18 with pointers from both other headers.

**The split ChatGPT proposed was tested on its own four examples and declined — three of the four do not survive it.** The proposal was to divide each rule in two: SPEC keeps *"editing must perform the same validation as creation"*, ARCHITECTURE takes *"implemented by routing both through the shared validator."* Clean as a principle. Against the passages:

- **SPEC §7.8 invariant 4 (edit-path revalidation).** The line is already drawn where the proposal wants it. SPEC states the rule, what is revalidated, and why a create-only validator fails *silently*; the implementation half — *"validation belongs to the model/form layer that both paths share, never to the create view"* — appears **only** in ARCHITECTURE §7.1. What is stated four times is not the rule but the *argument*, and the prompt's own point 4 is why: an instruction a builder can skip is not made safer by being shorter. Nothing to move.
- **SPEC §4.6.1 (credential security).** Partly a misreading, and the correction matters: **SPEC does not specify hashed codes or attempt caps** — those live in ARCHITECTURE §4's `credential_codes` row and §7.1 alone. SPEC says *single-use, time-limited*. Of what SPEC does name, **SPF/DKIM/DMARC at `p=reject` already ends with the citation the proposal asks for**, and it is a policy with a user-visible consequence rather than a mechanism. Only **Argon2id** is a clean split candidate — and the project already settled that boundary in the other direction at v1.18, when ARCHITECTURE §7.1 recorded that *"framing a mandatory dependency as an approved exception invites a later builder to treat it as optional."* Removing the name from SPEC would reopen a question already closed, and would be a content change besides.
- **SPEC §7.9, *"one string per post, not a per-viewer computation."*** Read as a performance instruction, which is how it sounds. **In context it is the privacy rule of the bullet it sits in** — *"derived from the post's own type and tags, never from the viewer"* — restated in implementation vocabulary, in a section whose other three rules are *never a number*, *never the audience itself*, and *never an oracle*. A line that varied by viewer would leak. Split off as performance, it would be deleted from the one document that needs it. **The wording invites the misreading and was left alone anyway**, because rewording it is a content change and this session makes none; it is queued.
- **The single-shared-helper rule (SPEC §4.5.1, §7.5.1, §8.1).** The one case with teeth: *"one shared helper"* is a code-structure instruction, and the behavioural half ("every surface renders the same thing; content never shows a stale name") survives without it. It was still not moved, and the reason is three lines above it in the same document: **SPEC's Purpose line promises that "a developer or an AI coding model with no access to prior conversations must be able to build from this document alone."** A SPEC that names the guarantee and withholds the one instruction that makes it checkable fails its own stated purpose. Whether that promise is the right one is a real question and a substantive one; it is queued rather than answered here.

**The changelog discipline was evaluated honestly and needs nothing (the prompt's item 5).** It is doing its job and can be shown doing it: `BIO_CHANGE_COOLDOWN_HOURS` and `BIO_EDIT_GRACE_MINUTES` were retired in SPEC §14 at v1.16 and are still live instructions in five places across ARCHITECTURE and BUILD_PLAN — **and TODO.md names all five, by section, with a warning not to start Phase 2 until prompt 09 clears them.** The drift was caught, recorded and queued by exactly the mechanism 1.17 built. What the status table makes visible is an unsynced *file*; it was never going to make an unsynced *rule* visible, and nothing in this session's findings asks it to. No new procedure was added, and the one that exists was not touched.

**`/healthz` and SPEC §2 — the boundary question TODO handed to this prompt. Founder decision 2026-08-18: SPEC §2 does not name the route.** §2's rule is about *pages*; an endpoint returning the literal body `ok`, with no HTML, no template, no theme and nothing about any user, is not one. ARCHITECTURE §7.3 owns the endpoint and already carried the argument; **SPEC §2 gained a pointer to it rather than a restatement of it**, which is the citation convention applied to the first case that came up under it. §7.3 and §15 item 6 now record the question as answered rather than open, and §7.3 states what a *future* unauthenticated route must meet — the test, not this route's precedent.

**Found while there and deliberately not fixed:** SPEC §2's list is narrower than the built system in a second way, unrelated to `/healthz`. The privacy policy and accessibility statement are linked from login (BUILD_PLAN §15.1, §15.2), and **SPEC §16.1's own scope line names a different three pages than §2 does** — "login, password reset, invite redemption" against "login/registration/invite-acceptance." Correcting a normative list is a content change; it is queued in `TODO.md`.

### The second item — reasoning that will not age well

**Adopted as recommended, and it was smaller than expected: two paragraphs.** ChatGPT's point was that decisions justified as "easier for AI models" will read as dated in five years, and that "sub-Fable" names a model generation that is already meaningless outside this project. Checked across all four documents, **"sub-Fable" appeared exactly twice, both in ARCHITECTURE** — Decision 1 reason 4, and §3.1 leg 3 of the Django argument. SPEC §2 already used the durable phrasing the reviewer asked for ("less capable AI models"), so the outlier was two sentences, not a theme.

**What was done, and what was deliberately not.** Both paragraphs now lead with the reason that holds whoever writes the code and keep the AI-capability reason **named** rather than removed:

- **Decision 1 reason 4** becomes *"Fewer moving parts, so fewer places to be wrong"* — a property of the design, not of its builder — with SPEC §2's requirement kept as the named second reason.
- **§3.1 leg 3** becomes *"Strong conventions and secure defaults — the safest stack for whoever assembles it"*, and says in the text why the AI argument is stated second: **the leg stands without it, which is why it is not the leg's name.** The training-data argument is retained in full, in the same paragraph.

**Nothing was scrubbed.** The AI-capability argument is a real and honest reason, this project's whole method depends on it, and deleting it would make the documents less honest — which is the objection this project makes to every other cosmetic tidy. **README was left alone**: its "written to be executable by AI models" is a description of how this repository actually works, not a justification for a technical choice, and it names no model generation. **BUILD_PLAN's tool names were left alone** — Step 1.3 and Step 2.4 name Claude Code as an example, hedged with "e.g." and "any capable coding agent works," which is an installation instruction rather than an argument.

### What was not done, and why

**No rule was moved, no reasoning was deleted, no section was renumbered, and no product or technical question was decided.** Three things surfaced that would have required a substantive decision, and all three are queued rather than taken: whether SPEC's Purpose line should promise buildability from SPEC alone (which is the real question under ChatGPT's finding), whether SPEC §7.9's performance-sounding clause should be reworded to the privacy rule it actually states, and whether SPEC §2's list should be corrected to match what is genuinely reachable logged out.

### Working files (outside the record)

`TODO.md`: prompt 08 marked done at 1.24; the `/healthz` note resolved with its answer; the three queued questions added; one sync item added for prompt 09 (both ARCHITECTURE's and BUILD_PLAN's `Companion to:` lines still cite per-file SPEC versions — v1.15 and v1.7 — a scheme retired at 1.17, and they were left alone here precisely because they carry honest information about staleness that only the sync can clear).

---

## 1.23 — 2026-08-18

| File | Status |
|---|---|
| README.md | changed — header status field only, to the new approval vocabulary; no content change |
| SPEC.md | changed — header status field only; no content change |
| ARCHITECTURE.md | changed — header status field only; no content change |
| BUILD_PLAN.md | changed — §0.2 rules 3 and 5, new §0.6, new §0.7, Step 1.2, Step 2.4 rewritten, Appendix lead-in and rules 1 and 4 |
| CHANGELOG.md | changed — this entry, three new preamble sections, and one annotation added to the 1.16 entry |

From prompt 07, and it answers the same question from nine directions: **what happens after an AI stops.**

**The finding, and what survived checking it.** Two reviewers of 1.16 reached the same place from opposite sides. ChatGPT: the law-file locks are excellent protection against AI drift, but "the AI cannot even produce a proposed correction," and proposed a **Design Review Mode**. DeepSeek: the rule "assumes the AI will recognize when it needs to change a law file. It won't." Checking both against the documents found the mechanisms **stronger than ChatGPT credited** — four layers at §2.4, the founder's filename glance at §0.2 rule 3, and four Appendix rules each ending in "stop and say so." **The gap was never the lock. It was that there was nothing on the other side of it.** §0.2 rule 5 said "stop — that's a design conversation," and the plan ended there: nothing said what the AI should produce when it stopped, where that went, how it became a document change, or how the build resumed. On a project where the founder is not the coder, **the handoff is the mechanism**, and it was the one part not written down. The live proof was in this repository the whole time: `prompts/` and `TODO.md` exist *because* there was no defined way to route a document question out of a working session, so a route was invented on the spot and never recorded.

**One decision refused, and it is the reason the rest is small.** ChatGPT's "Design Review Mode" is not adopted **as a mode**. Design sessions have been running here for twenty-two versions; there is nothing to switch on, and the founder is the switch — a session is a design session because he opened it as one. What was missing was not a mode but a **route into one from a build session**. So the answer is one artifact rather than a state machine, and the practice that already existed is simply written where a build session will read it (**new BUILD_PLAN §0.7**). Every design prompt to date has had to declare its own exemption from §0.2 rule 5 in its opening paragraph; that stops being necessary.

**The stop note.** Five fields, printed in the chat, under a screen: the step, the sentence in the way (verbatim, or an honest "no sentence — SPEC does not cover this, it would belong in §7.4"), what could not be done, the smallest change that would resolve it, and the state of the working tree. **Never applied, never committed, and no files written** — a session that has just stopped is the last one that should be creating artifacts, and in any case `prompts/` and `TODO.md` live in the other repository. Three acts follow and only the middle one is the founder's: the AI prints and stops, the founder pastes it into `TODO.md`'s new stopped-steps table, and it is later opened as a design session by pasting the note back in. **The note is deliberately not a prompt file.** It already carries what `prompts/README.md` asks of one — step, finding quoted, wall, proposal — in miniature; a full prompt file gets written only when the question turns out to be bigger than the note, which is the exception. The alternative considered and rejected was having the build session write a prompt file directly: it lands in the wrong repository, and it asks a model that has just hit a wall to produce a two-screen design document, which is the wrong size by an order of magnitude.

**The cheap test for whether a stop is real, and its honest limit.** A model saying "this contradicts SPEC §7.4" is the system working; a model saying "I can't do this" because it is confused, or has found a design it likes better, looks identical from where the founder sits. The rule adopted is one line: **a stop note must be falsifiable by reading one named place in one named document.** Search for the quoted sentence — found and it says what the note claims (real), not found (the model guessed; not a stop, re-run the step), found but meaning something else in context (one paragraph of reading settles it), or a "no sentence" note whose named section turns out to cover the case after all (not a stop). Stated plainly in the document: **this does not detect motive, and nothing can.** What it does is convert an unanswerable question — *is this model being straight with me* — into an answerable one: **is there a sentence, and does it say that.** If the conflict is real the motive stops mattering, and a verbatim quote is cheap to check and expensive to fake, which is all a test at 10 p.m. needs to be. Two permitted forms rather than one, because **gaps are the commonest true stop** — far more common than contradictions — and a format that only accepted quotes would push a model to manufacture one.

**A distinction §0.2 rule 5 had blurred.** That rule read every refusal as the system working — "it means the model wanted to move a goalpost." But an AI that *reports it could not edit a law file* **tried and was refused**: a deny rule fired, the hook rejected a commit, the tripwire went red. That is the lock working, and it is now also a rule violation, because the instruction is to stop and write a note rather than to attempt the edit. An AI that produces a stop note **did not try** — that is the plan working. Two different events with two different reactions, and they should not feel the same.

**The discovery loop.** DeepSeek's separate point — the plan "assumes that everything you'll need in step 12 is known at step 1" — is granted. A genuinely missing step is **inserted with a letter at the point of need** (Step 6.2a, which this plan has already done once), **never by renumbering**: renumbering would falsify every git commit message, every reference here and every prompt filename, and those are *history* rather than text one is free to correct. Appending to the end of a phase remains available where nothing depends on the new step, which is the rarer case — a step that turns out to be missing is usually missing *before* something. Four rules ride with it: letters do not nest; **the founder writes it into BUILD_PLAN, not the AI** (the discovery loop makes no exception to §0.2 rule 5); **it gets its own ✅**, since a step nobody can write a verification for is not a step but an unfinished design question — a free test of whether the insertion is ready; and the preceding step's verification is re-run once the new step is built. The loop is not a separate mechanism: it is one of the **four things a stop note resolves into**, alongside a SPEC/ARCHITECTURE change, a corrected prompt (no version bump — no law file changed), and nothing at all.

**DeepSeek's harder point, which the locks do not touch at all: code that quietly diverges from SPEC.** The guards stop the AI editing the *documents*; nothing stops it writing code the documents never asked for, while every step-level verification passes — because those verifications test the feature that was just built, not its conformance to the spec. **New §0.6** generalizes the one pattern in this plan that already worked: Step 4.2 has the founder read the visibility engine's test *names* and check they read like SPEC's rules restated, auditing coverage without reading code. At each phase milestone, in the sitting that already runs §0.4's browser matrix and §0.5's scan, the founder reads two columns — **A**, the SPEC and ARCHITECTURE sections this phase's steps name, and **B**, the sections this phase's tests cite (Appendix rule 4 now requires every test to cite one, which is what makes column B exist). **A section in A and not in B is the finding.** Step 4.2 keeps its deeper read; §0.6 is what scales to seventeen phases.

**And §0.6 states what it does not catch, because an overstated guard is worse than a stated limit.** A test that cites the right section and asserts the wrong thing is invisible to this check and to the founder, and **nothing in this plan catches it** — that sentence is in the document, not only here. Behaviour the code has that no document mentions opens no gap in either column. A rule right in the test's world and wrong on the page is only partly covered, by the founder's own hand-run ✅ verifications, the milestone browser matrix, and eventually the first users (ARCHITECTURE §9). What the check genuinely proves is that **every section the phase was meant to implement was thought about by name**, which is the failure that actually happens: a clause gets no code, therefore no test, and nothing anywhere goes red.

**Founder approval — the act that makes a document stop being a draft** *(founder-raised, not from any review)*. Nine versions of "DRAFT pending founder review" with no defined act to change it, and exactly two approval records in the whole project, both ad hoc and both buried. The scheme is in this file's preamble; three things about it are worth recording here.

- **The recommended shape needed one correction to work.** The proposal was to compare the approval version against the project version in the header. That fails: under the 1.17 scheme *every* file's header carries the current project version whether or not that file changed, so README would read as stale every time SPEC moved. The comparison is against the file's own **"This file last changed in"** number, which already sits on the next line of the same header — machinery that existed and was not being used. Two adjacent numbers, one comparison, and **the staleness marker maintains itself**: last-changed moves whenever the file changes, approved-at moves only when approval is renewed, so nobody has to remember to mark anything stale. It follows that **editing a header's status field does not count as the file changing**, or approving a file would instantly mark it unapproved.
- **Approval bumps nothing**, and this is the load-bearing rule: if approving 1.22 produced 1.23 then 1.23 would be unapproved and the process would never converge. It is the one edit in this project that changes files without a version bump — permissible because its content is fully specified in advance and mechanical: one header field, one annotation line, nothing else. It does trip the checksum tripwire, like any other founder-authored law-file change, and the fix is the same single `shasum` command.
- **The versioned record is now stated rather than assumed.** Five files. `TODO.md` and `prompts/` are **working files, explicitly outside it**, and the reason is structural rather than tidy-minded: the status table exists to make an *unsynced* document visible, and neither of them can be unsynced with anything. Earlier entries varied — 1.17 changed `TODO.md` silently, 1.22 gave it a table row — and **neither is corrected**, because entries are appended and not rewritten, which is now a stated rule with two narrow exceptions, both additions rather than rewrites.

**The tripwire paradox** *(Kimi 10, which the earlier two reviews missed)*. SPEC §1.3 permits raising a cap, so the *correct* act of raising `FRIEND_CAP` turns the suite red — and the fix, editing the tripwire's expected value, is the exact action the guard exists to make suspicious. §2.4 now defines the sequence: **SPEC §14 first** in a design session, then `constants.py`, then the tripwire, then the checksums, **all in one founder-authored commit with `--no-verify`** — and **a constants assertion that fails at any other time is a real alarm.** Two things make it navigable rather than alarming. The two assertions now **fail differently and say so**: a checksum failure means *a document changed* and is expected after every design session, while a constants failure means *`constants.py` changed* and is expected only inside that sequence; both failure messages are specified verbatim, as the checksum one already was. And §2.4 now says plainly that **there are three copies of every constant** — SPEC §14, `constants.py`, the tripwire — which is the price of the alarm and is deliberate: a tripwire that read SPEC's table would agree with SPEC by construction and would therefore assert nothing about it. This is the same shape of problem as the approval flow above — a legitimate act that trips a mechanism built to catch illegitimate ones — and the answer is the same in both cases: name the legitimate sequence, and make everything outside it an alarm.

**Which guard survives a change of tool** *(Kimi 10's second half)*. Stated plainly in §2.4, and the honest answer is not flattering. **Guard 1 does not survive**: the deny rules live in one tool's settings file, and a different assistant, a web interface or a manual paste finds them simply absent — **with no refusal appearing, because there is nothing left to refuse.** Re-creating them is now named as the first task of adopting any new tool, with the step's ✅ as the proof. **Guard 2 survives a tool change but little else** — `--no-verify` skips it, and `.git/hooks/` is not cloned, so a fresh clone on a new machine silently has no hook at all; the script therefore lives in the repository with a one-line install command in the README. **Guard 3 survives everything and prevents nothing** — an ordinary test that goes red at the next step for anybody, and the only tool-agnostic guard that cannot be bypassed. **Layer 4 is what is actually being relied on**: outside copies and diffable git history, whose one requirement is that somebody looks, which is what §0.2 rule 3's five-second filename glance is — and why that glance is less of an afterthought than it looks.

**Is CHANGELOG.md a law file? Yes — with one honest qualification the recommendation did not carry.** It is now the fifth law file (§0.2 rule 5), it travels to the build repository with the other three (Step 1.2), and it is in the deny rules and the checksums (§2.4). The reasoning holds: a build session has no legitimate reason to touch it, because a build step that wants to change the changelog is by definition a design conversation, so the protection costs nothing where the writing happens. Two arguments strengthen it beyond the original case — a coding model asked to tidy up after itself **reaches for a changelog by habit**, which is exactly the accidental edit guard 1 is good at; and a build repository *without* one invites an AI to create a **rival changelog** that diverges silently. **But the guards do not reach the place the file is actually at risk.** It is written in every design session, in the design repository, which has no deny rules and no hook by design. What protects it there is a discipline and a diff — appended, not rewritten, two exceptions, `git diff CHANGELOG.md` as the check — which is why that rule is in this file's preamble as well as in §2.4. Saying the guard covers it would have been the overstatement this project keeps refusing to make.

**One gap found while writing the resume path, which no reviewer raised.** §2.4 told the founder to re-bless the checksums after a design conversation and to commit the blessing "alongside the changed document" — but **nothing anywhere told him to carry the changed document across from the design repository to the build repository at all.** Step 1.2 copies the law files once, at the very beginning, and that was the only copy instruction in the plan. A build session reading a SPEC three versions stale would look exactly like everything working. §0.7 now closes with the three acts that resume a build — copy, re-bless, commit with `--no-verify` — and Step 1.2 says the copy is not a one-time act.

**Deliberately not done.** No lock was weakened: the deny rules, the hook, the tripwire and the rule that an AI never edits a law file during a build step all stand, and the only change in that direction is that the list of protected files got longer. `constants.py` values remain founder-only, through SPEC §14 first. Nothing in SPEC or ARCHITECTURE was touched, this being a BUILD_PLAN session; the one place that needs a matching sentence — ARCHITECTURE §9, which should carry Appendix rule 4's new requirement that every test cites its section — is handed to prompt 09 in `TODO.md`, along with a note that SPEC Appendix A's own 2026-07-07 approval record stays as it is, being a record of a specific act rather than a status line.

### BUILD_PLAN.md

**New §0.7, "Two kinds of session, and the one route between them,"** carries the build/design distinction, the stop note's five fields and three rules, the three-act route, the thirty-second falsifiability check, the four things a stop note resolves into, the discovery loop, and the three acts that resume the build. **New §0.6, "The standing conformance check,"** puts the two-column section-number read on the same milestone cadence as §0.4 and §0.5, with its limits stated. **§0.2 rule 3** adds CHANGELOG.md to the filename glance and states that an unfinished step is not committed. **§0.2 rule 5** becomes the single definition of the five law files, adds CHANGELOG.md with its reason, points at §0.7 for what happens after a stop, and separates a reported refusal from a stop note. **Step 1.2** copies four documents rather than three and says the copy repeats. **Step 2.4 is rewritten**: CHANGELOG.md in the deny rules and the checksums, a second specified failure message for the constants assertion, the four-step cap-raising sequence, the three-copies note, the hook's absence from a fresh clone, a paragraph on which guard survives a change of tool, a paragraph on where CHANGELOG.md is and is not protected, and a ✅ that tests the newest member of the list. **Appendix**: a lead-in defining "stop and say so" as §0.7's stop note, rule 1 requiring the verbatim quote or an honest statement that no sentence exists, and rule 4 requiring every test to cite the section it enforces.

### CHANGELOG.md

Three new preamble sections — **what the versioned record covers** (five files; `TODO.md` and `prompts/` outside it, with the reason), **founder approval** (the two header forms, the comparison against the file's last-changed number, per-file, bumps nothing, the trigger sentence and the two edits it authorizes, and its independence from external review), and **entries are appended, not rewritten** (with the two permitted additions). The **1.16 entry gains an external-review annotation**, which is the first use of that mechanism and is an addition to an existing entry rather than a rewrite.

### README.md · SPEC.md · ARCHITECTURE.md

Header status field only, from "DRAFT pending founder review" to `DRAFT — not yet founder-approved`. No content changed in any of the three. BUILD_PLAN's header, which had said "under founder review," now uses the same words as the others — the divergence being small evidence for the whole item.

### Working files (outside the record)

`TODO.md`: prompt 07 marked done at 1.23; a new **stopped-steps table** for §0.7's route, empty until the build starts; new sync notes for prompt 09. `prompts/README.md`: "Two kinds of session" reduced to a pointer at BUILD_PLAN §0.7 now that the distinction lives there, and stop notes described as the second kind of input to the queue.

---

## 1.22 — 2026-08-18

| File | Status |
|---|---|
| README.md | unchanged — version header only |
| SPEC.md | changed — §16.1 (new §16.1.1), §16.5 rewritten (new §16.5.1), §17 |
| ARCHITECTURE.md | changed — §3.8 (one bullet), §9 (the accessibility block and the tooling bullet), §15 (new item 7) |
| BUILD_PLAN.md | changed — §0.1, §0.3, new §0.5, §2.5, §8.2, §15.2, new §15.3, Phase 16 header, §16.5 rewritten, §17.3 (new runbook section 13), Appendix rule 9 |
| CHANGELOG.md | changed — this entry |
| TODO.md | changed — prompt 06 marked done; two triage rows annotated with their outcomes; the Kimi #9 row resolved; one new parked question; one new sync item for prompt 09 |

Two items, from prompt 06, and both were places where §16 said something softer than the commitment it sits under.

**The reviewer finding, and what survived checking it.** DeepSeek's review of 1.16 claimed accessibility testing here is manual only, with no automated scanning, and that focus order, keyboard operability, screen-reader announcements and error associations go untested. **Most of that was wrong**, and had already been recorded as wrong: BUILD_PLAN §16.5 pass 1 ran an axe/`pa11y` scan, ARCHITECTURE §9 specified template smoke tests and a contrast test over every theme, and passes 2–4 were the keyboard, screen-reader and zoom checks the reviewer said were absent. What survived was the *second* half of the objection, which is DeepSeek 22's rather than 17's: **every one of those checks was a gate, run once, immediately before launch**, in a project whose build plan ends at Phase 17 while SPEC §17 promises features keep arriving. Accessibility regressions are the easiest defects to introduce and the hardest to notice — nothing looks wrong, no test fails, nobody files a bug, and the person who can no longer use the page simply stops using it, on a network a family member invited them to.

**Checking the claim exposed a real defect the reviewer had not found.** The prompt for this session asserted that two thirds of the mechanical checks already ran continuously and only needed saying so. **Half of that was true.** The `THEME_SET` contrast test is built at Step 8.2 and has been a genuine continuous test since themes existed. **The template smoke tests were built nowhere:** ARCHITECTURE §9 specified them, and BUILD_PLAN's only mention of them was inside Step 16.5 pass 1 — so a check described in one document as a *test* was, in the document that builds things, a *gate run once*. They now belong to **Step 2.5**, with the base template and the shared partials, which is the first step that renders a page worth asserting anything about. Recorded in ARCHITECTURE §15 item 7 as the pattern it is: **a test one document specifies and the other never builds is indistinguishable, from inside either document, from a test that exists.**

**Four decisions, all taken in session on 2026-08-18** (the third had been taken by the founder before it).

1. **Conformance runs on three clocks, not one gate.** *Continuous* — the contrast test and the template smoke tests, on every change forever. *Per milestone* — the axe/`pa11y` scan. *Periodic* — the three human passes, on triggers. SPEC §16.5 now says this in those terms; it previously described only a pre-launch audit, which hid the fact that part of the work was already continuous and disguised the fact that the rest of it was not.
2. **The axe/`pa11y` scan joins the milestone cadence and stays out of the test suite.** ARCHITECTURE §9 had kept it as optional local tooling on the reasoning that nothing accessibility-related ships to the browser — good reasoning, but it answers a question nobody was asking here. **SPEC §15.2 is satisfied either way**, under every option considered; what rules the scan out of the suite is dependency weight alone — a headless Chromium and a Node toolchain in a Python project's test path, needing a running server. So it runs at each phase milestone from a documented command on the founder's Mac, which turns a third of real problems from a once-ever catch into a dozen. The reasoning is written into §9 so it is not re-proposed as an app dependency by a future session.
3. **The human passes are run by a qualified tester, not the founder** — the founder's decision, brought to this session already taken, from Kimi's finding 9. §16.5 had asked the founder to run a screen-reader pass while BUILD_PLAN §2.5 taught only how to switch VoiceOver on. **A screen-reader pass is a skill, not a setting**, and it was the only quality gate before launch. **Qualified** is defined in SPEC §16.5.1 with a stated preference: a person who uses a screen reader daily as their primary means of using the web, paid for their time, before a professional auditor — an auditor reports that an accessible name is missing, a daily user reports that the page cannot be used, and the second is the question this section actually asks. The real cost of the decision is not wording but **scheduling**: Phase 16 had quietly assumed the founder was available to himself, so **new Step 15.3** books the person, starting during Phase 13.
4. **The operator console is a bounded commitment** (SPEC §16.1.1), chosen over an explicit exemption and over full scope.

**On the operator console specifically**, since it is the decision most likely to be re-opened by a future reader. §16.1 said the Django admin was "held to the same standard as far as the framework allows; where it falls short, the shortfall is the operator's own, not a user's." A reviewer called that a cop-out, which is too strong — the reasoning is real and the distinction is genuine on a platform with exactly one operator. But **the sentence stated no obligation**: "as far as the framework allows" is satisfied by doing nothing, in a section whose opening sentence is that a feature which cannot be made accessible is not shipped. Two facts made it worth settling rather than leaving: **the operator will not always be this founder** (§15.3 contemplates funding phases, §2 contemplates going public), and **§13's operator duties are daily-use surfaces** — the moderation queue, the vocabulary editor, the URL allowlist editor with its redirector checks, the request queue — not a settings page visited twice.

- **In scope, over those four surfaces:** keyboard operability with no traps, a visible focus indicator, text contrast, programmatically labelled fields, and errors identified in text. Verified once at Step 16.5, in the sitting already being paid for, in about an hour.
- **Out of scope:** everything else, and the reason is stated rather than implied. Conformance would mean **owning Django's admin templates** — forking an upstream that must stay patched for security, or replacing the admin with a hand-built operator interface. **That is a stack-level reversal, not a §16 tweak:** ARCHITECTURE §3.1 leg 2 makes "the Django admin is the operator console for free" one of the five reasons Django was chosen. Full scope was weighed on those terms and rejected.
- **The consequence is acknowledged, not assumed away.** *"The operator is me and I can see fine"* is a statement with an expiry date. If the role is ever held by a person the admin excludes, the project has committed to solving it **then** — by building the operator surfaces as first-party pages, feasible because they are a small number of list-and-act screens — and **never by an overlay**, since §16.4's ban is not narrower for the operator's own screens. A deferral with a named trigger and a named remedy is a decision; the old sentence was not.
- **And the claim says which.** The accessibility statement names the carve-out in one sentence, because "we conform to WCAG AA" with a silent exclusion inside it is exactly what §16.5's honesty rule exists to prevent.

**The re-audit rule was kept deliberately small, and the tester decision is why.** A rule that assumed a free afternoon reads differently once every run costs another person's time and calendar — which is the strongest argument for modesty, not against it. The human passes repeat on **a new interactive pattern** (scoped to that pattern and its flows, never a full sweep) and **before any widening of who can join** (in full, scheduled with the attorney review that SPEC §15.1 requires at the same moment). **A new page built entirely from the shared partials of ARCHITECTURE §3.8 is explicitly not a trigger** — which is the first time this project has written down a practical reward for the single-source discipline rather than only its obligations. A third trigger is reactive: an accessibility report through §13.5 that the continuous checks did not catch re-audits the *pattern*, not just the page. Alongside them sits **one founder-run keyboard-and-reflow check a year**, in the sitting that already exists for the restore rehearsal, and it is honest about what it is not: it does not replace the tester, and its purpose is the opposite one — the site stands still while browsers, iOS and VoiceOver move underneath it.

**The accessibility statement is now a living document**, which was the last loose end and the one that would have quietly falsified everything else. §16.5's honesty rule forbids papering over a known defect; a statement written once and never revised **becomes a false claim by standing still**, so the same rule forbids letting it go stale. It carries a visible revision date, and its maintenance is a runbook item rather than an intention.

**Two things follow from the decisions and are answered rather than left to be discovered.** First, **a re-audit runs on the live system.** The launch audit is harmless — it precedes Step 17.1's wipe, so nothing the tester sees belongs to anybody — but there is one server and no staging copy, so every later run happens on a platform with real people on it. The answer taken: the returning tester holds **an ordinary member account whose only friend is the founder**, sees the founder's content and nobody else's, and is granted no operator view; where a pattern needs two participants, the second is the founder. An audit that required seeing strangers' content to be thorough would verify accessibility by breaking what accessibility is here to protect. Second, **the tester is now a single point of dependency**, in the same shape as the vocabulary's single operator (§11.2.1) and named the same way rather than solved: an unavailable tester **delays a re-audit and breaks nothing that already works** — the continuous checks keep running and shipped patterns keep behaving as verified. The fallback is the professional auditor, and a trigger that fired and was not run stays open as a known limitation, which puts it in the statement.

**Where the ongoing obligation lives.** BUILD_PLAN ends at Phase 17, and §17.3's operator runbook is the only page describing life after launch — so accessibility re-verification is now **runbook section 13**, beside the disk, the backups and the moderation queue. It carries the four things that outlive the build: what must stay green automatically, what repeats and on what trigger, what the founder does yearly, and the one queue item that is never read in a batch — an accessibility report, which is the signal that both the machine checks and the audit missed something, from the person being excluded, who will not send a second one.

### SPEC.md

(a) **§16.1's scope paragraph** stops asserting a standard for the operator console and points at **new §16.1.1**, "The operator console — a bounded commitment," which carries the named subset, the four surfaces, what is out of scope and why (with the §3.1-leg-2 argument stated in SPEC's own terms), the future-operator trigger and remedy, and the requirement that the statement name the carve-out.

(b) **§16.5 is rewritten** as "Verification, re-verification, and feedback": the three clocks, the re-audit rule with its three triggers, the yearly founder spot-check, the statement as a living document, the accessibility report as the un-batched queue item, and the honesty rule extended to cover a defect the tester finds and the founder cannot fix.

(c) **New §16.5.1**, "Who runs the human passes," carries the founder's decision, the skill-not-a-setting argument, the definition of *qualified* with its preference order and the reason for the preference, and the two consequences the build plan carries (the booking step, and the operator-console hour riding along).

(d) **§17** gains one clause: no full WCAG AA claim for the operator console, pointing at §16.1.1.

### ARCHITECTURE.md

**§3.8** gains a bullet stating the operator-console boundary as an *architectural* one, with the two builder consequences: the admin's templates are not forked to chase criteria, and the remedy if the role ever falls to someone the admin excludes is first-party operator pages, never an overlay. **§9's accessibility block** is rewritten to separate continuous from periodic, to give the smoke tests their build home at Step 2.5 and say plainly that they previously had none, and to name the tester. **A new bullet records the axe/`pa11y` decision in full** — including which constraint actually decided it — so it is not re-proposed. **§15 gains item 7**, the four decisions with their dates, in the format items 5 and 6 established.

### BUILD_PLAN.md

**New §0.5, "The standing accessibility checks,"** states the continuous and per-milestone cadences once, next to §0.4's browser matrix, rather than leaving them scattered. **§0.1** gains the `[FOUNDER + TESTER]` label, used exactly once and explained. **§0.3** names the one step that depends on somebody else's calendar. **§2.5** builds the template smoke tests and writes down the scan command; its verification adds them, and its VoiceOver instruction is re-labelled **familiarization, not verification**. **§8.2** says the contrast test is continuous. **§15.2** becomes a five-part statement with the carve-out and the living-document obligation. **New §15.3 [FOUNDER]** books the tester — who, when to start, what to send, what to book, and the standing relationship. **§16.5 is rebuilt**: what should already be true on arrival, six passes with their owners, the operator-console hour as pass 6, writing the claim, and setting the clock for next time. **§17.3** gains **runbook section 13**. **Appendix rule 9** gains the instruction that every step adding a page adds it to the smoke tests' page list.

### README.md

Unchanged apart from the project-version header. §2's invitation — *"if you use a screen reader, magnification, or keyboard-only navigation, your reading of §16 is the most valuable review this project can get"* — needed no amendment; this version is that sentence turned into a build step.

---

## 1.21 — 2026-08-17

| File | Status |
|---|---|
| README.md | unchanged — version header only |
| SPEC.md | changed — §11.2 (new §11.2.1), §7.9, §13.2, §13.5, §14, §17 |
| ARCHITECTURE.md | changed — §4 only (two table rows: `hashtag_vocab`, `reports`) |
| BUILD_PLAN.md | changed — Phase 10 header, §10.1, new §10.1a, Phase 10 milestone, §13.1, §17.3 (routine line + new runbook section 12) |
| CHANGELOG.md | changed — this entry |
| TODO.md | changed — prompt 05 marked done and its Touches column corrected; the parked vocabulary task rewritten with its decisions; one new parked question; the DeepSeek 3 triage row annotated with its outcome; one new sync item for prompt 09 |

One finding, from prompt 05, and the reviewer was right about the problem and wrong about both cures. DeepSeek's review of 1.16: hashtags are never free-typed, so **the operator is the single point of failure for all hashtag creation** — away for three weeks, nothing gets added; fifty suggestions in a week, fifty manual decisions. *"The exact kind of operational burden that kills solo projects."*

**Why it was worth a version even though curation was never in doubt.** §11.2 said users "may submit new-tag suggestions for operator review (§13.5)" and stopped there. Nothing said how long a suggestion waits, what the submitter is told, what happens to one that is never processed, or what the vocabulary looks like on day one. That silence is expensive **because hashtags are not decoration here**: §11.3 makes a profile hashtag one of three conditions for friend-of-friend visibility and §11.4 makes it the ranking signal on discover, so the vocabulary is the substrate of §1.1's second purpose. A user whose real interest has no tag is not inconvenienced — **they are invisible to precisely the people the platform exists to introduce them to, and nothing tells them that is why.** The load is also front-loaded in the worst way: suggestions peak in the first weeks, when the vocabulary is thinnest and the founder is busiest.

**The answer is content, not machinery, and the section says so in those words.** Most of this problem is solved by a starter vocabulary broad enough that suggesting a tag is the exception rather than the workflow. SPEC deliberately states **no size target** — it is not a cap, nothing enforces it, and a content number in a specification of behaviour would be the only one of its kind; the target lives in BUILD_PLAN Phase 10 where the writing happens. Four founder decisions, all taken in session on 2026-08-17:

1. **Starter vocabulary: ~300 tags, hand-written, across roughly twenty areas of life, every entry weighted toward things people do *with other people, offline*** (§1.1's measure of success). Importing and pruning a public taxonomy was considered and not chosen: taxonomies are built to classify, so they yield abstractions ("Transport", "Philosophy") that make poor interest tags, and pruning one is most of the hand-writing anyway. **The vocabulary is not written in this version** — it is Phase 10 content work, now with a target and a method.
2. **Search aliases — the change that does the most work.** Every vocabulary entry carries operator-curated synonyms: `#hiking` carries *hikes, rambling, trekking, trail walking*. Searching any of them finds the tag. **Aliases are never displayed, never selectable, and are not tags.** What this buys is not really search quality, it is the **decline path**: the commonest suggestion is a synonym for a tag that already exists, and without aliases declining it teaches nobody anything and the next user types the same word into the same empty result. With them, **the decline is the fix** — a declined suggestion normally becomes a permanent improvement to the picker. That is what stops the queue repeating itself, and it is the largest reduction in operator load in the section.
3. **A batching rhythm in the runbook, and no interval anywhere near a user.** The vocabulary is read **weekly, in the sitting that already exists** — §17.3's routine is already "read the digest, work the moderation/request queue," and a habit that needs no new habit is the only kind a solo operator keeps. Users are told the *rhythm* and never a time: submissions are read in batches, no reply is sent, an accepted tag simply appears in the picker. **Stating a cadence in the runbook costs an unread queue when it slips; stating one in the product breaks a promise.**
4. **Tag abuse is reported with a reason on the existing report action**, not through a new channel — see below.

**The two proposed cures are recorded in-document as rejected, per README's house rule** (§11.2.1, in the style of §4.5's rejected-uniqueness entry), so they do not arrive again as new. *"Auto-approve after three users suggest the same tag"* creates synonym fragmentation **automatically** — three people suggesting #hiking, #hikes and #trail walking are one interest arriving three times — removes the abuse screen at a bar of three coordinated accounts on a network where everyone holds invites, and would need its count kept off every user-facing surface (§17). Aliases are the version of that idea that works: repeated synonym suggestions are exactly the signal an alias is missing, and the operator acts on it without a new tag existing. *"Allow free-typed tags that only match if they are in the vocabulary"* is a text field that accepts input and silently does nothing — worse than a refusal, because the user believes they have tagged their post — and it reintroduces free text on a surface that carries none (§13.1).

**What is named as an accepted cost rather than solved (§7.8's model).** The operator remains a single point of failure and stays one; no mechanism removes that without giving up curation. It is survivable because of the *shape* of the load, not optimism: **a frozen vocabulary delays a new interest, it never breaks an existing one.** Every tag already on a profile keeps working, every §11.3 gate keeps evaluating live, discovery is unchanged for everyone already tagged. Three weeks away costs some new users some matches, later than they would have had them. Stated plainly, in both SPEC and the runbook.

**The one genuinely new requirement — reporting a tag that does not belong — turned out to need no new pipeline.** Founder-directed, following v1.18's settling of §11.3 on *any* shared tag: a post carrying ten tags reaches more friends-of-friends than one carrying one, which the founder accepts as correct and asked be reportable when abused. Three things made it small. **The vocabulary already bounds the abuse** — tags are never free-typed, so nobody invents `#freemoney`; the abuse available is **irrelevance**, over-tagging with real interests. **The reporter is a specific person on a specific surface** — the FoF who got the post *because* of the match, told so by §7.9's stated-visibility line — so the affordance belongs beside that line, and §7.9 says so without changing the line by one word. And **the report record already had somewhere to put it**: ARCHITECTURE §4's `reports` table has carried a `category` column all along.

Which exposed a drafting accident worth naming: **§13.2 gave *profile* reports a target category and a note in v1.16, while post and comment reports still carried only reporter, target and frozen copy** — so the operator opened a queue item with no idea what they were being asked to look at. That asymmetry was order-of-writing, not a decision. **v1.21 makes it one form, always carrying a reason**, with *the tags don't match this post* as one value among the ordinary ones. A §13.5 form category was the smaller-looking alternative and is **recorded as rejected**: it needs no build at all, but it makes the reporter leave the post and describe it from memory, it captures **no frozen copy** — and tags are editable (§7.8), uniquely able to change who can see a post, so evidence without a freeze can be edited away before the operator looks — and it would put one complaint into one queue in two shapes depending on how the user arrived. Two things are forbidden by name rather than left unbuilt: **no per-tag report count anywhere**, users' side or operator's ("a tag is not a thing that can be in trouble; a post is, and a person is"), and **no automated detection of irrelevant tagging**, on §13.2's own cost/benefit reasoning — relevance has no threshold, and a detector would misfire on the eclectic post, which on a platform for friends is most of the good ones.

**§17 gains a clause rather than an exception.** The picker searches a list, so the "no global search" rule had to be shown intact rather than assumed: querying `HASHTAG_VOCAB` returns **no person and no post**, and the same result goes to every user including one with no friends at all. Recorded the way §17 already handles the friend-list filter — which is admitted on a *different* ground, since it does search real people, but only the viewer's own 300.

### SPEC.md

(a) **§11.2 keeps its bullets unchanged and gains §11.2.1**, "The vocabulary as an operational commitment" — the starter-vocabulary argument and why no size is stated here, aliases and what they do to the decline path, the honest empty result and its §17 check, what the submitter is told, and the accepted cost of an absent operator.

(b) **§7.9** gains "Reporting a tag that does not belong," placed after the No-Reach paragraph: why irrelevance is the only abuse the vocabulary leaves available, why the affordance belongs beside the visibility line, and three bullets on what it does not become (the line unchanged, no per-tag count, no automated detection).

(c) **§13.2** gains "Every report carries a reason," ahead of the v1.16 profile-report paragraph it corrects the asymmetry with, including the frozen-copy argument and the rejected §13.5 alternative. **§13.5** gains "What the submitter is told," and its hashtag-suggestion bullet now names the alias outcome as the commonest one.

(d) **§14's `HASHTAG_VOCAB` row** records the aliases and states that no size target lives in SPEC. **§17's** no-global-search clause names the vocabulary search as not being one, with the reason.

### ARCHITECTURE.md

Two rows in §4, and nothing else — this version is a product decision, not an architectural one. **`hashtag_vocab`** gains search aliases, with the storage call recorded (on the row, not a table of their own: they have no identity apart from their tag and nothing queries them but that one search) and the three prohibitions restated where a builder will meet them (never rendered, never selectable, never joined to `profile_hashtags` or `post_hashtags`). **`reports`** records what its existing `category` column now carries, that v1.21 changed only which reports populate it, and that **no index or aggregate counts reports per hashtag**.

### BUILD_PLAN.md

**§10.1** specifies alias search and makes the empty result a built state rather than a leftover — honest text plus the suggestion link, never a text field that accepts a tag and fails to create one. **New §10.1a [FOUNDER]** is the starter vocabulary itself, with the ~300 target, the twenty areas, the offline-weighting rule, the write-aliases-as-you-go instruction, and a "done when" that tests the thing that matters: search each of ten interests the way five different people would phrase them and land on a tag every time. Phase 10's header becomes "[AI, with one FOUNDER content step]" and its milestone gains the picker checks. **§13.1** takes the report reasons and the placement rule, and says in terms that the column already exists so this is a form and a list of values, not a migration. **§17.3** adds **runbook section 12**, the weekly vocabulary pass — read as a batch because the batch is what makes synonym clusters visible, three outcomes in order of frequency, no reply ever sent, and the reminder that being away is survivable. The weekly routine line now names the suggestions.

**One question parked rather than answered**, recorded in §10.1a and TODO.md: **whether an LLM can draft candidate tags and alias sets for the founder to approve.** Worth trying, and it is **not** blocked by §1.3's "the platform never infers" — that rule governs what the running platform does with user data, and this is an operator writing a static word list at a desk, with no user and no user data anywhere in it. The conditions are written down so the trial stays honest: the founder approves every entry, nothing is loaded unread, and §10.1a's offline-weighting test is the acceptance bar.

### README.md

Unchanged apart from the project-version header. Nothing here changes what is or is not open to review.

---

## 1.20 — 2026-08-17

| File | Status |
|---|---|
| README.md | unchanged — version header only |
| SPEC.md | **unchanged — version header only, and deliberately so** |
| ARCHITECTURE.md | changed — §4, §6, §7 (subdivided, three new subsections), §8, §10, new §11.1, §13.3, §14, §15 |
| BUILD_PLAN.md | changed — header, §5.2, §5.4, §5.6, new §5.7, §15.1, new §16.6, §17.3, Appendix rule 7 |
| CHANGELOG.md | changed — this entry |
| TODO.md | changed — prompt 04 marked done; two notes re-aimed at the new §7 subsections; one boundary question added for prompt 08 |

One finding, from prompt 04, and it grew on inspection. DeepSeek's review of 1.16 said the ban on decrypting proxies left the project "exposed… with no DDoS protection layer" and "no mitigation plan." **That specific claim was wrong** — ARCHITECTURE §13.3 already separates network-level scrubbing (no decryption, included by Hetzner-class providers, handles the overwhelming majority of attacks) from application-level filtering (needs decryption, is what orange-cloud mode is, is the only thing knowingly given up), and none of that reasoning needed revisiting. **What checking it exposed was larger and nobody had raised it:** §13.3 lives in the *scaling* chapter, so a reader of §7 never met it, and §7 itself covered only what protects the data. A search of all four documents for monitoring, alerting, uptime or health checks returned nothing at all. README §3 has asked from the beginning *"what does a person who has carried a pager know that this plan forgot?"* — no reviewer answered it.

**Why this was worth a version.** Most outages here are survivable: the site is down, a friend mentions it, the founder restarts a container. **One class is not, and it is silent.** ARCHITECTURE §6 puts content expiry, inactivity warnings and deletions, invite replenishment and notification expiry in cron. A failing `expire_content` produces no error page and no complaint, because nothing a user can see is different — it produces a database quietly retaining content the platform promised to destroy. **The central promise of the project, broken invisibly, and discovered whenever somebody next happens to look.** Nothing in the documents would have caused anyone to look.

**SPEC was not touched, on purpose**, following 1.19's precedent: none of this is observable by a user. One SPEC-boundary question is deliberately left open rather than answered — whether §2's "no public pages except login/registration/invite-acceptance" should name `/healthz` — and handed to prompt 08.

**Three decisions were put to the founder** (ARCHITECTURE §15 item 6 records all three). One initially went against the recommendation and was then refined by the founder into a deferral, which is recorded in full because the difference between "declined" and "deferred with a named trigger" is the whole of whether it ever gets built:

1. **External monitoring: deferred with intent to build.** The recommendation was one free account doing both an uptime check and a heartbeat, on the argument that **a watchdog cannot live on the machine it watches**. The founder chose email alerts for launch — and, shown what that costs, **refined it within the same session** to *"email for now, but we should build out the watchdog later if this platform actually gets used."* That is a deferral, not the rejection the first answer read as, and the documents say so in those terms. The cost of the interim state stays in §7.3's body text rather than a footnote: `check_health` is itself a cron job and **cannot report its own death**, so a stopped machine produces an inbox indistinguishable from a healthy Tuesday. Three things follow.
   - The **weekly green digest** is the first-party substitute — a fixed-day email sent whether or not anything is wrong, so a *missing* email becomes the signal and the founder becomes the thing that notices.
   - **The trigger is named rather than felt**, because "later" is where deferrals go to die. Build it when **any one** of these is true: any public phase (non-negotiable, and it coincides with the attorney review SPEC §15.1 already requires); active users the founder does not speak with in an ordinary week — the condition is the relationship, not a number, and deliberately **not** a SPEC §14 constant; or **the first time a user reports an outage the founder did not already know about**, which is self-triggering and needs no judgment, being direct evidence that the human layer has already failed once.
   - **The deferral costs a signup and nothing else.** `/healthz`, `job_runs` and `check_health` are built at Step 5.7 regardless, so the eventual work is two monitors on one free account, about twenty minutes, and **no code change**. That is what makes the deferral honest rather than merely cheap — and it is why the design work belonged in this version even though the service does not.
   §7.3 carries all three, §14's row reads *deferred with intent to build*, and **build-plan §17.3 puts it on the operator runbook as a standing item (section 11)** rather than in a phase — it is triggered by the platform being used, not by a step being reached, and the runbook is the page still being read a year from now.

   *(Recorded here rather than as 1.21: the refinement arrived in the same session, on the same date, while 1.20 was still DRAFT. This follows 1.18's precedent, where a founder addition mid-session was "folded in here rather than deferred.")*
2. **Disk: the 80 GB instance, warn at 75%, alarm at 90% — approved**, with the growth arithmetic in the new §11.1.
3. **Nothing wakes the founder — approved.** This is the decision that keeps the whole thing one page rather than an incident-response programme, and it is why there is no escalation tier to configure and later ignore.

**Two findings the prompt did not ask for, both from reading the documents rather than from any review.**

- **The backup encryption key had only one copy, and it was on the server.** §8 said secrets live "in an environment file on the server"; §10 said backups are encrypted with restic. Together those sentences mean that losing the machine loses the key, and what survives is a storage bucket of ciphertext nobody can ever open. **Neither restore rehearsal would have caught it** — a founder rehearsing a restore copies the key off the server that morning and never notices it was the only one. Fixed in §8, §10 and Step 5.6, with the rehearsal itself now required to use the password-manager copy.
- **DNS TTL is part of the recovery path.** §13.2's disaster recovery ends in "repoint DNS," and at a registrar's default TTL that last step adds most of a day to every recovery. A 300-second TTL set once at Step 5.2 costs nothing.

### ARCHITECTURE.md

(a) **§7 is subdivided rather than renumbered**, following exactly what 1.19 did to §5: the section stays §7, so every cross-reference in all four documents survives, and it gains **§7.1 what protects the data** (the existing bullets, text unchanged), **§7.2 what keeps it running**, **§7.3 knowing when something has broken**, and **§7.4 DDoS at v1**. The section title becomes "Security Posture, and Staying Up," and its opening states why both belong there: to a user they are the same question asked twice, and the two failures that matter most on this platform are a leak and a promise quietly not kept.

(b) **§7.2 — what keeps it running.** The two recovery numbers are stated rather than implied, because "we have backups" is heard by almost everybody as "we lose nothing": **up to 24 hours of loss** (backups are nightly) and **recovery in hours, most of them the founder being asleep**. Then the cheap structural answers: `restart: unless-stopped` on every container with Docker enabled at boot — the highest-value availability line in the project, since a crashed worker, an OOM kill and the reboot after an automatic security update all recover with nobody awake; Compose healthchecks on `app` and `db`; the 300-second DNS TTL; and **no standby server, with the reason** (it covers host death, which provider redundancy largely covers anyway, and does nothing for the failures that actually happen — a full disk, a bad migration, a mistake). The database subsection names one ordering fact worth knowing at 2 a.m.: **Postgres refuses writes on a full disk, so the disk alarm is a database alarm arriving early.** The email-provider subsection carries the sharpest new rule in the section — **a job records an email as sent only once the provider has accepted it**, so idempotency makes the next run a retry rather than a skip, and **deletion at `INACTIVITY_DELETE_DAYS` requires the warnings to have actually been sent**. Marking a send complete before acceptance would let a provider outage erase an account whose owner was never warned, which is SPEC §4.8's legally serious case failing silently. Finally the **maintenance page**, in Caddy because Caddy stays up when the app does not, at **503 with `Retry-After`** and never 200, and subject to SPEC §16 like any other user-facing surface.

(c) **§7.3 — knowing when something has broken.** Failures are sorted into three kinds by how loud they are on their own — loud by itself (someone tells you; at twenty users the friends *are* the uptime monitor), loud if asked (disk, error rates), and **silent always** (a job that stopped). The mechanism is small and first-party: a **`job_runs` table** written by every §6 command in a `finally` block, **content-free by design** — it counts, it never names, so §15.2 has nothing to object to; **`check_health` daily**, comparing each job's newest success against a deliberately loose window (hourly late at 3 hours, daily at 26, weekly at 8 days) and emailing **only when something is wrong**; and the **weekly digest** described above, whose *weekly* cadence is itself argued — a daily green email is read for a fortnight and ignored forever after, and an alarm that gets ignored is worse than no alarm because it is still believed to be working. **Disk** warns at 75% and alarms at 90%, and the threshold is chosen against the *human* recovery time rather than the machine's: attaching a volume or resizing takes a person with a day job days of calendar time, so the warning has to be weeks of runway. **What an alert may contain** is a privacy rule as much as an operational one: counts and exception types only, never a request body or a traceback with local variables, and **Django's `mail_admins` is explicitly not used as it ships**, because its emails carry request data and would send a user's own post text off the server to the mail provider — an operational alert becoming exactly the leak §7.1 exists to prevent. **`/healthz`** is specified tightly: unauthenticated, 200 and the literal body `ok` when one `SELECT 1` succeeds, 503 otherwise, **and nothing else** — no version, no counts, no JSON, no timestamps, no user table, no session — so that it can never become an oracle for whether this platform exists, has users, or holds any particular person. It is argued not to be a *page*, which is why it does not contradict SPEC §2, with that boundary call handed to prompt 08. The subsection ends with the two things named as accepted rather than overlooked: **the unwatched machine** — deferred with intent to build, with its three triggers and its twenty-minute build spelled out, and with the honest note that this platform may stay at twenty friends forever and that this is an acceptable outcome — and **the circularity** that every alert leaves over the email provider, which is itself one of the things that can fail.

(d) **§7.4 — DDoS at v1**, promoted from §13.3 and kept deliberately short. What the provider includes and why it is compatible with the TLS rule; what is knowingly given up (application-level filtering, which is what an orange-cloud proxy is); what already stands in for it (login required everywhere but three routes and `/healthz`, login backoff, fail2ban, §13.6 rate limits, and the ability to stop the app); what the founder actually does, in order, ending in a fresh IP and a DNS repoint the 300-second TTL makes quick; and **the honest part** — a determined application-layer attack on a prototype for friends is survivable downtime, not a catastrophe, and saying so is the correct posture where buying machinery whose real product is reassurance is not. §13.3 keeps its scaling argument intact and gains a pointer down to §7.4.

(e) **Smaller placements.** §4 gains the `job_runs` table. §6's intro gains the two new job rules (the `finally`-block row and the email-acceptance rule) and its table gains `check_health` daily and `check_health --digest` weekly. §8's secrets sentence gains the off-server-key exception. §10 gains the 24-hour loss statement and the key cross-reference. **New §11.1** carries the disk arithmetic — a per-user table separating what expires from what does not (profile photo, `GALLERY_MAX` = 8 and up to `PIN_LIMIT` = 10 pinned images never expire; everything else is a 90-day rolling store), the ~3 MB stored figure that corrects the instinct to multiply by `IMAGE_UPLOAD_MAX_MB` = 20, and the two numbers that decide the purchase: 100 users ≈ 10 GB, **500 users ≈ 50 GB, which does not fit the 40 GB instance the cheapest tier ships**. That answers README's "what breaks first at 500 users" with something specific: not the CPU, not the database — the disk. §14 gains **six rejected or deferred rows** (the external monitoring service as *deferred*; Prometheus/Grafana; a daily all-clear email; `mail_admins` as shipped; a hot standby; a public status page). §15 gains item 6 with all three founder decisions and their reasoning.

### BUILD_PLAN.md

Five existing steps changed and two added, all folded into existing phases per the prompt's instruction and prior practice. **§5.2** takes the 80 GB disk and sets the DNS TTL to 300 seconds. **§5.4** gains the three compose/Caddy availability lines — restart policy, capped container logs, the 503 maintenance page — with a "done when" that includes stopping the app and rebooting the machine. **§5.6** gains **2b**, the password-manager step for the backup key, and its rehearsal now must use that copy rather than one taken off the server, because otherwise the rehearsal quietly tests the wrong thing. **New §5.7** builds `job_runs`, `/healthz`, `check_health` and the digest, placed in Phase 5 because the founder is already in server-configuration mode and because the failure it guards has no symptom. **§15.1** records that the outside-party list is two at launch and **expected to become three**, instructs that the policy be written so adding the monitoring service is a sentence rather than a rewrite, and keeps the honest qualifier that such a service is **not** a processor of user data. **§17.3's runbook gains an eleventh section**, the standing item to build the watchdog, with its triggers. **New §16.6** breaks four things on purpose (stop the database, skip a job, trip the disk warning by lowering the threshold rather than by actually filling a production disk, stop the app) and then checks the negative case, that a healthy day sends nothing at all: an untested alarm is a rumor in exactly the way an untested backup is. **§17.3** turns the weekly routine into reading one email, states that a missing digest is itself the finding, and **specifies the runbook's ten sections** rather than leaving them to a future session — including the one people forget, section 7, telling "this job failed" apart from "cron itself has stopped." **Appendix rule 7** gains the `job_runs` requirement and the email-acceptance rule.

### SPEC.md, README.md

Unchanged apart from the project-version header. SPEC's status is deliberate and follows 1.19: this version added an operational posture, and nothing in it is observable by a user. The one place SPEC arguably *could* change — §2's list of public pages, against `/healthz` — is left to prompt 08, which owns the SPEC-versus-ARCHITECTURE boundary, rather than decided in passing here.

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

**External review — annotation added 2026-08-18, under the scheme introduced in 1.23.** Version 1.16 of README.md, SPEC.md, ARCHITECTURE.md and BUILD_PLAN.md was reviewed by three outside models: **ChatGPT** (8 findings, `1.16_ChatGPT_review.md`, 2026-08-03), **DeepSeek** (27 findings, `1.16_DeepSeek_review.md`, 2026-08-03) and **Kimi** (12 findings, `1.16_Kimi_review.md`, 2026-08-04). All 47 were checked against the document text and triaged into `TODO.md`, which records what happened to each one; the reviews became prompts 01–12 and the versions 1.17 onward. **This changed no document's authority.** Every one of them still said "DRAFT pending founder review" throughout, which is the state that made external review a *CHANGELOG event* rather than a status in the first place. Two calibration notes kept because they cost nothing and are easy to forget: ChatGPT and DeepSeek both certified that no internal contradictions existed, and Kimi then found three, all verified — a reviewer's summary judgment is not evidence; and of the three reviews, only Kimi's had no factually wrong finding in it.

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
