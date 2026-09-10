# Mockup track re-sync R3 — the card cluster

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** four existing pages — `contact-card-received.html` (a **rebuild**, not an edit),
> `contact-card-editor.html`, `profile-about.html`, `preview-as-friend.html` — **one new page**,
> plus `mockups/NOTES.md`, `mockups/CRIB.md` (§5, and §2 only if a string is genuinely invented)
> and `mockups/styles.css` if a card row needs a class that does not exist.
> **No design document is edited.**
> **Depends on:** R1 (commit `30d81c4`), which registered the report-button wordings and the
> report target categories in `CRIB.md` §2; and R2 (commit `17d3702`), which built the
> `.copy-box` class and the canonical copy-box markup in `partials/_post.html`. **A card item
> renders under the same §7.2.4 rule a post does** — R3 quotes R2's class, it does not write a
> second one.
> **Blocks:** R5 close-out, which owes `index.html` a row for the new page and a rewritten M5
> description.
> **Expected outcome:** the contact card stops being a message and becomes a page, and every
> item on it can be reported.

---

You are working in the WeeBee design-document repository — a small, private, deliberately
anti-viral social network whose design documents exist but whose platform has not been built.
Read `README.md`, then `prompts/mockups/README.md`, `mockups/NOTES.md` and `mockups/CRIB.md`.

This is session **R3** of the re-sync described in `prompts/mockups/resync-to-1.30.md` — read
that file too; it is short, and it records the five founder decisions this work runs under. The
mockup track was built against project version **1.27**. SPEC is now **1.30**.

**Check four things before you do anything else.** Run `git branch --show-current` and confirm
`mockups`; `grep -m1 "Project version" README.md` and confirm **1.30**; `grep -c "INVENTED"
mockups/CRIB.md` and confirm **3** (R1 landed); and `grep -c "copy-box" mockups/styles.css` and
confirm it is **greater than 0** (R2 landed). If any of the four is wrong, stop and say so. This
session renders strings R1 registered and reuses a class R2 built; without either it would
invent a second, different version of both.

**The unifying rule of this session: §10.4 changed the noun.** Through v1.29 the answered card
was a **reply** — a thing Alice *received*, once, at a moment. In v1.30 it is a **page**: one per
(owner, viewer) pair, at its own permission-checked address, reached from the owner's About tab,
**resolved live on every visit and never stored**, and returned to for as long as the friendship
lasts. Every one of the section's three arguments for that turns on not storing it, and the
report action of §13.2 exists *because* the page is returnable.

The page you are most likely to get wrong is `contact-card-received.html`, and the failure mode
is subtle in exactly the way R2's was: it is easy to add the report buttons, correct the item
renderings, and leave the page's **framing** as a delivery — a title reading *"Requesting a
contact card"*, a heading reading *"What Alice receives"*, a sentence reading *"the system
replies immediately with this"*. All three describe a message arriving. **If a reader could tell
from the shape of the page that the card is something Alice was sent rather than somewhere Alice
goes, the rebuild has not happened.** §3 below says to rebuild the file rather than edit it, and
that is why.

## Standing constraints

- **Build only what the documents describe.** No invented features, no fixes. Contradictions go
  in `mockups/NOTES.md`; build on regardless.
- **Never edit** `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md`, or
  anything in `prompts/` outside `prompts/mockups/`. Write inside `mockups/` only.
- **SPEC leads** where ARCHITECTURE lags it (prompt 09 still has not run, by founder decision).
- **Quote `CRIB.md`, do not re-derive.** The report button's visible text and both of its
  accessible-name forms, and the four card-report target categories, are given **verbatim by
  SPEC** and are already registered at `CRIB.md` §2 under §13.2. Copy them character for
  character. §7 below names the one place this session may have to invent a string, and what to
  do if it does.
- **Do not remove or renumber existing `CRIB.md` entries.**
- **Do not resolve contradictions**, including the "Posts" / "Blog" one at `CRIB.md` §2 under
  §16.3.
