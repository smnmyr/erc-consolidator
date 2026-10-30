# Part B2 — Full Draft

**Project acronym (working):** ISLANDS
**Project title (working):** A New Web: Bridging NFPs for Heterogeneous
Requirements
**PI:** Prof. Dr. Simon Mayer
**Host institution:** University of St. Gallen (USG)
**Duration:** 60 months, indicative start **1 May 2028** (grant
agreement signature scheduled for 8 April 2028; M1 = May 2028, M60 =
April 2033) · **Requested budget:** **[TODO: pending the budget
decision in the Resources and Time Commitment section]** (CoG max €2.0M
plus up to €1.0M additional)
**Primary panel:** PE6 (Computer Science and Informatics)

> Drafting rules honored throughout: B2 is **Part II of the Scientific
> Proposal (7 pages)** plus the ongoing-grants annex, read at Step 2 alongside
> B1. It must be *complementary to, but not redundant with* Part I, so
> it does not re-argue the idea, the state of the art, or the
> objectives: it answers whether the idea can be implemented
> realistically, in the manner and with the approach proposed.
> Guiding maxim from the ERC info sessions (`sources/`): *impress
> non-experts in B1, convince experts in B2* — this document is
> written for domain experts and may be technically dense. Required
> content per the 2027 Work Programme (§1.5.1): project
> implementation, research methodology, work plan, risk assessment,
> and mitigating measures. The detailed budget, team, and time
> commitment sit in the separate **Resources and Time Commitment**
> section (≤2 pages, `draft/resources-and-time-commitment.md`), and
> the ongoing-grants annex does not count towards the page limit. Page
> budgets are marked per section. Items I could not know are marked
> **[TODO]**.
>
> Objectives O1–O5 and work packages WP1–WP5 are defined in B1 §b.3
> and §b.4 and are used here without redefinition.

---

## Section 1 — Implementation overview (~0.5 page)

The project is organized so that one cross-cutting theory work package
(WP1) is continuously constrained by three systems work packages
(WP2–WP4) and falsified by one validation work package (WP5). WP1 keeps revising the calculus as the systems work packages report back, because a calculus that no implementation ever tests would describe the design space without explaining it.<!-- was: The
dependency structure is deliberately not a waterfall: WP1 does not
"finish" and hand a specification downward, because a guarantee
calculus that is never contradicted by an implementation is not a
scientific result but a taxonomy. -->

**The integration mechanism.** Each project year closes with an
integration milestone at which the WP2–WP4 prototypes are built into a
single running island stack and deployed into at least one WP5 site.
Each milestone produces a versioned reference implementation and a written *calculus reconciliation* recording,<!-- was: Each milestone produces two artifacts: a versioned reference
implementation, and a written *calculus reconciliation* recording, --> for
every architectural decision taken in the systems WPs that year,
whether it was derivable from the current version of the WP1 model or
forced a revision of it. The reconciliation is the project's central methodological commitment: it makes the theory falsifiable once a year, on a schedule fixed in advance.<!-- was: The second artifact is the project's central
methodological commitment: it makes the theory falsifiable on a fixed
annual cadence rather than on the authors' judgement. -->

**Layering.** WP2 supplies the addressing and transclusion substrate.
WP3 elevates SMPC-based resolution from an application protocol to an
addressing primitive that WP2's link-class typing can name. WP4 exposes
both to agent clients as state-dependent affordances that carry the
link class of what they expose. WP5 instantiates the whole in two islands whose threat models, stakes, and governance differ, and that difference is what lets the WP1 model claim generality.<!-- was: in two
islands with genuinely different threat models, stakes, and
governance, which is what makes the WP1 model a general claim rather
than a description of one deployment. -->

