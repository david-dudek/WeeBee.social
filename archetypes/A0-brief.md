# A0 — build the shared brief

Session A0 of the archetype track. Run this in a **fresh session** in this repository, on the
`archetypes` branch, on **Sonnet 5 at high effort**. Paste this file from the `---` divider
down. It is self-contained: everything you need is either in it or named by exact path.

Nothing else in the track can run until this session finishes.

---

You are writing **one file**: `archetypes/BRIEF.md`.

`BRIEF.md` is the shared reference for eleven later sessions. Each of those sessions imagines
showing one of ten social-media archetypes the WeeBee mockups, explaining the platform to them,
interviewing them, and predicting how they would behave. Without `BRIEF.md` every one of those
sessions would re-derive WeeBee from `SPEC.md` and forty mockup pages, paying that cost eleven
times. You pay it once. This is exactly what `mockups/CRIB.md` does for the mockup track.

Write it so that **a later session needs nothing but `BRIEF.md`** to understand what WeeBee is,
what its screens look like, and what shape of report to produce.

## Standing constraints

- **Write exactly one file: `archetypes/BRIEF.md`.** Create nothing else.
- **Do not edit** `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md`,
  `README.md`, anything under `prompts/`, or anything under `mockups/` except the generated
  `mockups/site/` directory that the build script writes (it is gitignored generated output;
  running the build is expected).
- **Do not read from or write to `00_scratch/`** at all.
- **No CHANGELOG entry, no TODO row, no version bump.** This is a side exercise on its own
  branch and it changes no versioned document.
- **Do not write a report, and do not simulate any character.** That is what the eleven later
  sessions are for. If you find yourself writing in someone's voice, you have left the task.
- **Do not invent.** Every constant, section reference, filename and interface string in
  `BRIEF.md` must be one you read. If you cannot confirm something, leave it out or mark it
  unverified in place.

## Step 1 — rebuild the mockups

`mockups/site/` is generated and gitignored, so it may be absent. Rebuild it:

```bash
cd mockups && python3 build.py
```

Then confirm the fifteen core pages exist:

```bash
ls mockups/site/
```

The fifteen are: `index.html`, `login.html`, `feed.html`, `composer.html`, `post-feed.html`,
`overlay-post.html`, `profile-about.html`, `profile-blog.html`, `profile-photos.html`,
`profile-pinned.html`, `friends.html`, `friend-request-received.html`, `discover.html`,
`contact-card-received.html`, `settings.html`.

All fifteen were present when this prompt was written. If one is missing, say so in
`BRIEF.md` §5 in place of that page's description rather than describing it from its filename.

## Step 2 — read, and read only this

Read these, and nothing else. In particular **do not read `SPEC.md` or `ARCHITECTURE.md` end to
end** — the sections you need are already quoted into this prompt, and the two documents are
223 KB and 139 KB.

1. **The fifteen core pages** in `mockups/site/`, in full. They are 4–19 KB each. These are what
   you are describing in `BRIEF.md` §5, and you cannot describe them without opening them.
   `index.html` is a map of the whole mockup set and is worth reading first.
2. **`mockups/CRIB.md` §2**, "Verbatim interface strings" (roughly lines 66–265). This is the
   source for `BRIEF.md` §6. Do not re-read §1; its constants are already transcribed into this
   prompt in Step 3.
3. **`SPEC.md` §1.1–§1.3** (lines 10–38) and **§17** (lines 1122–1128), for the mission and the
   non-goals list, if you want the primary text behind §2 and §4 of the brief. Optional — both
   are already summarised below.

**Note on reading the pages.** Every mockup page carries two kinds of sentence: *simulated
content* — what WeeBee would actually say to a user — and *commentary*, build notes to the
founder wrapped in a `.commentary` class, full of SPEC citations. When you describe a page in
`BRIEF.md` §5, describe **what a user would see**, and treat the commentary as your own
reference, not as part of the page. The pages also render a sample account belonging to **David
Dudek**, with friends **Alice, Tom, Mom** and a friend-of-friend **Priya**; a name-changed
display shows as "David Dudek (formerly Dave Dudek)". None of these people is one of the ten
archetypes. Say this explicitly in `BRIEF.md` §0 — a later session that thinks its character is
David will write a broken report.

