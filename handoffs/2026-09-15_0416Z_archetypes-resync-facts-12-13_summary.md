---
type: handoff-summary
title: "Archetype track re-sync to 1.31: facts 12–13 and delegation rule"
detail: standard
created_utc: 2026-09-15T04:16:49Z
created_local: 2026-09-15T00:16:49-04:00
surface: claude-code
session_id: 2d71ed4a-e4a5-4ed2-9212-092cf5453e31
project_dir: /Users/dudek/Documents/Claude/social network
transcript_file: 2026-09-15_0416Z_archetypes-resync-facts-12-13_transcript.md
previous_summary: none found
---

# Archetype track re-sync to 1.31: facts 12–13 and delegation rule

The session ran the prompt from `archetypes/A0b-resync.md` on the `archetypes` branch: bring the archetype track's three source prompts from project version 1.27 up to 1.31, which SPEC had moved past in how links and contact cards work. It rewrote canonical facts 12 (contact card) and 13 (images and links) in `archetypes/PLAN.md` and `archetypes/A0-brief.md`. It added a "delegation rule" to `archetypes/A7-susan.md`, the pilot character prompt, and fixed stale version stamps and line-number pointers. Exactly three files changed. The edits are now committed on `archetypes` as `ac3655f` ("Ran A0b-resync.md"). `BRIEF.md` and `07-susan.md` have not been regenerated yet.

## Decisions

- **Facts 12 and 13 use the founder-session drafts from the prompt, unchanged, in both files.** Why: every clause checked out against SPEC §7.2, §7.2.3, §7.2.4, §10.2 and §10.4 at 1.31. A script confirmed the two copies match exactly once the blockquote `> ` prefix is stripped. Rejected: none discussed.
- **The quoted line in fact 13 is copied from `mockups/CRIB.md` §2 and was checked against it by script:** *"WeeBee holds one photo per post. If you have sixty, they live somewhere else — link to them here."*
- **The delegation rule's third paragraph was rewritten instead of pasted, because the draft got a fact wrong.** Why: the draft said a photo-host address in a post arrives as a copy box ("not a hyperlink"). But SPEC §7.2.3 puts photo hosts on the allowlist, scoped to posts and comments, so an allowlisted photo host shows as a tappable link. Only an address on neither list becomes a copy box. The draft also contradicted the new fact 13. The replacement heading is "not frictionless". It says the handoff always means leaving WeeBee, and that whether the link is tappable depends on an operator table the exercise can't read. The added sentence in probe 4 also dropped "the address her family copies" and now just says "with the address".
- **The delegation rule sits between "The honesty rule" and "Step 5 — the probes" in `A7-susan.md`.** Why: PLAN §13 copies that stretch of A7 unchanged into the other nine prompts, so the rule will apply to all ten characters. Rejected: putting it in one of the four per-character sections.
- **No fifteenth fact for reporting.** Why: "fourteen" is repeated across PLAN §4, A0-brief, BRIEF §2, and A7's Step 4 and finish checklist. Whether the canonical account should cover moderation at all is the founder's call.
- **`report-card.html` gets a note under PLAN §8's extras table but is not added to Karen's row.** Why: PLAN §7 leaves the choice of a character's pages to the prompt that builds that character.
- **Two stale references outside the prompt's list were fixed anyway, and both were reported.** First, A0 Step 3 told the session to stamp `BRIEF.md` "1.27 … through M8"; it now says 1.31 and "re-synced through the card cluster". Second, A0 Step 2's pointers were out of date: file sizes are now 267 KB / 155 KB, SPEC §1.1–§1.3 is at lines 12–37, and §17 moved from lines 1122–1128 to 1310–1317. A new optional read 4 points at SPEC §1.5 (lines 63–86).

## Open questions

