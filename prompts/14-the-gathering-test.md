# Prompt 14 — The gathering test

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** SPEC §1.1 and/or §1.3 (placement is Q1); cross-references from §7.6, §9.1,
> §9.7, §14 if Q3 goes that way. README.md if Q4 goes that way.
> **Depends on:** nothing — it reads three short SPEC sections and needs no other prompt run first.
> **Run BEFORE prompt 13** (`13-delegation-and-link-policy.md`). This material started as
> §4 of that prompt and has been split out; 13's §4 is now a pointer to this file and 13's
> header says to run this one first. The reason is not politeness: **both prompts add a named
> principle to SPEC §1.1/§1.3**, and neither session can see what the other did. This one is
> smaller and settles the structural question — whether a named principle gets its own
> subsection in the shape of §1.2's No-Reach Test, or a §1.3 bullet — so 13 can then match it
> instead of §1 acquiring two named principles in two different shapes.
> **Expected outcome:** one design principle stated, named, placed, and bounded by its own
> exceptions. Possibly nothing else. A session that concludes the analogy is better left
> unwritten is a legitimate outcome.

---

**This is a discussion prompt before it is an editing prompt.** The questions in §4 belong to
the founder. Do not settle them and start editing.

You are working in the WeeBee design-document repository — a small, private, deliberately
anti-viral social network, in design and not yet built. Read SPEC.md §1.1, §1.2 and §1.3
before anything else; they are three short sections and they are most of the context you
need. This is a **founder-directed design session**; you may edit SPEC.md and README.md if
the decisions below call for it.

## 1. The finding, in the founder's words

Asked what guides his judgement about which features belong in WeeBee, the founder described
a mental model that appears nowhere in any of the design documents:

> "When I envision WeeBee, I imagine being at a very large gathering of people, like a party,
> where there's ample space to move about the crowd and gather with small groups of people at
> a time, to have conversations. I think about what might be appropriate interactions in that
> situation. Showing a couple of photos of a vacation, the kids, your car, etc would be.
> Handing someone a stack of photo albums would not. I know that the large party gathering
> analogy doesn't hold everywhere in WeeBee, but I think it should be a guiding principle
> when discussing the features included."

The question this session settles: **does that become a written, named principle in SPEC, and
if so, in what form?**

## 2. Why it is worth writing down

**SPEC already proves the mechanism works.** §1.2 gives the no-reach thesis a named test:

> **The No-Reach Test (apply to every current and future feature):** *Can this feature cause
> content to travel beyond the audience its author deliberately chose, or let a person be
> seen by people with no real social connection to them?* If yes, the feature is wrong for
> this platform.

Named tests get cited. Later sections invoke the No-Reach Test by name and inherit its
reasoning instead of re-deriving it.

**The counter-example is in the same document.** §1.3's "Not a walled garden" bullet is a
real principle — *"Where a need is already well served by open, established channels, WeeBee
delegates rather than rebuilds"* — but it was never named or given a test, so every refusal
that depends on it (no DMs §10.1, no events §17, no video hosting §7.2) argues it again
locally, and it went unstated in README entirely. It was invisible enough that the founder
had to say it out loud in conversation before anyone noticed it was missing. That is the
failure mode this prompt exists to avoid repeating.

**The gathering test is a positive test where the No-Reach Test is a negative one.** The
No-Reach Test can only reject. Nothing in the documents currently helps decide what a feature
*should* look like, only what disqualifies it.

## 3. What it retro-fits, and what it does not

### 3.1 Decisions the analogy accounts for

Verified against SPEC as of v1.27. Constant names are exact.

