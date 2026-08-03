# Prompt 02 — Small corrections and two unresolved open items

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md
> **Depends on:** prompt 01 (CHANGELOG.md must exist).
> **Expected outcome:** one version bump covering twelve small items, two of which are
> founder decisions rather than corrections.

---

You are working in the WeeBee design-document repository. Read `README.md`, then
`SPEC.md`, `ARCHITECTURE.md` and `BUILD_PLAN.md`. This is a **founder-directed design
session**, so the BUILD_PLAN §0.2 rule 5 prohibition on editing those files does not
apply — it governs build steps, not design conversations.

Twelve items below came out of an external review of version 1.16. Ten are corrections;
**items 11 and 12 are decisions only the founder can make — ask, do not assume.**

Work through them in order. For each: state what you found in the document, propose the
exact wording, and get agreement before editing. Several are one-line changes; do not
turn them into rewrites. If you find that an item is already handled and the reviewer
missed it, say so and move on — that is a valid outcome, not a failure.

---

## 1. `argon2-cffi` is framed as an exception when it is a requirement

ARCHITECTURE §7 calls it "the **only** addition to the §3 stack for the security layer,
flagged for founder approval per the build-plan dependency rule," and BUILD_PLAN Appendix
rule 6 calls it "the one pre-approved addition."

But SPEC §4.6.1 *requires* Argon2id, so the dependency is not an addition anyone chose —
it is implied by the spec and should have been in the stack from the start. Framing a
mandatory dependency as an exception invites a future builder to treat it as optional.

**Change:** add a row to the ARCHITECTURE §3 stack table (`Password hashing` /
`Argon2id via django[argon2]` / `Slow, memory-hard hash — SPEC §4.6.1`). Then reword §7
and Appendix rule 6 so the dependency rule reads "no new dependencies beyond the §3
stack" with no exception clause, because there is no longer an exception.

## 2. "Months" in the inactivity sweep is never defined

SPEC §4.8 and §14 give the inactivity schedule in months — warnings at 6, 12, 22, 23;
deletion at 24 — and ARCHITECTURE §6 repeats it. Every other time quantity in the project
is a named constant in days, hours or minutes. A builder has to guess whether "6 months"
means 180 days or six calendar months, and the two diverge by days.

**Change:** name the constants in SPEC §14 and define the unit explicitly. Recommend
days (`INACTIVITY_WARN_DAYS` as a list, `INACTIVITY_DELETE_DAYS` = 730) because every
other constant is in days and the sweep is a daily job. If the founder prefers calendar
months, say so in §14 and the arithmetic rule becomes the builder's problem to state.

## 3. Email provider headroom

BUILD_PLAN §5.1 recommends Postmark on the strength of a free tier of 100 emails/month.
Count what Phase 17 actually sends: an invite, a verification code, and a few password
resets per new account, plus inactivity warnings and security notices. Twenty first-circle
users will exceed 100 in the launch month alone.

**Change:** state the real number in §5.1 — what the free tier covers, roughly where it
runs out, and what it costs past that — so the founder is not surprised mid-launch. This
is not a recommendation change; Postmark's transactional-only ethos is why it was picked.

Also check §5.5's verification step: it verifies DMARC via a lookup, but not SPF or DKIM
independently, and does not say "confirm the provider dashboard shows the message
delivered." Add both if they are genuinely missing.

## 4. The browser test is one phone

BUILD_PLAN §2.5 verifies on "your Mac and on your phone's browser." Every later phase
inherits that habit. Nothing tests other engines or the narrow widths the accessibility
requirements assume — SPEC §16.3 requires reflow at 320px, and the only place that gets
checked is the single Step 16.5 audit, at the very end.

**Change:** add a short browser and viewport matrix to BUILD_PLAN — Safari (macOS + iOS),
Chrome, Firefox; widths 320 / 375 / 768 / 1024 — and decide where it lives. Recommend
stating it once in §0 as a standing rule that phase verifications refer to, rather than
repeating a matrix in twenty steps. Keep it proportionate: this is a prototype for
friends, not a compatibility programme.

## 5. The accessibility-overlay ban is stated three times and tested nowhere

SPEC §16.4 bans overlay widgets, ARCHITECTURE §3.8 bans them outright, and BUILD_PLAN
§16.2's zero-foreign-requests check would in practice catch one — but only incidentally,
and only if the founder recognizes the domain.

**Change:** name it in §16.2's instructions. One clause listing the common overlay
vendors by domain so the check is mechanical rather than dependent on recognition.

## 6. The pre-commit hook can be bypassed

BUILD_PLAN §2.4 installs three guards on the law files. Guard 2 is a git pre-commit hook,
which `git commit --no-verify` skips — and an AI coding agent running shell commands can
issue that flag. The guard is real but it is the weakest of the three, and §2.4 presents
the three as equivalent layers.

**Change:** two parts.
- Be honest in §2.4 about what each layer actually stops. The tool deny rules are the
  strong guard (the harness refuses regardless of what the model decides); the hook stops
  accidents, not determination; the tripwire test is the loud one.
- Consider adding a fourth: a GitHub Actions workflow rejecting any push that touches a
  law file without a founder-authored marker. Discuss with the founder first — it adds a
  CI setup step to a project that currently has no CI, and the tool deny rules may already
  be sufficient. Recommend one way or the other rather than listing options.

