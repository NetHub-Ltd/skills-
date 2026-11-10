# VISUAL-QA — AI Visual Quality Assurance Standard
## Version 1.1.0

> Purpose: Verify rendered interfaces against an approved visual target and design system using observable evidence rather than subjective taste.

## 1. Mission and evidence

Verify that implementation matches its intended visual direction across routes, viewports, themes and states. This is verification, not design generation. If no approved target, design system, reference or requirement exists, mark expectation UNKNOWN.

- OBSERVED: visible in rendered output or supplied artifact.
- VERIFIED: confirmed through reproducible capture, measurement or checking.
- INFERRED: reasoned from observations.
- PROPOSED: remediation.
- UNKNOWN: target or behavior cannot be established.

Never claim browser verification from code review alone or call a discrepancy a defect when the expected target is unknown.

## 2. Preconditions and capture matrix

Establish rendered route, build/commit, design tokens, intended theme, supported viewports, meaningful states and references. Capture in a real browser where possible.

Include a proportionate sample of:
- desktop, tablet and mobile widths;
- light/dark themes where supported;
- default, hover, focus-visible, pressed, selected, disabled and loading states;
- empty, error, success, permission-restricted and long-content/overflow cases;
- authenticated and unauthenticated states where relevant;
- high-contrast/reduced-motion preferences where supported.

Prioritise critical journeys and shared components. Explain meaningful exclusions.

## 3. Comparison dimensions

- Composition/hierarchy: purpose, structure, grouping, content width, alignment, whitespace, density, scan path and action placement.
- Typography: family, size, weight, line-height, hierarchy, numeric alignment, wrapping, fallback, truncation and zoom.
- Colour/themes: semantic roles, surfaces, text, borders, actions, status, focus and contrast in every supported theme.
- Spacing/geometry: gutters, grid, gaps, component padding, dimensions, alignment, reflow and overflow.
- Surfaces/elevation: borders, radius, shadows, overlays, stacking and sticky/floating layers.
- Components/states: anatomy, variants, icons, hover/focus/pressed/disabled/loading/error/success, selection and permission.
- Responsive behavior: navigation, content priority, tables, forms, actions, touch targets, image crop, fixed elements and safe areas.

## 4. Accessibility-visible checks

Inspect contrast, focus, text readability, state distinction, colour-only communication, truncation, zoom/reflow and motion. These do not replace semantic accessibility testing, keyboard operation or assistive-technology review.

## 5. Visual regression

With an approved baseline: capture matching viewport/theme/state/data; compare; separate dynamic data/rendering from real regressions; classify differences as intentional, documented or unexplained; report evidence; re-capture after remediation.

Do not treat every pixel difference as a defect. Fonts, antialiasing, browser engines, dynamic content and animation can create legitimate variation.

## 6. Severity

- Blocker: prevents meaningful use or makes a critical workflow visually unusable.
- Critical: severely damages a major workflow, state, accessibility or visual contract.
- Major: consequential mismatch affecting hierarchy, consistency, responsive behavior or an important component.
- Moderate: noticeable issue with limited workflow impact.
- Minor: small inconsistency with little practical impact.

Severity describes impact, not aesthetic preference.

## 7. Finding format

~~~text
ID:
Severity:
Status: OBSERVED / VERIFIED / INFERRED
Route / location:
Viewport / theme / state:
Expected:
Observed:
Evidence:
Likely cause (if established):
Recommendation: PROPOSED
~~~

Include screenshot/capture reference or exact location where possible.

## 8. Design-system consistency

Check duplicate spacing values, arbitrary colours, typography drift, inconsistent radii/elevation, one-off styling, duplicate patterns, inconsistent status semantics and theme exceptions. Distinguish drift from documented intentional exceptions.

## 9. QA report

~~~text
# Visual QA Report
Scope / routes / build:
Browsers:
Viewports:
Themes:
States:
Approved target:
Design system:
Summary:
Verified:
Findings:
Not verified:
Responsive: desktop / tablet / mobile
Theme coverage: light / dark / other
State coverage: loading / empty / error / success / disabled / focus / other
Accessibility-visible checks:
Regression status:
Risks / unknowns:
Follow-ups:
~~~

Never claim a complete audit if important routes, themes, viewports, states or references were not inspected.

## 10. Stop conditions and anti-patterns

Stop and report when implementation cannot be rendered, target is missing, captures are incomplete, runtime data is unavailable or work requires inventing a direction.

Never invent a target, rank by taste, treat every pixel difference as a defect, ignore themes/responsive states, claim validation without re-rendering or approve solely because it "looks good".

## Final principle

Visual QA is evidence collection and conformance verification, not aesthetic opinion.