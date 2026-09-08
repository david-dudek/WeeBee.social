# Prompt 13 — The delegation principle and the link policy

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** SPEC new §1.5 + §1.3, §7.2, §7.2.3, §7.8, §9.4, §10.2, §4.6.1, §13.1, §14, §17;
> README.md; ARCHITECTURE §4, §7; BUILD_PLAN Steps 6.2a, 6.6, 8.1, 9.1, 13.3, 16.1.
> **Depends on:** 01. **Run BEFORE prompt 09** — 09 syncs ARCHITECTURE and BUILD_PLAN to the
> current SPEC, and this prompt changes SPEC in several places 09 would otherwise have to
> carry twice.
> **Prompt 14 has run (landed 1.28). The structural question is settled — here is the answer,
> so this session does not have to re-derive it.** Both prompts add a named principle to SPEC §1;
> 14 went first for exactly this reason.
>
> - **A named principle gets its own numbered subsection**, in the shape of §1.2's No-Reach Test —
>   not a §1.3 bullet. 14's own reasoning for rejecting the bullet is the evidence already in the
>   document: "not a walled garden" *is* a §1.3 bullet, and being one is why it went invisible.
>   **That bullet is the thing this prompt exists to fix, so do not fix it by leaving it a bullet.**
> - **Take §1.5.** §1.4 is the Gathering Test. §1.3 (Supporting principles) was deliberately *not*
>   renumbered — doing so would have rewritten 17 live citations in SPEC, 2 in BUILD_PLAN and 5 in
>   TODO, and broken six CHANGELOG entries. Do not renumber it now either; append at §1.5.
> - **Match §1.4's form:** a short statement of the principle, then its binding strength stated
>   **in the sentence rather than left to tone**, then the places it does not hold, named. §1.4 is
>   a question a feature must answer, carrying a duty to write down the reason for any exception;
>   §1.2 is a flat gate. **Decide explicitly which of those two the delegation principle is** — it
>   may well be the gate, since unlike the gathering analogy it has no standing exceptions — and
>   say so in the text. Two named principles in two shapes is fine when the shapes are *chosen*.
> - **§1.3's "not a walled garden" bullet must not be left standing as a duplicate** of whatever
>   §1.5 says. Replace it with a one-line pointer, or delete it and let §1.5 carry it.
> - **README:** 14 added a positive-statement paragraph to "What the project is (60 seconds)" and
>   a clause to "What is NOT up for review" that names the new principle while stating explicitly
>   that it closes none of the caps. Follow that pattern rather than inventing a second one.
>
> **Read §1.1, §1.3 and the new §1.4 as they now stand before editing.**
> **Expected outcome:** one design principle written down and named; the URL policy rewritten
> around it; three downstream reconciliations made honestly; README given the paragraph it
> is missing.

---

**This is a discussion prompt before it is an editing prompt.** Two decisions in §5 below are
genuinely open and belong to the founder. Do not settle them yourself and start editing. Put
them to the founder, take the answers, then write.

You are working in the WeeBee design-document repository. Read `README.md`, then SPEC.md
§1.1, §1.3, §4.6.1, §7.2, §7.2.3, §7.8, §9.4, §10.1–10.3, §13.1, §17. Skim ARCHITECTURE.md
§4 (the `url_allowlist` table) and §7 (link validation). This is a **founder-directed design
session**; you may edit SPEC.md, README.md, and ARCHITECTURE.md / BUILD_PLAN.md where the
decisions below require it.

## Why this prompt exists

The founder stated a design principle that has governed WeeBee from the start but was never
written down as a principle:

> "One of the design principles that I used when coming up with WeeBee is that I didn't want
> it to try to add features that are better implemented elsewhere. WeeBee is meant to be used
> in concert with other services like texting, email, Google Maps, Evite, DropBox, etc.
> Instead, links to other services that are approved can go on posts, and any other link can
> go on contact cards."

Two things came out of checking that against the documents. First, the principle **is** in
SPEC, but only ever as the local justification for individual refusals — never once as a
named rule that later sections cite, and not at all in README.md. Second, **the last sentence
of it is not true of the documents as written** (§3 below).

The same conversation produced a second, larger idea — the founder's mental model of what
WeeBee is — which was also written down nowhere. **That has become its own prompt** and is not
this session's work; see §4.