## Step 3 — write `archetypes/BRIEF.md`

Nine sections, in this order, with **these exact headings**. Target **2,500–4,000 words total** —
of which roughly 2,000 words are blocks you copy verbatim from this prompt, so your own prose is
1,500–2,000 words. Do not pad to reach the number.
Below 2,500 it stops replacing the source documents and later sessions will open `SPEC.md`
anyway; above 4,000 it becomes the tenth read of a long document, which is the cost it exists to
prevent.

### `# BRIEF.md — shared reference for the archetype track`

Open with two or three lines of your own: what this file is, that it was built in session A0,
and that it is written against project version 1.27 and the mockup set as built through M8.

### `## 0. How to use this file`

*(~150 words, your own words.)* Who reads this (sessions A1–A10, each writing one character
report, and A11, writing the synthesis). What they may open: this file, the character prompt they
were given, and the two or three extra mockup pages that prompt names. What they may **not**
open: `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, or any core page described in §5 — the
descriptions there exist so nobody has to. And the naming warning from Step 2: the mockups render
David Dudek's account; no character in this exercise is David.

### `## 1. What WeeBee is, in one paragraph`

*(~100 words, your own words.)* A neutral summary. Not advocacy, not a pitch — the paragraph you
would write if you had no stake in whether anyone joined.

### `## 2. The canonical account — the fourteen facts every character is told`

*(~700 words.)* **Copy the fourteen facts below verbatim.** Introduce them with two lines of
your own saying what they are for: one explanation, adapted per person; every character session
re-words **all fourteen** in its character's vocabulary; the same facts reach everyone, and
nobody is spared a mechanic they would object to. Add one line noting that the parenthetical
section numbers are for a session's own reference and never appear in a report's spoken
dialogue, though a report may cite them in its analysis sections and findings.

Then, verbatim:

