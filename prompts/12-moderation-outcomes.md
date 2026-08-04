# Prompt 12 — What a ban actually does

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** SPEC.md §13.2 (and §4.7, §4.8, §5.4, §12 by consequence)
> **Depends on:** prompt 01. **Run before prompt 09.**
> **Expected outcome:** the three moderation outcomes are defined well enough to build, and the operator knows what each one costs.

---

You are working in the WeeBee design-document repository. Read `README.md`, then `SPEC.md`
§4.7 (deletion and deactivation), §4.8 (dormancy), §5.4 (blocking), §13 in full, and §12.
This is a **founder-directed design session**; you may edit SPEC.md.

## The finding

A third external reviewer of v1.16, on §13.2:

> The spec says the operator can "ban an account" as a moderation outcome, but it never
> defines what a ban actually does. Does it hide all the user's content? Prevent them from
> logging in? Delete their data after a grace period? Keep their comments visible to others?
>
> You have a button in the admin panel labeled "Ban," but no document tells the builder what
> that button is supposed to do. Different AI models will guess differently — one might make
> it a permanent deletion, another might make it a reversible deactivation, and a third might
> only block new posts.

Verified. §13.2 says the whole of it in one clause:

> v1 workflow is simply: the operator reviews and acts manually (**delete content, warn, or
> ban an account**). Formal policies/appeals are deferred.

"Delete content" is self-explanatory. **"Warn" and "ban" are both undefined** — the reviewer
named only the second, but a warning has no defined delivery channel either, and §12's
notification types do not include one.

## Why this is worth a session rather than a sentence

The platform already has four adjacent account states, each carefully specified, and a ban
is not obviously any of them:

- **Deactivation** (§4.7) — reversible, hides content everywhere, user-initiated, and the
  first 30 days of the deletion path.
- **Deletion** (§4.7) — full erasure after a 30-day grace period, user-initiated.
- **Dormancy** (§4.8) — the 24-month inactivity sweep, ending in deletion.
- **Blocking** (§5.4) — mutual invisibility between two users, not an account state at all.

A ban has to be defined against these, and the interesting questions are the ones where it
differs from all four. It is also the only one of the five that is **done to** a person
rather than chosen by them, which is what makes the content question hard: the platform's
whole posture is that a person's words belong to them, and §7.6 already refuses to let one
person's decision make another person's words permanent.

## Questions to work out

1. **What happens to the banned account's login?** Blocked outright is the obvious answer.
   Say whether the person is told, and what they see — the platform's style is honest
   messages (§13.6's "slow down" wording), and a silent failure would be out of character.

2. **What happens to their content?** This is the substantive question. The options are not
   equivalent:
   - *Nothing* — posts and comments stay until their 90 days run out. Their words remain on
     other people's posts, which is exactly what §4.7 says happens when someone deletes
     their own account ("the former friend's own past comments remain where they are").
   - *Hidden everywhere, reversibly* — the §4.7 deactivation behaviour, which already exists
     and is already specified, making this the cheapest option to build.
   - *Deleted* — which destroys threads other people participated in, and does to their
     conversation what §7.6 refuses to do.

   **Recommend hiding rather than deleting**, and state the reason: a ban is a judgment about
   a person's future conduct, and deleting their past words also deletes half of other
   people's conversations. Note that hiding is what deactivation already does, so the
   mechanism exists — the decision is which one a ban reuses, not what to build.

3. **Is it reversible?** A solo operator will get one wrong. If a ban is irreversible it
   needs a confirmation the operator cannot fat-finger; if reversible, say what restoring
   does to content that expired while hidden — it does not come back, and the operator should
   know that before banning rather than after.

4. **What happens to their friendships, invites and invite tree?** §4.3 records invite
   ancestry "for forensics and future analysis (e.g., detecting clusters of abusive
   accounts)" and explicitly attaches no consequences in v1. A ban is the event that
   ancestry was recorded for, so this is the moment to confirm v1 still attaches nothing —
   or to decide it does. Also: does a ban free the inviter's invite budget, and can the
   banned person's own invitees still join?

5. **Define "warn" too.** It is the other undefined outcome and it is cheaper to settle
   here than to discover in Phase 13. What channel carries a warning — §12 has no
   operator-to-user notification type, and adding one is a real addition, not a wording fix.
   Consider whether warnings need to be recorded against the account, since "we warned them
   twice" is the normal basis for a later ban and nothing currently stores it.

6. **Does a ban ever become a deletion?** Left alone, a banned account's content expires at
   90 days and the account itself hits §4.8's 24-month sweep and is deleted. That may be the
   right answer and needs no machinery — say so explicitly if it is, because a builder will
   otherwise wonder whether a banned account should be purged sooner.

## Constraints to respect

- **Formal policies and appeals stay deferred** (§13.2). This session defines what the
  outcomes *do*, not the process for contesting them. Resist writing a policy.
- **Proportion.** One operator, a few hundred users. Anything requiring a workflow, a state
  machine or an appeals queue is out of scope; §13's whole posture is manual review by one
  person.
- **The banned person's data rights survive.** GDPR erasure and export (§4.9, §15.1) are not
  moderation outcomes and are not forfeitable. Check that whatever is decided leaves the
  export path reachable, or state plainly how someone banned from logging in exercises it.
- **No counts, no public signal.** Nothing about a ban may become visible to other users as a
  marker, a tombstone or an absence with an explanation (§7.6's reasoning about comment
  tombstones applies directly).

## Before you finish

- Write the CHANGELOG.md entry, naming every file's status including unchanged ones.
- If question 5 (warnings) turns out to need a new notification type, **split it out** rather
  than designing a notification channel inside a moderation prompt.
- Update `TODO.md`. Note in it whether ARCHITECTURE needs an account-state column, since
  prompt 09 will have to carry it.
