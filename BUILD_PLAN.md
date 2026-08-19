# Build Plan — WeeBee

**Project version:** 1.26 · 2026-08-18 · DRAFT — not yet founder-approved
**This file last changed in:** 1.24 (a citations line in the header, and an Appendix lead-in stating that this document defines no rule of its own)
**History:** see [CHANGELOG.md](CHANGELOG.md)
**Companion to:** SPEC.md v1.15 (§7.5.1, §7.8, §9.4, §12) and ARCHITECTURE.md v1.7 (§3.8, §4, §7). This is deliverable (c) per SPEC §18. The actual AI-coding prompts are deliverable (d); every `[AI]` step below will have a matching numbered prompt there.
**Citations:** `SPEC §x` and `ARCHITECTURE §x` name another document; a bare **§x** is a section of *this* one and `Step x.y` is a step of it. **This document defines no rule of its own** — every rule below is SPEC's or ARCHITECTURE's, cited to its owner (SPEC §18).
**Audience:** The founder, and the AI coding models that will execute the `[AI]` steps.

---

## 0. How to Read and Use This Plan

### 0.1 Step labels

- **[FOUNDER]** — you do this yourself, outside any AI chat: account signups, DNS settings, running commands on the server, plugging in credit cards. Exact instructions are given inline.
- **[AI]** — an AI coding model does this, driven by the matching prompt from deliverable (d). Your job on these steps is to run the prompt, skim the result, run the verification, and commit.
- **[FOUNDER+AI]** — collaborative: the AI drafts, you decide (e.g., the privacy policy, the reaction phrases).
- **[FOUNDER + TESTER]** *(v1.22)* — you plus a qualified accessibility tester who is not you (SPEC §16.5.1). **This label appears exactly once, at Step 16.5**, and it exists because those passes are a skill rather than a setting. You are present for all of it: the tester finds the defects, and you are the one who has to fix them and who owns what the accessibility statement then claims.

### 0.2 The working rhythm (read this twice — it is the plan's real safety mechanism)

1. **One step at a time, in order.** Steps are sequenced so that everything a step needs already exists. Skipping ahead is how AI-built projects rot.
2. **Every step ends with a verification.** Do it. If it fails, do not proceed — tell the AI model what you saw and let it fix the step. "It probably works" is not a state this project recognizes.
3. **Commit to git after every completed step**, with the step number in the message (e.g., `Step 6.2: feed post composer`). This makes every AI mistake reversible with one command, which is your insurance against a less capable model damaging working code. **Before committing, glance at the changed-file names** (`git status`) — SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md, CHANGELOG.md and `constants.py` must never appear in that list unless you personally ordered the change. You are reading filenames, not code; it takes five seconds and no law file can change without leaving its name there. **A step that did not finish is not committed** (§0.7): if the AI stopped, revert the working tree and leave the last good commit as the last good commit.
4. **Fresh chat per step (or small group of related steps).** Long AI chats degrade; the prompts in deliverable (d) are written to be self-contained so a new chat loses nothing.
5. **The AI never edits a law file. There are five of them (v1.23):** SPEC.md, ARCHITECTURE.md, this file, **CHANGELOG.md**, and the values in `constants.py`. **This is the list**, and every other place that names it — rule 3's filename glance above, Step 1.2's copy instruction, Step 2.4's guards — means this one. *CHANGELOG.md joined it in v1.23* because it did not exist when the list was first written and is now the file that makes an unsynced document **visible**: a changelog quietly rewritten to say ARCHITECTURE had been synced when it had not would defeat the whole mechanism 1.17 was built to create. A build step that wants to change the changelog is, by definition, a design conversation.
   If a step seems to require changing any of them, **stop and write the stop note of §0.7** — that's a design conversation, not a coding task, and §0.7 says what the note contains, where it goes, how you check it in thirty seconds, and how the build resumes afterwards. Until v1.23 this rule ended at "stop," and nothing described the other side of the stop; on a project where you are not the coder, **the handoff is the mechanism.**
   This rule is enforced by mechanism, not obedience: Step 2.4 installs tool-level deny rules, a git pre-commit hook, and a tripwire test over both the constants and the documents' checksums, and rule 3's filename glance is the human backstop. A prompt is a request; **the deny rules are the lock, and the other two make a bypass loud rather than invisible** — Step 2.4 says plainly which is which, and (v1.23) which of them still exists after you change AI tools, because presenting them as equivalent layers would overstate two of them.
   **Two events that look alike and are not (v1.23).** An AI that *reports it could not edit one of these files* **tried, and was refused** — a deny rule fired, the hook rejected a commit, the tripwire went red. That is the lock working, and it is now also a rule violation, because the instruction is to stop and write a note rather than to attempt the edit. An AI that produces a **stop note** did not try: that is the plan working. Earlier versions of this rule read every refusal as evidence "the model wanted to move a goalpost"; the two cases deserve different reactions and §0.7 tells them apart.
   **When *you* change a law file** in a design conversation, the checksum tripwire fails at the very next step and tells you to re-bless it — one `shasum` command, spelled out in Step 2.4. That failure is not a fault; it is the guard confirming the change was yours, and it is also the only reminder you need to carry. Re-blessing is the second of the three acts that put the build back on its feet after a design session; §0.7's closing paragraph has all three, including the one this plan had never written down.
6. **When stuck:** paste the exact error text and what you did into the chat. If two fix attempts fail, revert to the last commit (`git checkout .`) and re-run the step's prompt in a fresh chat, telling it what failed last time. This recovers from most AI dead ends.

### 0.3 Rough effort expectations

Phases 1–5 (skeleton to first deploy) are the steep part — expect several sessions of evenings/weekends. Phases 6–14 are repetitive feature work at a rhythm you'll have learned. There is no calendar deadline; the sequence protects you, not a schedule.

**One step depends on somebody else's calendar rather than yours (v1.22):** Step 15.3, lining up the accessibility tester who runs Step 16.5's human passes. It is the only place in this plan where you can be *waiting* rather than working, which is why it is a step of its own and why it tells you to start looking during Phase 13.

### 0.4 The standing verification matrix — browsers and widths (v1.18)

Wherever a verification below says "in a browser," this is the list. It is stated once here so that twenty steps need not repeat it, and it is deliberately short: this is a prototype for friends, not a compatibility programme.

- **Browsers:** Safari on macOS · Safari on iOS · Chrome · Firefox. That is three rendering engines, which is all there are. iOS Safari earns its own line because every iPhone user is on it whatever browser they believe they installed.
- **Widths:** 320 · 375 · 768 · 1024 px. **320 px is not decoration** — SPEC §16.3 requires the layout to reflow there with no sideways scrolling, and that requirement is live from the first page that has a layout, not from the audit at Step 16.5.

**The cadence, kept cheap:** an individual step's verification runs wherever you already are — one browser, one width. **At each phase milestone** (the ✅ lines marked *Phase milestone*), re-run that milestone's check across the whole matrix. Dragging a desktop window narrow covers the widths; your phone covers iOS Safari. A cell that fails is a bug in the step that built it, not a browser to drop from the list.

### 0.5 The standing accessibility checks (v1.22)

SPEC §16.5 puts conformance on three clocks rather than one pre-launch gate. Two of them live here, stated once so that twenty steps need not repeat them; the third is the human passes of Step 16.5, and those are not yours to run.

- **Continuous, automatic, every step:** the `THEME_SET` **contrast test** (Step 8.2) and the **template smoke tests** (Step 2.5). Ordinary tests in the suite, running beside everything else. **Nothing about them is a Phase 16 activity** — by the time the audit runs they should have been green for months, and a step that turns one red is a broken step, not a note for later.
- **At each phase milestone, in the same sitting as the §0.4 browser matrix:** the **axe/`pa11y` scan** against your locally running instance. One documented command, written down at Step 2.5 when the first real pages exist. It is a tool on your Mac — never in `requirements.txt`, never in the app image, never in the test suite (ARCHITECTURE §9). It finds perhaps a third of real problems, which is exactly why it belongs on a repeating cadence instead of in one pre-launch sitting.
- **Periodic, and not yours:** the three human passes of Step 16.5 — plus the operator-console hour that rides along with them (SPEC §16.1.1) — run by the tester you book at Step 15.3, at launch and afterwards whenever SPEC §16.5's re-audit triggers fire.

**Why this section exists at all.** Until v1.22 every accessibility check in this plan sat inside Step 16.5, which made conformance a thing verified once, the week before launch, and never again — while SPEC §17 promises the platform keeps growing afterwards. The checks were mostly already written; what was missing was a *cadence* for them, and a build step for the smoke tests, which this plan had specified nowhere.

### 0.6 The standing conformance check (v1.23)

Step 2.4's guards stop the AI editing the documents. **Nothing stops it writing code the documents never asked for** — and that is the larger risk, because every step-level verification tests *the feature that was just built*, not whether that feature is the one SPEC describes. A reviewer of 1.16 put it bluntly — *"the AI will generate code that violates the spec, and you'll have to manually fix it"* — and was right that nothing here covered it, and wrong that nothing *could*.

You cannot read the code. What you can read is **a list of section numbers**, and that is the whole of this check.

**At each phase milestone, in the same sitting as §0.4's browser matrix and §0.5's scan**, ask the AI for two lists and read them side by side:

- **A — every SPEC and ARCHITECTURE section number named by this phase's steps** in this plan. They are in the step text above; you can read them off the page yourself if you would rather not trust the list you were handed.
- **B — every SPEC and ARCHITECTURE section number cited by the tests written in this phase.** Appendix rule 4 requires every test to name the section it enforces, which is the only reason this list can exist.

**A section that is in A and not in B is the finding.** Ask for the test, or for the reason there isn't one — some sections are argument rather than rule, and *"no test, because §1.2 is a philosophical claim with nothing to assert"* is a good answer you should accept. A section in B and not in A is normal and means nothing: tests cite earlier phases constantly.

This is **Step 4.2's pattern generalized**, and 4.2 stays as it is — reading the visibility engine's test *names* top to bottom is a deeper read than this one and that phase deserves it. Everywhere else, matching two columns of section numbers is what a non-developer can actually do at 10 p.m., and it is the only conformance check in this plan that scales to seventeen phases.

**Be exact about what this does not catch**, because an overstated guard is worse than a stated limit:

- **A test that cites the right section and asserts the wrong thing.** The name reads correctly, the citation is real, the assertion is weaker than the rule. This check cannot see it, and neither can you. **Nothing in this plan catches it.** That is the honest residue of the whole law-file scheme, and it is written here rather than left for you to discover.
- **Behaviour the code has that no document mentions.** Extra is not missing; it opens no gap in either column.
- **A rule implemented correctly in the test's world and wrong on the actual page.** That one is partly covered elsewhere — every step's ✅ is a behavioural check you run by hand, the milestone re-runs it across §0.4's matrix, and your first users are the last line (ARCHITECTURE §9).

What the check *does* prove is that **every section this phase was supposed to implement was thought about by name**, which is the failure mode that actually happens: a clause gets no code and therefore no test, and nothing anywhere goes red.

### 0.7 Two kinds of session, and the one route between them (v1.23)

This project runs two kinds of AI session, with opposite rules about the same files.

- **Build sessions** — a step from this plan, run in the build repository (`thenetwork`). **The five law files are locked** (§0.2 rule 5) by the mechanisms of Step 2.4.
- **Design sessions** — a conversation *you* open, in the design-document repository, for the purpose of changing one of those files. There is no lock, because you are the one directing the change. Every version this project has ever had came out of one.