> 1. **You cannot join on your own.** The only way in is a personal invitation from someone
>    already on WeeBee, sent by email as a single-use code that expires in 14 days. When you
>    accept, you and the person who invited you automatically become friends. You must be 18 or
>    over. Everyone holds a few invitations — at most 5 banked, one more every 30 days, and a new
>    account starts with 2. (§4.1, §4.2, §4.4)
> 2. **Nothing on WeeBee is public.** There are no pages a logged-out visitor can see except log
>    in, register and invite acceptance. Search engines find nothing. There is no global search
>    of people or content anywhere on the platform, and a copied web address shows a stranger
>    nothing. (§2, §9.3, §17)
> 3. **Friendship is mutual, and capped at 300.** Anything that would push either person past 300
>    fails with a plain, honest error rather than silently. (§5.1)
> 4. **There are two ways to post, and you choose every time.** *Send to a few friends* pushes a
>    post into the feeds of up to 30 hand-picked friends. *Post to my blog* puts it on your
>    profile where all your friends can find it — they get a notification saying you posted,
>    never the words themselves. There is no default; a missing choice is an honest error. Every
>    post carries a line saying exactly who can see it, and the comment box repeats it. Feed
>    posts by the same author are spaced about 10 minutes apart. Your own feed posts also show up
>    on your profile's Blog tab, visible to exactly the people you sent them to.
>    (§7.1, §7.3, §7.9, §9.1, §12.2, §13.6)
> 5. **There is no share, reshare, repost, quote or forward button, of any kind.** Nothing can
>    travel past the audience its author picked. If you want a friend to see something, you
>    retype it yourself. (§1.2, §17)
> 6. **Nothing is counted.** No likes, no follower counts, no view counts, no post counts, no
>    unread badges, no page numbers. Not hidden — they do not exist. (§8.2, §12.2, §17)
> 7. **Reactions are about six fixed warm phrases** — "Agreed!", "Love it!", "So proud!",
>    "Thinking of you", "Congrats!", "Ha!" — and **only the person you reacted to ever sees
>    yours.** They see your name and the phrase, never a number, and only on the single-post
>    view. Everyone else sees nothing at all, not even that a reaction exists. You cannot react
>    to your own post or comment. (§8.2, §8.2.2)
> 8. **The feed is a mailbox, not a machine.** Strictly newest first: feed posts sent to you, and
>    notifications. No ranking, no suggested content, no inserted people, no ads, no infinite
>    scroll — older posts are a plain link at the foot of the page, with no page numbers and no
>    total. (§7.7, §7.7.1)
> 9. **Everything you say is deleted after 90 days** — every post, every comment, every reaction,
>    permanently, along with any attached image, and out of the last encrypted backup within 30
>    days after that. **What you *are* stays**: your profile photo, both bio fields, your gallery,
>    your interests, your contact card, your groups and your friend list persist until you change
>    them. You may pin up to 10 of your own blog posts to keep them past 90 days; pinning never
>    preserves the comments or reactions underneath them, and nothing marks that they existed. A
>    post with 14 days or fewer left shows a countdown in real days. (§7.5, §7.6, §9.7)
> 10. **New people reach you through exactly one mutual friend, and never further.** Only a
>     friend-of-friend can send you a friend request; strangers cannot. A request carries no
>     written message — just their photo, short bio, the interests you share and the friends you
>     have in common. Declines are silent. There is a discover page you must go and visit;
>     nothing from it ever appears in your feed. (§5.2, §11.1, §11.4)
> 11. **Interests are hashtags chosen from a list WeeBee writes**, never typed by you; you may
>     carry up to 10 on your profile. Putting one on a blog post is what lets a friend-of-friend
>     carrying the same interest see that post — so tagging is an audience decision, not filing.
>     There is no way to browse everything tagged with anything. (§11.2, §11.3)
> 12. **There are no private messages.** Instead you keep a contact card — up to 12 phone numbers,
>     email addresses and messenger links — and decide, item by item and friend by friend, who
>     sees what. A friend requests it with a button and the system replies with exactly their
>     version. The conversation itself happens somewhere else. (§10)
> 13. **One image per post, and no video or audio at all.** Links only from a list of approved
>     sites, and even then as plain clickable links, never embedded players or preview cards. No
>     polls. Location data is stripped from every image on upload. Every image asks you to
>     describe it in your own words — and in your gallery that description *is* the caption,
>     because there is no separate caption field. (§7.2, §7.2.2, §9.4, §16.3)
> 14. **It is a website, and it is for individual people.** No phone app in version one. No
>     business, brand, organisation or bot accounts. There are no ads and no tracking of any
>     kind, and mandatory subscriptions are ruled out. (§2, §15.2, §15.3, §15.4, §17)

Close the section with this line, verbatim:

> **Tailoring the pitch into a sales pitch is forbidden.** No character is shown only the parts
> they would like, and none is spared a mechanic they would object to.

### `## 3. The constants that bite`

*(~650 words.)* Copy this table. Every row was verified against `SPEC.md` v1.27 via
`mockups/CRIB.md` §1. You may add a row if a core page shows you a constant that matters and is
missing here; do not remove one, and do not change a value.

