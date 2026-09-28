# NetHub Agent Skills

The NetHub skills library defines reusable operating disciplines for AI agents working across NetHub products.

The goal is not to make agents produce more output. The goal is to make their decisions **evidence-backed, explicit, reusable, safe, and consistent**.

## Skills

| Skill | File | Owns |
|---|---|---|
| **CORE** — AI Product Engineering | `CORE-AI-Product-Engineering-Skill-v1.0.0.md` | Architecture, correctness, security, data, APIs, testing, reliability, observability, delivery safety |
| **HUMAN-EXPERIENCE** — AI UI/UX | `HUMAN-EXPERIENCE-AI-UI-UX-Skill-v1.0.0.md` | User journeys, usability, interaction design, information architecture, accessibility, UX writing |
| **VISUAL-DESIGN** — AI Visual Design | `VISUAL-DESIGN-Skill-v1.0.0.md` | Visual direction, references, design systems, typography, color, composition, visual states, responsive visual rules |
| **VISUAL-QA** — AI Visual QA | `VISUAL-QA-Skill-v1.0.0.md` | Rendered visual verification, visual regression, responsive/state inspection, evidence-backed findings |
| **MARKET-DISCOVERY** — AI Marketing/SEO/Growth | `MARKET-DISCOVERY-AI-Marketing-SEO-Growth-Skill-v1.0.0.md` | Market understanding, positioning, search intent, discoverability, messaging, conversion, growth |

## Ownership Model

The skills are complementary:

```
CORE
 ├── Engineering foundation
 ├── Correctness / security / data
 └── Delivery safety

HUMAN-EXPERIENCE
 ├── Human task
 ├── Journey / usability
 └── Interaction quality

VISUAL-DESIGN
 ├── Visual language
 ├── Design system
 └── Reference-backed appearance

VISUAL-QA
 ├── Rendered evidence
 ├── Conformance
 └── Visual regression

MARKET-DISCOVERY
 ├── Demand
 ├── Positioning
 └── Discovery / growth
```

A skill should own a decision once. Overlapping skills collaborate rather than duplicate each other's workflow.

## Evidence Vocabulary

All skills use the vocabulary established by `AGENTS.md`:

- **OBSERVED** — directly visible in repository, source, requirements, supplied evidence, or rendered output.
- **VERIFIED** — confirmed by a test, command, runtime result, measurement, or authoritative source.
- **INFERRED** — reasoned conclusion from evidence.
- **PROPOSED** — recommendation or design/implementation decision not yet established.
- **UNKNOWN** — not established.

Never turn a proposal into a fact or a visual impression into verification.

## Visual Design Philosophy

Visual design is deliberately **reference-driven**.

Agents should not manufacture a visual language from personal taste alone. Before making significant visual decisions, they should look for:

1. approved project design artifacts
2. existing product tokens/components
3. established design systems and documented principles
4. relevant real production interfaces
5. curated visual references
6. agent invention only where necessary, clearly marked as **PROPOSED**

A reference is not a template to copy. Extract the underlying decision and evaluate whether it fits the product.

> **Do not replace agent imagination with another agent's imagination. Replace ungrounded imagination with evidence, principles, references, and explicit decisions.**

## Recommended Workflow

```
CONTEXT
  ↓
CORE
  ↓
HUMAN-EXPERIENCE / VISUAL-DESIGN / MARKET-DISCOVERY
  ↓
DESIGN + APPROVAL
  ↓
IMPLEMENTATION
  ↓
VISUAL-QA (when rendered UI exists)
  ↓
CORE VERIFICATION
  ↓
REPORT
```

Not every task loads every skill.

Examples:

- Backend bug → CORE
- New user workflow → CORE + HUMAN-EXPERIENCE
- New dashboard visual direction → CORE + HUMAN-EXPERIENCE + VISUAL-DESIGN
- Implementing an approved interface → CORE + relevant UX/design skills
- Checking a rendered interface → VISUAL-QA + relevant UX/design context
- Landing page / acquisition work → CORE + HUMAN-EXPERIENCE + VISUAL-DESIGN + MARKET-DISCOVERY

## Reference Registry

When visual research materially informs a decision, maintain a small registry:

| Source | Context | Principle extracted | Applicability | Evidence level |
|---|---|---|---|---|
| URL / artifact | What was inspected | What was learned | Why it fits / does not fit | Project / system / production / curated / proposed |

This keeps visual decisions traceable and makes future design work faster.

## Repository Protocol

`AGENTS.md` is the binding operating charter.

In particular:

- inspect before changing
- classify evidence
- obtain required human approval
- work from `dev`
- create feature branches from the latest `dev`
- open PRs targeting `dev`
- verify before claiming success
- never commit secrets
- report Changed / Verified / Not verified / Risks / Rollback / Follow-ups

## Versioning and Contributions

Skills are versioned documents.

When changing a skill:

1. preserve its responsibility boundary
2. explain meaningful behavior changes
3. update the version
4. avoid silently changing another skill's ownership
5. keep guidance implementation-agnostic unless implementation detail is necessary
6. prefer concrete evidence and repeatable procedures over aesthetic or architectural slogans

New skills should answer:

- What decision/problem does this skill own?
- What evidence does it require?
- What is explicitly out of scope?
- How does it interact with existing skills?
- What does a good output look like?
- How can another agent verify its work?

## Final Principle

**Understand first. Ground decisions in evidence. Make ownership explicit. Build safely. Verify what was actually done.**
