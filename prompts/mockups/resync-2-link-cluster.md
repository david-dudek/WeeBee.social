# Mockup track re-sync R2 — the link cluster

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** `mockups/styles.css`, `mockups/partials/_post.html`, and four pages —
> `composer.html`, `post-editor.html`, `post-feed.html`, `overlay-post.html` — plus
> `mockups/NOTES.md`. **No design document is edited. No new page is created.**
> **Depends on:** R1 (commit `30d81c4`), which registered every string this session renders.
> `CRIB.md` §2 is the source for all of them — do not re-derive them from SPEC.
> **Blocks:** nothing. R3 (the card cluster) is independent of this and may run first or
> second; the two sessions share no file, and §6 below says how that is kept true.
> **Expected outcome:** the copy box exists as a real rendering with a real stylesheet class,
> and `composer.html` stops refusing a link that v1.29 says is not refused.

---

You are working in the WeeBee design-document repository — a small, private, deliberately
anti-viral social network whose design documents exist but whose platform has not been built.
Read `README.md`, then `prompts/mockups/README.md`, `mockups/NOTES.md` and `mockups/CRIB.md`.

This is session **R2** of the re-sync described in `prompts/mockups/resync-to-1.30.md` — read
that file too; it is short, and it records the five founder decisions this work runs under. The
mockup track was built against project version **1.27**. SPEC is now **1.30**, and R1 has
already brought `CRIB.md` up to it.

**Check the branch before you do anything else.** Run `git branch --show-current` and confirm
`mockups`, then `grep -m1 "Project version" README.md` and confirm **1.30**. Then confirm R1
landed: `grep -c "INVENTED" mockups/CRIB.md` must return **3**. If any of the three is wrong,
stop and say so — this session renders strings R1 registered, and without them it would invent
a second, different set.

**The unifying rule of this session: a copy box is not an error.** SPEC §7.2.4 is unambiguous —
an address on neither list gets *"no warning, no apology, no error styling, no 'this link is not
approved' note beside it."* Only a blocklisted domain is refused. The page you are most likely
to get wrong is `composer.html`, which today refuses an ordinary link with `aria-invalid` and a
`.field-error`, and the failure mode is subtle: it is easy to soften that section's copy and
leave the error *styling* in place, which still tells the reader they did something wrong. The
rule is about styling and affordances as much as wording. **If a reader could tell from the
shape of the page that the platform disapproves of their link, the section is still wrong.**

## Standing constraints

- **Build only what the documents describe.** No invented features, no fixes. Contradictions go
  in `mockups/NOTES.md`; build on regardless.
- **Never edit** `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md`, or
  anything in `prompts/` outside `prompts/mockups/`. Write inside `mockups/` only.
- **SPEC leads** where ARCHITECTURE lags it (prompt 09 still has not run, by founder decision).
- **Quote `CRIB.md`, do not re-derive.** Every user-facing string this session renders is
  already registered in `CRIB.md` §2, three of them marked **INVENTED**. Copy them character for
  character from there. If you find yourself composing a new sentence for a link outcome, stop —
  either it is in `CRIB.md` already, or you are inventing a fourth string, which is R2 exceeding
  its scope. A genuinely new gap goes in `NOTES.md` and gets registered in `CRIB.md` §2, marked
  invented, exactly as R1 did.
- **Do not remove or renumber existing `CRIB.md` entries.**
- **Do not resolve contradictions**, including the "Posts" / "Blog" one at `CRIB.md` §2 under
  §16.3.
- **Separate simulated content from build commentary** per
  `prompts/mockups/content-commentary-separation.md`. Every sentence on a page is either
  something WeeBee would say to a user who has never read a design document (simulated content —
  plain, warm, non-technical) or a note to the founder about how the page was built (commentary —
  SPEC citations, invented-vs-established calls, cross-references). Never mix the two in one
  sentence or paragraph. Wrap every commentary block in `.commentary`.