Until v1.23 this plan described only the first. The second had been running for twenty-two versions and was written down nowhere a build session would ever read it — which is why every design prompt has had to declare its own exemption in its opening paragraph. **It does not need to be a mode you switch on.** You are the switch: a session is a design session because you opened it as one. What was genuinely missing was not a mode but a **route into one from a build session**, and that route is a single artifact.

#### The stop note

When a step cannot be done as written, the AI **stops and prints exactly this, and nothing else**:

```
STOP — Step 6.2

The sentence in the way:
  SPEC §7.4: "<verbatim quote, copied not paraphrased>"
  — or —
  No sentence: SPEC does not cover <the case>. It would belong in §7.4.

What I could not do:
  <one or two sentences>

Smallest change that would resolve it:
  <a proposal, never applied>

State of the working tree:
  Nothing committed. <files touched — or "no files touched">
```

Five fields, under a screen, readable at 10 p.m. by someone who has already had a long day. Three rules go with it:

- **A proposal is never applied and never committed.** It is text in a chat. This is the whole of "Design Review Mode": the AI may *propose* a document change at any time, and may never make one.
- **A stopped step is not committed** (§0.2 rule 3). Revert the working tree. Reverting throws away real work, and it is still right: the design answer may change what that work should have been, the step gets re-run from its prompt anyway, and a half-built tree nobody can characterise is far worse for you than five minutes of re-generated code.
- **The AI writes no files.** Not into `prompts/`, not into `TODO.md` — those live in the *other* repository, and a session that has just stopped is the last one that should be creating artifacts.

#### Where it goes

1. **The AI prints the note and stops.** You are already there: §0.2 rule 2 has you running the step's verification.
2. **You paste it into `TODO.md`'s stopped-steps table**, with the date. Thirty seconds, and it is the act that turns "the AI stopped" into a queued design conversation instead of a dead end.
3. **When you get to it, you open a design session by pasting the note.** The note is already self-contained — step, sentence, wall, proposal — which is the shape `prompts/README.md` asks of a prompt file, in miniature. **Write a full prompt file only if the question turns out to be bigger than the note**, which is the exception rather than the rule.

That this repository grew a `prompts/` folder and a `TODO.md` at all is the proof the route was missing: there was no defined way to get a document question out of a working session, so one was invented on the spot. This section is that invention, written down and made smaller.

#### Checking a stop note in thirty seconds

A model saying *"this contradicts SPEC §7.4"* is the system working. A model saying *"I can't do this"* because it is confused, or because it has found an easier design it likes better, looks identical from where you are sitting. The test is the quote, and it works because of one property:

> **A stop note must be falsifiable by reading one named place in one named document.**

Search for the quoted sentence. Four outcomes, and you need no code and no judgment for any of them:

- **Found, and it says what the note says it says** → real. This is a design conversation.
- **Not found** → the model did not read; it guessed, and dressed the guess as a citation. **Not a stop.** Re-run the step in a fresh chat (§0.2 rule 6).
- **Found, but in context it means something else** → one paragraph of reading tells you. Not a stop.
- **A "no sentence" note** → read the section it names. If that section *does* cover the case, the model missed it: not a stop. If the section is genuinely silent, that is a real gap — and **gaps are the commonest true stop**, far more common than contradictions.

**What this test is, and what it is not.** It does not tell you whether the model was confused, tired or angling for an easier design; nothing can, from the outside. What it does is convert an unanswerable question — *is this model being straight with me* — into an answerable one: **is there a sentence, and does it say that.** And if the conflict is real, the motive stops mattering. A verbatim quote is cheap to check and expensive to fake, which is all a test at 10 p.m. needs to be.

#### What a stop note resolves into

Four things. The design session decides which:

1. **A change to SPEC or ARCHITECTURE** — the ordinary case. Version bump, CHANGELOG entry, then resume below.
2. **A new build step** — the discovery loop, next.
3. **A corrected prompt** — the documents were right and deliverable (d)'s prompt for that step was wrong. Fix the prompt; **no version bump**, because no law file changed.
4. **Nothing at all** — the model was confused and the quote did not survive the check. Re-run the step.

#### The discovery loop — a step found missing mid-build

A reviewer's objection worth taking seriously: this plan assumes everything needed at step 12 is known at step 1, and in practice you discover missing steps as you build. The rule:

- **Insert with a letter, at the point of need** — Step 6.2a, the way this plan already did it once. **Never renumber.** Renumbering would falsify every git commit message (`Step 6.2: feed post composer`), every CHANGELOG reference and every prompt filename, and those are *history*, not text you are free to correct. Appending to the end of the phase is available where genuinely nothing depends on the new step, which is the rarer case: a step that turns out to be missing is usually missing *before* something, not after it.
- **Letters do not nest.** 6.2a, 6.2b — never 6.2a.1. If you find yourself wanting that, you wanted a phase.
- **You write it into this file, not the AI.** This plan is a law file and the discovery loop makes no exception to §0.2 rule 5.
- **It gets its own ✅.** Every step here ends in a verification, and a step you cannot write one for is not a step — it is a design question that has not finished being answered. That is a free test of whether the insertion is ready to be made.
- **Re-run the preceding step's verification** once the new step is built. The new step almost certainly touched what the old one made, and that old ✅ is the only evidence it still holds.

#### How the build resumes

**When a design session has changed a law file, three acts put the build back on its feet — and until v1.23 this plan named only the second of them:**

1. **Copy the changed files from the design repository into the build repository.** Step 1.2 put them there once, at the very beginning, and nothing anywhere told you to carry them across again. A build session reading a SPEC three versions stale is precisely the failure the rest of this section exists to prevent, and it would look exactly like everything working.
2. **Re-bless the checksums** — the one `shasum` command in Step 2.4. You do not have to remember this one; the tripwire fails at the next step and asks for it by name.
3. **Commit both together, with `--no-verify`.** Guard 2 will refuse the commit, by design, and passing that flag yourself is the deliberate founder act guard 2 exists to require (Step 2.4).

Then **re-run the stopped step from its prompt, in a fresh chat**, against the documents as they now read. Mark the `TODO.md` row done.

---

## Phase 1 — Your Machine [FOUNDER]

Everything here happens on your Mac.

**1.1 [FOUNDER] Install the tools.**
1. Install **Docker Desktop for Mac** from docker.com (the free Personal tier). Launch it once so it finishes setup.
2. Verify **git** is present: open Terminal, run `git --version`. If macOS offers to install command-line developer tools, accept.
3. Install your AI coding tool (e.g., **Claude Code**: `npm install -g @anthropic-ai/claude-code` after installing Node.js from nodejs.org, or the desktop app). Any capable coding agent works with the deliverable-(d) prompts.
✅ *Done when:* `docker --version` and `git --version` both print versions in Terminal.

**1.2 [FOUNDER] Create the project folder and repository.**
1. In Terminal: `mkdir ~/thenetwork && cd ~/thenetwork && git init`
2. Copy SPEC.md, ARCHITECTURE.md, CHANGELOG.md and this file into it — **four documents (v1.23)**; they are the project's law and must travel with the code. CHANGELOG.md joins them because it is a law file (§0.2 rule 5) and because a build repository without one invites an AI to create a rival changelog of its own (Step 2.4). **This is not a one-time copy:** every design session that changes one of them means carrying the changed file across again, which is act 1 of the three in §0.7.
3. On github.com, create a **private** repository named `thenetwork`. Follow GitHub's shown commands to connect and push. (Code only, ever — never data, never secrets. Step 2.4's `.gitignore` enforces this.)
✅ *Done when:* the four documents are visible in the private GitHub repo.

**1.3 [FOUNDER] Register the domain. — ✅ DONE (2026-07-25)**
The domain is **`weebee.social`**, registered at **Porkbun**. The platform name is **WeeBee** (SPEC §2). No defensive/typo domains are being registered — this is a settled decision (SPEC §4.6.1). Remaining reminder for the DNS steps below (Phase 5):
- **Do not put the domain behind Cloudflare's proxy service** now or later. Cloudflare-the-registrar/DNS is fine, but its orange-cloud "proxy" mode would terminate HTTPS at Cloudflare, meaning a third party decrypts all user traffic — a violation of the privacy architecture (ARCHITECTURE §2, Decision 2). DNS-only, always. (Porkbun's own DNS is DNS-only by default, so simply using Porkbun's nameservers satisfies this.)
✅ *Done when:* ~~you own the domain and can see its DNS management page.~~ **Met — `weebee.social` owned, Porkbun DNS panel accessible.**

---

## Phase 2 — Skeleton Application [AI]

Goal: an empty but *running* Django site in Docker on your Mac.

**2.1 [AI] Project scaffold.** Django (current LTS) project + Docker Compose with three services (`app` via Gunicorn, `db` PostgreSQL 16, `caddy`), per ARCHITECTURE §3.4. A single placeholder page.
✅ `docker compose up` then http://localhost shows the placeholder.

**2.2 [AI] `constants.py`.** Every SPEC §14 constant, named exactly as in SPEC, each with a comment citing its SPEC section and the raise-only rule.
✅ You read the file side-by-side with SPEC §14 and every row matches.

**2.3 [AI] Custom user model.** UUID primary key; login email as unique credential; display name plus previous-name and name-changed-date fields (SPEC §4.5.1); the lifecycle fields from ARCHITECTURE §4 (last-login, deactivation state, invite budget fields). Includes the **single shared name-render helper** ("Name" or "Name (formerly Old)" during a transition) that every later template must use — names are never rendered any other way. Done **before anything else touches the database** — retrofitting a Django user model later is notoriously painful.

Build the **shared time-rendering helper** here too (SPEC §7.5.1, ARCHITECTURE §4), for the same reason the name helper is built here: it must exist before any surface can print a date, or surfaces will each grow their own. It takes a timestamp and returns one phrase from the 40-row ladder — "Just now", "A few hours ago", "Over a week ago" — and it **returns the phrase and nothing else**: no `title` attribute, no `<time datetime="…">`, no data attribute carrying the real timestamp. The two absolute-time cases (the expiry countdown, and account/security events) are separate formatters, not options on this one.
✅ AI-written model tests pass (including the helper's formerly-window arithmetic); you can create a user via Django admin. **The time helper's boundary table test passes**: one case per ladder row at its boundary and one unit either side, plus a totality test sweeping a wide range of ages and asserting every one returns a non-empty phrase. That totality test is the point — a gap between two bounds renders an empty string, which no feature test would ever catch and no user would report as anything more useful than "sometimes there's no date."

**2.4 [AI] Housekeeping files and the law-file guards.** `.gitignore` (secrets, environment files, images, database volumes — with comments saying why), an environment-file template, a README pointing at the four law documents. Plus the three mechanical guards enforcing §0.2 rule 5 (the AI never edits the law files). **They are not equivalent layers, and v1.18 stops implying they are** — each one's actual strength is stated, because a guard you overestimate is worse than one you know the limits of:
1. **Tool deny rules** — the AI coding tool's permission settings file (e.g., Claude Code's `.claude/settings.json`) refusing edits to the five law files of §0.2 rule 5: SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md, **CHANGELOG.md** and `constants.py`. **This is the strong guard:** the harness refuses the edit before the model's decision enters into it. Its limit is that it is per-tool — a different AI tool, a web interface, a manual paste, or a shell command issued from inside the tool itself, is outside its reach.
2. **A git pre-commit hook** — a small script git runs before accepting any commit, refusing any commit that touches a law file. **This one stops accidents, not determination:** `git commit --no-verify` skips it entirely, and an agent that can run shell commands can pass that flag. Worth having, because the accidental case is the common case. Not to be counted as a lock. **Keep the script in the repository** (say, `hooks/pre-commit`) and install it with one copy command recorded in the README, because `.git/hooks/` is **not** part of what git clones: a fresh clone on a new machine has no hook at all, and nothing announces its absence.
3. **A tripwire test** — a tiny test file with two assertions. First, **every SPEC §14 constant's exact value** (`FRIEND_CAP` is 300, `CONTENT_TTL_DAYS` is 90, …). Second, the **SHA-256 checksum of each law document** — SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md, CHANGELOG.md — compared against `law_files.sha256`, a small committed file you bless by hand. **This is the loud one:** it prevents nothing and hides nothing. Tests run at every step, so an edit that got past guards 1 and 2 fails at the next step, naming the file, instead of surfacing at launch. The failure messages are the entire point, and **the two assertions must fail differently, because they mean different things** (v1.23): a checksum failure says *a document changed* and is expected after every design session; a constants failure says *`constants.py` changed* and is expected only during the deliberate sequence below. They must read like this:

   ```
   SPEC.md no longer matches the blessed checksum in law_files.sha256.

   If you changed it deliberately (a design conversation), re-bless it:
       shasum -a 256 SPEC.md ARCHITECTURE.md BUILD_PLAN.md CHANGELOG.md > law_files.sha256
   then commit law_files.sha256 together with the document change.

   If you did NOT change it, an AI edit got through. Inspect it:
       git diff SPEC.md
   ```

   ```
   constants.py: FRIEND_CAP is 400. SPEC §14 says 300.

   If you raised this cap deliberately, the order is SPEC first (BUILD_PLAN §2.4):
       1. SPEC §14           (a design conversation)
       2. constants.py
       3. this test's expected value
       4. re-bless the checksums
   ...all in one commit of your own, with --no-verify.

   If you did NOT change it, an AI edit got through. Inspect it:
       git diff constants.py
   ```

