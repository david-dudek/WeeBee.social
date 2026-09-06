# Archetype reaction simulation — planning session

> **Run in a fresh session.** Paste everything below the line.
> **Writes:** three files under `archetypes/`. No law file is touched.
> **Model:** run this planning session on **Opus 5**. Every session in the track it plans
> runs on **Sonnet 5 at high effort** — write for that reader.

---

You are working in the WeeBee design-document repository at
`/Users/dudek/Documents/Claude/social network`. WeeBee is a social platform built
deliberately against virality.

## What this session produces

Three files, and nothing else:

1. **`archetypes/PLAN.md`** — the track design: the file list, the report skeleton, what
   goes in the shared brief, the running order, and a usage estimate.
2. **`archetypes/A0-brief.md`** — a self-contained prompt that builds the shared brief.
3. **`archetypes/A7-susan.md`** — one character prompt, written in full, as the pilot and
   the model every later character prompt is copied from.

**Do not simulate any character and do not write any report.** If you find yourself writing
in a character's voice for more than a few lines, you have left the task.

**Do not write the other nine character prompts, and do not write the synthesis prompt.**
They come after the pilot has been run and the format has proved itself — writing ten before
seeing one is how a format problem gets multiplied by ten. `PLAN.md` specifies them; it does
not contain them.

**You are Opus 5; the sessions you are writing for are Sonnet 5.** Write accordingly. Every
prompt you produce must be explicit and self-contained: state the constants rather than saying
"check the spec," name the files rather than saying "the relevant pages," give the section
headings verbatim rather than describing them. Settle here every judgement call you could
settle, instead of leaving it to the executing session. Anything you catch yourself trusting
the reader to infer is something to spell out instead.

Also summarise the plan in your reply so the founder can react without opening the files.

Before writing anything, create a branch off the current `mockups` branch:

```bash
git checkout -b archetypes
```

**No CHANGELOG entry. No TODO.md update.** This is a side exercise on its own branch, not a
design session, and it changes no versioned document. Do not touch `SPEC.md`,
`ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md`, `constants.py`, or anything
under `mockups/`. **Stay out of `00_scratch/` entirely** — do not read from it and do not
write into it. Everything this exercise needs and everything it produces lives in
`archetypes/`.

## The exercise being planned

Ten social-media archetypes are described in `archetypes/Social_Media_Archetypes.md`. In
source order, which is also their session numbering:

| # | Character | In one phrase |
|---|---|---|
| 1 | Joe Blah | the ghost — reads everything, reacts to nothing |
| 2 | Mary Jane | the influencer — presents a version of her life |
| 3 | Grandma Dorothy | the forwarder — sharing as an act of friendship |
| 4 | Jim Roxx | the hobby evangelist — motorcycles and classic rock, nothing else |
| 5 | Karen Commenter | the opinion department — 47-response threads, never quite an insult |
| 6 | Tyler | the aspiring creator — deletes what doesn't get engagement |
| 7 | Susan | the family historian — the unofficial archivist of an extended family |
| 8 | Dave Crypto | the guy who has it figured out — argues with strangers |
| 9 | Lisa | the perfect-life poster — a scrapbook and a mirror |
| 10 | Mike | the friend collector — 4,800 weak ties |

For each, the exercise imagines showing them the WeeBee mockups, explaining how the platform
works in language that person would follow, interviewing them, and predicting how they would
behave — then writes it up.

## The track

Twelve sessions, each run cold, each self-contained. This follows the repository's own rule
that long chats degrade and self-contained prompts are the answer (`prompts/README.md`,
BUILD_PLAN §0.2 rule 4), and it is the same shape as the `prompts/mockups/` track.

| Session | Prompt file | Produces |
|---|---|---|
| A0 | `A0-brief.md` | `archetypes/BRIEF.md` — the shared reference |
| A1–A10 | `A1-joe-blah.md` … `A10-mike.md` | one report each, `01-joe-blah.md` … `10-mike.md` |
| A11 | `A11-synthesis.md` | `SYNTHESIS.md` and `FINDINGS.md` |

