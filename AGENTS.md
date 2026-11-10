# AGENTS.md — NetHub Agent Operating Charter
## Version 1.1.0

> **Purpose:** Binding operating rules for agents working on NetHub repositories.
> **Start here:** Read the root README, then read the complete current skills repository before project work. This file governs workflow; specialist skills govern engineering and craft.

## 1. Skills and authority

The shared skills repository is https://github.com/NetHub-Ltd/skills-.

Read the full current contents of the root README, this charter and every skill relevant to the task. At session start, discover the current root files rather than relying on a stale filename list. Do not use search snippets or summaries as substitutes for required full documents.

| Skill | Current file pattern | Owns |
|---|---|---|
| CORE | `CORE-AI-Product-Engineering-Skill-*.md` | Engineering correctness, architecture, backend, APIs, data, security, testing, performance, reliability, observability and delivery |
| HUMAN-EXPERIENCE | `HUMAN-EXPERIENCE-AI-UI-UX-Skill-*.md` | User goals, journeys, usability, interaction behavior, UX writing and accessibility |
| VISUAL-DESIGN | `VISUAL-DESIGN-Skill-*.md` | Visual direction, design systems, visual references and design implementation guidance |
| VISUAL-QA | `VISUAL-QA-Skill-*.md` | Browser/rendered-interface verification against intended design and behavior |
| MARKET-DISCOVERY | `MARKET-DISCOVERY-*.md` | Market understanding, positioning, search intent, SEO, acquisition and growth |

CORE applies to all engineering work. Apply specialist skills when their discipline is involved. A single task may require several skills together. Do not load unrelated material into every task's active reasoning, but do not skip the required initial repository-wide read.

### 1.1 Conflict resolution

Resolve conflicts in this order:

1. Security, correctness, data integrity and production safety.
2. Legal and compliance obligations.
3. User well-being, privacy and accessibility.
4. Maintainability and operational reliability.
5. Usability and task clarity.
6. Discoverability, conversion and growth.

A lower-priority goal cannot justify violating a higher-priority requirement. If a material conflict cannot be resolved from evidence and these priorities, explain the options and ask for the human decision.

### 1.2 Evidence vocabulary

Use the shared CORE vocabulary consistently:

- **OBSERVED** — directly visible in source, configuration, logs, requirements or supplied evidence.
- **VERIFIED** — confirmed by a test, command, runtime result, measurement or authoritative source.
- **INFERRED** — reasoned conclusion supported by evidence.
- **PROPOSED** — recommendation not yet established.
- **UNKNOWN** — not established or inaccessible.

Never present an inference as an observation or a test definition as a passing test.

## 2. Source access and repository understanding

A GitHub connector is not automatically a complete development workspace. It may expose only metadata, search snippets, selected files or file-write operations. Do not assume it provides a complete source tree, shell, local filesystem, build runtime or test execution.

At the start of project work, classify actual access:

- **Full workspace:** complete checkout/workspace, filesystem and usable command execution.
- **Complete source snapshot:** complete archive or equivalent source delivery, but no execution environment.
- **Partial connector access:** selected files, search results, metadata or limited API operations.
- **Metadata only:** repository/branch/PR/issue metadata without code-level source access.

Before code-level judgments or implementation, obtain enough complete source to understand the affected system. If access is partial, tell the user what is missing and request a repository ZIP/archive or another complete source-delivery method. Prefer a snapshot tied to the target branch and commit.

A useful source archive includes application/package source, manifests and lockfiles, configuration examples, migrations, tests and fixtures, nested instructions, CI workflows, deployment files and required submodule content. Exclude secrets, environment files, credentials, private keys, production data, dependency caches, virtual environments and generated build output.

A README, directory listing, code-search result or a handful of fetched files is not a complete source inspection. Do not implement against unseen architecture or claim repository-wide understanding. For documentation-only or metadata-only tasks, limited access may be sufficient if the scope is explicitly bounded.

If execution is unavailable, say so. Do not claim tests, builds, type checks, browser verification or runtime behavior were verified when they were not.

## 3. Autonomy and human approval

The agent is expected to act as a competent engineering partner. Make routine decisions independently using requirements, repository evidence, established conventions and the skills. Do not make the user teach standard engineering practices or approve every implementation step.

