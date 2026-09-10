# Prompt 15 — Reporting a contact card

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** SPEC §10.2, §10.3, §13.2, §13.3, §13.4, possibly §14; ARCHITECTURE §4;
> BUILD_PLAN Steps 9.1, 9.2, 13.3.
> **Depends on:** 13 (done, landed in 1.29).
> **Blocks:** BUILD_PLAN Step 9.1's `link` item kind, which carries a 🚧 gate naming this prompt.
> **Expected outcome:** a contact card is a reportable object, and the gate on Step 9.1 lifts.

---

You are working in the WeeBee design-document repository. Read `README.md`, then SPEC.md
§5.2, §10.1–10.4, §13.2, §13.2.1, §13.3, §13.4, and §9.5. Skim ARCHITECTURE.md §4
(`contact_items`, `contact_overrides`, `card_requests`, `reports`) and §5 (the visibility
engine's `visible_contact_card`). This is a **founder-directed design session**; you may
edit SPEC.md, ARCHITECTURE.md and BUILD_PLAN.md.

## Why this session exists

Version 1.29 gave contact cards two things they never had: **a link item that may carry any
URL**, and **a free-text label on every item**. Both are author-chosen content delivered to
another person. Neither is reportable, because **a contact card is not a reportable object
anywhere in SPEC** — §13.2's report actions live on posts, comments and profiles.

That was tolerable when a card held a phone number, an email address and a messenger link
from an allowlisted domain. It is not tolerable now, and the precedent is in the document:
in v1.16 §13.2 put a report action on the **friend-request card** for exactly this reason,
and stated the rule this session inherits — *a report the recipient cannot reach is not a
defence.*

**SPEC §10.2 and BUILD_PLAN Step 9.1 both carry the gate:** the `link` item kind does not
ship until this lands. The founder's decision (2026-09-07) was to specify the link and label
rules in 1.29 and design the report path separately rather than badly.

## The hard part, so you do not have to find it

**A card is per-requester** (§10.3). What the owner shows today is not what the reporter
received: the cascade is default → group override → individual override, and the owner can
change any of it the moment a report is filed. So an operator opening a card report must see
**the version that reporter actually got**, or the evidence is whatever the reported person
last decided it should be.

**The shape of the answer already exists twice in this document, and they are different
shapes — pick deliberately, do not blend them.**

- **§5.2's friend-request card** freezes the photo and short bio at *send* time, and §9.1
  carries the complete frozen/live field split, which it calls **a security boundary rather
  than a rendering choice**. Note what that costs: a frozen copy of an image is storage that
  outlives nothing, which is why §5.2 also had to give pending requests a 90-day expiry.
- **§13.3's report freeze** captures the target at *report* time, with an appeal window and a
  hard cap (30 / 90 days) and a purge-by date. §13.2's profile report already freezes a
  render — *"the profile as it appeared to the reporter"* — which is the closer analogue,
  because it is a freeze of a **per-viewer** view.

**Freezing at report time is very probably right** and §13.2's profile report is the model,
but the session should say why rather than inherit it: a card is answered automatically on
request (§10.4), so a send-time freeze would mean storing a copy of every card every friend
ever requested, forever, against a report that will almost never come. Test that reasoning
before adopting it.

## What has to be decided

1. **Where the report action lives.** A received card is the output of a request (§10.4) —
   is it a page the requester can return to, or a one-time reply? The answer determines
   whether "report this card" is reachable at all after the moment it arrives, and it may
   force a small change to §10.4.
2. **What the frozen copy contains.** The resolved items *as delivered* — kind, value, label
   — and nothing else. Follow §9.1's precedent and say explicitly what renders **live** (the
   owner's display name, per §4.5.1's rule that names are never stored on content) and what
   is frozen. State it as a field list, not a description.
3. **A target category**, as §13.2's profile report has one. Candidates: *the label · the
   link · the item itself · this person's behaviour.* Keep the list short and operator-useful.
4. **Purge.** The frozen card inherits §13.3's freeze lifecycle (appeal 30 days, hard cap 90)
   unless there is a reason it should not. Check the reason before writing it down.
5. **What an upheld report does.** §13.2.1 defines delete-content / warn / ban. "Delete
   content" on a card item is not defined anywhere: does the operator remove the item, blank
   the label, or act on the account? Say so — this is the same gap §13.2.1 was written to
   close for posts.
6. **The engine.** Card resolution lives in `visible_contact_card` (ARCHITECTURE §5). A
   frozen copy is a rendering of that function's output at a moment; make sure the freeze
   calls the engine rather than re-resolving the cascade itself, which would be Decision 4
   broken in a new place.

## Constraints

- **Do not reopen 1.29.** The three link outcomes (SPEC §7.2.4), the label field and its cap,
  and the card-only scope for messenger domains are decided.
- **No notification machinery.** Reports notify nobody (§13.2), and card requests already
  auto-reply with no text (§10.4).
- **The operator queue is one queue** (§13.2, §13.5). A card report is a new *target type* in
  it, not a new queue and not a new form.
- **Accessibility is part of the work, not a follow-up** (§16.3): the report action is a real
  `<button>` with visible text, never an unlabelled icon (§16.4), and on a page that may
  carry twelve items it needs a **distinct accessible name** per the repeated-controls rule.

## Before you finish

- CHANGELOG.md entry and the version bump it earns.
- **Lift the gate in BUILD_PLAN Step 9.1 and in SPEC §10.2**, naming this version. Both say
  the `link` kind waits for this session; leaving them saying so afterwards is the failure
  this checklist item exists to prevent.
- TODO.md: prompt 15 marked run; the Step 9.1 gate recorded as lifted.
- If prompt 09 has not yet run, add the ARCHITECTURE and BUILD_PLAN work to its list or do it
  here and say in 09 that it is done — the same rule 13 followed.
