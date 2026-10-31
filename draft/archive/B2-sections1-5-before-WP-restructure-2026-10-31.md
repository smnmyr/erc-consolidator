# B2 Sections 1-5 before the WP restructuring of 2026-10-31

## Section 1 — Implementation overview (~0.5 page)

We organize the project so that one cross-cutting theory work package
(WP1) is continuously constrained by three systems work packages
(WP2–WP4) and tested by one validation work package (WP5). WP1 does
not hand down a finished specification: we revise the calculus
whenever the systems work packages report back, because a calculus
that no implementation tests would describe the design space without
explaining it.

**Integration.** Each project year closes with an integration
milestone at which we build the WP2–WP4 prototypes into a single
running *island* stack and deploy it at one or more WP5 sites. Each
milestone produces a versioned reference implementation and a written
*calculus reconciliation*, which records for every architectural
decision taken in the systems work packages that year whether it was
derivable from the current WP1 model or forced a revision of it. The
reconciliation makes the theory falsifiable once a year, on a
schedule fixed in advance.

**Layering.** WP2 supplies the addressing and *transclusion* substrate.
WP3 turns SMPC-based resolution from an application protocol into an
addressing primitive that WP2's link-class typing can name. WP4
exposes both to agent clients as state-dependent *affordances* that
carry the link class of what they expose. WP5 instantiates the whole
in two islands whose threat models, stakes, and governance differ;
this difference is what allows the WP1 model to claim generality.