**Re-blessing, in full — the only thing you ever do by hand here.** After a design conversation changes a law document: from the project folder, run the one `shasum` command above, and commit the updated `law_files.sha256` alongside the changed document. It takes one line and needs no judgment. Two things to know so neither surprises you: **the test tells you when it is needed**, so there is nothing to remember or diarize; and **guard 2 will refuse that commit**, by design — pass `--no-verify` yourself, deliberately, which is precisely the founder act guard 2 exists to require. An AI passing that flag is a bypass; you passing it is the mechanism working. Re-blessing is act 2 of the three that resume the build after a design session; §0.7's closing paragraph carries all three, and act 1 — carrying the changed document across from the design repository — is the one this plan used to leave unsaid.

**Raising a cap: the expected failure, in order (v1.23).** SPEC §1.3 permits caps to be raised and never lowered, so *the correct act of raising `FRIEND_CAP` makes the test suite go red* — and the fix, editing the tripwire's expected value, is the exact action the guard exists to make you suspicious of. Two facts make this navigable rather than alarming. First, **there are three copies of every constant**, not one: SPEC §14, `constants.py`, and the tripwire's assertion. They are three on purpose — a tripwire that read SPEC's table would agree with SPEC by construction and would therefore assert nothing about it; the third copy is worth having precisely because a human wrote it down at a moment when the number was confirmed. Second, three copies must move **in one direction, in one sitting**:

1. **SPEC §14 first**, in a design session. Nothing is a constant change until SPEC says so.
2. **`constants.py`** to match — your edit, never an AI's (§0.2 rule 5).
3. **The tripwire's expected value** to match.
4. **Re-bless the checksums**, since SPEC.md changed.

**All four in one commit, authored by you, with `--no-verify`.** And the rule that gives the guard its teeth back: **a constants assertion that fails at any other time is a real alarm** — it means `constants.py` moved without SPEC moving first, which is the one thing this test exists to catch.

**Which guard survives a change of tool (v1.23).** Say this plainly, because relying on a lock that quietly stopped applying is worse than knowing you have none:

- **Guard 1 does not survive.** The deny rules live in one tool's settings file. Switch AI tools, use a web interface, or paste a diff in by hand, and the deny rules are simply not there — **and nothing tells you they are gone.** No refusal appears, because there is nothing left to refuse. Treat re-creating them as the first task of adopting any new tool, and re-run this step's ✅ to prove it took.
- **Guard 2 survives a change of tool but not much else.** It is git, not the assistant, so any tool's commits go through it — but `--no-verify` skips it, and a fresh clone does not have it at all (see above).
- **Guard 3 survives everything and prevents nothing.** It is an ordinary test in the suite. It does not care who made the edit or with what tool; it goes red at the next step for anybody. **It is the only tool-agnostic guard that is not bypassable**, and it is pure detection.
- **Layer 4 survives every scenario in this list and is what you are actually relying on**: the authoritative document copies live outside the repo, and git keeps every committed version, so any tampering is diffable and reversible. Its one requirement is that somebody looks — which is what §0.2 rule 3's five-second filename glance is, and why that glance is not the afterthought it looks like.

**CHANGELOG.md is a special case worth stating (v1.23).** It is a law file here, in the build repository, where an AI has no legitimate reason to touch it and a strong habitual pull to try — asked to tidy up after itself, a coding model will reach for a changelog. It travels with the other three (Step 1.2) partly so that pull meets a deny rule, and partly because a build repository *without* one invites an AI to create a rival changelog that silently diverges from the real one. But **the guards in this list do not reach the place CHANGELOG.md is actually at risk**: it is written in every design session, in the design repository, which has no deny rules and no hook by design. What protects it there is a discipline and a diff — **a design session appends a new entry and does not alter existing ones**, with exactly two exceptions, both of which are *additions* to an old entry rather than rewrites: a founder-approval annotation, and an external-review event on the version that was reviewed. `git diff CHANGELOG.md` showing anything else is the alarm.
✅ `git status` shows no secret or data files as committable; an attempted edit to **CHANGELOG.md** via the AI tool is refused, and so is one to SPEC.md — test the newest member of the list, since it is the one a stale settings file will be missing; a commit touching a law file is rejected by the hook; temporarily change one constant → the tripwire test fails naming it **and printing the four-step order above** (then revert); add a stray character to SPEC.md → the checksum assertion fails, naming SPEC.md and printing the re-bless command with **all four documents** in it (then revert).

**2.5 [AI] Authentication pages and the credential layer.** Login, logout, and password reset, base page template + the single CSS file, mobile-first (ARCHITECTURE §3.5). Logged-out users can reach exactly: login, password reset, invite redemption (stub) — nothing else (SPEC §2, §9.3). The authentication specifics of SPEC §4.6.1 land here:
- **Credential tables** (ARCHITECTURE §4): a `credentials` table (type = password | passkey; only password rows in v1, so passkeys need no later user-model change), a `credential_codes` table (hashed, short-lived, single-use, attempt-capped), and a `login_attempts` table (per-account and per-source-address).
- **Argon2id** as the password hasher (SPEC §4.6.1) — Django's `argon2` hasher, installed via `django[argon2]`, which is part of the ARCHITECTURE §3 stack. Not an optional extra: SPEC §4.6.1 requires the slow memory-hard hash.
- **Codes, not links, for reset.** Password reset emails a numeric code (`RESET_CODE_TTL_MINUTES`, `RESET_CODE_LENGTH`) the user types into the reset page they opened themselves — **no login link is ever emailed.** Codes print to the console locally for now. Show the user-facing promise ("we will never email you a link to log in or reset your password — only a code you type in yourself") on the login and reset pages.
- **Login throttling** (SPEC §4.6.1, §13.6): exponential backoff and temporary lockout keyed on both account and source address (`LOGIN_ATTEMPT_LIMIT`, `LOGIN_LOCKOUT_MINUTES`).
- **The accessibility foundations (SPEC §16, ARCHITECTURE §3.8) — built here, once, and inherited by every later page.** This step is where WCAG 2.1 AA is cheap; retrofitting it in Phase 16 is where it is expensive. Specifically: the base template's `lang`, per-page `<title>`, landmark regions, and skip link; visible focus styling that no theme may remove; and the **shared partials** every later step must compose rather than reinvent — `_field.html` (label + error wiring), `_errors.html`, `_modal.html` (focus trap, Escape, focus restore), `_expandable.html` (`aria-expanded`), `_status.html` (polite live region). The login, reset, and lockout messages are the first users of them.
- **The template smoke tests are built here too (v1.22)** — the automated half of SPEC §16.5's continuous clock, and they belong at the first step that renders a real page rather than at the audit fifteen phases later. They walk a list of page URLs and assert the mechanical invariants on the rendered HTML: every `<img>` has an `alt` attribute (empty only where `is_decorative` is set), every input has a programmatically associated label, every page has exactly one `<h1>` and a non-empty `<title>`, no `tabindex` above 0, and no `<div>` carrying a click handler where a `<button>` belongs. **The list starts with login, reset and lockout, and every later step adds its own pages to it** — that instruction is repeated in Appendix rule 9, because a smoke test whose page list stopped growing in Phase 2 passes forever and checks nothing.
- **The axe/`pa11y` command is written down here** (§0.5, ARCHITECTURE §9): the exact one-line command that scans your locally running instance, recorded in the README beside the test command so it is findable at Phase 10 without archaeology. Installed on your Mac only — never in `requirements.txt`, never in the app image, never in the test suite.
✅ On your Mac **and on your phone's browser** (same Wi-Fi, using your Mac's local address) — and this once across the **whole §0.4 matrix**, since every later page inherits the base template and the single CSS file built here: log in, log out, reset your password by typing the console-printed **code** (confirm no login link is sent); the reset page shows the "only a code, never a link" promise; hammer a wrong password past the limit and get a clear temporary lockout. Try any other URL logged-out — always redirected to login. **Then unplug your mouse:** reach and operate every control on the login and reset pages with Tab/Shift-Tab/Enter alone, and see where the focus ring is at all times. Turn on VoiceOver (⌘F5) and log in with your eyes closed once — it will be slow and strange; that is the point, and it takes ten minutes on a two-page site. **This is familiarization, not verification** (SPEC §16.5.1): the pass that counts is run at Step 16.5 by someone who uses a screen reader daily. Doing it once here is how you come to understand what they will be telling you. **Also: the template smoke tests pass, and the documented axe/`pa11y` command runs against your local instance and reports clean on these two pages** — that is the baseline every later milestone is measured against.

**2.6 [AI] Seed-data command.** A management command creating ~20 fake users with a realistic friendship web (once friendships exist in Phase 3, it grows with each phase). This is how you test everything without real people.
✅ Command runs; you can log in as any fake user (documented shared password).

---

## Phase 3 — Invitations and the Social Graph [AI]

Goal: the data structures everything else stands on. Mostly models + minimal pages; the polished flows come after the visibility engine exists.

**3.1 [AI] Invites and the invite tree.** Invite creation (budget-checked: bank max 5, new accounts start with 2), single-use emailed code, 14-day expiry returning to budget, redemption flow (email verification **by numeric code, not a link — SPEC §4.6.1**; password **screened against known-breached passwords via the HIBP k-anonymity range API, server-to-server, fail-open on outage — SPEC §4.6.1**; display name — screened against `NAME_BLOCKLIST` with an honest rejection message (SPEC §4.5) — 18+ attestation, per SPEC §4.1), auto-friendship inviter↔invitee, permanent invite-tree record (SPEC §4.3).
✅ As a seeded user, invite a new fake address; redeem it (console code, not a link); a deliberately breached password (e.g., `password123`) is refused with an honest message while a strong one is accepted; the two accounts are friends; the tree row exists; the budget decremented.

**3.2 [AI] Friendships, friend requests, blocks — models and rules.** Symmetric friendships; 300-cap enforced with honest errors (SPEC §5.1); request records with the 90-day declined cooldown (§5.2); block records (§5.4). UI minimal for now.
✅ Model tests pass, including: cap at exactly 300, cooldown arithmetic, block ends friendship.

