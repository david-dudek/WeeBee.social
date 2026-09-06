# archetypes/PLAN.md — the track design

Written in the planning session on the `archetypes` branch, against project version 1.27 and
the mockup set as built through M8. This file is the design of the exercise: the file list, the
report skeleton, what goes in the shared brief, the running order, and the budget. It is **not**
a session prompt and nothing in the track reads it except the founder and whoever writes the
nine remaining character prompts.

Every constant, section number, file path and interface string below was verified by reading
`SPEC.md` and `mockups/site/` during the planning session. Anything unverified is marked as
such in place.

---

## 1. Scope, and what this exercise is not

Ten social-media archetypes (`archetypes/Social_Media_Archetypes.md`) are imagined being shown
the WeeBee mockups, having the platform explained to them, being interviewed, and having their
behaviour predicted. Twelve cold sessions produce a shared brief, ten reports, and a synthesis.

This is a **side exercise on its own branch**. It changes no versioned document. It produces no
CHANGELOG entry, no version bump, no TODO row. Nothing it finds is routed into the design queue
automatically, and no finding may be written as a decision. `SPEC.md`, `ARCHITECTURE.md`,
`BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md`, `prompts/` and everything under `mockups/` are
read-only for the entire track. `00_scratch/` is off limits in both directions.

Everything the track produces lives in `archetypes/`.

---

## 2. The twelve sessions

| Session | Prompt file | Produces | Status |
|---|---|---|---|
| A0 | `A0-brief.md` | `archetypes/BRIEF.md` | **written** |
| A1 | `A1-joe-blah.md` | `01-joe-blah.md` | to write, copied from A7 |
| A2 | `A2-mary-jane.md` | `02-mary-jane.md` | to write, copied from A7 |
| A3 | `A3-dorothy.md` | `03-dorothy.md` | to write, copied from A7 |
| A4 | `A4-jim-roxx.md` | `04-jim-roxx.md` | to write, copied from A7 |
| A5 | `A5-karen.md` | `05-karen.md` | to write, copied from A7 |
| A6 | `A6-tyler.md` | `06-tyler.md` | to write, copied from A7 |
| **A7** | **`A7-susan.md`** | **`07-susan.md`** | **written — the pilot** |
| A8 | `A8-dave-crypto.md` | `08-dave-crypto.md` | to write, copied from A7 |
| A9 | `A9-lisa.md` | `09-lisa.md` | to write, copied from A7 |
| A10 | `A10-mike.md` | `10-mike.md` | to write, copied from A7 |
| A11 | `A11-synthesis.md` | `SYNTHESIS.md`, `FINDINGS.md` | to write, after the ten |

Session numbering follows the source order of `Social_Media_Archetypes.md`, which is also the
report numbering. Report filenames are fixed: `01-joe-blah.md`, `02-mary-jane.md`,
`03-dorothy.md`, `04-jim-roxx.md`, `05-karen.md`, `06-tyler.md`, `07-susan.md`,
`08-dave-crypto.md`, `09-lisa.md`, `10-mike.md`.

**Running order.** A0 first — nothing else can run until `BRIEF.md` exists. A1–A10 in any
order, in any combination of sittings; none depends on any other. A11 last, and only once all
ten reports are on disk.

**Why twelve cold sessions rather than one long one.** The repository's own rule
(`prompts/README.md`, BUILD_PLAN §0.2 rule 4): long chats degrade, and self-contained prompts
are the answer. It buys two things specific to this exercise. Ten cold sessions cannot drift
into a single house voice the way one long conversation does — and a house voice is precisely
the failure mode here, since ten characters who all sound alike is the same as no characters at
all. And a report that comes out flat costs one re-run rather than a redo of the set.

**A7 is the pilot.** It is written in full and run first, before the other nine prompts exist.
If the format is wrong, it is wrong once. Whoever writes A1–A6 and A8–A10 copies `A7-susan.md`
structurally, changing only the four things §7 below says may change.

---

## 3. What goes in BRIEF.md

