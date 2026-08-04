# Prompt 10 — Reactions: how they look, where they show, and when they die

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** SPEC.md §8.2 (and §7.6, §9.7, §14); ARCHITECTURE.md §4, §6
> **Depends on:** prompt 01. **Run before prompt 09**, which syncs the build plan.
> **Expected outcome:** reactions have a stated lifecycle instead of an implied one, and §8.2 says what a reaction looks like on screen rather than only what it must never become.

---

You are working in the WeeBee design-document repository. Read `README.md`, then `SPEC.md`
§7.5–§7.6, §8.1–§8.2, §9.7, §12 and §14. Skim `ARCHITECTURE.md` §4 and §6. This is a
**founder-directed design session**; you may edit SPEC.md and ARCHITECTURE.md.

## The finding

From the v1.16 review by Kimi:

> SPEC §7.6 says comments on pinned posts still expire at 90 days, but §8.2 says nothing
> about reactions expiring. ARCHITECTURE.md §6's `expire_content` job only deletes
> reactions when their parent post is deleted. Because pinned posts are never deleted,
> reactions on them could accumulate indefinitely.
>
> A pinned post that stays up for two years could collect hundreds of reactions. Since the
> platform avoids counts, this may not seem like a problem, but it is a form of persistent
> state that the "statements expire" principle (§9.7) arguably should cover.

## What was verified in the documents

The reviewer is right on every factual point.

- **§7.6** handles comments on pinned posts at length — they expire on their own 90-day
  clock, their absence leaves no trace, and the section states the governing principle:
  *"an author may preserve their own words indefinitely, and may never preserve anyone
  else's."* It says nothing at all about reactions.
- **§8.2** describes what reactions are and what they must never become. It contains no
  lifetime, no expiry, and no rendering detail beyond "names, never numbers," author-only
  visibility, and the v1.16 rule that they never render in a list view.
- **§9.7** settles permanence as *statements expire; descriptions do not*, and lists what
  counts as account state (photo, gallery, bios, hashtags, contact card, groups, friend
  list). Reactions appear in neither list.
- **ARCHITECTURE §6**: `expire_content` runs hourly and deletes "posts/comments > 90 days
  (unpinned), their images, reactions." Reactions die with their parent and only with it.
  A pinned post has no parent expiry, so its reactions are permanent.

So the gap is real, and it is a gap in the *documents*, not a disagreement about the design.

## Questions to work out

1. **Do reactions on a pinned post expire?** There is a strong argument that §7.6 has
   already decided this and simply did not say so: a reaction is *another person's words*
   attached to content the author chose to preserve, which is exactly what the governing
   principle refuses. **Recommendation: yes — a reaction expires 90 days after it was
   given, on its own clock, exactly as a comment does, and its disappearance leaves no
   trace.** Confirm the principle governs, then write it into §8.2 rather than leaving a
   builder to derive it from §7.6.

2. **Does §9.7 need to name reactions?** §9.7's two lists are the place a builder looks to
   answer "does this expire?", and reactions are in neither. Decide which side they fall
   on and add them, whichever way question 1 goes. A reaction is a statement made at a
   moment about a specific piece of content, which suggests the expiring side.

3. **What does a reaction actually look like?** §8.2 is written almost entirely in
   negatives. A builder knows reactions must never be counted, never be public, and never
   appear in a list view — and does not know where on a single-post view they render, what
   the picker looks like, what a reactor sees of their own reaction, or whether a reactor
   can tell they have already reacted to something. Settle enough for Phase 8 to be built,
   including the 320 px case and the accessible name of the picker control (§16.3).

4. **Reactions on comments.** §8.2 grants "one reaction per post or comment" but only ever
   describes post reactions. Who sees a reaction on a comment — the comment's author only,
   or the post's author too? The answer follows from §8.2's own logic (reactions are for
   the person reacted to), but it is not stated, and the post author seeing reactions on
   other people's comments would quietly rebuild a scoreboard on their own post.

5. **Changing and removing a reaction.** §8.2 says reactions are "changeable or removable
   at any time" and §12 says notification actors render live "so deleted comments and
   removed reactions drop out." Verify those two are actually consistent and that removal
   retracts cleanly, then state it once rather than in two half-places.

6. **`REACTION_SET` curation.** §14 carries ~6 warm phrases and SPEC Appendix A item 8
   records them as placeholders for operator curation. Decide whether the current six are
   the six, and — more importantly for the build — what happens to existing reactions when
   the operator changes the set. A reaction whose phrase no longer exists must render as
   *something*.

## Constraints to respect

- **No counts, ever, in any form.** Reactions are shown as names or not at all (§8.2, §17).
  Nothing in this session may produce a number, a badge, or a "and 4 others" that is a
  number wearing a coat.
- **Author-only visibility stays.** Other viewers see nothing — no indicator that a
  reaction exists. That is the anti-validation-economy decision, and it is settled.
- **No free text and no arbitrary emoji.** The fixed operator-curated picker stays.
- **Reactions never render in a list view** (§8.2, v1.16) — not the Blog tab, not the
  Pinned tab, not the feed. The reasoning is recorded; do not reopen it.
- **Whether reactions should exist at all is not in scope.**

## Before you finish

- Write the CHANGELOG.md entry, naming every file's status including the unchanged ones.
- Update `TODO.md`.
- If questions 3–6 turn out to be a whole session's work on their own, do questions 1–2
  properly and split the rest into a new prompt rather than finishing all six badly.
