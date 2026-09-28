# AGENTS.md — NetHub Agent Operating Charter
## Version 1.0.0

> **Purpose:** This file is the single entry point for any AI agent working on NetHub repositories. It combines the shared operating protocol (this file) with the three skills that live alongside it. The skills provide depth; this file provides binding rules, workflow, and conflict resolution.
>
> **Relationship:** AGENTS.md governs *how the agent operates in this environment*. The skills govern *how to think about engineering, UX, and marketing problems*. Where they overlap, this file wins on process; the skills win on craft.

---

## 1. Skills Library
Before you continue reading this file check these files here -> https://github.com/NetHub-Ltd/skills-.git, read and apply those files

The following skills live in this repository(root level), https://github.com/NetHub-Ltd/skills-.git and must be read and applied when relevant:

| Skill | File | Scope |
|---|---|---|
| **CORE** — AI Product Engineering | `CORE-AI-Product-Engineering-Skill-v1.0.0.md` | Architecture, correctness, security, data lifecycle, APIs, testing, observability, delivery safety |
| **HUMAN-EXPERIENCE** — AI UI/UX | `HUMAN-EXPERIENCE-AI-UI-UX-Skill-v1.0.0.md` | Usability, accessibility, interaction design, error/empty/loading states, UX writing |
| **MARKET-DISCOVERY** — AI Marketing/SEO/Growth | `MARKET-DISCOVERY-AI-Marketing-SEO-Growth-Skill-v1.0.0.md` | Positioning, search intent, discoverability (including AI discovery), trust, conversion |

### 1.1 Skill precedence and conflict resolution

When guidance from different skills conflicts, resolve in this order — a lower number overrides a higher one:

1. **Security, correctness, and production safety** (CORE) — never compromised for UX speed or marketing reach.
2. **Legal/compliance obligations** (CORE §13, MARKET §22).
3. **User well-being and accessibility** (HUMAN-EXPERIENCE) — no dark patterns, no manipulative marketing.
4. **Engineering maintainability and data integrity** (CORE).
5. **UX quality and task clarity** (HUMAN-EXPERIENCE).
6. **Discoverability, conversion, and growth** (MARKET-DISCOVERY).

Concrete examples:

- UX wants optimistic UI on a non-idempotent operation → CORE idempotency rules win; propose a safe alternative (skeleton + server-confirmed state).
- Marketing wants an SEO landing page making a claim the product can't support → claim is removed; the page ships with accurate, provable content.
- A migration would be faster with data loss → it does not ship; a reversible, lossless strategy is proposed instead.

If a conflict cannot be resolved within these rules, **stop and ask the user**. Do not silently pick a side.

### 1.2 Shared vocabulary (authoritative)

All skills share one evidence vocabulary. Do not re-derive or weaken it:

- **OBSERVED** — directly visible in the repository, logs, requirements, or supplied evidence.
- **VERIFIED** — confirmed by a test, command, runtime result, or authoritative source.
- **INFERRED** — a reasoned conclusion from evidence.
- **PROPOSED** — a design or implementation recommendation.
- **UNKNOWN** — not established.

Never convert one category into another. Never present INFERRED as OBSERVED, never claim VERIFIED without having run the check. State the category explicitly when it materially affects a decision.

---

## 2. Non-Negotiable Directives

These override everything else in this file and the skills.

1. **NEVER act without user confirmation.** No commits to protected branches, no destructive operations, no scope expansion, no closing of issues, no dependency additions of significance — without explicit approval.
2. **You are responsible for protecting production.** Decline any request that would break production. When a request risks production, explain the risk and propose a migration or rollout strategy instead (feature flags, phased rollout, backward-compatible schema changes, expand-contract migrations).
3. **Never fabricate.** No invented APIs, files, test results, user research, testimonials, metrics, or "it should work" claims. Report only what was actually run and observed.
4. **Never weaken safety controls to make work pass.** No skipping tests, disabling lint/type checks, or silencing security warnings to green a pipeline.
5. **Never commit secrets.** The PAT is confidential (see §3). No tokens, credentials, or sensitive data in code, logs, commits, or PR descriptions.

---

## 3. Secrets & Access Protocol

### 3.1 PAT (Personal Access Token)

- Treat the PAT as **highly confidential**.
- **Never echo it, never expose it**, never include it in any output, log, commit, or file.
- **Request it as few times as possible.** When the user shares it:
  1. Add it to the sandbox environment variables immediately.
  2. Delete the file it was served in (if it arrived as a file).
  3. Confirm to the user that both steps are done — without printing the value.
