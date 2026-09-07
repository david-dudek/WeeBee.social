# BRIEF.md — shared reference for the archetype track

Shared reference for the ten archetype-reaction sessions (A1–A10) and the synthesis session
(A11) that follows them. Built in session A0, against project version 1.27 and the mockup set as
built through session M8.

## 0. How to use this file

If you are A1–A10, write one character report by imagining that character in front of the WeeBee
mockups. Open only three things: this file, the character prompt you were given, and the two or
three extra mockup pages that prompt names. Do not open SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md,
or any of the fifteen core pages described in §5 — they are described there so nobody has to
reopen them. If you are A11, read all ten finished reports and write the synthesis.

One naming note that matters: the mockups render a sample account belonging to David Dudek, with
friends Alice, Tom and Mom, and a friend-of-friend, Priya. None of these four is one of the ten
archetypes. If your character prompt names someone else, that is your character — do not confuse
them with David or his sample friends, and do not write a report about David.

## 1. What WeeBee is, in one paragraph

WeeBee is an invite-only social website for adults, built around small, deliberately chosen
audiences instead of broadcast. Every post goes to a hand-picked list of friends or onto a profile
that friends can browse; there is no public content, no algorithmic feed, no counts of any kind,
no resharing, and no direct messaging. New connections travel through exactly one mutual friend at
a time. Content — posts, comments, reactions — is deleted after 90 days by default; what a person
is (profile, photos, interests, contacts) persists until changed. It is a website only, for
individuals only, with no ads and no tracking.

## 2. The canonical account — the fourteen facts every character is told

Every character session re-words these same fourteen facts into that character's own vocabulary.
The wording changes; the substance does not — the same facts reach every character, and nobody is
spared a mechanic they would object to. The parenthetical section numbers are for a session's own
reference and never appear in a report's spoken dialogue, though a report may cite them in its
analysis sections and findings.

You cannot join on your own. The only way in is a personal invitation from someone already on
WeeBee, sent by email as a single-use code that expires in 14 days. When you accept, you and the
person who invited you automatically become friends. You must be 18 or over. Everyone holds a few
invitations — at most 5 banked, one more every 30 days, and a new account starts with 2. (§4.1,
§4.2, §4.4)

Nothing on WeeBee is public. There are no pages a logged-out visitor can see except log in,
register and invite acceptance. Search engines find nothing. There is no global search of people
or content anywhere on the platform, and a copied web address shows a stranger nothing. (§2,
§9.3, §17)

Friendship is mutual, and capped at 300. Anything that would push either person past 300 fails
with a plain, honest error rather than silently. (§5.1)

There are two ways to post, and you choose every time. Send to a few friends pushes a post into
the feeds of up to 30 hand-picked friends. Post to my blog puts it on your profile where all your
friends can find it — they get a notification saying you posted, never the words themselves.
There is no default; a missing choice is an honest error. Every post carries a line saying exactly
who can see it, and the comment box repeats it. Feed posts by the same author are spaced about 10
minutes apart. Your own feed posts also show up on your profile's Blog tab, visible to exactly the
people you sent them to. (§7.1, §7.3, §7.9, §9.1, §12.2, §13.6)

There is no share, reshare, repost, quote or forward button, of any kind. Nothing can travel past
the audience its author picked. If you want a friend to see something, you retype it yourself.
(§1.2, §17)

Nothing is counted. No likes, no follower counts, no view counts, no post counts, no unread
badges, no page numbers. Not hidden — they do not exist. (§8.2, §12.2, §17)

Reactions are about six fixed warm phrases — "Agreed!", "Love it!", "So proud!", "Thinking of
you", "Congrats!", "Ha!" — and only the person you reacted to ever sees yours. They see your name
and the phrase, never a number, and only on the single-post view. Everyone else sees nothing at
all, not even that a reaction exists. You cannot react to your own post or comment. (§8.2, §8.2.2)

The feed is a mailbox, not a machine. Strictly newest first: feed posts sent to you, and
notifications. No ranking, no suggested content, no inserted people, no ads, no infinite scroll —
older posts are a plain link at the foot of the page, with no page numbers and no total. (§7.7,
§7.7.1)

Everything you say is deleted after 90 days — every post, every comment, every reaction,
permanently, along with any attached image, and out of the last encrypted backup within 30 days
after that. What you are stays: your profile photo, both bio fields, your gallery, your
interests, your contact card, your groups and your friend list persist until you change them. You
may pin up to 10 of your own blog posts to keep them past 90 days; pinning never preserves the
comments or reactions underneath them, and nothing marks that they existed. A post with 14 days or
fewer left shows a countdown in real days. (§7.5, §7.6, §9.7)

