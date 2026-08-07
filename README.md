# WeeBee — Design Documents

**Project version:** 1.19 · 2026-08-05 · DRAFT pending founder review
**This file last changed in:** 1.18 (the 90-day line now states the 30-day backup window)
**History:** see [CHANGELOG.md](CHANGELOG.md)

**WeeBee** (`weebee.social`) is a **small, private, deliberately anti-viral social network**. This repository holds its complete design documents. The platform has not been built yet — these documents come first, on purpose, so that the thinking is settled before the first line of code, when changes are cheapest.

**I am a solo founder: an IT professional, not a professional developer.** WeeBee will be built with AI coding assistance, following these documents step by step. That's why they are unusually explicit — they are written to be executable by AI models and readable by humans.

**On feedback:** I'm not running an open, public review process. I'll refine these documents in conversation with my AI assistant, and I may share them with a handful of friends who work in technology for a sanity check. If you're one of those friends: thank you — the sections below tell you where a sharp eye is worth the most. Blunt is welcome; "this will fail because X," with a concrete X, is the most useful sentence you can write me.

## What the project is (60 seconds)

The core thesis: the reshare/repost button is the original sin of social media. Once content can travel beyond the audience its author chose, virality exists — and virality is the mechanism that commercial and political manipulation exploits. **This platform has no concept of reach. Nothing can go viral.**

Concretely: invite-only membership (permanently), a hard cap of 300 friends, posts pushed to at most 30 hand-picked people, every post and comment auto-deleted after 90 days (and purged from the last encrypted backup within 30 days after that), no DMs (structured contact-card exchange instead), no likes or counters of any kind, no algorithmic feed, no tracking of any kind, no ads, no API. Friend discovery works only through mutual friends and shared interests — never beyond friends-of-friends. One server, one database, server-rendered pages, everything self-hosted except outbound email.

**On the 90 days, precisely:** what expires is what you *say*. What you *are* — your profile photo, your bio, your gallery of eight pictures — stays until you change it. **Statements expire; descriptions do not** (SPEC §9.7). The one deliberate exception on the other side is a pinned post: up to ten, kept for as long as you keep them pinned, which is the only act of preservation the platform offers. And one honest caveat in the other direction: deletion is immediate and permanent in the live system, but nightly encrypted backups exist, so a deleted thing survives there until the backup ages out — **30 days at most** (SPEC §7.5, §4.7). Claiming instantaneous total erasure while running backups would be a lie; the documents say the true thing instead.

## What is NOT up for review

The **product philosophy is decided.** I know invite-only limits growth, that people love DMs, that 90-day expiry is radical, and that no-virality means no explosive adoption. These are the bets the project exists to make. Comments arguing the vision will be read with interest but won't change it — please don't spend your effort there.

Also decided: the rejection of blockchain/federation (AT Protocol), the 18+ rule, the tracking ban, and **WCAG 2.1 Level AA conformance** (SPEC §16) — an invite-only network of real friends and family cannot have a door some of them can't open. *How* to hit AA is very much open to review; *whether* is not.

## What IS up for review

### 1. The values of the caps and constants — explicitly open

The *existence* of hard caps is philosophy; the **numbers are honest judgment calls**, and I want them stress-tested (see SPEC §14 for the full table). For example:

- Friend cap **300** — too generous? too tight?
- Post audience / group size **30**
- Post and comment lifetime **90 days** (sticky in both directions once live — lowering it later deletes content people expected to keep, raising it outlives authors' expectations)
- Invite budget: **5 banked max, +1/month, new accounts start with 2** — is this the right growth throttle?
- Display-name change cooldown **90 days**, with 90 days of "NewName (formerly OldName)" dual display
- Pinned posts **10**, gallery images **8**, profile hashtags **10**, contact-card items **12**

If you've run a community or a service: which of these numbers will I regret, and in which direction? (Note: caps are raise-only by design — they can go up later, never down.)

### 2. SPEC.md — the product specification (read first)

The single authoritative description of every feature's behavior. Looking for:

- **Internal contradictions** — two sections that can't both be true.
- **Abuse vectors** — ways a bad actor works within these rules to harass, spam, stalk, or scrape. The permission model (friends / friends-of-friends / hashtag gates / blocks) is the heart; holes in it are the highest-value findings.
- **Missing edge cases** — states or transitions the spec doesn't define.
- **GDPR/privacy gaps** — the design aims to be GDPR-compatible (minimal collection, guaranteed erasure, export).
- **Accessibility (§16)** — where does this design fight WCAG 2.1 AA? The known tension is the preformatted/monospace post (§7.2.1), which deliberately scrolls horizontally under the 1.4.10 two-dimensional-layout exemption. If you use a screen reader, magnification, or keyboard-only navigation, your reading of §16 is the most valuable review this project can get.

### 3. ARCHITECTURE.md — the technology plan

Server-rendered Django monolith + PostgreSQL + Caddy in Docker on a single VPS; no CDN; every image served through permission checks; one central "visibility engine" module for all permission decisions. Looking for:

- **Will this hold?** What breaks first when 500 real people use it daily?
- **Security assumptions that are weaker than they look.**
- **Django-specific sharp edges** the plan walks into.
- **Ops gaps** — what does a person who has carried a pager know that this plan forgot? (Monitoring, alerting, failure recovery, the 2 a.m. scenarios.)

Before commenting "why not [other stack]": §14 has an alternatives-considered table. New arguments welcome; restatements of the ones already weighed are not.

### 4. BUILD_PLAN.md — the step-by-step construction plan

17 phases, each step labeled [FOUNDER] (I do it myself) or [AI] (an AI model codes it, I verify), each ending with a "done when" check. Looking for:

- **Sequencing errors** — steps that need something built later.
- **Missing steps** entirely.
- **Where does a solo non-developer most likely get stuck?**
- **Are the verifications adequate?** Each one is the only quality gate before the next step.

## How to give feedback (for the few I share this with)

- **However is easiest for you** — a message, a note, a marked-up copy. Please reference the document and section number (e.g., "SPEC §10.3") so I can find what you mean.
- **Please don't send pull requests.** These documents change only through a versioned design process on my side; every accepted change gets a version bump and an entry in [CHANGELOG.md](CHANGELOG.md), and every rejected suggestion gets its reasons recorded in-document (see SPEC §4.5's rejected-uniqueness entry for the format). The versioned record is the point.
- Blunt is fine. "This will fail because X" with a concrete X is the most useful sentence you can write me.

## The plan from here

Refine the documents to the point where they can be built, then build WeeBee — solo, with AI assistance, following BUILD_PLAN.md. If the core ideas have merit and it gets built and working, it either finds its small audience or the ideas get picked up by others. Either is a good outcome.
