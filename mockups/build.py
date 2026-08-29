#!/usr/bin/env python3
"""Builds mockups/site/ from mockups/pages/*.html + mockups/partials/_base.html.

Stdlib only, no dependencies, no watch mode. Two directives:
  {{include path/relative/to/mockups/dir.html}}   expanded recursively
  {{var_name}}                                     substituted from a page's
                                                    own front-matter lines

A page file may start with any number of front-matter lines of the form
  {{var title=Some page title}}
before its body content begins. Everything from the first non-front-matter
line onward is the page body, dropped into {{content}} in _base.html.

Run: python3 build.py   (from the mockups/ directory, or anywhere - paths
are relative to this file.)
"""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
PAGES_DIR = ROOT / "pages"
PARTIALS_DIR = ROOT / "partials"
SITE_DIR = ROOT / "site"

INCLUDE_RE = re.compile(r"\{\{include\s+([^\}]+?)\s*\}\}")
FRONT_MATTER_RE = re.compile(r"^\{\{var\s+(\w+)=(.*)\}\}\s*$")
VAR_RE = re.compile(r"\{\{(\w+)\}\}")


def expand_includes(text: str) -> str:
    def replace(match: re.Match) -> str:
        included_path = ROOT / match.group(1).strip()
        return expand_includes(included_path.read_text(encoding="utf-8"))

    previous = None
    while previous != text:
        previous = text
        text = INCLUDE_RE.sub(replace, text)
    return text


def split_front_matter(raw: str) -> tuple[dict, str]:
    variables = {}
    lines = raw.splitlines(keepends=True)
    body_start = 0
    for line in lines:
        match = FRONT_MATTER_RE.match(line)
        if not match:
            break
        variables[match.group(1)] = match.group(2)
        body_start += 1
    return variables, "".join(lines[body_start:])


def substitute(text: str, variables: dict) -> str:
    return VAR_RE.sub(lambda m: variables.get(m.group(1), m.group(0)), text)


def build() -> None:
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir()

    # Session M8: mockups/pages/emails/ holds platform email templates, each an
    # .html + .txt pair. Emails are copied through unwrapped, the same
    # treatment maintenance.html already gets below and for the same reason:
    # a real WeeBee email is never delivered inside the web app's own header,
    # navigation or stylesheet, and SPEC §16.3 itself places email "outside
    # WCAG's scope for pages" -- wrapping one in _base.html would link
    # styles.css into markup that has to demonstrate it is legible WITHOUT a
    # stylesheet, which is the opposite of what this session's build
    # instructions ask for. This is the one other place in the M1-M8 track
    # (besides maintenance.html) where build.py itself is extended rather
    # than only pages/ -- see mockups/NOTES.md.
    emails_dir = PAGES_DIR / "emails"
    if emails_dir.is_dir():
        site_emails_dir = SITE_DIR / "emails"
        site_emails_dir.mkdir(exist_ok=True)
        for email_path in sorted(emails_dir.iterdir()):
            if email_path.is_file():
                shutil.copy(email_path, site_emails_dir / email_path.name)
                print(f"copied emails/{email_path.name} (standalone, not wrapped in _base.html)")

    base_template = expand_includes((PARTIALS_DIR / "_base.html").read_text(encoding="utf-8"))

    for page_path in sorted(PAGES_DIR.glob("*.html")):
        if page_path.name == "maintenance.html":
            # Lives in Caddy in the real deployment, entirely outside the
            # Django app's page set (ARCHITECTURE §7.2) -- must not share
            # _base.html's stylesheet link or nav, so it is copied through
            # as-is rather than wrapped. Added in session M7 (see
            # mockups/NOTES.md); every other page still gets the standard
            # wrapping below.
            shutil.copy(page_path, SITE_DIR / page_path.name)
            print(f"copied {page_path.name} (standalone, not wrapped in _base.html)")
            continue
        variables, body = split_front_matter(page_path.read_text(encoding="utf-8"))
        variables.setdefault("title", "WeeBee mockup")
        variables["content"] = expand_includes(body)
        output = substitute(base_template, variables)
        (SITE_DIR / page_path.name).write_text(output, encoding="utf-8")
        print(f"built {page_path.name}")

    shutil.copy(ROOT / "styles.css", SITE_DIR / "styles.css")
    print(f"copied styles.css -> {SITE_DIR / 'styles.css'}")


if __name__ == "__main__":
    build()
