# Repo instructions for Claude Code

This file is auto-loaded by Claude Code whenever it runs inside this folder
(C:\Users\Chahat\Documents\01-Journal, repo: ChahatBeniwal04/OnboardingTasks).

## When I say "push my updates" (or similar: "push this", "commit and push", "update GitHub")

Follow this exact sequence. Do not skip steps or combine them silently.

1. Run `git status` and show me the result before doing anything else.
2. Run `git diff` on any modified tracked files and give me a one-line summary
   of what changed per file.
3. Stage files individually or by clear intent (e.g. `git add <file>`).
   Do NOT use `git add -A` or `git add .` unless I've confirmed every
   untracked file listed in status should be included.
4. Propose a commit message summarizing the *why*, not just the *what*.
   Show it to me before committing.
5. Run `git commit -m "<message>"`.
6. Before pushing: run `git status` again and confirm the local branch is
   `main` and not behind the remote (fetch first if unsure: `git fetch origin`
   then compare). If local is behind, STOP and tell me — do not pull-merge
   or push automatically.
7. Run `git push origin main`.

## Hard stops — always flag these explicitly before running, never run silently

- Any `git push --force` or `git push -f`
- `git reset --hard`
- `git checkout -- <file>` or `git restore` that would discard uncommitted changes
- Pulling when there are uncommitted local changes that could conflict
- Any rewrite of shared/pushed history (rebase of already-pushed commits, amend of a pushed commit)

If a push is rejected because the remote has commits I don't have locally,
explain that plainly, run `git pull origin main` to merge them in, help me
resolve any conflicts, and only then push — never force past it.

## General style

- Keep me informed of each command before running it, not just after.
- If `git status` shows anything unexpected (unrelated files changed, wrong
  branch, detached HEAD), stop and ask rather than guessing.
