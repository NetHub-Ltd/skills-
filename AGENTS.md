# AGENTS.md — NetHub Agent Operating Charter
## Version 1.5.0

> **Purpose:** Binding operating rules for agents working on NetHub repositories.
> **Start here:** Read the root README, then read the complete current skills repository before project work. This file governs workflow; specialist skills govern engineering and craft.

## 1. Skills and authority

The shared skills repository is https://github.com/NetHub-Ltd/skills-.

Read the full current contents of the root README, this charter and every skill relevant to the task. At session start, discover the current root files rather than relying on a stale filename list. Do not use search snippets or summaries as substitutes for required full documents.

| Skill | Current file pattern | Owns |
|---|---|---|
| CORE | `CORE-AI-Product-Engineering-Skill-*.md` | Engineering correctness, architecture, backend, APIs, data, security, testing, performance, reliability, observability and delivery |
| FRONTEND | `FRONTEND-AI-Frontend-Engineering-Skill-*.md` | Next.js/React architecture, browser implementation, state, rendering, security and frontend performance |
| HUMAN-EXPERIENCE | `HUMAN-EXPERIENCE-AI-UI-UX-Skill-*.md` | User goals, journeys, usability, interaction behavior, UX writing and accessibility |
| VISUAL-DESIGN | `VISUAL-DESIGN-Skill-*.md` | Visual direction, design systems, visual references and design implementation guidance |
| VISUAL-QA | `VISUAL-QA-Skill-*.md` | Rendered-interface verification across routes, states, themes and viewports |
| COMMERCIAL-PRODUCT | `COMMERCIAL-PRODUCT-*.md` | Business model, monetisation, pricing, conversion, retention, analytics and unit economics |
| PRIVACY-DATA-GOVERNANCE | `PRIVACY-DATA-GOVERNANCE-*.md` | Personal data, lawful purposes, cookies, consent, analytics governance, retention and data rights |
| MARKET-DISCOVERY | `MARKET-DISCOVERY-*.md` | Market understanding, positioning, search intent, SEO, acquisition and growth |

CORE applies to all engineering work. FRONTEND applies to browser application work. Apply HUMAN-EXPERIENCE, VISUAL-DESIGN and VISUAL-QA to interface work; MARKET-DISCOVERY to market/SEO/growth work; COMMERCIAL-PRODUCT to monetisation and product economics; and PRIVACY-DATA-GOVERNANCE whenever personal data, cookies, consent, analytics or third-party tracking is involved. A single task may require several skills together. Do not load unrelated material into every task's active reasoning, but do not skip the required initial repository-wide read.

### 1.1 Conflict resolution

Resolve conflicts in this order:

1. Security, correctness, data integrity and production safety.
2. Privacy, legal and compliance obligations.
3. User well-being and accessibility.
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

### 4.0 Repository issue and PR templates are mandatory

For every implementation task, agents MUST use the repository's GitHub templates. This is a required workflow control, not optional guidance.

- Before implementation, create or update the issue using `.github/ISSUE_TEMPLATE/implementation.md`. Populate every applicable section; do not leave template placeholders or vague acceptance criteria. If exact symbols/paths are unknown, inspect first and update the issue with the precise scope before changing project files.
- Every implementation PR MUST use `.github/PULL_REQUEST_TEMPLATE.md`. Preserve its sections and complete the change-specification, issue links, acceptance evidence, verification, CI readiness, risk and handoff fields. Do not replace it with an unstructured summary.
- A PR covering multiple issues MUST include a closing keyword for every issue. A single issue may cover a coherent set of changes; do not create duplicate issues for the same scope.
- Before presenting a PR for user review, verify the template is complete, all linked issues are current, all acceptance criteria have evidence, and every required check for the latest head SHA is green.
- If GitHub's template is unavailable (for example, a cross-repository contribution), reproduce the same sections in the issue/PR body and record why the repository template could not be applied. Never silently bypass the requirements.
- Agents must inspect and follow any more specific issue/PR templates in the target project repository; the shared template is the minimum standard, not a reason to ignore project-specific requirements.

### 4.2 CI ownership and pull-request readiness

CI is part of implementation, not a post-implementation report. The implementing agent owns the complete feedback loop for every code push until all required checks are green.