**3.3 [AI] Groups.** Named private friend lists, ≤30 members, cap warnings (SPEC §6).
✅ Create a group as a fake user; try to add a 31st member; get refused with a clear message.

---

## Phase 4 — The Visibility Engine [AI] ← the most important phase

Goal: the one module every permission decision flows through (ARCHITECTURE §5), built **before any content feature exists**, so no page is ever written that decides visibility for itself.

**4.1 [AI] The engine.** First, the **bare data models the engine reasons over** — posts, post_audience, post/profile hashtag tables, contact_items and contact_overrides: tables only, no pages, no UI (their features arrive in Phases 6–10). Then the five functions of ARCHITECTURE Decision 4 (`are_connected`, `can_see_post`, `can_see_profile_tier`, `visible_contact_card`, `can_act`), blocks checked first in both directions, plus the read-only preview-as mechanism (SPEC §9.5).
**4.2 [AI] The dense test suite.** The project's largest test file: block symmetry and total invisibility, FoF boundaries, audience-snapshot + current-friendship (§7.4), the three-condition hashtag gate (§11.3) **including the multi-tag case — a post carrying three tags is visible to a FoF who carries any one of them, not only to one who carries all three (SPEC §11.3, v1.18); the "all" reading fails silently, hiding posts with nothing anywhere raising an error** — contact-cascade conflicts with deny-beats-allow (§10.3), friend-list filtering (§11.5). Tests written from SPEC sentences, each test naming the SPEC section it enforces.
✅ *Phase milestone:* the full suite passes, and you personally read the **test names** top to bottom — they should read like SPEC's rules restated. Any rule you can't find a test for, ask the AI to add. (You are not reading code here; you are auditing coverage by name.)

**4.3 [AI] Friendship flows, now user-facing.** Friend-request send (FoF-only, auto-generated context, no free text), silent decline, unfriend (silent), block/unblock pages — all through the engine.
✅ With two browser windows logged in as two fake users: send/accept a request; block; verify the blocked pair see nothing of each other anywhere.

---

## Phase 5 — The Server: First Deploy [FOUNDER, with AI-written scripts]

Goal: the empty-but-real site running at your domain with HTTPS and real email — while the codebase is still small. Infrastructure problems are far easier to diagnose now than after fourteen more phases. From here on you develop locally and deploy occasionally.

**5.1 [FOUNDER] Decide the two deferred picks.** (Carried here from ARCHITECTURE §15 at your request.)
- **VPS:** recommendation **Hetzner**. Founder stated (2026-07-13 review): first users are in the US plus some in Canada → recommended location **Ashburn VA** (closest to both US and eastern-Canadian population centers; Hillsboro OR only if the circle turns out west-coast-heavy). A ~€6–12/month shared-vCPU instance (2 vCPU / 4 GB) is ample.
- **Email:** recommendation **Postmark**, chosen for its transactional-only ethos (ARCHITECTURE §3.6) — **not for its free tier, which this project outgrows in its first month.** Count it honestly (v1.18): every new account costs at least two emails (the invite and the verification code); every password reset, new-device login, password change and email change costs one (SPEC §4.6.1); each dormant account costs four warnings over two years (§4.8); and **optional email notifications (SPEC §12.5) are unbounded per user by design.** The free developer tier is **100 emails/month**: the twenty accounts of Step 17.2 spend roughly half of it on signup traffic alone, and the first few users who switch email notifications on spend the rest inside a week. The next step up is Postmark's paid tier — of the order of **$15/month for 10,000 emails** at the time of writing; confirm the current figure when you sign up. Budget for it from the launch month rather than meeting it mid-launch; ARCHITECTURE §11 already carries "$0–15" on this line.
✅ Decisions written down; if you deviate from the recommendations, note it so the privacy policy (Step 15.1) names the right processors.

**5.2 [FOUNDER] Create the VPS.**
1. Sign up at the chosen provider; add your **SSH public key** during server creation (if you've never made one: `ssh-keygen -t ed25519` in Terminal, accept defaults, paste the contents of `~/.ssh/id_ed25519.pub`). Password SSH stays off.
2. Create the server (Ubuntu LTS, the size above). **Take the 80 GB-class disk, not the 40 GB one (v1.20).** A few euros a month, and ARCHITECTURE §11.1 does the arithmetic that decides it: images are the only unbounded store, about nineteen per user never expire, and 500 users land near 50 GB. Disk is the first resource this design exhausts — not CPU, not the database — and a full disk stops Postgres and takes the site down hard.
3. In your registrar's DNS page: an **A record** pointing your domain (and `www`) at the server's IP. **Set the TTL to 300 seconds (v1.20)**, not the registrar's default. Disaster recovery ends in "repoint DNS" (ARCHITECTURE §3.4, §13.2); at a default TTL of hours that last step adds most of a day to every recovery, and lowering it costs nothing and changes nothing else.
✅ `ssh root@yourdomain.com` gives you a server prompt; a DNS lookup of your domain reports a TTL of 300.

**5.3 [AI→FOUNDER] Server preparation script.** The AI writes a commented, idempotent setup script (firewall allowing only SSH/80/443, automatic security updates, fail2ban, Docker installation, non-root deploy user); **you** read the comments, then run it on the server per its instructions.
✅ Script's own final check passes; you can log in as the deploy user.

**5.4 [AI→FOUNDER] Deploy script + Caddy config.** The three-line-spirit deploy of ARCHITECTURE §8 (push code, run migrations, restart containers), Caddy serving your domain with automatic HTTPS. You run your first deploy.

**Three availability settings belong in this step (v1.20), because they are compose-file and Caddy lines and you are already here** (ARCHITECTURE §7.2):
1. **`restart: unless-stopped` on every container, and Docker enabled at boot.** The cheapest availability in the whole project: a crashed worker, an out-of-memory kill and the reboot that follows an automatic security update all recover with nobody awake.
2. **Cap the container logs** (`max-size` and `max-file` on the logging driver). Unbounded `json-file` logs are the classic way a small server fills its disk with nothing.
3. **A maintenance page in Caddy** — one static, first-party page served with **HTTP 503 and `Retry-After`**, never 200. Caddy stays up when the app is down, which is why the page lives there. It is a user-facing surface, so SPEC §16 applies: `lang`, a title, one `<h1>`, readable contrast without a theme, and nothing loaded from anywhere.
✅ `https://yourdomain.com` shows the login page, padlock valid, plain `http://` redirects to `https://`; `docker compose stop app` shows the maintenance page and `curl -I` reports **503**; rebooting the server brings the whole stack back with no keystrokes.

**5.5 [FOUNDER] Email provider setup.**
1. Sign up (Postmark asks what you send — answer: transactional only, invitation/verification/security emails for a private social site).
2. Add the DNS records they give you (DKIM, return-path) at your registrar; wait for their dashboard to verify.
3. **Add SPF and DMARC records (SPEC §4.6.1):** an SPF record authorizing the provider to send for your domain, and a **DMARC record at `p=reject`** so mailbox providers reject anything forging your domain. (Optionally start DMARC at `p=none` for a few days to confirm your legitimate mail passes, then move to `p=reject`.)
4. Put the API key in the server's environment file (never in git).
✅ Password-reset **code** email from the live site lands in your **personal inbox** (not spam); **the provider's own dashboard shows that specific message as delivered** — not queued, not bounced; and a lookup tool (MXToolbox or equivalent) confirms all three records **independently**: **SPF** present and authorizing the provider, **DKIM** present and valid on the provider's selector, **DMARC** at `p=reject`. Belt and braces: open the delivered message's headers in your mail client and confirm `spf=pass` and `dkim=pass`. (Step 2's dashboard check verifies the *domain* setup; this verifies that a real message actually arrived.)

**5.6 [FOUNDER] Backups.**
1. Create the backup target: **Hetzner Storage Box** (if Hetzner) or **Backblaze B2** — a few dollars/month.
2. The AI writes the nightly backup job (ARCHITECTURE §10: pg_dump + images, encrypted with restic, 30-day retention `BACKUP_RETENTION_DAYS`); you install its credentials and schedule.
2a. The AI also writes **`verify_restore`** (ARCHITECTURE §6, §10), the weekly automatic check: fetch the newest backup, restore it into a scratch database, run a smoke query, drop it, record the result, and **email you if any step fails**. It checks free disk first and alerts rather than restoring if there is not room — a verification job that fills the disk is worse than no verification job. Runnable by hand like every other job (Appendix rule 7).
2b. **Put the backup encryption key somewhere that is not the server (v1.20).** This is the one step in Phase 5 whose omission is unrecoverable. Backups are encrypted; a restic key living only in the server's environment file is a key that dies in the same fire as the machine, and what is left is a bucket of ciphertext nobody can ever open. **Into your password manager, today: the restic password/key, the backup-storage credentials, the VPS login, and the DNS registrar login.** The runbook (Step 17.3) records where they are, and never records the values.
3. **Rehearse a restore** onto your Mac following the AI-written runbook. An untested backup is a rumor (ARCHITECTURE §10) — and this manual rehearsal, unlike the weekly automatic one, is the only test of the case that actually matters: the server is gone and you have a laptop. **Do the rehearsal using the password-manager copy of the key, never one copied off the server**, or the rehearsal quietly tests the wrong thing: taking the key off the machine on the morning of the test is exactly how a founder proves a restore works and still loses everything the day the machine dies.
✅ You have personally restored a backup and logged into the restored copy locally, using credentials taken from your password manager and nothing from the server; `verify_restore` run by hand completes and records a success, and run against a deliberately corrupted backup file sends you the failure email.

**5.7 [AI→FOUNDER] The watchdog you actually have (v1.20).** Set up here rather than later, because you are already in server-configuration mode and because the thing it guards — a scheduled job that stops running — is the one failure on this platform with **no symptom at all**. A failing `expire_content` shows no error page and draws no complaint; it just quietly keeps content the platform promised to destroy (ARCHITECTURE §7.3).
1. **[AI] `job_runs` and the health endpoint.** Every §6 command writes one `job_runs` row per run, in a `finally` block so a crash records a failure rather than nothing (ARCHITECTURE §4). `GET /healthz` returns **200 and the literal body `ok`** when the app can reach the database (one `SELECT 1`), **503** otherwise — no version, no counts, no JSON, no timestamps, touching no user table and creating no session. It answers *is the database alive* and deliberately nothing else, so that it can never become an oracle for whether this platform has users.
2. **[AI] `check_health`, daily.** Job windows (hourly job late at 3 hours, daily at 26, weekly at 8 days), disk usage, and the last 24 hours' count of unhandled errors. **Emails you only when something is wrong**, and the email carries **counts and exception types only — never a request body, never a traceback with local variables** (ARCHITECTURE §7.3: an alert that ships user content to the mail provider is the leak §7.1 exists to prevent). Disk warns at **75%** and alarms at **90%**.
3. **[AI] `check_health --digest`, weekly, on a fixed day.** The same report sent **whether or not anything is wrong**. This is not redundancy — until the watchdog is built it is the whole of your outside-the-machine monitoring. You deferred the external service to *after* launch (ARCHITECTURE §15 item 6), so `check_health` cannot report its own death; the digest makes a **missing** email the signal. It replaces the manual "go and look" of Step 17.3. **Everything the watchdog will later need is being built right here** — `/healthz`, `job_runs`, `check_health` — so adding it is a signup and two monitors, never a code change.
4. **[FOUNDER] Docker's own healthcheck.** Point the compose `healthcheck:` for `app` at `/healthz` and add one to `db`, so a wedged-but-alive process is restarted and the app waits for Postgres at boot instead of crash-looping (ARCHITECTURE §7.2).
✅ `curl https://yourdomain.com/healthz` returns `ok`; with the database container stopped it returns **503**. `check_health` run by hand against a job you deliberately have not run emails you, and the email contains no post text and no traceback. The weekly digest arrives on its day. You have written the digest's fixed day on the runbook, because from launch onward **its absence is a finding**.