**Openness.** All software is released open-source under a permissive
licence, all specifications are submitted to open standards fora (W3C
Community Group or IETF, the choice itself being a WP1-informed
decision per RFC 9518's guidance on reusing proven mechanisms), all
publications are open access, and all benchmark harnesses and datasets
that are not legally restricted are published alongside the papers.

---

## Section 2 — Methodology (~3 pages)

### 2.1 WP1 — The guarantee calculus (M1–M60)

*Method: formal modeling with design-science iteration.*

**Construction.** The calculus is a lattice of guarantee bundles
ordered by strength. Each bundle is annotated with (i) its minimal
coordination requirements, expressed as a set of standing obligations
on island members (registration, replication factor, identity binding,
availability coupling); (ii) the threat models under which it is
admissible; and (iii) its cost vector. Formalization follows the
information-flow-control tradition: a link class is a label on a
lattice in the style of the decentralized label model (Myers and
Liskov 1997), extended from confidentiality and integrity components
to persistence and attribution components, so ordering, join, and the proof techniques of label lattices come with it.<!-- was: so that ordering, join, and
the proof techniques that come with label lattices are inherited
rather than invented. --> Persistence and integrity components are
expressed as safety and liveness obligations over a content-addressed
store; confidentiality components reuse the simulation-based definitions of WP3.<!-- was: confidentiality components inherit the simulation-based
definitions used in WP3 rather than restating them. -->

**The link classes.** Table 1 fixes the link-class vocabulary that WP2's structural typing enforces.<!-- was: **The link classes.** Table 1 fixes the vocabulary the rest of this
document and WP2's structural typing use. B1 names the ladder and the
four axes; the two narrower classes and the treatment of retraction
are specified only here. -->

| Class | Axis | Resolution guarantee | Minimal coordination; precedent |
|---|---|---|---|
| Classic Jumplink | ladder | nothing: location-addressed, mutable | none; the Web default and the fallback outside any island |
| Archived/Resilient Link | ladder | stays resolvable across edits and removals; not verified | redundant snapshots and signatures (LOCKSS, Memento, Perma.cc, robust links) |
| Trusted Link | ladder | registrant known and accountable; bidirectionally tracked | island link registry (Microcosm/DLS lineage) |
| Verified Link | ladder | the exact cited span at the pinned version, or visible failure | content-addressed store (Git/IPFS, SWHID) |
| Cryptographic Link | ladder | a verified derivation from data the client never sees | secret-shared targets, SMPC/ZK resolution (PEP-LCA) |
| Attributed Link | attribution | reference bound to a verified author | identity binding (PROV, C2PA, integrity-by-design codes) |
| Anonymous/Pseudonymous Link | attribution | eligibility verified without identity | anonymous credentials, revocable pseudonyms |
| Endorsed/Reputation Link | trust | decay-bounded, Sybil-resistant score returned with the target | retractable endorsement web (nanopublication IDEBT) |
| Purpose-Bound Link | usage | derivation valid for a stated recipient, purpose, and window; re-resolved on expiry | terms carried in the reference; priced economically (transcopyright, insight economy) |
| Capability/Affordance Link | modality | an action, exposed only while valid; any rung applies | O4 agent gateway (signifier line) |
| Live/Subscription Link | narrower | notification when the held version is superseded | WebSub-style hub per island |
| Personalized/Disclosed Link | narrower | resolution varies by requester, with the criteria disclosed | disclosed-filter design; counterpart to undisclosed platform curation |

*Table 1. The link-class family WP1 formalizes and WP2 enforces.*
Retraction is a state, not a class: content stays immutable in the
substrate and a superseding retraction record changes default
resolution, which is how a Verified or Archived Link honours GDPR Art.
17 without breaking the history other references depend on.

**Proof obligations.** For each named link class the model must discharge *realizability* and *necessity*. *Realizability:*<!-- was: **What a proof obligation looks like.** For each named link class the
model must discharge two statements. *Realizability:* --> given an island
satisfying coordination requirement set C under threat model T, a
conforming implementation resolving a reference of class L either
returns a result meeting L's guarantee or fails visibly, with no silent
downgrade. *Necessity:* dropping any element of C admits an execution
in which L's guarantee is violated without visible failure. Necessity keeps the ladder honest: it is the claim that a rung cannot be had more cheaply.<!-- was: The second
is what keeps the ladder honest, since it is the claim that a rung
cannot be had more cheaply. -->

**Coordination cost and economic cost.** Coordination cost is measured in the standing obligations above and is directly instrumented by the WP2 benchmarks. Economic cost enters with the *usage* axis:<!-- was: **Pricing in two currencies.** Coordination cost is measured in the
standing obligations above and is directly instrumented by the WP2
benchmarks. The second currency is required by the *usage* axis: --> a
Purpose-Bound Link's terms cannot be enforced after resolution, so the
model scores such bundles by the margin by which the compliant path
undercuts defection for the party able to defect. Operationally this is
a comparison of the cost of re-requesting a fresh derivation against
the cost of storing, indexing, and re-using a stale one, computed
per actor class from the WP5 incentive data. Transcopyright priced reuse this way, and current data-economy proposals price derived insights the same way; the contribution here is to treat the margin as a term in a guarantee calculus, so that<!-- was: The mechanism is not
novel to us (transcopyright priced reuse this way, and current
data-economy proposals price derived insights the same way); what is
new is treating the margin as a term in a guarantee calculus, so that -->
the theory can return "this guarantee is not affordable for this actor"
as a first-class answer.

**Falsification protocol.** At each annual integration milestone the
reconciliation document lists every systems decision that could not be
derived from the current model. Each such decision is triaged as a
model gap (the calculus is extended), a model error (a claim is
retracted, and the retraction is published), or an implementation
artifact (no model change). The count and disposition of these are
themselves reported, so the model's revision history is visible.

**Deliverables.** Formal model and proofs; the link-class taxonomy as a
citable specification; decision procedures in the form of a design
questionnaire that maps an island's size, stake, threat model, and
actor mix onto an affordable bundle; and the *island design handbook*
consolidating all of it.

### 2.2 WP2 — The reference layer (M1–M42)

*Method: systems research with a reference implementation.*

**Design.** Span-level identifiers pinned to immutable versions in a
Merkle-DAG store, built on Git and IPFS primitives and on Software Heritage's ISO-standardized SWHIDs.<!-- was: built on Git and IPFS primitives and on Software
Heritage's ISO-standardized SWHIDs rather than on a new identifier
scheme. --> An island-scoped bidirectional link registry makes explicit the
coordination Xanadu wanted globally. Transclusion records provenance in
a W3C PROV-compatible form. Every reference is typed by its WP1 link
class, and typing is structural: resolving a Verified or Cryptographic
Link returns the exact cited span, or a verified derivation of it, or
fails visibly. Purpose-binding terms are carried in the reference itself, and<!-- was: Purpose-binding terms are carried in the reference
itself rather than in an out-of-band contract, and --> the registry records
issuance (to whom, for what, until when) as immutable history even
though the derivation itself expires.

**Boundary protocols.** *Outbound:* a Verified or Cryptographic Link
degrades to a Classic Jumplink for a non-member client, interoperating with Memento and Robust Links.<!-- was: interoperating
with Memento and robust links rather than replacing them. --> *Inbound:* an
admission protocol by which a client discovers the island's NFP set and
binds to it, which is where the attribution regime is applied and where
the guarantee bundle becomes enforceable on the client as well as on stored content.<!-- was: becomes enforceable on the client rather than
being merely a property of stored content. --> In label terms the two
directions are declassification and endorsement, and the boundary must
satisfy a nonmalleability condition of the kind Cecchetti, Myers, and
Arden (CCS 2017) formalize: no outsider may influence what the island
releases, and the island may not endorse a claim whose content it
cannot read. The second half is what makes admission under an
anonymous credential a case the WP1 model must treat explicitly, and it makes the border crossing a proof obligation.<!-- was: and
it turns the border crossing from a design convention into a proof
obligation. -->

**Evaluation.** A reference implementation benchmarked per link class
on resolution latency, storage overhead, and link-maintenance cost, at
island scales of 10² to 10⁵ members. Baselines: a plain HTTP fetch<!-- was: Baselines are the honest ones: a
plain HTTP fetch --> for Classic Jumplinks, a Memento/Perma-style archival
pipeline for Archived Links, and, for the registry, the measured
editorial cost of manual citation archiving in Island L. Workloads come from the real WP5 corpora, so span-size and citation-density distributions are realistic. All artifacts are public.<!-- was: Workloads are
generated from the real corpora in WP5 rather than synthesized, so the
span-size and citation-density distributions are realistic. Public
artifacts throughout. -->

### 2.3 WP3 — Confidential and verifiable references (M6–M54)

*Method: cryptographic protocol design with proofs and empirical
benchmarks.*

The PEP-LCA results are generalized into a *resolution protocol
family*: references whose targets are secret-shared across island
members and whose resolution is a joint computation with a verifiable
result. SMPC has been deployed for single fixed functions since the
Danish sugar-beet auction (Bogetoft et al. 2009) and in Estonian
government statistics (Bogdanov et al. 2016), and general-purpose
frameworks such as SPDZ (Damgård et al. 2012) and MP-SPDZ (Keller
2020) make arbitrary circuits practical; WP3 builds on MP-SPDZ and
contributes what these lack, a resolution protocol bound to a
citable, version-pinned reference. The nearest system precedent,
Fabric (Liu et al., SOSP 2009),
enforces its labels by placing cleartext only on nodes the data owner
trusts; the protocol family here removes that requirement, since a
Cryptographic Link's target is held in full by no node. Viaduct (Acay
et al., PLDI 2021) shows that the choice among multi-party
computation, zero-knowledge proofs, and commitments can be derived
from labels automatically; WP3 takes the same stance at the
granularity of a reference, with the WP1 link class selecting the
protocol. The research arcs run partly in parallel.<!-- was: Three research arcs run partly in parallel. -->

