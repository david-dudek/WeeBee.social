# A7 — Susan, the family historian

Session A7 of the archetype track, and **the pilot**: the first character report written, run
before the other nine prompts exist, so that a format problem is found once instead of ten times.

Run this in a **fresh session** in this repository, on the `archetypes` branch, on **Sonnet 5 at
high effort**. Paste this file from the `---` divider down. It is self-contained: everything you
need is either in it, in `archetypes/BRIEF.md`, or named by exact path.

---

You are writing **one file**: `archetypes/07-susan.md`.

You are imagining that a woman named Susan — one of ten social-media archetypes described for
this exercise — is shown the WeeBee design mockups, has the platform explained to her, is
interviewed about it, and has her likely behaviour predicted. You write that up as a report.

Susan is fictional and the interview is imagined. Nobody is contacted and nothing is published.
Write the report as the record of a session you are imagining, not as though a meeting occurred.

## Step 1 — read `archetypes/BRIEF.md`, in full

**If `archetypes/BRIEF.md` does not exist, stop and say so** — session A0 has not been run, and
nothing in this track can proceed without it. Do not attempt to reconstruct it from `SPEC.md`.

`BRIEF.md` is the shared reference for this whole track. It carries what WeeBee is, the fourteen
facts every character is told, the constants, the absences, a description of every core mockup
page, the verbatim interface strings, the honesty rule, and **the report skeleton you must
follow**. Read all of it before anything else.

**Do not open `SPEC.md` or `ARCHITECTURE.md`.** They are 223 KB and 139 KB and everything you
need from them is already in `BRIEF.md`. **Do not open the fifteen core mockup pages** — §5 of
the brief describes each one precisely so that you do not have to.

## Step 2 — open Susan's three extra pages

These three, and only these, from `mockups/site/`:

| Page | Why Susan is shown it |
|---|---|
| `gallery-manage.html` | The profile gallery, rendered **at its 8-of-8 cap**, showing the honest refusal text a user meets when they try to add a ninth photo. Also the profile-photo controls and the image-description field. |
| `overlay-gallery.html` | What opening one gallery photo looks like: the description shown as a visible caption beneath the image, previous/next, and no caption field of its own. |
| `export.html` | The data export. Its own copy states that the export is **the one place on WeeBee where exact dates and times live**, and that it works whether an account is active, being deleted, or suspended. |

`mockups/site/` is generated and gitignored, so it may be absent. If it is, rebuild it first:

```bash
cd mockups && python3 build.py
```

The mockups are a **static design mockup**, not a working product. Nothing on them saves,
submits or logs in. Where Susan asks what a button would do, answer from the fourteen facts in
`BRIEF.md` §2, not by clicking.

## Step 3 — the character

Susan is archetype 7 of 10. This is her description, verbatim from
`archetypes/Social_Media_Archetypes.md`. Everything you write about her must be consistent with
it, and you may not add biography that contradicts it.

> ### 7. Susan — The Family Historian
>
> Susan is 58, married, works as an elementary-school administrator, and has become the
> unofficial archivist of her entire extended family.
>
> She photographs everything.
>
> Birthdays. Graduations. Christmas dinners. Family reunions. Trips to the beach. Cousins who
> haven't seen each other in twelve years. Dogs wearing Santa hats.
>
> Susan is constantly tagging relatives and creating albums. She remembers exactly who was at a
> particular event and will correct you if you misidentify the year.
>
> Her posts aren't particularly clever, controversial, or entertaining. They are a running
> documentary of family life.
>
> She also loves posting old photographs with captions like, "This popped up in my memories
> today!" followed by a picture of someone who was 30 years younger and several people who are
> now dead.
>
> Susan's relationship with social media is fundamentally archival. She isn't trying to build a
> personal brand. She's building a family history.

Her epigraph, for the line under the report's title:

> *the family historian — the unofficial archivist of an extended family*

**The other nine, for section 6 of the report only.** You have their one-phrase descriptions and
nothing more; that is deliberate, and section 6 is a light prediction rather than an analysis.

1. Joe Blah — the ghost: reads everything, reacts to nothing.
2. Mary Jane — the influencer: presents a version of her life.
3. Grandma Dorothy — the forwarder: sharing as an act of friendship.
4. Jim Roxx — the hobby evangelist: motorcycles and classic rock, nothing else.
5. Karen Commenter — the opinion department: 47-response threads, never quite an insult.
6. Tyler — the aspiring creator: deletes what doesn't get engagement.
7. **Susan — your character.**
8. Dave Crypto — the guy who has it figured out: argues with strangers.
9. Lisa — the perfect-life poster: a scrapbook and a mirror.
10. Mike — the friend collector: 4,800 weak ties.

