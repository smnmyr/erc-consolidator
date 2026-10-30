# B1 Section b as of 2026-10-04, before the narrative opening and numbered references

Kept verbatim (including its inline `<!-- was: -->` comments) so deleted text stays recoverable.

## Section b — Extended synopsis (max 5 pages)

### b.1 The problem and the idea (~1 page)

The World Wide Web's original design favored simplicity,
decentralization, and low coordination overhead, which enabled
explosive adoption but sacrificed stable references, built-in
versioning, and native bidirectional linking. Its road not taken,
Project Xanadu, insisted on the opposite: immutable versions,
addressable spans, and fine-grained *transclusion* (reuse that
carries a persistent, verifiable reference back to its source), at the
price of global coordination the early Web rightly refused. As requirements shift toward durability and accountability, Xanadu-style guarantees (persistent citation, traceable reuse, integrity) become more attractive, at the cost of the coordination overhead the Web originally avoided.<!-- was: As
requirements shift toward durability, verifiability, and
accountability, the case for Xanadu-style guarantees (persistent
citation, traceable reuse, integrity) becomes architecturally more
attractive, at the cost of the coordination overhead the Web
originally avoided. -->

The shift is already visible, and it hits the legal system hardest, because in law a reference's stability *is* the substance of the claim it supports.<!-- was: That shift is no longer hypothetical, and the legal system is where it
lands hardest, because law is where a reference's stability *is* the
substance of the claim it supports. --> Roughly half of URLs cited in
U.S. Supreme Court opinions and >70% in flagship law journals no
longer resolve to what they cite; the profession's remedy (Perma.cc)
manually rebuilds, citation by citation, the coordination layer the
Web never had. By early 2026, over 1,200 court decisions worldwide
involved AI-fabricated citations (references that were never real,
with no architectural way to check), triggering escalating sanctions
and, in 2026, appellate-level discipline and a license suspension. Deepfake
growth is pushing provenance into camera silicon (C2PA) and statute
(EU AI Act, from August 2026; proposed US FRE 707). And 50+
AI-copyright suits, led by *NYT v. OpenAI*, litigate at enormous cost a question that native transclusion would have recorded for free: which sources were consumed, in what form, with what attribution. In each case the Web's avoided coordination cost was deferred and is now re-billed, per incident, to whoever stands downstream.<!-- was: litigate at enormous cost
a question — which sources were consumed, in what form, with what
attribution — that native transclusion would have recorded for free.
The pattern across all four: the Web's avoided coordination cost was
deferred and is being re-billed, per incident, to whoever stands
downstream. --> Each field is already paying it by hand, bolting a private
profile of guarantees onto Web architecture to treat its own symptom
while the principles that produced the problem stay untouched.

