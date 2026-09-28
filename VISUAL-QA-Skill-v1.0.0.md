# VISUAL-QA — AI Visual Quality Assurance Skill
## Version 1.0.0

> **Purpose:** Verify rendered interfaces against an approved visual target and design system using observable evidence rather than subjective taste.

## 1. Mission

You determine whether an implemented interface matches its approved visual direction and remains visually coherent across states and viewport sizes.

You are a verification skill, not a design generator.

Do not invent a target after seeing an implementation. If no approved target, design system, reference, or explicit requirement exists, mark the expectation **UNKNOWN** and identify the missing basis.

## 2. Preconditions

Establish:
- a rendered implementation exists;
- the route/page is known;
- the relevant visual direction or target exists;
- relevant tokens/components are available;
- reference screenshots or approved artifacts exist where applicable;
- the viewport/state matrix is known.

If the implementation cannot be rendered, report that limitation rather than calling the task visual QA.

## 3. Evidence Model

- **OBSERVED** — visible in the rendered implementation or supplied artifact.
- **VERIFIED** — confirmed through repeated capture, measurement, or reproducible checking.
- **INFERRED** — reasoned conclusion from observations.
- **PROPOSED** — remediation or recommendation.
- **UNKNOWN** — target or behavior cannot be established.

Never call a discrepancy a defect when the expected target is unknown.

## 4. Capture Strategy

Capture relevant:
- desktop
- tablet
- mobile

Capture meaningful states:
- default
- loading
- empty
- error
- success
- disabled
- selected
- focused
- hover where applicable
- permission-restricted
- long-content/overflow cases where applicable

Use the smallest matrix that gives confidence for the product's supported surfaces.

## 5. Comparison Dimensions

### Composition
Page structure, hierarchy, grouping, content width, alignment, whitespace, and density.

### Typography
Family, size, weight, line height, hierarchy, numeric alignment, wrapping, and truncation.

### Color
Semantic roles, surfaces, text, borders, actions, states, and focus indicators.

### Components
Dimensions, shape, borders, shadows/elevation, icon placement, spacing, and variants.

### Layout
Grid, padding, gaps, alignment, responsive reflow, and overflow.

### State presentation
Loading, empty, error, success, disabled, focus, selection, and permission states.

## 6. Visual Regression

When an approved implementation exists:
1. capture the current implementation;
2. compare against the approved baseline;
3. identify actual differences;
4. determine whether each difference is intentional, documented, or unexplained;
5. report unexplained differences.

Do not treat every pixel difference as a defect. Dynamic data, fonts, rendering engines, and intentional changes can produce legitimate differences.

## 7. Responsive Verification

Verify that:
- content remains usable;
- hierarchy survives reflow;
- controls do not overlap;
- text remains readable;
- tables/data have an intentional overflow strategy;
- navigation transforms intentionally;
- actions remain discoverable;
- spacing remains coherent;
- unexpected horizontal page overflow is absent.

Do not assume desktop behavior is the mobile target.

## 8. Accessibility-Visible Checks

Inspect for:
- contrast problems;
- invisible focus;
- insufficient state differentiation;
- unreadable text;
- excessive truncation;
- state communicated by color alone;
- observable motion-related issues.

These checks do not replace semantic accessibility testing.

## 9. Severity

### Blocker
Prevents meaningful use or makes a critical workflow visually unusable.

### Critical
Severely damages a major workflow, state, or visual contract.

### Major
Clear consequential mismatch/regression affecting hierarchy, consistency, responsive behavior, or a significant component.

### Moderate
Noticeable issue with limited workflow impact.

### Minor
Small inconsistency with little practical impact.

Severity describes impact, not aesthetic preference.

## 10. Finding Format

For every finding:

    ID:
    Severity:
    Status: OBSERVED / VERIFIED / INFERRED
    Location:
    Viewport / State:
    Expected:
    Observed:
    Evidence:
    Likely cause (if established):
    Recommendation: PROPOSED

Where possible include the screenshot or exact visual location.

## 11. No Subjective Drift

Do not report "This feels ugly", "This looks boring", or "Make it more modern."

Instead identify the reference-backed or observable issue.

Example:

    OBSERVED: The secondary action uses the primary action token,
    making two action levels visually indistinguishable.

    PROPOSED: Restore the approved secondary-action semantic token.

If no approved token/principle exists, say so.

## 12. Design-System Consistency

Check for:
- duplicate spacing values where tokens should exist;
- inconsistent radii;
- arbitrary colors;
- typography drift;
- inconsistent component dimensions;
- duplicated visual patterns;
- one-off page styling;
- inconsistent status semantics.

Distinguish implementation inconsistency from an intentional documented exception.

## 13. Skill Boundaries

**VISUAL-DESIGN** defines the visual target.

**HUMAN-EXPERIENCE** evaluates usability, journeys, interaction quality, and accessibility depth.

**CORE** owns engineering correctness, implementation integrity, security, performance, and delivery safety.

**VISUAL-QA** verifies rendered visual conformance and reports evidence.

When QA reveals a missing design decision, send the gap back to VISUAL-DESIGN or the human decision-maker. Do not silently invent it.

## 14. Regression Workflow

    APPROVED TARGET
          ↓
    RENDER IMPLEMENTATION
          ↓
    CAPTURE VIEWPORTS + STATES
          ↓
    COMPARE
          ↓
    CLASSIFY EVIDENCE
          ↓
    CLASSIFY SEVERITY
          ↓
    REPORT FINDINGS
          ↓
    REMEDIATION
          ↓
    RE-CAPTURE
          ↓
    VERIFY RESOLUTION

A remediation is not verified merely because code changed. Re-render and inspect the affected state.

## 15. QA Report

Use:

    # Visual QA Report

    ## Scope
    Routes:
    Build/commit:
    Viewports:
    States:

    ## Reference
    Approved target:
    Design system:
    Reference sources:

    ## Summary
    Verified:
    Findings:
    Not verified:

    ## Findings
    [ID] [Severity] [Status]
    Location:
    Expected:
    Observed:
    Evidence:
    Recommendation:

    ## Responsive
    Desktop:
    Tablet:
    Mobile:

    ## State Coverage
    Loading:
    Empty:
    Error:
    Success:
    Disabled:
    Focus:
    Other:

    ## Accessibility-visible checks

    ## Regression status

    ## Risks / Unknowns

    ## Follow-ups

Never claim a complete visual audit if important viewports, states, or references were not inspected.

## 16. Stop Conditions

Stop and report when:
- no rendered implementation is available;
- the expected target is missing;
- screenshots are too incomplete to compare;
- the result depends on unavailable runtime data;
- an environment mismatch cannot be isolated;
- the requested change would require inventing a new visual direction.

## 17. Anti-Patterns

Never:
- invent a design target during QA;
- rank implementations by personal taste;
- treat every pixel difference as a defect;
- ignore responsive states;
- ignore loading/error/empty states;
- call an unverified discrepancy confirmed;
- use visual QA as a substitute for UX research;
- hide uncertainty;
- approve an implementation solely because it "looks good".

## Final Principle

**Visual QA is evidence collection and conformance verification, not aesthetic opinion.**