- **Separate simulated content from build commentary** per
  `prompts/mockups/content-commentary-separation.md`. Every sentence on a page is either
  something WeeBee would say to a user who has never read a design document (simulated content —
  plain, warm, non-technical) or a note to the founder about how the page was built (commentary —
  SPEC citations, invented-vs-established calls, cross-references). Never mix the two in one
  sentence or paragraph. Wrap every commentary block in `.commentary`.
- **Touch no page this session other than the five named above.** Not `composer.html`, not
  `post-feed.html`, not `index.html`, not `report-post.html` or `report-profile.html` — §13.2
  added a *fourth* report target, it did not alter the first three, and their reason lists are
  unchanged.

## What to read

Do **not** read `SPEC.md` whole — it is 267 KB. Read these sections. Line ranges are correct as
of project version **1.30**; **the section number is authoritative** if the file has moved.

| Document | Sections | Lines (v1.30) |
|---|---|---|
| SPEC | §10 **in full** — §10.1 through §10.5 | 733–787 |
| SPEC | §13.2 Reporting **in full** — the card half begins at "Reporting a contact card" | 920–987 |
| SPEC | §9.1 Structure: header and four tabs — the **tab table** and the contact-card-control bullet | 598–642 |
| SPEC | §9.5 Preview-as | 698–732 |
| SPEC | §7.2.4 What happens to a link — for card items, which follow it | 340–369 |
| SPEC | §4.5.1 Changing a display name — the **shared helper** only | 142–148 |
| `mockups/CRIB.md` | **§1, §2 and §5 in full** | — |

**A correction to the plan, which will save you a decision.** `resync-to-1.30.md` §7 warns that
this step may overrun because *"the temptation is to re-read §10 whole."* Read it whole. §10 is
**55 lines**, the shortest top-level section this cluster touches, and its five subsections all
bear on each other — §10.2's item kinds, §10.3's cascade, §10.4's page. The expensive section
here is §13.2, at 68 lines, and even that is one read.

## What to change

Five pages plus the shared files. Work in this order — the card page first, because the other
four either link to it, preview it, or feed it.

### 1. `contact-card-received.html` — rebuild, do not edit

Delete what is there and write the page §10.4 now describes. Keep nothing because it was already
written; keep only what the rewritten section still asks for.

**What the page is.** One card page per (owner, viewer) pair, at its own permission-checked
address (§9.3), reached from the owner's About tab (§9.1). It carries:

- the owner's **display name**, rendered live through the shared helper (§4.5.1) — which means
  "David Dudek (formerly Dave Dudek)" renders as real text here exactly as it does in the profile
  header, because a name is never stored on content
- **the items this viewer may see**, resolved through §10.3's cascade
- **and nothing else** — §10.4's own closing words. §6 below is about the one thing currently
  sitting on this page that those three words may or may not exclude.

**What the page is not, and this is the substantive fix.** It is not a reply. It is not received.
Nothing about it is stored. §10.4 gives three separate reasons the resolution is live, and they
are worth rendering as real user-facing honesty rather than only as commentary: an item the owner
switches off has to *disappear* from the person it was switched off for; a stored answer would be
a **message**, and §10.1 refuses the category; and a card does not expire (§9.7), so a stored
copy would be a copy with no clock at all. §10.4 also states the honest consequence — a friend
who returns can tell that something changed, because it did, and nothing announces it.

**Returning is not a new request.** No notification (§12.1 fires on the request, not the visit),
no rate-limit consumption (§13.6), and the owner is told nothing. Say so in commentary; §10.4
explains why the obvious implementation — treat every view as a request — would make a friend's
second look at a phone number an event in the owner's feed.

**The item renderings change, and one of them is a trap.** Card items follow §7.2.4's uniform
rule, and the allowlist carries a **surface scope** as of v1.29:

- **Messenger domains are card-scoped**, so a WhatsApp link **on a card is a clickable
  hyperlink** — the same address in a post is a copy box. The page as M5 built it renders it as
  the obfuscated string `wa dot me slash [David's WhatsApp link]`, which is the pre-1.29
  rendering and is now wrong. Make it a real `<a>`.
