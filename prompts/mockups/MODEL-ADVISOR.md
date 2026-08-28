# Model advisor recommendations — mockup track

Recommendations from the `model-advisor` agent for how to configure each session in the
`prompts/mockups/` track, generated 2026-08-28. These are suggestions for which Claude model
and effort/reasoning level to run each session with before pasting the prompt in — not part of
the mockup track's own rules, and not something the mockup sessions need to read.

| # | File | Recommendation |
|---|---|---|
| M1 | [M1-scaffold-and-feed.md](M1-scaffold-and-feed.md) | Sonnet 5, high effort |
| M2 | [M2-composer-and-post-views.md](M2-composer-and-post-views.md) | Sonnet 5, high effort |
| M3 | [M3-profile-friend-view.md](M3-profile-friend-view.md) | Sonnet 5, high effort |
| M4 | [M4-visibility-set.md](M4-visibility-set.md) | Sonnet 5, high effort |
| M5 | [M5-friendship-and-contact-flows.md](M5-friendship-and-contact-flows.md) | Sonnet 5, high effort |
| M6 | [M6-authoring-and-forms.md](M6-authoring-and-forms.md) | Sonnet 5, high effort |
| M7 | [M7-account-edges.md](M7-account-edges.md) | Sonnet 5, high effort |
| M8 | [M8-emails.md](M8-emails.md) | Sonnet 5, high effort |

All eight sessions landed on the same configuration, for the same underlying reason: every
prompt in this track is exhaustively specified (exact copy, exact constants, exact section
citations back to SPEC.md/ARCHITECTURE.md) rather than open-ended, so there's little call for
Opus-level judgment. What drives effort up to **high** instead of medium is breadth and
verification load — several files per session, many small correctness traps (ARIA/a11y rules,
negative requirements like "no page numbers," "no relative ages," "no CAPTCHA"), and a mandatory
"before you finish" checklist plus CRIB.md/NOTES.md/index.html bookkeeping that has to be run
for every page, not sampled.

---

## M1 — scaffold and feed

**Recommendation:** Sonnet 5 at high effort

**Why:** Ambiguity 2 and novelty 2 — the prompt is unusually well-specified (exact constants,
verbatim strings, file layout, a checklist at the end) with a clear template to follow, so this
doesn't need Opus-level judgment. Reasoning depth is low-moderate (mechanical HTML/CSS
templating plus careful accessibility rule-following, not architecture). Breadth 3 and autonomy
3 push effort up: it's ~10 files (build script, five partials, stylesheet, CRIB/NOTES, index,
feed page) with a lot of cross-referencing to exact SPEC line numbers and a mandatory self-check
list before finishing — that's the kind of multi-step, verification-heavy work where effort
matters more than raw model capability.

**Dial it down if** you're comfortable reviewing the output closely yourself — Sonnet 5 at
medium would save cost, but given the "don't invent, note gaps in NOTES.md" discipline this task
demands, high is worth it.

**Dial it up if it struggles:** If Sonnet produces markup that's factually wrong against SPEC
(wrong constant, invented feature, made-up nav item) despite having the section text in front of
it, that's a ceiling problem — bump to Opus. If it instead skips a checklist item, forgets to
update NOTES.md/index.html, or stops before finishing all the required page states, that's an
effort problem — bump to xhigh.

---

## M2 — composer and post views

**Recommendation:** Sonnet 5 at high effort

**Why:** This is well-specified, not ambiguous — the prompt pins exact section numbers, line
ranges, verbatim strings, constants, and even the accessible names to use, so ambiguity is low
(2). Reasoning depth is moderate (2-3): mostly translating spec prose into semantic HTML/CSS
using existing partials, no architecture decisions. Breadth is real (4) — four pages, dozens of
interlocking requirements (live regions, ARIA names, focus rings, 320px reflow, alt-text flow),
and autonomy/verification is significant (4) — it must self-check against a checklist (headings,
labels, tabindex, horizontal scroll) before finishing, then update CRIB.md/NOTES.md/index.html.
That breadth-and-verification profile is what pushes effort to high rather than medium — this is
a "don't stop until every checklist item is actually verified" task, not a quick scoped edit.
Novelty is low since it's copying an established pattern from M1's partials.

**Dial it down if** you want a faster/cheaper first pass and are willing to review the
accessibility details yourself — Sonnet 5 at medium would likely get the structure right but
might be less rigorous about every ARIA-name and 320px edge case.

**Dial it up if it struggles:** Watch for the failure mode. If pages come out with real errors —
wrong ARIA names, wrong visibility logic, misunderstanding which content gets reactions vs. not —
that's a reasoning ceiling problem, bump to Opus 5. If instead it skips a page, forgets the
NOTES.md write, doesn't actually verify 320px reflow, or leaves the horizontal-scroll check
undone — that's an effort/thoroughness problem, bump to xhigh.

