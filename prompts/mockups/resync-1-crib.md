# Mockup track re-sync R1 — the crib sheet

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** `mockups/CRIB.md` and `mockups/NOTES.md`. **No page is edited, no partial, no
> stylesheet. No design document is edited.**
> **Depends on:** the `main` → `mockups` merge (commit `2079802`). This branch must carry SPEC
> 1.30 before the session starts — the first instruction below checks it.
> **Blocks:** R2 (the link cluster) and R3 (the card cluster). Neither may start until this
> lands, because both quote strings this session registers.
> **Expected outcome:** `CRIB.md` is a true register of SPEC 1.30, so every session after it
> quotes 1.30 strings instead of 1.27 ones.

---

You are working in the WeeBee design-document repository — a small, private, deliberately
anti-viral social network whose design documents exist but whose platform has not been built.
Read `README.md`, then `prompts/mockups/README.md`, `mockups/NOTES.md` and `mockups/CRIB.md`.

This is session **R1** of the re-sync described in `prompts/mockups/resync-to-1.30.md` — read
that file too; it is short, and it records the five founder decisions this work runs under. The
mockup track was built against project version **1.27**. SPEC is now **1.30**, and three
versions of change have landed that the track has never seen.

**Check the branch before you do anything else.** Run `git branch --show-current` and confirm
`mockups`, then `grep -m1 "Project version" README.md` and confirm **1.30**. If either is
wrong, stop and say so — `mockups/CRIB.md` does not exist on `main`, and a session that starts
in the wrong place will create files rather than edit them.

**The unifying rule of this session: `CRIB.md` is a register, not a design surface.** It exists
so that M2–M8 quote constants and interface strings instead of re-deriving them from a 267 KB
SPEC each time. That makes it the highest-leverage file in the track and the most dangerous one:
a wrong string here propagates silently into every session that follows. Copy character for
character. Where SPEC gives no wording and one has to be invented, **say so in the entry
itself** — an unmarked invention is indistinguishable from a quotation to the next reader.

## Standing constraints

- **Build only what the documents describe.** No invented features, no fixes. Contradictions go
  in `mockups/NOTES.md`; build on regardless.
- **Never edit** `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md`, or
  anything in `prompts/` outside `prompts/mockups/`. Write inside `mockups/` only.
- **SPEC leads** where ARCHITECTURE lags it (prompt 09 still has not run, by founder decision —
  the re-sync goes first).
- **Edit no page this session.** Not `composer.html`, not `contact-card-editor.html`, not
  `contact-card-received.html`, however plainly wrong they now are. They are R2's and R3's work
  and they are already scheduled. Registering the strings is this session's whole job.
- **Do not remove or renumber existing `CRIB.md` entries** — the file's own header says so, and
  later sessions cite its section numbers.
- **Do not resolve contradictions**, including the "Posts" / "Blog" one already logged at
  `CRIB.md` §2 under §16.3.
- **Separate simulated content from build commentary** per
  `prompts/mockups/content-commentary-separation.md`. `CRIB.md` is entirely commentary — it is a
  note to the founder and to later sessions, never a surface a user sees — so the `.commentary`
  class does not apply here. What matters is that the *strings it registers* are recorded as the
  user-facing text they will become, quoted exactly and never blended with explanation.

## What to read

Do **not** read `SPEC.md` whole — it is 267 KB. Read these sections. Line ranges are correct as
of project version **1.30**; **the section number is authoritative** if the file has moved.

| Document | Sections | Lines (v1.30) |
|---|---|---|
| SPEC | §7.2.3 The two link lists (rewritten v1.29) | 306–339 |
| SPEC | §7.2.4 What happens to a link: three outcomes (new v1.29) | 340–369 |
| SPEC | §10.2 Card contents (amended v1.29) | 742–755 |
| SPEC | §10.4 Requesting a card, and the card page (amended v1.30) | 762–780 |
| SPEC | §13.2 Reporting — the contact-card material | 920–987 |
| SPEC | §13.2.1 — the card-item "delete content" outcome only | 988–1037 |
| SPEC | §14 Configuration Constants | 1082–1141 |
| SPEC | §16.3 Requirements by area | 1213–1268 |

That is roughly 330 lines, and §13.2.1 is the only one you read selectively. **Nothing from 1.28 is on the list, and that is deliberate:** SPEC
§1.4, the Gathering Test, adds no constant, no state and no surface — the CHANGELOG's 1.28 entry
says so in those words and records that nothing is owed downstream. It generates no crib entry.

## What to change

### 1. The two stale statements of fact

- **`CRIB.md` line 7** reads *"All citations are to SPEC.md at project version 1.27 unless marked
  ARCHITECTURE."* → **1.30**.
- **The note under §1's table** reads *"Full table: SPEC §14 (lines ~898–953 at v1.27)."* §14 now
  begins at line **1082** and runs to **1141**. Correct the range and the version.

### 2. Section 1 — three rows to add to the constants table

Keep the existing `| Constant | Value | Ref |` shape and leave every existing row alone.
`CONTACT_ITEMS_MAX` = 12 is already there and is still correct.

- **`CARD_ITEM_LABEL_MAX`** — **40 characters** (v1.29). The label on a contact-card item. Ref
  §10.2. Worth carrying its condition into the Value cell as the table already does for
  `NAME_CHANGE_COOLDOWN_DAYS`: it is new free text on a surface that had none, so it is capped
  hard *and* screened against `NAME_BLOCKLIST` at every save.
- **URL allowlist** — operator-curated. Each row carries an **admitting category** and a
  **surface scope**: posts and comments, contact cards, or both (v1.29). **Messenger domains are
  card-only.** Ref §7.2.3.
