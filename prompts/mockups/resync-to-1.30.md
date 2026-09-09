# Mockup track — re-sync plan, SPEC 1.27 → 1.30

**Status:** agreed plan, not yet executed. Written 2026-09-08 against project version 1.30.
**Scope:** `mockups/` and `prompts/mockups/` only. No law file is edited by this plan or by
the work it describes.
**Founder decisions this plan records** (taken 2026-09-08, all five put and answered before
any of it was written):

| # | Question | Decision |
|---|---|---|
| Q1 | Which branch | **Merge `main` into `mockups`**, work there |
| Q2 | Full re-run or targeted patch | **Targeted patch** of the affected pages |
| Q3 | Do the M prompts get updated | **Yes — full revision of all eight** |
| Q4 | Tracked in `TODO.md`'s queue | **No.** Note it in `prompts/mockups/README.md` instead |
| — | Run prompt 09 first | **No.** Re-sync now; 09 later |

---

## 1. The branch, and the merge

Work happens on **`mockups`**, after merging `main` into it.

**The merge is clean, and this was verified rather than assumed.**
`git merge-tree --write-tree refs/heads/mockups main` returns a tree OID with **zero
conflicts**. The
reason is that the two branches touched strictly disjoint file sets since their merge base
(`fac2288`):

- `mockups` has not touched `SPEC.md`, `README.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`,
  `CHANGELOG.md`, `TODO.md` or `prompts/09-sync-arch-and-buildplan.md` at all.
- `main` has not touched `prompts/mockups/` or `mockups/` at all.

**Disambiguate the branch name in every git command.** A directory named `mockups/` exists
alongside a branch named `mockups`, so a bare `mockups` argument is ambiguous and git will
refuse it — this was hit while verifying the merge. Use `git switch mockups` (which only takes
branch names) and `refs/heads/mockups` anywhere a revision is wanted.

The merge brings `mockups` the 1.28/1.29/1.30 SPEC, prompts 13/14/15, the updated 09, and
`main`'s person-tagging `TODO.md` commit. `mockups` keeps `MODEL-ADVISOR.md`,
`content-commentary-separation.md`, its longer `prompts/mockups/README.md`, and the nine-line
commentary rule in each of the eight M prompts.

**Do not let `mockups/site/` be committed.** It is generated output. It is gitignored on the
branches that carry the track, but shows as untracked on `main` because `main` lacks those
`.gitignore` lines — a stale `mockups/site/` from an earlier checkout is sitting in the working
tree on `main` right now. Confirm `git status` is clean of it after the merge.

**`archetypes` was considered and is not used.** It descends from `mockups`, so it carries the
1.27 SPEC and would need this same merge anyway; it is additionally missing `main`'s `06ef1e0`
and carries archetype material irrelevant to this work.

---

## 2. What 1.28 owes: nothing

**No mockup work comes from 1.28.** SPEC §1.4, the Gathering Test, is a stated principle with
no user-facing surface. This is verified, not assumed: the CHANGELOG's 1.28 entry records
ARCHITECTURE and BUILD_PLAN as *"unchanged — version header only, and nothing is owed,"* and
its "Nothing downstream" section states that §1.4 *"asserts nothing a test could check, and
adds no constant, no state and no surface."*

No page changes. No CRIB entry. It is named here so that a future reader can see it was
addressed rather than overlooked.

---

## 3. The pages that change

Verified page by page against `mockups/pages/` on the `mockups` branch. **Every page named
below exists**, except the one marked NEW.

### 3.1 Substantively wrong — the page says something 1.30 contradicts

