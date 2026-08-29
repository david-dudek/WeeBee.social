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

---

## 26. Track-wide convention change: separating simulated content from build commentary

**Session:** a cross-cutting retrofit run after M5, not one of the numbered M1–M8 sessions
(`prompts/mockups/content-commentary-separation.md`). **Surface:** every page M1–M5 had built
(~28 files in `pages/`), plus `partials/_base.html`, `styles.css`, `prompts/mockups/README.md`,
and each `M1.md`–`M8.md`'s own "Standing constraints" section.

**What triggered it:** every page built so far mixed two audiences in one stream of text — copy a
real WeeBee user would see, and commentary explaining a build decision to the founder (SPEC
citations, "this is invented," cross-references to other pages). The `.session-note` class
(added in M1) was meant to mark the second kind, but it was applied inconsistently: a lot of
commentary sat in plain, unclassed paragraphs, including raw SPEC section numbers and phrases
like "§5.3, verbatim:" inside what was meant to read as product copy.

**What changed:**

1. **The rule.** A new third standing rule, "separate simulated content from build commentary,"
   added to `prompts/mockups/README.md` alongside the two existing ones, and to the same bullet
   list in every `M1.md`–`M8.md`. The test: would WeeBee actually say this to a user who has never
   read a design document? If not, it is commentary — full stop. This covers any SPEC/ARCHITECTURE
   section reference, any named constant in its shouty code form, anything explaining *why* a page
   was built a certain way or referencing another mockup file, and anything using words like
   "verbatim," "this session," "this track," "worked example," or "placeholder." The one exception:
   a genuine SPEC-mandated verbatim interface string (e.g. the unfriend confirmation's blockquote)
   stays real copy — SPEC just happens to mandate its exact wording.
2. **The style.** `.session-note` renamed to `.commentary` everywhere it appeared (every page that
   used it, plus `styles.css`), and restyled as italic monospace in the existing muted color and
   size — a bigger visual break than grey-and-small alone, unmistakable as a build note even when
   skimming.
3. **The toggle.** One real, visibly labelled `<input type="checkbox" id="commentary-toggle"
   checked>` ("Show build commentary and SPEC citations") added once to the shared header in
   `partials/_base.html`, plus a single CSS rule in `styles.css`
   (`body:has(#commentary-toggle:not(:checked)) .commentary { display: none; }`) that hides every
   commentary block on the page when unchecked. No scripts. Default checked (visible), matching
   the track's behavior up to now.
4. Every page M1–M5 built was re-audited sentence by sentence: existing `.session-note` blocks
   were renamed in place; plain paragraphs that were actually commentary (most of the intro
   paragraph under each page's `<h1>`, and most of the explanatory text under each section's `<h2>`
   describing what a tab or state shows) were reclassified; a handful of paragraphs that mixed a
   real fact with a trailing citation or a shouty constant were split, keeping the human-readable
   fact in real copy and moving the citation/constant to an adjacent commentary note; and two
   verbatim SPEC quotes (`unfriend-confirm.html`'s §5.3 blockquote and its block-framing quote)
   that had been embellished with mockup-only asides (e.g. "below on the received card" inserted
   into what CRIB.md registers as a verbatim quote) were restored to SPEC's actual wording, with
   the aside moved to an adjacent commentary note instead.

**Left alone, deliberately:** `pages/index.html`. It is the founder's own review index by design —
M1's instructions call it out explicitly as doubling for that purpose, so it was never simulated
product copy in the first place and the grandma test does not apply. It keeps its SPEC citations
in plain text, unwrapped.

**No-persistence limitation, accepted rather than chased:** the toggle is pure CSS with no script
and no cookie, so it cannot remember its state across a page load. Every page opens with
commentary visible (the default), regardless of what state a previous page was left in. A founder
clicking through several pages with the toggle off will find it re-checked on each new page. This
is inherent to a static, script-free mockup track and is not a bug to fix within it.

See `CRIB.md` §6 for the registered convention M6–M8 should follow from the start.

---

## 27. `report.html` vs. `report-post.html` / `report-profile.html` — a filename mismatch left uncorrected

**Session:** M6. **Surface:** `pages/post-profile-tagged.html` (M2)'s report action, versus
`pages/report-post.html` and `pages/report-profile.html` (M6).

M2 built `post-profile-tagged.html`'s tag-mismatch report action as a link to `report.html`, a
single unsplit filename, and CRIB.md recorded it as a forward reference expected to land in this
session. This session's own prompt, however, specifies two separate filenames instead —
`report-post.html` and `report-profile.html` — reflecting that post/comment reports and profile
reports carry different reason categories. `report.html` itself is therefore never built, and
`post-profile-tagged.html`'s link now points at a filename this track will not produce.

**Drawn:** nothing corrected. M3 and M4 each established the precedent of leaving a link inside a
file outside their own session's touched set exactly as they found it, rather than reaching back
to retarget it (see entries 8, 16, 20, 21). This session follows the same precedent:
`post-profile-tagged.html` is untouched, and the mismatch is recorded here instead. A founder
decision or a later pass can retarget that one link to `report-post.html`, which renders the
identical scenario (Priya reporting David's Cornwall post for a tag mismatch) as its first worked
example.

---

## 28. §13.2's free-text note on a post/comment report — an ambiguity rendered, not resolved

**Session:** M6. **Surface:** `pages/report-post.html`.

§13.2 was written in two passes: the original stub gave every report a reason category only, and
a later addition (v1.16) gave *profile* reports specifically a target category **and** a short
free-text note to the operator. Read together, the section's own summary sentence — "there is
one report form, and it always carries a reason category, plus the optional short note to the
operator this section already gives profile reports" — reads most plainly as extending that note
to post and comment reports too, since it treats all report types as one form. But nothing in
§13.2 says so in so many words for the post/comment case specifically, and the M6 prompt itself
calls this out as ambiguous rather than settled.

**Drawn:** the plainest reading. `report-post.html` gives its post-report and comment-report
forms the same optional free-text note the profile-report form already carried, on the reasoning
that one report form ought to behave one way. This is flagged here exactly as the session's own
instructions ask, and is not resolved — a founder call on whether post/comment reports were ever
meant to carry a note is still open.

---

## 29. `THEME_SET` has no members named anywhere — placeholder theme names on `settings.html`

**Session:** M6. **Surface:** `pages/settings.html`.

SPEC §9.1.1 and §16.3 both require `THEME_SET` — the operator-curated fonts and colour schemes a
user can choose between — to exist and to meet WCAG contrast in every combination, but neither
document nor §14's constants table names a single actual theme or font. A settings page has to
render *some* control for this choice to be legible at all.

**Drawn:** bracketed placeholder option text — "[Theme option A]," "[Font option A]," and so
on — following the same convention `contact-card-editor.html` (M5) already established for an
unspecified value ("[David's WhatsApp link]"). A visible hint states plainly that these names
are placeholders, and the page's own commentary repeats that `THEME_SET` names no members in
either document. No actual theme or font names are invented.

---

## 30. Why `settings.html` and `groups.html`'s provenance label is not wrapped in `.commentary`

**Session:** M6. **Surface:** `pages/settings.html`, `pages/groups.html`; the new
`.page-provenance` class in `styles.css`.

Both pages are required to carry a visible label stating that the documents don't specify them,
so the founder can tell at a glance. But every other piece of build commentary on every page in
this track is wrapped in `.commentary`, which the header's toggle can hide — and hiding *this*
particular label would defeat its own purpose: a founder who has switched commentary off should
still be able to tell an assembled or inferred page apart from an ordinary mockup without having
to switch it back on first.

**Drawn:** a new, separate class, `.page-provenance`, deliberately left outside the
`body:has(#commentary-toggle:not(:checked))` rule that hides `.commentary`. It is styled
distinctly from both `.commentary` (plain weight, not italic monospace) and `.notice` (a heavier
border), so it reads as its own category of note. Everything else on both pages — ordinary
section-by-section SPEC citations — still uses `.commentary` as normal; only the one top-of-page
label is exempted, the same narrow scope `pages/index.html`'s whole-page exemption does not
extend to. See `CRIB.md` §6 for the registered convention.

---

## 31. Groups.html asserts only the one group membership fact this track has already established

**Session:** M6. **Surface:** `pages/groups.html`.

`contact-card-editor.html` (M5) established that Tom belongs to both "Hiking crew" and "Book
club," used there to demonstrate the deny-beats-allow override conflict. It never stated who
else, if anyone, belongs to either group.

**Drawn:** `groups.html` renders both groups' membership as a checkbox list over David's full
established friend list (Alice, Ben, Grace, Henry, Mom, Nadia, Sofia, Tom), with only Tom's box
checked in each — the one fact this track actually established — rather than inventing plausible
company for him. The over-the-cap warning state is demonstrated on a separate, explicitly
hypothetical "New group" instead of on Hiking crew or Book club, so as not to assert either real
group is anywhere near 30 members.

---

## 32. `post-editor.html` and `gallery-manage.html` have no real entry point yet

**Session:** M6. **Surface:** `pages/post-editor.html`, `pages/gallery-manage.html`.

Both pages render David editing his own content — his own posts, comments, gallery, and profile
photo. The natural link to either would sit on "David viewing his own profile" or "David viewing
his own single-post view," neither of which exists: entry 16 already recorded that
`profile.html`, the filename the main nav and several M1/M2 pages point at, remains unbuilt, and
every profile page actually built so far (M3's four tabs, M4's non-friend tiers) renders someone
*else's* view of David, never his own.

**Drawn:** nothing added to bridge this. Both pages are reachable only from `pages/index.html`
for now. A future session or founder decision that finally builds the owner's-own-profile case
should link to `post-editor.html` and `gallery-manage.html` from it.

---

## 33. `post-editor.html` reuses established posts and comments rather than inventing new ones

**Session:** M6. **Surface:** `pages/post-editor.html`.

Every scenario on this page reuses content already on record elsewhere in this track: the "Small
dinner this Friday" feed post and its Alice/Tom/David comments (M2's `post-feed.html`), and the
Cornwall coast-path blog post and its Alice/Tom/Priya comments (M2's `post-profile-tagged.html`).
This keeps the editor's states — the edited marker, the widening notice, the narrowing case, and
who may edit versus only delete a comment — attached to posts the founder has already seen,
rather than introducing new text purely to demonstrate an editing control. One consequence
follows the widening scenario in section 3: SPEC requires every existing commenter to be
notified when a tag they were not covered by is added ("David added a hashtag to a post you
commented on. More people can see it now."), but that notification would render on Alice's,
Tom's and Priya's own feeds, none of which this track builds — the page states the rule in
commentary rather than rendering a feed row nobody asked for.

---

## 34. `invites.html` — inferred, not specified, and the one number §17 arguably requires anyway

**Session:** M7. **Surface:** `pages/invites.html`.

Like M6's `settings.html` and `groups.html`, no section of either document describes a screen for
seeing an invite budget or sending an invite — SPEC §4.2 gives only the mechanics
(`INVITE_BANK_MAX` = 5, `INVITE_REPLENISH_DAYS` = 30, new accounts start with
`INVITE_NEW_ACCOUNT` = 2). §17 separately states a platform-wide ban on "likes or visible counts
(followers, reactions, views, post counts, page numbers — none exist)."

**Drawn:** the minimum screen the mechanics imply, labelled `.page-provenance` exactly as M6's two
inferred pages are, plus a form to send an invite. The budget itself is genuinely in tension with
§17: a number the user cannot see is a number they cannot use to decide whether sending an
invite will do anything. This session's resolution is to state it as an ordinary sentence —
"You have 3 invites saved up right now, out of a possible 5" — rather than as a progress bar or a
numeric badge, on the reasoning that §17's ban targets *scorekeeping widgets* (a follower count,
a like count) rather than every number a page might ever state in prose. Flagged here because it
is arguably the one visible count this platform cannot avoid showing somebody, and a founder
reviewing §17's "no visible counts" line against this page should know the exception exists.

---

## 35. `banned.html` cannot literally drop the shared nav within this static harness

**Session:** M7. **Surface:** `pages/banned.html`.

The M7 prompt requires this page to carry no navigation at all, explicitly: "this means the page
does not use the standard `_nav.html`." But every page this track builds is wrapped, uniformly,
by `build.py` substituting a page's body into the one shared `partials/_base.html`, whose header
includes `{{include partials/_nav.html}}` unconditionally — there is no per-page mechanism to
omit it. Suppressing the nav specifically for this one page would mean editing `partials/` (or
`build.py`'s templating logic to support a per-page override), and this session's touched files
are `mockups/pages/`, `CRIB.md`, `NOTES.md` and `pages/index.html` — not `partials/`.

**Drawn:** nothing technical. This mirrors M3's own precedent for the missing `_modal.html`
partial (entry 13): a real gap between what a page needs and what the harness can express is
documented rather than papered over by extending shared infrastructure beyond a session's own
touched-files scope. `banned.html` goes through the normal pipeline — its shared header therefore
mechanically carries the ordinary Feed/Post/Profile/Friends/Discover/Settings nav, an artifact of
the review harness that the real, live page must not have — and the page carries a prominent,
unmissable note saying so at the top of its own content. Nothing inside the page's own body links
anywhere except data export and account deletion, which is the part this mockup can actually be
faithful to. Contrast entry 36, immediately below, where this session made the opposite call for
a harder constraint on `maintenance.html`.

---

## 36. `maintenance.html` needed an actual `build.py` change — the one harness extension this session makes

**Session:** M7. **Surface:** `pages/maintenance.html`, `build.py`.

Unlike `banned.html`'s "no nav" requirement (entry 35), `maintenance.html`'s constraint —
"nothing fetched from anywhere... it must not link to styles.css either" — is not a matter of
degree. Every page wrapped in `partials/_base.html` gets a hardcoded
`<link rel="stylesheet" href="styles.css">` in its `<head>`; a browser loading that page issues a
real network request for that file regardless of anything the page's own body content does. There
is no CSS-only or content-only way to prevent that fetch from inside the existing pipeline — the
requirement is binary, and it was one of the four items this session's own "before you finish"
checklist calls out by name.

The deeper reason is categorical, not just technical: every other page in `mockups/pages/`
represents something the Django app would render. `maintenance.html` represents the opposite —
what Caddy serves *when the Django app is not rendering anything at all* (ARCHITECTURE §7.2).
Routing it through the app's own shared template, which assumes the app and its static-file
serving are both up, contradicts the page's entire reason for existing.

**Drawn:** a narrow, clearly-commented special case in `build.py`: when the loop over
`pages/*.html` reaches `maintenance.html`, the file is copied straight to `site/maintenance.html`
instead of being substituted into `_base.html`. `pages/maintenance.html` is therefore written as
a complete, standalone HTML document — its own `<!DOCTYPE html>`, its own inline `<style>`, the
HTTP 503 / `Retry-After` note in an HTML comment at the top, since a static file can't send real
response headers. This is the one place across M1–M8 (so far) where a session edits `build.py`
itself rather than only `pages/`, made deliberately rather than by default: the bar was "the
requirement is impossible to satisfy any other way and is checklist-verified," which
`banned.html`'s nav requirement did not clear.

---

## 37. `settings.html`'s `account-deletion.html` forward reference doesn't match this session's `deactivated.html`

**Session:** M7. **Surface:** M6's `pages/settings.html` versus this session's
`pages/deactivated.html`.

M6's `settings.html` links its "Delete your account" action at `account-deletion.html`, and
CRIB.md registered that filename as a forward reference expected to land in "M7's account-edges
session." This session's own prompt, however, specifies `deactivated.html` as the page to build
for the deletion grace period — a different filename for what is functionally the same surface
`account-deletion.html` was standing in for. `account-deletion.html` itself is therefore never
built, and `settings.html`'s link now points at a filename this track will not produce.

**Drawn:** nothing corrected, following the same precedent M3, M4 and M6 already set for a link
sitting inside a file outside the current session's own touched set (entries 8, 16, 20, 21, and
most directly 27, which records the analogous `report.html` / `report-post.html` mismatch).
`settings.html` is left exactly as M6 built it. `banned.html`, built this session, faces the same
choice for its own "Delete your account" action and resolves it by pointing at
`account-deletion.html` too — consistent with `settings.html` rather than with
`deactivated.html`, since `deactivated.html` as built assumes a deletion is already under way (it
shows the grace-period banner and a cancel button), which is not the state either linking page is
in. A founder decision or a later pass can retarget both links to whichever page is meant to
carry the actual deletion *confirmation* step — a step neither M6 nor M7 built, since both
sessions' own prompts named the pages around it (settings, and the grace-period view) rather than
that step itself.

---

## 38. Splitting the two required states across `reset-request.html` and `reset-code.html`

**Session:** M7. **Surface:** `pages/reset-request.html`, `pages/reset-code.html`.

The M7 prompt lists two required states under one shared header covering both files — "the time
limit is told to the user in text, and they can always request a new code" and "the lockout
state" (login attempts rate-limited per account and per source address, §4.6.1) — without saying
which file gets which.

**Drawn:** the time-limit text and the "request a new code" link went on `reset-code.html`, since
that is the page that actually carries the time-limited code (`RESET_CODE_TTL_MINUTES` = 15) and
an expired-code state alongside it. The lockout message went on `reset-request.html` instead,
reasoning that a person who has just been locked out of *login* is the person this page's own
purpose — starting a password reset — exists to help next; the message is rendered as a second,
clearly separated state on that page rather than invented as a new state on `login.html`, which
the M7 prompt does not ask for. Recorded because it is a page-organization judgment call filling
a real gap in the prompt's own structure, in the same spirit as entries 24 and 25's control-shape
decisions.

---

## 39. `invite-redeem.html` cannot render David's own view, and reuses him as the inviter instead

**Session:** M7. **Surface:** `pages/invite-redeem.html`.

Every mockup in this track renders David's own point of view, with a small number of established
exceptions (M2's Priya, M4's preview-as pages) where SPEC's own rules make David's view
impossible to use for the thing being demonstrated (entry 12). Account redemption is a new
exception in the opposite direction: nobody has an account yet at the point this page renders, so
there is no "David" to be logged in as at all.

**Drawn:** David stands in as the **inviter** instead of the viewer — a role any other
established friend could equally have played — which has the added benefit of letting the page
state §4.1's automatic inviter/invitee friendship concretely ("you and David automatically become
friends") rather than abstractly. See `mockups/CRIB.md` §3 for the cast note.

---

## 40. Two messages this session had to invent, since SPEC gives no wording for either

**Session:** M7. **Surface:** `pages/errors.html` (§9.3's single response), `pages/invite-redeem.html`
(§4.5's blocklisted-name rejection).

§9.3 requires "a viewer who may not see a profile gets one response," identical across a block, no
mutual friend, a deactivated account, a banned account, and a profile that never existed — but
never states what that one response actually says. §4.5 requires a blocked display name to be
"rejected at save time with an honest message" — but likewise gives no wording.

**Drawn:** both messages are this session's own invented text — *"This page isn't here, or you
don't have permission to see it"* and *"That name isn't allowed on WeeBee. Please choose a
different one"* — deliberately generic in the second case, since the message can't quote the
blocklist itself back at the user without exposing it. Flagged here, and in `mockups/CRIB.md`,
because both read easily as SPEC-verbatim quotes the way most of this track's other quoted
strings are, and are not.
