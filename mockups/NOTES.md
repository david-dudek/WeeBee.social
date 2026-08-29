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

---

## 9. §8.2.3's "Ha!" retirement is recommended but not adopted here

**Session:** M2. **Surface:** `pages/post-feed.html`.

SPEC §8.2.3 states plainly that *"Ha!" fails criteria 1 and 3* (warmth on the worst post it
could land on; no irony carrier) and is **recommended for removal**, with *"Thank you!"*
recommended in its place. That recommendation has not been adopted anywhere else in the
document — `REACTION_SET`'s worked examples throughout SPEC still list "Ha!" as a current
member, and no CHANGELOG entry retires it.

**Drawn:** `post-feed.html` uses the six-phrase set exactly as SPEC's own examples give it —
"Agreed!", "Love it!", "So proud!", "Thinking of you", "Congrats!", "Ha!" — per the standing
instruction to build what the documents currently say, not what one section of them recommends
changing. Recorded here so "Ha!" appearing in a 2026 mockup does not read as an oversight.

---

## 10. Reconciling §8.2.2's worked accessible-name examples with "no react control on your own content"

**Session:** M2. **Surface:** `pages/post-feed.html`, `pages/post-profile-tagged.html`.

SPEC §8.2.2 gives two worked examples for the react control's distinct-accessible-name rule:
*"React to David's post"* and *"React to Alice's comment."* Both use SPEC's own illustrative
cast (the same pattern NOTES.md's entry 5 already flagged for §12.2's notification wordings).
But §8.2 also says plainly: *"Nobody reacts to their own content. The react control is absent
on your own post and your own comment."* Read together as a literal instruction to reproduce
both worked examples on one single-post view, they conflict — a post authored by David, viewed
by David (the only view every other mockup in this track renders), can never carry a react
control naming itself "React to David's post," because that control must not exist there at
all.

**Drawn:** the two examples are split across the two pages where each is actually true.
`post-feed.html` renders David's own feed post from David's own point of view, so per §8.2 no
react control appears on the post itself — the omission is documented in an HTML comment
rather than silently dropped, and "React to Alice's comment" is used verbatim on the one
control that page does carry legitimately. `post-profile-tagged.html` renders the same kind of
post from a viewpoint that is *not* the author's (see entry 12, immediately below), so "React
to David's post" renders there, correctly and literally, on a control that is legitimately
present. Flagged as an interpretive resolution across two pages rather than a literal per-page
rendering of both quotes, which SPEC's own rules make impossible on a single page.

---

## 11. Single-post-view pages show the post author's name; the Blog/Pinned-tab omission rule is not applied here

**Session:** M2. **Surface:** `pages/post-feed.html`, `pages/post-profile-tagged.html`,
`pages/post-preformatted.html`.

§9.1 omits the post author's name on the Blog and Pinned tabs specifically, *"since every post
there belongs to the profile's owner, whose name is in the header above it."* None of these
three pages is a tab in that sense — each is a standalone single-post view, of the kind reached
from a notification link or a comment permalink, and `profile.html` (which would supply that
header context) is not built until M3.

**Drawn:** all three pages render the author's name in the ordinary `.post-meta` position, as
`_post.html` already does for feed posts. This is the plainest reading available before a
profile page exists to make the tab-context question concrete; M3 may want to confirm that a
real single-post-view template also shows the name once `profile.html`'s header exists to
compare it against.

---

## 12. `post-profile-tagged.html` renders as seen by a friend-of-friend, not David

**Session:** M2. **Surface:** `pages/post-profile-tagged.html`.

Every other mockup in this track renders David's own view (CRIB.md §3). This page cannot: a
reaction is visible only to the author of the thing reacted to (§8.2.2), and a commenter's name
links or renders as plain text depending on *the viewer's* connection to them (§8.1) — neither
rule can be demonstrated from David's own point of view on a post David himself authored, since
David is trivially connected to anyone who can reach his own tagged post. The M2 prompt's own
requirements for this page (a plain-text commenter name, a plain-text reaction) are only
satisfiable from a friend-of-friend's point of view.

