# Prompt 08 — Where SPEC ends and ARCHITECTURE begins

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md (potentially all three, lightly)
> **Depends on:** prompt 01.
> **Expected outcome:** possibly nothing. This is the one prompt in the queue where
> "we looked, and the current arrangement is right" is a likely and acceptable result.
> **Priority:** lowest in the queue. Skip it if time is short; it is hygiene, not a defect.

---

You are working in the WeeBee design-document repository. Read `README.md`, then `SPEC.md`
and `ARCHITECTURE.md`. This is a **founder-directed design session**; you may edit both.

## The finding

ChatGPT, reviewing version 1.16, called this the biggest long-term risk in the project —
above any product or technical concern:

> The SPEC repeatedly specifies implementation details that are architectural decisions
> rather than product behavior… Those also appear in ARCHITECTURE.md. That means changing
> an implementation detail may eventually require editing both documents… If one changes
> before the other — even temporarily — you'll have conflicting sources of truth. That
> isn't happening yet, but it's the direction the documents are drifting.

**It is happening.** This is not speculative:

- **The edit-path revalidation rule** is stated in full, with its security argument, in
  SPEC §7.8 invariant 4, ARCHITECTURE §7 (link validation), BUILD_PLAN Appendix rule 10,
  and BUILD_PLAN §16.1. Four independent statements of one rule.
- **The single-shared-helper rule** is in SPEC §4.5.1 and §7.5.1, ARCHITECTURE §4, and
  BUILD_PLAN Appendix rule 11.
- **SPEC §7.9** specifies "one string per post, not a per-viewer computation" — a
  performance and implementation instruction, in the product specification.
- **SPEC §4.6.1** specifies Argon2id, SPF/DKIM/DMARC at `p=reject`, hashed single-use
  codes with attempt caps. All of it is also in ARCHITECTURE §7.

And ARCHITECTURE and BUILD_PLAN were, at the moment this prompt was written, both stale
against SPEC v1.16 — which is precisely the failure mode ChatGPT describes, already
realized once.

## The argument on the other side, which the session must take seriously

The duplication is not accidental and it is not obviously wrong:

- **README's second paragraph** says these documents are "written to be executable by AI
  models." A rule stated in exactly one place, in a 900-line document, read by a fresh
  session that was given a different document, gets missed. The redundancy is a
  reliability measure.
- **The redundancy is where the reasoning lives.** SPEC §7.8 invariant 4 does not merely
  say "revalidate on edit" — it explains that a create-only validator fails *silently*,
  which is why a builder must not treat it as optional. Deleting the argument to avoid
  duplication would leave a bare instruction that is much easier to skip.
- **The "defective implementation" phrasing** appears repeatedly and deliberately across
  the documents. It reads like emphasis; it functions as a tripwire for a model that would
  otherwise take the cheaper path.

So the honest question is **not** "how do we remove duplication." It is: **when the same
rule is stated in three places and one of them changes, how does anyone notice?**

## What to work out with the founder

1. **Designate a normative home per rule, not a wholesale reorganization.** Recommend
   this framing before any others. For each rule that appears in more than one document,
   name the document that owns it; the others keep their prose but gain an explicit
   citation making clear they are restating, not defining. Nothing is deleted, and a future
   reader can tell which copy to change first. This is a light pass with most of the
   benefit.

2. **Build the inventory first, and stop there if it is small.** Before proposing any
   edit, list the rules that are stated normatively in more than one document. If the list
   is a dozen items, the problem is smaller than the reviewer thinks and the answer is
   twelve cross-references. If it is a hundred, that is a different conversation and
   deserves its own session rather than a decision made at the end of this one.

3. **The line to draw, if one is drawn.** ChatGPT's proposed division is clean and worth
   testing against real cases: SPEC says *"editing must perform the same validation as
   creation"*; ARCHITECTURE says *"implemented by routing both through the shared
   validator."* Try it on three or four actual passages and see whether the SPEC half
   survives losing the implementation half — or whether the argument dies with it. Report
   what you find. **If the division damages the documents, say so and stop.**

4. **Resist any change that loses reasoning.** README's stated purpose for the versioned
   record is that rejected suggestions keep their reasons. The same instinct applies here:
   a shorter SPEC that no longer explains why a rule exists is a worse document, not a
   cleaner one.

5. **The maintenance answer may be procedural rather than structural.** CHANGELOG.md now
   names every file's status per version, including "unchanged" — which exists precisely to
   make drift visible. It is possible that the changelog discipline from prompt 01 already
   solves most of what ChatGPT is worried about, and the documents need nothing. Evaluate
   that honestly before proposing edits.

---

## Second item — reasoning that will not age well

ChatGPT, separately:

> Many design decisions are justified as "easier for AI models"… The risk is five years
> from now. Future contributors won't necessarily care what Claude or GPT liked in 2026.
> Where possible, phrase decisions as "reduces overall complexity" instead of "AI performs
> better." The reasoning becomes timeless.

The clearest instance is ARCHITECTURE §3.1, leg 3 of the five-leg Django argument:

> **It is the safest stack for AI-built software.** … Sub-Fable models will make fewer and
> less dangerous mistakes in Django than in a stack that requires assembling ten libraries
> by hand.

"Sub-Fable" names a specific model generation. It will be unreadable within a couple of
years and is already meaningless to anyone outside this project. README's fifth paragraph
carries the same framing more mildly.

The judgment to make:

- **The AI-capability argument is a real and honest reason**, and this project's whole
  method depends on it. Scrubbing it would make the documents *less* honest, which cuts
  against everything else in them.
- **But it is rarely the only reason.** Every one of these choices also reduces complexity
  on its own merits — one language, one CSS file, no build step, no frontend framework,
  strong conventions, secure defaults. Those reasons hold whoever or whatever writes the
  code.

Recommend: lead with the durable reason, keep the AI reason as a named supporting one, and
replace model-generation references with something that does not expire ("less capable
models" rather than a product name). This is a wording pass over a handful of paragraphs,
not a restructuring. It costs an hour and it is worth doing regardless of what item 1
decides.

## Constraints to respect

- **Delete nothing that carries a reason.** Rejected-alternative records, "accepted cost"
  paragraphs and "considered and declined" entries are load-bearing by design.
- **No content changes.** This session moves and cross-references; it does not decide any
  product or technical question. If a boundary question turns out to require a substantive
  decision, stop and queue it as a new prompt.
- **Do not renumber sections.** Every document, both reviews, this prompt queue and the
  entire changelog reference sections by number.

## Before you finish

- Write the CHANGELOG.md entry, naming every file's status including unchanged ones. If
  the outcome was "no change," record that too — a considered no is worth as much as a
  change, and it stops the question returning.
- Update `TODO.md`.