A0 runs first. **A1–A10 may then run in any order** — nothing makes one depend on another.
A11 runs last and reads all ten reports.

The split is doing real work: ten cold sessions cannot drift into a house voice the way one
long session does, and a report that comes out flat costs one re-run instead of a redo.

## Decisions already made by the founder

These are settled. Plan around them; do not reopen them.

**1. The shared brief is the load-bearing artifact.** Ten sessions each re-deriving WeeBee
from `SPEC.md` and the mockups would pay that cost ten times. A0 reads the source material
**once** and writes `archetypes/BRIEF.md`, which every later session reads instead. This is
what `mockups/CRIB.md` does for the mockup track. Each character prompt must say plainly:
*read `BRIEF.md`; do not re-read `SPEC.md` or `ARCHITECTURE.md`.*

**2. What each character sees.** A shared **core set** of pages, described in `BRIEF.md` by
A0 so that character sessions need not open them, plus **per-character extras** the session
opens for itself. Proposed core set, to be confirmed against what is actually in
`mockups/site/`: `index.html`, `login.html`, `feed.html`, `composer.html`, `post-feed.html`,
`overlay-post.html`, `profile-about.html`, `profile-blog.html`, `profile-photos.html`,
`profile-pinned.html`, `friends.html`, `friend-request-received.html`, `discover.html`,
`contact-card-received.html`, `settings.html`. Examples of extras — verify each filename
exists before using it:

| Character | Extras |
|---|---|
| Joe Blah | `feed-older.html`, `deactivated.html` |
| Mary Jane | `preview-as-friend.html`, `preview-as-fof.html` |
| Dorothy | `hashtag-suggest.html`, `discover-tag.html` |
| Jim Roxx | `groups.html`, `discover-tag.html` |
| Karen | `report-post.html`, `report-profile.html`, `unfriend-confirm.html` |
| Tyler | `discover-tag.html`, `export.html` |
| Susan | `gallery-manage.html`, `overlay-gallery.html` |
| Dave Crypto | `report-post.html`, `banned.html`, `operator-request.html` |
| Lisa | `post-editor.html`, `preview-as-fof-tagged.html` |
| Mike | `invites.html`, `friend-requests-sent.html`, `introduction-broker.html` |

`mockups/site/` is gitignored and may be absent — rebuild it with `python3 build.py` run
from `mockups/`. A0 rebuilds it; character sessions should expect it to be there.

**3. Honesty.** Full latitude, including outright rejection. A character may say they would
never sign up, find it boring, fail to understand it, or join and then quietly stop logging
in. Several of these archetypes are structurally impossible on a platform with no public
content, no follower counts, and a capped audience — the reports must say so plainly rather
than inventing a workaround that keeps everyone happy. A report in which the character
politely likes WeeBee is a failed report. **This rule goes in `BRIEF.md` and is restated
verbatim in every character prompt.**

**4. Whose reactions.** The ten are a **closed cast** who are friends with each other on
WeeBee. Because the sessions run in any order, an individual report makes only a **light
prediction** of how the other nine would receive this character, reasoned from the archetype
descriptions. The real collision analysis — what Karen's commenting does to Susan's family
albums, what Mike's collecting does against the friend cap — belongs to **A11**, which has
all ten reports in front of it.

**5. Output.** One report per character in `archetypes/`, named `01-joe-blah.md` through
`10-mike.md`, plus `SYNTHESIS.md` and `FINDINGS.md` from A11. The synthesis covers who
WeeBee is genuinely for, who it repels, and — the part worth getting right — which
repulsions are the design working as intended versus which are accidental.

**6. Report format.** A short interview transcript in the character's own voice, then prose
analysis. Target 800–1,200 words. **The section headings live in `BRIEF.md`, not in ten
separate prompts**, so the ten stay comparable; a reasonable starting point is: first contact
with the mockups / how WeeBee was explained to them / interview excerpt / what they like and
dislike / predicted behaviour / likely reception by the other nine / verdict. Settle the
skeleton in `PLAN.md`, and have A0 copy it into `BRIEF.md` verbatim.