## 1. What is already in the documents

Do not rewrite these from scratch. The substance is good; what is missing is a name and a
home.

- **SPEC §1.3, the "Not a walled garden" bullet** — *"Where a need is already well served by
  open, established channels — person-to-person messaging above all (§10.1) — WeeBee
  delegates rather than rebuilds, and makes the handoff cleanly. It aims to be one useful
  tool among many, never the place a user cannot leave."* This is the principle. Its only
  example is messaging, so it reads as a footnote to the no-DMs decision.
- **SPEC §10.1** has the best prose on it: *"A platform that rebuilds messaging is not adding
  a capability — it is trying to own a relationship it did not create."*
- **SPEC §7.2.3** — the allowlist "states what the platform is for," with three admitting
  categories: convening / hosting-what-WeeBee-cannot-host / messenger handoff.
- **SPEC §17** — *"no events system (delegated to allowlisted external services)."*

**The contrast to draw:** §1.2 gives no-reach a **named test** — the No-Reach Test, stated
once and applied to every current and future feature. Delegation has no equivalent, so every
refusal re-argues it locally. That asymmetry is why the principle was invisible enough to go
unwritten in README.

**README.md has none of it.** The "What the project is (60 seconds)" section describes WeeBee
almost entirely by negation — a list of twelve absences. Nothing tells a reader those
absences are deliberate delegation to services that already do those jobs well. README is the
document the founder hands to reviewers, so this is the gap that costs the most.

## 2. What the founder has decided

Settled in conversation. Implement these; do not reopen them.

**2.1 One uniform link rule across every surface.**

| Link | Renders as |
|---|---|
| Approved service | clickable hyperlink |
| Anything else | **plain text — see decision Q1** |
| Blocklisted domain | refused; the post cannot publish |

This replaces the current arrangement, where a non-allowlisted URL is **rejected at
composition time**. Under the new rule the allowlist governs **clickability**, not delivery.
Note what that costs, and be honest about it in §6.

**2.2 The rule is the same on posts, comments and contact cards.** SPEC §7.2 already governs
posts and comments together, so comments follow automatically. Contact cards need §10.2
extended (see §3). The founder has left open the option of marking *some* services clickable
**only** on cards — see Q3, which is optional and can be deferred.

**2.3 Photo hosting joins the allowlist categories.** The founder's rationale, which is
better than the "does not host at scale" framing and should survive into the document:

> "I think we could add photo hosting because what we can offer for that is meager. Even
> though there are better photo hosting services, we still have to provide what we do,
> because this will never get off the ground if users can't even post one photo."

So: WeeBee hosts photographs as a **courtesy minimum, not as a photo service** — one per
post, eight in a gallery (`GALLERY_MAX`), enough that the platform works without an outside
account, never enough to be anyone's photo library. §7.2.3's category 2 is currently scoped
as *"Hosting what WeeBee **cannot** host"* and justified with *"WeeBee hosts no video or
audio"* — which excludes photo hosts by its own logic, since WeeBee does host images. Rewrite
the category so it covers both cases honestly.

This also gives the composer copy almost verbatim: *"WeeBee holds one photo per post. If you
have sixty, they live somewhere else — link to them here."*

**2.4 A domain blocklist exists.** The founder has asked for **the mechanism, not a debate
about its contents** — do not spend the session litigating what belongs on it. Specify:

- A second operator-maintained table alongside `url_allowlist` (ARCHITECTURE §4 already
  establishes the pattern, including the "deactivating beats deleting" discipline and the
  `NAME_BLOCKLIST` precedent at SPEC §4.5).
- Checked by the **same shared validator** as the allowlist, on **every save path, create and
  edit alike** — SPEC §7.8 invariant 4, ARCHITECTURE §7, BUILD_PLAN Steps 6.2a and 6.6. The
  founder specifically called out the edit interface; §7.8 already calls a create-only
  validator "a defective implementation," and this is the second control to depend on it.
- **The author is warned before the post is published**, not after.

One copy question that is *not* litigation of contents and does need answering: §16.3
requires an error to state its fix, and the honest fix for a blocklisted link is "remove it,"
not an appeal. §13.5's operator request channel exists for *adding* to the allowlist;
whether it also accepts *removal* from the blocklist is a real question — decide it and say
so, rather than writing copy that implies a door that isn't there.

