# Prompt 07 — What happens when the build meets a wall

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** BUILD_PLAN.md §0.2, §2.4 and the Appendix; the status line in all four document headers; CHANGELOG.md; possibly `prompts/README.md`
> **Depends on:** prompt 01.
> **Expected outcome:** a defined path from "the AI stopped" back to "the build continues," and a defined act that moves a document from DRAFT to founder-approved.

---

You are working in the WeeBee design-document repository. Read `README.md`, then
`BUILD_PLAN.md` in full — §0 and the Appendix especially — then `CHANGELOG.md`'s preamble
and its 1.17 entry. Skim `SPEC.md` §14 and `ARCHITECTURE.md` §5 so you know what the law
files actually contain. This is a **founder-directed design session**; you may edit
BUILD_PLAN.md, and — for item 7 only — the status line in the other three document headers
and CHANGELOG.md.

## The finding

Both external reviewers of version 1.16 arrived at the same place from opposite
directions.

ChatGPT:

> The AI is forbidden from ever modifying SPEC, ARCHITECTURE, BUILD_PLAN, constants.py,
> with multiple technical mechanisms preventing it. This is excellent protection against
> accidental AI drift. However, software design always uncovers mistakes… Now the AI
> cannot even produce a proposed correction. I might allow a dedicated **Design Review
> Mode** where the AI may propose document edits without applying them.

DeepSeek, on the same rule:

> This assumes the AI will recognize when it needs to change a law file. It won't. The AI
> will generate code that violates the spec, and you'll have to manually fix it.

And separately, on the one-step-at-a-time rule:

> It assumes that everything you'll need in step 12 is known at step 1. In practice you'll
> discover missing steps as you build. Add a "discovery loop" rule.

## What the documents actually say

The mechanisms are stronger than ChatGPT credits. §2.4 installs four layers — tool deny
rules (the harness refuses regardless of what the model decides), a pre-commit hook, a
constants tripwire test, and the authoritative copies living outside the repo. §0.2 rule 3
adds the founder's five-second glance at changed filenames. Appendix rules 1, 9, 10 and 11
each end with "stop and say so."

**The gap is not the lock. It is that there is nothing on the other side of it.** §0.2 rule
5 says "stop — that's a design conversation, not a coding task," and the plan ends there.
It does not say what the AI should produce when it stops, where that goes, how the founder
turns it into a document change, or how the build resumes. On a project where the founder
is a non-developer and the AI is doing the coding, the handoff *is* the mechanism.

There is also a live proof that the gap is real: **this repository now has a `prompts/`
folder and a `TODO.md` precisely because there was no defined way to route a document
question out of a working session.** That was invented ad hoc. It should be written down.

## What to work out with the founder

1. **A proposal format.** When an AI step hits a wall, what does it emit? Recommend a
   short, fixed shape: the step it was on, the exact SPEC/ARCHITECTURE sentence in
   conflict, what it was unable to do, and the smallest change that would resolve it —
   written as a *proposal*, never applied. Keep it short enough that a tired founder reads
   it at 10 p.m.

2. **Where the proposal goes.** The obvious answer, now that the machinery exists, is a
   new file in `prompts/` plus a row in `TODO.md`. That turns "the AI stopped" into a
   queued design conversation instead of a dead end, and it uses the same route as every
   other design change. Confirm or replace.

3. **Distinguishing the two reasons an AI stops.** A model saying "this contradicts SPEC
   §7.4" is the system working. A model saying "I can't do this" because it is confused,
   or because it wants an easier design, looks identical from the outside — and BUILD_PLAN
   §0.2 rule 5 already frames a refusal as evidence "the model wanted to move a goalpost."
   The founder needs a cheap test for which one it is. Requiring the proposal to quote the
   conflicting sentence verbatim is probably that test: a confused model cannot produce a
   real quote that actually conflicts. Work out whether that holds.

4. **The discovery loop — inserting a missing step.** Decide the rule for a genuinely
   missing step found mid-build. The plan is numbered and sequenced, so the options are
   insert-with-a-letter (Step 6.2a, which the plan has already done once and which avoids
   renumbering) or append-to-the-phase. State it, and state the accompanying rule: a new
   step is added by the founder to BUILD_PLAN, not by the AI, and the preceding
   verification is re-run.

