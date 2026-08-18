# prompts/

One file per design conversation. Each is written to be **pasted whole into a fresh
session** — it carries its own context, so nothing is lost by starting cold. This follows
BUILD_PLAN §0.2 rule 4: long chats degrade, and self-contained prompts are the answer.

`../TODO.md` is the tracker. It says which prompts have been run, in what order they
should go, and what each one landed in.

## Running one

1. Check `../TODO.md` for the next prompt whose dependencies are met.
2. Open a fresh session in this repository.
3. Paste the prompt file's contents from the `---` divider down.
4. Work through it. Argue back where the prompt is wrong — several of these prompts
   contain judgments that deserve pushback, and a session that ends in "we looked and the
   current arrangement is right" is a legitimate outcome.
5. Before the session ends: CHANGELOG.md entry written, `../TODO.md` updated.

## Two kinds of session

**This now lives in BUILD_PLAN §0.7** (v1.23), which is where a build session will actually
read it. There are five law files — SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md, CHANGELOG.md
and `constants.py` — locked during build sessions and directed by the founder during design
sessions, which is what these prompts are.

One practical consequence for this folder: a prompt file **no longer has to declare its own
exemption** from BUILD_PLAN §0.2 rule 5 in its opening paragraph. Naming the files it may
edit is still worth doing, because it scopes the session; arguing for permission is not.

## Where stop notes go (v1.23)

The queue has a second inlet. When a build session hits a wall it prints a **stop note** —
five fields, BUILD_PLAN §0.7 — and stops without writing any file. It does **not** land
here. It goes into `../TODO.md`'s stopped-steps table, and it is already self-contained
enough to open a design session with: it names the step, quotes the sentence in the way,
says what could not be done, and proposes the smallest fix.

**Write a prompt file only when the question turns out to be bigger than the note** — when
it touches several sections, reopens a settled decision, or needs the finding-and-evidence
treatment below. That is the exception. Most stops should be answered from the note itself,
and a folder that grew a file for every stopped step would be its own kind of failure.

## Writing a new one

Keep the shape:

- **A header block** — what it touches, what it depends on, what the expected outcome is.
  Naming the expected outcome up front is what stops a session sprawling.
- **The finding, quoted.** If it came from a review, quote the reviewer. If the reviewer
  was partly wrong, say which part and why — that saves the next session from
  re-discovering it.
- **What was actually verified in the documents.** Section numbers and current wording.
  A prompt that describes a problem the documents already solved wastes a session.
- **Questions to work out**, numbered, with a recommendation where there is one.
- **Constraints** — the settled decisions the session must not reopen. This is the most
  useful part. Without it, every session relitigates the philosophy.
- **Before you finish** — changelog entry, TODO update, and permission to split the work
  out rather than finish it badly.

A prompt that grows past roughly two screens of questions should be two prompts.