`BRIEF.md` is the load-bearing artifact. Ten sessions re-deriving WeeBee from `SPEC.md` and the
mockups would pay that cost ten times; A0 pays it once. It is to this track what
`mockups/CRIB.md` is to the mockup track, and every character prompt says plainly: **read
`BRIEF.md`; do not open `SPEC.md` or `ARCHITECTURE.md`.**

Nine sections, in this order, with these exact headings:

| § | Heading | Contents | Target |
|---|---|---|---|
| 0 | `## 0. How to use this file` | Who reads it, what they may and may not open, the naming warning (the mockups render an account called David Dudek; the character is not David) | 150 w |
| 1 | `## 1. What WeeBee is, in one paragraph` | The neutral summary, no advocacy | 100 w |
| 2 | `## 2. The canonical account — the fourteen facts every character is told` | The single explanation, verbatim from §4 below | 700 w |
| 3 | `## 3. The constants that bite` | Table: constant, value, SPEC ref, what it means in practice (32 rows) | 650 w |
| 4 | `## 4. What is absent` | Every absence a character could collide with, each marked *forbidden by rule* or *verified absent* | 500 w |
| 5 | `## 5. The core page set — what each page shows` | One short paragraph per core page, written so a session need never open it | 700 w |
| 6 | `## 6. Verbatim interface strings worth quoting` | The strings a character may be quoted reading | 300 w |
| 7 | `## 7. The honesty rule` | Verbatim from §5 below | 130 w |
| 8 | `## 8. The report skeleton` | Verbatim from §6 below, with word budgets | 350 w |
| 9 | `## 9. House rules for a character session` | Write one file; touch nothing else; never append to BRIEF.md; the character is fictional | 200 w |

**Total target: 2,500–4,000 words**, of which roughly 2,000 are blocks A0 copies verbatim from its prompt, so A0's own prose is 1,500–2,000 words. Long enough to replace the source documents; short enough
that ten sessions can each afford to read it. Below 2,500 it stops replacing anything and
sessions will open SPEC.md anyway; above 4,000 it is a tenth read of a long document, which is
the cost this file exists to avoid.

`BRIEF.md` is deliberately **neutral about the ten characters**. It names no archetype and
predicts no reaction. Per-character material lives in the character prompts, never in the
shared brief — otherwise every session reads a steer meant for someone else.

---

## 4. The canonical account — the fourteen facts

One explanation, adapted per person. A0 writes this into `BRIEF.md` §2. Each character session
**re-words all fourteen** in its character's vocabulary and concerns. Dorothy hears plainer
language than Mike does; neither is told about a different product, and neither is spared a
fact they would object to.

Verified against SPEC.md at v1.27. Citations are SPEC unless marked.

1. **You cannot join on your own.** The only way in is a personal invitation from someone
   already on WeeBee, sent by email as a single-use code that expires in 14 days. When you
   accept, you and the person who invited you automatically become friends. You must be 18 or
   over. Everyone holds a few invitations — at most 5 banked, one more every 30 days, and a new
   account starts with 2. (§4.1, §4.2, §4.4)
2. **Nothing on WeeBee is public.** There are no pages a logged-out visitor can see except log
   in, register and invite acceptance. Search engines find nothing. There is no global search
   of people or content anywhere on the platform, and a copied web address shows a stranger
   nothing. (§2, §9.3, §17)
3. **Friendship is mutual, and capped at 300.** Anything that would push either person past 300
   fails with a plain, honest error rather than silently. (§5.1)
4. **There are two ways to post, and you choose every time.** *Send to a few friends* pushes a
   post into the feeds of up to 30 hand-picked friends. *Post to my blog* puts it on your
   profile where all your friends can find it — they get a notification saying you posted,
   never the words themselves. There is no default; a missing choice is an honest error. Every
   post carries a line saying exactly who can see it, and the comment box repeats it. Feed
   posts by the same author are spaced about 10 minutes apart. Your own feed posts also show up
   on your profile's Blog tab, visible to exactly the people you sent them to.
   (§7.1, §7.3, §7.9, §9.1, §12.2, §13.6)
5. **There is no share, reshare, repost, quote or forward button, of any kind.** Nothing can
   travel past the audience its author picked. If you want a friend to see something, you
   retype it yourself. (§1.2, §17)