*(i) From honest-but-curious to malicious security.* Verifiable secret
sharing and zero-knowledge correctness proofs, with security stated and
proved in standard simulation-based models against a static, then an
adaptive, adversary. The deliverable is a quantified privacy-performance frontier.<!-- was: The deliverable is a quantified
privacy-performance frontier rather than a single protocol. -->

*(ii) Breaking availability coupling.* The PEP-LCA deployment (Grau
2025) shows that resolution<!-- was: Our own prior work documents
that resolution --> currently requires enough members to be online
simultaneously, which is a hard obstacle to interactive use. We
investigate threshold reconstruction and precomputed correlated
randomness so that resolution tolerates member downtime, and we treat
the resulting availability guarantee as an explicit WP1 coordination requirement.<!-- was: as an explicit WP1 coordination
requirement rather than an implementation detail. -->

*(iii) Input integrity.* Committed inputs, and attested sources
connecting to C2PA-style hardware roots, so that a verified derivation
over garbage inputs is distinguishable from a verified derivation over
attested ones.

**Evaluation.** Performance is measured on realistic island topologies
drawn from Island S's actual supply-chain structure, reporting<!-- was: drawn from Island S's actual supply-chain structure, not on uniform
random graphs, reporting --> resolution latency against member count,
share-reconstruction threshold, and circuit depth. External
cryptographic collaboration with K. Mitrokotsa and N. Cheng continues
the supervision constellation of the team's thesis work.

