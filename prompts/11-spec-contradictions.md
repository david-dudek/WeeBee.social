# Prompt 11 — Three internal contradictions in SPEC

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** SPEC.md §9.1/§5.2, §8.1/§5.4, §4.6.1/§12.3 (and ARCHITECTURE.md §5 by consequence)
> **Depends on:** prompt 01. **Run before prompt 09.**
> **Expected outcome:** three pairs of sentences that cannot both be true become three pairs that can.

---

You are working in the WeeBee design-document repository. Read `README.md`, then `SPEC.md`
§5.2, §5.4, §7.5.1, §8.1, §9.1, §9.2, §12.3 and §4.6.1. Skim `ARCHITECTURE.md` §5. This is
a **founder-directed design session**; you may edit SPEC.md, and ARCHITECTURE.md where item
2 requires it.

## Why this prompt exists

Two external reviewers of v1.16 each stated explicitly that they found no internal
contradictions — ChatGPT: *"I didn't find an outright contradiction among the current
versions"*; DeepSeek: *"The documents are internally consistent."* A third reviewer found
three. All three were then verified against the document text and are real.

That history matters for how this session should work: **these are not obvious, and two
capable readers missed them.** Read the actual sentences before proposing anything, and be
willing to conclude that a fix is one word.

None of the three is a philosophy question. Each is a place where two true intentions were
written down in a way that cannot both hold.

---

## 1. The friend-request card is required to be both frozen and live

**§9.1** states the basic-tier invariant:

> The header plus the About tab, minus the extended bio, is **exactly** §9.2's basic tier,
> and **exactly** what §5.2's friend-request card shows. All three render from one component
> with one friends-only flag. This is a requirement, not an observation: if the three
> surfaces drift apart, the screening arguments of §5.2 and §13.1 quietly stop being true.

**§5.2** states the snapshot rule:

> The requester's **profile photo and short bio are frozen into the request at the moment it
> is sent**; a later change never alters a card already delivered. Without this, any limit
> on changing them is defeated by the obvious move — send twenty clean requests, then change
> the photo, and every unanswered card shows the new image.

Both requirements are correct and both are load-bearing — the invariant protects the
screening argument, the snapshot defeats the edit-and-blast attack. But "render from one
component" and "frozen at send time" cannot both be implemented literally, because one reads
current rows and the other reads stored copies. A builder following §9.1 to the letter
rebuilds the exact attack §5.2 exists to stop.

**The spec already half-knows this.** §5.2 carves out the display name: *"The requester's
display name still renders live through the shared helper, per §4.5.1's rule that names are
never stored on content."* So the card is already acknowledged to be a mix of live and
frozen data, and §9.1's "one component" was written before that was true.

**Recommended resolution:** the invariant is about the **field set and its rendering**, not
the data source. One component, one template, one set of fields — fed either from live rows
or from a snapshot, which is what makes the drift argument hold (a field added to the profile
appears on the card automatically) while leaving the snapshot intact. Write that distinction
explicitly in §9.1 rather than leaving the reconciliation to the builder, and state which
fields are frozen and which render live, since that list is now a security boundary.

Check the consequence for prompt 09's §G, which already asks ARCHITECTURE §4 for snapshot
fields including a stored copy of the image.

## 2. Comment visibility is smaller than post visibility, and one sentence denies it

**§8.1**:

> Who can comment = who can see the post (§7.4, §11.3). **A comment is visible to exactly
> the people who can see the post — never more.**

**§5.4**, on blocking:

> Neither can see the other's comments or reactions anywhere, including on shared friends'
> posts. (Others still see those comments; invisibility is only between the pair.)

So if Bob can see Charlie's post, and Alice has blocked Bob, Bob sees the post and not
Alice's comment on it. The comment audience is a **strict subset** of the post audience.

Note the reviewer got the diagnosis slightly wrong and it is worth being precise: **"never
more" is correct.** The word that fails is **"exactly"**, which asserts equality. The fix is
therefore small — but the consequence is not.

**The consequence is in ARCHITECTURE §5**, and it is the real finding. The engine exposes:

- `can_see_post(viewer, post)`
- `can_see_profile_tier(viewer, owner)`
- `can_act(viewer, action, target)`

There is no `can_see_comment`. Since §8.1 asserts comment visibility is identical to post
visibility, no separate check was ever specified — so today every template rendering a
comment either applies the block rule itself or does not apply it at all. Both outcomes
break ARCHITECTURE's central rule that one module makes every permission decision.

**Recommended resolution:** correct §8.1's wording to say the comment audience is the post
audience *minus anyone blocked in either direction*, and add `can_see_comment` to the engine.
Check whether reactions need the same treatment — §5.4 covers "comments **or reactions**",
and §8.2 makes reactions visible only to the author of the reacted-to content, so the
block interaction there may already be trivially satisfied. Say which, rather than leaving it.

Prompt 09 §L is written to pick up the ARCHITECTURE side; decide here, implement there, or
implement here if it is genuinely two lines.

## 3. Security emails must and must not carry a timestamp

**§4.6.1**:

> **These events carry absolute timestamps wherever they appear** — one of the two narrow
> exceptions to the relative-time rule of §7.5.1, because *"was that login me?"* is not a
> question anyone can answer with "several hours ago."

**§12.3**, restated at §7.5.1:

> **Email carries no timestamp at all.** A relative age is computed when mail is sent and
> read whenever the recipient opens it — three days later it would be false. The mail
> client's own received-time is more accurate than anything the body could assert.

Security events are delivered by email (§12 lists account/security events among the
notification types, and §4.6.1 calls them "security-event emails"). So the same message must
carry an absolute timestamp and no timestamp.

**The diagnosis is in §12.3's own reasoning.** Every word of its justification is about
**relative** ages decaying between send and open. An absolute timestamp has no such problem —
"2026-08-04 21:14 UTC" is as true on Friday as it was on Monday. §12.3 was written to ban
relative times in email and states a broader rule than it argues for, and that over-reach is
the entire collision.

**Recommended resolution:** narrow §12.3 to relative timestamps, leaving §4.6.1 untouched.
This lands exactly where §7.5.1's stated principle already points — *deliberately vague about
how old something is, exactly precise about when something will be destroyed* — with security
events on the precise side by the same logic as the expiry countdown.

Check the consequence for the inactivity warnings of §4.8, which are email-only and state a
deletion date. Under the current wording they arguably cannot say when the account will be
deleted, which would make them useless.

---

## Constraints to respect

- **No philosophy is in play here.** The no-counts rule, the snapshot mechanism, the block
  semantics, the relative-time ladder and the anti-scorekeeping posture are all settled and
  all correct. Every fix should make the documents say what they already mean.
- **Smallest correct change.** Two of these three are plausibly a sentence each. Do not turn
  a wording fix into a redesign; if a fix starts growing, that is a signal it is a different
  question and belongs in its own prompt.
- **§8.1's "consciously accepted consequence" stays.** Item 2 corrects a description of who
  sees a comment, not the decision that FoFs may comment (§11.3) or that §7.9 discloses it.

## Before you finish

- Write the CHANGELOG.md entry, naming every file's status including unchanged ones.
- **State explicitly which parts you left for prompt 09**, since two of the three have an
  ARCHITECTURE consequence and 09 is written expecting a handover.
- Update `TODO.md`.