6. **Nothing is counted.** No likes, no follower counts, no view counts, no post counts, no
   unread badges, no page numbers. Not hidden — they do not exist. (§8.2, §12.2, §17)
7. **Reactions are about six fixed warm phrases** — "Agreed!", "Love it!", "So proud!",
   "Thinking of you", "Congrats!", "Ha!" — and **only the person you reacted to ever sees
   yours.** They see your name and the phrase, never a number, and only on the single-post
   view. Everyone else sees nothing at all, not even that a reaction exists. You cannot react
   to your own post or comment. (§8.2, §8.2.2)
8. **The feed is a mailbox, not a machine.** Strictly newest first: feed posts sent to you, and
   notifications. No ranking, no suggested content, no inserted people, no ads, no infinite
   scroll — older posts are a plain link at the foot of the page, with no page numbers and no
   total. (§7.7, §7.7.1)
9. **Everything you say is deleted after 90 days** — every post, every comment, every reaction,
   permanently, along with any attached image, and out of the last encrypted backup within 30
   days after that. **What you *are* stays**: your profile photo, both bio fields, your gallery,
   your interests, your contact card, your groups and your friend list persist until you change
   them. You may pin up to 10 of your own blog posts to keep them past 90 days; pinning never
   preserves the comments or reactions underneath them, and nothing marks that they existed. A
   post with 14 days or fewer left shows a countdown in real days. (§7.5, §7.6, §9.7)
10. **New people reach you through exactly one mutual friend, and never further.** Only a
    friend-of-friend can send you a friend request; strangers cannot. A request carries no
    written message — just their photo, short bio, the interests you share and the friends you
    have in common. Declines are silent. There is a discover page you must go and visit;
    nothing from it ever appears in your feed. (§5.2, §11.1, §11.4)
11. **Interests are hashtags chosen from a list WeeBee writes**, never typed by you; you may
    carry up to 10 on your profile. Putting one on a blog post is what lets a friend-of-friend
    carrying the same interest see that post — so tagging is an audience decision, not filing.
    There is no way to browse everything tagged with anything. (§11.2, §11.3)
12. **There are no private messages.** Instead you keep a contact card — up to 12 phone numbers,
    email addresses and messenger links — and decide, item by item and friend by friend, who
    sees what. A friend requests it with a button and the system replies with exactly their
    version. The conversation itself happens somewhere else. (§10)
13. **One image per post, and no video or audio at all.** Links only from a list of approved
    sites, and even then as plain clickable links, never embedded players or preview cards. No
    polls. Location data is stripped from every image on upload. Every image asks you to
    describe it in your own words — and in your gallery that description *is* the caption,
    because there is no separate caption field. (§7.2, §7.2.2, §9.4, §16.3)
14. **It is a website, and it is for individual people.** No phone app in version one. No
    business, brand, organisation or bot accounts. There are no ads and no tracking of any
    kind, and mandatory subscriptions are ruled out. (§2, §15.2, §15.3, §15.4, §17)

**Tailoring the pitch into a sales pitch is forbidden.** No character is shown only the parts
they would like, and none is spared a mechanic they would object to. A session that drops fact
5 for Dorothy, fact 6 for Tyler, or fact 9 for Susan has broken the exercise.

---

## 5. The honesty rule

A0 copies this into `BRIEF.md` §7. Every character prompt restates it **verbatim**.

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

The last two sentences are deliberate. The founder's rule guards against politeness; without the
counterweight a cold session reads "a report where they like it is a failure" as an instruction
to be negative, and ten hostile reports tell the founder no more than ten polite ones.

---

## 6. The report skeleton

A0 copies this into `BRIEF.md` §8, verbatim, with the word budgets. Headings are **identical
across all ten reports** and are pronoun-free on purpose, so the set stays comparable and no
heading has to be edited per character.

```
# NN — Name

> *the archetype in one phrase*

## 1. First contact
## 2. How WeeBee was explained
## 3. Interview
## 4. What worked, and what was refused
## 5. Predicted behaviour
## 6. How the other nine would receive this person
## 7. Verdict
## Possible design findings
```