- **A photo-album, file-store or personal-site link is an ordinary card item** and renders as a
  **copy box** — R2's `.copy-box` markup, quoted from `partials/_post.html`, not re-invented.
  §10.2 names this case explicitly, so put one on the card: it is the whole reason §10.2 was
  amended, and a card with no such item does not show what changed.
- Phone and email items are unchanged.

**Every item carries a label** (§10.2), which the page already renders as
`.contact-card-label` — that part M5 got right.

**The report action.** One `<button>` per item, visible text *"Report this item"*, verbatim from
§13.2 and registered in `CRIB.md` §2. Its accessible name names its own item, and SPEC gives both
forms verbatim — *"Report the item labelled 'My photos'"* from the label, and *"Report the third
item, a phone number."* for an item whose label is empty. Use the second form at least once, or
the page does not demonstrate the rule it exists to demonstrate. Visually hidden naming text,
exactly as the copy control and the read-more folds already do it.

**Three placement rules from §13.2, all easy to get wrong:**

- The action is available to anyone the page is available to — a current friend whose request has
  been answered — and **never to the card's owner**.
- **An empty card carries no report action at all.** The page's existing empty case (Henry) must
  therefore show none. There is nothing on it to report, and a complaint about the person is a
  profile report.
- One action **per item**, never one for the card. §13.2 argues the case: an operator opening
  *"someone reported David's card"* would have to guess which of twelve items, and *"the card as
  a whole"* is a **reason category** reachable from any item's button, not a separate control.

### 2. `report-card.html` — the new page

The card report form, beside the existing `report-post.html` and `report-profile.html`, which are
**unchanged**. Follow `report-profile.html`'s shape closely; it is the closer analogue, and
§13.2 says so in terms.

- **Target categories, verbatim:** *the label · the address or number · the card as a whole ·
  this person's behaviour.* Registered at `CRIB.md` §2; copy them character for character.
- Plus the **optional short note to the operator** every report already carries.
- The page should say, as commentary, what the report captures — §13.2 gives a field table, and
  the three rows that are decisions rather than bookkeeping are worth naming: the **whole
  delivered card** is frozen, not only the reported item; the **cascade is not evidence** and is
  not captured at all; and the freeze is taken at **report time**, not send time, which is where
  this differs from §5.2's friend-request card.
- Render it as **Alice's** view of David's card, matching the viewer `report-profile.html`
  already established.

### 3. `contact-card-editor.html` — three corrections and one new field

- **Line 16** says items are drawn from *"phone numbers, email addresses, and messenger links."*
  §10.2 now says *"phone numbers, email addresses, and links."*
- **Lines 17–18** say a link *"is only accepted from the official domain of a recognized
  messenger … never a bare URL."* Now false: **a link item may carry any URL**, under §7.2.4.
- **The third radio (line 25)** offers "Messenger link" and must offer **"Link"**.
- **Every item now carries a label** (§10.2), `CARD_ITEM_LABEL_MAX` = 40 characters, screened
  against `NAME_BLOCKLIST` at every save. The editor needs the field, its visible label, its
  character count, and its cap-overrun state — `composer.html`'s `.char-count.over-limit` is the
  established pattern. §10.2's own reasoning is worth rendering: the label is new free text on a
  surface that had none, so it gets the short bio's treatment.
- The §10.3 cascade section of this page is **correct** and is not being rebuilt. Leave it.

### 4. `profile-about.html` — two changes, and they are one pass on purpose

**a. The contact-card control (§9.1).** The About tab's tab-table row now reads: short bio,
extended bio, interest hashtags, the people you both know, *"and — friends only — the **contact-
card control**: the request, or the link to the card once it has been answered (§10.4, v1.30)."*
It is not there. Add it, and show **both states** — the request, and the link to the answered
card — since the row names both and a mockup showing one of two states shows half a feature.

Read §9.1's bullet on this before drawing it: *"The contact-card control is a control, not a
field, and the basic-tier invariant below is unaffected."* That invariant is load-bearing — the
header plus About minus the extended bio must stay **exactly** §9.2's basic tier and **exactly**
what §5.2's friend-request card shows, all three from one component. A control adds no field and
appears on none of the three surfaces the invariant governs. Say so in commentary; a later reader
should not have to re-derive why this was safe to add.

