Context: WeeBee project (this repo). I've run TODO prompts 01–08 and 10–12; only
09-sync-arch-and-buildplan.md remains, and TODO.md says it must run last since it
depends on all the others. Before running 09, I need to read and approve SPEC.md
and ARCHITECTURE.md myself — I have not done that yet, and I may want design
changes as a result. Do not raise or suggest any design changes yourself; that's
my review to do, separately from this task.

I can run a local web server on my Mac or my Bazzite (Linux) machine if that's
useful for the mockups — e.g. to share one nav/header partial across pages
instead of duplicating it in every file, or for live-reload while I review. I'm
not tied to plain static files if serving them works better; decide which is
actually worth it given the scope, don't default to either.

Task: Produce a PLAN (not the mockups themselves) for building browser-viewable
mockups of the design exactly as SPEC.md and ARCHITECTURE.md currently describe it
— no invented features, no fixes for issues you notice along the way. Note any
apparent gaps or inconsistencies you hit while scoping the plan, but don't resolve
or work around them.

Before proposing the plan, ask me to clarify anything that changes its shape,
rather than assuming a default — in particular:
- Which pages/flows to cover (e.g. all of SPEC's page list, or a subset)
- Fidelity level: layout-only wireframes, or styled visual comps (WeeBee has no
  documented visual style guide beyond the name/domain, so "styled" means you'd
  be inventing a look)
- Delivery approach: given a local server is available on either machine, decide
  and recommend whether serving the mockups (shared layout/nav partials, live
  reload) is worth it over standalone HTML files for this page count, or whether
  it's overkill — tell me which you'd pick and why, and keep the tooling as
  simple as the choice allows (don't reach for a build toolchain/framework just
  because a server is on the table)
- Whether this should wait until after I finish my SPEC/ARCHITECTURE review, or
  proceed now against the current version (v1.27)
- Whether to fold this into the existing numbered prompts/TODO.md queue, or keep
  it as a separate, unnumbered track

Once scope is confirmed: if the work fits in one session, describe that single
plan. If it doesn't, break it into multiple self-contained prompts, one per
session, following this repo's existing convention in prompts/ (see prompts/*.md
and TODO.md for the pattern) — but only propose this split; don't create the
prompt files yet without my go-ahead.

Ground rules for how you work on this:
- Do exactly what's asked here — don't expand scope, don't start building
  mockups, don't touch SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md, or TODO.md.
- Base every claim about the design on what SPEC.md/ARCHITECTURE.md actually say
  — quote or cite section numbers rather than paraphrasing from memory. Don't
  invent file paths, section names, or tool capabilities.
- Where something is genuinely unclear or you're inferring rather than reading
  it directly, say so explicitly instead of presenting a guess as fact.
- Before giving me the plan, check it yourself for gaps: pages you might have
  missed, a fidelity/format choice that's inconsistent with itself, effort
  estimates that don't add up.
- I'm on a Claude Pro plan with a fixed monthly budget, not pay-as-you-go API
  usage — so if the full mockup effort (across however many sessions) looks like
  it will consume significant usage, flag that up front as part of the plan,
  and favor the more efficient way to reach the same visual result.