| Section | What goes in it | Words |
|---|---|---|
| 1. First contact | Which pages were put in front of them, in what order, and their unguided reaction *before* anything was explained. Names the extra pages this session opened. | 100–140 |
| 2. How WeeBee was explained | The fourteen facts re-worded in this person's vocabulary — **the actual words used**, not a description of them. All fourteen, including the ones they will hate. Compress freely; drop nothing. | 130–180 |
| 3. Interview | A transcript. `**Interviewer:**` / `**Name:**`, six to ten exchanges. The character's own voice throughout — not the analyst's, not WeeBee's. The longest section. | 250–350 |
| 4. What worked, and what was refused | Two short paragraphs or two short lists. Honest in both directions. | 100–150 |
| 5. Predicted behaviour | Do they sign up? What happens in week one, month one, month six? Which constants do they hit, **named and numbered**. | 130–200 |
| 6. How the other nine would receive this person | A light prediction reasoned from the archetype descriptions only. Marked as provisional in the text — A11 does the real collision analysis with all ten reports in hand. | 70–110 |
| 7. Verdict | One paragraph. Does WeeBee want this person? Does this person want WeeBee? The two answers may differ, and often will. | 50–90 |
| Possible design findings | Zero to three bullets, forty words each at most. Observational only. Each names the SPEC section it touches. Write `None.` rather than manufacture one. | not counted |

**Total for sections 1–7: 800–1,200 words.** Over budget, cut from 1, 5 and 6 first; never from
the interview, which is the section carrying the thing the founder cannot get any other way.

The `> *the archetype in one phrase*` line is the phrase from the founder's own table (for Susan:
*the family historian — the unofficial archivist of an extended family*), so ten reports open the
same way.

**Does the skeleton accommodate all ten?** Checked against each. The one that strains is Joe
Blah: a character who does not participate has thin material for §5, and an interview with
someone who never reacts to anything is a real risk of six shrugs. A1's probes must therefore
work harder than most — ask Joe what he *reads*, what he says out loud in person about what he
read, and whether a platform that cannot tell anyone he was there is better or worse for him
than one that also cannot. That is a note for whoever writes A1, not a change to the skeleton.

---

## 7. What may be tweaked per character, and what may not

**May be tweaked — four things, and only these:**

1. **The character** — name, number, the pasted archetype description, the epigraph.
2. **The extra pages** opened beyond the core set (§8 below).
3. **The probes** — the specific questions the interview must cover.
4. **The vocabulary** in which the fourteen facts are re-worded.

**May never be tweaked: what they conclude.** A prompt that hints Tyler will probably hate
WeeBee has written the answer into the question, and the exercise stops telling the founder
anything. The test is mechanical — read every probe and ask whether it would be a fair question
to put to someone who turned out to love the mechanic it is about.

Worked example, both ways, from A7:

- **Allowed:** *"Ask her what she thinks happens to a post about her mother's eightieth birthday
  ninety-one days after she writes it. Then tell her (fact 9) and ask again."*
- **Forbidden:** *"Susan is an archivist and the 90-day expiry destroys everything she is trying
  to do, so explore how she reacts to losing her archive."* — the conclusion is in the question,
  the session's only remaining job is to agree, and if Susan would in fact have shrugged and
  said her real photos are on a hard drive anyway, the founder will never learn it.

Same rule applies to the pages: pointing Karen at the report and unfriend flows is choosing what
she is shown; telling the session those flows exist *because of people like Karen* is writing her
verdict.

---

## 8. Pages: the core set and the per-character extras

**The mockups.** `mockups/site/` is generated and gitignored, and may be absent. A0 rebuilds it:

```bash
cd mockups && python3 build.py
```

Character sessions expect it to be there. If it is not, they run the same command themselves;
it is stdlib-only and takes under a second.

**The core set — fifteen pages, all verified present in `mockups/site/` during planning.** A0
describes each in `BRIEF.md` §5, so that **no character session ever opens a core page.** That
rule is what makes ten sessions cheap.

`index.html` · `login.html` · `feed.html` · `composer.html` · `post-feed.html` ·
`overlay-post.html` · `profile-about.html` · `profile-blog.html` · `profile-photos.html` ·
`profile-pinned.html` · `friends.html` · `friend-request-received.html` · `discover.html` ·
`contact-card-received.html` · `settings.html`