| Page | Session | Governing SPEC | What is wrong now |
|---|---|---|---|
| `composer.html` | M2 | §7.2.4, §7.2.3, §16.3 | Its `<h2>9. A rejected link` (line 204) refuses `https://bit.ly/3xyz9` with `aria-invalid="true"` and a `.field-error`. Under §7.2.4 an address on **neither** list is not refused and is **not an error**: it renders as an inert copy box with *"no warning, no apology, no error styling, no 'this link is not approved' note."* The section must become **two** cases — a copy box with no error affordance at all, and a **blocklisted** domain genuinely refused. The `bit.ly` example cannot stay as a refusal: §7.2.3 says a shortener is *never allowlistable*, which makes it a copy box, not a refusal, unless the operator blocklisted it. |
| `contact-card-editor.html` | M5 | §10.2, §7.2.3, §14 | Line 16 says items are drawn from *"phone numbers, email addresses, and messenger links"*; §10.2 now says *"phone numbers, email addresses, and links."* Line 17 says a link *"is only accepted from the official domain of a recognized messenger"* — now false: **a link item may carry any URL**. The three radio buttons (lines 23–25) offer "Messenger link" and must offer **"Link"**. Every item now carries a **label**, `CARD_ITEM_LABEL_MAX` = 40, screened against `NAME_BLOCKLIST` at every save. |
| `contact-card-received.html` | M5 | §10.4, §13.2, §7.2.4 | Wrong **shape**, not merely out of date. It is titled *"Requesting a contact card"* and built around *"What Alice receives"* — the one-time reply of §10.4 before 1.30. The answered card is now **a page**: one per (owner, viewer) pair, at its own permission-checked address (§9.3), **resolved live on every visit, never stored**, carrying the owner's display name through the shared helper (§4.5.1), the items that viewer may see, **and nothing else**. Returning to it is not a new request: no notification (§12.1), no rate-limit consumption (§13.6). It gains **one "Report this item" button per item**. |
| `profile-about.html` | M3 | §9.1, §10.4 | The About tab must carry the friends-only **contact-card control** — *"the request, or the link to the card once it has been answered (§10.4, v1.30)"* (§9.1's tab table). Not present. §9.1 also states this is *"a control, not a field"* and therefore does not disturb the basic-tier invariant — worth reading before drawing it, because the invariant is load-bearing. |

### 3.2 Needs the new surface added — the page is not wrong, it is incomplete

| Page | Session | Governing SPEC | What to add |
|---|---|---|---|
| `report-card.html` **(NEW)** | M6 | §13.2 | The card report form. Target categories **verbatim**: *the label · the address or number · the card as a whole · this person's behaviour*, plus the optional short note to the operator. Sits beside the existing `report-post.html` and `report-profile.html`, which are unchanged. |
| `post-feed.html` | M2 | §7.2.4 | A copy box in an ordinary post body — the common case, and the one §7.2.4 says the whole no-scolding rule exists to protect. |
| `overlay-post.html` | M3 | §7.2.4, §16.3 | A single-post view is where **many** copy controls collect, so it is the page that demonstrates the distinct-accessible-name rule §16.3 names explicitly. |
| `preview-as-friend.html` | M4 | §13.2, §9.5 | It already renders the card (line 74, *"Contact card, as Alice would see it"*). §13.2: *"In preview-as the action renders and does nothing."* Add the report buttons, inert. |
| `index.html` | M1 | — | A row for `report-card.html`; the M5 description changes from a received reply to a card page. |
| `styles.css` | M1 | §7.2.4, §16.3 | **No copy-box class exists** (verified: the file has `.field-error`, `.contact-card-preview`, `.contact-card-label`, `.contact-card-value`, and nothing for a copy box). It must wrap **break-anywhere inside its own container** and must **not** acquire a horizontal scrollbar — §7.2.4 is explicit that this would be a second 1.4.10 reflow exception arriving by accident, and §7.2.1's preformatted post stays the only documented one. It must not look like an error. |
| `partials/_post.html` | M1 | §7.2.4 | The copy box inside a post body, so no page hand-rolls it. |
| `partials/_status.html` | M1 | §7.2.4 | **Already correct — compose it, do not invent one.** It is `<p class="status-message" role="status" aria-live="polite">`, which is exactly the polite live region §7.2.4 requires the copy confirmation to use. |

### 3.3 Checked and **not** affected — stated so it is visibly addressed

- **`errors.html`** — the prompt that commissioned this plan listed it as a candidate. It is
  **not** affected. Its four sections are permission, rate limit, feed-post spacing and the
  empty feed; the blocklist refusal is a **composer field error**, not a page-level error state.
- **`post-preformatted.html`** — §7.2.1 is unchanged.
- **`report-post.html`, `report-profile.html`** — §13.2 adds a *fourth target*, it does not
  alter the first three. Their report reasons are unchanged.
- **The M8 email set** — no email in §16.1's scope carries a link outcome or a card report.
  Confirm in session rather than assuming; it is the cheapest of the eight to check.

---

## 4. Order of work

Six steps. Steps 2–5 are separate sittings; see §7.

1. **Merge.** `git switch mockups && git merge main`. Verify zero conflicts, verify
   `mockups/site/` is not staged, rebuild, confirm the site still builds.
2. **`CRIB.md` first.** It is the register M2–M8 read instead of re-deriving, so a stale CRIB
   propagates a stale string into every session after it. Details in §5. **Nothing else starts
   until this is done.**
3. **The link cluster** — `composer.html`, `post-feed.html`, `overlay-post.html`,
   `partials/_post.html`, `styles.css`.
4. **The card cluster** — `contact-card-editor.html`, `contact-card-received.html`,
   `profile-about.html`, `preview-as-friend.html`, and the new `report-card.html`. The largest
   step; `contact-card-received.html` is a rebuild, not an edit.
5. **The M prompt revision** — all eight, per Q3. Details in §6.
6. **Close out** — `index.html` row, `NOTES.md` entries, the `README.md` line from Q4, rebuild,
   run the accessibility checklist each M session ends with.

Steps 3 and 4 are independent of each other and may be swapped. Step 5 may be done before 3
and 4 if you would rather have the prompts correct first; the plan puts it after because the
pages will teach it things — in particular the exact copy that gets invented in step 3.

---

## 5. `CRIB.md` and `NOTES.md`

### `CRIB.md` — updated

Three kinds of change, all verified against the current file:

**a. Stale statements of fact.**
- Line 7: *"All citations are to SPEC.md at project version 1.27 unless marked ARCHITECTURE."*
  → 1.30.
- Line 41: *"Full table: SPEC §14 (lines ~898–953 at v1.27)."* → §14 now begins at **line 1082**.

**b. New constants** in §1's table:
- `CARD_ITEM_LABEL_MAX` = **40 characters** (v1.29) → §10.2.
- The **URL allowlist** row gains its **admitting category** and **surface scope** (v1.29);
  messenger domains are **card-only**.
- The **URL blocklist** row is new (v1.29) → §7.2.3, §7.2.4.
- `CONTACT_ITEMS_MAX` = 12 is already present and correct.

**c. New verbatim interface strings** in §2. These are given word-for-word in SPEC and must be
copied, not paraphrased:
- §7.2.3's two composer/help lines, which that section says stay *"exactly"* this:
  *"WeeBee doesn't host video or audio. This is where your own recording lives."* and
  *"WeeBee holds one photo per post. If you have sixty, they live somewhere else — link to them
  here."*
- §13.2's **card report target categories**: *the label · the address or number · the card as a
  whole · this person's behaviour.*
- §13.2's **report-button naming pattern**: *"Report the item labelled 'My photos'"*, and for an
  item with no label, *"Report the third item, a phone number."*
- The existing §13.2 report-reasons block (line 226) gains the card target, without disturbing
  the post/comment and profile lists.

**One string has to be invented**, and it is the one to be most careful with. §7.2.4 requires
the blocklist refusal to *"say plainly that this address cannot be posted here and that the fix
is to remove it"* and to **name no appeal** — but gives no verbatim wording. Write it, put it in
`CRIB.md` marked as invented, and record it in `NOTES.md` as a place the documents were silent.
§16.3's rule that an error states its fix is the constraint; §7.2.4's *"names no appeal, because
there is none"* is the trap.

### `NOTES.md` — appended, never resolved

It is notes for the founder's review, **not a to-do list**; nothing in it gets fixed by this
track. Entries this work will generate, at minimum:

- The invented blocklist refusal copy (above).
- **§10.4 says the card page carries the owner's display name, the permitted items, "and
  nothing else"** — while `contact-card-received.html` currently carries a
  *"Request more access (may ship in v1.1)"* section from §10.5. Whether a v1.1 feature belongs
  on a page §10.4 closes with *"and nothing else"* is a genuine reading question. **Record it;
  do not resolve it.**
- Any place §7.2.4's copy box collides with an existing layout.

---

## 6. The M prompts — full revision (Q3)

Every one of the eight cites at least one section that 1.28–1.30 changed. Verified by grepping
each prompt for the changed section numbers:

| Prompt | Changed sections it cites | Depth |
|---|---|---|
| M1 | §4.6.1, §7.2, §7.5, §7.8, §9.1, §14, §16.3, §17 | **Heavy** — the "What to read" table is the main job |
| M2 | §7.2, §7.2.1, §7.2.3, §7.5, §9.1, §16.3 | **Heavy** — §7.2.3 rewritten, §7.2.4 new and uncited |
| M3 | §7.2, §7.5, §9.1, §9.4, §13.2, §16.3 | Moderate |
| M4 | §9.1, §13.2, §16.3, §17 | Light |
| M5 | §7.5, §9.1, §10.1, §10.2, §10.4, §13.1, §13.2, §16.3 | **Heavy** — §10.2 amended, §10.4 rewritten |
| M6 | §4.6.1, §7.8, §9.1, §9.4, §13.1, §13.2, §13.3, §13.5, §16.3, §17 | **Heavy** — gains the new report page |
| M7 | §4.6.1, §7.2, §7.5, §13.2, §16.3, §17 | Light |
| M8 | §4.6.1, §7.5, §13.2, §16.3, §17 | Light |

**M1's "What to read" table is the single most important fix.** Its header says the line ranges
are *"correct as of project version 1.27"* and that *"the section number is authoritative."* The
section numbers are mostly still right, but the line numbers have all moved and **one row is
wrong in substance**: SPEC §14 is cited at lines **898–956** and now begins at **1082**. Either
re-derive every range against 1.30 or drop the column and keep the section numbers — dropping it
is defensible, since the column's own header concedes it is only a hint, and it is the part
guaranteed to rot again at 1.31.

**M2 and M5 need new content, not corrections.** M2 does not cite §7.2.4 because §7.2.4 did not
exist; M5 was written against a §10.4 that has been rewritten. **M6 gains the new report page.**

Do **not** disturb: the nine-line commentary rule in each prompt, the two standing rules, the
fidelity rules, or the SPEC-led rule. This is a revision, not a rewrite.

---

## 7. Cost

**These are estimates, not measurements. I have no instrumentation for what a past M session
actually consumed.** They are anchored on what the eight M commits produced — 700 to 1,553
inserted lines across 8 to 25 files each — and on the size of what has to be read.

| Step | Estimate | Notes |
|---|---|---|
| 1. Merge | negligible | Minutes. Verified conflict-free in advance. |
| 2. `CRIB.md` | 40–70k tokens | Targeted SPEC re-reads plus edits. |
| 3. Link cluster | 100–150k | One new rendering, applied across four files plus CSS. |
| 4. Card cluster | 150–250k | The big one. A page rebuilt from scratch and a page created. |
| 5. M prompts ×8 | 250–400k | Reading all eight is ~84 KB (~25k tokens) before a single edit. This is the step Q3 made expensive; a targeted-rows-only revision would have been roughly half. |
| 6. Close out | 40–60k | Index row, NOTES entries, README line, rebuild, a11y checklist. |
| **Total** | **~600k–950k tokens** | |

**Plainly: this is not one sitting on a Claude Pro plan.** Budget **three to four sittings across
two or three days**. The natural split is one sitting per numbered step, with steps 2 and 6
folded into their neighbours if a window has room left.

**The two steps most likely to overrun** are step 4 — because `contact-card-received.html` is a
rebuild against a rewritten §10.4 and the temptation is to re-read §10 whole — and step 5, where
reading eight prompts before editing any of them is a large fixed cost paid up front. In both,
read targeted sections and stop; `SPEC.md` is 267 KB and reading it whole is never the right move.

---

## 8. Tracking (Q4)

**This work stays outside `TODO.md`'s queue**, consistent with the track's own rule that it is
*"deliberately outside"* it, with no version bump and no CHANGELOG entry.

The one record: in `prompts/mockups/README.md`, the line *"**Started against project version
1.27.**"* is amended to say the track started against 1.27 and was re-synced to 1.30, and to
point here. That is inside `prompts/mockups/`, so it breaks no rule.

**No law file is touched.** Not `TODO.md`, not `CHANGELOG.md`, not `SPEC.md`, `ARCHITECTURE.md`
or `BUILD_PLAN.md`. No version bump.

---

## 9. Unverified — carry these as open

1. **`profile-about.html:39`** carries `<a href="https://www.openstreetmap.org/">here's the
   stretch</a>` in the extended bio — anchor text that is not the URL. §7.2.4 states, of posts,
   that *"a URL is linkified as itself, and there is no markup with which link text could ever
   lie about where it goes."* **I have not read §9.4** and cannot say whether the extended bio is
   plain text under the same rule. Check §9.4 in step 3 before touching the line. Whether
   `openstreetmap.org` is allowlisted is also unverified — §7.2.3 names Google Maps and Apple
   Maps, not OSM.
2. **`post-profile-tagged.html`** may or may not need a copy box. One post view demonstrating the
   rendering may be enough; confirm in step 3 rather than changing it on spec.
3. **The M8 email set** is assumed unaffected. Cheap to confirm; not confirmed.
4. **Whether the card page needs its own filename.** `contact-card-received.html` is the obvious
   home, but §10.4 gives the page its own permission-checked address, and `CRIB.md` §5 lists nav
   target filenames assumed by M1. Check that list before renaming anything.
5. **The token figures in §7 are estimates**, stated as a range for that reason.