The ten are a closed cast who are friends with each other on WeeBee.

## Step 4 — how WeeBee is explained to her

Use **all fourteen facts** from `BRIEF.md` §2. Not thirteen. The ones she will like least are the
ones the exercise most needs her to have heard.

**Re-word them in Susan's vocabulary.** She is 58, runs an elementary school office, and is
organised, practical and completely un-technical without being helpless. She thinks in events,
names, years and who-was-there. So:

- Say "your posts get deleted after three months," not "`CONTENT_TTL_DAYS` = 90."
- Say "someone who's friends with one of your friends," not "a friend-of-friend."
- Say "you can send it to thirty people at most," not "`POST_AUDIENCE_MAX`."
- Use her own examples — a reunion, a graduation, Christmas dinner, a cousin she hasn't seen in
  twelve years.
- Never use the words "archetype," "constant," "mechanic," or any SPEC section number in
  anything Susan hears or says. Section numbers may appear in your analysis sections and in the
  findings block, never in dialogue.

**Do not tailor it into a sales pitch.** She is not shown only the parts she would like and is
not spared a fact she would object to. Section 2 of the report records the actual words used, not
a summary of them.

## The honesty rule

This is the rule the whole exercise stands or falls on. It is in `BRIEF.md` §7 and is restated
here verbatim because it is not optional.

> **The honesty rule.** This character has full latitude, including outright rejection. They may
> say they would never sign up; that WeeBee is boring; that they do not understand it; that they
> would join and then quietly stop logging in; that the thing they use social media for does not
> exist here and no amount of explaining changes that. Several of these archetypes are
> structurally impossible on a platform with no public content, no follower counts, no reshare
> and a capped audience — where that is true of your character, say so plainly and do not invent
> a workaround that keeps everyone happy. **A report in which the character politely likes
> WeeBee is a failed report.** Equally, do not manufacture hostility: where a mechanic genuinely
> suits this person, say that too, with the same directness. What is forbidden is the
> comfortable middle — the report that finds something for everyone and commits to nothing.

## The delegation rule

**The delegation rule.** When this character runs into something WeeBee will not hold — sixty
photographs against a gallery of eight, a video, a file, an album — the interviewer must **name
the way out**: keep it wherever they already keep it, and post about it here with the address.
Then ask the second question, and record the answer honestly: **would they actually do that?**

**Two things this rule is not.** It is **not a rescue.** Offering the handoff is not the same as
the character taking it, and this character is entitled to answer *"then what am I here for"* —
**if they do, that is the finding**, and it is worth more to the founder than agreement. The
rule exists so that nobody is asked to judge half a product; it does not exist to talk anyone
round.

And it is **not frictionless.** The way out is still somewhere else to go: the album stays on
whatever service already holds it, and everyone who wants to look leaves WeeBee to do it.
Whether the address in the post is something they tap or something they have to copy by hand
depends on the host — mainstream photo services are the kind WeeBee approves, but which
addresses are on that list is an operator's table this exercise cannot read. So the honest form
of the offer is *"post about the album and give the address, and your family goes and looks"* —
a deliberate step out of WeeBee for every person who wants to see the photographs. Whether that
is good enough for this character is exactly what the interview should find out rather than
assume.

## Step 5 — the probes

These are the questions the interview must cover. They are questions, not answers: **every one of
them is a fair question to put to a woman who might turn out to love the mechanic it is about**,
and you must not write her conclusion for her. If Susan would shrug and say her real photographs
are on a hard drive at home anyway, that is a legitimate finding and you should write it.

**Three are mandatory.** Cover at least three more of the rest, and add your own if the
conversation goes somewhere.

1. **Mandatory.** Ask her what she expects to happen to a post about her mother's eightieth
   birthday ninety-one days after she writes it. Then tell her what actually happens, and ask
   again.
2. **Mandatory.** Tell her about pinning — ten of her own posts, kept indefinitely — and then
   about the part that follows from it: a pinned post keeps her words and her picture, but the
   comments and reactions underneath it still disappear at ninety days, and nothing marks that
   they were ever there. Ask her what she makes of that.
3. **Mandatory.** Ask her how she would establish that a photograph is from 1994, on a platform
   whose screens never show a calendar date or a clock time — only vague relative phrases like
   "a few days ago" and "about a year ago", with a single exception: a countdown in real days to
   a post's deletion. Then show her `export.html` and ask whether that answers it.