---

## Phase 6 — Posts [AI]

**6.1 [AI] Image pipeline.** Pillow decode → full re-encode (guaranteed EXIF/GPS destruction) → bounded resize → random filename in a non-web-served folder → DB record; serving only through a permission-checked view (ARCHITECTURE §3.7). **Alt text (SPEC §16.3):** the `images` table gets `alt_text` (≤ `ALT_TEXT_MAX`) and `is_decorative`; every upload form requires a deliberate choice between the two — never silently skipped, never auto-generated — and every rendering surface reads the stored value.
✅ Upload a photo that has GPS EXIF (take one with your phone); download it back; inspect it (Preview → Tools → Show Inspector): no GPS, no EXIF. Copy the image URL into a logged-out window: refused.

**6.2 [AI] Feed posts.** Composer with audience picker (individuals + groups, live count, hard ≤30 with honest narrowing prompt — SPEC §7.3), one optional image, audience snapshot rows (§7.4), and URL allowlist enforcement at composition — see 6.2a, which this step, Step 6.6 (editing) and Step 7.1 (comments) all call. Also **`POST_MIN_INTERVAL_MINUTES` spacing** (SPEC §7.3, §13.6): compare against the author's last feed post's timestamp — not a daily counter — and refuse with "you can post again in N minutes." Profile posts are exempt.

**6.2a [AI] The link validator (SPEC §7.2.3, ARCHITECTURE §7).** **One shared function**, called by every composer that accepts text (feed posts, profile posts, comments) — never reimplemented per surface. It parses the URL (no regex string matching), requires `https`, matches the host **exactly or as a subdomain** of an allowlisted row, and then **rejects that row's redirector patterns**. The redirector step is the one an implementer is most likely to skip and the one that matters most: `youtube.com/redirect?q=…` and `google.com/url?q=…` pass any host check while handing the reader to an arbitrary attacker page. Belt-and-braces: refuse any otherwise-allowed URL whose query string contains an absolute `http(s)://` URL. Shorteners are never allowlistable. **The rejection message** follows SPEC §7.2.3 and the error rules of §16.3 — it says the link isn't permitted, what the allowlist is for, and that anything else can be shared through the contact methods on the user's contact card, with a pointer to the operator request form (§13.5). Links render as **plain clickable links, never embedded or preview-carded** (§7.2).
✅ Attack cases, as tests, not a manual click-through: `https://youtube.com/redirect?q=https://evil.example` → refused; `https://www.google.com/url?q=https://evil.example` → refused; `https://evil-youtube.com/watch?v=1` → refused; `https://youtube.com.attacker.net/watch?v=1` → refused; `http://` (not https) on an allowed host → refused; a plain `https://maps.google.com/…` → accepted. Each refusal names the contact card.
**6.3 [AI] Profile posts.** All-friends visibility, lives on the blog only, friends get a notification record (§7.1).
**6.4 [AI] The feed page.** Strict reverse-chronological: audience-of feed posts + profile-update notifications + system notifications; no ranking of any kind (§7.7).
**6.5 [AI] Expiry.** The `expire_content` cron job (90 days, idempotent — ARCHITECTURE §6), pinning ≤10 profile posts and "pinned" markers (§7.5–7.6). **Two kinds of time appear here and they are deliberately different** (SPEC §7.5, §7.5.1): a post's *age* renders through the Step 2.3 relative helper ("A few days ago"), while the ≤14-day deletion countdown renders as **absolute days** ("deletes in 6 days"), computed per page load, never live-ticking. Vague about the past, exact about the destruction — that contrast is the feature, not an inconsistency to tidy up.

**6.6 [AI] Editing posts and comments (SPEC §7.8).** Authors may edit their own posts (text, image, preformatted toggle, hashtags) and their own comments, until expiry. A nullable `edited_at` drives a permanent plain-text **"edited"** marker showing the *relative* time of the last edit. No version history, no diff, **no notification on edit**. Four rules that are easy to get wrong and expensive to get wrong:
- **Validation is shared with creation, not duplicated.** The edit path runs the same link validator (6.2a), length caps, whitespace normalization, hashtag-vocabulary check and image re-encode as the create path — which in practice means content validation lives in the shared model/form layer, never in the create view.
- **`edited_at` is display-only.** Feed order reads `created_at`; expiry reads `created_at`. No query sorts or filters by `edited_at`, or editing silently becomes a way to bump a post or outlive the 90-day promise.
- **An edit writes no `post_audience` rows.** The one thing an edit may legitimately change is a *profile* post's hashtags, because §11.3's FoF gate is evaluated live by design — and newly-matched FoFs are never notified.
- **The post author may delete any comment but never edit one.** Wire the author's power to the delete path only.
✅ **Written as attack cases, not a click-through:** publish a post with clean text, then edit a disallowed URL into it → **refused** (this is the whole reason this step exists — a validator wired only into the create path is the defect being prevented, and it fails silently); edit a post and confirm it does *not* move in a second account's feed; backdate a post 89 days, edit it, confirm it still expires on schedule rather than getting another 90 days; confirm no notification fires to anyone on the edit; as the post author, confirm there is no route to edit someone else's comment.
✅ Also: submit an image with neither a description nor the "decorative" tick — the composer refuses with an honest message; the audience picker's live count is reachable by keyboard and announced (SPEC §16.3); a folded long post expands with a real button that keeps focus where it was.
✅ *Phase milestone (two browser windows):* post to a hand-picked audience — the included friend sees it, the excluded one doesn't; unfriend and confirm old posts vanish; try a disallowed URL — rejected with explanation; backdate a seeded post 80 days — countdown appears; run `expire_content` against a backdated-91-days post — gone, image file too.

---

## Phase 7 — Comments and Reactions [AI]

**7.1 [AI] Comments.** Flat list; visibility = the post's exactly (via engine); attribution with the visibility-aware profile-link rule (name links only with ≥basic-tier access, plain text otherwise — SPEC §8.1 v1.3); author-delete + post-owner-delete; **author-edit only**, per Step 6.6; own 90-day clock; no images. **Folded at `COMMENT_FOLD_CHARS` = 300** (SPEC §8.1, v1.18) — the same display-only mechanism as long-post folding (SPEC §7.7), with a real "read more" `<button>` per comment carrying its own distinct accessible name ("Read more of Alice's comment"), because a thread produces many identical ones (SPEC §16.3).
**7.2 [AI] Reactions.** One per user per target from `REACTION_SET`; changeable/removable; **visible only to the content's author, as names, never counts** (§8.2).
✅ *Milestone:* commenter's name links for a friend-viewer and is plain text for a stranger-viewer (use a hashtag-gated scenario from the seed data once Phase 10 lands — noted in (d) to re-verify then); reactions invisible to a third account; author sees names, no numbers anywhere.

---

## Phase 8 — Profile Pages and Theming [AI]