**Drawn:** the page states its viewpoint explicitly in an intro paragraph — Priya, a
friend-of-friend of David's who matched via #hiking through their mutual friend Alice — and
every name-link and reaction-visibility decision on the page is worked out from Priya's
connections, not David's. Alice's name links (Priya knows her); Tom's renders as plain text
(Priya doesn't); Priya's own comment carries a reaction line visible to her as its author, with
a reactor (Mom) she has no connection to, rendered plain text. Recorded because it is a
deliberate, spec-required exception to this track's own established convention, not an
inconsistency to fix later.

---

## 13. ARCHITECTURE §3.8 names a shared modal-dialog partial that M1 never built

**Session:** M3. **Surface:** `pages/overlay-gallery.html`, `pages/overlay-post.html`.

ARCHITECTURE §3.8 lists the shared accessibility-unit partials as "`_field.html`,
`_errors.html`, `_modal.html`, `_expandable.html`, `_status.html`" — but M1 built only
`_field.html`, `_errors.html`, `_status.html` (plus `_post.html` and `_nav.html`, which
ARCHITECTURE doesn't name). `_modal.html` was never built, because M1 and M2 had no dialog
surface to demonstrate. Every session's standing constraints repeat "no page hand-rolls a form
control, dialog, or status message" — M3 is the first session that actually needs a dialog, and
there is no partial to compose.

**Drawn:** the two overlay pages hand-build the dialog markup directly (`role="dialog"`,
`aria-modal="true"`, `aria-labelledby` pointing at the figcaption), following the same
non-literal-include treatment M1 already gives `_post.html` and `_field.html` — a documented
pattern, copied by hand, because `build.py`'s `{{include}}` takes no per-call parameters and a
dialog's image, caption and control set differ every time. M3's own "Touches" list scopes this
session to `mockups/pages/` and does not include `partials/`, so no `_modal.html` was added
here; a later session (or a founder decision) may want to add one to `partials/` as a written
reference structure, matching `_post.html`'s treatment, so this gap does not recur in M6's
forms or wherever else a dialog appears next.

---

## 14. David's own dual-name state is not reconciled with his plain name on already-built pages

**Session:** M3. **Surface:** the persistent header on all four profile-tab pages.

The M3 prompt requires showing §4.5.1's "NewName (formerly OldName)" dual display in the
profile header, so M3 gives David his own name-change pair: "David Dudek (formerly Dave
Dudek)." But M1 and M2 already rendered plain "David" dozens of times — `feed.html`'s
notifications, `post-feed.html`'s byline, `post-profile-tagged.html`'s byline — with no
"(formerly …)" tag. Per §4.5.1, a name change during its 90-day transition window would render
the dual form "everywhere it appears," which strictly would mean retrofitting every earlier
mockup too.

**Drawn:** no retrofit. This mirrors the precedent already recorded in entries 5 and 7 for
Priya's dual-name state, which likewise appears on exactly one page rather than everywhere
Priya is named across the track. Each mockup illustrates the pattern of the idiom it was built
to show, not one fully self-consistent fictional timeline across all eight sessions. Flagged
here for the same reason those entries were: so it reads as a deliberate, repeated fidelity
choice, not an oversight specific to M3.

---

## 15. The Blog/"Posts" title contradiction (entry 4) — how M3 built around it, not into it

**Session:** M3. **Surface:** `pages/profile-blog.html`'s `<title>` versus its tab label.

Entry 4 recorded that §9.1 names the landing tab "Blog" while §16.3's own worked example gives
that tab's page title as "David Dudek — Posts" — two SPEC passages disagreeing with each other,
left as a founder call rather than resolved by this track.

**Drawn:** M3 uses both literal strings, for two different UI elements that don't have to
match: the tab strip's visible label reads "Blog" (§9.1's name for the tab), while the
browser-facing `<title>` reads "David Dudek — Posts" (§16.3's own literal worked example),
extended to the other three tabs by the same pattern ("David Dudek — Pinned", "— Photos", "—
About"). This is a way of building on both texts without declaring either one wrong — it is not
a resolution of the underlying contradiction, which entry 4 leaves for the founder.

---

## 16. `profile.html` remains unbuilt: M3's four pages are a friend's view, never the owner's own

**Session:** M3. **Surface:** `partials/_nav.html`'s "Profile" link; closes the open question
in entry 8, but only partially.

Entry 8 asked whether "my own profile" and "a friend viewing someone else's profile" would end
up sharing one filename or land as two. M3 answers half of that: it builds
`profile-blog.html`, `profile-pinned.html`, `profile-photos.html` and `profile-about.html`
strictly as **a friend's (Alice's) view of David's profile** — the case the M3 prompt scopes
this session to. M3 never renders "David viewing his own profile," which is a materially
different case (no report action would show to an owner viewing their own page, per §13.2:
"not to its owner"; the composer/editing affordances of later sessions would appear instead).

**Left open:** `profile.html`, the filename the main nav's "Profile" link and several M1/M2
pages already point at, is presumably meant for that self-view case — it remains completely
unbuilt, and none of M3's four new filenames are a substitute for it. A future session (or the
founder) still needs to decide whether the self-view gets its own `profile.html`-style filename
or reuses `profile-*.html` with a viewer-is-owner state — entry 8's question, still open.