4. A family reunion produced sixty photographs. Ask what she does with them here. Then tell her
   the gallery holds eight and a post carries one image, and ask again. Then offer her the way
   out — the album stays wherever she keeps it, and she posts about it here with the address —
   and ask whether she would actually do that.
5. Ask which ten posts she would pin, why those ten, and what she does when she wants an
   eleventh.
6. Ask her how she would tag her cousins in a photograph — and let her find out that she cannot,
   because WeeBee has no way to tag or mention a person at all.
7. Ask what "This popped up in my memories today!" becomes on a platform that has no memories
   feature, and where the notification type it would need is specifically ruled out.
8. Ask whether her grandchildren could see any of this.
9. Ask whether she would use WeeBee alongside whatever she does now, or instead of it — and what
   she would tell the rest of the family it is for.

## Step 6 — write `archetypes/07-susan.md`

**Follow the report skeleton in `BRIEF.md` §8 exactly** — the eight headings, in order, spelled
as given, with the per-section word budgets. Do not add a heading, remove one, or rename one.
Ten reports are only comparable if ten sessions use the same shape.

The title line is `# 07 — Susan`, and the epigraph line beneath it is the one given in Step 3.

Two things to get right, because they are what the founder cannot get any other way:

**The interview must sound like Susan and not like you.** Write her actual sentences. She
digresses. She corrects a detail nobody asked about. She answers a question about software with
a story about a person. She is warm and she is stubborn, and when she does not understand
something she says so rather than nodding. A transcript in which she speaks in tidy, analytical
paragraphs is a transcript of the report's author, and it is the failure this whole exercise is
arranged to avoid.

**Section 5 names constants and numbers.** "She hits the gallery cap in her first afternoon —
eight photographs against sixty from one reunion" is the sentence that is worth something.
"She may find some limits frustrating" is not.

Section 6 is a **light** prediction from the one-phrase descriptions in Step 3 only, and must say
in its own text that it is provisional because session A11 does the real collision analysis with
all ten reports in hand.

`## Possible design findings` takes zero to three bullets, forty words each at most, each naming
the SPEC section it touches. Observational only — never a recommendation, never a decision,
never a change to any document. If you find nothing genuine, write `None.` A manufactured
finding is worse than no finding, because A11 will treat it as real.

## Standing constraints

- **Write exactly one file: `archetypes/07-susan.md`.** Create nothing else.
- **Never append to, edit, or "improve" `BRIEF.md`.** Ten character sessions run in any order; a
  shared file they all write to is a merge conflict waiting to happen. If the brief is wrong or
  incomplete, say so in your findings block and carry on.
- **Do not edit** `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md`,
  `README.md`, anything under `prompts/`, or anything under `mockups/` except the generated
  `mockups/site/` directory the build script writes.
- **Do not read from or write to `00_scratch/`.**
- **No CHANGELOG entry, no TODO row, no version bump.** This is a side exercise on its own branch
  and it changes no versioned document.
- **Do not propose design changes.** You are recording what a person would do, not fixing
  anything.
- **Do not invent.** Every constant, number, page name and interface string must come from
  `BRIEF.md` or from the three pages you opened. If you cannot confirm something, leave it out.

## Before you finish

Check every one of these, in order:

1. `archetypes/07-susan.md` exists and is the **only** file you created or modified, other than
   the generated `mockups/site/` directory.
2. The eight headings match `BRIEF.md` §8 exactly, in order, and the title and epigraph match
   Step 3.
3. Sections 1–7 total 800–1,200 words. If you are over, cut from sections 1, 5 and 6 — **never
   from the interview.** If the report is genuinely better at 1,300 words, say so explicitly when
   you report back rather than trimming something load-bearing; this is the pilot, and the budget
   is one of the things it is testing.
4. All fourteen facts appear, re-worded, in section 2. Count them.
5. The three mandatory probes are all in the interview, and at least three others.
6. No SPEC section number, no constant name, and no word from this prompt's own vocabulary
   ("archetype," "mechanic," "audience cap") appears in anything Susan says.
7. Section 6 says in its own text that it is provisional.
8. The findings block is observational, cites its sections, and contains no recommendation — or
   says `None.`
9. Read the interview once more against the honesty rule. If Susan ends it broadly content, ask
   yourself whether that is what this woman would actually feel about a platform that deletes
   what she says after three months, holds eight photographs, and cannot tag a single relative —
   and if the answer is no, rewrite it.

Then report back to the founder in four or five sentences: the word count, whether the skeleton
fitted Susan or strained anywhere, anything on the three pages that surprised you, and — since
this is the pilot — the one thing you would change about the format before the other nine
sessions copy it.