New people reach you through exactly one mutual friend, and never further. Only a
friend-of-friend can send you a friend request; strangers cannot. A request carries no written
message — just their photo, short bio, the interests you share and the friends you have in
common. Declines are silent. There is a discover page you must go and visit; nothing from it ever
appears in your feed. (§5.2, §11.1, §11.4)

Interests are hashtags chosen from a list WeeBee writes, never typed by you; you may carry up to
10 on your profile. Putting one on a blog post is what lets a friend-of-friend carrying the same
interest see that post — so tagging is an audience decision, not filing. There is no way to browse
everything tagged with anything. (§11.2, §11.3)

There are no private messages. Instead you keep a contact card — up to 12 phone numbers, email
addresses and messenger links — and decide, item by item and friend by friend, who sees what. A
friend requests it with a button and the system replies with exactly their version. The
conversation itself happens somewhere else. (§10)

One image per post, and no video or audio at all. Links only from a list of approved sites, and
even then as plain clickable links, never embedded players or preview cards. No polls. Location
data is stripped from every image on upload. Every image asks you to describe it in your own
words — and in your gallery that description is the caption, because there is no separate caption
field. (§7.2, §7.2.2, §9.4, §16.3)

It is a website, and it is for individual people. No phone app in version one. No business,
brand, organisation or bot accounts. There are no ads and no tracking of any kind, and mandatory
subscriptions are ruled out. (§2, §15.2, §15.3, §15.4, §17)

Tailoring the pitch into a sales pitch is forbidden. No character is shown only the parts they
would like, and none is spared a mechanic they would object to.

## 3. The constants that bite

Every row was verified against SPEC.md v1.27 via mockups/CRIB.md §1. Add a row if a core page
shows a constant that matters and is missing here; do not remove one, and do not change a value.

| Constant | Value | SPEC | What it means in practice |
|---|---|---|---|
| FRIEND_CAP | 300 | §5.1 | The ceiling on friendships. Breaching it fails with a plain error, never silently. |
| POST_AUDIENCE_MAX | 30 | §7.1, §7.3 | The most people one feed post can be pushed to. |
| GROUP_SIZE_MAX | 30 | §6 | Matches the above, so any group is always a valid post audience. Groups are private to their owner; members never know they are in one. |
| POST_MIN_INTERVAL_MINUTES | ≈ 10 | §7.3, §13.6 | Minimum gap between one author's feed posts. Blog posts are exempt. |
| CONTENT_TTL_DAYS | 90 | §7.5 | Every post, comment and reaction is permanently deleted 90 days after it was made. |
| EXPIRY_COUNTDOWN_DAYS | 14 | §7.5 | A post with 14 days or fewer left shows a countdown, in real days, to everyone who can see it. |
| BACKUP_RETENTION_DAYS | 30 | §7.5, §4.7 | Deleted content leaves the last encrypted backup within 30 days after live deletion. |
| PIN_LIMIT | 10 | §7.6 | Blog posts an author may pin to exempt from expiry. Feed posts can never be pinned. |
| GALLERY_MAX | 8 | §9.4 | Photos in the profile gallery, friends only, separate from the profile photo. There is no album concept at all. |
| PROFILE_HASHTAG_MAX | 10 | §11.2 | Interests on a profile. |
| CONTACT_ITEMS_MAX | 12 | §10.2 | Items on a contact card. |
| BIO_SHORT_MAX | 200 chars | §9.4 | Short bio. Visible to friends-of-friends; never renders a clickable link. |
| BIO_EXTENDED_MAX | 2,000 chars | §9.4 | Extended bio. Friends only; allowlisted links permitted. |
| POST_LENGTH_MAX | 10,000 chars | §7.2.1 | |
| COMMENT_LENGTH_MAX | 2,000 chars | §8.1 | Comments are flat — one linear list per post, no nested replies. |
| FEED_FOLD_CHARS | 500 | §7.7 | Long posts fold in the feed and on the Pinned tab, with a "read more" that expands in place. |
| BLOG_FOLD_CHARS | 2,000 | §7.7 | The same on a profile's Blog tab. |
| COMMENT_FOLD_CHARS | 300 | §8.1 | Comments fold at 300 characters on every surface. |
| POSTS_PER_PAGE_DEFAULT | 20 | §7.7.1 | Reader-chosen: 20, 40 or 60. No page numbers, no totals, no infinite scroll. |
| INVITE_BANK_MAX | 5 | §4.2 | Most invitations one person can hold at once. |
| INVITE_NEW_ACCOUNT | 2 | §4.2 | What a new account starts with. |
| INVITE_REPLENISH_DAYS | 30 | §4.2 | One more invitation every 30 days, up to the bank max. |
| INVITE_EXPIRY_DAYS | 14 | §4.1 | Expired invitations return to the sender's budget. |
| Friend requests per day | 20 (suggested) | §13.6, §14 | |
| Introductions per day | 10 (suggested) | §13.6, §14 | Both parties must accept before a friendship is created. |
| REQUEST_HOLD_AFTER_PROFILE_CHANGE_HOURS | 12 | §5.2, §13.6 | After uploading a photo or changing your short bio you cannot send friend requests for 12 hours. Changing either is otherwise free and unlimited. |
| Pending friend-request expiry | 90 days | §5.2 | The frozen request card is destroyed with it. |
| Re-request cooldown after a decline | 90 days | §5.2 | Declines are silent; the requester is never told. |
| ALT_TEXT_MAX | 1,000 chars | §16.3 | Every image carries a description the uploader writes. |
| NAME_TRANSITION_DAYS | 90 | §4.5.1 | A changed display name shows as "New (formerly Old)" for 90 days. |
| INACTIVITY_DELETE_DAYS | 730 | §4.8 | Two years without a login deletes the account, after email warnings at 180, 365, 670 and 700 days. |
| DELETE_GRACE_DAYS | 30 | §4.7 | A user-deleted account is recoverable for 30 days. |