5. **DeepSeek's harder point: code that quietly diverges from SPEC.** This is the risk the
   locks do not cover at all. The guards stop the AI editing the *documents*; nothing stops
   it writing code that implements something the documents do not say, while every
   step-level verification passes — because those verifications test the feature that was
   just built, not its conformance to the spec.

   The plan's existing answer is partial and worth noting: Appendix rule 3 forbids bare
   numbers in favour of `constants.py` names, §2.4's tripwire asserts every constant's
   value, and Step 4.2's milestone has the founder read the visibility test *names* and
   check they read like SPEC's rules restated. That last one is the good pattern — the
   founder audits coverage by name, without reading code.

   Decide whether that pattern generalizes: a per-phase check where the founder reads test
   names against the relevant SPEC sections. Be realistic about what a non-developer can
   actually verify, and be honest in the document about what remains unguarded. An
   overstated guard is worse than a stated limit.

6. **Whether "Design Review Mode" needs a name.** ChatGPT proposes it as a mode. The
   simpler framing is that design sessions already exist — this repository has been running
   them for sixteen versions — and what was missing was the route *into* one from a build
   session. Decide whether BUILD_PLAN §0 should describe the two kinds of session
   explicitly (build sessions, where the law files are locked; design sessions, where the
   founder directs changes to them), because right now the documents describe only the
   first and every design session has to declare its own exemption ad hoc. **That is a
   small change with unusually good returns** — it makes the existing practice legible.

7. **Founder approval — the act that makes a document stop being a draft.** *(Raised by the
   founder, not by the reviewers.)* Every document has said "DRAFT pending founder review"
   for nine versions and there is no defined act that changes it. The founder wants to be
   able to record that he has read a file end to end and signed off, to send a version out
   for outside eyes, and to mark a file finally approved.

   The evidence that this is missing: the whole project contains exactly **two**
   founder-approval records, both ad hoc and both buried — ARCHITECTURE's old status line
   ("1.3 and earlier approved as a whole by founder 2026-07-08", now in CHANGELOG's 1.7
   entry) and SPEC Appendix A ("All ten were reviewed and confirmed by the founder on
   2026-07-07"). Neither is findable, and nothing has been approved since.

   Points to settle:

   - **Founder approval and external review are independent facts, not two rungs of one
     ladder.** v1.16 was reviewed by ChatGPT and DeepSeek — both review files are in this
     repository and 35 findings were triaged into `TODO.md` — while every document still
     said "DRAFT pending founder review." Any three-state ladder that puts external review
     *after* founder approval cannot represent a state this project has already been in,
     and will be in again.

   - **Recommended shape: the header records founder approval and the version it was given
     at.** `**Project version:** 1.18 · <date> · founder-approved at 1.17` — when the file
     changes and approval is not renewed, the mismatch between the two numbers is visible
     at a glance. That is the same mechanism that makes an unsynced document visible, which
     is the whole reason 1.17 exists. `DRAFT` before first approval. Approval is **per
     file**, since SPEC will be approved long before ARCHITECTURE is synced to it.

   - **External review becomes a CHANGELOG event, not a status.** "v1.16 reviewed by
     ChatGPT and DeepSeek" is a thing that happened to a version, and belongs in that
     version's entry. It does not change a document's authority; only the founder's
     approval does. A reviewer looking for what is open to challenge reads README's "What
     IS up for review", which already exists for exactly that job.

   - **Approval must not bump the project version.** If approving 1.17 produces 1.18, then
     1.18 is unapproved and the process never converges. State that approval is an
     annotation on an existing CHANGELOG entry plus the header line, and bumps nothing.
     This rule is load-bearing — without it the scheme eats itself.

   - **The trigger is a sentence in chat; the record is the file.** Settle the words the
     founder says to make it official, and confirm that a session receiving them writes the
     CHANGELOG annotation and the header line and nothing else.

   - **Settle what the versioned record actually covers.** CHANGELOG.md names README, SPEC,
     ARCHITECTURE, BUILD_PLAN and itself. `TODO.md` and `prompts/` are changed by almost
     every design session and appear in no entry — including 1.17, which changed `TODO.md`
     without recording it. Decide whether they are inside the record or explicitly outside
     it as working files, and say which in CHANGELOG's preamble either way.

8. **The tripwire paradox, and what the guards actually depend on.** A third reviewer of
   v1.16 raised two points about §2.4 that the earlier reviews missed.

   - **The tripwire has no defined "expected failure" path.** Guard 3 asserts every SPEC §14
     constant's exact value, and SPEC §1.3 explicitly permits raising a cap (caps are
     raise-only by design). So the *correct* act of raising `FRIEND_CAP` makes the test
     suite fail, and nothing tells the founder whether that failure is the system working or
     something broken. Worse, the fix — editing the tripwire — is the exact action the guard
     exists to make suspicious. Define the sequence: SPEC §14 changes first in a design
     session, then `constants.py`, then the tripwire, all in one founder-authored commit,
     and state that a tripwire failure at any other time is a real alarm. This is the same
     shape of problem as item 7's approval flow — a legitimate act that trips a mechanism
     built to catch illegitimate ones.
   - **Two of the three guards are tool-specific.** The deny rules live in Claude Code's
     settings; a different assistant, a web interface, or a manual paste bypasses them
     without any refusal appearing. The pre-commit hook is the only tool-agnostic guard, and
     prompt 02 item 6 already records that it is the weakest of the three. Say plainly in
     §2.4 which guard survives a change of tool, so the founder is not relying on a lock
     that quietly stopped applying. Do not overstate the fix — the honest answer may be
     "layer 4 (diffable git history) is what actually survives," which §2.4 already lists.