**Before the first push**
- Inspect the repository's actual CI workflows, branch protection/required checks where accessible, test scripts and project quality gates.
- Identify the required checks for this change and ensure the pipeline covers the affected code and risk. If required CI is missing or insufficient, add or repair appropriate automated gates within scope and permissions; do not treat an absent pipeline as a pass.
- Run the relevant checks locally where an execution environment exists. Record any checks that cannot be run locally and rely on the configured CI only where it genuinely covers them.

**After every push**
1. Record the pushed commit SHA and update the linked issue/PR with the commit, change summary and CI state.
2. Inspect the status checks and workflow runs for that exact commit. Do not assume the previous commit's green result applies to a new push.
3. Monitor queued and in-progress checks until they reach terminal states. A pending or missing result is not green.
4. For every failure, inspect the failed job, step and logs; identify whether it is caused by the code, tests, configuration, dependency/environment, flaky infrastructure or an external service.
5. Fix failures caused by the change or repository configuration. Add or correct regression coverage where appropriate, commit and push the fix, then repeat this entire loop for the new SHA.
6. Retry a failed job only when evidence indicates a transient runner/service failure; a retry does not replace diagnosing a reproducible failure.
7. Keep the issue/PR updated with failed check names, causes, corrective changes, rerun results and remaining blockers. Never hide, dismiss, weaken or bypass a required check to obtain a green badge.

**PR review readiness — all conditions mandatory**
- The PR is open against the correct integration branch.
- Every required check for the latest PR head SHA has completed successfully.
- No required check is pending, missing, skipped unexpectedly, neutral, cancelled or failing. A skipped check is acceptable only when its condition is intentional, documented and the repository's required-check policy permits it.
- All issue acceptance criteria are evidenced; relevant tests and final diff review are complete.
- The PR links every issue it covers and contains a closing keyword for each one (for example, `Closes #12` and `Fixes #15`). Verify the closing references are present in the PR body.
- The linked issues and PR contain current status, latest commit, CI results, test evidence, blockers (none for a ready PR) and next action.

Do not request user review, mark the PR ready for review, or tell the user it is ready while any required gate is unresolved. If a required check cannot run because CI is unavailable or permissions are missing, report the PR as blocked/not review-ready, document the exact missing capability and next action, and ask only for the access or decision genuinely required. The agent remains responsible for fixing failures it can fix; it must not hand routine CI repair back to the user.

The final tracker completion update is posted only after the PR is review-ready under these rules. The issue remains open until GitHub closes it automatically on merge.

### 4.1 Mandatory issue and PR tracking

Repository work must be resumable by another qualified agent without access to the original agent, its memory or its chat. The repository and its trackers—not an agent's private context—are the durable project record.

**Tracking is mandatory for every implementation PR.** Before changing tracked project files:
1. Search open issues and PRs for an exact match or overlap.
2. Create a dedicated issue if no existing issue accurately covers the requested change. Do not begin implementation on an untracked task.
3. Make the issue actionable before coding. It must identify:
   - the user/business outcome and current behavior or defect;
   - exact affected file paths and symbols/components/endpoints where discoverable;
   - the requested change as **current/from → desired/to** (not vague goals such as "improve UX" or "fix backend");
   - explicit in-scope and out-of-scope work;
   - test cases and quality gates to run, including relevant failure/boundary cases;
   - measurable acceptance criteria;
   - dependencies, compatibility/data/security risks and unresolved decisions.
4. If exact paths or symbols cannot be known until inspection, record the discovery task and update the issue with exact paths, symbols and before→after behavior **before implementation begins**.
5. Update the issue at implementation start with status, scope, branch/agent-independent task state, intended approach and next action. Keep it current when decisions, blockers or scope materially change.

A single issue may cover a coherent PR-sized feature set. Do not create duplicate issues for every commit or trivial subtask. Every implementation PR must link its issue and include GitHub's closing keyword (Closes #N, Fixes #N or Resolves #N) so the issue closes automatically **when the PR is merged**. Do not manually close it before merge.

**The end-of-implementation tracker update is gated.** Do not mark work complete or post the final completion update until:
- the PR has been opened against `dev`;
- all required CI checks and configured quality gates have completed successfully (green);
- acceptance criteria have been checked against evidence;
- the final diff and test results have been reviewed.