### 2.4 WP4 — Agents as hypermedia clients (M12–M54)

*Method: design plus controlled comparative evaluation.*

The island's agent gateway exposes capabilities as state-dependent
affordances, as a HATEOAS-style layer over MCP-class agent protocols,
with semantics for *why* an action is currently valid and explicit
ordering guarantees for dependent state-changing calls. Each affordance
carries the WP1 link class of the resource it exposes, so an agent can
distinguish a Verified citation from a Classic Jumplink before acting.
The gateway doubles as the border crossing for agent clients: an
agent's first affordance is acceptance of the island's NFP set, so
identity and obligations bind before any state-changing call.

**Evaluation design.** A within-scenario comparison across conditions:<!-- was: A within-scenario comparison across three
conditions: --> (a) static tool catalogues, (b) our affordance layer, (c)
hybrids. Scenarios are drawn from WP5's two islands, so tasks are realistic. Dependent measures:<!-- was: Scenarios are drawn from WP5's two islands so that task
realism is not manufactured. Three dependent measures: --> task success
rate; safety violations, operationalized as state-changing actions
taken on references whose declared class does not support them,
ordering violations on dependent calls, and the attack success rate
under the indirect-prompt-injection tasks of AgentDojo (Debenedetti
et al. 2024; Greshake et al. 2023), adapted to island scenarios; and evolvability, measured by
re-running a fixed task suite after a scripted change to the island's
capability surface and recording the proportion of tasks that survive
without client modification. Model choice, prompt, and random seed are
held fixed across conditions and reported. **Hypothesis:**
affordance-scoped exposure dominates static catalogues on safety and
evolvability without a significant loss in task success. A negative
result here is publishable and is treated as such (see §5).
Standardization proceeds through the W3C Web Agents CG, extending the
PI's signifier line, and through the Web of Things channel that the
PI's Chips JU commitment already funds (§3).

### 2.5 WP5 — Validation islands and stakeholder incentives (M12–M60)

*Method: two full-depth case studies plus a mixed-methods incentive
analysis.*

**Island L (legal citation).** An end-to-end pilot in which citations
in a working corpus are span-level, version-pinned, and verifiable. The
corpus is a real editorial pipeline (a law journal's, or a moot-court
record) **[TODO:<!-- was: record) rather than a constructed one **[TODO: --> confirm the partner
corpus and its data-sharing terms]**. Verified Links anchor to ECLI
and ELI identifiers where the cited source has one, so the island
adds span and version pinning to the EU's existing document-level
identifiers. Measures: citation-integrity
failures made structurally impossible, counted against a baseline
audit of the same corpus; editorial cost per citation versus
Perma-style manual archiving; and practitioner acceptance through
structured interviews and task observation with the editorial team.
Island L also instantiates the *attribution* NFP, weighing verified
authorship against pseudonymous regimes, with the anonymity side
grounded in the partner group's doctoral work on chilling effects.
Partner: Prof. Tamò-Larrieux (Lausanne), docking onto the PI's running
SNSF CoCoDa and *Access to Justice* projects.

