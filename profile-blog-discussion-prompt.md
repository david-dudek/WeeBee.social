Read SPEC.md and README.md in this repo (WeeBee — a small, private, deliberately anti-viral
social network; design documents only, nothing built yet). Then let's discuss **the profile page
and the blog** (SPEC §9, plus §7.6 pinning and §11.3/§11.5 as they touch the profile).

This is a design discussion, not an implementation task. Do not edit SPEC.md unless I ask.

## Ground rules

- The product philosophy is settled — see README "What is NOT up for review." Don't relitigate
  no-reach, invite-only, 90-day expiry, no DMs, no counters, or WCAG 2.1 AA. Apply them.
- Cite section numbers (e.g. "§9.2") for everything you claim the spec already says, and say
  plainly when the spec is **silent** rather than filling the gap and presenting it as existing.
- Flag internal contradictions between sections, and missing constants (§14) that the answers
  would require.
- Give me a recommendation with reasoning, not a survey of options. Blunt is welcome.
- Every proposal must pass the No-Reach Test (§1.2) and the "platform never infers" principle
  (§1.3) — say so explicitly where it's non-obvious.
- End with (a) a list of decisions I need to make, and (b) draft spec-ready wording for the ones
  where my answer is predictable, marked as drafts.

## Where the last session got to

The immediately preceding session worked the feed and notification side, and its conclusions are
**already written into SPEC v1.15** — read that changelog entry first. In short: relative
timestamps (§7.5.1), post and comment editing (§7.8), the rewritten notification model with
per-field profile triggers, coalescing, comment/reaction notifications and post-following (§12),
the two capped bio fields (§9.4), the friend-request free-text vector with its screening and
change cooldown (§5.2, §13.6), and structured profile fields considered and rejected (§9.6).

Treat all of that as settled. Your job is the profile page and blog *as surfaces* — everything
below is either still open, or newly exposed by those decisions.

## What I want to work through

**A. Structure and content of the page**

1. §9.1 fixes the section order (identity header → pinned posts → static about → gallery → blog).
   Is that the right order for the three viewer tiers of §9.2? What does an FoF actually see, and
   what does a hashtag-matched FoF see, section by section? What are the empty states?
2. Does the extended bio (§9.4) obey the whitespace rules of §7.2.1? Does it get a preformatted
   toggle (I assume no)? Does it fold at `BLOG_FOLD_CHARS`, or is 2,000 characters short enough
   that folding never triggers and the rule would be dead code?
3. The profile photo: required or optional? Default avatar? §16.3 requires uploader-authored alt
   text on every image *including the profile photo* — what does a sensible prompt for "describe
   your own face" look like, and is "decorative" ever a legitimate answer for a profile photo?
   (Note the photo is now rate-limited alongside the short bio, §13.6.)
4. Gallery (§9.4, 8 images): captions? Ordering and reordering? Does replacing an image re-prompt
   for alt text? Does reordering count as a change for notification purposes (§12.1)?

**B. Permanence — the sharpest tension on this page**

5. §7.5 expires "every post and every comment" at 90 days, but the gallery, both bio fields, and
   the profile photo are not posts, so they appear to be **permanent**. Is that intended? A
   permanent 8-image gallery sitting on a platform whose defining stance is that nothing outlives
   90 days deserves an explicit decision either way.
6. Pinned posts (§7.6) are exempt from expiry indefinitely, but §8.1 expires comments at their own
   90 days regardless. So a pinned post outlives all conversation on it and eventually shows as a
   bare post with its comments silently gone. Intended? Should a pinned post display that it once
   had comments, or nothing at all?
7. Pinned posts are the **only** content that can reach the long tail of the §7.5.1 timestamp
   ladder, since everything else dies at 90 days. Given that §7.5 already replaces their expiry
   countdown with a "pinned" marker, should a pinned post show its age at all?
8. Does the blog need pagination? Its maximum depth is ~90 days of posts plus up to 10 pinned, so
   it may be self-limiting. Infinite scroll is banned (§16.2) — what's the navigation?

**C. The blog as a surface**

9. Where does a user compose a profile post — on their own profile, or one composer with a
   feed/profile toggle? Can a draft switch type before posting? Can a posted one convert? (I
   assume no.)
10. Hashtags on a profile post are the FoF visibility gate (§11.3), which means the composer is
    making an audience decision that looks like decoration. How does the composer make that
    consequence unmissable without nagging? Note that §7.8 invariant 1 now lets an author change
    that gate *after* posting by editing tags — does the editor need the same warning?
11. Possibly the biggest hole still open: a **commenter is never told the audience they are
    speaking to.** On a hashtag-gated post their words become readable by people who aren't even
    the author's friends — §8.1's accepted consequence, one hop further. Should every post display
    its visibility scope in text to everyone who can see it? And does this make §17's parked
    "per-post friends-only comments switch" load-bearing enough to un-park?
12. §9.1 says the blog is "filtered per viewer." Confirm exactly what a hashtag-matched FoF sees
    in the blog section, and what the pinned-posts section shows them if a pinned post carries no
    matching tag.

**D. Navigation, privacy, and the edges**

13. §9.3 bans deep links and requires non-guessable identifiers. So how does a user actually reach
    a profile — from the feed, comments, mutual-friend lists (§11.5), discover (§11.4)? Is there
    any in-app way to point a friend at another friend's profile besides an introduction (§5.5)?
14. §11.5 shows a viewer only their mutual friends with the profile owner plus hashtag-matched
    non-mutual friends. Is that rendered as **names** rather than a count? §17 bans visible counts,
    so confirm there is no friend count, no post count, and no "last active" anywhere on the page.
15. §9.5 preview-as: what are the mechanics — pick any friend, plus a generic FoF, plus a generic
    hashtag-matched FoF? Does it cover the blog's per-viewer filtering, not just the static tiers?
16. What does the page look like for: a blocked viewer (§5.4), an unfriended former friend (§7.4),
    an account in its 30-day deletion grace period (§4.7), and the owner themselves?
17. The report action on a profile (§13.2) — where does it live, and what does it capture given
    that a profile has no single frozen "content"? Note the bio is now screened (§9.4) but the
    photo is not, so the report queue is the only backstop for an abusive profile image.

**E. Accessibility (§16)**

18. Walk the profile page and blog against §16.3 specifically: heading hierarchy across the five
    sections, the gallery as a keyboard-navigable structure, the click-to-expand overlay as a
    modal, per-viewer theming plus the "always use my own theme" override (§9.1), and the "read
    more" folds at `BLOG_FOLD_CHARS` = 2,000 (§7.7).

Start by telling me where the spec is already clear, where it contradicts itself, and where it is
simply silent — then work through the questions in order.
