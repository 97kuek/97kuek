# CLAUDE.md

This file gives guidance to Claude Code when working in this repository.

## Repository purpose

This is the GitHub profile repository for `97kuek` (Keitaro Ueki). The repository name matches the username, so `README.md` is rendered at the top of the GitHub profile page (https://github.com/97kuek).

The README is a styled, image-driven profile page: a header, stat cards, a curated project list, a 3D contribution graph, and a contribution activity graph.

## Structure

- `README.md` - profile page content (the main deliverable).
- `.github/workflows/profile3d.yml` - GitHub Actions workflow that regenerates the 3D contribution graph daily and commits the result.
- `profile-3d-contrib/` - auto-generated 3D contribution graph SVGs. Do not edit these by hand; the workflow overwrites them.
- `.gitignore` - excludes local tooling directories such as `.claude/`.

## Conventions

- Do not use emojis anywhere: not in `README.md`, not in `CLAUDE.md`, and not in commit messages.
- Light mode only. Use a single unified palette (sage green) across every card and graph:
  - background `#ffffff`
  - title `#2DA44E`
  - icon / accent `#57A65A`
  - body text `#2F4858`
  - muted text `#8B949E`
  - no card borders (`hide_border=true`)
- When adding or changing any external card (github-readme-stats, top-langs, streak-stats, activity-graph, etc.), reuse the exact palette parameters above so the page stays visually consistent.
- Layout is centered with inline HTML (`<div align="center">`, `<img>`, `<h2>`). The markdownlint warnings MD033 (inline HTML) and MD041 (first line not a heading) are expected and acceptable for a styled profile README; do not "fix" them by removing the HTML.
- Section headings are plain text with no leading emoji.

## Auto-generation

- The files under `profile-3d-contrib/` are produced by `profile3d.yml` (action `yoshi389111/github-profile-3d-contrib`) and committed by the workflow. Regenerate by pushing to `main`, or via the Actions tab using Run workflow.
- The README references `profile-3d-contrib/profile-season-animate.svg` for the 3D graph. Other generated variants (night-rainbow, gitblock, green-animate, etc.) are available in the same directory if a different style is desired.
- The previous "Detailed Metrics" card and its `metrics.yml` workflow have been removed. Do not reintroduce them unless explicitly requested.

## Profile facts

- Name: Keitaro Ueki
- Role: AI Engineer
- Portfolio: https://97kuek.github.io/
- University: Waseda University (https://www.comm.waseda.ac.jp/)
- Internship: neoAI (https://neoai.jp/)
- Core stack shown: Python, C/C++, Arduino, MATLAB, TypeScript, Astro