## 7. SPEC never says profile URLs are not display names

SPEC §4.5 establishes that display names have **no uniqueness requirement**. SPEC §8.1
says names link to profiles. Read together and read alone, SPEC never states what a
profile URL is built from — a builder could reasonably reach for the name and produce
collisions. ARCHITECTURE §4 and BUILD_PLAN Appendix rule 8 both say UUIDs, so nothing is
actually at risk; the gap is that SPEC is meant to stand on its own.

**Change:** one clause in §9.3, which already discusses non-guessable identifiers: profile
and post addresses are built from the account's permanent internal identifier and never
from a display name, which is neither unique nor stable. Note the tension with prompt 08
(SPEC absorbing implementation detail) and keep the wording behavioural, not technical.

## 8. The friends-page filter will be read as search

SPEC §11.6 correctly distinguishes filtering your own ≤300 friends from the global search
§17 forbids, and explains why. But it specifies no label, and a box labelled "Search" on
a friends page is exactly what a user will read as network-wide search — on a platform
whose central promise is that no such thing exists.

**Change:** require the label in §11.6. Something like "Filter your friends" — the point
is that the requirement is stated, not that this exact string is chosen. Placeholder text
too, if the founder wants that level of specificity.

## 9. The backup restore is rehearsed twice and then never again

BUILD_PLAN §5.6 rehearses a restore during setup and §16.4 rehearses it again pre-launch.
After that, nothing. ARCHITECTURE §10's own line is "an untested backup is a rumor" — and
after launch that is exactly what it becomes. The failure mode is specific: backups keep
succeeding, the *restore* path silently rots (a changed schema, an expired credential, a
rotated encryption key), and this is discovered at the worst possible moment.

**Change:** BUILD_PLAN §17.3's operator runbook is a weekly routine that already checks
"the backup job's last-success." Add a periodic restore verification — quarterly is
plausible for a prototype. Decide with the founder between a manual runbook item and an
automated job that restores to a scratch database and runs a smoke query. The automated
version is better and is also a new moving part on a single server; recommend one.

## 10. The shared helpers are single points of correctness

The project deliberately funnels behaviour through one implementation each: the visibility
engine, the name renderer, the time renderer, the alt-text renderer, the theme selector,
the URL validator, the accessible partials. That is the right design, and it means a bug
in any one of them changes behaviour across the whole application at once.

ARCHITECTURE §9 already reflects this for the visibility engine and the time helper — the
time helper's totality test exists precisely because of it. The name, alt-text and theme
helpers get no equivalent treatment.

**Change:** state the principle once in ARCHITECTURE §9 — a helper that is the single
source of a behaviour carries test depth proportional to its blast radius, not to its size
— and check whether the name and theme helpers need a named test the way the time helper
does. This may be a two-sentence addition. Do not manufacture work.

---

## 11. DECISION — the backup window and the deletion promise

ARCHITECTURE §10 resolves the backup-versus-deletion tension the standard way: encrypted
off-server backups, `BACKUP_RETENTION_DAYS` = 30, stated plainly in the privacy policy. It
then says:

> This slightly amends the mental model of §7.5 ("deleted at 90 days" → "deleted from the
> live system at 90 days, gone from the last backup by day 120") — flagged here for
> explicit founder approval since SPEC is authoritative.

**That approval has never been given, and SPEC still says content is simply gone at 90
days.** This is a live inconsistency between the two documents on a user-facing promise,
and it is the kind of promise that matters most if it is ever tested.

**Ask the founder to decide**, then implement:
- **(a) Approve the amendment.** SPEC §7.5 and §15.1 gain the honest version, and README's
  "auto-deleted after 90 days" line is checked for the same precision.
- **(b) Something stricter.** Shorter retention, or per-deletion backup scrubbing. Say
  plainly what each costs — scrubbing backups is real engineering on a solo project.

Recommend (a) with a note on wording: the promise reads better as "deleted at 90 days;
purged from the last encrypted backup within 30 days after that" than as an arithmetic
day-120 figure, because the figure invites a reader to compute an exact date that depends
on when the backup ran.

## 12. DECISION — `COMMENT_LENGTH_MAX` was asserted, never discussed

SPEC's own history records it: "`COMMENT_LENGTH_MAX` = 2,000 asserted, not yet discussed."
It is still marked ✎ operator-tunable in §14 and still 2,000. It is the only constant
carrying an explicit note that nobody ever agreed to it.

2,000 characters is roughly 300 words — a long comment. `POST_LENGTH_MAX` is 10,000, so a
comment can be a fifth of a post. Ask the founder whether that ratio is intended.

Whatever they choose, **remove the "not yet discussed" status**: either the value is
confirmed at 2,000 or it changes. An unresolved marker on a constant that the tripwire
test in BUILD_PLAN §2.4 will assert is a small trap.

---

## Before you finish

- Write the CHANGELOG.md entry for this version: which of the twelve landed, which were
  found already handled, which the founder declined. Declined items keep their reasons —
  README's rule.
- Mark every file's status in the entry, including unchanged ones.
- Update `TODO.md`: prompt 02 status and version.
- If any item turns out to be larger than described here, **stop and split it out** rather
  than growing this session. Add it to TODO.md as a new prompt.