**The idea.** ISLANDS designs, formalizes, and validates the *island*:
a bounded information space (a legal-citation community, a supply chain, a health-data federation)<!-- was: (a legal-citation ecosystem, a supply
chain, a health-data federation) --> whose members share stakes high
enough to afford coordination. An island is the unit through which a
*new Web* carries the *non-functional properties* (NFPs) today's Web
cannot hold together: each island selects the NFPs its stakes demand
and satisfies them at once, letting communities with heterogeneous
requirements interoperate under one architecture while staying
backwards-compatible with the open Web. Within an island, references
are span-level, version-pinned, bidirectional, and verifiable; across
islands and toward the open Web, the architecture keeps the Web's
low-coordination interoperation. Entering an island is an explicit act: at its boundary<!-- was: Entering an island is an explicit act,
not a mere fetch: at its boundary --> a client, human or agent, crosses a
*border* where it is shown the island's NFP set and accepts the
obligations of membership (the point at which the attribution regime is
applied), while outsiders still read island content over the open Web
through degraded references. Beyond both parents, islands add *confidentiality-preserving references*:<!-- was: through degraded references. Two extensions go beyond both
parents. First, *confidentiality-preserving references*: --> in
multi-organization islands, members must reference and compute over
each other's data without exposing it; building on our own deployed
secure multi-party computation (SMPC) systems, a reference becomes "a
pointer to a value you can verify was correctly derived from bytes you
may not read." Its companion is *purpose binding*: the terms on which a
party was willing to answer a reference at all (for this recipient,
this purpose, this window) travel with the derivation instead of
lapsing at the moment of disclosure, so a reference is re-resolved when its terms expire. Islands also treat *agents as a first-class client class*: the Web's access pattern is shifting from read-and-navigate to ask-and-respond,<!-- was: so a reference is re-resolved when
its terms expire rather than reused
indefinitely. Second, *agents as a first-class client class*: the Web's
access pattern is shifting from Read→Navigate to Ask→Response, --> with AI
intermediaries controlling the front door to content (a new
centralization vector), while today's static agent tool catalogues
repeat the hard-coding mistake of CRUD-over-HTTP; islands instead
expose capabilities through state-dependent, hypermedia-style
affordance discovery, so the island, not the intermediary, shapes what
agents can see and do. These NFPs include *attribution*: the same
machinery that makes a reference verifiable can also bind it to an
author, so an island chooses where it sits between verified authorship,
under which a fabricated citation becomes a sanctionable act, and
unlinkable anonymity, which keeps participation from being chilled;
cryptographic identity (anonymous credentials, revocable pseudonyms)
turns the choice into a continuum with designed intermediate points.<!-- was: makes this a designed frontier rather than a binary switch. --> The
unifying scientific contribution is a **theory of chosen
guarantees**: a principled account of which NFP bundles an island can
provide, at which coordination cost, under which threat model, for
which stakeholders. Neither forty years of hypertext
research nor thirty years of Web engineering has produced such an
account.

Figure 1 shows the resulting architecture: a guarantee stack an island
assembles over a content-addressed substrate, with the theory (O1)
selecting the affordable bundle and the open Web reached through a
low-coordination boundary.

```
   +----------------------------- ISLAND -----------------------------+
   |  a bounded information space (legal citation, supply chain, ...)  |
   |                                                                   |
   |   O4  Agent affordance layer                                      |
   |       state-dependent capability discovery for autonomous agents  |
   |   O3  Confidential references                                     |
   |       SMPC resolution: verify a value without reading its bytes   |
   |   O2  Reference and transclusion layer                            |
   |       span-level . version-pinned . bidirectional . verifiable    |
   |   --  Content-addressed substrate                                 |
   |       Merkle-DAG over Git / IPFS / SWHID primitives               |
   |                                                                   |
   |   O1  Theory of chosen guarantees: which layers an island of a    |
   |       given size, stake, and threat model can afford, at what     |
   |       coordination cost, and for which stakeholders.              |
   +-------------------------------------------------------------------+
      |  ^   inward: cross the border, accept the island's NFP set       
      |  |   (attribution regime applied); outward: low-coordination     
      v  |   interop, references degrade gracefully (Memento/robust)     
    open Web                                                           

   O5  instantiated and measured in two high-stakes islands:
       Island L (legal citation)   .   Island S (supply chain)
```

*Figure 1. The ISLANDS reference architecture. Layers map to objectives
O2–O4 over a content-addressed substrate; O1 is the cross-cutting theory
that decides which layers a given island can afford; O5 validates the
whole in two domains. To be redrawn as a vector figure in the template.*

### b.2 State of knowledge and the gap (~0.75 page)