- **Touch no page this session other than the four named above.** Not `profile-about.html`, not
  the contact-card pages, not `post-profile-tagged.html` except as §6 permits. They are R3's, and
  §6 explains why one of them stays R3's even though it carries a link problem.

## What to read

Do **not** read `SPEC.md` whole — it is 267 KB. Read these sections. Line ranges are correct as
of project version **1.30**; **the section number is authoritative** if the file has moved.

| Document | Sections | Lines (v1.30) |
|---|---|---|
| SPEC | §7.2.3 The two link lists (rewritten v1.29) | 306–339 |
| SPEC | §7.2.4 What happens to a link: three outcomes (new v1.29) | 340–369 |
| SPEC | §7.8 Editing posts and comments — **invariant 4 only** | 452–477 |
| SPEC | §9.4 Limits, the two bio fields — **the two bio bullets only**, for §6 | 672–697 |
| SPEC | §16.3 Requirements by area | 1213–1268 |
| `mockups/CRIB.md` | **§1 and §2 in full** — the register you are rendering from | — |

`CRIB.md` §2 is not optional reading and not a summary of SPEC: it is where R1 put the exact
strings, including the three it had to invent. Read it before you read SPEC, and read SPEC to
understand the *rules* around the strings rather than to re-derive the strings themselves.

## What to change

Six files plus `NOTES.md`. Work in this order — the stylesheet and the partial first, because
the four pages copy from them.

### 1. `styles.css` — the copy-box class

**No copy-box class exists.** The file has `.field-error`, `.contact-card-preview`,
`.contact-card-label`, `.contact-card-value`, and nothing for a copy box.

Add one. Its obligations are SPEC requirements, not polish:

- It **must not look like an error.** `.field-error` is the shape to stay away from. A copy box
  is ordinary post furniture and should read as such.
- The address **wraps break-anywhere inside its own container** and must **never acquire a
  horizontal scrollbar.** §7.2.4 is explicit that a copy box that quietly scrolled sideways
  would be a second 1.4.10 reflow exception arriving by accident, and §7.2.1's preformatted post
  stays the platform's single documented one. The stylesheet already has
  `overflow-wrap: break-word; word-break: break-word` at lines ~78–79 for ordinary text; a URL
  needs the stronger break, and the difference matters — check it at 320 px rather than assuming.
- The copy control is a real `<button>` with a 44 × 44 px touch target like every other control
  in this stylesheet.

Keep the file's own conventions: neutral greys, mobile-first, the header comment's rules. The
header comment names link blue as the one palette exception (NOTES entry 49) — a copy box is not
a link and should not borrow that colour.

### 2. `partials/_post.html` — the copy box's canonical markup

The partial is a **reference structure, not a literal `{{include}}`** — its own header comment
says so, and `build.py`'s include takes no parameters. Add the copy box to it as one more
documented part, in the same style as the parts already there, so no page hand-rolls the markup.

The shape it must document:

- the address **in full and verbatim** — never truncated in the value itself, never re-written,
  never resolved
- a real `<button>` whose **visible text** and **accessible name** are the ones registered at
  `CRIB.md` §2 under *"The copy control: visible text and accessible name"* — the name begins
  with the visible word, which is what keeps 2.5.3 true
- the visually-hidden naming text, exactly as the existing `read-more` button in this same file
  already does it (`<span class="visually-hidden">`)
- a note that the copy confirmation composes **`partials/_status.html`**, which is already
  correct and must not be rewritten

Add the SPEC references to the partial's existing "Required parts, per SPEC …" comment block so
it stays a true index of what governs the markup.

### 3. `composer.html` — section 9 becomes two cases

This is the substantive fix of the session.

Section 9 is `<h2>9. A rejected link</h2>` at line 204. It refuses `https://bit.ly/3xyz9` with
`aria-invalid="true"` and a `.field-error` whose text runs *"That link isn't allowed in a WeeBee
post…"* Under 1.29 that is wrong twice over:

- An address on **neither list is not refused at all.** It renders as an inert copy box, and the
  composer says nothing about it.
