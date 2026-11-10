# VISUAL-DESIGN — AI Visual Design Methodology
## Version 1.1.0

> Mission: Teach agents to make and evaluate visual decisions that produce clear, coherent, distinctive interfaces fit for their product context. This is a practical design methodology, not a list of styling preferences.

## 1. Ownership and principles

VISUAL-DESIGN owns visual language, design systems, composition, typography, colour, spacing, shape, surfaces, elevation, themes and component appearance. HUMAN-EXPERIENCE owns usability and interaction quality; FRONTEND owns implementation; VISUAL-QA verifies rendered output; COMMERCIAL-PRODUCT supplies business context. CORE and PRIVACY govern engineering and data protection.

1. Design for the user's task and product context, not a screenshot or trend.
2. Establish hierarchy before decoration.
3. Use a coherent visual system, not page-by-page styling.
4. Use semantic tokens rather than arbitrary raw values.
5. Make colour, type, spacing, shape and elevation communicate structure and state.
6. Preserve existing identity unless redesign is requested or evidence justifies change.
7. Include responsive behavior, accessibility and component states in the design.
8. Ground significant choices in product evidence, platform conventions, references or requirements. Mark unsupported choices PROPOSED.

"Modern", "premium", "clean" and "beautiful" are not specifications. Translate them into observable decisions.

## 2. Design decision workflow

For a new page, redesign or substantial component:

1. Understand users, job, context, frequency, device, urgency, product category, brand and business outcome. Mark unknowns.
2. Inspect existing tokens, components, global styles, typography, themes, responsive rules and current screens.
3. Research a small number of relevant production references or established design systems. Extract principles; do not clone.
4. Structure the page purpose, information architecture, task sequence, content hierarchy and primary action with HUMAN-EXPERIENCE.
5. Choose a direction for personality, density, colour, typography, layout, surfaces and imagery.
6. Systematise semantic tokens, component variants, responsive rules and state treatments.
7. Prototype on a representative page and key interaction states.
8. Evaluate task clarity, hierarchy, accessibility, consistency, responsiveness and commercial context.
9. Implement with FRONTEND and verify rendered output with VISUAL-QA.
10. Record meaningful decisions, exceptions and unresolved assumptions.

Use a proportionate version of this workflow for small changes. A reference is evidence of a choice, not proof that the choice fits this product.

## 3. Page composition and layout

Design around the task and content, not arbitrary cards. Evaluate:

- Hierarchy: what should be noticed first, next and last?
- Grouping: which elements belong together? Use proximity, alignment, containers and labels consistently.
- Alignment: establish shared edges and deliberate alignment lines; avoid near-alignment.
- Content width: choose readable measures for prose and useful working widths for dashboards and tools.
- Grid: use repeatable columns, gutters and margins.
- Whitespace: separate unrelated groups and connect related items. Empty space is a tool, not a target.
- Density: match the user's work. Operational dashboards often need efficient density; marketing pages need narrative breathing room.
- Scan path: make headings, values, labels and actions easy to locate.
- Action placement: place primary actions where expected after the user understands the task; distinguish destructive actions.
- Responsive reflow: decide what stacks, collapses, moves, scrolls or becomes secondary.

Use a consistent layout scale. Do not put every element in a card. Reserve containers for meaningful grouping or hierarchy.

## 4. Spacing, sizing and rhythm

Choose one base unit and a small scale. A 4px base allows finer control; an 8px base is simpler and coarser. Choose based on product density and existing conventions.

A practical starting scale is 4, 8, 12, 16, 24, 32, 40, 48, 64 and 80 CSS pixels. Treat it as a proposal, not a universal law. Name tokens consistently.

- Use smaller gaps within a component and larger gaps between semantic groups.
- Keep repeated controls, form rows and cards consistent.
- Define page gutters, section spacing, component padding and inline gaps separately.
- Avoid unexplained one-off values; document necessary exceptions.
- Include line-height and text measure in vertical rhythm.
- Test dense and long-content states, not only ideal short copy.

Define component dimensions by content, usability and platform—not by forcing every control to the same height.

## 5. Typography methodology

