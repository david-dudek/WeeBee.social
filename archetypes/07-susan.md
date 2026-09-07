# 07 — Susan
> *the family historian — the unofficial archivist of an extended family*

## 1. First contact

Susan was walked through the core screens in order: the feed (posts and notices, newest on top), the posting screen with its two destinations, her own profile's Blog, Pinned and Photos tabs, her friend list, and the discover page. Then the three this session added for her: gallery-manage.html, showing her gallery already full at eight of eight; overlay-gallery.html, a photo opened full-size with its description sitting underneath it; and export.html, the data-download page.

Before anything was explained, she started narrating — asking whose kids were in a thumbnail, noting there was nowhere to write who's standing next to whom, and going straight for the export button. "So where does the real copy of all this actually live?" she asked, before anyone had told her.

## 2. How WeeBee was explained

She got the full rundown. Getting in takes a one-time email code, good two weeks, eighteen or over only; invitations replenish. Nothing turns up in a search engine, and there's no way to search for people or posts. Friends must agree both ways and cap at three hundred; past that, it just says no. Posting means choosing: a short list of friends straight to their feed, or your own page for everyone, who only hear you posted. No share, forward or repost — you retype it yourself. Nothing is counted, ever. Reactions are six set phrases, seen only by you. The feed runs newest-first, nothing suggested, nothing ranked. Everything you write, and every picture, is gone for good at ninety days — ten posts can be pinned to survive that. New friends arrive only through someone you already know, one step, never further. Interests come from a fixed list, ten at most. There's no messaging, only a contact card shared item by item. One photo per post, described by you. It's a website, for people, nothing sold, nothing tracked.

## 3. Interview

**Interviewer:** You post something for your mother's eightieth birthday. What happens ninety-one days later?

**Susan:** Nothing, I'd think. I've got comments on my dad's memorial post a year later.

**Interviewer:** It's deleted — post, comments, reactions, the photo, permanently, at ninety days.

**Susan:** For my mother's eightieth? That's not archiving. That's tossing it before the thank-you cards go out.

**Interviewer:** You can pin ten posts to keep forever — but the comments and reactions underneath still vanish at ninety days, unmarked.

**Susan:** I keep the photo and lose Carol remembering that dress. That's keeping the cake and pitching the guest book.

**Interviewer:** A photo needs a real date later. Nothing shows one, only "about a year ago." How would you prove 1994?

**Susan:** I couldn't, not from the site. I'd write "Christmas 1994" in the description — but that's me saying it, not the site.

**Interviewer:** *[shows export.html]* There's a data export — the one place exact dates actually live.

**Susan:** That helps, if you think to download a file. My cousins will squint at the hat and argue about the year.

**Interviewer:** Your last reunion produced sixty photographs. What happens to those here?

**Susan:** I'd post a dozen — the group shot, the lake ones, Denise getting Frank to smile.

**Interviewer:** Each post carries one photo; the whole gallery holds eight, total, forever.

**Susan:** Eight? For my entire gallery? One weekend uses those up, let alone forty years of Christmases.

**Interviewer:** Could you tag your cousins in a lake photo, the way you'd label a print?

**Susan:** That's exactly what I do on prints. So how, here?

**Interviewer:** You can't. There's no way to tag or name a person anywhere on the site.

**Susan:** Then it's a picture with my guess written underneath, hoping someone reads it.

**Interviewer:** You've mentioned posting old photos captioned "this popped up in my memories today." Anything like that here?

**Susan:** No memories feature, I'd guess, from how you asked.

**Interviewer:** None — ruled out on purpose, not an oversight.

**Susan:** That stings — it's how I keep my mother's sister present.

## 4. What worked, and what was refused

What worked: nobody outside the family can see any of it, which matches her instinct already — this is family business, not a broadcast. The reactions being private, warm phrases rather than a running score suits her; nobody needs to "win" a funeral photo. Writing a description for every picture is no burden — she already narrates every photo she takes, out loud, to whoever's in the room.

What was refused: the deletion of everything not specifically rescued inside ninety days, which cuts against the entire reason she does this. A gallery capped at eight photographs total, when one weekend produces sixty. A pinned post that keeps her words but silently drops every comment underneath it, with no sign anything is missing. And no way, anywhere, to put a name to a face in a picture — the single thing she does most.

## 5. Predicted behaviour

She joins if a sibling or her sister-in-law sends the invite — family loyalty carries her past the sign-up screen. Week one, she loads the gallery to its cap of eight (GALLERY_MAX) from a single recent event and starts posting to her blog so the whole family sees things, not a picked list. Within a month she's pinned her ten allowed posts (PIN_LIMIT) — birthdays, the reunion, her mother's picture — and is already asking what happens to an eleventh. By month three she's watched a Christmas post and its comments vanish at ninety days (CONTENT_TTL_DAYS) and starts treating the export page as her real backup, downloading her own data the way she used to burn photo CDs. The friend cap of three hundred never troubles her; her list stays well under it. By month six she's still logged in, mostly to see what others posted, but has quietly gone back to keeping the actual family record the way she always did — on her own hard drive, in her own boxes.

## 6. How the other nine would receive this person

Provisional — this is a light guess from one-line descriptions only; A11 does the real comparison once all ten reports exist. Grandma Dorothy, who shares as an act of friendship, would react to nearly everything Susan posts, since there's no forward button for her to pass it along instead. Karen Commenter would find plenty to weigh in on under a disputed year or a misremembered cousin. Joe Blah would read every post and react to none of them, leaving Susan with no idea whether he ever looked. Mike, tracking thousands of loose connections, would likely let her carefully captioned photos scroll past unread with everyone else's.

## 7. Verdict

WeeBee doesn't want an archivist, and can't use one — it's built to forget on a schedule, and forgetting is the one thing her habit exists to prevent. Eight photographs, ninety days, and no way to name a face in a picture aren't friction for her; they contradict the job she's assigned herself. Susan doesn't want WeeBee as her record either — she'd keep the real archive where it already lives, at home, and treat this site, if she used it at all, as somewhere to say hello, not remember.

## Possible design findings

- Pinning (§7.6) preserves a post's words and image but silently drops every comment and reaction beneath it at ninety days (§7.5), with nothing marking that they once existed — an archival user experiences this as data loss, not a feature.
- GALLERY_MAX = 8 (§9.4) is small enough that a single family event can exceed a user's entire lifetime gallery in one afternoon.
- Person-tagging is absent everywhere (§17), leaving no way to record who appears in a photo beyond the free-text description — the exact task this archetype does most.