- **The `bit.ly` example cannot stay a refusal.** §7.2.3 says a URL shortener is *never
  allowlistable* — which makes it a copy box, not a refusal, unless the operator has separately
  blocklisted it. A shortener is the textbook thing the allowlist won't make clickable; it is not
  the textbook thing the blocklist refuses.

Rebuild it as **two sections**:

- **An unapproved link** — a link the allowlist does not carry, rendered as a copy box, with
  **no error affordance whatsoever**: no `aria-invalid`, no `.field-error`, no warning, no
  apology, no note beside it. `bit.ly` is the honest example here. The commentary block explains
  why nothing is flagged; the simulated content says nothing at all, because the platform says
  nothing at all.
- **A blocklisted link** — genuinely refused, using the **invented refusal string registered at
  `CRIB.md` §2**, verbatim. This one keeps `aria-invalid` and `.field-error`, because it is the
  one case that really is an error. Use a domain that is plainly a stand-in rather than a real
  site being accused of anything — the operator's blocklist contents are deliberately unspecified
  (§7.2.3), so the example must not imply a policy the documents do not state. Say so in the
  commentary.

**Renumber what follows.** Section 10 (*"Switching destination"*) becomes 11, and the two new
sections take 9 and 10. Check for in-page references to the old numbers before you renumber, and
check that `pages/index.html`'s description of `composer.html` does not quote a section number.

Also fix the section's existing commentary, which states the pre-1.29 rule: *"URLs are permitted
only from the operator-curated allowlist."* That is no longer what the allowlist does — it now
governs **clickability**, not delivery.

One thing worth noticing rather than repeating: the old error text ends *"Anything else can be
shared through your contact card."* That sentence is a rendering of the exact claim SPEC §10.2
identifies as having been **false** when it was written — the card permitted no such item until
v1.29. It is true now, but the section it lived in is gone; do not carry it forward into either
new section, and do not treat its truth as a reason to keep it.

### 4. `post-editor.html` — one line of commentary

Line 31, inside that section's `.commentary` block, says saving *"re-runs every content check a
new post would (length caps, the URL allowlist, whitespace rules)."* Incomplete since 1.29: the **blocklist** is checked by the same
shared validator on **every save path, create and edit alike** (§7.8 invariant 4), and §7.2.3
says in terms that *"a create-only implementation is a defective implementation of this
section."* Name both lists.

**Copy only. No new control, no new section.** This page is otherwise R3-adjacent and you are
not rebuilding it.

### 5. `post-feed.html` and `overlay-post.html` — render the thing

- **`post-feed.html`** gets a copy box in an ordinary post body. This is the common case, and
  §7.2.4 says the whole no-scolding rule exists to protect exactly this reader: an ordinary
  member linking to their own photographs. One copy box, no ceremony, nothing flagged.
- **`overlay-post.html`** is where **many** copy controls collect, so it is the page that
  demonstrates §16.3's distinct-accessible-name rule — the reason the accessible name has to name
  its own address rather than reading "Copy" every time. Put enough of them on the page that the
  rule is visibly doing work.

**Confirm the page shapes before you write.** `overlay-post.html` is built around the image
overlay dialog ("The page behind the dialog" / "The dialog, open"), while `post-feed.html` is the
one that carries comments. Whichever actually holds several links most naturally is the one that
should carry the many-controls demonstration; the plan assigned them from a file list rather than
from the pages. If you swap them, say so in `NOTES.md`.

Neither page currently contains a single `https://` in a post body, so every link here is new
content. Keep it inside the established cast and the established posts (`CRIB.md` §3) rather than
inventing new people or new events for it.

### 6. Two open questions from the plan's §9 — one you answer, one you do not

**a. `profile-about.html:39` — answer it, do not fix it.** The plan lists this as unverified:
the extended bio carries `<a href="https://www.openstreetmap.org/">here's the stretch</a>`, anchor
text that is not the URL, and the plan could not say whether the extended bio falls under the same
rule as a post.

