# Prompt 07 — What happens when the build meets a wall

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** BUILD_PLAN.md §0.2 and the Appendix
> **Depends on:** prompt 01.
> **Expected outcome:** a defined path from "the AI stopped" back to "the build continues."

---

You are working in the WeeBee design-document repository. Read `README.md`, then
`BUILD_PLAN.md` in full — §0 and the Appendix especially. Skim `SPEC.md` §14 and
`ARCHITECTURE.md` §5 so you know what the law files actually contain. This is a
**founder-directed design session**; you may edit BUILD_PLAN.md.

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