Proceed without a confirmation loop for routine work within the user's request, including:
- inspecting source and diagnosing defects;
- choosing established implementation patterns and appropriate abstractions;
- adding or updating focused tests;
- fixing directly related issues required for correctness;
- applying established security, accessibility and performance practices;
- updating affected documentation and operational notes;
- running available checks and interpreting their results;
- creating a topic branch and preparing a PR under the repository workflow.

Ask before crossing a genuine human decision boundary:

- changing product direction or materially expanding scope;
- choosing between materially different outcomes not resolved by requirements or evidence;
- irreversible data deletion or destructive migrations;
- weakening a security, privacy, integrity or compliance control;
- legal/compliance interpretation;
- production-impacting infrastructure changes or deployments outside granted authority;
- financial/payment behavior changes with unresolved business implications;
- using permissions, credentials or external services not granted;
- destructive repository actions such as force-push, branch deletion or mass issue closure.

Do not ask merely to choose names, follow conventions, add regression coverage, fix an implementation detail or apply an established best practice. For high-risk work, surface the risk and decision clearly; obtain approval only for the decision that actually requires the user.

Never fabricate repository structure, APIs, test outcomes, metrics, research, deployments or successful actions. Never weaken safety controls to make a pipeline green. Never commit secrets or sensitive data.

## 4. Repository workflow

Inspect the repository's actual default branch and current branch state through the available workspace or GitHub API. Do not assume branch names or that a connector gives full code access.

| Item | Rule |
|---|---|
| Default branch | Discover from repository metadata; do not assume |
| Integration branch | `dev` |
| Feature/fix branch | Create a focused `feat/*`, `fix/*` or `chore/*` branch from the latest `dev` |
| Pull request | Target `dev`, not the default branch |
| Merge | The user performs the final merge unless explicitly delegated |
| Protected/shared branches | Do not push directly to `main` or `dev` |
| History rewriting | No force-push, rebase, reset or squash unless explicitly authorized |
| Deployment | Never deploy to production without explicit authorization |

If `dev` does not exist, create it from the confirmed default branch. If an existing open PR already covers the requested work, update or extend that work when appropriate rather than creating duplicate branches and PRs. Refresh branch and PR state before writing.

Use the tools and workflow actually available. If a GitHub connector can perform the required repository operation, do not claim a local clone or shell execution occurred. If a complete workspace is available, inspect and test it rather than relying on connector snippets.

### 4.1 Issues and PRs

- Search existing issues and open PRs for overlap before creating new work.
- Use an existing issue where one accurately tracks the task.
- Create an issue for substantial, independently trackable work when useful; do not create an issue for every small change as ceremony.
- Group a coherent feature set into a focused PR. Split only when independent review, risk or delivery requires it.
- Every PR must describe scope, verification, limitations, risks and rollback/recovery where relevant.
- Do not close issues or merge PRs unless explicitly authorized.

## 5. Default task workflow

1. **Load instructions:** root README, this charter, complete skills repository and project-specific instructions.
2. **Establish access:** determine whether the actual project source and execution environment are complete.
3. **Inspect:** review project structure, entry points, conventions, trackers, CI, tests, configuration and deployment.
4. **Understand:** establish the user outcome, existing behavior, acceptance conditions and constraints.
5. **Trace:** follow affected behavior through relevant UI/API, authorization, domain, persistence, integrations and operations.
6. **Assess:** identify security, data, compatibility, performance, accessibility, reliability and rollout implications.
7. **Decide:** choose the smallest maintainable design consistent with the repository and skills. Explain material trade-offs; ask only for genuine human decisions.
8. **Implement:** keep changes focused; avoid unrelated refactors and speculative infrastructure.
9. **Verify:** run relevant tests and quality gates available in the environment; investigate failures rather than hiding them.
10. **Review:** inspect the complete diff, contracts, security boundaries, tests, documentation and rollback/recovery.
11. **Deliver:** open or update a PR to `dev`; report evidence and limitations accurately.

For a clear, low-risk task, keep the plan concise and proceed. Do not stop after every phase to request approval. For ambiguous or high-risk work, ask the one question or decision that blocks safe progress.

## 6. Quality gates

Apply the relevant CORE and specialist-skill controls. A gate is complete only when it was actually checked.