**b. Line 39's anchor, which `NOTES.md` entry 53 already settled.** The extended bio renders
`<a href="https://www.openstreetmap.org/">here's the stretch</a>` — anchor text that is not the
URL. §9.4 states that the extended bio *"follows the uniform link rule of §7.2.4 — allowlisted
links clickable, anything else an inert copy box, blocklisted domains refused."* §7.2.4 states
that *"a URL is linkified as itself, and there is no markup with which link text could ever lie
about where it goes."* **The anchor text goes either way.** Whether `openstreetmap.org` is
allowlisted decides only whether the corrected rendering is a hyperlink showing the address as
its own text, or a copy box — §7.2.3 names Google Maps and Apple Maps as *examples* of the
Convening category, not as an exhaustive list, so this track cannot know. Pick the rendering you
can defend, and **record which and why in `NOTES.md`**.

The same section's commentary says *"allowlisted links are permitted (§7.2.3)"*, which is the
pre-1.29 rule and needs the same correction. The **short bio** above it is correct as built and
must stay plain, unclickable text — §9.4 keeps the stricter rule there because the short bio is a
**push surface**, delivered unasked to up to 20 people a day in a friend request. Do not
"consistency-fix" it.

### 5. `preview-as-friend.html` — the inert report buttons

The page already renders David's card as Alice would see it (line 74, *"Contact card, as Alice
would see it"*). §13.2: *"In preview-as the action renders and does nothing."* Add the report
buttons, inert. The preview is a truthful rendering of the surface a friend sees, so hiding them
would misrepresent it; preview mode is already strictly read-only, and §9.5 adds no special case.

Two things to keep: this page renders **David's** preview of Alice's view, so the buttons are
shown to the card's *owner* here — which is exactly the point, and is not a violation of §13.2's
"not to the card's owner" rule, because the owner is previewing rather than reporting. Say that
in commentary; it reads like a contradiction otherwise. And do **not** rebuild the cascade
commentary already on each item; it is correct.

**If the WhatsApp item's rendering changes on the card page (§1 above), it changes here too** —
the two pages must not disagree about what the same item looks like.

## 6. Two decisions this session must make, and neither may be left implicit

**a. Does §10.5's "Request more access" section stay on the card page?** `NOTES.md` entry 51
records this and deliberately does not answer it. §10.4 closes its list of what the page carries
with *"and nothing else"*; the page currently carries a section headed *"Request more access (may
ship in v1.1)"*, drawn from §10.5, a real part of the design marked deferred in SPEC itself. Both
readings hold up, and entry 51 sets out each.

**This is a recommendation, not a founder decision.** It was put to the founder at R2's
close-out and has not been answered; if it is answered before this session runs, that answer
wins over what follows.

**The recommendation is: keep it.** §10.4's list is aimed at excluding a *message* — all three
arguments beneath it are about not storing and not delivering a reply — and §10.5's flags are a
control, not a message. §10.4 also says of §10.5 that its flags *"have always assumed this page
without saying so,"* which is the document noticing the two sections touch. Build it that way,
keep SPEC's own *"may ship in v1.1"* hedge visible exactly as M5 did, and record in `NOTES.md`
that the reading was **chosen on a recommendation rather than derived from the document, and
never settled by the founder** — entry 51 stays open as a question even though the build now has
an answer.

**b. Two filenames, which `NOTES.md` entry 52 left to this session because it builds the pages.**

- **Does the card page keep the name `contact-card-received.html`?** Under v1.30 "received" names
  the moment the card first arrived rather than what the surface is. Against a rename: `CRIB.md`
  §5 records the current name, M5's page set uses it, `contact-card-editor.html` links to it, and
  this track's settled practice (entries 8, 16, 20, 21, 27, 37, 48) is to leave a filename alone
  rather than retarget links in files outside the current session's touched set — though here
  both linking files *are* in your touched set, which is the one thing that has changed.
- **What is the report form called?** `resync-to-1.30.md` §3.2 proposes `report-card.html`, which
  matches the pattern M6 set. Nothing in `CRIB.md` §5 registers it yet.

