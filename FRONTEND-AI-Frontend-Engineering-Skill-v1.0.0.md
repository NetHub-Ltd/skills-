# FRONTEND — AI Frontend Engineering Standard
## Version 1.0.0

> Mission: Build frontend applications that are reliable, secure, fast, accessible, maintainable and commercially effective.
>
> Default for new projects: Next.js App Router + strict TypeScript, unless the existing product or requirements justify another stack. This is not permission to migrate an existing application.

## 1. Scope and integration

FRONTEND owns browser architecture, React/Next.js implementation, rendering, client/server boundaries, state, data fetching, forms, frontend security, runtime performance, browser compatibility and frontend verification.

Apply CORE for engineering correctness and security; HUMAN-EXPERIENCE for journeys and accessibility; VISUAL-DESIGN for visual methodology; VISUAL-QA for rendered verification; MARKET-DISCOVERY for public SEO; COMMERCIAL-PRODUCT for monetisation; PRIVACY-DATA-GOVERNANCE for data collection, consent and tracking.

## 2. Inspect before choosing

Establish framework/version, package manager and lockfile, route structure, rendering model, component library, styling system, design tokens, API contracts, authentication model, analytics, consent tooling, deployment platform, CI, browser support and existing conventions.

Do not add dependencies or replace patterns merely because another tool is preferred. Use repository-supported versions and documented APIs. Do not assume a connector provides complete source or that a command ran.

## 3. Application architecture

For new Next.js projects:
- use App Router and TypeScript strict mode;
- keep Server Components as the default;
- introduce Client Components only for browser APIs, local interactivity or client-only state;
- keep server-only modules, credentials and privileged operations out of client bundles;
- organise by product feature/domain where that improves ownership and change locality;
- separate UI, domain behavior, data access and transport concerns;
- share components for repeated patterns, not speculative abstraction;
- define clear loading, error, not-found and unauthorized boundaries;
- use layouts and nested routes to preserve navigation context;
- keep Route Handlers and Server Actions thin, validated and authorization-aware.

Choose state ownership deliberately: URL state for shareable filters/navigation/pagination; server state for persisted remote data; local component state for transient interaction; shared client state only for genuinely cross-component concerns. Avoid duplicated sources of truth, unnecessary hydration and client copies of server data.

## 4. Data fetching and API integration

Treat API contracts as authoritative. Use generated typed clients where the repository supports them. Fetch close to the server boundary where possible; avoid waterfalls and duplicate fetches. Define cache, revalidation and freshness behavior explicitly. Handle timeouts, cancellation, retries and partial failure. Retry only safe/idempotent operations or operations protected by an idempotency contract.

Distinguish empty, stale, unavailable, unauthorized and failed states. Validate untrusted input at server boundaries; TypeScript types do not validate runtime data. Do not expose internal service endpoints, credentials or privileged tokens to the browser. Do not cache user-specific or sensitive responses publicly.

## 5. Forms and interactions

Use HUMAN-EXPERIENCE and VISUAL-DESIGN for form/control decisions. Implement semantic HTML, typed values, explicit validation, accessible labels/descriptions/errors, browser autocomplete/input modes, client feedback plus authoritative server validation, preserved values after recoverable failures, duplicate-submit protection, pending states and actionable server errors.

Do not trust client validation, hidden fields, disabled controls or UI state for authorization or business invariants.

## 6. Security boundaries

Enforce authentication and authorization on trusted server boundaries for every protected resource and mutation. Route hiding and client-side role checks are not access control. Keep secrets in server-only configuration. Validate untrusted input and encode output by context. Prevent XSS, CSRF where applicable, open redirects, clickjacking and unsafe file handling. Use secure session/cookie attributes appropriate to the auth architecture. Apply safe cache headers and prevent cross-user cache leakage. Treat third-party scripts, tag managers, embeds, fonts and analytics as supply-chain and privacy surfaces. Do not expose tokens, personal data or internal details in client logs/errors.

Use CORE and PRIVACY-DATA-GOVERNANCE for deeper controls. Review actual data flows, not framework conventions alone.

## 7. Accessibility and interaction quality

Target WCAG 2.2 AA unless stricter requirements apply. Use semantic elements, keyboard-operable controls, visible focus, logical focus order, accessible names, status announcements, sufficient contrast, zoom/reflow, reduced motion and accessible validation.

Verify every control performs its stated action; links navigate and buttons act; dialogs manage and return focus; keyboard users can operate controls; pending/disabled states are understandable; failures preserve work and offer recovery; touch behavior is reliable. Automated checks do not replace manual keyboard and assistive-technology review.

## 8. Performance and resilience

Design for realistic devices and networks. Minimise client JavaScript and hydration; prevent layout shift with stable dimensions and font strategy; optimise images/fonts/media; split code at meaningful route/feature boundaries; avoid render loops, unnecessary effects and expensive client computation; measure LCP, INP and CLS on representative routes; define budgets where useful; avoid third-party scripts without measurable value; define degraded/offline behavior where required.

Measure the bottleneck and verify the improvement. Do not optimise by guesswork.

## 9. SEO and public page behavior

Apply MARKET-DISCOVERY and the Google SEO reference to indexable public pages: server-render meaningful content, metadata, canonical URLs, robots directives, sitemap, semantic headings, internal links, structured data matching visible content, image alternatives, Open Graph, redirects and useful 404 behavior.

Authenticated, private, transactional and user-specific pages should not be indexed by default. Prevent private data leakage through metadata, pre-rendering, static generation, caching or structured data.

## 10. Analytics and consent integration

Do not install analytics by default without a documented purpose and privacy review. Define events and minimum properties; classify cookies, local storage, pixels and SDKs; gate non-essential technologies according to applicable consent requirements; prevent pre-consent requests/storage writes where required; provide withdrawal and preference changes; avoid credentials, sensitive data and unnecessary identifiers. Test consent in browser storage and network activity.

## 11. Testing and verification

Select tests by risk: unit tests for pure logic; component tests for behavior and semantics; integration tests for data/auth boundaries; E2E for critical journeys; visual regression for stable targets; accessibility tests plus manual keyboard checks; responsive/cross-browser checks; performance checks for critical routes; security tests for authorization, redirects, input and caching.

A passing build does not prove a page works. A screenshot does not prove an interaction works. Verify behavior and rendered output.

## 12. Production readiness

Confirm as applicable: environment variables are validated and server/client exposure intentional; production build and type checks pass; critical journeys have E2E coverage; errors are observable without sensitive leakage; analytics/consent is verified; caching and authorization are safe; routes, metadata and redirects are correct; rollback/deployment implications are understood; documentation matches implementation.

## 13. Definition of done

~~~text
[ ] Existing stack, design system and route architecture inspected
[ ] Server/client boundaries deliberate
[ ] Data contracts and runtime validation correct
[ ] Loading, empty, error, success and permission states handled
[ ] Authentication and authorization enforced server-side
[ ] No secrets or sensitive data leak to client bundles, logs or caches
[ ] Responsive layouts and real interactions verified
[ ] Keyboard, focus, semantics and contrast checked
[ ] Performance risks measured or explicitly bounded
[ ] SEO and indexing correct for page type
[ ] Analytics and consent reviewed and tested
[ ] Relevant tests, type checks, lint and production build run where possible
[ ] Visual QA completed or limitations reported
[ ] Changed / Verified / Not verified / Risks reported accurately
~~~

## Final principle

The frontend is the product's working interface—not a thin layer over the backend. Engineer the whole browser experience with the same rigor as every trusted system boundary.