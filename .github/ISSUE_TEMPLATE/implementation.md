---
name: Implementation issue
about: Specify an implementation task with testable scope and acceptance criteria
title: "type: concise outcome"
labels: []
assignees: []
---

## Outcome
<!-- User/business outcome and why this work matters. -->

## Current state / defect
<!-- Observable current behavior, evidence, reproduction or source reference. -->

## Exact change specification
<!-- Identify paths and symbols. If not yet known, say so explicitly and make source inspection the first task before implementation. -->
| File path | Symbol / component / endpoint | Current (from) behavior | Desired (to) behavior |
|---|---|---|---|
| `path/to/file` | `SymbolName` | Current behavior | Required behavior |

## Scope
### In scope
- 

### Out of scope
- 

## Acceptance criteria
<!-- Observable, measurable statements. Each criterion must be verifiable. -->
- [ ] 

## Required tests and quality gates
<!-- Name the exact tests/checks and important failure, boundary, permission and regression cases. -->
- [ ] Unit tests:
- [ ] Integration / contract / component / E2E tests (as applicable):
- [ ] Static analysis, type checks, build and security checks:
- [ ] CI workflows / required status checks:

## Dependencies, compatibility and risks
- Dependencies:
- API/data/schema compatibility:
- Security/privacy/data-integrity considerations:
- Rollback/recovery:

## Execution state — maintain this section throughout delivery
- Status: NOT STARTED / IN PROGRESS / BLOCKED / PR READY FOR REVIEW / COMPLETE AFTER MERGE
- Responsible owner / agent role:
- Branch and latest commit SHA:
- PR:
- Progress and decisions:
- Tests run and exact results:
- CI checks for latest SHA:
- Blockers / risks:
- Next action:

## Completion conditions
- [ ] PR opened against the repository integration branch.
- [ ] PR links this issue using an automatic closing keyword.
- [ ] All acceptance criteria have evidence.
- [ ] Required CI checks for the latest PR head SHA are green.
- [ ] Final diff and security/compatibility review completed.
- [ ] Tracker and handoff details are current.
- [ ] Issue remains open until GitHub closes it on PR merge.
