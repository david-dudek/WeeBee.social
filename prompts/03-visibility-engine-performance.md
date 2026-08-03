# Prompt 03 — Visibility engine performance and request-scoped caching

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** ARCHITECTURE.md §5 (and probably §2 Decision 4, §9, §13)
> **Depends on:** prompt 01.
> **Expected outcome:** ARCHITECTURE gains a caching rule. SPEC should not need to change.

---

You are working in the WeeBee design-document repository. Read `README.md`, then
`ARCHITECTURE.md` in full and the parts of `SPEC.md` it points at — §5.4 blocks, §7.4
audience semantics, §8.1 comments and name linking, §9.2 profile tiers, §10.3 the contact
cascade, §11.3 the hashtag gate. This is a **founder-directed design session**; you may
edit ARCHITECTURE.md.

## The finding

An external reviewer of version 1.16 raised the strongest technical point in either
review. Paraphrased:

> Everything routes through one visibility engine. That's architecturally excellent. The
> danger isn't correctness — it's performance. If every item on a page independently asks
> `can_see_post(...)`, and each of those repeatedly checks friendship, blocks, hashtags,
> snapshots and overrides, you accidentally create many repeated database lookups.

I checked. ARCHITECTURE §5 states the routing rule in absolute terms and says nothing
whatsoever about how often it runs or what it costs. Neither does §2's Decision 4.

## Why this is worth a session

The load is not hypothetical, and the recent spec versions increased it:

- **SPEC §7.7.1** sets `POSTS_PER_PAGE_DEFAULT` = 20 with a viewer-chosen 20/40/60. A
  reader on 60 is a normal reader, not an edge case.
- **SPEC §8.1** requires every rendered name to be linked or not linked according to
  `can_see_profile_tier(viewer, that_person)` — and v1.16 extended that rule from
  commenters to post authors, mutual-friend context, and reaction name lists.
- **SPEC §11.5** renders mutual friends by name on profiles.
- **SPEC §7.9** puts an audience line on every post — derived from the post, so cheap, but
  one more per-item computation.

A 60-post page where each post has a handful of comments and reactions asks the engine
several hundred questions, and a large fraction are *the same question asked again*: is
this viewer blocked by that person, are these two connected, what tier does this viewer
have. The answers cannot change during a single page render.

The failure mode is not a crash. It is a feed that takes four seconds on a €8 VPS, which
is the kind of problem that gets fixed by someone inlining a query in a template — which
is precisely the thing Decision 4 exists to forbid. **The performance gap is a threat to
the architectural rule, not just to speed.**

## What to work out with the founder

1. **Where the caching rule belongs.** §5 restates Decision 4 as an implementation rule
   for AI builders and is the natural home. Consider whether Decision 4 itself needs a
   sentence, since that is where the "one engine" principle is argued.

2. **What is safe to memoize within one request.** Propose the actual list. Candidates:
   block status between two accounts, friendship, friend-of-friend status, profile tier,
   the viewer's own profile hashtag set. Say which are per-pair and which are per-viewer.

3. **What must not be cached, and for how long.** State the scope hard: **one HTTP
   request, discarded at the end of it, never a cross-request cache and never a persisted
   one.** SPEC §11.3 requires the hashtag gate be evaluated live, and §7.4 pairs a
   snapshot audience with *current* friendship — a stale cache turns both into privacy
   bugs. Cross-request caching of visibility answers should be named and forbidden, not
   left unmentioned.

4. **The cache key must include the viewer.** SPEC §9.5's preview-as substitutes a
   different viewer into the same code inside one request. A cache keyed on the object
   alone would leak the real viewer's answers into the preview or the reverse. This is a
   small detail with a bad failure mode; make it explicit.

5. **Bulk questions, not just cached ones.** Memoization removes repeats; it does not fix
   asking 60 separate questions where one would do. Consider whether the engine should
   expose plural forms — "which of these posts may this viewer see", "which of these
   people may this viewer link to" — so a page fetches in bounded queries rather than
   per-item ones. This is the larger design decision of the session, and it changes the
   engine's shape. Weigh it against the project's stated preference for the simplest
   thing that works.

6. **Whether this needs a test.** ARCHITECTURE §9 tests the engine's correctness densely.
   A query-count assertion on the feed view — render a seeded feed, assert the number of
   database queries stays under a stated bound — is cheap in Django and catches the
   regression the moment it appears. Decide whether it earns its place.

7. **Whether BUILD_PLAN needs a step.** Probably not a new one: Phase 4 builds the engine
   and Phase 6 builds the feed. Note anything for prompt 09 to fold in rather than editing
   BUILD_PLAN here.

## Constraints to respect

- **Do not weaken Decision 4.** The rule that no template, page, list, notification,
  export or job decides visibility for itself is the heart of the architecture. Caching
  lives *inside* the engine, invisible to callers. If a proposal requires callers to know
  about the cache, it is the wrong proposal.
- **No new infrastructure.** ARCHITECTURE §2 commits to one server and one database. A
  request-local dictionary is in scope. Redis is a conversation the founder has not had,
  and starting it here would be scope creep — if you believe it is genuinely needed,
  say so plainly and let the founder decide.
- **This is an architecture change, not a spec change.** SPEC describes what the platform
  does; caching is invisible to users. If you find yourself wanting to edit SPEC, that is
  a signal you have drifted — see prompt 08.

## Before you finish

- Write the CHANGELOG.md entry, naming every file's status including unchanged ones.
- Update `TODO.md`.
- If the bulk-query question (item 5) turns out to be a genuine redesign rather than an
  addition, **stop and split it into its own prompt** rather than deciding it tired at the
  end of a long session.