---

## 17. The profile report button's visible text is not given verbatim anywhere

**Session:** M3. **Surface:** the persistent header's report action on all four profile-tab
pages.

§13.2 requires the profile-level report action to be "a real `<button>` with visible text,
never an unlabelled icon," and §9.1 says it belongs in the persistent header. Neither section,
nor any other, gives the button's actual label text verbatim the way CRIB.md's §2 registry does
for most other interface strings on the platform.

**Drawn:** "Report this profile," chosen as the simplest text that states what the button does,
per this track's standing rule for filling a gap the documents leave silent. Recorded because
it is easy to mistake for a verbatim SPEC string when it is not — unlike, say, the friends
page's "Filter your friends" (§11.6), which is quoted directly.

---

## 18. Priya's status contradicts itself between M2 and M3 — not a SPEC contradiction, a mockup-cast one

**Session:** M4, discovered while building the pages this session depends on Priya for.
**Surface:** `pages/profile-about.html` (M3) versus `pages/post-profile-tagged.html` (M2) and
CRIB.md §3.

M2 built Priya specifically as a **friend-of-friend** of David's, never a direct friend —
NOTES.md's own entry 12 spends a full paragraph establishing why that departure from "every
mockup renders David's view" was necessary, and CRIB.md's cast table describes her exactly that
way. M3's `profile-about.html`, built later, lists David and Alice's mutual friends for the
§11.5 "people you both know" line as "Tom, Mom and Priya" — which can only be true if Priya is
herself a **direct friend** of David's, since a mutual friend of David and Alice must be friends
with both of them. The two sessions' own established facts about the same named character
disagree with each other. This is not a contradiction inside SPEC.md or ARCHITECTURE.md — it is
one this track introduced across two of its own sessions, and the standing instruction to record
a contradiction and build on regardless applies to it just the same.

**Drawn:** M4 needed Priya to be a genuine friend-of-friend for its own pages to mean anything —
§9.2's tagged tier is vacuous for a viewer who already holds full friend access — so M4
**continues M2's characterization** rather than M3's: Priya remains connected to David through
exactly one mutual friend, Alice, on every page this session builds
(`profile-fof-tagged.html`, `discover.html`, `discover-tag.html`). M3's `profile-about.html` is
outside this session's touched files and is not corrected here. A founder decision is needed on
which of the two facts about Priya is the real one; until then, the two already-built mockups
disagree about her, and this entry is the map of exactly where.

---