- **Should the canonical account mention reporting?** SPEC §13.2 now lists four report targets: post, comment, profile and contact-card item. No fact mentions any of them, and Karen's prompt sends her straight to the report flows. Adding a fifteenth fact would touch four files plus a checklist. The founder decides.
- **Fact 12 says "asks for it with a button", but SPEC §10.4 says "picker (no text)".** The button wording matches the mockup, which has `<button>Request contact card</button>` in `mockups/pages/profile-about.html`. It doesn't match SPEC's own word. Founder may want to reconcile.
- **Fact 13 no longer says "never embedded players or preview cards".** That's still true (SPEC §7.2) and still listed in BRIEF §4's absence table, but the fact itself no longer says it. Founder may want it restored.
- **The extended bio has no allowlist surface scope** (`mockups/NOTES.md` entry 61, still open). §7.2.3 scopes allowlist rows to posts and comments, contact cards, or both, and the bio is neither. Logged; not touched.
- **Are contact-card labels required or optional?** (`mockups/NOTES.md` entries 64/65.) §10.2 says "every item carries a label", yet §13.2 describes what happens when a label is empty. Fact 12 follows §10.2's wording.

## Next steps

1. **Re-run `archetypes/A0-brief.md`** in a fresh session on `archetypes` to regenerate `archetypes/BRIEF.md` from the corrected sources and re-synced mockups. User starts it. Nothing else in the track can run until this is done.
2. **Re-run `archetypes/A7-susan.md`** to regenerate `archetypes/07-susan.md`. User starts it. Depends on step 1.
3. After judging the new `07-susan.md`, write the other nine character prompts and A11 following PLAN §13. User or a later session does this. Depends on step 2.
4. Founder settles the reporting question, then the button-vs-picker and embed-clause questions under Open questions. Only the reporting one is needed before the nine prompts are copied from A7.

## Files and references

- `archetypes/A0b-resync.md`: the prompt this session ran (added in commit `f81ff4b`).
- `archetypes/PLAN.md`: header provenance now reads 1.31. §4 preamble now says v1.31, and facts 12–13 are replaced. §8 has a new `report-card.html` note. §9 citation line updated, and the Dorothy and Dave Crypto rows were corrected: they had said non-approved links are refused at composition, and now say they arrive as copy boxes, with §7.2.4 added to their citations.
- `archetypes/A0-brief.md`: Step 2 sizes and line pointers updated, including CRIB §2 at lines 78–407, plus the new item 4 (SPEC §1.5). Step 3: version stamp updated and facts 12–13 replaced. The §3 table intro now says v1.31, and three rows were added: `CARD_ITEM_LABEL_MAX` = 40, URL allowlist and URL blocklist, followed by a no-backticks warning for the two lists. The `BIO_EXTENDED_MAX` row now follows §7.2.4. Two bullets were added to §6, pointing at CRIB §2 for the hosting lines and the §13.2 contact-card report strings.
- `archetypes/A7-susan.md`: new `## The delegation rule` section, and probe 4 has a third beat.
- `SPEC.md` sections read: §1.5 (lines 63–86), §7.2 (lines ~284–288), §7.2.3–§7.2.4 (lines 306–369), §9.4 bio rules (lines 675–677), §10.2–§10.4 (lines ~742–782), §13.2 opening.
- `mockups/CRIB.md` §1 (lines 11–76) and §2 (lines 78–407, especially 293–301 and 372–385); `mockups/NOTES.md` entries 59–65 (lines 1410–1644).
- Unchanged, and regenerated later by re-runs: `archetypes/BRIEF.md`, `archetypes/07-susan.md`.

## Since the previous handoff

No previous summary found.

## Caveats

- At handoff time the working copy was on `main`, not `archetypes`. `git status` showed `handoffs/` and `mockups/` as untracked there; that state did not come from this session and wasn't investigated. The session's edits were found committed on `archetypes` as `ac3655f`. Its diff stat against `f81ff4b` (A0-brief +65/−, A7 +27, PLAN +47) is consistent with this session's edits, but a line-by-line comparison wasn't done.
- `handoffs/` isn't gitignored (exporter warning). Review the transcript before committing it.