Then update the issue with the PR link, final changed paths, acceptance results, exact tests/checks and outcomes, remaining limitations/risks, and the fact that it will close on merge. If CI is red, pending, skipped unexpectedly or unavailable, keep the issue in progress/blocked, record the exact gate and next action, and do not claim completion. Do not bypass, weaken or silently waive a required gate.

**No stale or orphaned issues.**
- At task start, inspect relevant open issues and PRs; at task end, reconcile every issue touched by the work.
- Every open issue must communicate its current status, owner or responsible role, latest meaningful progress, blocker (if any), and concrete next action.
- Reconcile stale issues: update and continue active work, document blockers and a review point, or close completed/duplicate/superseded work with a clear explanation. Never silently close unrelated work or leave an issue stale merely because the original agent disappeared.
- Use the repository's configured stale-review interval; if none exists, flag issues with no meaningful update for 14 calendar days for review. Do not auto-close active work solely due to age.

**Agent-independent handoff.** Before ending a session, pausing, changing agents or handing off unfinished work, update the issue and/or PR with:
- current status and precise next action;
- branch and latest relevant commit SHA;
- files/symbols changed and remaining;
- decisions made and rationale;
- tests already run and exact results; tests not run and why;
- CI state, failing/pending checks and links;
- blockers, risks, dependencies and recovery notes.

The next agent must be able to resume by reading repository instructions, the issue, PR, commits/diff, CI and relevant source/tests. It must not depend on chat history, undocumented assumptions or the previous agent's memory.

- Group a coherent feature set into a focused PR. Split only when independent review, risk or delivery requires it.
- Every PR must describe scope, issue link, verification, limitations, risks and rollback/recovery where relevant.
- The user performs the final merge unless explicitly delegated. Never merge or deploy without authorization.

## 5. Default task workflow

1. **Load instructions:** root README, this charter, complete skills repository and project-specific instructions.
2. **Establish access:** determine whether the actual project source and execution environment are complete.
3. **Inspect:** review project structure, entry points, conventions, trackers, CI, tests, configuration and deployment.
4. **Understand:** establish the user outcome, existing behavior, acceptance conditions and constraints.
5. **Trace:** follow affected behavior through relevant UI/API, authorization, domain, persistence, integrations and operations.
6. **Assess:** identify security, data, compatibility, performance, accessibility, reliability and rollout implications.
7. **Decide:** choose the smallest maintainable design consistent with the repository and skills. Explain material trade-offs; ask only for genuine human decisions.
8. **Implement:** keep changes focused; avoid unrelated refactors and speculative infrastructure.
9. **Verify:** run relevant tests and quality gates available in the environment; investigate failures rather than hiding them. The implementing agent owns CI monitoring and repair after every push until the latest SHA is fully green; update the issue/PR with every pushed SHA, CI state, failure diagnosis, fixes and test outcomes.
10. **Review:** inspect the complete diff, contracts, security boundaries, tests, documentation and rollback/recovery. Do not request user review until the PR meets every CI and tracker readiness condition in §4.2.
11. **Deliver:** open or update a PR to `dev`; verify all required checks on the latest PR head are green, every covered issue has a closing keyword, and tracker updates are current before presenting it for user review. Report evidence and limitations accurately.

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
1. Read and apply FRONTEND, HUMAN-EXPERIENCE, VISUAL-DESIGN and VISUAL-QA in addition to CORE.
2. Inspect the existing design system, global styles, theme tokens, typography, components and route structure before changing UI.
3. Preserve established visual direction unless the task explicitly calls for a redesign or evidence demonstrates a problem.
4. Prefer Server Components; introduce client-side JavaScript only for genuine interaction/state needs.
5. Verify responsive layouts, keyboard/focus behavior, semantics, accessible names, contrast, loading/empty/error/success states and real browser interactions.
6. Verify rendered output against the design intent. A passing build or component test does not establish visual correctness.
7. Treat SEO and indexing according to MARKET-DISCOVERY; apply COMMERCIAL-PRODUCT to pricing, onboarding and revenue journeys; apply PRIVACY-DATA-GOVERNANCE to analytics, cookies and personal data.
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
