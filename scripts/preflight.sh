#!/bin/bash
# preflight.sh - git and repo sanity checks before any work
# Usage: ./scripts/preflight.sh [expected-branch]
#
# Checks: working tree status, current branch, last 3 commits, divergence from origin/main
# Aborts with nonzero exit if working tree is dirty or if expected-branch is specified and doesn't match.

set -euo pipefail

EXPECTED_BRANCH="${1:-}"
CURRENT_BRANCH=$(git branch --show-current)
STATUS=$(git status --porcelain)

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  PREFLIGHT CHECK"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

echo ""
echo "Branch: $CURRENT_BRANCH"
echo "Status: $([ -z "$STATUS" ] && echo "clean ✓" || echo "DIRTY ✗")"

if [ -n "$EXPECTED_BRANCH" ] && [ "$CURRENT_BRANCH" != "$EXPECTED_BRANCH" ]; then
  echo ""
  echo "❌ ERROR: Expected branch '$EXPECTED_BRANCH' but on '$CURRENT_BRANCH'"
  exit 1
fi

if [ -n "$STATUS" ]; then
  echo ""
  echo "❌ ERROR: Working tree has uncommitted changes:"
  echo "$STATUS"
  echo ""
  echo "Stash them first: git stash -u"
  exit 1
fi

echo ""
echo "Recent commits:"
git log --oneline -3

echo ""
echo "Divergence from origin/main:"
if git rev-parse origin/main >/dev/null 2>&1; then
  DIVERGE=$(git rev-list --count origin/main..$CURRENT_BRANCH 2>/dev/null || echo "0")
  BEHIND=$(git rev-list --count $CURRENT_BRANCH..origin/main 2>/dev/null || echo "0")
  echo "  Ahead of origin/main: $DIVERGE commits"
  echo "  Behind origin/main: $BEHIND commits"
else
  echo "  origin/main not found (offline or new repo)"
fi

echo ""
echo "✓ Preflight passed"
echo ""