**Per-character extras.** Each session opens its own, two or three files, at roughly 1,000–4,500
tokens each. Every filename below was verified present in `mockups/site/` during planning.

| # | Character | Extras | Why |
|---|---|---|---|
| 1 | Joe Blah | `feed-older.html`, `deactivated.html` | the only two surfaces a pure reader ever reaches |
| 2 | Mary Jane | `preview-as-friend.html`, `preview-as-fof.html` | she manages an impression; preview-as is the tool for it |
| 3 | Dorothy | `hashtag-suggest.html`, `discover-tag.html` | where a forwarder's instincts meet a curated vocabulary |
| 4 | Jim Roxx | `groups.html`, `discover-tag.html` | the band audience as a group; one interest as a whole world |
| 5 | Karen | `report-post.html`, `report-profile.html`, `unfriend-confirm.html` | the three consequences of a 47-response thread |
| 6 | Tyler | `discover-tag.html`, `export.html` | the nearest thing to reach, and the exit |
| **7** | **Susan** | **`gallery-manage.html`, `overlay-gallery.html`, `export.html`** | the 8-photo cap in its refusal state; the caption-is-alt-text rule; the only place exact dates exist |
| 8 | Dave Crypto | `report-post.html`, `banned.html`, `operator-request.html` | what happens to him, and the one channel he has for arguing with the operator |
| 9 | Lisa | `post-editor.html`, `preview-as-fof-tagged.html` | curation after the fact; the widest audience she can reach |
| 10 | Mike | `invites.html`, `friend-requests-sent.html`, `introduction-broker.html` | every mechanism he would use to collect, and every ceiling on it |

**One addition to the founder's proposed list, flagged rather than made silently:**
`export.html` is added to Susan's extras. Her central collision is the 90-day expiry, and the
export is the only answer the platform has to it — `export.html` states in its own copy that the
export is the one place exact timestamps live, which is also the only answer to a woman who
corrects people about years. Without it the interview has a hard question and no artifact behind
the answer. Extras are not exclusive; Tyler keeps it too.

---

## 9. The constraints that do the work

Every constant verified against `SPEC.md` v1.27 and `mockups/CRIB.md` §1 during planning. This
table is raw material for writing A1–A6 and A8–A10 — **it is not copied into `BRIEF.md`**, which
stays neutral about the ten.