**2.5 Three outcomes, and only one of them is an error.** Approved → clickable. Not approved
→ plain text; **this must not read as a rejection.** No warning, no apology, no error
styling — it is a different rendering, not a refusal. If it feels like a scolding, users
experience the whole platform as scolding them. Blocklisted → the only actual error.

## 3. The founder's principle is not true of the documents — fix it

> "...and any other link can go on contact cards."

**SPEC §10.2 does not permit this.** Card items are phone numbers, email addresses, and
*"messenger links (links only from the allowlisted official domains of recognized
messengers)."* An arbitrary URL is not a permitted card item.

Worse, §7.2.3's **rejection message already promises otherwise**: it tells a user that
"anything else can be shared through the contact methods on the user's contact card." That
sentence means *once you are on that channel nothing is restricted* — but it reads as *put
it on your card*, and BUILD_PLAN Step 6.2a bakes the same wording into the composer.

Consequence, worth stating plainly to the founder if it comes up: **today there is nowhere
durable in WeeBee to put "here is my photo album."** Not the card (messenger domains only),
not the short bio (renders no links at all, §9.4), not the extended bio or a pinned post
(allowlisted domains only).

Extend §10.2 so cards may carry non-messenger links under the §2.1 rule. Then:

- **A label field per item**, so a URL is not a naked address. This is new free text and the
  spec is rightly hostile to that, so give it the short-bio treatment: a length cap named in
  §14, and `NAME_BLOCKLIST` screening at every save.
- **A report path.** This is the real gap, not a footnote. Report actions exist on posts,
  comments and profiles (§13.2); a contact card is **not a reportable object**. The operator
  queue works from a frozen copy of the target, and a card is per-requester (§10.3), so the
  operator needs *the card the reporter actually received*, not the owner's current one.
  Compare §5.2's snapshot rule, which solved the same shape of problem for friend-request
  cards. **If this turns out to be more than a section's worth of work, it is a legitimate
  outcome to gate card links to v1.1 and say so** — see Q4.

## 4. The gathering test — moved to prompt 14

The founder's mental model of WeeBee — the large-gathering analogy he uses to judge whether a
feature belongs — came out of the same conversation as everything else in this prompt, and was
carried here in an early draft. **It is now `prompts/14-the-gathering-test.md`, to be discussed
on its own.** Nothing in this prompt depends on it, and this session should not write it.

**14 has now run and landed in 1.28**, as **SPEC §1.4 — the Gathering Test**. The structure it
settled is in this prompt's header: a named principle takes its own numbered subsection, this one
takes **§1.5**, §1.3 is not renumbered, and the binding strength goes in the sentence. Read §1.4
before writing §1.5 — not to copy its argument, but so the two read as a pair rather than as two
sessions that could not see each other.

## 5. The open decisions — put these to the founder first

**Q1. Plain text, or a one-click copy box?** The founder is undecided. This is the only part
of the mechanism still open, and everything else in §2 holds either way.

The copy box is the pattern where a text box carries a small copy-to-clipboard icon in the
corner. What is already established about the trade:

- **As an anti-phishing control the copy box is the better of the two**, and better than the
  warning banner that was considered and dropped. A warning is advisory; this is structural.
  It shows the raw URL, so the destination is disclosed by construction and the link text
  cannot lie about where it goes — which is most of what makes a deceptive link work. And it
  breaks the one-tap reflex without depending on anyone reading anything.
- **But the copy button is a friction *reducer*.** Plain text with no button costs a fiddly
  select-and-drag or retyping thirty characters; the button takes it back to one click plus a
  paste. Still meaningfully more than a hyperlink — no accidental clicks, no one-tap
  phishing, and on a phone the app-switch is genuinely annoying — but less than "plain text"
  sounds. The founder's stated purpose for the friction is *"enough friction to prevent WeeBee
  devolving into link sharing,"* and the copy box is the weaker of the two against exactly
  that.
- **Honest limitation, either way:** a platform with no counters cannot measure whether a
  content-shape control is working. There is no metric that would tell the founder in three
  years whether feeds have drifted — only his own reading and the report queue. That is the
  design working as intended, not a flaw, but it means this decision cannot be revisited on
  evidence later. Say so once, in the document, where the choice is recorded.