| Decision | Ref | The analogy's account of it |
|---|---|---|
| No likes, no counters of any kind | §8.2, §17 | Nobody at a party announces how many people enjoyed your story |
| No reshare, repost or quote | §1.2, §17 | You don't carry someone else's conversation to another group |
| `CONTENT_TTL_DAYS` = 90 — everything said expires | §7.5 | Party conversations are not transcribed |
| No DMs; contact card and handoff instead | §10.1 | You step outside to talk privately; you don't build a phone booth in the venue |
| No ads, no tracking | §15.2, §17 | Nobody is handing out flyers |
| `POST_AUDIENCE_MAX` = 30 | §7.3, §14 | The largest group you can actually address at once |
| One image per post; `GALLERY_MAX` = 8 | §7.2, §9.4 | A couple of photos from your wallet, not an album — the founder's own example |
| Invite-only, permanently | §4.1 | It is a private party |
| Hashtag-gated FoF discovery | §11.3 | A host introducing two people who share an interest |
| `FRIEND_CAP` = 300 | §5.1 | The outer bound of people you could plausibly know at one gathering |

Two of these are worth looking at closely, because the analogy does not merely agree with
them — it supplies a **second, independent** justification that the document currently lacks:

- **`GALLERY_MAX` = 8.** §9.4 sets it; §9.7 defends it at line 624 with an anti-accumulation
  argument — *"Expiry exists to prevent accumulation and to refuse to be an archive; a fixed
  eight-slot shelf is neither."* That is a structural argument. The analogy gives the same
  number an intuitive one, and it is the founder's own worked example.
- **The §14 caps generally.** README tells reviewers the caps' *existence* is philosophy but
  their *values* are "honest judgment calls" open to stress-testing. Several of them turn out
  to have a principled account after all. That does not settle the numbers, but it changes
  what a reviewer is arguing against, and §14 or README may want to say so.

**A caution to carry into the writing.** The analogy did not generate these decisions — they
were made first, and it explains them afterwards. Retro-fitting is weak evidence: you notice
the cases an analogy explains and not the ones it is silent about. What the table establishes
is that a real intuition was already operating consistently, which is a good reason to name
it. It is **not** proof the test is correct, and the document should not claim more than that.

### 3.2 Where it breaks — write these in the same breath

The founder has already conceded the analogy does not hold everywhere. Naming where is not a
concession, it is what makes the principle safe to write down: an unbounded analogy in a spec
will be quoted later to argue against something the founder wants.

- **The profile Blog tab** (§9.1) is not party behaviour. Nobody at a gathering maintains a
  standing display of their past remarks for others to browse later. That is a bulletin board
  in the lobby.
- **Pinned posts** (§7.6) likewise, and deliberately. `PIN_LIMIT` = 10, exempt from expiry;
  §7.6 calls pinning *"the deliberate, editorial act of preservation — the only one on the
  platform,"* and README calls it *"the only act of preservation the platform offers."*
- **The contact card's per-item, per-friend visibility cascade** (§10.3) is far more
  deliberate and more granular than anything at a party, though exchanging numbers is
  squarely in the spirit.

**That the analogy breaks precisely where WeeBee has knowingly departed from its own ethic is
itself the argument for writing it down.** It does not only guide new features; it
**identifies the existing exceptions**, and every one it finds is already flagged in the
document as deliberate. A test that independently rediscovers the known exceptions and
invents no new ones is a test worth having.

## 4. The questions

**Q1. Where does it live — §1.1 or §1.3?**

Recommendation: **§1.1**. That section already says *"The measure of success is offline"* and
*"The platform is working when it puts people in the same room."* The gathering analogy is
the **shape** of that claim, and the two read as one thought. §1.3 is a list of one-line
supporting principles and would compress the analogy into a bullet, which is how "not a
walled garden" became invisible.

Counter-argument worth weighing: §1.2's No-Reach Test sits in its own subsection, and a
parallel structure — §1.2 the negative test, a new subsection the positive one — has a
symmetry that would make both easier to cite.

**Q2. What is it called?** "The gathering test" is a placeholder from conversation, not a
decision. It needs a name that survives being cited in a dozen later sections. Offer the
founder two or three and let him pick. The name should not be "the party test" if the
document elsewhere needs to be read by people for whom that reads as frivolous — but it also
should not be so abstract that it stops evoking the picture, because the picture is the whole
value.