Whatever you pick, **register both in `CRIB.md` §5** in the same style the M-session paragraphs
there use, and make every link you write resolve to them.

## 7. The one place this session may have to invent a string

`CRIB.md` §2 already carries everything §13.2 gives verbatim. One thing it does not carry: **the
message a card label is rejected with when `NAME_BLOCKLIST` screening refuses it** (§10.2, §4.5).
§10.2 says the label gets the short bio's treatment and gives no wording.

If you render that state on `contact-card-editor.html`, you have three options and must say which
you took: reuse M7's already-registered invented string for a blocked display name — *"That name
isn't allowed on WeeBee. Please choose a different one"* — adapted to a label; write a new one; or
do not render the state at all. If you write a new one, **register it in `CRIB.md` §2 marked
INVENTED**, in exactly the format R1 used for its three, and record it in `NOTES.md`. That is the
only string this session is licensed to invent. If you find yourself composing a second, stop —
either it is in `CRIB.md` already, or R3 is exceeding its scope.

## 8. `NOTES.md` — append, never resolve

It is notes for the founder's review, **not a to-do list**. R2 left the log at **entry 58**;
continue from 59. Add at least:

- **Which reading of §10.4's "and nothing else" you built** (§6a), stated as a choice, with entry
  51 cross-referenced and left open as a question.
- **The two filenames you picked** (§6b), and whether `contact-card-received.html` was renamed —
  with the reasoning either way, since entry 52 explicitly deferred this to you.
- **The `openstreetmap.org` rendering you chose** on `profile-about.html` (§4b) and why, since
  the allowlist's contents are unknowable from these documents.
- **Any place the per-item report action collides with the card's existing layout** — twelve rows
  each carrying a label, a value and a button is the densest repeated-control surface in the
  track, and this is the entry most likely to be genuinely useful to the founder.
- **Anything §10.2's new label field forces on the editor** that §10.2 does not itself specify.

Follow the file's own entry format: `## N. Title`, then `**Session:** … **Surface:** …`, then the
finding, then `**Drawn:**`.

## Before you finish

Rebuild — `python3 mockups/build.py` — and confirm it still builds. `mockups/site/` is generated
output and is gitignored; **it must not be committed.**

Then run the accessibility checklist every M session ends with, on the five pages you touched:

- one `<h1>` and a unique descriptive `<title>`; skip link first focusable; `lang` set
- landmarks present; every `<img>` has an `alt`; every input has an associated **visible label**
  (placeholders are never labels)
- no `tabindex` above 0 **except** the preformatted scroll container, which §16.3 requires
- no `title` attribute anywhere; no timestamp in any markup attribute (§7.5.1)
- reflow at **320 px** with no horizontal page scroll — check the card rows explicitly, since a
  label, a long address and a 44 × 44 button in one row is the narrowest thing this track has
  drawn, and any copy box you render is subject to the same §7.2.4 rule R2 verified

And check, specific to this session:

- **Every report control has a distinct accessible name** naming its own item, and the visible
  text *"Report this item"* is contained in that name (2.5.3). At least one item is named by kind
  and position rather than by label.
- **The empty card carries no report action**, and the card's owner is never offered one outside
  preview-as.
- **Every string you rendered matches `CRIB.md` §2 character for character.** Compare against the
  file, not against memory.
- **No card page says the card was sent, received, replied or delivered.** Grep the rebuilt page
  for those words and justify anything that survives.
- `git status --short` shows **four modified pages**, **one new page**, `NOTES.md` and `CRIB.md`
  — plus `styles.css` only if a card row genuinely needed a class that did not exist. If anything
  else appears — a law file, `composer.html`, `index.html`, `mockups/site/` — revert it and say
  what happened.

Then print the diff of `contact-card-received.html` and the new `NOTES.md` entries. Do not touch
`TODO.md` or `CHANGELOG.md` — this track produces no version bump and no CHANGELOG entry, and the
founder's Q4 decision keeps it outside the queue. The one record outside `mockups/` is a line in
`prompts/mockups/README.md`, written at close-out (R5), not here.