## 19. §5.4's mutually-invisible blocked pair cannot be shown as a page — captioned, not faked

**Session:** M4. **Surface:** `pages/profile-fof-tagged.html`.

§5.4 makes blocking fully mutually invisible per pair: a comment on a post can be visible to one
viewer of that post and invisible to a second viewer, with every other viewer seeing it
normally. Demonstrating that literally would require rendering the *same* post twice on the
*same* page, once as each of two different blocked viewers would see it — which a static mockup
showing one viewer's page at a time cannot do without either faking a second viewer's session or
silently pretending the rule doesn't exist.

**Drawn:** neither. `profile-fof-tagged.html` renders Priya's one real view in full, exactly as
every other page in this track renders its one viewer, and carries a session-note captioning the
limitation directly rather than fabricating a second rendering to illustrate it. Recorded here
per the M4 prompt's own explicit instruction to caption this on the page rather than fake it.

---

## 20. `profile-fof-tagged.html` is a single file standing in for one tab of a three-tab tier

**Session:** M4. **Surface:** `pages/profile-fof-tagged.html`, contrast M3's four separate
per-tab files for the friend view.

§9.2's third tier can carry up to three tabs (About, Blog, Pinned), and M3 built one file per
tab for the friend tier it covered. The M4 prompt, by contrast, asks for exactly **one** file for
this tier: `profile-fof-tagged.html`. Comments must be shown on a visible post for this page to
satisfy its own requirements, and comments only exist on Blog/Pinned content, so a single file
cannot be the About tab; it has to be one of the other two.

**Drawn:** the one file renders the **Blog tab**, since that is where the established
Cornwall-coast-path post and its comments (built in M2) already live, giving this session a real
post to filter to rather than inventing a new one. Its tab strip links an About tab at
`profile-fof-tagged-about.html`, not built this session — an assumed, forward-referenced
filename in the same spirit as every other unbuilt link this track has carried since M1's nav
(see CRIB.md §5). The Pinned tab is not linked at all: David's only pinned post carries no
hashtag, so nothing of Priya's profile matches it, and per §9.2 a tab with nothing to show is not
rendered. That happens to make the real, current-data case a **two**-tab strip (About, Blog)
rather than the tier's three-tab ceiling — a truer demonstration of "each tab omitted if nothing
matches" than inventing a matching pinned post would have been, and it is left that way rather
than padded out to look like the maximum case.

---

## 21. The tag-filtered discover view is one hardcoded example, not a generic filter

**Session:** M4. **Surface:** `pages/discover-tag.html`, and every hashtag link across this
session's own new pages.

§11.4's tag filter is, in the real product, a live view parameterized by whichever tag was
clicked. A static mockup with no scripts and no server cannot build one page per vocabulary
entry, and building even a handful of near-identical filtered pages would be padding, not
fidelity — the same reasoning `post-preformatted.html` and other single-example pages in this
track already rest on.

**Drawn:** `discover-tag.html` is one concrete worked example, hardcoded to `#hiking` — the tag
already load-bearing elsewhere in this track's cast (Priya's match, §11.3). Every hashtag link
this session adds across its own new pages points to `discover-tag.html` when the tag is
#hiking, and to the plain, already-established `discover.html` placeholder for #jazz, #cornwall
and #baking, consistent with the forward-reference convention this track has used since M1's
nav. M3's own hashtag links (`profile-about.html` and its siblings) are untouched, since they
sit outside this session's files; they continue pointing every tag, #hiking included, at plain
`discover.html`.

---

## 22. A preview-as page's own `<h1>` displaces the previewed profile's name from that role

**Session:** M4. **Surface:** all four `preview-as-*.html` pages.

§16.3 requires the real profile page's one `<h1>` to be the owner's display name, in the
persistent header. A preview-as page is a different kind of page — a tool wrapped around a
rendering of that same profile — and the standing accessibility checklist this track has
followed since M1 requires exactly one `<h1>` per page. The two rules collide the moment a
preview page needs to both name itself ("Preview — as a friend") and show what would, on the
real page, be another `<h1>`.

