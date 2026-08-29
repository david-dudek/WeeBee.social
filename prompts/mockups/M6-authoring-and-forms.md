# Mockup session M6 — editing, managing, and the forms that reach the operator

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** `mockups/pages/` (post editor, gallery management, report forms, operator request, hashtag suggestion, settings, groups), `mockups/CRIB.md`, `mockups/NOTES.md`, `mockups/pages/index.html`. **No design document is edited.**
> **Depends on:** M1 (harness, crib sheet), M2 (the composer, which the post editor mirrors), M3 (the gallery these controls manage).
> **Expected outcome:** the remaining authoring surfaces exist — and the two pages the documents do **not** specify are built and clearly labelled as unspecified rather than quietly invented.

---

You are working in the WeeBee design-document repository — a small, private, deliberately
anti-viral social network whose design documents exist but whose platform has not been built.
Read `README.md`, then `prompts/mockups/README.md`, `mockups/NOTES.md` and `mockups/CRIB.md`.

This is session M6 of eight building **browser-viewable mockups of the design exactly as
`SPEC.md` and `ARCHITECTURE.md` already describe it.**

**Two pages in this session are not specified by either document** — settings and groups. Build
them, because SPEC §16.1 names settings as an in-scope surface and §6 implies a group editor,
but **label each page visibly as assembled or inferred**, and record in `mockups/NOTES.md`
exactly which parts came from where. They are closer to proposals than mockups, and the founder
must be able to tell at a glance.

## Standing constraints

- **Build only what the documents describe.** No invented features, no fixes. Contradictions
  go in `mockups/NOTES.md`; build on regardless.
- **Never edit** `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md` or
  anything in `prompts/`. Write inside `mockups/` only.
- **SPEC leads** where ARCHITECTURE lags it (prompt 09 has not been run).
- **Neutral, layout-true fidelity**; the existing `styles.css`; no invented brand palette.
- **Static pages, no scripts**; **nothing fetched from anywhere**; compose the M1 partials.
- **Separate simulated content from build commentary.** Every sentence on a page is either
  something WeeBee would actually say to a user who has never read a design document
  (simulated content — plain, warm, non-technical language) or a note to the founder about how
  the page was built (commentary — SPEC/ARCHITECTURE citations, invented-vs-established calls,
  cross-references to another mockup file, NOTES.md or CRIB.md). Never mix the two in one
  sentence or paragraph. Wrap every commentary block in `.commentary` (a distinct
  italic-monospace style in `styles.css`) so the shared header's build-commentary checkbox in
  `_base.html` can hide it. See `prompts/mockups/content-commentary-separation.md` for the full
  rule, worked examples, and the toggle mechanism.

## What to read

| Document | Sections | Lines (v1.27) |
|---|---|---|
| SPEC | §7.8 Editing posts and comments | 352–378 |
| SPEC | §7.9 Stated visibility | 378–411 |
| SPEC | §9.4 (the gallery, reordering, the alt-text re-prompt) | 571–597 |
| SPEC | §13.2 Reporting | 792–812 |
| SPEC | §13.5 Operator request channels | 865–876 |
| SPEC | §11.2.1 The vocabulary as an operational commitment | 673–694 |
| SPEC | §7.7.1 Paging long lists (the page-size setting) | 341–352 |
| SPEC | §9.1.1 Theming (the theme and font settings, the viewer override) | 542–554 |
| SPEC | §12.3 Coalescing and following (the follow default) | 766–777 |
| SPEC | §4.6 Authentication (the email change), §4.7 Deletion, §4.9 Export | 102–107, 135–143, 150–153 |
| SPEC | §6 Groups | 201–210 |
| SPEC | §16.3, §16.4 | 1027–1089 |

## What to build

### 1. `pages/post-editor.html`

§7.8. **What may be edited: a post's text, its image, its preformatted toggle, and its
hashtags; a comment's text. Nothing else.**

