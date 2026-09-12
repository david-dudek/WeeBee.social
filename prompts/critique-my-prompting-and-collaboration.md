Act as a candid reviewer of *my* performance as the human running this project — not a reviewer of the code, and not of your own output.

Context: I recently ran `/insights` and liked how concrete its suggestions were. I want that same concreteness aimed at me. Do not assume you know what `/insights` produced — if you have no record of it, say so and design the critique on your own terms.

## 1. Before you start

- Tell me which evidence sources you can actually reach (past session transcripts, git history, project docs). Never claim access to a source you cannot read, and never invent quotes, commits, file paths, tool names, or capabilities.
- Estimate roughly how much reading this will take, and warn me up front if it will burn significant Claude Pro usage. Prefer sampling a representative set of sessions over exhaustively reading everything — and tell me what you sampled.
- Ask me any question whose answer would change the review (scope, time window, tone). Do not guess. If I have already answered it in this session, do not ask again.

## 2. Evidence

Base every claim on something you actually read: a session exchange, a commit message, or a line in CLAUDE.md / TODO.md / PLAN.md / prompts/ / the archetypes track. Cite the source for each finding (file:line, commit hash, or a short verbatim excerpt). A pattern needs at least two instances before you call it a pattern; with only one instance, label it a single observation.

## 3. What to critique — my behaviour, not yours

- How I write prompts and requests: clarity, scope, hidden assumptions, where I over- or under-specify.
- How I run the project: scope creep, unfinished threads, decisions I reopen, decisions I never close.
- How I use you: work I hand over that I should keep, work I do by hand that I should delegate, moments where I accept output without checking it.
- Process discipline: branch and file hygiene, verification habits, whether I follow my own CLAUDE.md rules.
- Wasted effort: things I have asked for more than once, rounds that produced nothing.

## 4. Output

- 800 words maximum. Count them before presenting and report the count.
- Ranked by impact, worst first. For each finding: **the pattern** (one line) → **evidence** (citation) → **what it costs me** → **the specific change**. For prompting habits, give the replacement wording verbatim.
- Then: three things I am doing well, one line each, so I do not stop doing them.
- Then: the single highest-leverage change, in one sentence.
- Mark each finding **[confident]** or **[uncertain]** according to the strength of the evidence. Where you are guessing, say so plainly rather than smoothing it over.
- Be blunt. Do not cushion, flatter, or pad with caveats. If the honest finding is "nothing major is wrong here", say that instead of manufacturing findings to fill the list.

## 5. Check your own work before presenting

Re-read your draft and strike: any claim you cannot point to evidence for, any advice generic enough to apply to anyone, and anything I already do. Then do exactly what is asked here and nothing more — no new files, no edits to the repo, no follow-up work beyond the review itself.