- **URL blocklist** — operator-curated, **new in v1.29**. Domains refused outright, in any form,
  on every surface. Checked by the same shared validator as the allowlist, on **every save path,
  create and edit alike**. Retired by deactivating, never deleting. **No appeal channel.** Ref
  §7.2.3, §7.2.4.

Note in the entry that the last two are operator-maintained tables rather than constants in
code — §14 marks them, and a page must never render them as a code-style constant.

### 3. Section 2 — the strings SPEC gives verbatim

Add these as new `### §…` blocks in the existing style. All are quoted directly from SPEC; copy
them exactly, including the em dashes.

**§7.2.3 — the composer and help copy.** SPEC says the stated purpose "stays exactly that", so
these two are quotations, not paraphrases:

> *"WeeBee doesn't host video or audio. This is where your own recording lives."*

> *"WeeBee holds one photo per post. If you have sixty, they live somewhere else — link to them
> here."*

**§13.2 — the contact-card report target categories:**

> *the label · the address or number · the card as a whole · this person's behaviour.*

Record with them that **"the card as a whole" is reachable from any item's button**, and that
**an empty card carries no report action at all**.

**§13.2 — the per-item report button.** Visible text: *"Report this item"*. Its accessible name
must name its own item, and SPEC gives both forms:

> *"Report the item labelled 'My photos'"* — taken from the item's label.
> *"Report the third item, a phone number."* — for an item whose label is empty, named by kind
> and position instead.

### 4. Section 2 — extend the two blocks that already exist

- **The §13.2 report-reasons block** currently carries the post/comment reasons and the profile
  target categories. Add the card categories from §3 above as a third list. **Leave the first two
  untouched** — 1.30 added a fourth target, it did not alter the existing three.
- **The §16.3 worked-examples list** gains two entries, because §16.3 names both explicitly as
  repeated controls needing distinct accessible names: the **copy control on a link's copy box**
  (v1.29), and the **per-item card report action** (v1.30), of which one page may carry
  `CONTACT_ITEMS_MAX` = 12.

### 5. The three strings that must be invented — mark every one

SPEC specifies what these must *do* and gives no wording. Write them, register them, and label
each one **invented** in the `CRIB.md` entry itself.

1. **The blocklisted-link refusal.** §7.2.4 requires that it say plainly that this address cannot
   be posted here **and that the fix is to remove it**, per §16.3's rule that an error states its
   fix. It must **name no appeal**, because there is none — §7.2.3 is explicit that an error
   gesturing at a door that does not open is worse than one that names no door. This is the
   string to be most careful with; R2 will quote it into `composer.html` and `post-editor.html`.
2. **The copy control's accessible name.** §16.3 requires it to say *which address it copies* —
   a feed page may carry many, and an element list reading "Copy" twelve times is the dead end
   the rule exists to prevent. Register a pattern, in the shape of the existing
   *"Read more of David's post from a few days ago"* entry.
3. **The copy confirmation.** §7.2.4 requires the copy to be confirmed **in a polite live
   region**, composing the existing `_status.html` partial (which is already correct — it is
   `role="status" aria-live="polite"`; do not write a new one).

**The hard constraint on all three, and on every entry in §3 and §4: a copy box is not an
error.** §7.2.4 is unambiguous — an address on neither list gets "no warning, no apology, no
error styling, no 'this link is not approved' note beside it." Only the blocklisted case is an
error. If a string you write reads as a telling-off, it is wrong.

### 6. `NOTES.md` — append, never resolve

It is notes for the founder's review, **not a to-do list**. Add at least:

- The three invented strings, with what SPEC did and did not specify for each.
- **The §10.4 "and nothing else" question.** §10.4 says the card page carries the owner's display
  name, the items the viewer may see, *and nothing else* — while `contact-card-received.html`
  currently carries a *"Request more access (may ship in v1.1)"* section from §10.5. Whether a
  v1.1 feature belongs on a page §10.4 closes with those words is a real reading question.
  **Record it. Do not resolve it, and do not touch the page.**
- **Two open filename questions**, for R3 to settle when it builds: whether the card page keeps
  the name `contact-card-received.html` now that §10.4 makes it a page rather than a received
  reply, and what the new card report form is called. `CRIB.md` §5 lists the nav target filenames
  M1 assumes; **read it, and leave it alone this session** — naming a page belongs to the session
  that builds it.

## Before you finish

**The accessibility checklist does not apply to this session** — no page is built, so there is
nothing to check for landmarks, labels or reflow. Do not go looking for page work to justify it.

Check instead:

- **Every quoted string is character-for-character from SPEC.** Re-open the section and compare;
  do not check it from memory.
- **Every citation points at the section that actually says the thing.** Section numbers moved
  between 1.27 and 1.30 and several sections were rewritten under the same number.
- **Every invented string is marked as invented** in `CRIB.md` *and* recorded in `NOTES.md`.
- **No existing entry was removed or renumbered.**
- **`git status --short` shows exactly two modified files**: `mockups/CRIB.md` and
  `mockups/NOTES.md`. If anything else appears — a page, a partial, `styles.css`, a law file —
  revert it before finishing and say what happened.

Then print the diff of `CRIB.md` and the contents of `NOTES.md`. Do not touch `TODO.md` or
`CHANGELOG.md` — this track produces no version bump and no CHANGELOG entry, and the founder's
Q4 decision keeps it outside the queue. The one record of this work outside `mockups/` is a line
in `prompts/mockups/README.md`, and that is written at close-out (R5), not here.
