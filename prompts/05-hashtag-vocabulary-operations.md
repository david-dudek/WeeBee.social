# Prompt 05 — The hashtag vocabulary as an operational load

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** SPEC.md §11.2, §13.5, §14 (possibly §11.4)
> **Depends on:** prompt 01.
> **Expected outcome:** the curation policy survives, with the operator load bounded.

---

You are working in the WeeBee design-document repository. Read `README.md`, then `SPEC.md`
— §1.3 (supporting principles), §11 in full, §13.5, §14. This is a **founder-directed
design session**; you may edit SPEC.md.

## The finding

An external reviewer of version 1.16:

> Hashtags are "never free-typed" — users can only pick from a single, operator-curated
> vocabulary. This means the operator (the founder) becomes the **single point of failure**
> for all hashtag creation. If you're on vacation, no new hashtags can be added. If users
> propose 50 tags in a week, you have to manually approve each one. This is the exact kind
> of operational burden that kills solo projects.

The reviewer's proposed fixes are both wrong for this platform, and it is worth saying why
before the session starts, so time is not spent on them:

- **"Auto-approve after 3 users suggest the same tag."** Three users suggesting
  "#hiking", "#hikes" and "#trail walking" produce three approvals of the same interest,
  which is precisely the synonym fragmentation §11.2 exists to prevent. Automatic approval
  by count also removes the abuse screen; three coordinated accounts is not a high bar on
  an invite-only network where invites come in twos.
- **"Allow free-typed tags that are only matchable if in the vocabulary."** This gives
  users a text field that silently does nothing, which is worse than refusing them. It
  also reintroduces free text on a surface that currently cannot carry any.

**The underlying observation is nonetheless correct and unaddressed.** §11.2 says users
"may submit new-tag suggestions for operator review (§13.5)" and stops. Nothing states how
long a suggestion waits, what the user is told meanwhile, what happens to a request that
is never processed, or what the vocabulary looks like on day one.

## Why it matters more than it looks

Hashtags are not decoration here. SPEC §11.3 makes a profile hashtag one of three
conditions for friend-of-friend visibility, and §11.4 makes them the ranking signal on
the discover page. **The vocabulary is the substrate of the entire friend-discovery
mission** (§1.1's second purpose). A user whose actual interest has no tag is not
inconvenienced — they are invisible to the exact people the platform exists to connect
them with, and they have no way to know that is why.

The load is also front-loaded in the worst way. The suggestion rate is highest in the
first weeks, when the vocabulary is thinnest and every new user finds it lacking — which
is also when the founder is busiest with launch.

## What to work out with the founder

1. **The day-one vocabulary is the real answer.** Most of this problem is solved by a
   starter vocabulary broad enough that suggestions are rare. Decide the target size and,
   more importantly, the *method* — a few hundred interests, drawn from an existing public
   taxonomy or written by hand, weighted toward things people actually do together offline
   (§1.1: the measure of success is offline). Decide whether SPEC should state a target
   size at all, or whether that belongs in BUILD_PLAN Phase 10 as content work. **Do not
   write the vocabulary in this session** — that is a separate task and it will eat the
   whole conversation.

2. **What the user is told.** A suggestion that vanishes into a queue is a bad experience
   on a platform that prides itself on honest messages. Decide what the submitter sees on
   submission, and whether they are told the outcome. Note the tension: §13.5 says
   "submissions are private, carry no notification machinery, and the operator's decisions
   need no public justification." A per-suggestion reply contradicts that. A simple
   "suggestions are read in batches; check the picker in a few weeks" does not.

3. **A batching rhythm, not an SLA.** The honest framing for a solo operator is not "we
   respond within N days" but "the vocabulary is reviewed on a regular cadence." Decide the
   cadence and put it in the operator runbook (BUILD_PLAN §17.3) rather than promising it
   to users.

4. **Whether near-misses can be surfaced without free text.** Consider whether the picker
   can help a user who searches for a word that is not a tag — showing related existing
   tags rather than an empty result. This reduces suggestions at the source, and it is a
   search over a curated list, not free text. Check it against §17 (no global search)
   before proposing it: searching a static vocabulary reveals nothing about people, but say
   so explicitly so the rule is not read as broken.

5. **What happens when the operator is genuinely absent.** Vacation, illness, a bad month.
   The vocabulary being frozen for three weeks is survivable if the starter set is good and
   users are told the rhythm. State that plainly rather than leaving it implicit — the
   project's style is to name accepted costs (§7.8's "accepted cost, recorded rather than
   solved" is the model to follow).

6. **Whether any of this is a spec change at all.** It may be that §11.2 gains two
   sentences, §13.5 gains one, and everything else is operator practice belonging in
   BUILD_PLAN §17.3's runbook. That is a legitimate outcome. Resist the pull to add
   machinery to SPEC for a problem whose real solution is a good starter list.

## Constraints to respect

- **Curation stays.** The rationale in §11.2 — synonym fragmentation defeats the matches
  the feature exists to create, and curation blocks abusive or coded tags — is settled.
  Nothing here reopens free-typed tags.
- **No new counters.** Any proposal involving "how many people suggested this" must not
  surface a number to users (§17, BUILD_PLAN Appendix rule 12). An operator-side count in
  the admin queue is fine; it is not a user-facing count.
- **No inference.** Auto-generating tags from user behaviour or content violates §1.3's
  "the platform never infers."

## Before you finish

- Write the CHANGELOG.md entry, naming every file's status including unchanged ones.
- Record the two rejected reviewer proposals and the reasons, in-document, in the style of
  §4.5's rejected-uniqueness entry. README makes this the house rule, and it prevents the
  same suggestions arriving again as new.
- Update `TODO.md`, and add the starter-vocabulary content task to its parked list if it is
  not already there.