- **The "edited" marker**: permanently displayed as real text beside the post's age, carrying
  the relative time of the most recent edit. **No version history and no diff** (§7.8).
- **Replacing an image re-prompts for alternative text** — §16.3 requires a deliberate choice
  every time (§7.8, §9.4).
- **Editing hashtags is an audience change and is treated as one** (§7.8, v1.16). The editor
  shows **the same live audience line as the composer** (§7.9), updating as tags change — and
  §7.8 is explicit that *"it is not a warning that appears only on 'dangerous' choices — a
  notice people can learn to click through is worth nothing."* So the line is always present.
- **Adding a tag to a post that already has comments** re-exposes those comments. The editor
  says so, verbatim: *"This post has comments. Widening who can see it also shows those
  comments to the people it reaches."* Render that state.
- **Removing a tag narrows the audience and notifies nobody** — no warning on that path.
- **Comments may be edited only by their author.** The post's author can **delete** any comment
  on their post but may never edit one (§7.8, §8.1) — *"deleting someone's words is a host's
  prerogative, rewriting them is ventriloquism."* Show both controls on the right posts.

### 2. `pages/gallery-manage.html`

§9.4, the Photos tab in its owner-facing state:

- `GALLERY_MAX` = 8, separate from the profile photo. **Order is author-arranged**, new images
  placed first on upload and freely rearranged thereafter.
- **Reordering uses "Move up" / "Move down" controls named from the image's own alternative
  text** — §9.4's own example is *"Move 'Me on a beach in Cornwall' up"* — **with the result
  announced in a polite live region** (§16.3, 4.1.3). Use the `_status.html` partial.
- **Drag-and-drop may be offered in addition, never instead**: §9.4 — *"a reorder only a mouse
  can perform is a 2.1.1 failure."* Since the mockups carry no scripts, render the buttons and
  say in visible text that drag-and-drop would be additive.
- **Replacing an image re-prompts for alternative text.** The same applies to the profile
  photo.
- **Editing an image's alternative text alone changes nothing else** — no hold, no
  notification (§9.4).
- **No caption field** — the alternative text is the caption (§9.4, §17).
- The profile photo control: every account has one at all times, **there is no "no photo"
  state**, and the picker over `DEFAULT_AVATAR_SET` sits beside upload. **Selecting a picker
  image triggers no hold and no notification**; uploading one does (§9.4, §13.6). Say so in
  real text where the user makes the choice.

### 3. `pages/report-post.html` and `pages/report-profile.html`

§13.2. **There is one report form, and it always carries a reason category.** The action is a
real `<button>` with visible text, **never an unlabelled icon** (§13.2, §16.4), and it is
available to any viewer who can see the target — **not to its owner**.

- **Post and comment reasons**, verbatim from §13.2: *harassment or abuse · unwanted or
  commercial content · someone else's private information · **the tags don't match this post**
  (profile posts only) · something else*.
- **Profile target categories**, verbatim: *the photo · the name · the short bio · the about
  section · the gallery · this person's behaviour*.
- **A short free-text note to the operator.** §13.2 says this is not an exception to §13.1's
  no-free-text principle, *"which governs user-to-user surfaces; a report reaches the operator
  alone."*
- **A NOTES.md entry is required here.** §13.2's sentence — *"There is one report form, and it
  always carries a reason category, plus the optional short note to the operator this section
  already gives profile reports"* — reads most plainly as extending the note to post and
  comment reports too, but it is ambiguous. **Render the plainest reading, flag the ambiguity,
  and do not resolve it.**
- Reported content **stays live while the report is open** (§13.3) — nothing on the page should
  suggest the content has been removed by reporting it.

### 4. `pages/operator-request.html` and `pages/hashtag-suggest.html`

§13.5: **one simple submission form with a category dropdown**, feeding the operator queue.
Categories, verbatim: *Hashtag suggestion · External service request · Bug report ·
Accessibility problem · General feedback / feature request*. §13.5 notes accessibility problems
are **triaged ahead of feature requests** — say so on the page.