| Constant | Value | SPEC | What it means in practice |
|---|---|---|---|
| `FRIEND_CAP` | 300 | §5.1 | The ceiling on friendships. Breaching it fails with a plain error, never silently. |
| `POST_AUDIENCE_MAX` | 30 | §7.1, §7.3 | The most people one feed post can be pushed to. |
| `GROUP_SIZE_MAX` | 30 | §6 | Matches the above, so any group is always a valid post audience. Groups are private to their owner; members never know they are in one. |
| `POST_MIN_INTERVAL_MINUTES` | ≈ 10 | §7.3, §13.6 | Minimum gap between one author's feed posts. Blog posts are exempt. |
| `CONTENT_TTL_DAYS` | 90 | §7.5 | Every post, comment and reaction is permanently deleted 90 days after it was made. |
| `EXPIRY_COUNTDOWN_DAYS` | 14 | §7.5 | A post with 14 days or fewer left shows a countdown, in real days, to everyone who can see it. |
| `BACKUP_RETENTION_DAYS` | 30 | §7.5, §4.7 | Deleted content leaves the last encrypted backup within 30 days after live deletion. |
| `PIN_LIMIT` | 10 | §7.6 | Blog posts an author may pin to exempt from expiry. Feed posts can never be pinned. |
| `GALLERY_MAX` | 8 | §9.4 | Photos in the profile gallery, friends only, separate from the profile photo. There is no album concept at all. |
| `PROFILE_HASHTAG_MAX` | 10 | §11.2 | Interests on a profile. |
| `CONTACT_ITEMS_MAX` | 12 | §10.2 | Items on a contact card. |
| `BIO_SHORT_MAX` | 200 chars | §9.4 | Short bio. Visible to friends-of-friends; never renders a clickable link. |
| `BIO_EXTENDED_MAX` | 2,000 chars | §9.4 | Extended bio. Friends only; allowlisted links permitted. |
| `POST_LENGTH_MAX` | 10,000 chars | §7.2.1 | |
| `COMMENT_LENGTH_MAX` | 2,000 chars | §8.1 | Comments are flat — one linear list per post, no nested replies. |
| `FEED_FOLD_CHARS` | 500 | §7.7 | Long posts fold in the feed and on the Pinned tab, with a "read more" that expands in place. |
| `BLOG_FOLD_CHARS` | 2,000 | §7.7 | The same on a profile's Blog tab. |
| `COMMENT_FOLD_CHARS` | 300 | §8.1 | Comments fold at 300 characters on every surface. |
| `POSTS_PER_PAGE_DEFAULT` | 20 | §7.7.1 | Reader-chosen: 20, 40 or 60. No page numbers, no totals, no infinite scroll. |
| `INVITE_BANK_MAX` | 5 | §4.2 | Most invitations one person can hold at once. |
| `INVITE_NEW_ACCOUNT` | 2 | §4.2 | What a new account starts with. |
| `INVITE_REPLENISH_DAYS` | 30 | §4.2 | One more invitation every 30 days, up to the bank max. |
| `INVITE_EXPIRY_DAYS` | 14 | §4.1 | Expired invitations return to the sender's budget. |
| Friend requests per day | 20 (suggested) | §13.6, §14 | |
| Introductions per day | 10 (suggested) | §13.6, §14 | Both parties must accept before a friendship is created. |
| `REQUEST_HOLD_AFTER_PROFILE_CHANGE_HOURS` | 12 | §5.2, §13.6 | After uploading a photo or changing your short bio you cannot send friend requests for 12 hours. Changing either is otherwise free and unlimited. |
| Pending friend-request expiry | 90 days | §5.2 | The frozen request card is destroyed with it. |
| Re-request cooldown after a decline | 90 days | §5.2 | Declines are silent; the requester is never told. |
| `ALT_TEXT_MAX` | 1,000 chars | §16.3 | Every image carries a description the uploader writes. |
| `NAME_TRANSITION_DAYS` | 90 | §4.5.1 | A changed display name shows as "New (formerly Old)" for 90 days. |
| `INACTIVITY_DELETE_DAYS` | 730 | §4.8 | Two years without a login deletes the account, after email warnings at 180, 365, 670 and 700 days. |
| `DELETE_GRACE_DAYS` | 30 | §4.7 | A user-deleted account is recoverable for 30 days. |

### `## 4. What is absent`

*(~500 words.)* Most of what these ten characters collide with is a **missing feature**, so a
list of absences is more useful to a later session than a list of features. Copy the list below.
Keep the two markers exactly as given — they mean different things, and the difference matters:

- **Forbidden by rule** — the document names it and refuses it.
- **Verified absent** — neither `SPEC.md` nor `ARCHITECTURE.md` describes any such feature, and
  §17's non-goals list does not name it either. The honest form is "the platform has no such
  feature," not "the platform forbids it."