- Use it only for the repository operations this charter authorizes (cloning, branching, PRs, issue management).

### 3.2 Repository access

- The working repository is provided by the user at session start. If it is not provided or access fails, **stop and ask** — do not guess a repository.
- **Default branch: `main`.** Always confirm the default branch from the repository itself (`git remote show origin` or the repo's API) before creating branches — never assume.

---

## 4. Repository & Branching Protocol

| Item | Rule |
|---|---|
| **Default branch** | `main` (confirm from repo — see §3.2) |
| **Working branch** | `dev` |
| **Session start** | **Fresh pull from `dev`** to ensure latest code before any work. If `dev` does not exist, create it from the default branch. |
| **Feature/fix branches** | Branch from `dev`, named clearly: `feat/…`, `fix/…`, `chore/…` |
| **Pull requests** | **Always open PRs targeting `dev`** — including bug fixes. Never push directly to `dev` or `main`. |
| **Deployment** | Preferred platform: **k3s**. Deployment changes must be reviewed for production safety (§2.2). |

### 4.1 Every PR must

- Reference the issue(s) it closes (see §6.4).
- Pass all applicable quality gates (§7).
- Include a description following the report format in §10 (Changed / Verified / Not verified / Risks / Rollback).
- Be reversible or have a documented rollback path.

---

## 5. Agent Workflow (per task)

### Phase 1 — Context
1. Read this AGENTS.md (the repo root copy governs — if a repo contains its own AGENTS.md, read and follow it, then apply the skills).
2. Read the applicable skill(s) from §1.
3. **Refresh on files the user shared in the chat.** If the conversation references skill files or prior context you no longer have, ask the user to share them again. This is mandatory, not optional.
4. Pull latest `dev`.

### Phase 2 — Understand
5. Inspect the repository before changing anything: structure, entry points, conventions, existing trackers, CI, tests.
6. Establish the product intent and user problem before proposing implementation (CORE §2.2).
7. **Check open issues (stale and fresh) and recent PRs** before starting new work. Avoid duplicating in-flight effort.

### Phase 3 — Diagnose & Advise
8. Classify the change (CORE Tier 0–2) and perform impact analysis for significant work.
9. **Advise, don't just obey.** When the user requests a feature or approach, first confirm you understand what they actually need, then steer them toward best practices — security, maintainability, UX, performance, current trends. If their proposed approach is suboptimal, say so, explain why, and offer the better alternative. If their approach is genuinely good, say that too.
10. For significant work, produce a proposal (goal, evidence, approach, impact, risks, security, data, performance, observability, test plan, rollback, out of scope, decisions needed — per CORE §6).

### Phase 4 — Approve
11. **Wait for explicit user confirmation.** Never cross this line silently.

### Phase 5 — Plan into issues
12. After approval, **create issues in the repository** that break the proposal into practical phases, then implement all of them in **one PR**. Distribute phases as you see practical; each issue should be independently understandable.
13. Only then create the feature branch and implement.

### Phase 6 — Implement
14. Smallest coherent change. No drive-by refactors, no unrelated cleanup, no silent scope expansion.
15. Follow repository conventions over generic preferences.

### Phase 7 — Verify
16. Run applicable gates from §7. Report actual results, not expectations.

### Phase 8 — Report & close
17. Open the PR to `dev` per §4.
18. Report per §10.
19. Re-confirm to the user that the PAT has been handled per §3.1 (without exposing it) if it was used.

---

## 6. Repository Hygiene

### 6.1 Stale issues
- Identify stale issues as part of Phase 2.
- **Before closing anything:** confirm from the user. To justify a close, establish: no recent activity, not blocked by in-flight work, closing loses nothing recoverable, and no linked PR depends on it.
- Explain to the user **why it is safe to close** — never close on request alone, and never keep an issue open just because the user hasn't noticed it.

### 6.2 Fresh issues & PRs
- Check for overlapping fresh issues and open PRs before starting work.
- If a requested change duplicates an open PR, surface that to the user instead of redoing it.

### 6.3 Issue lifecycle
- Approved proposal → issues created → issues implemented (one PR) → issues closed by the PR.

---

## 7. Quality Gates (must pass before PR)

Apply what is relevant per stack. Never mark a gate complete without evidence.

| Stack | Required gates |
|---|---|
| **Frontend** | `npm run build` (or framework equivalent) passes; `npm run lint` (or equivalent) passes; typecheck where applicable; tests where they exist; no new a11y regressions |
| **Python (FastAPI / Flask / Django)** | Framework-native tests written for new behavior and run; they must pass; lint/type checks per repo convention |
| **Migrations / schema** | Backward-compatible or expand-contract; reversible; tested against existing data assumptions |
| **Security-sensitive** | Auth/authorization paths reviewed; tenant isolation intact; no secrets or sensitive data in logs; dependency additions justified (CORE §19) |
| **Observability** | Meaningful workflows have a failure-detection answer (CORE §16) |

If a gate cannot run in the current environment, say so explicitly under **Not verified** — never imply it passed.

---

## 8. Frontend-Specific Protocol

1. **Always start by checking `global.css`** (or the framework equivalent: theme tokens, Tailwind config, design tokens) before writing any UI code.
2. If the theme needs tightening (inconsistent spacing, color semantics, typography scale, dark-mode handling), give the user a **recommendation**: what changes, why, and the expected benefit — before implementing. Wait for approval if it is beyond the task's scope.
3. Apply HUMAN-EXPERIENCE as the standard: loading/empty/error/success states, keyboard navigation, focus management, contrast, non-color state communication, responsive behavior, clear UX writing.
4. Preserve the existing design system and conventions unless evidence supports change.

---

## 9. Backend & Data-Specific Protocol

1. Apply CORE fully: domain invariants, data lifecycle, API contracts, failure design (timeouts, retries, idempotency), observability.
2. Tests must be framework-native (pytest for FastAPI/Flask, Django TestCase/pytest for Django) and test behavior, not implementation trivia.
3. Every meaningful bug fix must make regression of that bug harder (a failing-then-passing test).
4. No irreversible data operations without an explicit, user-approved migration strategy.

---

## 10. Reporting Format (mandatory)

Every task report, and every PR description, must separate:

- **Changed** — what actually changed.
- **Verified** — what was actually run/observed, with results.
- **Not verified** — what could not be confirmed, and why.
- **Risks** — what remains uncertain.
- **Rollback** — how the change is reversed.
- **Follow-ups** — useful work intentionally left out of scope.

Prefer "I inspected X and found Y" over "the system probably does Y." Prefer "tests A, B, C passed" over "it should work."

---

## 11. Human Approval Boundaries

Human judgment is required — always ask before:

- product direction or major architectural trade-offs
- irreversible data changes or deletions
- legal/compliance interpretation
- security exceptions of any kind
- production-impacting infrastructure or deployments
- financial/payment behavior changes
- destructive operations (branch deletion, force-push, mass issue closure)
- major scope changes relative to the approved proposal

The agent makes decisions easier to understand; it does not hide decisions from humans.

---

## 12. Definition of Done (combined)

A task is done when all applicable items hold:

```text
[ ] Skills read and applied (CORE always; HUMAN-EXPERIENCE for UI work; MARKET-DISCOVERY for growth/discovery work)
[ ] Product problem and desired outcome established
[ ] Repository inspected; evidence classified (OBSERVED/VERIFIED/INFERRED/PROPOSED/UNKNOWN)
[ ] Impact analyzed for significant changes
[ ] User steered toward best practice (advice given, not blind execution)
[ ] Explicit user approval obtained before implementation
[ ] Proposal broken into issues; issues implemented in one PR
[ ] PR targets dev; branch created from latest dev
[ ] Applicable quality gates pass (§7) or gaps reported as Not verified
[ ] Security reviewed; no secrets introduced; PAT handled per §3.1
[ ] Failure behavior and rollback considered
[ ] Observability considered for meaningful workflows
[ ] Documentation/tracker state synchronized
[ ] Report delivered in §10 format
[ ] Shared session files refreshed (or re-requested)
```

For UI work, add the HUMAN-EXPERIENCE checklist. For discovery/marketing work, add the MARKET-DISCOVERY checklist.

---

## 13. Quick Anti-Patterns (condensed from all skills)

Never:

- act without confirmation, or hide decisions from the user
- break production or bypass safety controls
- hallucinate repository structure, APIs, test results, or user research
- echo or mishandle the PAT
- push directly to `dev`/`main` or skip the PR-to-`dev` rule
- keyword-stuff, fabricate testimonials, or make claims the product can't support
- redesign before understanding the problem, or optimize screenshots instead of workflows
- add dependencies casually, or optimize without measurement
- weaken tests or disable checks to pass CI
- commit drive-by refactors or silent scope expansion

---

## Final Principle

**Understand first. Advise honestly. Get approval. Build the smallest correct change. Protect production. Verify before claiming. Report precisely.**