**Island S (supply chain).** Extension of the running GDT/PEP-LCA
deployment into a full island with confidential references and
agent-mediated onboarding, using its existing industrial constellation
(Empa, Siemens). Its workloads follow the data duties of the EU
battery passport (Regulation (EU) 2023/1542, Art. 77, from February
2027) and of CBAM (Regulation (EU) 2023/956), both of which require
emissions data from upstream suppliers. Because the deployment already exists, Island S is the
project's early-evidence site: it can exercise WP3 protocols on real
topologies well before Island L's editorial integration is complete.

**Incentive analysis.** A per-actor-class study (hyperscaler, legacy
industry, OSS/privacy community, browser vendor, platform, and public
record-keepers such as parliaments, courts, and national archives) combining
semi-structured interviews **[TODO: target n per class; ethics approval
route at USG]**, institutional analysis of funding models, and the RFC
9518 mitigation checklist, read against the European Commission's
DSA enforcement record, including its December 2025 decision against
X on deceptive verification badges and researcher data access. For each class: does an island<!-- was: Two questions per class: does an island -->
change the incentive to centralize, and can the island be configured so
that the guarantee-respecting path is that actor's cheapest one? The
second question supplies WP1's economic currency. Grounding comes from
the team's published platform-transparency and DSA data-access work,
from the PI's seat on the European VLOP-auditing oversight board, and
from a direct working relationship with the ODI through CoCoDa. For
the legacy-industry class, which is otherwise the hardest to recruit,
the PI's standing role in a 33-partner Chips JU consortium of
semiconductor, edge-platform, and system-integration vendors supplies named interviewees (§3).<!-- was: supplies
named interviewees rather than cold outreach (§3). -->

---

## Section 3 — Feasibility (~1 page)

Most of the work packages extend systems that are already running.<!-- was: The project is unusually well de-risked for its ambition, because three
of its five work packages extend systems that are already running. -->

**Preliminary results in hand.**

- *Confidential resolution (WP3).* The PEP-LCA protocol computes joint
  supply-chain assessments across up to 50,000 participants with no
  trusted third party. This establishes that the scale WP3 targets is
  reachable; the open problems are the security model, availability
  coupling, and input integrity, which WP3's arcs address. Production
  SMPC deployments elsewhere (Bogetoft et al. 2009; Bogdanov et al.
  2016) confirm that the approach survives contact with real
  institutions.<!-- was: input integrity, which is precisely what WP3 is
  scoped to. -->
- *SMPC over pods (WP3/WP2 boundary).* The Solid Symposium 2026 system
  anchors SMPC share disclosure in an access-control layer with
  WASM-sandboxed data transformation, demonstrating the
  confidentiality-boundary integration the island architecture assumes.
- *Agent affordances (WP4).* The signifier line (AAMAS 2023/2024) has
  already delivered first-class runtime action-repertoire abstractions
  and BDI agents reasoning over them, so WP4 begins from working systems.<!-- was: so WP4 begins from a working
  conception rather than a position paper. -->
- *Standardization (WP2/WP4).* The PI's W3C Web of Things Thing
  Description contributions are deployed in shipped industrial
  products.<!-- was: which shows that this team's specifications reach production. --><!-- was: which is direct evidence that this team's specifications
  reach production rather than stopping at the draft stage. --> That channel
  is open forward as well as backward: the PI's Chips JU role funds and
  schedules a W3C community report on Web of Things application, due
  inside the WP2 and WP4 windows.
- *Empirical/regulatory instrument set (WP5).* The team's published
  platform-transparency and DSA Article 40(12) audit work supplies a
  validated method and existing instruments for the incentive analysis.

**Institutional feasibility.** Running projects dock onto the work and de-risk site access:<!-- was: Three running projects dock onto the
work and de-risk site access: --> Innosuisse Flagship WISER (supply-chain
LCA, Island S), SNSF CoCoDa (VLOP regulation, with the ODI as partner,
supplying the Solid and governance line), and SNSF/Innosuisse *Access
to Justice* (the legal-domain relationship behind Island L). The Chips JU action **AFarEdge** (2026–2029) docks onto WP4,<!-- was: A fourth,
the Chips JU action **AFarEdge** (2026–2029), docks onto WP4, --> which is
otherwise the least institutionally anchored part of the programme: it
places the PI as architect of a Web-of-Things architecture spanning<!-- was: places the PI as architect of a Web-of-Things framework spanning -->
heterogeneous edge hardware and cognitively heterogeneous agents,
giving the agent layer a live industrial reference point, a
standardization channel, and a standing working relationship with
silicon and platform vendors. The validation sites remain the islands of WP5.<!-- was: It is a reference point and a
relationship, not a validation site: the islands remain those of WP5. -->
The PI
stepped down as Dean in February 2026 specifically to refocus on
research, which frees the time the ≥40% commitment requires.<!-- was: which is what makes the ≥40% commitment credible rather than
nominal. -->