| Character | Mechanics they collide with | SPEC |
|---|---|---|
| 1 Joe Blah | Feed is strictly reverse-chronological with no ranking, no suggested content, no inserted people — there is no algorithm to put anything in front of him; reactions are author-private so his silence is unreadable either way; no view counts or "seen by"; invite-only and no public content mean he cannot lurk without an account and a vouching friend; `INACTIVITY_DELETE_DAYS` = 730 never touches a daily visitor | §7.7, §8.2, §17, §4.1, §2, §4.8 |
| 2 Mary Jane | `POST_AUDIENCE_MAX` = 30 per feed post; `POST_MIN_INTERVAL_MINUTES` ≈ 10 between them; `FRIEND_CAP` = 300 ceiling; no reshare; no counts of any kind; reactions are ~6 fixed phrases only she sees; comments *do* exist and are real feedback; preview-as lets her check exactly what her boss sees; **no way to tag a person** (verified absent) ends "tags people in old photos" | §7.1, §13.6, §5.1, §1.2, §17, §8.2, §8.1, §9.5 |
| 3 Dorothy | No reshare or forward button of any kind — her entire mode of use has no control; the URL allowlist rejects non-approved links **at composition time with an honest error**; only friends-of-friends may send friend requests, so "hundreds of friends she has never met" cannot form; `FRIEND_CAP` = 300; hashtags cannot be free-typed; every image asks for a description she writes (the glare photos); `GALLERY_MAX` = 8 | §1.2, §7.2, §7.2.3, §5.2, §5.1, §11.2, §16.3, §9.4 |
| 4 Jim Roxx | `POST_MIN_INTERVAL_MINUTES` ≈ 10 stops the flyer going up six times in an evening; **no person-tagging** (verified absent) ends "personally tags everyone"; no business or brand accounts, so The Afterburners cannot have a page; no video or audio hosting, and allowlisted media links never embed as players; one image per post; no events system; groups capped at `GROUP_SIZE_MAX` = 30, which is exactly a valid post audience; profile hashtags gating FoF visibility genuinely works in his favour | §13.6, §15.4, §7.2, §17, §6, §11.3 |
| 5 Karen | Comments are flat — no nested replies, so a 47-response thread is a single column; `COMMENT_LENGTH_MAX` = 2,000 and `COMMENT_FOLD_CHARS` = 300; **the post's author can delete any comment on their post** and can never edit one; unfriending and blocking are both silent; report reasons are a fixed list; on a profile post her words are readable by all the author's friends, who may be strangers to her; the whole thread evaporates at 90 days; there is no public content and nothing trending to have an opinion *about* — only what her friends chose to send her | §8.1, §5.3, §5.4, §13.2, §7.5, §7.7 |
| 6 Tyler | **No video or audio at all** — his medium is absent; nothing is counted, so "deletes what doesn't get enough engagement" has no input to run on; no reshare and no virality; no public or logged-out pages, so nothing he makes can reach a non-member; no business accounts and no sponsorship surface; no trending and no global hashtag browsing; `FRIEND_CAP` = 300 is the ceiling on any audience he can ever build; 90-day expiry deletes the portfolio, `PIN_LIMIT` = 10 is the whole exemption; export is the exit | §7.2, §17, §1.2, §2, §15.4, §11.2, §5.1, §7.5, §7.6, §4.9 |
| 7 Susan | `CONTENT_TTL_DAYS` = 90; `PIN_LIMIT` = 10, and **pinning preserves her post but never the comments or reactions on it, with nothing marking that they existed**; `GALLERY_MAX` = 8 with no album concept; one image per post; **no person-tagging** (verified absent); no gallery captions — the description is the caption; **no absolute dates anywhere in the interface** and no date-based archive; **"you have memories!" is named in SPEC as the banned example of an engagement-bait notification**; minimum age 18, so grandchildren cannot be on it; the data export is the one place exact timestamps live | §7.5, §7.6, §9.4, §7.2, §17, §7.5.1, §7.7.1, §12.2, §4.4, §4.9 |
| 8 Dave Crypto | The URL allowlist rejects the basement-video link at composition with an honest error naming the alternative; no reshare; **there are no strangers to argue with** — only FoFs may friend-request, and only people who can see a post may comment on it; no public content, no global search, no global hashtag browsing; discovery stops permanently at one hop, so a community of the like-minded cannot assemble; one image per post caps the screenshot-and-chart habit; the three operator outcomes are defined — delete content, warn by email with no link, or ban, which hides everything reversibly and **hides his words rather than deleting them**; the invite tree records who let him in | §7.2.3, §1.2, §5.2, §8.1, §17, §11.1, §7.2, §13.2.1, §4.3 |
| 9 Lisa | Nothing is counted, so the mirror returns nothing; preview-as is the feature built for exactly her instinct; profile state — photo, both bios, gallery, interests — **does not expire**, which is the half of the platform that suits her; posts do, at 90 days, with 10 pins as the exemption; `GALLERY_MAX` = 8; hashtag-gated FoF visibility is the only route by which a non-friend ever sees anything of hers; a blog post reaches all 300 friends by pull; **no person-tagging** (verified absent) | §17, §9.5, §9.7, §7.5, §7.6, §9.4, §11.3, §7.1 |
| 10 Mike | `FRIEND_CAP` = 300 against 4,800, and an action that would breach it **fails with a clear, honest error, never silently**; only FoFs may request, so the gaming-community contacts cannot be added at all; invites are `INVITE_BANK_MAX` = 5, +1 per 30 days, 2 for a new account; 20 friend requests and 10 introductions a day; an introduction needs **both** parties to accept; no DMs — a contact card instead; the friend list sorts alphabetically and nothing else, with a filter box labelled "Filter your friends"; unfriending is silent, so churn beneath the cap is invisible in both directions | §5.1, §5.2, §4.2, §13.6, §5.5, §10, §11.6, §5.3 |