The ingredients of an island exist separately, but nobody has composed them or explained which combinations an island can afford.<!-- was: Every ingredient exists in isolation; the composition and the theory
do not. --> Hypertext research (Bush, Engelbart, Nelson) assumed rich,
versioned, span-anchored links and named its own agenda early (Halasz's
"seven issues," 1988); the open-hypermedia systems that followed built
versioned links and referential integrity at workgroup scale (Microcosm;
Davis 1998), so link rot was a solved problem before the Web made it
endemic. The Web scaled by dropping these guarantees deliberately
(Berners-Lee 1989; Fielding's REST), in full knowledge of how to provide them.<!-- was: (Berners-Lee 1989; Fielding's REST), not for want of knowing how to
provide them. --> Remedial
infrastructure such as DOIs, Web archiving, Memento (RFC 7089),
Perma.cc, and robust links accepts the mutable substrate and builds compensating
archives beside it: it neither prevents drift nor verifies integrity,
and it recreates central coordination points. This is the general shape
of the field's response: services and platforms each assemble a bespoke
NFP profile on top of Web architecture (persistence via Perma.cc,
provenance via C2PA, identity and notarization via DOIs or blockchains),
treating a symptom in one silo while the architectural principles that
produce it stay in place. Such profiles are evidence of demand for
chosen guarantees; being unshared and non-composable, they do not
supply them, and several would be subsumed by an island's Xanadu-style
constraints made selectable per island.<!-- was: constraints made selectable rather than rebuilt per domain. --> Content-addressed and
versioned storage (Git, IPFS, Software Heritage's ISO-standardized
SWHIDs) and provenance attestation (W3C PROV, C2PA) supply the substrate Xanadu lacked<!-- was: supply exactly the
substrate Xanadu lacked -->, but only as storage and signing primitives:
they offer no span semantics, no link layer, and no governance model.
Nanopublications come closest: a deployed,<!-- was: The nanopublication ecosystem comes closest: a deployed, --> federated
network of immutable, signed, hash-identified (self-verifying)
semantic statements with a decentralized, Sybil-resistant trust
layer. It is in effect a working island at statement granularity, and
a candidate component for ours, but it lacks span addressing over
arbitrary content, transclusion, and confidentiality-preserving
resolution.
Re-decentralization efforts relocate *control* and leave *addressability* as it was:<!-- was: Re-decentralization efforts relocate *control*, not *addressability*: -->
Solid's pods (now ODI-stewarded, deployed as civic infrastructure in
Flanders) keep location-addressed mutable resources; data spaces
(Gaia-X, PACT) relocate contracts and governance. Work in that same
line now argues that raw-data transfer cannot sustain a market at all
and proposes trading purpose-bound derivations under terms limiting
their shelf life and use, which gives up on the resource as the unit of
exchange but supplies no reference layer able to name such a
derivation, pin it to a version, or carry its terms. Usage control
formalized such terms two decades ago (UCON, Park and Sandhu 2004;
distributed usage control, Pretschner, Hilty, and Basin 2006), and
sticky policies bind them to the data itself (Pearson and Casassa Mont
2011), but enforcement after release needs a trusted monitor at the
recipient or falls back on detection after the fact, and none of this
work attaches the terms to a pinned, re-resolvable reference. RFC 9518 shows why
open specifications alone do not prevent practical centralization
(the XMPP and Solid/Inrupt patterns) and supplies design-level
mitigations this project adopts. SMPC has matured into deployed
systems: our own PEP-LCA protocol computes joint supply-chain
assessments across up to 50,000 participants with no trusted third
party, and our Solid Symposium 2026 system anchors SMPC share
disclosure in Solid's access-control layer with WASM-sandboxed data
transformation. Information-flow control took the systems route to
the same problem: the decentralized label model (Myers and Liskov 1997)
and Fabric (Liu et al. 2009) let mutually distrusting principals share
persistent objects under confidentiality and integrity labels, but
enforce them by placing cleartext only on nodes the owner trusts, over
mutable, store-identified objects, without pricing what a policy costs
to sustain. Hypermedia multi-agent systems research (including the
PI's AAMAS 2019 line) has long argued for runtime affordance
discovery; current LLM-agent practice (static tool lists) runs
opposite to it, and no existing design connects capability discovery<!-- was: and no framework connects capability discovery --> to a
verifiable reference layer.

**The gap:** no existing system composes immutability, span-level
verifiable addressing, transclusion, confidentiality-preserving
resolution, and agent-facing affordance discovery into one reference
architecture; and no existing theory predicts which of these
guarantees an island of a given size, stake, and threat model can
afford.<!-- was: afford. That composition and that theory are the ground ISLANDS
breaks. -->

### b.3 Objectives (~0.5 page)

- **O1 — Theory of chosen guarantees.** A formal model relating
  guarantee bundles (persistence, span addressing, bidirectionality,
  integrity, confidentiality, attribution, trust, usage,
  discoverability) to coordination *and economic* costs, island size,
  threat models, and stakeholder incentives, instantiated as a named
  **link-class** taxonomy: a core persistence/integrity ladder
  (Classic Jumplinks, Archived, Trusted, Verified, and Cryptographic Links, in increasing strength)<!-- was: (Classic Jumplinks → Archived → Trusted → Verified → Cryptographic Links) --> plus
  four cross-cutting axes (attribution, trust, usage, modality), each
  class with proofs of what it minimally requires; with decision
  procedures an island designer can apply.
- **O2 — Reference layer.** An addressing and transclusion layer
  providing span-level, version-pinned, bidirectional, verifiable
  references, typed by link class and able to carry purpose-binding
  terms, over content-addressed storage, interoperating with the open
  Web at island boundaries.
- **O3 — Confidential references.** Elevation of SMPC-based
  verifiable-but-undisclosed resolution from bespoke application
  protocols (our PEP-LCA) to a first-class addressing primitive, with
  explicit per-island threat-model semantics (from honest-but-curious to malicious-secure, via verifiable secret sharing and zero-knowledge proofs)<!-- was: (honest-but-curious →
  malicious-secure via verifiable secret sharing and zero-knowledge
  proofs) -->.
- **O4 — Agent affordance layer.** A capability-exposure layer for
  autonomous agents: state-dependent, hypermedia-style discovery of
  valid next actions, with link-relation semantics and explicit
  ordering/consistency treatment for state-changing agent actions.
- **O5 — Validation islands and incentives.** Instantiation and
  empirical evaluation in two high-stakes domains (legal citation
  infrastructure and cross-organizational supply-chain data), plus a
  stakeholder-incentive analysis (per RFC 9518) determining, per actor
  class, whether islands change the incentive to centralize.

### b.4 Research strategy and methods — draft (~1.75 pages)

WP1 provides the theory that the systems work packages (WP2–WP4) instantiate and the validation work package (WP5) tests.<!-- was: The project runs five interlocking work packages over 60 months; WP1
provides the theory that the systems WPs instantiate and the
validation WP tests. (High-level strategy only; implementation and
feasibility detail is deliberately excluded at this stage.) -->

**WP1 — Foundations: the theory of chosen guarantees (M1–M60,
continuous).** Method: formal modeling and design-science iteration.
We develop a guarantee calculus: a lattice of guarantee bundles
ordered by strength and formalized as labels in the information-flow
control tradition (Myers and Liskov 1997), extended with persistence
and attribution components. Each bundle is annotated with its minimal
coordination requirements (registration, replication, identity,
availability coupling) and admissible threat models, drawing on
distributed-systems
impossibility results, the SMPC security-model literature, and RFC 9518's centralization vocabulary. Some guarantees cannot<!-- was: RFC
9518's centralization vocabulary. Coordination cost is not the only
currency. Some guarantees cannot --> be enforced once a reference has
resolved but can be priced, so the calculus also scores each bundle by
the margin by which the compliant path undercuts defection for the
actor able to defect, which is the mechanism transcopyright used for
reuse and current data-economy proposals use for derived insights. To
make the calculus checkable, each bundle is named as a *link class* a
reference can declare and a client can enforce, the operational role
RFC 8288 link relations or HTTP status codes play at lower stakes. The
core is a persistence/integrity ladder: **Classic Jumplinks** (the Web
default, location-addressed, no guarantee; the fallback outside any
island), **Archived Links** (kept resolvable by redundancy, as Memento
and Perma.cc do, but not verified), **Trusted Links**
(island-registered and bidirectionally tracked, accountable but not
cryptographically checked), **Verified Links** (span-level,
version-pinned, content-addressed: resolution matches the cited bytes
exactly or fails visibly), and **Cryptographic Links** (SMPC/ZK-resolved
per O3: a verified derivation from data the client never sees). Further axes cut across the ladder without lengthening it.<!-- was: Four
axes cut across the ladder without lengthening it. --> *Attribution* is
non-monotone, since binding actions to identities trades
accountability against chilling effects, so it is a pair (Attributed
versus Anonymous/Pseudonymous Links) priced against island governance
as well as coordination cost. *Trust* adds Endorsed Links, whose
resolution carries a decay-bounded, Sybil-resistant score over
retractable endorsements. *Usage* adds Purpose-Bound Links, whose
terms (recipient, purpose, window) travel with the reference, so an
expired derivation is re-resolved instead of reused; since no
substrate can prevent retention, this class is priced economically.<!-- was: this class is priced economically
instead of asserted as a hard guarantee. --> *Modality* adds Capability
Links, O4's state-dependent affordances, to which every rung applies
as it does to content. A declared class is a falsifiable claim with
two proof obligations. *Realizability:* under its coordination
requirements and threat model, a conforming implementation returns the
class's guarantee or fails visibly, never silently downgrading.
*Necessity:* dropping any one requirement admits an execution that
violates the guarantee undetected, so no rung can be had more cheaply.
The calculus then predicts, for an island of given size, stake, and
threat model, the highest class it can sustain and at what cost. The calculus is developed
iteratively against WP2–WP4 designs and falsified against WP5
measurements: every architectural choice in the systems WPs must be
derivable from, or force a revision of, the theory. Deliverables:
formal model, the full link-class taxonomy, design decision
procedures, and a published "island design handbook."

**WP2 — The reference layer (M1–M42).** Method: systems research with
a reference implementation. We design the island addressing model:
span-level identifiers pinned to immutable versions in a Merkle-DAG
store (building on Git/IPFS primitives per RFC 9518's
reuse-proven-mechanisms guidance), a bidirectional link registry
scoped to the island (making explicit the coordination Xanadu wanted
globally and the Web refused), and transclusion with recorded
provenance (W3C PROV-compatible). Every reference is typed by its WP1
link class, and the type is enforced structurally: resolving a Verified or Cryptographic Link either returns the exact cited span (or a verified derivation of it) or fails visibly. The same registry stores retraction as a superseding record and deletes nothing, so<!-- was: the type is enforced structurally rather than merely
documented: resolving a Verified or Cryptographic Link either returns
the exact cited span (or a verified derivation of it) or fails
visibly, never a silent downgrade. The same registry stores retraction
as a superseding record rather than a deletion, so --> a Verified or
Trusted Link can honor a legal erasure request without breaking the
immutable history other references depend on. Boundary design runs both ways. Outbound, references degrade gracefully at the island edge: a Verified or Cryptographic Link becomes a Classic Jumplink for a non-member client, interoperating with Memento and Robust Links. Inbound, an *admission protocol* (the border crossing) lets a client discover the island's NFP set and bind to it; this is where the attribution regime is applied (issuing a credential, or asking for verified identity) and where the guarantee bundle becomes enforceable on the client as well as on stored content.<!-- was: Boundary design runs in two
directions: outbound, how references degrade gracefully when they cross
the island edge to the open Web — a Verified or Cryptographic Link
becomes a Classic Jumplink for a non-member client, interoperating
with Memento/robust-links rather than replacing them; and inbound, an
*admission protocol* (the
border crossing) by which a client discovers the island's NFP set and
binds to it, the point at which the attribution regime is applied
(issued a credential, or asked to present verified identity) and the
guarantee bundle becomes enforceable on the client rather than only a
property of stored content. -->
Evaluation: reference implementation benchmarked per link class for
resolution latency, storage overhead, and link-maintenance cost at
island scales (10²–10⁵ members), with public artifacts.

**WP3 — Confidential and verifiable references (M6–M54).** Method:
cryptographic protocol design with proofs and empirical benchmarks. We
generalize our PEP-LCA results into a *resolution protocol family*:
references whose targets are secret-shared across island members and
whose resolution is a joint computation with a verifiable result.
Research arcs: (i) from honest-but-curious to malicious-secure
(verifiable secret sharing, ZK correctness proofs), quantifying the
privacy-performance frontier; (ii) breaking the availability coupling
our own prior work documents (protocols tolerant to member downtime);
(iii) input-integrity mechanisms (committed inputs; attested sources
connecting to C2PA-style hardware roots). Security proofs in standard
simulation-based models; performance evaluated on realistic island
topologies. External cryptographic collaboration: K. Mitrokotsa and
N. Cheng (continuing the supervision constellation of our thesis
work).

**WP4 — Agents as hypermedia clients (M12–M54).** Method: design and
comparative evaluation. We build the island's agent gateway:
capability exposure as state-dependent affordances (a HATEOAS-style
layer over MCP-class agent protocols), with semantics for *why* an
action is currently valid and explicit ordering guarantees for
dependent state-changing calls; each affordance also carries the WP1
link class of the resource it exposes, so an agent can tell a Verified
citation from a Classic Jumplink before acting on it, with the same typing WP2 enforces<!-- was: before acting on it — the same typing
WP2 enforces --> for human-facing references. The gateway is also the border crossing
for agent clients: an agent's first affordance is acceptance of the
island's NFP set, so identity and obligations bind before any
state-changing call. This extends the PI's signifier line
(AAMAS 2023/2024) toward standardization via the W3C Web Agents CG.
Evaluation compares agent task performance, safety violations, and
evolvability under (a) static tool catalogues, (b) our affordance
layer, (c) hybrids, across island scenarios from WP5. Hypothesis:
affordance-scoped exposure dominates static catalogues on safety and
evolvability without sacrificing task success.

**WP5 — Validation islands and stakeholder incentives (M12–M60).**
Method: two full-depth case studies plus mixed-methods incentive
analysis. *Island L (legal citation):* an end-to-end pilot in which
citations in a working corpus (e.g., a law journal's editorial
pipeline or a moot-court record) are span-level, version-pinned, and
verifiable. We measure citation-integrity failures made structurally
impossible, editorial cost versus Perma-style manual archiving, and
practitioner acceptance; it also instantiates the *attribution* NFP,
weighing verified-authorship against pseudonymous regimes for the
accountability that makes fabrication sanctionable and the shielding
sensitive filings need; with legal partner Prof. Tamò-Larrieux
(Lausanne), whose group's doctoral work on chilling effects grounds the
anonymity side of the attribution analysis, docking onto the PI's
running law/technology projects
(SNSF CoCoDa; *Access to Justice*). *Island S (supply chain):*
extension of our running GDT/PEP-LCA deployment into a full island
(confidential references, agent-mediated onboarding) with its existing
industrial constellation (Empa, Siemens). *Incentive analysis:*
per-actor-class study (hyperscaler, legacy industry, OSS/privacy
community, browser vendor, platform) combining interviews,
institutional analysis of funding models, and the RFC 9518 mitigation
checklist, asking of each actor whether an island changes the incentive to centralize and whether it can be configured so the guarantee-respecting path is that actor's cheapest one, since a guarantee no actor is paid to keep is one the theory should decline to promise. This delivers the stakeholder half of O1's decision procedures, grounded in<!-- was: asking of each actor not only whether an island changes the
incentive to centralize but whether it can be configured so the
guarantee-respecting path is that actor's cheapest one, since a
guarantee no actor is paid to keep is one the theory should decline to
promise; delivering the stakeholder half of O1's decision
procedures, grounded in --> the team's direct line to Solid's steward
(the ODI, a CoCoDa partner) and the PI's seat on the European
VLOP-auditing oversight board.

**Integration and openness.** Annual integration milestones bind
WP2–WP4 prototypes into one architecture evaluated in WP5; all
software open-source, all specifications submitted to open fora (W3C
CG or IETF as appropriate; itself a WP1-informed choice), all
publications open access.

### b.5 Team (~0.25 page)

The PI (≥40% commitment; stepped down as Dean in February 2026 to refocus on research)<!-- was: The PI (≥40% commitment; stepping down as Dean in February 2026
specifically to refocus on research) --> has led both halves of the
project's intellectual ancestry: the machine-usable-Web line (W3C Web
of Things standardization now deployed in industrial products;
hypermedia multi-agent systems, AAMAS 2019; signifiers as first-class
abstractions, AAMAS 2023/2024) and the law/technology co-design line
(Routledge book *AI and Law*, 2025; Nature Computational Science,
2025; membership in the European VLOP-auditing oversight board). The
starting team carries the two running systems the project builds on:
**Luka Bekavac** (through 2029, ≈M20) brings the empirical/regulatory
instrument set (platform transparency, DSA data-access auditing,
integrity-by-design referencing), anchoring WP5's legal island and
incentive analysis; **Jan Grau** (through 2029, ≈M20) built the
PEP-LCA SMPC stack and its Solid integration, anchoring WP3's first
arc and Island S. Planned recruitment adds an applied-cryptography
postdoc (WP3 lead, from M1), two PhD students (reference layer, WP2,
M1; agent layer, WP4, ~M6), a socio-technical postdoc succeeding the
Bekavac line (WP5, from ~M17 with overlap), a further PhD student on
the legal island (from ~M21, co-supervised with the legal partner),
and a research engineer sustaining the shared prototype. External
collaborators: Mitrokotsa/Cheng (cryptography, continuing the PEP-LCA
supervision constellation), Ciortea (hypermedia MAS, USG),
Tamò-Larrieux (law, Lausanne), the ODI/Solid community (via CoCoDa),
and the industrial WISER constellation (Empa, Siemens).