- **Accessibility differs between the two options** and is real §16 work, not a detail. A copy
  control needs an accessible name, keyboard operability, and a live-region confirmation that
  the copy happened. Both options put a bare URL on the page, and **URLs do not wrap** — a
  long one is a 320px reflow risk under §16.3. SPEC §7.2.1 already fought this battle once
  over preformatted posts and that is the platform's *single* documented reflow exception;
  a second one arriving by accident would be a bad trade. Solve it (break-anywhere wrapping in
  a scrollable container, or truncation with the full URL still copyable) rather than
  inheriting it.

**Q2. Moved to prompt 14** — where the gathering test lives and what it is called. Not a
question for this session. See §4.

**Q3 (optional, deferrable).** The founder raised marking some services clickable **only** on
contact cards. A test that decides it cleanly, offered but not adopted: *a link that
identifies a **person** belongs on the card; a link that identifies a **thing** belongs in a
post.* A WhatsApp handle is you; a Maps pin for a restaurant is a thing. That already
describes §7.2.3's messenger category without changing it, and it gives a principled answer
for the awkward future cases (payment handles, scheduling links). **Nothing else in this
prompt depends on Q3** — if the session is running long, park it.

**Q4.** Does the card-report path of §3 get built for v1, or does it gate card links to v1.1?

## 6. Three reconciliations this forces — do not skip these

The founder's standing instruction is that inconsistencies get raised every time, until he
explicitly says he is overriding a rule for a particular feature. These three are consequences
of §2.1 and each needs an honest edit, not a paper-over.

**6.1 §4.6.1's anti-phishing claim.** It currently lists *"a URL allowlist on every post and
comment"* as one of four controls closing the in-platform link-delivery vector. Under the new
rule the allowlist no longer blocks delivery — **any URL can now be delivered in-platform**,
just not as a hyperlink. Still a real reduction, but the claim has to become something like
*no way to deliver a **clickable** deceptive link, and no unsolicited delivery at all*.
**§13.1's structural-defence list carries the same sentence and needs the same edit.**

**6.2 §9.4's short bio now contradicts its own stated reasoning.** The short bio *rejects*
disallowed URLs at save, and v1.16 changed it from inert-rendering **specifically because**
*"an unclickable address is still readable and retypeable"* (§13.1). That is a general claim.
If it is true for the bio it is true for a post, so under the new rule the two rules
contradict each other's justification.

The *outcome* is defensible and should not change — the short bio is a **push** surface,
delivered to people who never asked, up to 20 requests a day (§13.6); a post is not. What has
to change is the **reason given**: from "inert is not enough" to "this surface is pushed at
people who did not ask for it, so it gets the stricter rule." Leave the old reasoning in place
and a careful reader finds the contradiction — which is precisely what README asks reviewers
to hunt for.

**6.3 Does expiry become decorative?** The sharpest fair challenge to the new policy: if the
durable record lives elsewhere and WeeBee only holds the pointer, what is the 90-day promise
worth? The answer is available and consistent — the promise is about what **the platform**
retains and could be compelled to produce, never about what users choose to keep, which is the
same posture §1.2 takes on screenshots and off-platform re-propagation. Answer it in one
sentence in §7.5 or §9.7 rather than leaving it to be discovered.

## 7. Downstream — already located, so you don't have to hunt

- **ARCHITECTURE §4** — `url_allowlist` is a table with host, admitting category, and
  redirector-rejection patterns. The **category list is enumerated there** (convening /
  hosts-what-we-cannot-host / messenger handoff) and changes with §2.3. A blocklist table
  joins it, and §4's "operator-curated sets are tables, not constants" paragraph should name it.
- **ARCHITECTURE §7** — the link validator. Currently specified to *refuse* non-allowlisted
  URLs; becomes a **classifier** returning clickable / plain / refused. The host-matching and
  redirector rules are unchanged and still load-bearing.
- **BUILD_PLAN Step 6.2a** — the shared validator and its attack-case tests. The ✅ block
  asserts refusals that will no longer be refusals; the tests need rewriting to assert
  *rendering*, and new cases for the blocklist. Also carries the rejection copy from §7.2.3.
- **BUILD_PLAN Steps 6.6 and 16.1** — the edit-path validation and its re-verification. Both
  name the create-only defect explicitly; the blocklist inherits the same requirement.