9. **Is CHANGELOG.md a law file?** *(Founder-raised during the 1.17 session; deferred to
   here.)* §2.4's guards protect SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md and `constants.py`.
   CHANGELOG.md did not exist when that list was written and is now part of the versioned
   record — arguably the most sensitive part, because it is the file that makes an unsynced
   document *visible*. A changelog quietly rewritten to say ARCHITECTURE was synced when it
   was not would defeat the mechanism 1.17 was built to create.

   **The tension is real and it is why this was not decided unilaterally:** protecting the
   file stops an AI rewriting history, but the file must also be *written* in every design
   session — which is exactly what the deny rules block.

   **Recommendation: add it, and let the repository split do the work.** §2.4's guards are
   installed in the **build** repository (`thenetwork`) — the deny rules are its
   `.claude/settings.json`, the hook is its pre-commit hook. Design sessions run in the
   design-document repository, which has no deny rules at all. A build session has no
   legitimate reason to touch the changelog, because a build step that wants to change it is
   by definition a design conversation. The protection lands where the risk is and costs
   nothing where the writing happens.

   Two things to get right if the answer is yes:

   - **The list is enumerated in four places**, not one, and they must not drift: BUILD_PLAN
     §0.2 rule 3 (the founder's filename glance), §0.2 rule 5 (the prohibition itself), §2.4
     guard 1 (the deny rules), and `prompts/README.md`'s "Two kinds of session". Item 6 may
     be about to move that last one into BUILD_PLAN, which would reduce this to three.
   - **§2.4's ✅ verification is part of the change.** It currently checks that an attempted
     edit to SPEC.md is refused. A fifth protected file that nothing verifies is not
     protected.

   This interacts with item 7's last bullet: if `TODO.md` and `prompts/` are ruled *inside*
   the versioned record, the same question arises for them — and the answer is probably
   different, since build sessions may legitimately need to file a discovery-loop proposal
   into `prompts/` under item 2.

## Constraints to respect

- **The locks stay.** No proposal weakens the tool deny rules, the pre-commit hook, the
  tripwire test, or the rule that the AI never edits law files during a build step. The
  question is what happens *after* a stop, not whether stopping is required.
- **`constants.py` values are founder-only**, always. A proposal may suggest a value; only
  the founder changes one, and only through SPEC §14 first.
- **Proportion.** This is a solo builder with a day job. A process with more than about
  three steps will not be followed, and an unfollowed process is worse than none.

## Before you finish

- Write the CHANGELOG.md entry, naming every file's status including unchanged ones.
- Update `TODO.md`, and update `prompts/README.md` if this session changes how prompt files
  are meant to be written or filed.