**Openness.** We release all software as open source under a
permissive licence, submit all specifications to the W3C groups that
maintain the protocols islands build on, or to their successors (Linked
Web Storage WG, Social Web WG and CG, Verifiable Credentials and
Federated Identity WGs, Web of Things WG, Autonomous Agents on the Web
CG; RFC 9518 advises reusing such proven mechanisms),<!-- was: permissive licence, submit all specifications to open standards fora
(a W3C Community Group or the IETF, chosen as WP1 informs, following
RFC 9518's guidance on reusing proven mechanisms), --> publish open
access, and publish all benchmark harnesses and datasets that are not
legally restricted alongside the papers.

---

## Section 2 — Methodology (~3 pages)

### 2.1 WP1 — The guarantee calculus (M1–M60)

*Method: formal modeling with design-science iteration.*

**Construction.** The calculus is a lattice of guarantee bundles
ordered by strength. We annotate each bundle with (i) its minimal
coordination requirements, expressed as standing obligations on
*island* members (registration, replication factor, identity binding,
availability coupling); (ii) the threat models under which it is
admissible; and (iii) its cost vector. Information-flow control
approached the problem from programming languages. The decentralized
label model (Myers and Liskov 1997) and Fabric (Liu et al. 2009) let
mutually distrusting principals share persistent objects under
confidentiality and integrity labels. They enforce these labels by
placing cleartext only on trusted nodes, over mutable,
store-identified objects, and they do not quantify what sustaining a
policy costs. Our formalization follows this tradition: a *link class*
is a label on a lattice in the style of the decentralized label model,
which we extend from confidentiality and integrity
components to persistence and attribution components, so that
ordering, join, and the proof techniques of label lattices carry
over. We express persistence and integrity components as safety and
liveness obligations over a content-addressed store; confidentiality
components reuse the simulation-based definitions of WP3.

**Link classes.** Table 1 fixes the link-class vocabulary that WP2's
structural typing enforces.

| Class | Axis | Resolution guarantee | Minimal coordination; precedent |
|---|---|---|---|
| *Classic Jumplink* | ladder | nothing: location-addressed, mutable | none; the Web default and the fallback outside any island |
| *Archived/Resilient Link* | ladder | stays resolvable across edits and removals; not verified | redundant snapshots and signatures (LOCKSS, Memento, Perma.cc, robust links) |
| *Trusted Link* | ladder | registrant known and accountable; bidirectionally tracked | island link registry (Microcosm/DLS lineage) |
| *Verified Link* | ladder | the exact cited span at the pinned version, or visible failure | content-addressed store (Git/IPFS, SWHID) |
| *Cryptographic Link* | ladder | a verified derivation from data the client never sees | secret-shared targets, SMPC/ZK resolution (PEP-LCA) |
| *Attributed Link* | attribution | reference bound to a verified author | identity binding (PROV, C2PA, eIDAS 2.0 wallets) |
| *Anonymous/Pseudonymous Link* | attribution | eligibility verified without identity | anonymous credentials, revocable pseudonyms |
| *Credentialed Link* | trust | an issuer's verifiable credential about the source, with its current revocation status | W3C Verifiable Credentials 2.0, SD-JWT (RFC 9901), eIDAS 2.0 wallets; island-defined list of accepted issuers |
| *Endorsed/Reputation Link* | trust | decay-bounded, Sybil-resistant score returned with the target | retractable endorsement web (nanopublication IDEBT) |
| *Purpose-Bound Link* | usage | derivation valid for a stated recipient, purpose, and window; re-resolved on expiry | terms carried in the reference, in ODRL 2.2 with DPV purposes; assessed by compliance margin (transcopyright, insight economy) |
| *Capability/Affordance Link* | modality | an action, exposed only while valid; any rung applies | O4 agent gateway (signifiers) |
| *Static Link* | link time | interface bound at design time in a fixed binary encoding; no run-time discovery; fails visibly if either side changes | design-time agreement on schema and encoding; static linking (Levine 2000); WoT TD binary protocol bindings (e.g., Modbus), WoT Binding Templates |
| *Live/Subscription Link* | narrower | notification when the held version is superseded | WebSub-style hub per island |
| *Personalized/Disclosed Link* | narrower | resolution varies by requester, with the criteria disclosed | disclosed-filter design; counterpart to undisclosed platform curation |

*Table 1. The link-class family that WP1 formalizes and WP2 enforces.*
Retraction is a state, not a class: content stays immutable in the
substrate, and a superseding retraction record changes the default
resolution. This is how a Verified or *Archived Link* honours GDPR Art.
17 without breaking the history on which other references depend.

**Proof obligations.** For each link class, the model must discharge
*realizability* and *necessity*. *Realizability:* given an island
that satisfies coordination requirement set C under threat model T, a
conforming implementation that resolves a reference of class L either
returns a result meeting L's guarantee or fails visibly, with no
silent downgrade. *Necessity:* dropping any element of C admits an
execution in which L's guarantee is violated without visible failure.
Necessity keeps the ladder honest, since it states that a rung cannot be attained at lower coordination cost<!-- was: a rung cannot be had more cheaply -->.

**Coordination cost and economic cost.** We measure coordination cost
in the standing obligations above and instrument it directly in the
WP2 benchmarks. Economic cost enters with the *usage* axis: a
Purpose-Bound Link's terms cannot be enforced after resolution, so the
model scores such bundles by the margin by which compliance is less costly than defection<!-- was: the margin by which the compliant path undercuts defection --> for the party able to defect. Operationally, we
compare the cost of re-requesting a fresh derivation with the cost of
storing, indexing, and re-using a stale one, per actor class and from
the WP5 incentive data. Transcopyright set the terms of reuse in this way, and current data-economy proposals set the terms of derived insights in the same way<!-- was: Transcopyright priced reuse in this way, and current data-economy proposals price derived insights in the same way -->; our contribution is to treat the margin as a term in a *guarantee
calculus*, so that the theory can return "this guarantee is not attainable for this actor"<!-- was: "this guarantee is not affordable for this actor" --> as a first-class answer.

**Falsification protocol.** At each annual integration milestone, the
reconciliation document lists every systems decision that the current
model could not derive. We triage each such decision as a model gap
(the calculus is extended), a model error (a claim is retracted, and
the retraction is published), or an implementation artifact (no model
change), and we report the count and disposition of these decisions,
so that the model's revision history is visible.

**Deliverables.** Formal model and proofs; the link-class taxonomy as
a citable specification; decision procedures in the form of a design
questionnaire that maps an island's size, stake, threat model, and
actor mix onto an attainable bundle<!-- was: onto an affordable bundle -->; and the *island design handbook*
that consolidates them.

### 2.2 WP2 — The reference layer (M1–M42)

*Method: systems research with a reference implementation.*

**Design.** We pin span-level identifiers to immutable versions in a
Merkle-DAG store built on Git and IPFS primitives and on Software
Heritage's ISO-standardized SWHIDs. Clients reach *island* resources
through the Linked Web Storage protocol that the W3C LWS Working Group
standardizes from Solid (Wright and Bremer 2026), and WP2 contributes
version-pinned identifiers to it as a profile. An island-scoped bidirectional<!-- was: Heritage's ISO-standardized SWHIDs. An island-scoped bidirectional -->
link registry makes explicit the coordination that Xanadu wanted
globally. Transclusion records provenance in a W3C PROV-compatible
form. Every reference is typed by its WP1 *link class*, and typing is
structural: resolving a Verified or *Cryptographic Link* returns the
exact cited span, or a verified derivation of it, or fails visibly.
Purpose-binding terms travel in the reference itself, expressed in
the W3C ODRL policy language (Iannella and Villata 2018) with purposes
from the Data Privacy Vocabulary of the W3C DPV Community Group
(Golpayegani, Flake, and Ryan 2026), and the<!-- was: Purpose-binding terms travel in the reference itself, and the -->
registry records issuance (to whom, for what, until when) as
immutable history even though the derivation itself expires.

**Boundary protocols.** *Outbound:* a Verified or Cryptographic Link
degrades to a *Classic Jumplink* for a non-member client, carrying a
text fragment (Burris and Bokan 2023) that keeps the cited passage
addressable where the page still contains it, and interoperates with
Memento and Robust Links.<!-- was: degrades to a Classic Jumplink for a non-member client and
interoperates with Memento and Robust Links. --> *Inbound:* an *admission
protocol* lets a client discover the island's NFP set and bind to it;
here the island applies its attribution regime, and the guarantee
bundle becomes enforceable on the client as well as on stored
content. In label terms, the two directions are declassification and
endorsement, and the boundary must satisfy a nonmalleability
condition of the kind Cecchetti, Myers, and Arden (2017) formalize:
no outsider may influence what the island releases, and the island
may not endorse a claim whose content it cannot read. The second half
of this condition forces the WP1 model to treat admission under an
anonymous credential explicitly, and it makes the *border crossing* a
proof obligation. Clients present credentials in the W3C Verifiable
Credentials 2.0 data model, with selective disclosure through SD-JWT
(RFC 9901) or BBS-style signatures. Browser clients request the
presentation through the W3C Digital Credentials API (Caceres et al.
2026), so that the European Digital Identity Wallet can serve as a
client from the start;<!-- was: (RFC 9901) or BBS-style signatures, so that the European Digital
Identity Wallet can serve as a client from the start; --> the island
publishes the issuers it accepts as part of its NFP set, and the
registry checks revocation status at resolution time.

**Evaluation.** We benchmark the reference implementation per link
class on resolution latency, storage overhead, and link-maintenance
cost, at island scales of 10² to 10⁵ members. Baselines are a plain
HTTP fetch for Classic Jumplinks, a Memento/Perma-style archival
pipeline for *Archived Links*, and, for the registry, the measured
editorial cost of manual citation archiving in Island L. Workloads
come from the WP5 corpora, so that span sizes and citation densities
are realistic. All artifacts are public.

### 2.3 WP3 — Confidential and verifiable references (M6–M54)

*Method: cryptographic protocol design with proofs and empirical
benchmarks.*

We generalize the PEP-LCA results (Grau 2025) into a *resolution
protocol family*: references whose targets are secret-shared across
*island* members and whose resolution is a joint computation with a
verifiable result. SMPC has been deployed for single, fixed functions
since the Danish sugar-beet auction (Bogetoft et al. 2009) and in
Estonian government statistics (Bogdanov et al. 2016), and
general-purpose protocols and implementations such as SPDZ (Damgård
et al. 2012) and MP-SPDZ (Keller 2020) make arbitrary circuits
practical. We build on
MP-SPDZ and contribute what these systems lack: a resolution protocol
bound to a citable, version-pinned reference. The nearest system
precedent, Fabric (§2.1), places cleartext only on nodes the data
owner trusts; our protocol family removes that requirement, since no node holds a *Cryptographic Link*'s
target in full. Viaduct (Acay et al. 2021) shows that the choice among
multi-party computation, zero-knowledge proofs, and commitments can be
derived from labels automatically; we take the same stance at the
granularity of a reference, with the WP1 *link class* selecting the
protocol. The research arcs run partly in parallel.

*(i) From honest-but-curious to malicious security.* We use verifiable
secret sharing and zero-knowledge correctness proofs, and state and
prove security in standard simulation-based models against a static,
then an adaptive, adversary. The deliverable is a quantified
privacy-performance frontier.

*(ii) Breaking availability coupling.* In the PEP-LCA deployment,
resolution requires enough members to be online simultaneously, which
obstructs interactive use. We investigate threshold reconstruction and
precomputed correlated randomness so that resolution tolerates member
downtime, and we treat the resulting availability guarantee as an
explicit WP1 coordination requirement.

*(iii) Input integrity.* Committed inputs and attested sources that
connect to C2PA-style hardware roots make a verified derivation over
garbage inputs distinguishable from one over attested inputs.

**Evaluation.** We measure performance on island topologies drawn from
Island S's actual supply-chain structure and report resolution latency
against member count, share-reconstruction threshold, and circuit
depth. K. Mitrokotsa and N. Cheng, who co-supervised the PEP-LCA work,
continue as external cryptographic collaborators.

### 2.4 WP4 — Agents as hypermedia clients (M12–M54)

*Method: design and controlled comparative evaluation.*

The *island*'s agent gateway exposes capabilities as state-dependent
*affordances*, through a HATEOAS-style layer over MCP-class agent
protocols, with semantics for *why* an action is currently valid and
explicit ordering guarantees for dependent state-changing calls. Each
affordance carries the WP1 link class of the resource it exposes, so
that an agent can distinguish a Verified citation from a *Classic
Jumplink* before acting. The gateway is also the *border crossing* for
agent clients: an agent's first affordance is acceptance of the
island's NFP set, together with a *verifiable credential* that states
on whose behalf the agent acts and within which limits, so that
identity, delegated authority, and obligations bind before any
state-changing call.<!-- was: agent clients: an agent's first affordance is acceptance of the
island's NFP set, so that identity and obligations bind before any
state-changing call. -->

**Evaluation design.** We compare, within each scenario, (a)
statically linked tool catalogues, (b) our affordance layer, (c)
hybrids, and (d) *Static Links* over binary protocol bindings. Scenarios
come from WP5's two islands and from fixed installations in building
automation (Siemens) and edge computing (AFarEdge), which change
rarely and need low latency. Dependent measures are task success
rate; latency per interaction;<!-- was: (a) static
tool catalogues, (b) our affordance layer, and (c) hybrids, in
scenarios drawn from WP5's two islands. Dependent measures are task
success rate; --> safety violations, operationalized as state-changing
actions on references whose declared class does not support them,
ordering violations on dependent calls, and the attack success rate
under the indirect-prompt-injection tasks of AgentDojo (Debenedetti
et al. 2024; Greshake et al. 2023), adapted to island scenarios; and
evolvability, measured by re-running a fixed task suite after a
scripted change to the island's capability surface and recording the
share of tasks that succeed without client modification. Model
choice, prompt, and random seed are held fixed across conditions and
reported. **Hypotheses:** affordance-scoped exposure outperforms
statically linked catalogues on safety and evolvability without a
significant loss in task success; Static Links outperform both on
latency in installations that do not change. Together, the conditions
measure the trade-off that the WP1 link-time axis captures<!-- was: the trade-off that the WP1 link-time axis prices -->, and hence
which *link time* the calculus should recommend for a given
installation.<!-- was: **Hypothesis:** affordance-scoped exposure outperforms
static catalogues on safety and evolvability without a significant
loss in task success. --> We treat a negative result as publishable (see
§5). Standardization proceeds through the W3C Autonomous Agents on the Web
Community Group, extending our work on *signifiers*, and through the AI
Agent Protocol Community Group for the agent credential. Static Links
go to the W3C Web of Things Working Group as a profile of its protocol
binding templates (Koster and Korkan 2025), through the Web of Things
channel that the PI's Chips JU role already funds (§3).<!-- was: Standardization proceeds through the W3C Web Agents Community
Group, extending our work on signifiers, and through the Web of
Things channel that the PI's Chips JU role already funds (§3). -->

### 2.5 WP5 — Validation islands and stakeholder incentives (M12–M60)

*Method: two full-depth case studies and a mixed-methods incentive
analysis.*

**Island L (legal citation).** In an end-to-end pilot, the citations in
a working corpus become span-level, version-pinned, and verifiable.
The corpus is a real editorial pipeline (a law journal's, or a
moot-court record) **[TODO: confirm the partner corpus and its
data-sharing terms]**. *Verified Links* anchor to ECLI and ELI
identifiers where the cited source has one, so the *island* adds span
and version pinning to the EU's document-level identifiers. We measure
the citation-integrity failures made structurally impossible, against
a baseline audit of the same corpus; the editorial cost per citation,
compared to Perma-style manual archiving; and practitioner acceptance,
through structured interviews and task observation with the editorial
team. Island L also instantiates the *attribution* NFP and weighs
verified authorship against pseudonymous regimes. *Credentialed Links*
let an author prove membership of the bar, or a court the origin of a
judgment, without the island holding a full identity record; the partner group's
doctoral work on chilling effects grounds the anonymity side. Our
partner is Prof. Tamò-Larrieux (Lausanne), and Island L docks onto
the PI's running SNSF CoCoDa and *Access to Justice* projects.

**Island S (supply chain).** We extend the running GDT/PEP-LCA
deployment into a full island with confidential references and
agent-mediated onboarding, together with its industrial partners
(Empa, Siemens). Its workloads follow the data duties of the EU
battery passport (Regulation (EU) 2023/1542, Art. 77, from February
2027) and of CBAM (Regulation (EU) 2023/956), which both require
emissions data from upstream suppliers. Under CBAM, actual emission
values must be checked by accredited verifiers (Implementing
Regulation (EU) 2025/2546; Delegated Regulation (EU) 2025/2551), so
Island S also tests Credentialed Links that carry the verifier's
attestation alongside a confidential value. Because the deployment already
exists, Island S provides early evidence: it exercises WP3 protocols
on real topologies well before Island L's editorial integration is
complete.

**Incentive analysis.** We study each class of actor (hyperscaler,
legacy industry, OSS/privacy community, browser vendor, platform, and
public record-keepers such as parliaments, courts, and national
archives) through semi-structured interviews **[TODO: target n per
class; ethics approval route at USG]**, institutional analysis of
funding models, and the RFC 9518 mitigation checklist, read against
the European Commission's DSA enforcement record, including its
December 2025 decision against X on deceptive verification badges and
researcher data access. For platforms, it also covers licensing of
content to AI model providers as a new incentive to close access, as
in Reddit's move to a primarily logged-in experience after AI answers
cut its search referrals (Reddit 2026). For each class, we ask whether an island
changes the incentive to centralize, and whether the island can be
configured so that the guarantee-respecting path is that actor's least costly one<!-- was: guarantee-respecting path is that actor's cheapest one -->; the second question supplies WP1's economic cost. The
analysis builds on our published platform-transparency and DSA
data-access work, on the PI's seat on the European VLOP-auditing
oversight board, and on our working relationship with the ODI through
CoCoDa. For the legacy-industry class, which is otherwise the hardest
to recruit, the PI's role in a 33-partner Chips JU consortium of
semiconductor, edge-platform, and system-integration vendors provides
named interviewees (§3).

---

## Section 3 — Feasibility (~1 page)

Most of the work packages extend systems that are already running.

**Preliminary results.**

- *Confidential resolution (WP3).* The PEP-LCA protocol computes joint
  supply-chain assessments across up to 50,000 participants with no
  trusted third party, which shows that the scale WP3 targets is
  reachable. Production SMPC deployments elsewhere (Bogetoft et al.
  2009; Bogdanov et al. 2016) show that the approach works with real
  institutions. The open problems are the security model,
  availability coupling, and input integrity, which WP3's arcs
  address.
- *SMPC over pods (WP3/WP2 boundary).* Our Solid Symposium 2026 system
  anchors SMPC share disclosure in an access-control layer with
  WASM-sandboxed data transformation, demonstrating the
  confidentiality-boundary integration that the *island* architecture
  assumes.
- *Agent affordances (WP4).* Our work on *signifiers* (AAMAS 2023/2024)
  has delivered first-class run-time action-repertoire abstractions
  and BDI agents that reason over them, so WP4 begins from working
  systems.
- *Standardization (WP2/WP4).* The PI's contributions to the W3C Web of
  Things Thing Description are deployed in shipped industrial
  products. The PI's Chips JU role also funds and schedules a W3C
  community report on Web of Things application, due within the WP2
  and WP4 windows.
- *Empirical and regulatory instruments (WP5).* Our published
  platform-transparency and DSA Article 40(12) audit work supplies a
  validated method and existing instruments for the incentive
  analysis.

**Institutional feasibility.** Running projects dock onto the work and
secure site access: Innosuisse Flagship WISER (supply-chain LCA,
Island S), SNSF CoCoDa (VLOP regulation, with the ODI as partner, for
the Solid and governance line), and SNSF/Innosuisse *Access to
Justice* (the legal-domain relationship behind Island L). The Chips JU
action **AFarEdge** (2026–2029) docks onto WP4, which would otherwise
be the least institutionally anchored part of the programme: the PI
leads the definition of its Web-of-Things architecture for
heterogeneous edge hardware and cognitively heterogeneous agents,
which gives the agent layer an industrial reference point, a
standardization channel, and a working relationship with silicon and
platform vendors. The validation sites remain the islands of WP5. The
PI stepped down as Dean in February 2026 to refocus on research, which
frees the time that the ≥40% commitment requires.

**Team feasibility.** The two researchers who built the systems the
project extends (Bekavac; Grau) are in post from M1 and carry the two
running deployments through the end of 2029 (M20), with overlapping
handovers to their successors (Resources and Time Commitment, §2).

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
| D4.3 | Specification submitted to W3C Autonomous Agents on the Web CG | WP4 | M54 |
| D5.1 | Both islands instantiated | WP5 | M24 |
| D5.2 | First measurement campaign | WP5 | M36 |
| D5.3 | Second campaign + incentive analysis | WP5 | M48 |
| D5.4 | Final evaluation across both islands | WP5 | M60 |
| M-I1..I5 | Annual integration milestone + calculus reconciliation | all | M12/24/36/48/60 |

### 4.2 Calendar

Indicative start 1 May 2028 (M1).

- **Year 1** (M1–M12): calculus v0 (WP1); reference-layer design and
  first prototype (WP2); protocol-family design (WP3); hires 1–4 in
  post; *islands* scoped with partners. **I1.**
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

The critical path runs from WP3(i) through WP3(ii) to D3.3, because
availability-decoupled malicious-secure resolution is both the hardest
result and the one on which Island S's sustained operation depends. WP2
can be scheduled independently of WP3 until the *Cryptographic Link*
class is integrated at I2. WP4 depends on WP2's link typing (M12) but
not on WP3's completion, since it can expose Cryptographic Links as
opaque *affordances* before the underlying protocols are
malicious-secure. Island S can begin measurement before WP2 is
complete; Island L cannot, since its value lies in span-level
verifiable citation.

---

## Section 5 — Risk assessment and mitigation (~1 page)

| # | Risk | L | I | Mitigation |
|---|---|---|---|---|
| R1 | Coordination cost exceeds what islands of realistic size can sustain, so the top link classes are unreachable in practice | M | H | WP1 can return "not attainable" as a result, so this outcome is itself a finding. The lattice degrades gracefully: a negative result at the top rung still yields a validated boundary of attainable bundles, which is publishable. WP2's coordination instrumentation detects the problem early, at I1. |
| R2 | SMPC resolution latency stays too high for interactive use | M | H | The deliverable is the privacy-performance frontier (D3.2), so the result stands either way. Asynchronous and precomputed-randomness designs (WP3 ii), using the preprocessing model of SPDZ/MP-SPDZ, are the primary mitigation; Island S's batch workloads remain viable even if interactive resolution does not. |
| R3 | The malicious-secure arc does not close within budget | M | M | The arc has intermediate publishable states (static, then adaptive adversary). Honest-but-curious results (D3.1) already go beyond the deployed state of the art and stand alone. |
| R4 | **Purpose binding is not technically enforceable after resolution** | H | M | We accept this by design. WP1 scores the guarantee by the margin by which re-requesting is less costly than hoarding, and documents the class as an economic guarantee, the mechanism on which transcopyright and current data-economy proposals both rely. The failure mode is a guarantee that the theory declines to promise for a given actor, which the calculus can express. |
| R5 | Loss of a validation site (editorial partner withdraws; industrial partner reorganizes) | M | H | Two independent islands in unrelated sectors with separate partners, so no single withdrawal ends WP5. Island L has alternative corpora (law journal, moot-court record, and the *Access to Justice* corpus) **[TODO: secure a written second option]**. Island S sits inside a running deployment. |
| R6 | The agent-layer comparison returns a negative or null result | M | L | Pre-registered hypothesis and analysis plan. We expect a null result on task success with a positive result on safety and evolvability, which is publishable; the evaluation is informative in either direction. |
| R7 | The applied-cryptography postdoc cannot be recruited (hardest profile) | M | H | The search opens at the Step 2 result (scheduled for 17 December 2027), about four months before M1. Grau's SMPC expertise covers WP3's first arc regardless. Fallback: two PhD positions with more advisory time from Mitrokotsa and Cheng. |
| R8 | Standardization uptake does not materialize | M | M | WP1 informs the choice of fora, and the PI's specifications have reached shipped products before (WoT TDs). The reference implementation and artifacts stand on their own, independent of adoption. |
| R9 | Legal exposure from the Island L corpus (personal data in citations) | L | M | Retraction is designed in as a superseding record, which reconciles immutability with GDPR Art. 17; DPIA at island scoping; legal partner embedded in WP5 **[TODO: confirm USG ethics/DPIA route]**. |

In R1, R4, and R6 the likely failure is a bounded negative result, and
we design each work package to deliver that result as a finding, as
fits a project whose core contribution is a theory of what is attainable.<!-- was: a theory of what is affordable. -->

