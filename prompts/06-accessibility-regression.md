# Prompt 06 — Accessibility after launch, and the operator-console hedge

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** SPEC.md §16.1 and §16.5, ARCHITECTURE.md §9, BUILD_PLAN.md §16.5 and §17.3
> **Depends on:** prompt 01.
> **Expected outcome:** two decisions — how conformance is held after launch, and whether
> the Django admin is in scope or exempt.

---

You are working in the WeeBee design-document repository. Read `README.md`, then `SPEC.md`
§16 in full, `ARCHITECTURE.md` §3.8 and §9, and `BUILD_PLAN.md` §2.5, §8.2, §15.2, §16.5
and §17. This is a **founder-directed design session**; you may edit all three documents.

Two items. They are related only in that both concern §16, and both are places where the
documents currently say something softer than the commitment they sit under.

---

## Item 1 — Conformance is verified once, then never again

### What the reviewer said, and what is actually true

An external reviewer of version 1.16 claimed the accessibility testing is manual only,
with no automated scanning, and that focus order, keyboard operability, screen-reader
announcements and error associations go untested.

**Most of that is wrong.** BUILD_PLAN §16.5 pass 1 already runs an axe/`pa11y` scan.
ARCHITECTURE §9 already specifies template smoke tests (every `<img>` has `alt`, every
input has a label, one `<h1>`, a `<title>`, no positive `tabindex`) and a contrast test
over every `THEME_SET` combination. Passes 2 through 4 are keyboard, screen reader, and
zoom/reflow — exactly the things the reviewer said were missing. ARCHITECTURE §9 even
states why the human passes cannot be automated.

**The reviewer's second point stands.** Every one of those checks is a **gate**, run once,
at Step 16.5, immediately before launch. SPEC §17's "Everything after this is SPEC v1.16+"
means features will keep arriving, and nothing in the plan re-runs any of it. Accessibility
regressions are among the easiest defects to introduce and the hardest to notice: nothing
looks wrong, no test fails, no user files a bug — the person who can no longer use the page
simply stops using it, on a network where they were invited by a family member.

This is a real gap in a project that ranks accessibility with the tracking ban.

### What to work out with the founder

1. **Which checks become continuous rather than one-off.** The contrast test and the
   template smoke tests are ordinary Python tests that already run on every step — those
   are effectively continuous today. Confirm that, and say so in SPEC §16.5, because right
   now §16.5 describes only a pre-launch audit and hides the fact that two thirds of the
   mechanical checks already run constantly.

2. **Whether the axe/`pa11y` scan can join them.** ARCHITECTURE §9 deliberately keeps it
   as optional local tooling and *not* a project dependency, and the reasoning is good
   (nothing accessibility-related ships to the browser). Running it against a locally
   served instance as part of a check the founder runs — rather than as an app dependency
   — may thread that needle. Decide, and if the answer is no, say why in §9 so it is not
   re-proposed.

3. **A re-audit trigger.** The five-pass human audit is hours of work and cannot run per
   commit. Define when it repeats. Candidates: after any phase that adds a new interactive
   pattern (a picker, a modal, an expandable); on a fixed calendar cadence; before any
   invite expansion. Recommend a rule that is small enough to actually be followed — a rule
   the founder skips is worse than a rule that is modest.

4. **Where the ongoing obligation lives.** BUILD_PLAN ends at Phase 17. §17.3's operator
   runbook is the only document describing life after launch, and it currently covers
   moderation, disk, backups and OS updates. If accessibility re-verification is not in
   that runbook, it does not exist.

5. **The honesty rule already covers the failure case.** §16.5 requires that a known
   unfixed defect be listed in the accessibility statement rather than papered over. Check
   that the statement (BUILD_PLAN §15.2) is described as a living document rather than a
   launch artifact — a statement written once and never revised quietly becomes a false
   claim, which is exactly what the honesty rule forbids.

---

## Item 2 — The operator console is neither in scope nor exempt

SPEC §16.1 scopes the commitment, then says:

> The **operator console** (Django admin, §13) is held to the same standard as far as the
> framework allows; where it falls short, the shortfall is the operator's own, not a user's.

A reviewer called this a cop-out. That is too strong — the reasoning is real, and "the
shortfall is the operator's own" is a genuine distinction on a platform with exactly one
operator. But the sentence does not resolve anything. "As far as the framework allows"
states no obligation and can be satisfied by doing nothing, in a section whose opening
sentence is that a feature which cannot be made accessible is not shipped.

Two things make this worth settling rather than leaving:

- **The operator will not always be this founder.** §15.3 contemplates funding phases and
  §2 contemplates going public. "The operator is me and I can see fine" is a statement with
  an expiry date, and the document does not acknowledge that.
- **§13's operator duties are not trivial.** The moderation queue, the hashtag vocabulary
  editor, the URL allowlist editor with its redirector checks, the request queue. These are
  daily-use surfaces, not a settings page visited twice.

### What to work out with the founder

Pick one and write it plainly:

- **(a) Explicit exemption.** The operator console is outside the WCAG AA commitment, with
  the reason stated and the consequence acknowledged: if the operator role is ever held by
  someone the Django admin excludes, that is a problem the project has committed to solving
  then, not now. This is defensible and honest.
- **(b) A bounded commitment.** The admin is in scope for a named subset — keyboard
  operability and contrast, say — which is roughly what Django's admin actually delivers
  and what can be verified cheaply. Anything beyond that is out of scope.
- **(c) Full scope.** Which realistically means building a custom operator interface, since
  Django's admin cannot be made to conform by configuration. ARCHITECTURE §3.1 leg 2 makes
  "the Django admin is the operator console for free" one of the five reasons Django was
  chosen — so this option is a stack-level decision, not a §16 tweak. Weigh it honestly and
  expect to reject it.

Recommend (b) if a bounded subset can be stated crisply; otherwise (a). Whichever is
chosen, the accessibility statement (BUILD_PLAN §15.2) should say which, because "we
conform to WCAG AA" with a silent carve-out is the kind of claim §16.5's honesty rule
exists to prevent.

---

## Constraints to respect

- **WCAG 2.1 AA is not up for review.** README states this explicitly: *how* to hit AA is
  open, *whether* is not.
- **No overlay widgets, no separate accessible version, no CAPTCHA** (§16.4). Nothing here
  reopens those.
- **No third-party JavaScript ships to the browser**, ever (§15.2, ARCHITECTURE §3.8). Any
  tooling proposal must be a build-time or founder-run tool, never a page dependency.

## Before you finish

- Write the CHANGELOG.md entry, naming every file's status including unchanged ones.
- Record the operator-console decision with its reasoning in-document, not only in the
  changelog — it is exactly the kind of thing a future reader will otherwise re-open.
- Update `TODO.md`.
