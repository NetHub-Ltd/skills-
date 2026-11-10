# PRIVACY-DATA-GOVERNANCE — AI Privacy, Consent and Data Governance Standard
## Version 1.0.0

> Mission: Ensure products collect, use, share, retain and protect personal data deliberately, transparently, lawfully and securely.
>
> This is an engineering and governance standard, not legal advice. Obligations depend on the organisation, people, data, purpose, technology and jurisdictions involved. Obtain qualified legal/privacy review for material interpretations.

## 1. Scope and integration

Own privacy-by-design, data inventories, purpose/lawful-basis mapping, consent, cookies and similar technologies, analytics governance, notices, retention, data-subject workflows, processors, transfers, privacy risk assessments and operational verification.

Work with CORE for security/data lifecycle; FRONTEND for browser behavior; COMMERCIAL-PRODUCT and MARKET-DISCOVERY for analytics/marketing; HUMAN-EXPERIENCE for clear and non-coercive choices.

## 2. Jurisdiction and applicability

Before making a compliance claim identify organisation/controller/processor roles, establishment, affected people and locations, data categories/sensitivity, purposes/means, service/technology, vendors/subprocessors and transfer locations, sector obligations and exemptions.

For Kenya, start with the Data Protection Act, 2019, applicable 2021 regulations and current ODPC guidance. For EU/EEA users assess GDPR and applicable national/ePrivacy rules. For UK users assess UK GDPR and PECR. Other markets may have national or state privacy, consumer, marketing and communications laws.

Do not assume one global cookie rule or one lawful basis applies to every processing activity. Verify current official texts, amendments, regulator guidance and territorial scope. Record research date/source. Escalate uncertain interpretations to qualified counsel or the responsible privacy professional.

## 3. Data inventory and processing map

Before introducing collection or a vendor, create/update an inventory:

| Field | Required description |
|---|---|
| Data element | Specific data collected or inferred |
| Person | Customer, employee, prospect, visitor, child, other |
| Purpose | Specific reason for processing |
| Necessity | Why needed; alternatives considered |
| Source | User, device, third party, generated |
| Legal basis | Applicable basis and evidence; do not assume consent |
| Recipient | Internal roles, processors, other recipients |
| Location/transfer | Storage/access regions and safeguards |
| Retention | Period or deletion trigger |
| Security | Access, encryption, logging and protection |
| Rights path | How relevant requests are handled |
| Owner | Accountable business/technical owner |

Map collection, browser storage, transmission, APIs, databases, analytics, exports, backups, logs, support tools and deletion. Include derived data and identifiers. Pseudonymous/device-linked data may remain personal data under applicable law.

## 4. Privacy-by-design

Apply relevant principles: lawfulness, fairness, transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity/confidentiality and accountability.

Collect only what is needed for a defined purpose. Do not reuse data for an incompatible purpose without assessing legal and transparency requirements. Avoid collecting sensitive data "just in case". Pseudonymisation is not anonymisation; claim anonymisation only where re-identification is not reasonably possible under the relevant standard.

## 5. Lawful basis, consent and choice

Assess lawful basis separately for each purpose. Consent is not a universal substitute for analysis. Where relied on, verify that it is valid under applicable law: appropriately informed, specific, freely given, affirmative where required, demonstrable and withdrawable.

A consent experience must explain the organisation, purpose, data and relevant recipients; separate distinct purposes where required; avoid bundling unrelated processing; avoid preselected optional choices and deceptive hierarchy; make refusal/withdrawal practical; record the choice; and avoid treating silence or continued browsing as consent where affirmative consent is required.

Do not condition unrelated core service access on optional marketing/analytics consent unless qualified legal analysis supports it.

## 6. Cookies and similar technologies

Cookies are only one mechanism. Audit local/session storage, IndexedDB, pixels, SDKs, tags, fingerprinting, scripts, embedded content and other device access/storage technologies.

Maintain a register containing vendor/name, first-/third-party status, technology/domain, purpose/category, data accessed/stored/transmitted, duration/trigger, recipients/transfers, strict-necessity assessment, consent/legal basis/evidence, owner and review date.

Categories might include strictly necessary, preferences, analytics, advertising/targeting and embedded media. Category labels do not determine legal status.

### 6.1 Consent manager behavior

Where prior consent is required:
1. Block scripts, tags, pixels, SDK initialization, storage writes and related network calls until valid consent.
2. Provide clear first-layer choices and granular preferences.
3. Make reject/accept choices comparably accessible where required by applicable standards.
4. Allow later preference changes and withdrawal.
5. Persist a proportionate consent record.
6. Re-prompt when purposes/vendors materially change where required.
7. Respect the latest choice across relevant pages/sessions.
8. Ensure server-side tagging/proxying does not bypass the same rules.

Do not call a banner compliant merely because it renders. Verify network requests, browser storage, tag initialization and state before/after each choice. Essential technologies must be genuinely necessary for the requested service, not merely convenient for the business. Explain them in notices where appropriate.

## 7. Notices and transparency

Provide accessible layered notices at collection and a complete privacy notice. Explain as applicable controller identity/contact, purposes/legal bases, data categories/sources, recipients/processors, transfers/safeguards, retention, rights/how to exercise them, withdrawal, complaint route, mandatory/optional data and consequences, and relevant automated decision-making/profiling.