**It does, and §9.4 says so directly** — the extended bio *"follows the uniform link rule of
§7.2.4 — allowlisted links clickable, anything else an inert copy box, blocklisted domains
refused."* So the line is wrong as built on the first count regardless of the second: §7.2.4 says
*"a URL is linkified as itself, and there is no markup with which link text could ever lie about
where it goes."* Whether `openstreetmap.org` is allowlisted (§7.2.3 names Google Maps and Apple
Maps as examples of the Convening category, not as an exhaustive list) decides only whether the
corrected rendering is a hyperlink or a copy box.

**Record the finding in `NOTES.md` and leave the page alone.** `profile-about.html` is R3's — it
also needs the contact-card control added (§9.1), and the plan's own claim that steps 3 and 4 are
independent and may be swapped is only true if no file belongs to both. R3 gets the answer from
your note and makes both changes in one pass.

**b. `post-profile-tagged.html` — decide and say which.** The plan says it *"may or may not need
a copy box. One post view demonstrating the rendering may be enough; confirm in step 3 rather
than changing it on spec."* Confirm it. If two post views already demonstrate the rendering, say
so in `NOTES.md` and leave the page untouched; if you do add one, that is a fifth page and you
should note why.

### 7. `NOTES.md` — append, never resolve

It is notes for the founder's review, **not a to-do list**. R1 left the log at **entry 52**;
continue from 53. Add at least:

- **The §9.4 finding** above, with what it means for `profile-about.html:39` and the explicit
  statement that R3 owns the fix.
- **The `post-profile-tagged.html` decision** and its reasoning.
- **Any place §7.2.4's copy box collides with an existing layout** — the plan anticipates this
  and it is the entry most likely to be genuinely useful to the founder.
- **The blocklisted example domain** you chose on `composer.html`, and the fact that it stands in
  for a list whose contents SPEC deliberately does not specify.

Follow the file's own entry format: `## N. Title`, then `**Session:** … **Surface:** …`, then the
finding, then `**Drawn:**`.

## Before you finish

Rebuild — `python3 mockups/build.py` — and confirm it still builds. `mockups/site/` is generated
output and is gitignored; **it must not be committed.**

Then run the accessibility checklist every M session ends with, on the four pages you touched.
Unlike R1, this session builds, so the checklist applies in full:

- one `<h1>` and a unique descriptive `<title>`; skip link first focusable; `lang` set
- landmarks present; every `<img>` has an `alt`; every input has an associated **visible label**
  (placeholders are never labels)
- no `tabindex` above 0 **except** the preformatted scroll container, which §16.3 requires
- no `title` attribute anywhere; no timestamp in any markup attribute (§7.5.1)
- reflow at **320 px** with no horizontal page scroll — the preformatted post's own container is
  the only thing allowed to scroll sideways, and **the copy box must be checked explicitly
  against this**, since it is the control §7.2.4 warns would create a second exception by
  accident

And check, specific to this session:

- **Every copy control has a distinct accessible name** naming its own address, and the visible
  text is contained in that name (2.5.3).
- **No copy box carries an error affordance** — grep the four pages for `aria-invalid` and
  `field-error` and confirm every remaining instance is a genuine error: the character-cap
  overrun, the audience overrun, the blocklisted link, and nothing else.
- **Every string you rendered matches `CRIB.md` §2 character for character.** Compare against the
  file, not against memory.
- `git status --short` shows **exactly seven modified files** and no new ones: `styles.css`,
  `partials/_post.html`, the four pages, and `NOTES.md` — plus `CRIB.md` **only if** §2 genuinely
  gained an entry under the rule above, which would make eight. If anything else appears — a law
  file, a contact-card page, `mockups/site/` — revert it and say what happened.

Then print the diff of `composer.html` and the new `NOTES.md` entries. Do not touch `TODO.md` or
`CHANGELOG.md` — this track produces no version bump and no CHANGELOG entry, and the founder's Q4
decision keeps it outside the queue. The one record outside `mockups/` is a line in
`prompts/mockups/README.md`, written at close-out (R5), not here.