**Drawn:** each preview-as page's own `<h1>` names the preview tool itself; the previewed
profile's display name renders as styled text sized and weighted to match a profile header's
`<h1>` (`.profile-preview-name` in `styles.css`), not as a second heading of any level. This
keeps every page's heading outline strictly nested (SPEC §16.3, WCAG 1.3.1) without contradicting
the "exactly one `<h1>`" rule the smoke tests of §16.5 check for. Recorded because it is a
structural choice specific to this new page type, not a literal instance of anything SPEC
describes.

---

## 23. §5.5 gives verbatim wording for flow (a)'s ask, none for flow (b)'s

**Session:** M5. **Surface:** `pages/introduction-requested.html`.

§5.5(a) quotes the broker-initiated wording directly: *"M wants to introduce you to [other
party]."* §5.5(b) describes the requested flow in full — A asks mutual friend M for an
introduction to M's friend C, M's decline is silent, agreeing runs flow (a) with A's side
pre-accepted — but never gives the wording for the one new event flow (b) actually introduces:
what M sees when A's ask arrives. Nothing else in SPEC supplies it either; §12.1's "everything
else" notification table lists "introduction proposals" as a type that generates a notification
but gives no wording example for it, the way §12.2 does for blog posts or photo uploads.

**Drawn:** *"Alice asks you to introduce her to Henry,"* built on the same pattern as the actor +
specific-event-text idiom §12.2 establishes elsewhere, using this track's own established pair
(Alice, a friend; Henry, a friend Alice can see but doesn't know). Flagged here so it is not
mistaken for a SPEC quote the way the flow (a) wording on the same page legitimately is — see
CRIB.md's new §5.5 entry, which registers exactly this distinction.

---

## 24. Neither document specifies the broker-introduction picker's mechanics

**Session:** M5. **Surface:** `pages/introduction-broker.html`.

§5.5(a) states the rule the picker must enforce — M selects two friends "who are not friends with
each other" — but neither SPEC nor ARCHITECTURE says anything about the control itself: whether
it is one widget or two, how "not already friends with each other" gets enforced or communicated
at pick time, or what happens to the second list once the first name is chosen. This track's own
cast, moreover, carries no friend-to-friend relationship data among David's friends (only each
friend's tie to David is ever established), so there is no data to filter against even if a
mechanic were drawn.

**Drawn:** two independent fieldsets, "First friend" and "Second friend," each a plain radio list
over David's full alphabetical friend list — the same list `friends.html` and
`preview-as-friend.html`'s picker already use — with Ben and Grace pre-selected as this session's
worked example, simply asserted (per §5.5(a)'s own requirement) to not be friends with each
other. No in-picker filtering or cross-list exclusion is drawn, since building one would imply a
relationship graph this mockup track does not otherwise maintain.

---

## 25. The contact-card override cascade's control shape is an interpretive choice

**Session:** M5. **Surface:** `pages/contact-card-editor.html`.

§10.3 specifies the cascade's *logic* — a default, a group override, an individual override that
always wins, and deny-beats-allow among conflicting groups — and ARCHITECTURE §3.8 requires "the
contact-card toggles" to be real `<input type="checkbox">` elements. Neither says what a
*non-existent* override looks like as a control: a checkbox is natively two-state (on/off), but
"no override set at this level" is a third state the cascade description implies without ever
naming a widget for it.

**Drawn:** an override is modelled as a row that either exists or doesn't, rather than a
three-way control masquerading as a checkbox. Each item lists whatever group or individual
overrides are actually set, each as its own plain on/off checkbox with a visible label; a
separate "Add a group override" / "Add an individual override" fieldset (a `<select>` naming the
group or friend, plus one checkbox for the value) is how a new row gets created. "Use the
default" is therefore the absence of a row, never a third checkbox state. Recorded because this
is a real design decision the documents leave open, not a literal rendering of anything either
one specifies.