**Team feasibility.** The two researchers who built the systems the
project extends (Bekavac; Grau) are in post from M1 and carry the two
running deployments through the end of 2029 (M20), with scheduled
overlapping handovers to their successors<!-- was: to their successors rather than cliff-edge
departures --> (Resources and Time Commitment, §2).

---

## Section 4 — Work plan (~1 page)

### 4.1 Deliverables and milestones

| ID | Deliverable | WP | Due |
|---|---|---|---|
| D1.1 | Guarantee calculus v0 + link-class taxonomy spec | WP1 | M12 |
| D1.2 | Calculus v1, revised against first measurements | WP1 | M36 |
| D1.3 | Island design handbook | WP1 | M60 |
| D2.1 | Addressing/transclusion model + first prototype | WP2 | M12 |
| D2.2 | Bidirectional registry, retraction, boundary protocols | WP2 | M30 |
| D2.3 | Benchmarked reference implementation + artifacts | WP2 | M42 |
| D3.1 | Resolution protocol family, honest-but-curious | WP3 | M18 |
| D3.2 | Malicious-secure arc + privacy-performance frontier | WP3 | M36 |
| D3.3 | Availability-decoupled resolution + input integrity | WP3 | M54 |
| D4.1 | Agent gateway v1 | WP4 | M24 |
| D4.2 | Comparative agent evaluation | WP4 | M42 |
| D4.3 | Specification submitted to W3C Web Agents CG | WP4 | M54 |
| D5.1 | Both islands instantiated | WP5 | M24 |
| D5.2 | First measurement campaign | WP5 | M36 |
| D5.3 | Second campaign + incentive analysis | WP5 | M48 |
| D5.4 | Final evaluation across both islands | WP5 | M60 |
| M-I1..I5 | Annual integration milestone + calculus reconciliation | all | M12/24/36/48/60 |

### 4.2 Calendar

Indicative start 1 May 2028 (M1).

- **Year 1** (M1–M12): calculus v0 (WP1); reference-layer design and
  first prototype (WP2); protocol-family design (WP3); hires 1–4 in
  post; islands scoped with partners. **I1.**
- **Year 2** (M13–M24): first integrated prototype (WP2+WP3); agent
  gateway v1 (WP4); both islands instantiated (WP5); Postdoc B in post
  from ~M17, Bekavac and Grau handovers completed with overlap by M20
  (end of 2029); PhD 3 in post from ~M21. **I2.**
- **Year 3** (M25–M36): malicious-secure arc (WP3); comparative agent
  evaluation begins (WP4); islands in sustained operation, first
  measurement campaign (WP5); calculus v1 revised against evidence.
  **I3.**
- **Year 4** (M37–M48): scale and availability-decoupling results (WP3);
  cross-island interoperation (WP2/WP4); second measurement campaign
  and incentive analysis complete (WP5); specifications to W3C/IETF.
  **I4.**
- **Year 5** (M49–M60): consolidation, island design handbook (WP1),
  final evaluations, standardization handoff, open artifacts. **I5.**

### 4.3 Critical path and dependencies

The critical path runs from WP3(i) through WP3(ii) to D3.3, because<!-- was: The critical path runs WP3(i) → WP3(ii) → D3.3, because -->
availability-decoupled malicious-secure resolution is both the hardest
result and the one Island S's sustained operation depends on. WP2 is
schedulable independently of WP3 until the Cryptographic Link class is
integrated at I2. WP4 depends on WP2's link typing existing (M12) but
not on WP3 completing, since it can expose Cryptographic Links as
opaque affordances before the underlying protocols are
malicious-secure. WP5's Island S can begin measurement before WP2 is
complete; Island L cannot, since its whole value is span-level
verifiable citation.

---

## Section 5 — Risk assessment and mitigation (~1 page)