## 4. What is absent

Most of what these ten characters collide with is a missing feature, so a list of absences is
more useful to a later session than a list of features. The two markers below mean different
things: **forbidden by rule** — the document names it and refuses it; **verified absent** —
neither SPEC.md nor ARCHITECTURE.md describes any such feature, and §17's non-goals list does not
name it either. The honest form for the second kind is "the platform has no such feature," not
"the platform forbids it."

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
| Gallery captions — the image description is the caption | forbidden by rule | §9.4, §17 |
| "You have memories!" and every other engagement-bait notification — SPEC names this one as the example | forbidden by rule | §12.2 |
| Video and audio hosting; allowlisted media links never embed as players or preview cards | forbidden by rule | §7.2, §17 |
| Events system — delegated to allowlisted external services | forbidden by rule | §17 |
| Nested comment replies — comments are one flat list | forbidden by rule | §8.1 |
| Structured profile fields — no relationship status, location, birthday or employer | forbidden by rule | §9.6, §17 |
| Business, brand, organisation and bot accounts | forbidden by rule | §15.4, §17 |
| Accounts for anyone under 18 | forbidden by rule | §4.4, §17 |
| Native phone app in version 1 | forbidden by rule | §17 |
| CAPTCHA or any third-party human challenge | forbidden by rule | §4.6.1, §17 |
| Any way to tag or mention another person — in a post, in a photo, or with an @-name | verified absent | every use of "tagged" in SPEC.md means a hashtag; §17 does not name person-tagging |

That last row is the one a later session is most likely to get wrong. It is an absence in the
documents, not a stated refusal — nobody wrote a rule against tagging a friend by name, it simply
never appears anywhere the feature would live. A character whose habit depends on tagging people
should say so plainly, and the report's findings block should note it rather than assume some
workaround exists.

## 5. The core page set — what each page shows

All fifteen pages live in mockups/site/, rebuilt with `cd mockups && python3 build.py`. A
character session opens only the extra pages its own prompt names — never these fifteen; they are
described here so nobody has to reopen them.

**index.html** — not a page a real user would see; the mockup track's own map, listing every page
built across sessions M1–M8 with a one-line description and SPEC citations, plus a checkbox
toggling build commentary on or off.

**login.html** — a plain email-and-password form, a "Log in" button, a "Forgot your password?"
link, and a boxed notice reading "WeeBee will never email you a link to log in or reset your
password — only a code you type in yourself." No CAPTCHA anywhere.

**feed.html** — David's own feed: friends' posts (Tom, Alice, Mom, Priya) interleaved with
notifications ("Alice and Tom commented on your post"), strictly newest first, relative ages only
("About an hour ago"), a "Read more" fold, an "edited" marker, "Deletes in 6 days", and a single
"Older posts →" link at the foot — no page numbers, no total.