### b.6 Ambition, risk, gain (~0.25 page)

ISLANDS bets that a coordination cost two generations of architects
deemed prohibitive is affordable at island scale; that cryptographic
reference resolution can be fast enough for interactive use; and that
actors with divergent incentives will adopt shared guarantees. Each bet can fail, which is why the theory (O1) treats guarantees as *chosen* and why<!-- was: Each
bet can fail; that is why the theory (O1) treats guarantees as
*chosen* rather than assumed, and why --> validation (O5) measures
incentives as well as latency. If the bets pay off, the gain is a
validated architectural alternative for those parts of the<!-- was: for exactly those parts of the -->
information space (the legal record,<!-- was: information ecosystem (the legal record, --> the scientific record,
regulated industrial data) where the Web's founding trade-off now demonstrably
fails at a cost measured in sanctions, suspended licenses, statutory
retrofits, and years-long litigation; and a habitat in which
autonomous agents can act on high-stakes information without
inheriting the Web's unverifiability. This is not an incremental
improvement of Web infrastructure: it is a re-negotiation of its
founding trade-off, with the evidence, the components, and the team to
carry it out arriving only now.

---



<!-- b.5 PI paragraph as of 2026-10-05, before the consolidation rewrite -->
The PI (≥40% commitment; stepped down as Dean in February 2026 to
refocus on research) has led both halves of the project's
intellectual ancestry: the machine-usable-Web line (Web of Things
architecture [ref] and its W3C standardization
[ref], now deployed in industrial products; hypermedia multi-agent
systems [ref]; signifiers as first-class abstractions
[ref]) and the law/technology
co-design line [ref],
with membership in the European VLOP-auditing oversight board. The
starting team