| # | Risk | L | I | Mitigation |
|---|---|---|---|---|
| R1 | Coordination cost exceeds what islands of realistic size can afford, so the top link classes are unreachable in practice | M | H | WP1 is built to return "not affordable" as a result, so this outcome is itself a finding.<!-- was: This is a research finding, not a failure: WP1 is built to return "not affordable" as a result. --> The lattice degrades gracefully, so a negative result at the top rung still yields a validated affordable-bundle boundary, which is publishable.<!-- was: affordable-bundle boundary, which is the paper. --> Early detection at I1 via WP2's coordination instrumentation. |
| R2 | SMPC resolution latency stays too high for interactive use | M | H | The deliverable is the privacy-performance frontier (D3.2), so the result stands either way.<!-- was: The privacy-performance frontier is the deliverable (D3.2), not a single protocol, so the result stands either way. --> Asynchronous and precomputed-randomness designs (WP3 ii), using the preprocessing model of SPDZ/MP-SPDZ, are the primary mitigation; Island S's batch workloads remain viable even if interactive resolution does not. |
| R3 | Malicious-secure arc does not close within budget | M | M | Scoped as an arc with intermediate publishable states (static then adaptive adversary). Honest-but-curious results (D3.1) already exceed the deployed state of the art and stand alone. |
| R4 | **Purpose-binding is not technically enforceable after resolution** | H | M | Accepted by design. WP1 prices the guarantee: it scores it<!-- was: Accepted by design rather than mitigated away. The guarantee is priced, not asserted: WP1 scores it --> by the margin by which re-requesting undercuts hoarding, and the class is documented as an economic guarantee.<!-- was: the class is documented as economic rather than cryptographic. --> This is the mechanism transcopyright and current data-economy proposals both rely on. The failure mode is a guarantee the theory declines to promise for a given actor, which the calculus can express. |
| R5 | Loss of a validation site (editorial partner withdraws; industrial partner reorganizes) | M | H | Two independent islands in unrelated sectors with separate partner constellations, so no single withdrawal ends WP5. Island L has alternative corpora (law journal, moot-court record, and the *Access to Justice* corpus) **[TODO: secure a written second option]**. Island S sits inside an existing running deployment. |
| R6 | Agent-layer comparative evaluation returns a negative or null result | M | L | Pre-registered hypothesis and analysis plan; a null result on task success with a positive result on safety and evolvability is the expected shape and is publishable. The evaluation is designed to be informative in either direction. |
| R7 | Applied-cryptography postdoc cannot be recruited (hardest profile) | M | H | Search opens at the Step 2 result (scheduled for 17 December 2027), about four months before M1. Grau's in-post SMPC expertise covers WP3's first arc regardless. Fallback: convert to two PhD positions with increased external advisory time from Mitrokotsa/Cheng. |
| R8 | Standardization uptake does not materialize | M | M | Fora chosen by WP1-informed analysis,<!-- was: Fora chosen by WP1-informed analysis rather than by default, --> and the PI has a track record of specifications reaching shipped products (WoT TDs). Impact does not depend on adoption: the reference implementation and artifacts stand on their own. |
| R9 | Legal exposure from the Island L corpus (personal data in citations) | L | M | Retraction is designed in as a superseding record, reconciling immutability with GDPR Art. 17; DPIA at island scoping; legal partner embedded in WP5 **[TODO: confirm USG ethics/DPIA route]**. |

In R1, R4, and R6 the likely failure is a bounded negative result, and each work package is designed to deliver that result as a finding, as fits a project whose core contribution is a theory of what is affordable.<!-- was: Risks R1, R4, and R6 share a structure worth stating: each is a case
where the honest outcome is a bounded negative result, and in each the
work package is designed so that outcome is a deliverable rather than a
loss. That is the intended shape of a high-risk/high-gain project whose
core contribution is a theory of what is affordable. -->

### References (not counted toward the page limit)

- Acay, Recto, Gancher, Myers, Shi. Viaduct: An extensible, optimizing compiler for secure distributed programs. *PLDI 2021*, 740–755. doi:10.1145/3453483.3454074
- Bogdanov, Kamm, Kubo, Rebane, Sokk, Talviste. Students and taxes: A privacy-preserving study using secure computation. *PoPETs* 2016(3):117–135. doi:10.1515/popets-2016-0019
- Bogetoft, Christensen, Damgård, Geisler, Jakobsen, Krøigaard, et al. Secure multiparty computation goes live. *FC 2009*, LNCS 5628:325–343. doi:10.1007/978-3-642-03549-4_20
- Cecchetti, Myers, Arden. Nonmalleable information flow control. *ACM CCS 2017*, 1875–1891. doi:10.1145/3133956.3134054
- Damgård, Pastro, Smart, Zakarias. Multiparty computation from somewhat homomorphic encryption. *CRYPTO 2012*, LNCS 7417:643–662. doi:10.1007/978-3-642-32009-5_38
- Debenedetti, Zhang, Balunović, Beurer-Kellner, Fischer, Tramèr. AgentDojo: A dynamic environment to evaluate prompt injection attacks and defenses for LLM agents. *NeurIPS 2024* (Datasets and Benchmarks), 82895–82920.
- Grau. Towards decentralized privacy-enhancing life cycle assessment. MSc thesis, University of St. Gallen, 2025.
- Greshake, Abdelnabi, Mishra, Endres, Holz, Fritz. Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection. *ACM AISec '23*, 79–90. doi:10.1145/3605764.3623985
- Keller. MP-SPDZ: A versatile framework for multi-party computation. *ACM CCS 2020*, 1575–1590. doi:10.1145/3372297.3417872
- Liu, George, Vikram, Qi, Waye, Myers. Fabric: A platform for secure distributed computation and storage. *SOSP 2009*, 321–334. doi:10.1145/1629575.1629606
- Myers, Liskov. A decentralized model for information flow control. *SOSP 1997*, 129–142.
- European regulation cited by number in the text: Regulation (EU) 2016/679 (GDPR), Art. 17; Regulation (EU) 2023/1542 (Batteries), Art. 77; Regulation (EU) 2023/956 (CBAM); Regulation (EU) 2022/2065 (DSA); European Commission, decision fining X under the DSA, 5 December 2025; Council conclusions on ECLI (OJ C 127, 2011) and ELI (OJ C 325, 2012).