**8.1 [AI] The profile page.** SPEC §9.1 section order; the §9.2 tier table via `can_see_profile_tier`; gallery ≤8; the blog filtered per viewer; no deep-link value (every URL permission-checked, UUIDs only). **The two bio fields (SPEC §9.4) are separate columns with different rules, not one field with a length check:**
- `short_bio` ≤ `BIO_SHORT_MAX` — basic tier, so **FoFs see it and it rides along in every friend-request card** (§5.2). Screened against `name_blocklist` at every save (the same check as display names, Step 2.3's neighbour), and **rendered with links disabled** — URLs in it are inert text, never linkified, not even allowlisted ones.
- `extended_bio` ≤ `BIO_EXTENDED_MAX` — friends only, so it is not a push surface: allowlisted links permitted (via 6.2a), no cooldown.
- **`BIO_CHANGE_COOLDOWN_HOURS` on `short_bio` and the profile photo** (SPEC §13.6), with a `BIO_EDIT_GRACE_MINUTES` free window measured from the *first* save in a burst so the clock never restarts. Three carve-outs to implement explicitly: clearing the short bio to empty is never limited; a save rejected by screening starts no clock; the extended bio is exempt.
- Bios get **no "edited" marker** and notify nobody (SPEC §9.4, §12.1) — but every save re-runs validation, or the screening is decorative.
✅ Set a short bio, immediately fix a typo (allowed, inside the grace window), then try a third change an hour later → refused with an honest "you can change this again in N hours"; clear it to empty → allowed immediately; paste a URL into the short bio → renders as plain text with no link; paste an allowlisted URL into the extended bio → renders as a link.
**8.2 [AI] Theming.** `THEME_SET` as named CSS-variable sets; server picks the theme per surface (own view / profile owner's / viewer-override) per SPEC §9.1 v1.4 and ARCHITECTURE §3.5. **Includes the automated contrast test** (ARCHITECTURE §3.8, §9): every `THEME_SET` combination's text and UI-boundary token pairs are computed against WCAG 2.1 AA ratios (4.5:1 / 3:1) and a failing theme fails the build by name. A theme that cannot pass is not shipped — no exceptions for one that "looks nice." **This test is continuous, not a Phase 16 check (v1.22, §0.5):** it runs beside every other test from here on, so a theme added in year two fails the build on the day it is added rather than at an audit that may never run again.
**8.3 [AI] Preview-as.** Profile as any chosen friend or generic FoF sees it — same engine, substituted viewer, strictly read-only (§9.5).
**8.4 [AI] Display-name change.** The settings flow per SPEC §4.5.1: 90-day cooldown since creation/last change (honest "you can change again on [date]" message), blocklist screening, and the 90-day "formerly" dual display — which costs nothing here because every surface already renders names through the step-2.3 helper.
✅ *Milestone:* view a seeded profile as friend, as FoF (basic tier only), as stranger (nothing); set a profile theme in one account and see it from another; flip the viewer-override and see your own theme win; preview-as matches what the real second browser shows. Change a seeded user's name (test hook past the cooldown): "New (formerly Old)" appears on their old posts, comments, profile, and in a reaction list; a second change attempt is refused with the correct date.

---

## Phase 9 — Contact Cards [AI]

**9.1 [AI] Card + cascade.** ≤12 items (phone/email/messenger-link from allowlisted domains); default → group override → individual override, deny-beats-allow between groups (SPEC §10.2–10.3) — resolution lives in the engine and the tables were defined in Step 4.1 (already tested in 4.2; this step is UI only).
**9.2 [AI] Card requests.** Picker-based request; system auto-replies with exactly the permitted version (§10.4). (Request-more-access flags stay parked for v1.1, §10.5 — table may exist, no UI.)
**9.3 [AI] Preview-as for the card** (§9.5).
✅ *Milestone:* build a card with a phone number off-by-default, on for group "Close", off individually for Bob who is in "Close" — Bob's auto-reply lacks the number (individual wins); a friend in no group gets defaults only; preview-as agrees with reality.

---

## Phase 10 — Hashtags and Discovery [AI, with one FOUNDER content step]

**10.1 [AI] Vocabulary + pickers.** `HASHTAG_VOCAB` operator-curated in Django admin; searchable picker (never free-typed — SPEC §11.2); ≤10 profile hashtags; post tagging. **The picker searches tag names *and* each tag's operator-curated search aliases** (SPEC §11.2.1) — aliases are matched, never rendered, never selectable, and never stored on a profile or a post. **The empty result is a real, specified state, not a leftover:** honest text saying no tag matches, plus a link to the suggestion form (SPEC §13.5) — never a text field that accepts a tag and silently fails to make one. Both the picker and its empty state are WCAG AA surfaces like everything else (ARCHITECTURE §3.8 names the combobox pattern).

**10.1a [FOUNDER] Write the starter vocabulary.** Content work, not code, and the largest single lever on the operator load this whole area creates (SPEC §11.2.1) — a vocabulary broad enough that suggesting a tag is the exception is worth more than any workflow built to process suggestions.
- **Target ~300 tags across roughly twenty areas of life** (sport, outdoors, making and repairing, music, food and drink, games, reading and writing, film, faith, care and volunteering, animals, travel, craft, growing things, learning, collecting…). The number is a target, not a cap, and deliberately lives here rather than in SPEC §14 — nothing enforces it and it is content, not behaviour.
- **Hand-written, not imported.** Public taxonomies are built to classify, so they yield abstractions ("Transport", "Philosophy") that make poor interest tags, and pruning one is most of the writing anyway. **Weight every entry toward things people do *with other people, offline*** (SPEC §1.1: the measure of success is offline). "#hiking" and "#board games" earn their place; "#productivity" does not.
- **One tag per interest, and write the aliases as you go.** Each rejected synonym becomes an alias on the canonical tag rather than being lost — *#hiking* takes *hikes, rambling, trekking, trail walking, hillwalking*. This is the same anti-synonym judgment SPEC §11.2 requires, made once at the desk instead of repeatedly in the queue.
- ✅ *Done when:* the vocabulary is loaded, and searching each of ten interests the way five different people would phrase them lands on a tag every time.
- **Open question, parked and deliberately not answered here (2026-08-17):** whether an LLM can draft candidate tags and alias sets for the founder to approve. It is worth trying, and it is **not** blocked by SPEC §1.3's "the platform never infers" — that rule governs what the *running platform* does with *user data*, and this is an operator writing a static word list at a desk, with no user, no user data and no inference about anybody involved. What it would need is stated so the trial is honest: **the founder approves every entry**, nothing is loaded unread, and the offline-weighting test above is the acceptance bar. Recorded in TODO.md.

**10.2 [AI] The FoF gate.** §11.3's three live-evaluated conditions (engine already tests this; wire it to real pages), including FoF commenting on gated posts.
**10.3 [AI] The discover page.** Pull-only: ranked people suggestions with auto-context, matched posts, and the clickable-hashtag tag filter (§11.4 v1.3). Nothing from here ever touches a feed.
**10.4 [AI] Friend-list visibility** per §11.5.
✅ *Phase milestone:* seed Alice–Mutual–Bob with #hiking on both Alice's and Bob's profiles; Bob sees Alice's #hiking-tagged profile post on discover and can comment; Bob removes his tag — access ends live; clicking #hiking anywhere lands on the filtered discover view; a blocked pair see nothing of each other in any of it. **Plus the picker:** searching *rambling* finds #hiking through its alias while the word *rambling* appears nowhere in the result, on the profile, or on any post; searching a word with no tag and no alias produces the honest empty state and the suggestion link, and no path anywhere in the picker creates a tag.

---

## Phase 11 — Introductions [AI]

**11.1 [AI] Broker flow** (§5.5a): both must accept; declines silent in every direction; auto-context only.
**11.2 [AI] Requested flow** (§5.5b): pointable-Charlies rule; converts to flow (a) with requester pre-accepted.
✅ *Milestone (three browser windows):* run both flows end-to-end including a decline — verify the broker learns only "did not complete" and the other candidate learns nothing; a flow that would breach either 300-cap errors clearly.

---

## Phase 12 — Notifications and Email [AI]

**12.1 [AI] In-feed notifications** for the full SPEC §12.1 list, with read state. **Profile updates are per event type, not one generic "updated their profile"** — new blog post and profile-photo change notify; gallery additions notify, coalesced; bio, about, hashtag and theme changes are **silent**. Wording is specific per type and is real text, never an icon carrying the meaning.

**12.2 [AI] The two coalescing modes (SPEC §12.3).** These are genuinely different mechanisms and collapsing them into one will produce either a flooded feed or news that arrives too late:
- **Profile updates coalesce on a clock** — one row per (author, recipient, event type) per `PROFILE_NOTIFY_WINDOW_HOURS`, *updated in place*, carrying the most recent event's age. Two blog posts inside a window become "David posted twice to his blog", linking to the blog rather than either post.
- **Comment and reaction activity coalesces on unread state, with no clock at all** — one row per (post, recipient), updated until it is read.
Both are "find the open row and update it," never "insert another row."

**12.3 [AI] Following a post (SPEC §12.3).** A `post_follows` row per (post, follower); commenting turns it on, a visible per-post toggle turns it off, a global default lives in settings. Two rules the table cannot enforce by itself: **following is private** — nothing exposes followers to the post author and no count of them exists — and **the row is permission-to-be-notified, not permission-to-see**, so delivery re-asks the visibility engine every time rather than trusting the row.

**12.4 [AI] Rendering rules (SPEC §12.2).** **Never an excerpt of post or comment text** — actor + event type + relative age + link, nothing more; a body excerpt would turn a pull-model profile post into a push-model feed post with a 300-person audience. **Names, never numbers** ("Alice and Tom commented on your post", overflowing to "and others") — no unread badges, no counts anywhere. **Actors render live** through the Step 2.3 helpers, so deleted comments and removed reactions drop out instead of freezing into the feed. Plus the `expire_notifications` job (ARCHITECTURE §6), so notifications never outlive the content they point at.

**12.5 [AI] Optional email notifications** with per-category user settings; content-minimal (no post content beyond what the recipient may see); through Django's email abstraction. **Emails carry no timestamp at all** (SPEC §12.3) — a relative age computed at send time is false by the time the mail is read, and the mail client already stamps it.
✅ *Milestone:* each §12.1 event produces exactly its notification and (when enabled) email, and the silent ones produce **nothing** — change a bio and a theme in one account, confirm the other account's feed stays empty. Comment three times from three accounts on one post → the author has **one** notification naming them, not three. Delete one of those comments → that name disappears from the notification. Unfriend a follower → their notifications stop silently, and nothing anywhere tells the author they were following. Search the rendered feed for any digit that is a count of anything: there should be none.

---

## Phase 13 — Moderation and the Operator Console [AI]

**13.1 [AI] Reports.** Report action on every post/comment/profile → queue with frozen copy; content stays live; purge rules (dismiss→now, upheld→+30d, hard cap 90d) via the `purge_moderation` job (SPEC §13.2–13.3); content-free upheld counters (§13.4). **One report form, and every report carries a reason** (SPEC §13.2, v1.21): the profile target categories, and for posts and comments *harassment or abuse · unwanted or commercial content · someone else's private information · the tags don't match this post (profile posts only) · something else*, plus the optional short note to the operator. The column already exists (ARCHITECTURE §4) — this is a form and a list of values, not a migration. **On a tagged profile post the report control sits with the §7.9 visibility line**, because that line is what tells a friend-of-friend the tag is why they are seeing the post (SPEC §7.9, v1.21). Build **no** per-tag report count, ranking or flag anywhere, admin included.
**13.2 [AI] Operator request form.** One form, category dropdown (hashtag / external service / bug / **accessibility problem** / feedback), rate-limited, into the same queue (§13.5). Accessibility reports sort ahead of feature requests in the queue (SPEC §16.5).
**13.3 [AI] Django admin as operator console.** Moderation queue with act-on actions (delete content / warn / ban), vocabulary editor, `NAME_BLOCKLIST` editor (SPEC §4.5), `REACTION_SET` and `THEME_SET` editors; admin at a non-default path (ARCHITECTURE §7). **URL-allowlist editor** (SPEC §7.2.3, ARCHITECTURE §4): each row carries host, **admitting category** (convening / hosts-what-we-cannot-host / messenger handoff), and **redirector-rejection patterns**; rows are **created inactive by default**, so activating one is the deliberate moment the operator confirms the service has no open redirector. Seed the known cases (`youtube.com/redirect`, `google.com/url`). Deactivating beats deleting — it keeps the record of why a domain was added.
**13.4 [AI] Rate limits.** Per-account daily counters in the database, §14's ✎ values, honest "slow down" messages (§13.6); plus the `reset_rate_counters` job. The stricter **login backoff** (per-account + per-source-address lockout) built in Step 2.5 is confirmed wired here as the security-specific case of the same framework (SPEC §4.6.1). **Confirm the three non-counter controls are wired and are *not* day tallies** (ARCHITECTURE §4): feed-post spacing (`POST_MIN_INTERVAL_MINUTES`, Step 6.2) and the two bio/photo cooldowns (`BIO_CHANGE_COOLDOWN_HOURS`, Step 8.1) are elapsed-time comparisons against stored timestamps — a daily counter cannot express "not again for 12 hours," and `reset_rate_counters` must not touch them.
✅ *Milestone:* report a seeded post; see the frozen copy in admin; dismiss → copy purged; uphold another → live content gone, counter incremented, copy purged after the (test-shortened) window; a script-speed action burst hits the limit politely.

---

## Phase 14 — Account Lifecycle and Data Export [AI]

**14.1 [AI] Deletion.** Request → immediate deactivation → 30-day grace with cancel-on-login → `process_deletions` full erasure + anonymized invite-tree stub (SPEC §4.7, §4.3); comments/reactions removed everywhere.
**14.2 [AI] Inactivity.** `inactivity_sweep`: warnings at `INACTIVITY_WARN_DAYS` = 180/365/670/700 days since last login, deletion at `INACTIVITY_DELETE_DAYS` = 730 (SPEC §4.8). **Days, never calendar months** — the arithmetic is a subtraction, not a calendar walk.
**14.3 [AI] Login-email change** (verified-new-address flow, notice to old — §4.6).
**14.4 [AI] Data export.** One click → ZIP of JSON + images, everything §4.9 lists.
**14.5 [AI] Remaining cron wiring.** All ARCHITECTURE §6 jobs scheduled on the server; each also runnable by hand; idempotency tests.
✅ *Milestone:* delete a seeded account and fast-forward the grace (test hook) — data gone, stub present, their comments vanished from friends' posts; export your own test account and open the ZIP — it's complete and readable.

---

## Phase 15 — Legal and Public Documents [FOUNDER+AI]

**15.1 [FOUNDER+AI] Privacy policy + Terms of Service**, written plainly (SPEC §15.1): what's collected (nearly nothing), the 90-day expiry, the 30-day backup retention (ARCHITECTURE §10), the named email provider and VPS host as processors, GDPR rights (export §4.9, erasure §4.7), 18+ rule, invite-tree stub disclosure. **The list of outside parties is exactly two at launch, and expected to become three (v1.20):** the availability work of Steps 5.4–5.7 added no processor, because the external monitoring service is **deferred, not rejected** — email alerts for launch, the watchdog built out when any of ARCHITECTURE §7.3's three triggers fires (ARCHITECTURE §15 item 6). **Write the policy so that adding it is a sentence, not a rewrite**, and when it arrives name it here with the honest qualifier that it is **not** a processor of user data: it sees one URL replying `ok` and nothing about anybody. Note that trigger 1 is *any public phase*, which is the same moment SPEC §15.1 requires attorney review — so the two land together and neither is a surprise. AI drafts from SPEC; **you** read every sentence and own it. Linked from login and inside the app.
✅ *Done when:* you can honestly say every sentence is true of the system as built. (Attorney review is required before any *public* phase — SPEC §15.1; friends-only prototype proceeds without.)

**15.2 [FOUNDER+AI] Accessibility statement** (SPEC §16.5), published alongside the privacy policy and linked from login and settings. It carries five things:
1. **The conformance target** — WCAG 2.1 Level AA.
2. **The scope of the claim (v1.22)** — every user-facing surface, and **one sentence naming the operator-console carve-out** (SPEC §16.1.1): the Django admin is held to keyboard operability, visible focus, contrast, labelled fields and text errors, and not to the standard as a whole. Say it plainly. "We conform to WCAG AA" with a silent exclusion inside it is the exact claim SPEC §16.5's honesty rule exists to stop, and a carve-out stated in one sentence costs nothing while an unstated one costs the whole claim's credibility.
3. **The date and method of the most recent verification** — Step 16.5, and who ran which passes.
4. **Known limitations, listed honestly** — the preformatted-post horizontal-scroll exemption (SPEC §16.3), and anything Step 16.5 found that you have not yet fixed.
5. **How to report a problem** — the §13.5 form, plus an email address for someone who cannot use the form at all, which is the whole point of naming it separately.

**Sequencing:** draft it here with the rest of the public documents, but leave the conformance claim, the verification date and the known-limitations list **blank until Step 16.5 fills them in** — the audit is what turns a draft into a claim.

**It is a living document, not a launch artifact (v1.22).** SPEC §16.5 now repeats the human passes on triggers rather than once, which means this page has a maintenance obligation and the runbook carries it (§17.3 section 13). Revise it whenever the passes repeat, whenever a listed defect is fixed, and whenever a new one is found and not yet fixed. **A statement written once and never revised becomes false by standing still** — the site changes underneath it — and a stale statement is therefore a breach of the honesty rule rather than an untidy page. Put the date of last revision on it, visibly, so its staleness is legible to a reader instead of only to you.
✅ *Done when:* the statement is drafted; and (after Step 16.5) it claims **only** what was actually verified, names the operator-console carve-out, and carries a visible date. A conformance claim you have not tested is the one accessibility lie that matters.

**15.3 [FOUNDER] Line up the accessibility tester (v1.22).** Step 16.5's three human passes are run by someone who is not you (SPEC §16.5.1) — this is the step that makes sure such a person exists before the gate rather than at it. Phase 16 previously assumed you were available to yourself; you are, but you are not qualified for this, and finding out at the gate means either a delayed launch or a pass run badly.
- **Who.** First choice: **a person who uses a screen reader daily as their primary means of using the web** — a friend, a friend of a friend, or a member of a local disability organization — and **offer to pay them for their time**; this is professional work and asking for it free is asking the excluded party to subsidize their own inclusion. Second choice, if nobody suitable turns up: **a paid professional accessibility auditor** (a few hundred to low four figures for a site this small). Either satisfies SPEC §16.5.1's bar.
- **When to start.** During **Phase 13**, not Phase 15. Finding the right person takes weeks of other people's replies, and by Phase 13 the platform is real enough to be worth their afternoon.
- **What to send them ahead of time.** A test account with seeded data, the page-type list from Step 16.5, SPEC §16 itself, and one plain sentence about what the platform is. Not the whole document set.
- **What to book.** One session covering the keyboard, screen-reader and zoom/reflow passes over every page type, **plus about an hour on the operator console** for SPEC §16.1.1's bounded subset — a short addition to a visit already being paid for. Ask for findings written down, page by page, with what they were trying to do.
- **The standing relationship, not a one-off.** SPEC §16.5's re-audit triggers mean you will want this person again — when a new interactive pattern ships, and before any widening of who can join. Ask at the end of the session whether they would be willing to be called back, and record how to reach them in the same place the runbook lives (§17.3 section 10).
- **What a return visit looks like, and say it now rather than then.** This first audit happens before Step 17.1 wipes the seed data, so nothing they see belongs to a real person. **Every later one runs on the live system** — there is one server and no staging copy — so a returning tester gets **an ordinary member account whose only friend is you**. They see your posts and your profile, and nothing of anyone else's: no operator view, no exception, exactly what the visibility engine gives any member. Where a pattern needs two people, the second one is you. Mention this when you book them, because it shapes what they can and cannot report on.
✅ *Done when:* a named person has agreed, a date is in the calendar for after Step 16.4, and they have the test account and the page list.

---

## Phase 16 — Hardening and the Pre-Flight Audit [AI + FOUNDER, plus a tester at 16.5]

**16.1 [AI] Security settings pass.** The Django production checklist (`manage.py check --deploy` clean), cookie flags, header settings, upload size limits — ARCHITECTURE §7. **Confirm the auth-security layer (SPEC §4.6.1):** Argon2id is the active password hasher, reset/verification use codes with no login link anywhere, login backoff is enforced, and the breach-password check runs at registration and password change. **Confirm the link validator (SPEC §7.2.3):** the Step 6.2a attack cases still pass against the live allowlist, every composer routes through the one shared function, and no active allowlist row has an unchecked redirector. **Confirm the validator runs on the edit path too** (SPEC §7.8 invariant 4, Step 6.6): re-run the attack cases as *edits* to already-published clean content, not just as new posts. A create-only validator is the single most likely way this control gets defeated in practice, and it fails silently — nothing errors, the link simply goes live.
**16.2 [FOUNDER] The zero-foreign-requests check.** In Firefox or Chrome on the live site: open Developer Tools → Network tab, then browse every page type (feed, profile, discover, composer, settings, admin). **Every single request must go to your domain only.** One request to any foreign domain is a tracking-ban violation (SPEC §15.2) — file it as a bug.
**Two things to look for by name (v1.18)**, so the check is mechanical rather than a test of what you happen to recognize: (1) **accessibility overlay widgets**, banned outright by SPEC §16.4 and ARCHITECTURE §3.8 — `accessibe.com`, `acsbapp.com`, `userway.org`, `equalweb.com`, `audioeye.com`, `reciteme.com`, and anything of that shape; (2) the classic silent arrivals — `fonts.googleapis.com`, `fonts.gstatic.com`, any `cdn.*`, `jsdelivr.net` or `unpkg.com` asset host, and any analytics endpoint. A hit on the first list is worse than an ordinary tracking-ban violation: it means something installed the one class of tool this project bans three times over, and it will have been added in good faith by someone trying to help.
**16.3 [FOUNDER] The stranger test.** Logged out (or as a stranger account): try saved URLs of a post, an image, a profile. All must show nothing (SPEC §9.3).
**16.4 [FOUNDER] Restore rehearsal #2** — this time from the automatic nightly backup, following the runbook.

**16.5 [AI + FOUNDER + TESTER] The accessibility audit (SPEC §16.5).** The gate that turns "we built it accessibly" into a claim you can defend. Over **every** page type — login, reset, invite redemption, feed, both composers, a profile (as friend, as FoF), discover, contact card, settings, every error and empty state.

**First, what should already be true when you arrive here (v1.22).** Two of these checks are not gates and have been running for months (§0.5): the **contrast test** since Step 8.2 and the **template smoke tests** since Step 2.5, on every step in between; and the **axe/`pa11y` scan** at every phase milestone. If any of that is red or has never been run, that is the finding — stop and fix it before booking anybody's afternoon, because a tester's time spent on defects a machine catches for free is the most expensive way this project can find them.

1. **[AI] Automated scan, final run.** axe/`pa11y` over the running site (a local dev tool, not an app dependency — ARCHITECTURE §9) plus the full template smoke-test suite. Fix everything it finds. It catches perhaps a third of real problems, and by now it should be finding almost nothing — a long list here means the milestone cadence was skipped.
2. **[FOUNDER + TESTER] Keyboard-only pass.** No mouse. Reach and operate everything with Tab / Shift-Tab / Enter / Space / arrows / Escape. Watching for: focus you cannot see, focus that jumps somewhere surprising, a control you can reach but not activate, and above all a **trap** you cannot Tab out of (the image overlay and the pickers are the likely offenders).
3. **[FOUNDER + TESTER] Screen-reader pass.** **This is the tester's pass and the reason there is a tester** (SPEC §16.5.1) — a screen-reader pass is a skill, not a setting, and a first-timer will miss real failures and chase false ones for hours. Post something, read a profile, add a contact item, hit a validation error. Listening for: unlabelled buttons ("button, button, button"), images announced as filenames, errors that are never announced, the audience-picker count going silent, and twenty identical "read more" controls in an element list (SPEC §16.3 requires each to be distinct — this pass is where that requirement is proved or not). **Your job in this pass is to watch and write down**, not to drive.
4. **[FOUNDER + TESTER] Zoom and reflow pass.** Browser zoom to 200% and a 320px-wide window: nothing clipped, nothing overlapping, no horizontal scrolling anywhere — **except** a preformatted post, which is the documented exemption (SPEC §16.3) and must still be scrollable by keyboard.
5. **[AI] Contrast gate.** The `THEME_SET` contrast test (Step 8.2) passes for every theme, including the viewer-override combinations. This is a confirmation, not a test run for the first time.
6. **[FOUNDER + TESTER] The operator console, bounded subset (v1.22).** About an hour, on the four surfaces you use weekly — moderation queue, request queue, vocabulary editor, URL allowlist editor. Only the four things SPEC §16.1.1 commits to: **keyboard-operable with no traps, visible focus, text contrast, labelled fields with errors in text.** Everything else about the Django admin is explicitly out of scope; do not let a thorough tester spend the afternoon there, and do not record what they find beyond the subset as a defect against the commitment.

**Then write the claim.** Anything found and not fixed goes into the accessibility statement (Step 15.2) as a stated known limitation — never quietly, **including anything the tester found that you cannot fix.** Fill in the statement's conformance claim, its verification date, and who ran which passes.

**And set the clock for next time.** SPEC §16.5's re-audit rule is what stops this being a one-off: the human passes repeat when a **new interactive pattern** ships (scoped to that pattern — a page built from existing partials is not a trigger), and in full **before any widening of who can join**. Both need this same person again, so confirm at the end of the session that they are willing to be called back, and put the rule itself into the runbook (§17.3 section 13) rather than into your memory.
✅ All six passes complete, findings either fixed or written into the statement, the statement dated and claiming only what was verified, and the re-audit rule recorded in the runbook.

**16.6 [FOUNDER] Break things on purpose (v1.20).** An untested alarm is a rumor in exactly the way an untested backup is, and it fails the same way — silently, and only when it matters. Four deliberate breakages on the production server, each undone immediately afterward:
1. **Stop the database container.** `/healthz` must return **503**, the site must show something honest rather than a stack trace, and Docker must not leave the app crash-looping (Step 5.4).
2. **Skip a job.** Move a job's last `job_runs` success back beyond its window and run `check_health`: the email must arrive, must name the job, and must contain **no post text and no traceback**.
3. **Trip the disk warning — by lowering the threshold, not by filling the disk.** Temporarily set the warning percentage below current usage and run `check_health`; the warning must fire. Do not manufacture a real 75% on a production server: filling the disk to test the disk alarm is how you cause the outage you were checking for.
4. **Stop the app container** and confirm Caddy's maintenance page appears with a **503**, then start it and confirm the site returns by itself.
✅ All four alarms fired, all four states were restored, and the alert emails carried counts rather than content. **Then confirm the negative case**: with everything healthy, `check_health` sends nothing at all — an alarm that fires on a good day gets muted, and a muted alarm is worse than none.

✅ *Phase milestone:* all six checks pass on the production server, and every alarm has been proven to fire at least once.

---

## Phase 17 — Launch to Friends [FOUNDER]

**17.1 [FOUNDER] Reset to zero.** Wipe all seed/test data (AI provides the command), create your real account via a bootstrap invite.
**17.2 [FOUNDER] Invite your first circle.** Your invite budget is the throttle by design. Tell invitees plainly what this is (the SPEC §1 pitch, in your own words) and that it's a prototype.
**17.3 [FOUNDER] Operate.** The weekly routine is now **reading one email** (v1.20). Step 5.7's digest arrives on its fixed day carrying every job's last success, disk percentage, the error count, and the results of `backup` and `verify_restore` — so the routine is: read it, then work the moderation/request queue in admin — **including the week's hashtag suggestions, read as a batch (section 12)** — and confirm OS updates applied. **A digest that does not arrive is itself the finding**, and the most important one the routine produces: the external watchdog is deferred to after launch (ARCHITECTURE §15 item 6), so until it exists a machine that has stopped sends no alarm — it just goes quiet, and you are the thing that notices.

**The operator runbook is still the AI's final Phase-17 task, and v1.20 specified its contents** rather than leaving them to a future session's judgment (**v1.21 adds section 12; v1.22 adds section 13**). One page per section, written for someone tired:

1. **First question: is it down, or is a job dead?** These are different emergencies with different pages, and confusing them wastes the night. *Down* = the site does not load, and someone told you. *A job is dead* = the site is perfectly fine and `job_runs` has an old last-success. **The second is the one that breaks a promise to users** (ARCHITECTURE §7.3).
2. **Triage, three commands:** `docker compose ps` · `docker compose logs --tail=200 app` · `df -h`. What each healthy answer looks like, printed beside it, so a wrong one is recognizable at 2 a.m.
3. **The restart ladder:** the app container, then the whole stack, then the machine. When to stop climbing and restore instead.
4. **Disk full.** What is safe to delete (Docker's image cache, old logs, the restic cache) and what is **never** deleted (the image folder, the Postgres volume). The Postgres-refuses-writes symptom, named, because it reads like database corruption and is not.
5. **The maintenance page:** turning it on before you start work, and off afterwards.
6. **Restore from backup**, two versions: onto this server, and onto a brand-new one — ending in the DNS repoint, which the 300-second TTL of Step 5.2 makes quick. **Where the keys are** (password manager, Step 5.6.2b) and never what they are.
7. **The silent case, in full:** how to read `job_runs` in admin, each job's expected window, how to run any job by hand, and how to tell "this job failed" from "**cron itself has stopped**" — the second looks like every job going quiet on the same day.
8. **Email provider down:** the site is fine, and nothing needs draining. Warnings retry by themselves, because a send is recorded only once accepted (ARCHITECTURE §7.2), so an outage delays an inactivity deletion rather than erasing somebody who was never warned.
9. **What does not require action at 2 a.m.:** almost everything. An overnight outage on a prototype for friends is survivable downtime (ARCHITECTURE §7.2, §7.4) — you decided nothing wakes you, and the runbook's job is to make the morning short, not the night long.
10. **Where this runbook lives:** in the repo *and* somewhere reachable when the server and the repo are not. A recovery runbook stored only on the machine it recovers is not a runbook.
11. **The one standing item: build the watchdog.** Deferred, not dropped (ARCHITECTURE §15 item 6). It goes on the runbook rather than into a phase above, because it is triggered by the platform being used rather than by a step being reached, and the runbook is the page you will actually still be reading a year from now. **Build it the first time any of these is true** — you are going public; there are active users you do not speak with in an ordinary week; or **a user tells you the site is down before you knew**, which is self-triggering and settles the question by itself. It is one free account and two monitors against `/healthz`, about twenty minutes, and **no code change**, because Step 5.7 built every part of it that lives in the application. Add the service to the privacy policy when you do (Step 15.1).
12. **The weekly vocabulary pass (v1.21).** In the same sitting as the moderation queue, read the hashtag suggestions (SPEC §13.5) — as a **batch, never one at a time**, because the batch is what makes the synonym clusters visible. Three outcomes and roughly this order of frequency: **it is a synonym for a tag we already have** → add it as a search alias to that tag and decline the suggestion, which fixes the miss permanently for every future user and is the outcome that keeps this queue from repeating itself (SPEC §11.2.1); **it is a genuinely missing interest** → add the tag, and write its aliases at the same time; **it is abusive, coded, or not an interest** → decline it, and nothing is sent to anybody either way. **No reply is ever sent and no interval was ever promised to users** — the cadence is yours, and it is stated here rather than in the product precisely so that missing a week costs an unread queue instead of a broken promise. **Being away is survivable and the documents say so** (SPEC §11.2.1): a frozen vocabulary delays a new interest, it never breaks an existing tag, an existing profile or an existing §11.3 gate. Come back and read the batch.

13. **Accessibility after launch (v1.22).** The section that stops SPEC §16 being something that was true in the week before launch. Six things live here, because BUILD_PLAN ends at Phase 17 and a rule that is not on this page does not exist.
    - **What must stay green, automatically:** the contrast test and the template smoke tests (§0.5). They run with every other test. If a change ever turns one red, that change is broken — the correct response is never to adjust the test.
    - **What repeats, and when.** The three human passes (Step 16.5) are re-run by the tester of Step 15.3: **when a new interactive pattern ships** — a picker, a dialog, an expandable, a reorder control, a new composer mode — **scoped to that pattern and the flows it appears in**; and **in full before any widening of who can join**, meaning a raise of the invite constants or any public phase, which is the same moment attorney review is required (Step 15.1), so book them together. **A new page built entirely from the existing shared partials is not a trigger** — that is the payoff for having used them. Keep the tester's contact details here, with the keys and the rest of what you will need when the repo is not reachable (section 10).
    - **Where a re-audit happens.** On the live system — there is one server and no staging copy — with the tester on **a member account whose only friend is you**. They see your content and nobody else's, which is what any member sees; no operator view is granted for testing. Where a pattern needs two people, the second is you.
    - **What is yours, once a year:** a keyboard-only and 200%/320px pass over the main flows, in the same sitting as the restore rehearsal below. It does not replace the tester's passes and is not claimed as one. Its job is different: the site stands still while browsers, iOS and VoiceOver move underneath it.
    - **The one queue item you do not batch.** An **"Accessibility problem"** report (SPEC §13.5) is not read with the weekly batch. Everything else in that queue can wait a week; this one is the signal that both the automated checks and the audit missed something, and it comes from the person being excluded — who will not send a second one. Fix the report, then re-audit the *pattern* it belongs to, not just the page.
    - **And update the statement** (Step 15.2) every time any of the above changes what is true. A conformance statement that is never revised becomes a false claim by standing still, which the honesty rule of SPEC §16.5 forbids as squarely as it forbids papering over a known defect.

**Plus one yearly item on that runbook: rehearse a restore by hand (v1.18).** Not "check that the backup ran" — actually restore the newest nightly backup onto your Mac and log into the restored copy, exactly as in Step 5.6 and following the same runbook. Backups fail loudly; **restores fail silently**, and what rots is the restore path (a schema that moved on, an expired storage credential, a rotated encryption key) and the runbook itself. The weekly `verify_restore` job catches most of that rot within a week, but it proves only that the server can read its own backups using credentials already in its own environment. The manual rehearsal is the only test of the case worth surviving: the server is gone, and you have a laptop, a runbook and nothing else — **which is why it uses the password-manager copy of the encryption key and nothing taken off the server** (Step 5.6.2b, v1.20). ARCHITECTURE §10's "an untested backup is a rumor" has a shelf life, and after launch the rumor restarts the day after the last test.
**17.4 [FOUNDER] Feed reality back.** Friends' confusions and wishes go through the in-app request form (§13.5) — you'll be reading your own moderation queue as its first user. Feature ideas flow back into SPEC amendments first, never straight into code.

🏁 *The prototype is live. Everything after this is SPEC v1.16+.*

---

## Appendix — Cross-Phase Rules for the AI Coding Models

Deliverable (d) will restate these in every prompt's preamble; they live here as the master copy **of the restatement, not of the rule**. Every rule below belongs to SPEC or ARCHITECTURE and cites its owner (SPEC §18): if one of these lines and the document it cites ever disagree, the cited document is right and the disagreement is a stop (§0.7), not a judgment call. The citation is also what tells you which document to change first when a rule genuinely has to move.

**Wherever a rule below says "stop and say so," it means §0.7's stop note (v1.23)** — the five-field block, printed in the chat, nothing applied and nothing committed. That is the defined form of stopping, and it is the same form for all of them.

1. SPEC.md and ARCHITECTURE.md are law. On any conflict between a prompt and those documents, stop and say so — **quoting the conflicting sentence verbatim**, or stating plainly that no sentence covers the case and naming the section where one would belong. A stop that points at no readable place in a named document is not a stop the founder can check, and §0.7 says what happens to it.
2. All visibility decisions call the visibility engine — never inline (ARCHITECTURE §5). Any diff that inlines a permission rule is wrong even if its output is correct today.
3. Reference `constants.py` names, never bare numbers.
4. Tests are written alongside each feature, in the same step, densest where bugs equal privacy breaches (ARCHITECTURE §9). **Every test cites the SPEC or ARCHITECTURE section it enforces, by number, somewhere a plain text search will find it** (v1.23) — in the test's name where that reads naturally, in a one-line comment where it does not. This is what makes §0.6's phase-milestone conformance check possible at all: the founder cannot read the code, but can read a list of section numbers and notice which ones are missing.
5. No third-party requests from any page: no CDNs, no external fonts, no embeds, no analytics (SPEC §15.2).
6. No new dependencies beyond the ARCHITECTURE §3 stack without the founder's explicit approval in the chat. **There are no standing exceptions** — Argon2id is not one, having been part of the §3 stack since v1.18 rather than an addition to it.
7. Every scheduled job is idempotent, runnable by hand, and **writes one `job_runs` row per run in a `finally` block** (ARCHITECTURE §6, §7.3) — a job that crashes must record a failure, never nothing. **A job that sends email records the send only once the provider accepted it**, so the next run retries instead of skipping.
8. UUIDs for anything URL-visible; every request permission-checked (SPEC §9.3).
9. **Every user-facing surface meets WCAG 2.1 Level AA (SPEC §16)** — in the step that builds it, never "later." Compose the shared accessible partials from Step 2.5 (`_field`, `_errors`, `_modal`, `_expandable`, `_status`); never hand-roll a form control, dialog, or status message. Semantic HTML before ARIA; real `<button>`s and `<input>`s, never clickable `<div>`s; a visible focus indicator on everything; text errors tied to their field; images with stored alt text; nothing conveyed by color alone; no auto-updating or focus-stealing content. If a feature seems to need an inaccessible pattern, stop and say so — that is a design conversation (§0.2 rule 5), not a coding decision. **And every step that adds a page adds it to the template smoke tests' page list (Step 2.5, v1.22)** — those tests are continuous, not a Phase 16 gate, and a page list that stopped growing in Phase 2 is a suite that passes forever while checking nothing.
10. **Every content save re-runs every content check** (SPEC §7.8 invariant 4). Validation belongs to the shared model/form layer that both the create and the edit path call — never to a create view. A check that runs only on creation is a defective implementation, and with the URL allowlist that defect is a security hole rather than a bug: it fails silently, with nothing to notice.
11. **Four things are rendered by one shared helper each, never reimplemented** (ARCHITECTURE §4): display names, relative timestamps, image alt text, and theme selection. The time helper emits the phrase **only** — no `title` attribute, no `<time datetime="…">`, no data attribute carrying the true timestamp (SPEC §7.5.1). If a surface seems to need a date formatted some other way, stop and say so; that is a design conversation, not a coding decision.
12. **No counters.** No unread badge, no follower count, no reaction count, no post count, no view count — SPEC §17 has none anywhere, and §12.2's rule is names overflowing to "and others." If a feature seems to need a number that describes people or attention, it is the wrong feature.