**The confirmation copy does the whole job**, because no reply is ever sent. §13.5 and §11.2.1:
submissions are **read in batches, no reply is sent, and an accepted change simply appears
where it belongs** — a new tag in the picker, a domain in the allowlist. **No interval is
stated to users. There is no status page, no "pending" state, and no per-submission outcome.**
Render the confirmation; do not invent a tracking surface.

`hashtag-suggest.html` is the path from the picker's **empty search result** (§11.2.1): when a
search matches no tag and no alias, the picker **says so plainly and offers the suggestion
form** — and *"it never presents a text field that would accept a tag and then silently fail to
create one."* Show the empty result and the form together. Note on the page that **aliases are
never displayed, never selectable, and are not tags** (§11.2.1).

### 5. `pages/settings.html` — **assembled, not specified**

SPEC §16.1 names settings as an in-scope surface, but **no section of SPEC defines the page.**
Assemble it from the settings each section mentions, cite each one on the page itself, and
label the page visibly as assembled:

- **Page size** — `POSTS_PER_PAGE_DEFAULT` = 20, from `POSTS_PER_PAGE_OPTIONS` 20 / 40 / 60,
  one setting applying to the feed and every profile visited. §7.7.1: it **takes effect on an
  explicit Apply, never on the change of a dropdown** — *"a control that reloads the page the
  instant it is touched is a 3.2.2 failure."* This one is a hard requirement, not a detail.
- **Theme and font** from `THEME_SET`, plus the **"always use my own theme" viewer override**
  (§9.1.1), which is *"applied server-side at render, never as a client-side toggle a page
  could defeat."* `THEME_SET` has **no members named anywhere in either document** — say so on
  the page and in NOTES.md rather than inventing a list of theme names.
- **The global follow-by-default setting** (§12.3).
- **Optional email notifications** (§12 opening: delivery is in-feed *"plus optional email"*).
- **Login email change**, completed with a **numeric code sent to the new address and typed
  back into the already-open settings page** — never a link (§4.6, §4.6.1).
- **Data export** (§4.9) — a complete copy in JSON plus image files.
- **Account deletion** (§4.7) — request, then a `DELETE_GRACE_DAYS` = 30 grace period. The
  deletion flow itself is session M7; link to it.

### 6. `pages/groups.html` — **inferred, not specified**

§6 gives the rules but describes no screen. Build the minimum they imply and label it inferred:

- Named groups, **private to their owner; members never know they are in one.**
- `GROUP_SIZE_MAX` = 30, matching the feed-post audience cap so any group is always a valid
  post audience.
- **The UI warns when an edit would exceed the cap and refuses it** — an honest text error
  naming the fix (§16.3).
- **The platform must not auto-create, auto-populate, or auto-modify groups.** The only
  suggestion permitted is the composer's "Save this selection as a group?", which is *"memory
  of the user's explicit choices, never behavioral inference about relationship strength."*
  Nothing on this page may imply otherwise.

## Before you finish

Check every page, as in the earlier sessions, plus three specific to this set:

- **the page-size control has an explicit Apply** and does nothing on change (§7.7.1)
- **`settings.html` and `groups.html` each carry a visible label** saying the documents do not
  specify them, with the sections each part came from
- **every form field has an associated visible label and every error is text tied to its
  field** (§16.3 1.3.1, 3.3.1, 3.3.2, 3.3.3) — this session is almost entirely forms, so it is
  the session where the `_field.html` and `_errors.html` partials earn their keep

Plus the standing list: one `<h1>` and a unique `<title>` per page; skip link first focusable;
`lang` set; landmarks present; every `<img>` has an `alt`; no `tabindex` above 0; no `title`
attribute; no timestamp in any markup attribute; reflow at **320 px** with no horizontal page
scroll.

Then: add this session's strings to `CRIB.md`, add its pages to `pages/index.html`, update
`NOTES.md`, and **print the contents of NOTES.md**. Do not touch `TODO.md` or `CHANGELOG.md`.