---

## M3 — profile friend view

**Recommendation:** Sonnet 5 at high effort

**Why:** Ambiguity is low (2/5) — the prompt cites exact SPEC/ARCHITECTURE line ranges and
quotes the literal text to render, leaving little to interpret. Reasoning depth is low (2/5) —
this is precise markup composition against explicit rules, not architecture or tradeoff work.
Novelty is low (1/5) — it explicitly reuses M1's partials and pattern. Breadth is moderate (3/5)
— seven output files (four tabs, two overlay states, plus CRIB.md/NOTES.md/index.html updates)
with many "easy to get wrong" gotchas called out (no reactions on these tabs, empty alt on
overlay images, no page numbers unless paging, exact ARIA/heading structure). That combination —
clear spec, many small correctness traps, several files to keep consistent — is exactly
workhorse territory: Sonnet 5 with high effort so it reads all the cited sections, builds every
file, and runs the "before you finish" checklist rather than shortcutting it.

**Dial it down if** you just want a rough first pass to sanity-check the file structure — Sonnet
5 at medium would do, accepting it might miss a couple of the finer gotchas (e.g., the
pinned-post "no tombstone" rule).

**Dial it up if it struggles:** watch which way it fails. If it renders something factually
wrong despite having the spec text in front of it (e.g., misjudges what §9.1 "friend view"
actually requires) — that's a ceiling problem, bump to Opus 5. If instead it skips a file
(forgets one of the two overlay pages), doesn't run through the full "before you finish"
checklist, or leaves CRIB.md/NOTES.md/index.html unupdated — that's an effort problem, bump to
xhigh so it doesn't stop short across this many files.

---

## M4 — visibility set

**Recommendation:** Sonnet 5 at high effort

**Why:** This is well-specified, not ambiguous — the prompt is exhaustively detailed (exact copy
strings, exact tab logic, exact frozen/live field splits) with citations back to specific spec
sections, so ambiguity and novelty are low (2/5): there's a clear template to follow, not
invention. It's mechanical-but-large frontend HTML/CSS work (static pages, no scripts, reuse
existing styles.css and M1 partials), so reasoning depth is low-moderate (2/5). Breadth is what
pushes this up: 10 pages across 4 distinct surfaces, each with several negative-requirement
checks (no tab strip, no placeholders, no counts, specific ARIA/a11y rules) that need verifying
per-page, plus cross-file bookkeeping (CRIB.md, NOTES.md, index.html). That breadth and the
"check every page against a checklist before finishing" requirement is a thoroughness/
verification problem, not a smarts problem — hence high effort rather than a bigger model.

**Dial it down if** you want a faster, cheaper first pass and are willing to manually spot-check
the negative requirements yourself — Sonnet 5 at medium would likely still produce correct
pages, just with less rigorous self-checking.

**Dial it up if it struggles:** If pages come out with plausible-but-wrong content (e.g.,
misapplying which fields are frozen vs. live, or getting the FoF tagged-filter logic wrong)
despite having read the spec, that's a ceiling problem — bump to Opus 5. If instead it skips a
page, forgets to update CRIB.md/NOTES.md, or leaves a placeholder/count in violation of the
explicit "before you finish" checklist, that's sloppiness — bump to xhigh effort, not the model.

---

## M5 — friendship and contact flows

**Recommendation:** Sonnet 5 at high effort

**Why:** This is well-specified, template-driven frontend work — the prompt spells out exact
fields, wording (much of it verbatim quotes), file names, and reuses M1's partials/M4's markup,
so ambiguity and novelty are low (2/5). It's not architecturally hard (reasoning depth 2/5), but
it's broad — six HTML pages, a field-source table to render exactly, several silent/no-
notification behaviors to get consistently right across pages, plus CRIB/NOTES/index updates and
a long accessibility checklist to verify (breadth 4/5, autonomy 4/5). That combination — easy to
understand, but a lot of ground to cover thoroughly and check off — is exactly what effort (not
model tier) is for. High effort gives it room to read all the cited SPEC sections, build all six
pages, and actually run through the "before you finish" checklist rather than skipping items.

**Dial it down if** you want a faster/cheaper first pass and are willing to review the checklist
yourself — Sonnet 5 at medium would likely produce most of the pages fine, just with more risk of
missed checklist items.

**Dial it up if it struggles:** Watch which failure mode shows up. If pages come out with the
*wrong* facts — e.g. it lets the decline leak, or gets the frozen/live split wrong despite
reading §9.1 — that's a reasoning-ceiling problem, bump to Opus 5. If instead it just skips a
page, forgets to update CRIB.md/NOTES.md/index.html, or doesn't run the full pre-finish
checklist, that's an effort problem — bump to xhigh.

---

## M6 — authoring and forms