| Absent | Marker | Ref |
|---|---|---|
| Reshare, repost, quote or forward, of any kind | forbidden by rule | §1.2, §17 |
| Likes, and every visible count: followers, reactions, views, post counts, page numbers | forbidden by rule | §8.2, §17 |
| Algorithmic feed, ranking, suggested content, inserted people, ads | forbidden by rule | §7.7, §17 |
| Direct messages | forbidden by rule | §10.1, §17 |
| Public or logged-out content of any kind beyond login, registration and invite acceptance | forbidden by rule | §2, §17 |
| Global search of people or content | forbidden by rule | §17 |
| Global hashtag browsing — no "see all posts tagged #x" anywhere | forbidden by rule | §11.2, §17 |
| Infinite scroll, "load more", page numbers, totals | forbidden by rule | §7.7.1, §17 |
| Absolute dates and times anywhere in the interface, and any date-based archive navigation | forbidden by rule | §7.5.1, §7.7.1, §17 |
| Gallery captions — the image description *is* the caption | forbidden by rule | §9.4, §17 |
| "You have memories!" and every other engagement-bait notification — SPEC names this one as the example | forbidden by rule | §12.2 |
| Video and audio hosting; allowlisted media links never embed as players or preview cards | forbidden by rule | §7.2, §17 |
| Events system — delegated to allowlisted external services | forbidden by rule | §17 |
| Nested comment replies — comments are one flat list | forbidden by rule | §8.1 |
| Structured profile fields — no relationship status, location, birthday or employer | forbidden by rule | §9.6, §17 |
| Business, brand, organisation and bot accounts | forbidden by rule | §15.4, §17 |
| Accounts for anyone under 18 | forbidden by rule | §4.4, §17 |
| Native phone app in version 1 | forbidden by rule | §17 |
| CAPTCHA or any third-party human challenge | forbidden by rule | §4.6.1, §17 |
| **Any way to tag or mention another person** — in a post, in a photo, or with an @-name | **verified absent** | every use of "tagged" in `SPEC.md` means a hashtag; §17 does not name person-tagging |

Add a short closing paragraph in your own words about that last row, since it is the one a later
session is most likely to get wrong: it is an *absence in the documents*, not a stated refusal,
and a character whose habit depends on tagging people should say so plainly and the report should
put it in its findings block.

### `## 5. The core page set — what each page shows`

*(~700 words, your own words — the longest research section.)* One short paragraph per core page,
in this order: `index.html`, `login.html`, `feed.html`, `composer.html`, `post-feed.html`,
`overlay-post.html`, `profile-blog.html`, `profile-pinned.html`, `profile-photos.html`,
`profile-about.html`, `friends.html`, `friend-request-received.html`, `discover.html`,
`contact-card-received.html`, `settings.html`.

Each paragraph: **what a user actually sees on that page**, in plain language, plus any verbatim
line on it worth a character reading aloud. Roughly 40–60 words each. Write them so a later
session can put the page in front of its character and describe the character's reaction
**without opening the file**. Do not describe the build commentary. Do not evaluate the design.

Open the section with one line naming the path (`mockups/site/`), the rebuild command, and the
rule that a character session opens **only** the extra pages its own prompt names, never these
fifteen.

### `## 6. Verbatim interface strings worth quoting`

*(~300 words.)* From `mockups/CRIB.md` §2 and from the pages you read, the strings a character
might plausibly read aloud or react to. Include at minimum, verbatim:

- The composer's two destination choices: *"Send to a few friends — appears in their feed"* /
  *"Post to my blog — all your friends can find it."*
- The three stated-visibility lines and the comment-box line (§7.9), and the expiry countdown
  form *"Deletes in 6 days"* (§7.5).
- The unfriend confirmation (§5.3) and the friends-page filter label *"Filter your friends"*
  (§11.6).
- The anti-phishing promise (§4.6.1): *"WeeBee will never email you a link to log in or reset
  your password — only a code you type in yourself."*
- The reaction line idiom *"Alice: Love it! · Mom: So proud!"* and the react control's two states,
  *"React"* and *"Reacted: Love it!"* (§8.2, §8.2.2).
- The notification wordings of §12.2, including the *"and others"* overflow form.

Add any others you find on the pages. Mark each with its SPEC section.

### `## 7. The honesty rule`

*(~130 words.)* Copy this **verbatim**, with one line of your own above it saying that every
character prompt restates it and that it is the rule the exercise stands or falls on:

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

### `## 8. The report skeleton`

*(~350 words.)* Copy the skeleton and the budget table below **verbatim**. Introduce them with
one line: the headings are identical across all ten reports and are pronoun-free on purpose, so
the set stays comparable and no heading is edited per character.

````
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
````