Keep public claims consistent with actual code, vendor configuration and internal practices. Do not generate policies that claim unverified technologies or practices.

## 8. Rights and data lifecycle

Design operational workflows for applicable rights: access, correction, deletion, objection, restriction, portability, withdrawal and review of certain automated decisions. Rights/exceptions vary; do not promise an absolute right where law provides limits.

Define ownership, proportionate identity verification, response deadlines, audit trail, export, deletion propagation, backup treatment and exception handling. Avoid collecting extra sensitive data merely to process a request. Provide a clear contact route.

Retention must be purpose-based. Define deletion/anonymisation triggers for primary systems, analytics, vendors, logs and backups. Document lawful retention exceptions; do not keep data indefinitely because deletion is inconvenient.

## 9. Vendors, processors and international transfers

Assess vendor purpose, data access, security, subprocessors, retention, location, transfer mechanism, contract terms, incident support and deletion behavior. Maintain an approved vendor/processor register and data-processing agreements where required.

Do not send customer/analytics data to a new vendor before privacy/security review. Assess storage, remote access and replication across borders and applicable safeguards.

## 10. Security, DPIA and incidents

Apply CORE controls: least privilege, access reviews, encryption in transit/at rest as appropriate, secure secrets, audit logs, tenant isolation, backups, vulnerability management and incident response.

For higher-risk processing assess whether a DPIA or equivalent is required before processing. Consider sensitive data, children, large-scale monitoring, profiling, automated decisions and novel technology. Record mitigations and residual risk. Escalate material residual risk.

Define breach handling: detect, contain, preserve evidence, assess data/people/jurisdictions, notify privacy/security owners, and meet applicable regulator/individual notification duties and deadlines. Do not invent a universal deadline.

## 11. Analytics and measurement

Analytics must have a defined decision purpose. Prefer aggregate/privacy-preserving measurement where practical. Define event schemas and prohibit passwords, tokens, payment credentials, sensitive free text and unnecessary identifiers.

Separate product analytics, operational telemetry, security logs, advertising and marketing measurement; they have different purposes, access, retention and consent/legal-basis requirements. Do not use analytics identifiers as authentication identifiers. Limit access, retention, exports and joins.

Inspect real network payloads. Ensure browser tags, server-side events and downstream vendors respect the same choices. Consent for one purpose does not automatically authorise another.

## 12. Children, sensitive data and automated decisions

Treat children's data, health, biometrics, precise location, financial data, identity documents, private communications and other legally sensitive categories as elevated risk. Apply stricter minimisation, access, retention and review.

Where children may use the service, determine applicable age/parental-consent and design obligations with qualified review. For profiling or solely automated decisions with significant effects, assess transparency, lawful conditions, safeguards, human review and contestability.

## 13. Implementation verification

~~~text
[ ] Jurisdictions and controller/processor roles assessed
[ ] Data flows and purposes documented
[ ] Data minimisation and retention considered
[ ] Lawful basis assessed per purpose
[ ] Consent and withdrawal tested where applicable
[ ] Cookies and similar technologies inventoried and gated
[ ] No prohibited pre-consent requests or writes
[ ] Privacy notice and preference controls accessible
[ ] Rights-request path documented and operational
[ ] Retention/deletion behavior implemented
[ ] Vendor, processor and transfer risks assessed
[ ] Access and security controls tested
[ ] DPIA/legal review escalated where required
[ ] Analytics payloads contain only approved fields
[ ] No unsupported compliance claim is made
~~~

## 14. Governance records

Maintain proportionate records: data inventory/processing map; cookie/tracking register; purpose/lawful-basis register; consent record schema/retention; privacy notice/change history; processor/vendor register; retention/deletion schedule; rights procedure; DPIA/risk assessment where required; incident response; owner and review cadence.

Do not create paperwork for its own sake. Each record must correspond to real processing and have an accountable owner.

## 15. Official reference starting points

Check current official material and amendments before relying on it:
- Kenya ODPC regulatory framework: https://www.odpc.go.ke/data-protection-laws-kenya/
- Kenya Data Protection Act, 2019: https://new.kenyalaw.org/akn/ke/act/2019/24/eng/
- Kenya Data Protection (General) Regulations, 2021: https://www.odpc.go.ke/wp-content/uploads/2024/03/THE-DATA-PROTECTION-GENERAL-REGULATIONS-2021-1.pdf
- ODPC Guidance Notes on Consent: https://www.odpc.go.ke/wp-content/uploads/2024/02/ODPC-Guidance-Notes-on-Consent.pdf
- European Commission data protection information: https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en
- UK ICO cookies and similar technologies: https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/cookies-and-similar-technologies/

These are starting points, not a determination that a law applies to a product. Verify territorial scope and seek qualified interpretation.

## 16. Definition of done

~~~text
[ ] Jurisdictions and roles assessed
[ ] Data flows, purposes and legal bases documented
[ ] Consent/withdrawal behavior tested where applicable
[ ] Cookies and similar technologies gated correctly
[ ] Privacy notices reflect actual behavior
[ ] Rights and retention workflows exist
[ ] Vendor and transfer risks assessed
[ ] Security controls verified
[ ] Specialist/legal review escalated where required
[ ] Analytics payloads and retention reviewed
[ ] No unsupported compliance claim made
~~~

## Final principle

If a product collects data, it must explain why, prove what it does, protect what it holds and respect the choices and rights of the people behind that data.