**Recommendation:** Sonnet 5 at high effort

**Why:** Ambiguity is low-to-moderate (2/5) — the prompt is extremely precise, quoting exact
spec text and required behaviors, but two pages (settings, groups) require assembling scattered
requirements and labeling them clearly as inferred, which needs care. Reasoning depth is low
(mechanical HTML/CSS composition from partials, no architecture decisions). Breadth is high (7
pages, many fields, cross-referencing ~12 spec sections) and autonomy/length is high (long
unattended run, multiple checklist items to verify at the end — Apply-button behavior, labels,
a11y checks, NOTES.md, CRIB.md, index.html updates). This is exactly the "well-specified but wide
and long, with a verification checklist" profile that Sonnet at high effort handles well without
paying for Opus-level reasoning it doesn't need.

**Dial it down if** you just want a fast first pass on one or two pages to sanity-check the
approach before running the full session — Sonnet 5 at medium is fine for that.

**Dial it up if it struggles:** If it gets details factually wrong (e.g., misreads what belongs
in settings.html vs groups.html, or mishandles the ambiguous report-form note requirement)
despite having the spec in front of it — that's a ceiling problem, bump to Opus 5. If instead it
skips a page, forgets to update CRIB.md/NOTES.md/index.html, or doesn't run through the full
"before you finish" checklist — that's a thoroughness problem, bump effort to xhigh.

---

## M7 — account edges

**Recommendation:** Sonnet 5 at high effort

**Why:** Ambiguity is low (2/5) — the spec quotes exact copy, exact constants, exact rules for
nearly every page; only `invites.html` is explicitly flagged as inferred. Reasoning depth is
low-medium (2/5) — no architecture or tradeoff calls, just careful transcription of spec
requirements into HTML/CSS following the established M1 harness/pattern. Novelty is low (1/5) —
this is session 7 of 8 in a track with conventions already set. Breadth and autonomy are the real
drivers here (4/5): nine pages, cross-referencing a dozen spec sections, updating
CRIB.md/NOTES.md/index.html, plus a long pre-finish verification checklist (accessibility, no
CAPTCHA, exactly one page with absolute dates, no fetches on maintenance.html) that spans every
file. That's a job for high effort — enough budget to touch all nine pages and actually run the
checklist rather than sampling a few.

**Dial it down if** you're comfortable reviewing the output yourself and want a faster/cheaper
pass — Sonnet 5 at medium would likely still hit the mechanical parts fine, just with less
certainty the full checklist gets applied to every page.

**Dial it up if it struggles:** watch which way it fails. If a page's *content* contradicts the
spec (wrong wording on the breach promise, wrong constants, an invented reason on banned.html)
despite having read the sections — that's a ceiling problem, bump to Opus 5. If instead it skips
a page, forgets to update NOTES.md, or half-runs the pre-finish checklist — that's an effort
problem, bump to xhigh so it doesn't stop short with nine pages and a long verification list to
get through.

---

## M8 — emails

**Recommendation:** Sonnet 5 at high effort

**Why:** Ambiguity is low (2) — the prompt enumerates exactly nine templates with precise
content rules pulled from spec sections, and even gives verbatim strings to reuse. Reasoning
depth is modest (2) — no architecture or tradeoff decisions, just correct application of
well-specified rules (codes vs. links, absolute vs. relative timestamps, no excerpts). Breadth is
moderate-high (3-4) — nine templates × two files each (HTML + plain-text), plus updates to
CRIB.md, NOTES.md, and index.html, so there's a lot of mechanical surface area and easy-to-miss
checklist items. Novelty is low (1-2) since it's following an established mockup pattern from
prior sessions. Autonomy/length is moderate-high (4) — a long unattended run with many small,
easy-to-drop compliance checks (no images, no relative ages except two exceptions, no links
except one, plain-text fidelity, 320px reflow). This profile — clear spec, low reasoning, but
wide checklist-driven breadth — is exactly Sonnet's sweet spot; the effort dial (high, not
xhigh) reflects that it's a lot of file output with a strict compliance checklist to self-verify
against, but not an open-ended multi-day refactor.

**Dial it down if:** you want a faster/cheaper first pass and are willing to manually spot-check
the "no link except invite" and "no relative age" rules yourself — Sonnet 5 at medium would
likely still produce good templates, just with less rigorous self-checking against the "Before
you finish" list.

**Dial it up if it struggles:** distinguish which failure mode you see. If a template gets a
*rule wrong* (e.g., puts a link in reset-code, uses a relative age in inactivity-deletion)
despite having the spec excerpts right there, that's a genuine misunderstanding — bump the model
to Opus 5. If instead it *skips* the plain-text file for one template, forgets to update
CRIB.md/NOTES.md, or doesn't run the final checklist across all nine — that's it doing too little
work, not being too dumb — bump the effort to xhigh instead.