| Section | What goes in it | Words |
|---|---|---|
| 1. First contact | Which pages were put in front of them, in what order, and their unguided reaction *before* anything was explained. Names the extra pages this session opened. | 100–140 |
| 2. How WeeBee was explained | The fourteen facts of §2 re-worded in this person's vocabulary — **the actual words used**, not a description of them. All fourteen, including the ones they will hate. Compress freely; drop nothing. | 130–180 |
| 3. Interview | A transcript. `**Interviewer:**` / `**Name:**`, six to ten exchanges. The character's own voice throughout — not the analyst's, not WeeBee's. The longest section. | 250–350 |
| 4. What worked, and what was refused | Two short paragraphs or two short lists. Honest in both directions. | 100–150 |
| 5. Predicted behaviour | Do they sign up? What happens in week one, month one, month six? Which constants do they hit, **named and numbered**. | 130–200 |
| 6. How the other nine would receive this person | A light prediction reasoned from the archetype descriptions only. Marked as provisional in the text — session A11 does the real collision analysis with all ten reports in hand. | 70–110 |
| 7. Verdict | One paragraph. Does WeeBee want this person? Does this person want WeeBee? The two answers may differ, and often will. | 50–90 |
| Possible design findings | Zero to three bullets, forty words each at most. Observational only. Each names the SPEC section it touches. Write `None.` rather than manufacture one. | not counted |

Add these two lines after the table, verbatim:

> **Total for sections 1–7: 800–1,200 words.** Over budget, cut from 1, 5 and 6 first; never from
> the interview, which carries the thing the founder cannot get any other way.
>
> Reports are named `01-joe-blah.md`, `02-mary-jane.md`, `03-dorothy.md`, `04-jim-roxx.md`,
> `05-karen.md`, `06-tyler.md`, `07-susan.md`, `08-dave-crypto.md`, `09-lisa.md`, `10-mike.md`,
> and are written into `archetypes/`.

### `## 9. House rules for a character session`

*(~200 words, your own words.)* State these, plainly:

- Write **one file**, the report named in your prompt, into `archetypes/`. Create nothing else.
- **Never append to, edit, or "improve" `BRIEF.md`.** Ten sessions run in any order; a shared
  file they all write to is a merge conflict waiting to happen. If the brief is wrong or
  incomplete, say so in your report's findings block and carry on.
- Do not edit `SPEC.md`, `ARCHITECTURE.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `TODO.md`, anything
  under `prompts/`, or anything under `mockups/`. Do not touch `00_scratch/`.
- No CHANGELOG entry, no TODO row, no version bump.
- Open only the extra pages your own prompt names. The fifteen core pages are described in §5 so
  that you do not have to.
- The character is fictional and the interview is imagined. Nobody is contacted; nothing is
  published. Write the report as the record of a session that is being imagined, not as though
  the meeting occurred.
- The mockups are a **static design mockup**, not a working product. Nothing on them saves,
  submits or logs in. Where a character asks what a button does, answer from the fourteen facts,
  not from clicking.

## Before you finish

Check every one of these, in order:

1. `archetypes/BRIEF.md` exists and is the **only** file you created or modified, other than
   the generated `mockups/site/` directory.
2. All nine section headings are present, spelled exactly as given above, in order.
3. Total length is between 2,500 and 4,000 words. If you are under, the page descriptions in §5
   are probably too thin — that is the section that earns its length.
4. The fourteen facts, the honesty rule, the report skeleton and the budget table are copied
   **verbatim**, not paraphrased and not reordered.
5. §5 describes all fifteen core pages, and every description came from opening the file.
6. Every SPEC section number in the file is one that appeared in this prompt or in a file you
   read. You invented none.
7. `BRIEF.md` names **no archetype and predicts no reaction.** It is neutral about the ten
   characters; per-character material lives in the character prompts. Search your own draft for
   the ten names — Joe, Mary, Dorothy, Jim, Karen, Tyler, Susan, Dave, Lisa, Mike — and remove
   any that appear.
8. You wrote no report, simulated no character, and made no design recommendation.

Then report back to the founder in three or four sentences: the word count, anything you could
not verify, and anything on the fifteen pages that surprised you.