- **BUILD_PLAN Step 8.1** — the ✅ block asserts *"paste a URL into the short bio → renders as
  plain text with no link."* Check this still says what §6.2 decides it should.
- **BUILD_PLAN Step 9.1** — the card, currently *"≤12 items (phone/email/messenger-link from
  allowlisted domains)"*. Changes with §3, including the label field.
- **BUILD_PLAN Step 13.3** — the admin allowlist editor, with rows created inactive by
  default. The blocklist editor belongs here.
- **SPEC §14** — a new constant for the card-item label cap; the blocklist joins the
  operator-curated ✎ rows.
- **SPEC §17** — the non-goals list currently reads as though non-allowlisted links are
  refused. Check the whole paragraph.

## 8. Constraints — settled, do not reopen

- **The product philosophy is decided** (README, "What is NOT up for review"). No-virality,
  invite-only, the 90-day expiry, no DMs, the tracking ban, WCAG 2.1 AA.
- **Off-platform re-propagation stays out of scope.** Screenshots, retyping, chain letters —
  §1.2 and §17 already concede these honestly and the founder reaffirmed it. Note the
  distinction that matters here, though: screenshots are **outbound leakage**, unpreventable
  and correctly conceded; link policy is **inbound content shape**, entirely within the
  platform's control. Conceding the first does not license loosening the second, and "we
  can't solve every problem on the internet" is not an argument for the link change.
- **Discussing outside content is legitimate.** §7.2.3 already says so — *"Sharing something
  you did not make in order to talk about it with people you know is ordinary friendship and
  long predates the internet."* Do not re-argue that the feed will fill with news links; the
  founder has weighed it and the document already agreed with him.
- **The founder may override any rule or principle.** He has asked that inconsistencies be
  raised every time regardless, until he explicitly states he is overriding one for a
  particular feature. Raise them; do not pre-emptively suppress them, and do not re-raise one
  he has already overridden.

## 9. The archetype track — a consequence, but a separate session

Do not do this work here; it belongs on the `archetypes` branch and after the decisions above.
Recorded so it is not lost.

The archetype interview track (`archetypes/`) tells every character *"Links only from a list
of approved sites"* and never mentions the door out — that the intended answer to a hosting
limit is to host it elsewhere and link or announce it here. The wording originates in
`archetypes/PLAN.md` §4 fact 13 and is copied into `archetypes/BRIEF.md` §2, so **every
character inherits the blind spot**, not just the one where it was noticed.

It surfaced in `archetypes/07-susan.md` (the family historian): she hits `GALLERY_MAX` = 8
against sixty reunion photographs, and the interviewer never once suggests hosting them
elsewhere and posting about it. Her verdict — that WeeBee cannot use an archivist — may be
right, but it was reached without her being told the whole product.

Only the pilot has run. **Nine character prompts and the synthesis are unwritten**, and
`PLAN.md` §13 says they are copies of `A7-susan.md`, so this is the cheapest moment it will
ever be to fix. When that session runs, it should: restate fact 13 in PLAN.md and BRIEF.md
with both halves; add an interview-conduct rule to A7 (which then copies into the other nine)
that when a character hits a hosting wall the interviewer **offers** the delegation answer and
records the reaction; and guard it against becoming a rescue — `archetypes/PROMPT.md` rule 9
forbids writing a character's conclusion, so the rule must be *offer it, then ask whether
they would actually do it*. Susan is entitled to answer "then what am I here for," and if she
does, that is the finding. Then re-run A7.

**Do not re-run A7 before the decisions in §5 are made**, or the re-run teaches Susan a rule
that does not exist.

## Before you finish

- CHANGELOG.md entry, and the version bump the change earns.
- `TODO.md` updated — this prompt marked run, and the archetype follow-on recorded wherever
  the queue keeps work that is not a numbered prompt.
- **Check prompt 09's scope.** It syncs ARCHITECTURE and BUILD_PLAN to SPEC and has not run.
  Either fold §7's downstream items into 09's list, or do them here and say in 09 that they
  are done — but do not leave them for 09 to rediscover.
- **Splitting is legitimate.** If the card-report path (§3) or the accessibility work behind
  Q1 turns out to be a section's worth of design on its own, write it as **prompt 15** — 14 is
  taken — rather than finishing it badly. Say which parts you split and why.