---

## Annex — Ongoing and submitted grants (outside the page limit)

**[TODO]** Complete per the current template: ongoing and submitted
grants with role, funder, reference number, period, amount, and
percentage of PI time, plus an explicit statement of non-overlap with
ISLANDS. Entries to include: Innosuisse Flagship WISER (2022–2026);
SNSF CoCoDa (2025–2029); SNSF/Innosuisse *Access to Justice*
(2026–2030); EU Chips JU AFarEdge (2026–2029). For AFarEdge, state the
effort explicitly (39.5 person-months over 36 months, ≈ 0.09 FTE) so<!-- was: effort explicitly — 39.5 person-months over 36 months, ≈ 0.09 FTE — so -->
that it reads against the ≥40% ISLANDS commitment as negligible rather
than as competing load, and resolve the funding status before stating
any amount (see TODO 4). For each, state which parts of the ISLANDS work programme
are adjacent and why they are not redundant, since WISER and CoCoDa
both dock onto WP5 and a reviewer will look for double funding.

---

## Open TODOs for this draft

1. **Confirm the Island L corpus** and its data-sharing terms; secure a
   written second option (R5).
2. **Ethics and DPIA route at USG** for the WP5 interviews and the
   Island L corpus (R9).
3. **Interview design**: target n per actor class, sampling frame, and
   consent model for the incentive analysis.
4. **Ongoing-grants annex** (formerly Section 7) to be completed from the PI's
   current grant record. **Blocking sub-item:** confirm whether USG is a
   funded beneficiary or an unfunded associated partner in AFarEdge —
   the submitted budget lists it as a beneficiary (€201,031 requested),
   while the PCA V4.0 draft designates it an associated partner with no
   EU funding. Every other mention of AFarEdge in B1 and B2 is phrased
   in terms of *role*, which holds either way; only this section needs
   the resolved status.
5. **Page budget, measured 2026-09-04**: Sections 1-7 total 3,911
   words, about 6.5 template pages against the 7-page limit, so the
   draft currently fits. (2026-09-14: the information-flow-control
   additions in §2.1–§2.3 add roughly 200 words; re-measure.
   2026-09-28: the former Section 6, team and budget, about 0.75 page,
   moved to the separate Resources and Time Commitment section, and
   the ongoing-grants annex no longer counts, so Part II is probably
   back inside 7 pages.) The margin is thin and the tables will render
   larger than their word count suggests, so re-measure in the
   template. Section 4's two tables compress well into a single Gantt
   figure; Sections 2 and 5 are the next compression targets if needed.
6. **Cross-check against B1** once B1's own compression pass is done, so
   that no B2 section re-argues Part I rather than implementing it.
7. **Formalization setting** for WP1 (§2.1): a candidate is now written
   in (2026-09-14): a label lattice in the decentralized-label-model
   tradition, with the border crossing as a declassification/endorsement
   pair under a nonmalleability condition (§2.2). PI to confirm; if
   accepted, D1.1 should name the label algebra explicitly.
8. **Budget does not close (found 2026-09-14).** Moved on 2026-09-28
   to `draft/resources-and-time-commitment.md` (§3 and TODO 1), which
   now costs the full team and lays out two scenarios for the PI to
   choose between.
9. **Page budget after the taxonomy swap (2026-09-14)**: Table 1 adds
   about 300 words to §2.1; re-measure in the template and, if over
   7 pages, fold §4.2 (calendar) into the §4.1 table as a Gantt figure.
10. **Ethics Issues Table** (mandatory per the 2027 Work Programme):
    declare the WP5 interviews (human participants) and the personal
    data in the Island L corpus; this ties to TODOs 2 and 3.