**One verified absence deserves its own line, because it hits four characters and is not in
SPEC's non-goals list.** Neither `SPEC.md` nor `ARCHITECTURE.md` describes any way to **tag or
mention another person** — in a post, in a photo, or with an @-name. Every use of "tagged" in
SPEC means a *hashtag*. This is stated here as **verified absent, not forbidden**: §17 does not
name it, so it is an absence rather than a refusal, and the honest form for `BRIEF.md` is "the
platform has no such feature." It ends Susan's tagging of relatives, Jim's tagging of everyone
who might attend, Mary Jane's tagging in old photos, and part of Lisa's family posts. Whichever
report reaches it first should put it in its findings block; A11 collects it.

**Nothing in the founder's prompt was found to be wrong.** Every constant carried in it —
`FRIEND_CAP` 300, `POST_AUDIENCE_MAX` 30, `CONTENT_TTL_DAYS` 90, the absence of an algorithmic
feed, the absence of public content — checks out against SPEC §5.1, §7.1, §7.5, §7.7 and §2/§17
respectively, and every mockup filename it names — the fifteen core pages and the twenty extras — exists in `mockups/site/`.

---

## 10. Findings discipline

Reports stay **observational**. A character session notices things; it does not decide anything.

- A genuine design gap goes at the foot of that character's report, under
  `## Possible design findings`, as at most three bullets of at most forty words each, naming the
  SPEC section it touches.
- A session that finds nothing writes `None.` A manufactured finding is worse than no finding,
  because A11 will treat it as real.
- No finding may be phrased as a decision, a recommendation with a preferred option, or a change
  to any document. "The platform has no way to tag a person; §17 does not name this as a
  non-goal" is a finding. "§17 should be amended to name person-tagging" is not.
- A11 collects the ten blocks into `FINDINGS.md`, deduplicated and grouped, for the founder to
  triage. Nothing routes into `TODO.md` automatically.

---

## 11. Model and effort

**Every session in the track — A0, A1–A10 and A11 — runs on Sonnet 5 at high effort**, for the
reason `prompts/mockups/MODEL-ADVISOR.md` gives for the mockup track: these prompts are
exhaustively specified rather than open-ended, so the work is broad and verification-heavy rather
than architecturally deep. The asymmetry is deliberate. The judgement is spent here, in the
prompts; the track sessions should only have to execute.

**One dissent, stated once as instructed, then planned around.** A11 is the one session in the
track that is genuinely synthetic rather than executional. Nine of its ten inputs are prose it
did not write, and its hardest task — separating repulsions that are the design working as
intended from repulsions that are accidental — is a judgement about *intent*, which is not the
kind of question a well-specified prompt can pre-answer. My judgement, and it is a judgement
rather than a measurement: A11 would be better on Opus at high effort. **It is planned for Sonnet
5 at high effort as directed.** The mitigation available inside that constraint is to make
A11-synthesis.md unusually prescriptive about *method* — give it the classification test in
writing, worked on two examples, rather than asking it to invent one.

---

## 12. Budget across twelve sessions

Estimates from measured file sizes, at roughly four characters per token. "Unique input" is what
each session actually reads once; billed input is larger because context accumulates across tool
calls.

| Session | Unique input | Output | Notes |
|---|---|---|---|
| A0 | ~45k tokens | ~5k | 15 core pages (~28k) + `index.html` (~5k) + CRIB §1–2 (~3k) + targeted SPEC reads (~6k) + prompt (~3k). **The heaviest session by a wide margin.** |
| One character | ~16k tokens | ~1.8k | `BRIEF.md` (~4k) + prompt (~2.5k) + 2–3 extra pages (~8k) + pasted archetype (~0.3k) |
| A11 | ~23k tokens | ~5k | `BRIEF.md` (~4k) + ten reports (~16k) + prompt (~3k); two output files |
| **Twelve total** | **~230k unique** | **~30k** | billed input, with accumulation, plausibly 1.3–2.0M |