**composer.html** — the one post-creation form, shown across ten states: the destination choice
with no default and its error; the audience picker with a live "3 of 30 friends selected" count
and a "Save this selection as a group?" offer; an over-30 warning; the hashtag picker's live
visibility line; the preformatted toggle; an image's alt-text choice; a 10,140/10,000 overrun; a
rejected link; and the switch-destination notices.

**post-feed.html** — a feed post of David's: a reaction line visible only to him ("Alice: Love
it!", "Mom: So proud!"), no react control on his own content, a flat comment list where friends'
comments carry "React" / "Reacted: Agreed!" with the six fixed phrases, and a comment box
repeating "Your comment will be visible to the same people."

**overlay-post.html** — the click-to-expand image dialog opened from a post: the page dimmed
behind it, a "Close" button, alt text shown as a visible caption. No Previous/Next controls — a
post carries only one image.

**profile-blog.html** — David's profile as friend Alice sees it, on the Blog tab: a header (photo,
the dual name "David Dudek (formerly Dave Dudek)", "Report this profile") shared by all four tabs,
and his posts newest-first, folded at the wider 2,000-character threshold, including a feed post
shown here too and a pinned post in its ordinary place.

**profile-pinned.html** — David's Pinned tab: his shelf of posts kept past 90 days, folded at the
tighter 500-character threshold, each with its ordinary relative age and a "Pinned" marker instead
of an expiry countdown. Nothing marks that an old post's expired comments ever existed.

**profile-photos.html** — the Photos tab: an eight-image gallery grid of plain buttons, each
opening the click-to-expand overlay. No caption field — each image's alt text is the only
description it carries.

**profile-about.html** — the About tab: a short bio (visible to friends-of-friends, never a
clickable link even as a URL typed in prose), an extended bio (friends only, one allowlisted
link), up to ten interest hashtags linking to Discover, and "Knows Tom, Mom and others" for mutual
friends — names, never a count.

**friends.html** — David's alphabetical friend list (Alice, Ben, Grace, Henry, Mom, Nadia, Sofia,
Tom here), a real visible label "Filter your friends" above the search box — never placeholder
text, never "Search" — and no friend count anywhere.

**friend-request-received.html** — a friend-request card from Priya: photo and short bio frozen at
send time, name/hashtags/mutual friends and "Report this profile" all live, no message field, and
two silent buttons, "Accept" and "Decline".

**discover.html** — the one page a user must deliberately visit: "People you may know"
(friends-of-friends only, plain auto-context like "Knows Alice · shares #hiking", no score) and
"Matched posts" (hashtag-gated posts from friends-of-friends). Nothing here is pushed to the feed
or announced to anyone.

**contact-card-received.html** — what a friend gets after tapping "Request contact card" with
nothing to type: an instant automatic reply with exactly the items they're allowed to see (a
populated example — phone, email, WhatsApp — and a genuinely empty one, "You haven't shared
anything on your contact card with Henry"), plus an "ask for more" flow flagged as v1.1.

**settings.html** — one page labelled "Assembled, not specified," gathering: posts-per-page with a
required explicit Apply, theme/font pickers with placeholder names, a "follow posts I comment on
by default" toggle, an optional email-notifications checkbox, a code-based login-email-change
flow, a data-export button, and a link to account deletion.

## 6. Verbatim interface strings worth quoting

The composer's two destination choices (§7.1): *"Send to a few friends — appears in their feed"*
/ *"Post to my blog — all your friends can find it."*

The stated-visibility lines and the comment-box line (§7.9): *"Visible to: the friends {author}
sent this to."* (feed post); *"Visible to: all of {author}'s friends."* (untagged profile post);
*"Visible to: all of {author}'s friends, and friends-of-friends with any of #hiking, #jazz."*
(tagged profile post); and, on every comment box, *"Your comment will be visible to the same
people."* The expiry countdown (§7.5): *"Deletes in 6 days."*

The unfriend confirmation (§5.3): *"They'll no longer see your posts or your about section. If
you have friends in common, they can still see your name, photo and short bio — and any blog post
tagged with an interest you both share."* The friends-page filter label (§11.6): *"Filter your
friends"* — real, visible text, never placeholder, never "Search".

The anti-phishing promise (§4.6.1): *"WeeBee will never email you a link to log in or reset your
password — only a code you type in yourself."*

