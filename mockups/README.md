# mockups/

Browser-viewable mockups of WeeBee exactly as `SPEC.md` and `ARCHITECTURE.md` describe it,
built session by session (see `prompts/mockups/`) so the founder can look at the platform
before approving those documents — static HTML and one hand-written stylesheet, no
JavaScript, nothing loaded from anywhere off this machine. `pages/*.html` holds each mockup's
body content; `partials/` holds the shared shell and the accessibility-unit fragments pages
compose; `build.py` (stdlib only) expands both into full pages under `site/`, which is
generated and gitignored. To rebuild after editing anything in `pages/`, `partials/`, or
`styles.css`, run:

```bash
python3 build.py
```

from this directory, then open `site/index.html` in a browser (`file://` works fine — nothing
here needs a server). `CRIB.md` holds the constants, verbatim interface strings, sample cast,
and relative-age phrases every session draws from; `NOTES.md` is the running log of places the
design documents were silent and something had to be drawn anyway.