**Q3. How binding is it?** This is the most important question in the prompt, and getting it
wrong is the main risk of writing the analogy down at all.

The No-Reach Test is **absolute**: *"If yes, the feature is wrong for this platform."* The
gathering test cannot be, because §3.2 lists three existing features that fail it and stay.

So it has to be written as **a question a feature must answer, not a gate it must pass** —
something closer to *"If a feature would be out of place at that gathering, that is a strong
signal to reconsider it, and the reason for keeping it anyway must be stated"* than to the
No-Reach Test's flat refusal. If the wording does not make that distinction unmistakable, the
test will be quoted as though it were a gate, and the first casualty will be a feature the
founder wants. **Decide the binding strength explicitly and put it in the sentence**, do not
leave it to tone.

**Q4. Does it go in README?** README's "What the project is (60 seconds)" describes WeeBee
almost entirely by negation — a list of twelve absences. The analogy is the shortest possible
positive statement of what the thing *is*, and README is the document the founder actually
hands to reviewers. Recommendation: yes, one sentence. But note that README's "What is NOT up
for review" section then has to be checked — a newly named principle in the philosophy tier is
not open for review, and reviewers should not be invited to argue it.

**Q5. Does anything else cite it once it exists?** A principle nothing references decays. If
it goes in, consider whether §7.6 (pinning), §9.7 (what expires), §14 (the caps table), and
§17 (non-goals) should point at it — particularly §7.6 and §9.7, which are two of the three
named exceptions and currently justify themselves without reference to any principle at all.
Do not scatter references for their own sake; three good ones beat ten.

## 5. Constraints — settled, do not reopen

- **The product philosophy is decided** (README, "What is NOT up for review"): no-virality,
  invite-only, the 90-day expiry, no DMs, the tracking ban, WCAG 2.1 AA conformance. This
  session names an existing intuition. **It does not use the analogy to reopen a decision**,
  in either direction.
- **The three exceptions in §3.2 are deliberate, not defects.** Do not propose removing the
  Blog tab or pinning because they fail the test. The test is being written to describe
  WeeBee, not to prosecute it.
- **The analogy is the founder's, and his words are the source.** Quote or paraphrase his
  formulation rather than composing a better-sounding one; the vacation-photos-versus-stack-
  of-albums example in particular is the part that makes it land.
- **The founder may override any rule or principle.** He has asked that inconsistencies be
  raised every time regardless, until he explicitly states he is overriding one for a
  particular feature. Raise them; do not pre-emptively suppress them.
- **"We looked and it is better left unwritten" is a legitimate outcome.** If the session
  concludes that an analogy in a specification will cause more misreading than it prevents,
  say so and say why. Do not write it in merely because the prompt exists.

## 6. Before you finish

- **Tell prompt 13 what landed.** 13 adds the delegation principle to the same part of SPEC
  §1 and is written to follow whatever structure this session settles. If Q1 and Q3 produce a
  shape 13's §1 should match — a new numbered subsection rather than a §1.3 bullet, say — note
  it in 13's header while it is fresh, rather than leaving that session to infer it. If this
  session concludes the principle is better left unwritten, say so there too: 13 should not be
  left waiting on a decision that has already been made.
- **CHANGELOG.md entry**, and the version bump the change earns. A new named principle in §1
  is not a small edit, even if it is a short one.
- **`TODO.md` updated** — this prompt marked run. Both 13 and 14 are already registered in
  the queue table.
- **Check whether prompt 09 needs to know.** 09 syncs ARCHITECTURE and BUILD_PLAN to the
  current SPEC and has not run. A principle stated in SPEC §1 with no downstream mechanism
  probably needs nothing from 09 — but confirm rather than assume, and say which you did.
- **Splitting is legitimate.** If Q5 turns into a survey of every section that might cite the
  principle, do the naming and placement here and write the cross-referencing as its own
  prompt.