Choose fonts by suitability, not popularity. Evaluate legibility at actual UI sizes, x-height, letterforms, numeral clarity, language/glyph coverage, available weights, variable-font support, readability in long text and dense tables, brand character, licensing, loading cost and reliable fallbacks.

A single high-quality family with several weights is often enough. Add a second family only when it creates a meaningful role distinction. Pair by role contrast, not novelty.

Define display, page heading, section heading, body, label, caption, code and numeric/data roles. Specify size, weight, line-height and letter-spacing together. Check line length, heading wrapping, labels, tabular numerals, truncation, overflow and zoom. Do not use tiny text for secondary information or rely on weight alone for hierarchy.

## 6. Colour theory and palette construction

Understand colour through:
- Hue: colour family.
- Saturation/chroma: vividness or muting.
- Value/lightness: relative lightness or darkness.
- Temperature: warm/cool character.
- Context: adjacent colours alter perceived contrast and balance.

Choose a palette deliberately:
1. Start with brand/product personality and user context.
2. Select a primary hue that supports the intended identity; avoid category stereotypes.
3. Choose supporting relationships: analogous for harmony, complementary/split-complementary for stronger contrast, or restrained monochromatic ranges for quiet systems.
4. Build neutral surfaces and text colours.
5. Create semantic success, warning, danger and information roles.
6. Create usable tonal steps for light/dark surfaces, borders, text and interaction states.
7. Test real text, controls, focus rings, charts and status combinations.
8. Name tokens by semantic purpose, not by colour name.

Colour-wheel relationships are starting tools, not recipes. A complementary palette can still be harsh or inaccessible. Tune saturation, value and area balance in the real interface.

Define semantic roles for page background, elevated background, surface, overlay, primary/secondary/muted text, subtle/default/strong borders, action hierarchy, destructive actions, focus, selection, success, warning, danger, information, disabled/read-only and data visualisation. Do not use brand primary for every element. Never communicate status through colour alone.

Target WCAG 2.2 AA unless stricter requirements apply: normal text contrast at least 4.5:1; large text at least 3:1; meaningful non-text UI components and graphical information at least 3:1 against adjacent colours. Verify actual combinations in every theme and state, including hover, focus, disabled, selected and error. Do not reduce contrast for subtle aesthetics.

## 7. Theming and design tokens

Build tokens in layers:
1. Primitive tokens: raw palette, spacing, type, radius, shadow and motion values.
2. Semantic tokens: background, surface, text-primary, border-subtle, action-primary, status-danger and similar roles.
3. Component tokens: only where a repeatable component-specific need exists.

Components consume semantic tokens, not hard-coded palette values. Keep semantic names stable when the brand palette changes.

Support light/dark themes when needed. Dark mode is not mechanical colour inversion: retune surface elevation, text hierarchy, borders, shadows, imagery, charts and focus states. Define switching, persistence and system-preference behavior. Avoid theme-specific exceptions scattered through CSS. Use the repository's token mechanism. Consider high contrast and reduced motion.

## 8. Shape, borders, shadows and elevation

Define restrained radius, border width/colour and elevation scales. Use elevation to communicate layering, not decorate every box. Establish hierarchy first with spacing, background and border. Shadows should be subtle, consistent and purposeful. Avoid competing shadows, heavy blur, arbitrary glow and shadows that disappear in dark mode.

Distinguish flat content, grouped surfaces, raised interactive surfaces, sticky/floating controls and modal overlays. Not every level needs a shadow.

## 9. Component methodology

Define each component by purpose, hierarchy, anatomy, dimensions, variants, states, responsive behavior and accessibility.

### Buttons and actions
A good button has a specific verb-led label, communicates one action, has visual weight proportional to importance, appears where expected, is not confused with navigation, has sufficient contrast and a comfortable target, and exposes hover, focus-visible, pressed, disabled and loading states. Prevent duplicate activation during pending operations. Make destructive consequences clear. Use icons only when they clarify meaning; icon-only controls need accessible names.

