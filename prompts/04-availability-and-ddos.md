# Prompt 04 — Availability, monitoring, and the 2 a.m. scenarios

> **Run in a fresh session.** Paste everything below the line.
> **Touches:** ARCHITECTURE.md §7 (probably a new section), BUILD_PLAN.md §5 and §17.3
> **Depends on:** prompt 01.
> **Expected outcome:** the project gains an operational posture it does not currently have.

---

You are working in the WeeBee design-document repository. Read `README.md`, then
`ARCHITECTURE.md` in full, then `BUILD_PLAN.md` Phases 5, 16 and 17. This is a
**founder-directed design session**; you may edit both documents.

## The finding, and how it grew

An external reviewer of version 1.16 flagged the ban on decrypting proxies as a security
risk:

> This means you're exposing your VPS directly to the internet with no DDoS protection
> layer… A DDoS attack could take you offline for hours or days, and you have no
> mitigation plan.

**That specific claim is wrong, and the document already answers it.** ARCHITECTURE §13.3
distinguishes network-level scrubbing (no decryption, fully compatible with the TLS rule,
included by Hetzner-class providers, handles the overwhelming majority of attacks) from
application-level filtering (requires decryption, is what orange-cloud mode is, and is the
only thing knowingly given up). The reasoning is sound and does not need revisiting.

**But checking it surfaced something larger.** §13.3 is inside "How This Survives 'Public
Later'" — the *scaling* chapter, written about a platform with staff. ARCHITECTURE §7,
the security posture for the platform actually being built, covers what protects data and
says nothing at all about what keeps the service running. And a search of all four
documents for monitoring, alerting, uptime checks or health checks returns **nothing**.

The founder's own README asks for exactly this: *"what does a person who has carried a
pager know that this plan forgot? (Monitoring, alerting, failure recovery, the 2 a.m.
scenarios.)"* Neither reviewer answered it. This session should.

## The failure that matters most

Most outages on a prototype for friends are survivable — the site is down, someone
mentions it, the founder restarts a container. One class is not, and it is silent:

**If a cron job stops running, nothing tells anyone.** ARCHITECTURE §6 puts content expiry
(SPEC §7.5, the 90-day promise), inactivity warnings and deletions (§4.8), invite
replenishment (§4.2), and notification expiry in cron. A failing expiry sweep does not
produce an error page or a user complaint. It produces a database quietly retaining
content the platform promised to destroy — the central promise of the project, broken
invisibly, discovered whenever someone next looks.

The same shape applies to the nightly backup. BUILD_PLAN §17.3 has the founder check "the
backup job's last-success" in a weekly routine, which means a failure can go unnoticed for
up to seven days, and only if the routine is actually performed that week.

## What to work out with the founder

1. **A short availability section in ARCHITECTURE §7 (or its own section).** What the
   platform does when the machine, the database, the email provider, or a job fails. This
   is the deliverable; the items below are its contents.

2. **Job failure must be loud.** Decide the mechanism. Cheapest honest option: every
   housekeeping job records a last-success timestamp and a result, and a daily check emails
   the operator when any job has not succeeded within its expected window. Note the
   circularity — the alarm goes out over the same email provider that might be the thing
   that failed — and decide whether that matters at this size. It probably does not, but
   it should be a decision rather than an oversight.

3. **An external uptime check.** A third-party service pinging a health endpoint every few
   minutes is the standard answer and costs nothing at this scale. It needs care here:
   SPEC §15.2 bans tracking absolutely and ARCHITECTURE §7 bans third-party requests *from
   pages*. An external monitor requesting an unauthenticated health URL is neither — no
   user is involved and no page loads anything — but the distinction must be written down,
   or a later reader will read it as a violation. Define what the health endpoint may
   expose: it must not be an oracle for whether the platform exists, has users, or is
   reachable in any way that leaks state. Recommend a specific service and endpoint shape.

4. **Disk.** Images live on the server's filesystem (§3, §4). Nothing bounds total storage
   — `IMAGE_UPLOAD_MAX_MB` = 20 per image, `GALLERY_MAX` = 8 per user, times a growing
   user base, and gallery images never expire (SPEC §9.7: descriptions do not expire). A
   full disk stops Postgres and takes the site down hard. Decide: a disk-usage alert
   threshold, and whether the growth arithmetic belongs in §11's cost section.

5. **What the founder actually does at 2 a.m.** BUILD_PLAN §17.3 already commissions an
   operator runbook as the final Phase-17 task. Specify its contents here rather than
   leaving it to a future session's judgment: how to tell what broke, how to restart the
   stack, how to restore from backup, how to put up a maintenance page, and — the one
   people forget — how to tell the difference between "the site is down" and "the site is
   up and one job is silently dead."

6. **The DDoS paragraph, promoted.** §13.3's reasoning is correct but lives in the
   scaling chapter, so a reader of §7 never meets it. Move or summarize it into the v1
   security posture, and state the v1 answer plainly: what the chosen VPS provider
   actually includes, what the founder does if it happens anyway, and the honest
   acknowledgement that a determined attack against a prototype for friends is survivable
   downtime rather than a catastrophe. Keeping this short is a virtue — the point is that
   §7 stops being silent, not that the project acquires an incident-response programme.

7. **Where BUILD_PLAN gains steps.** Likely §5 (set up monitoring alongside the first
   deploy, while the founder is already in server-configuration mode) and §17.3 (the
   runbook contents). Prefer folding into existing phases over adding new ones — that is
   how every prior sync was done. Note anything ambiguous for prompt 09 rather than
   editing BUILD_PLAN speculatively.

## Constraints to respect

- **Proportion.** This is one server serving friends, run by one person with a day job.
  The goal is that silent failures become loud, not that the project acquires Prometheus,
  Grafana and an on-call rotation. If a proposal would take more than an afternoon to set
  up, argue for it explicitly or drop it.
- **The TLS rule is not up for review.** "TLS may terminate only on machines this project
  administers" is a settled principle (§13.3). Nothing here reopens it.
- **No new dependency without saying so.** ARCHITECTURE §3 is the stack. An external
  monitoring service is not a code dependency, but naming it makes it a processor that the
  privacy policy (BUILD_PLAN §15.1) must list. Flag that consequence.

## Before you finish

- Write the CHANGELOG.md entry, naming every file's status including unchanged ones.
- Update `TODO.md`.
- If the monitoring discussion turns into a build-tooling project, stop and split it out.
