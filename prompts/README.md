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

The project runs two kinds of AI session, and they have opposite rules about the law
files (SPEC.md, ARCHITECTURE.md, BUILD_PLAN.md, `constants.py`):

- **Build sessions** — driven by a BUILD_PLAN step. The law files are locked, by tool deny
  rules, a pre-commit hook and a tripwire test (BUILD_PLAN §2.4). An AI that wants to
  change one must stop and say so.
- **Design sessions** — these prompts. The founder directs changes to the law files, so the
  lock does not apply. Each prompt file states this at the top, because a session that has
  read BUILD_PLAN §0.2 rule 5 will otherwise refuse to edit anything.

Prompt 07 exists to write this distinction into BUILD_PLAN itself, since at present it
lives only here.

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
