# NOTES.md — running gap log

Notes for the founder's review, not a to-do list. Nothing here gets fixed by this track — each
entry records where a document was silent (or, twice below, where two passages disagree) and
what got drawn anyway so the mockup could exist. One entry per gap, in the order found.

---

## 1. The main navigation's contents are not specified

**Session:** M1. **Surface:** `partials/_nav.html`, which every page includes.

SPEC names the main navigation exactly once — §7.1: the composer is "reached from the main
navigation" — and never says what else belongs in it. Whatever gets drawn here propagates
through roughly forty mockups across all eight sessions.

**Drawn:** six items — Feed, Post, Profile, Friends, Discover, Settings — chosen as the
minimum the rest of SPEC implies: each names a distinct, primary surface elsewhere in the
document (§7.7 the feed, §7.1 the composer, §9 the profile, §11.6 the friends page, §11.4
discover, and settings is referenced in passing at, e.g., §7.7.1's page-size preference). Left
out deliberately: no notifications item (notifications live inline in the feed, §7.7, and
there is no unread badge to justify a separate destination, §12.2/§17); no messages (no DMs,
§10.1); no search (§17 forbids one; a nav item implying it would misstate the platform the way
§11.6 warns a "Search" label would).

Only `feed.html` exists yet. The other five nav links point at filenames (`composer.html`,
`profile.html`, `friends.html`, `discover.html`, `settings.html`) that later sessions in this
track are expected to build — see CRIB.md §5. Until each lands, clicking that link 404s. This
is expected of an eight-session incremental build, not a bug in this session's output.

---

## 2. ARCHITECTURE.md lags SPEC.md pending prompt 09

**Session:** M1 (standing for the whole track). **Surface:** every session.

`prompts/09-sync-arch-and-buildplan.md` has not been run as of project version 1.27, so
ARCHITECTURE.md and BUILD_PLAN.md are known to lag SPEC.md. Per the track's standing rule,
every mockup in this track is SPEC-led: where the two disagree about a user-facing surface,
SPEC wins. No specific disagreement was hit while building the harness or the feed — recorded
here as a standing note for sessions M2–M8, who are more likely to find one on the surfaces
they build (forms, the operator console) where ARCHITECTURE goes into more implementation
detail than SPEC does.

---

## 3. Visual distinction between a feed post and a notification row is not specified

**Session:** M1. **Surface:** `pages/feed.html`.

SPEC §7.7 requires feed posts and profile-update/system notifications to interleave in one
strict reverse-chronological list, but never says how a reader tells the two apart at a
glance — the whole section is written in terms of ordering and content rules, not layout.

**Drawn:** the plainest distinction available without color-as-meaning (§16.4 bans color as
the only carrier): a notification row gets a light grey background, a left border, and a small
uppercase "Notification" label; a post is plain, unadorned text in an `<article>`. Both are
real text differences (the label) plus a boundary (the border), not color alone.

---

## 4. Contradiction: the profile's landing tab is named differently in two sections

**Session:** M1, found while assembling CRIB.md's verbatim-string register; **relevant to:**
M3 (the profile-friend-view session), not resolved here.

§9.1 names the profile's four tabs Blog / Pinned / Photos / About, with **Blog** as the
landing tab. §16.3's own worked example for the profile page gives that same landing tab's
page title as *"David Dudek — Posts"* — not "— Blog." One of these two names is stale. Per the
standing instruction to record a contradiction and build on regardless, this is recorded here
rather than resolved. M3 will need to pick one when it builds the profile's tab strip; SPEC
leads generally, but both passages are SPEC, so this one is a founder call, not a SPEC-vs-
ARCHITECTURE tiebreak.

---

## 5. §12.2's notification wordings all use "David" as the actor, which reads oddly on David's own feed

**Session:** M1. **Surface:** `pages/feed.html`.

feed.html mocks David's own feed. Per §7.7/§9.2, the notifications a person receives are about
their *friends'* activity, not their own — so in strict narrative terms, "David posted to his
blog" and "David changed his profile photo" are not notifications David himself would ever
receive. But §12.2's own wording examples use "David" as the illustrative actor for three of
the four core wordings, and the M1 build instructions ask explicitly for these wordings to be
used verbatim.

**Drawn:** used the wordings exactly as SPEC gives them, "David" included, on the reasoning
that they are illustrating the *pattern* of the idiom (actor name + specific event text) for
the founder's review, not asserting a fully self-consistent fictional timeline. Flagged here so
it reads as a deliberate fidelity choice, not an oversight.

---

## 6. Only one of §7.9's three visibility lines is reachable on the feed page itself

**Session:** M1. **Surface:** `pages/feed.html`; **relevant to:** M2, M3.

§7.9 gives three stated-visibility lines (feed post / untagged profile post / tagged profile
post). But per §7.7 and §9.1, a *profile* (blog) post never appears as rendered content in the
feed — only a notification about it does, without an excerpt (§12.2). So every actual `<article
class="post">` on feed.html is necessarily a feed-type post, and every visibility line on this
page is correctly the single "Visible to: the friends {author} sent this to." row. The other
two rows are registered in CRIB.md for M2 (single-post views) and M3 (profile tabs) to use
where they actually apply.

---

## 7. Whether the dual-name display substitutes inside generated sentences, or only where a bare name renders

**Session:** M1. **Surface:** `pages/feed.html`, Priya's post.

§4.5.1 says the "NewName (formerly OldName)" form renders "everywhere [the name] appears,"
and lists several surfaces — all of them places a name is rendered directly (a byline, a
comment, a mutual-friends list). It does not say whether that includes a *generated* sentence
that merely names someone, like §7.9's "Visible to: the friends {author} sent this to."

**Drawn:** the dual-name form appears in the post's byline (a direct name render — "Priya
(formerly Priyanka)"), and the plain current name only inside the generated visibility
sentence ("Visible to: the friends Priya sent this to."), on the reasoning that stacking the
parenthetical into a generated sentence produces dense, harder-to-read prose without adding
information the byline hasn't already given the reader on the same post. Flagged as an
interpretive choice a later session or the founder may want to revisit, not a certainty.

---

## 8. Own-profile vs. friend-viewing-a-profile filename is not yet settled

**Session:** M1. **Surface:** `partials/_nav.html`'s "Profile" link, `profile.html`.

M1's nav links "Profile" to a single `profile.html`, standing in for wherever the viewer's own
profile lands. M3 builds "the four profile tabs as a friend sees them" (i.e., viewing someone
*else's* profile), which is a different page in practice even if it shares the same template.
Whether "my own profile" and "a friend's profile" end up as one filename with different
states, or two distinct filenames, is left for M3 to decide — `profile.html` here is a
placeholder link target, not a naming decision.