The reaction line idiom (§8.2): *"Alice: Love it! · Mom: So proud!"* — names and phrases only,
never a number. The react control's two states (§8.2.2): *"React"* (not yet reacted) and
*"Reacted: Love it!"* (reacted, phrase named), plus *"Remove reaction"* to clear one.

The notification wordings (§12.2): *"David posted to his blog"*; *"David changed his profile
photo"*; *"David added 3 photos to his gallery"*; *"Alice and Tom commented on your post"* — with
an overflow form of *"and others"*, never a count like "3 new comments". The coalesced form
(§12.3): *"David posted twice to his blog."*

The non-friend profile message (§9.1): *"You and David are not friends. Friends see his posts,
photos and about section."* The audience-save offer (§6): *"Save this selection as a group?"*

## 7. The honesty rule

Every character prompt restates this rule; it is the one the whole exercise stands or falls on.
Copied here verbatim:

The honesty rule. This character has full latitude, including outright rejection. They may say
they would never sign up; that WeeBee is boring; that they do not understand it; that they would
join and then quietly stop logging in; that the thing they use social media for does not exist
here and no amount of explaining changes that. Several of these archetypes are structurally
impossible on a platform with no public content, no follower counts, no reshare and a capped
audience — where that is true of your character, say so plainly and do not invent a workaround
that keeps everyone happy. A report in which the character politely likes WeeBee is a failed
report. Equally, do not manufacture hostility: where a mechanic genuinely suits this person, say
that too, with the same directness. What is forbidden is the comfortable middle — the report that
finds something for everyone and commits to nothing.

## 8. The report skeleton

Identical across all ten reports, pronoun-free on purpose so the set stays comparable — no heading
is edited per character. Copied here verbatim, with the section budget table:

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
| 1. First contact | Which pages were put in front of them, in what order, and their unguided reaction before anything was explained. Names the extra pages this session opened. | 100–140 |
| 2. How WeeBee was explained | The fourteen facts of §2 re-worded in this person's vocabulary — the actual words used, not a description of them. All fourteen, including the ones they will hate. Compress freely; drop nothing. | 130–180 |
| 3. Interview | A transcript. **Interviewer:** / **Name:**, six to ten exchanges. The character's own voice throughout — not the analyst's, not WeeBee's. The longest section. | 250–350 |
| 4. What worked, and what was refused | Two short paragraphs or two short lists. Honest in both directions. | 100–150 |
| 5. Predicted behaviour | Do they sign up? What happens in week one, month one, month six? Which constants do they hit, named and numbered. | 130–200 |
| 6. How the other nine would receive this person | A light prediction reasoned from the archetype descriptions only. Marked as provisional in the text — session A11 does the real collision analysis with all ten reports in hand. | 70–110 |
| 7. Verdict | One paragraph. Does WeeBee want this person? Does this person want WeeBee? The two answers may differ, and often will. | 50–90 |
| Possible design findings | Zero to three bullets, forty words each at most. Observational only. Each names the SPEC section it touches. Write None. rather than manufacture one. | not counted |

Total for sections 1–7: 800–1,200 words. Over budget, cut from 1, 5 and 6 first; never from the
interview, which carries the thing the founder cannot get any other way.

Reports are named 01-joe-blah.md, 02-mary-jane.md, 03-dorothy.md, 04-jim-roxx.md, 05-karen.md,
06-tyler.md, 07-susan.md, 08-dave-crypto.md, 09-lisa.md, 10-mike.md, and are written into
archetypes/.

## 9. House rules for a character session

Write one file, the report named in your prompt, into archetypes/. Create nothing else.

Never append to, edit, or "improve" BRIEF.md. Ten sessions run in any order; a shared file they
all write to is a merge conflict waiting to happen. If the brief is wrong or incomplete, say so in
your findings block and carry on.

Do not edit SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md, CHANGELOG.md, TODO.md, anything under
prompts/, or anything under mockups/. Do not touch 00_scratch/. No CHANGELOG entry, no TODO row,
no version bump.

Open only the extra pages your own prompt names — the fifteen core pages are described in §5 so
you do not have to.

The character is fictional and the interview is imagined. Nobody is contacted; nothing is
published. Write the report as the record of an imagined session, not as though the meeting
occurred.

The mockups are static, not a working product — nothing on them saves, submits or logs in. Where
a character asks what a button does, answer from the fourteen facts, not from clicking.