**Is twelve sessions realistic on Claude Pro?** Yes, and the evidence is in this repository
rather than in an estimate: the eight-session mockup track ran on this plan, and a character
session is materially *smaller* than any of M1–M8 — it reads one 4k brief and two or three small
pages, and writes 1,200 words, where M2 read CRIB.md and SPEC sections and wrote four full HTML
pages. A0 is comparable to a mockup session. A11 is comparable to a mockup session.

**Concrete schedule, rather than reassurance.** Run A0 alone in its own sitting — it is the one
session with a real chance of running long, and everything else is blocked on it. Then two or
three character sessions per sitting; they are independent, so a sitting that only gets through
two costs nothing. Run A11 alone, after all ten reports are on disk. Spread across three or four
days this is comfortable; twelve back-to-back in one day risks the weekly limit, and the failure
mode there is being cut off mid-A11, which is the one session it is annoying to restart.

**Should any be combined? No — with one caveat about where to economise if usage does bite.**
Combining two characters into one session gives back exactly the property the split was bought
for: the second character in a session has already read the first one's report and will
differentiate against it rather than being drawn independently. The saving is also small — two
characters in one session still read both sets of extras, and only `BRIEF.md` and the prompt
preamble are shared, perhaps 6k tokens. If usage genuinely binds, the cheaper cut is **A0's page
descriptions**: dropping `overlay-post.html` and `login.html` from the core set saves A0 real
reading and costs the track almost nothing, since neither page carries a mechanic any character
turns on. Do that before combining characters.

**One step to flag up front:** A0 reads fifteen mockup pages. That is the single largest
consumption in the track and it happens in the first session. It is also the whole point — it is
paid once instead of ten times.

---

## 13. Writing the nine remaining prompts

After A7 has run and `07-susan.md` has been read and judged:

1. Copy `A7-susan.md` to the new filename.
2. Change the four things §7 permits: character block (name, number, pasted description,
   epigraph), extras (§8's table), probes, vocabulary note.
3. Leave everything else byte-identical — the standing rules, the honesty rule (verbatim), the
   pointer to `BRIEF.md` §8 for the skeleton, the "do not open SPEC.md" rule, the file-writing
   rules, and the finish checklist.
4. Do **not** add a section, a heading, or a rule to one prompt and not the others. Ten reports
   are only comparable if ten prompts are the same shape.

A11 is written last and separately; it is not a copy of A7. It reads `BRIEF.md` and the ten
reports, and produces `SYNTHESIS.md` (who WeeBee is genuinely for, who it repels, and which
repulsions are the design working as intended versus which are accidental) and `FINDINGS.md`
(the ten findings blocks, deduplicated and grouped, for triage).

---

## 14. Uncertainties, marked as such

These are my judgements or guesses, not settled facts.

1. **The 800–1,200 word target is tight for eight sections.** The per-section budgets in §6 sum
   to 830–1,220, which fits, but only just. My guess is the first real report will want to run
   long in the interview. A7's checklist tells the session to cut sections 1, 5 and 6 rather than
   the interview; if `07-susan.md` still comes out at 1,400 words and reads well, the honest fix
   is to raise the band to 1,000–1,400 in `BRIEF.md` §8 before the other nine run — a change to
   make once, between the pilot and the rest, not nine times afterwards.
2. **I am guessing at how much interview a cold Sonnet session will produce in one voice.** The
   risk the split is meant to solve is house voice across ten sessions; the risk it does not
   solve is a flat voice *within* one. A7 counters it with an explicit instruction to write
   Susan's actual sentences, including her digressions and her corrections. Whether that is
   enough is the pilot's real test, and is the thing to look for in `07-susan.md` first.
3. **"Verified absent" is doing real work and could be wrong in one direction.** I searched
   `SPEC.md` and `ARCHITECTURE.md` for person-tagging and @-mentions and found nothing. That is
   evidence of absence from those two documents; it is not proof the founder never intended the
   feature. `BRIEF.md` states it as "the platform has no such feature," which is true of the
   documents as written, and the reports will surface it as a finding for exactly this reason.
4. **I have not read every core page in full**, only enough of each to confirm it exists, what it
   is titled, and what it renders. A0 reads them properly and writes the descriptions; if one of
   them turns out to show something `BRIEF.md` §5 cannot summarise honestly, A0 says so in the
   description rather than smoothing it over.