Use primary/secondary/tertiary/destructive variants intentionally. Usually provide one dominant primary action per local decision context. Do not make every button primary. Avoid vague "Submit" labels when a specific outcome is possible. Do not disable a button without explaining the condition when users need to understand it. Prefer touch targets around 44×44 CSS px where practical, while meeting applicable WCAG target-size requirements and exceptions.

### Inputs and form controls
A good input has a persistent visible label; placeholder is not a label. It communicates required/optional status and expected format, uses the correct input type/autocomplete/input mode/keyboard, provides safe defaults, has visible focus and clear error states, associates helper/error text programmatically, validates at a useful time, explains how to fix errors, preserves values after recoverable failures, and supports keyboard, screen reader and mobile interaction.

Use formatting assistance without blocking legitimate formats. Do not clear the form because one field failed. Avoid noisy per-keystroke validation when it interrupts users. Distinguish read-only, disabled, invalid and successful states.

### Cards, tables, navigation and dialogs
Cards group related content; do not turn every paragraph into one. Tables need scannable labels, aligned numeric values, clear sorting/filtering, row actions and a responsive overflow strategy. Navigation communicates current location. Dialogs are for focused decisions or interruptions; provide a clear title/actions, focus management and safe close behavior.

### Page quality
A good page has one clear purpose, understandable hierarchy, predictable navigation, coherent content width, consistent alignment, visible next action, appropriate density, useful feedback and responsive behavior. The first viewport should orient the user, not hide essential task information for visual drama.

For business applications optimise frequent workflows, scanning, data entry and recovery. For marketing pages clarify value, proof, offer and next step. For checkout/onboarding minimise uncertainty and unnecessary effort without hiding material terms.

## 10. States, motion and responsive behavior

Specify default, hover, focus-visible, pressed, selected, disabled, loading, success, error, empty, permission-restricted and read-only states as relevant. State must not rely on colour alone.

Motion should communicate cause, continuity, hierarchy or progress. Keep transitions purposeful and brief; respect reduced-motion preferences. Avoid animation that delays tasks or causes discomfort.

Set breakpoints based on content failure, not device names. Specify gutters, maximum widths, grid collapse, content order, navigation, table behavior, button stacking, type/spacing changes, image crop, sticky elements and safe areas. Test real content, long labels, translation, zoom and touch. Do not hide essential actions to make layouts fit.

## 11. Design evaluation rubric

Score a representative page 0–2 per dimension: 0 = fails/absent, 1 = partial/inconsistent, 2 = clear/consistent.

| Dimension | Evaluation question |
|---|---|
| Purpose | Can the user tell what the page is for? |
| Hierarchy | Is the most important information/action dominant? |
| Composition | Are grouping, alignment, width and density deliberate? |
| Typography | Is text readable and hierarchy consistent? |
| Colour | Are semantic roles clear and contrast sufficient? |
| Spacing | Is rhythm consistent and grouping understandable? |
| Components | Are controls recognisable and consistent? |
| States | Are focus, loading, disabled, error and success visible? |
| Theming | Do supported themes preserve hierarchy and contrast? |
| Responsive | Does the task remain usable at supported widths? |
| Accessibility | Are visual cues perceivable and not colour-only? |
| Brand fit | Does the visual language suit the product and audience? |

This is diagnostic, not proof of quality. A critical accessibility, task clarity or state failure blocks release regardless of total. An agent review is not user validation.

## 12. Existing systems, handoff and anti-patterns

Inspect tokens/components before creating primitives. Reuse and extend rather than fork. New tokens/variants must solve repeatable needs. Record justified exceptions; remove accidental drift.

For substantial work hand off user/business intent, observed system, reference principles, page hierarchy, visual direction, tokens, typography, colour, spacing, shape/elevation, component variants/states, themes, responsive behavior, accessibility, exceptions and unknowns.

Never choose styles solely because fashionable; equate whitespace with quality; make everything a card or primary action; use arbitrary values; use placeholders as labels; communicate status by colour alone; use gradients/glow/motion instead of hierarchy; mechanically invert light mode; optimise screenshots at the expense of workflows; or claim validation without evidence.

## Final principle

A good visual system makes purpose, hierarchy, action and state immediately legible—and remains coherent across the entire product.