**7. Findings.** Reports stay observational. Anything that looks like a genuine design gap is
noted at the foot of that character's report and collected by A11 into `FINDINGS.md` for the
founder to triage. Nothing is routed into the design queue automatically, and no finding may
be presented as a decision.

**8. The pitch.** **One explanation, adapted per person.** A0 writes a single canonical
account of how WeeBee works into `BRIEF.md` — the same facts, the same mechanics, the same
honest description of what the platform will and will not do. Each character session re-words
that one account to match its character's vocabulary and concerns. Dorothy hears it in
plainer terms than Mike does; neither is told about a different product. Tailoring it into a
sales pitch is forbidden: no character is shown only the parts they would like, and none is
spared a mechanic they would object to.

**9. What may be tweaked per character.** Tweak **what they are shown and what they are
asked** — Karen's prompt points at the report and unfriend flows and probes comment threads;
Susan's points at the galleries and asks a hard question about her archive reaching the
expiry horizon. **Never tweak what they conclude.** A prompt that hints Tyler will probably
hate WeeBee has written the answer into the question, and the exercise stops telling the
founder anything. Say this rule in `PLAN.md` so it survives into the nine prompts written
later.

**10. Model.** This planning session runs on **Opus 5**. Every session in the track — A0,
A1–A10 and A11 — runs on **Sonnet 5 at high effort**, for the reasons the mockup track gives
in `prompts/mockups/MODEL-ADVISOR.md`: that work is broad and verification-heavy rather than
architecturally deep. The asymmetry is deliberate. The judgement is spent here, in the
prompts; the track sessions should only have to execute. If you think A11 in particular wants
a different configuration, say so once in `PLAN.md` and then plan for Sonnet 5 as directed.

## What you still have to work out

- **What goes in `BRIEF.md`.** This is the decision the whole track rests on. Specify its
  contents precisely enough that A0 can build it and that a character session needs nothing
  else: how WeeBee works (the canonical account), the constants that bite and what they mean
  in practice, what each core-set page shows, the verbatim interface strings worth quoting,
  the report skeleton, and the honesty rule. Say roughly how long it should be — long enough
  to replace the source documents, short enough that ten sessions can each afford to read it.
- **Which constraints do the work.** Name the specific mechanics these characters collide
  with, cited to their SPEC sections. Candidates include the friend cap, the per-post
  audience maximum, content expiry, the absence of an algorithmic feed, and the absence of
  public content. **Verify every constant against `SPEC.md` or `mockups/CRIB.md` before
  putting it in the plan — do not carry a number over from this prompt on trust.** If one of
  them is wrong here, say so.
- **Budget across twelve sessions.** Estimate what A0, a single character session, and A11
  each cost, and say whether twelve sessions on a Claude Pro plan is realistic or whether
  some should be combined. Be concrete rather than reassuring.

## Standing rules for this session

- **Follow the instruction precisely.** Produce the three files asked for — no more, no less.
  Do not write the nine remaining character prompts, do not expand into design changes, and
  do not add deliverables.
- **Do not fabricate.** Every constant, section reference, file path, page name, and
  interface string must be one you verified by reading the repository. Never invent a SPEC
  section number or a mockup page that does not exist. If you cannot confirm something, leave
  it out or mark it unverified.
- **Ask rather than guess.** If something above is ambiguous or you are missing information
  the founder holds, ask in your reply instead of picking an answer and moving on.
- **Verify before finishing.** Re-read all three files hunting for errors, weak points, and
  edge cases: unverified citations, steps that will blow the budget, instructions a cold
  session could misread, characters the report skeleton does not accommodate. Check
  specifically that `A7-susan.md` can be run by someone who has read nothing but `BRIEF.md`.
- **State uncertainty explicitly.** Mark guesses about the founder's intent, or about how the
  track will go, as guesses. Do not present a judgement call as settled.
- **Work economically.** This runs on a Claude Pro ($20/month) budget. Prefer targeted reads
  over whole files, do not re-read what you have already read, and rebuild the mockups only
  if you need to look at them. Flag up front any step likely to consume significant usage.
