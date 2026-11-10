# NetHub Agent Skills — Start Here

**Repository:** https://github.com/NetHub-Ltd/skills-

This repository is the shared engineering and product-quality standard for agents working on NetHub projects. It exists so agents apply established professional practices independently—not so the user has to teach software engineering fundamentals in every task.

## Instructions for the agent

**Before doing project work, read and apply the complete skills repository. Do not stop at this README.**

1. Inspect the current repository root and identify every instruction and skill document. Do not rely on this file's list alone; the repository may have changed.
2. Read the complete current contents of:
   - `AGENTS.md` — operating rules, repository workflow and approval boundaries.
   - `CORE-AI-Product-Engineering-Skill-*.md` — engineering foundation; always applicable to engineering work.
   - `FRONTEND-AI-Frontend-Engineering-Skill-*.md` — frontend architecture, browser implementation, performance and security.
   - `HUMAN-EXPERIENCE-AI-UI-UX-Skill-*.md` — user journeys, interaction quality and accessibility.
   - `VISUAL-DESIGN-Skill-*.md` — visual direction, design systems and reference-grounded design.
   - `VISUAL-QA-Skill-*.md` — rendered-interface verification.
   - `MARKET-DISCOVERY-*.md` — market, positioning, SEO and growth.
   - `COMMERCIAL-PRODUCT-*.md` — monetisation, pricing, conversion, retention and unit economics.
   - `PRIVACY-DATA-GOVERNANCE-*.md` — data governance, privacy, cookies, consent and analytics.
3. Read every other relevant instruction or skill file currently present. Read full documents, not just search snippets, summaries, headings or selected excerpts. Resolve conflicts using the repository's stated precedence.
4. Select the skills relevant to the task and apply them together. CORE is the engineering foundation; specialist skills own their defined disciplines. Do not load unrelated material into every reasoning step, but do not skip the initial repository-wide read.
5. Then inspect the actual project repository and its own instructions, code, tests, CI, configuration and deployment conventions before making code-level judgments or changes.

## Source access is not the same as repository access

A GitHub connector may expose only metadata, search results, selected files or file-write actions. **Do not assume it gives you the complete source code, a local workspace, shell access or the ability to run tests.**

Establish what you can actually access:

- If you have a complete checkout and can inspect files and run commands, inspect the project directly.
- If you have a complete source archive but no runtime, inspect the source and clearly report which checks cannot run.
- If you only have partial connector access, do not pretend you have inspected the codebase. Explain the limitation and ask the user for a repository ZIP/archive or another complete source-delivery method before code-level work.
- Request a snapshot for the intended branch/commit where possible. It should include source, manifests and lockfiles, configuration examples, migrations, tests, CI and deployment files, nested instructions and required submodule content.
- Never ask the user to include secrets, environment files, private keys, credentials, production data, dependency caches or generated build artifacts.

A repository listing, README, code-search result or handful of fetched files is not a complete source inspection. Do not implement against unseen architecture. If command execution is unavailable, do not claim tests, builds, type checks or runtime behavior were verified.

## How to work

- Inspect first; use evidence from the actual repository.
- Understand the requested outcome and trace the affected system end to end.
- Make routine engineering decisions autonomously when requirements and evidence are sufficient. Do not create unnecessary approval loops.
- Ask only for genuine human decisions, missing requirements, unavailable source/access, permission boundaries or material unresolved risk. Follow the binding approval rules in `AGENTS.md`.
- Prefer secure, maintainable, typed, observable and proportionate solutions. Avoid speculative abstractions and unnecessary infrastructure.
- Test behavior and failure paths appropriate to the risk. Never weaken tests or safety controls to get a green result.
- Treat issue/PR tracking as mandatory: create or update an actionable issue before implementation, record exact file/symbol before→after changes, acceptance criteria and tests, keep agent-independent handoff state, and make the PR close the issue on merge. The final tracker completion update waits until the PR is open and all required CI gates are green.
- The implementing agent owns CI after every push: track checks for the exact latest SHA, monitor them to completion, diagnose and fix failures, push corrections and repeat. Never ask the user to review a PR until every required CI gate is green, tracker state is current and all covered issues have automatic close keywords. Missing/pending CI is blocked, not passed.
- Test changed executable behavior wherever meaningful, prefer unit tests for isolated logic, and use the correct higher-level test boundary where appropriate. Minimise unrelated code changes and wasted compute without skipping required gates.
- Review the final diff. Report **Changed**, **Verified**, **Not verified**, **Risks** and **Follow-ups** accurately. Never claim work or checks that did not happen.

## Skill ownership

| Skill | Primary responsibility |
|---|---|
| CORE | Engineering correctness, architecture, backend, APIs, data, security, testing, performance, reliability, observability and delivery |
| FRONTEND | Next.js/React architecture, browser implementation, rendering, state, security and frontend performance |
| HUMAN-EXPERIENCE | User goals, journeys, usability, interaction behavior and accessibility |
| VISUAL-DESIGN | Visual language, design systems, visual references and implementation-ready design rules |
| VISUAL-QA | Evidence-based verification of rendered UI across routes, states, themes and viewports |
| MARKET-DISCOVERY | Market understanding, positioning, search intent, SEO, acquisition and growth |
| COMMERCIAL-PRODUCT | Monetisation, pricing, conversion, retention, analytics and unit economics |
| PRIVACY-DATA-GOVERNANCE | Data inventory, lawful processing, cookies, consent, rights, retention and privacy risk |

**Do not ask the user to repeat information already available in the repository or conversation. Do not confuse confident reasoning with verified evidence. Understand the real system, apply the right skills, and deliver work that can be independently checked.**