| Area | Expected verification where relevant |
|---|---|
| Frontend | Production build, lint, typecheck, unit/component/integration/E2E tests, accessibility and browser/responsive checks |
| Backend | Unit, integration, API/contract and E2E tests; lint, formatting, type checks and build/package checks |
| Security | Authentication, resource authorization, tenant isolation, input handling, secret exposure, dependency and relevant security scans |
| Data/migrations | Constraints, transaction/concurrency behavior, representative migration tests, backfill and recovery strategy |
| Integrations | Timeout, retry, idempotency, malformed response, duplicate delivery and partial-failure behavior |
| Performance | Query plans, bundle/runtime measurements, load/capacity checks or budgets where requirements and risk justify them |
| Operations | Configuration, health/readiness, logs/metrics/traces, backup/restore and deployment smoke checks where applicable |
| Documentation | API contracts, setup, architecture, migrations, runbooks and user-facing claims remain accurate |

Do not run every possible test for every change. Select the tests that prove the changed behavior and control the relevant risks. Add a regression test for confirmed defects where practical. Do not delete, skip or weaken a failing test merely to obtain a green result.

If a check cannot run, list it under **Not verified**, explain why and state what would be needed. Static analysis is not browser verification; a successful build is not proof of a correct user journey.

## 7. Frontend-specific operating rules

Use Next.js App Router and TypeScript as the default for new frontend projects unless the existing product, requirements or deployment constraints justify another choice. Do not migrate an existing application just to match the default.

For frontend work:
1. Read and apply HUMAN-EXPERIENCE, VISUAL-DESIGN and VISUAL-QA in addition to CORE.
2. Inspect the existing design system, global styles, theme tokens, typography, components and route structure before changing UI.
3. Preserve established visual direction unless the task explicitly calls for a redesign or evidence demonstrates a problem.
4. Prefer Server Components; introduce client-side JavaScript only for genuine interaction/state needs.
5. Verify responsive layouts, keyboard/focus behavior, semantics, accessible names, contrast, loading/empty/error/success states and real browser interactions.
6. Verify rendered output against the design intent. A passing build or component test does not establish visual correctness.
7. Treat SEO, metadata, structured data, indexing and conversion claims according to MARKET-DISCOVERY and the actual page purpose.
8. Protect server-only credentials and enforce authorization at trusted server boundaries; never rely on client-side checks for access control.

Routine implementation within an established design system does not need prior approval. Ask before a material brand, design-system or product-experience direction change outside the requested scope.

## 8. Backend and data-specific operating rules

Apply CORE fully. Identify domain invariants, API contracts, identity and authorization boundaries, tenant isolation, data lifecycle, transaction/concurrency behavior, integration failure modes, observability and recovery.

Use the repository's existing supported stack and conventions. For Python API projects, follow the stack and tooling actually present; do not migrate frameworks, drivers or dependency managers without a concrete reason.

Use framework-native tests. For meaningful defects, reproduce the issue and add regression coverage where feasible. No irreversible data operation or destructive migration without an explicit human-approved strategy.

## 9. Reporting and definition of done

Every substantial delivery and PR description must distinguish:

- **Changed** — files and behavior actually changed.
- **Verified** — exact tests, commands, reviews or observations actually completed, with results.
- **Not verified** — checks not run or unavailable, with reasons.
- **Risks** — unresolved uncertainty, security or operational concerns.
- **Rollback/recovery** — how to reverse or safely recover, where relevant.
- **Follow-ups** — useful work intentionally outside scope.

A task is complete when all applicable conditions hold:

~~~text
[ ] Required skills and project instructions read
[ ] Source access is sufficient and accurately characterized
[ ] User outcome and acceptance conditions understood
[ ] Actual implementation and relevant dependencies inspected
[ ] Security, authorization, privacy and data integrity considered
[ ] Compatibility, failure behavior and performance considered
[ ] Relevant tests and quality gates run where possible
[ ] Browser/accessibility/visual verification completed for UI work where possible
[ ] Documentation and operational recovery updated where needed
[ ] Final diff reviewed; no unrelated scope or secrets
[ ] PR targets dev and user retains final merge control
[ ] Changed / Verified / Not verified / Risks / Rollback / Follow-ups reported accurately
~~~

## Final principle

**Understand the real system. Apply the right skills. Make routine decisions autonomously. Protect users and production. Verify what you claim. Ask only when human judgment is genuinely required.**
