# B1 b.3 and b.4 before the WP restructuring of 2026-10-31

### b.3 Objectives (~0.5 page)

The goal of ISLANDS is to find out which guarantees a Web
architecture can provide to the communities that need them, and at
what cost, and to demonstrate these guarantees in practice. This
involves:

- **O1 — Theory of chosen guarantees.** We develop a formal model
  that relates guarantee bundles (persistence, span addressing,
  bidirectionality, integrity, confidentiality, attribution, trust,
  usage, discoverability) to coordination *and economic* costs, *island*
  size, threat models, and stakeholder incentives. We instantiate the
  model as a taxonomy of named *link classes*: a persistence and
  integrity ladder (*Classic Jumplinks*, *Archived*, *Trusted*, *Verified*,
  and *Cryptographic Links*, in increasing strength) with five
  cross-cutting axes (attribution, trust, usage, modality, *link
  time*).<!-- was: with four
  cross-cutting axes (attribution, trust, usage, modality). --> For each
  class, we prove what it minimally requires, and we derive decision
  procedures that an island designer can apply.
- **O2 — Reference layer.** We build an addressing and *transclusion*
  layer over content-addressed storage. It provides span-level,
  version-pinned, bidirectional, verifiable references, typed by link
  class and able to carry purpose-binding terms, and it interoperates
  with the open Web at island boundaries.
- **O3 — Confidential references.** We turn SMPC-based resolution,
  which verifies a value without disclosing its inputs, from a bespoke
  application protocol [87] into a first-class addressing primitive.
  Each island states its threat model explicitly, from
  honest-but-curious to malicious-secure.
- **O4 — Agent affordance layer.** We build a capability-exposure
  layer through which autonomous agents discover the valid next
  actions in the current state, with link-relation semantics [93]
  and explicit ordering guarantees for state-changing actions.
- **O5 — Validation islands and incentives.** We instantiate and
  evaluate islands in three high-stakes domains: legal citation,
  cross-organizational supply-chain data, and social media.<!-- was: evaluate islands in two high-stakes domains, legal citation and
  cross-organizational supply-chain data. --> For each class of actor, we
  analyze whether islands change the incentive to centralize [9].

### b.4 Research strategy and methods (~1.75 pages)

To achieve these objectives, we propose a theory work package (WP1)
that three systems work packages (WP2–WP4) instantiate and a
validation work package (WP5) tests.

**WP1 — Foundations: the theory of chosen guarantees (M1–M60,
continuous).** Method: formal modeling and design-science iteration.
We develop a *guarantee calculus*, i.e., a lattice of guarantee bundles
ordered by strength. We formalize the bundles as labels in the
information-flow control tradition [94, 95] and extend these
labels with persistence and attribution components. Each bundle
carries its minimal coordination requirements (e.g., registration,
replication, identity, availability coupling) and its admissible
threat models. Here we draw on distributed-systems impossibility
results [96, 97], simulation-based security definitions [98],
and RFC 9518's centralization vocabulary [9]. Some guarantees cannot
be enforced once a reference has resolved, but compliance with them can be made incentive-compatible. The calculus hence also scores each bundle by the margin by which compliance is less costly than defection for the actor able to defect.<!-- was: but they can be priced. The calculus hence also scores each bundle by the margin by which the compliant path undercuts defection for the actor able to defect. --> This
is the mechanism that transcopyright used for reuse [99] and that
current data-economy proposals use for derived insights [43].

To make the calculus checkable, we name each bundle as a *link class*
that a reference can declare and a client can enforce, much as link
relations [93] or HTTP status codes do at lower stakes. The core is
a ladder of persistence and integrity. *Classic Jumplinks* are the
Web default (location-addressed, no guarantee) and the fallback
outside any *island*. *Archived Links* stay resolvable through
redundancy, as with Memento and Perma.cc [31, 60], but are not
verified. *Trusted Links* are registered in the island and tracked
bidirectionally, which makes them accountable but not
cryptographically checked [58]. *Verified Links* are span-level,
version-pinned, and content-addressed, so that resolution matches the
cited bytes exactly or fails visibly. *Cryptographic Links* are
resolved through SMPC or zero-knowledge proofs (O3) and return a
verified derivation from data the client never sees. Further axes cut
across the ladder. *Attribution* is non-monotone, since binding
actions to identities trades accountability against chilling effects
[100, 101]; European courts have weighed this balance since the
census judgment [102] and for anonymous online comment [103].
Attribution is hence a pair (*Attributed* versus *Anonymous/Pseudonymous
Links* [45]), which we evaluate against island governance<!-- was: which we price against island governance --> as well as
coordination cost. *Trust* adds *Endorsed Links*, whose resolution
carries a decay-bounded, Sybil-resistant [104] score over retractable
endorsements, and *Credentialed Links*, whose resolution returns a
*verifiable credential* about the source together with its current
revocation status [14]. Endorsements aggregate the judgment of
peers; credentials rest on the authority of an issuer, and the island
decides which issuers it accepts. *Usage* adds *Purpose-Bound Links*, whose terms
(recipient, purpose, window) travel with the reference, so that an
expired derivation is re-resolved instead of reused. Since no
substrate can prevent retention [80], we assess this class by its compliance margin<!-- was: we price this class economically -->. *Modality* adds *Capability Links* (O4's state-dependent
*affordances*), to which every rung applies as it does to content.
*Link time* records when a reference is resolved, in the sense of
program linkers [105]. Capability Links bind as late as
possible, at each interaction. *Static Links* bind at design time,
in a fixed binary encoding, as Web of Things descriptions already
allow for protocols such as Modbus [106]. They give up the
evolvability that a uniform interface provides and regain the efficiency it sacrifices<!-- was: evolvability that a uniform interface buys and regain the efficiency it costs --> [48], which suits fixed, high-speed installations. Like
attribution, *link time* is non-monotone: the calculus assesses it by when the coordination cost is incurred, once at design time or incrementally at every interaction<!-- was: the calculus prices it by when coordination is paid, once at design time or a little at every interaction -->.

A declared class is a falsifiable claim with two proof obligations.
*Realizability* requires that, under its coordination requirements
and threat model, a conforming implementation returns the class's
guarantee or fails visibly, and never downgrades silently. *Necessity*
requires that dropping any one requirement admits an execution that
violates the guarantee undetected, i.e., that no rung can be attained at lower coordination cost<!-- was: no rung can be had more cheaply -->. For an island of given size, stake, and threat model, the
calculus then predicts the highest class it can sustain and at what
cost. We develop the calculus iteratively against the WP2–WP4 designs
and test it against WP5 measurements: every architectural choice in
the systems work packages should be derivable from the theory or
force a revision of it. Deliverables are the formal model, the
link-class taxonomy, design decision procedures, and a published
island design handbook.

**WP2 — The reference layer (M1–M42).** Method: systems research with
a reference implementation. We design the island addressing model.
Span-level identifiers are pinned to immutable versions in a
Merkle-DAG store, which we build on Git and IPFS primitives [69] and
on SWHIDs [70], following RFC 9518's advice to reuse proven
mechanisms [9]. A bidirectional link registry scoped to the island
makes explicit the coordination that Xanadu wanted globally and the
Web refused [39], and *transclusion* records its provenance [71].
Every reference is typed by its WP1 link class, and the type is
enforced structurally. Resolving a Verified or Cryptographic Link
thereby returns the exact cited span (or a verified derivation of it)
or fails visibly. The registry stores retraction as a superseding
record and deletes nothing. A Verified or Trusted Link can hence honour
a legal erasure request [107] without breaking the immutable history
on which other references depend. Boundary design runs in both
directions. Outbound, references degrade gracefully at the island
edge: a Verified or Cryptographic Link becomes a Classic Jumplink for
a non-member client, carrying a text fragment [64] that keeps
the cited passage addressable where the page still contains it, and
interoperates with Memento [60] and robust hyperlinks [61].<!-- was: a non-member client and interoperates with Memento [60] and robust
hyperlinks [61]. --> Inbound, an *admission protocol* (the *border
crossing*) lets a client discover the island's NFP set and bind to it.
The binding is a *credible commitment* in the sense of the W3C TAG
[23]: the client's user agent restricts the use of the island's
content, and nothing beyond it, and keeps that restriction loyally
after admission, e.g., by re-resolving a Purpose-Bound Link once its
terms expire.
This is where the island applies its attribution regime (e.g., by
asking the client to present verifiable credentials, with selective
disclosure [89], or by issuing one), and where the<!-- was: This is where the island applies its attribution regime (e.g., by
issuing a credential or asking for verified identity), and where the -->
guarantee bundle becomes enforceable on the client as well as on
stored content. We benchmark the reference implementation per link
class for resolution latency, storage overhead, and link-maintenance
cost at island scales of 10² to 10⁵ members, and we publish all
artifacts.

**WP3 — Confidential and verifiable references (M6–M54).** Method:
cryptographic protocol design with proofs and empirical benchmarks. We
generalize the PEP-LCA results [87, 88] into a *resolution
protocol family*. In this family, a reference's target is
secret-shared across island members, and its resolution is a joint
computation with a verifiable result. Research arcs: (i) from
honest-but-curious to malicious security, using verifiable secret
sharing [108] and zero-knowledge correctness proofs, which we expect
to yield a quantified privacy-performance frontier; (ii) protocols
that tolerate member downtime, which removes the availability coupling
we documented in PEP-LCA [87]; and (iii) input integrity through
committed inputs and attested sources that connect to hardware-rooted
provenance [34]. We prove security in the simulation-based model
[98] and evaluate performance on realistic island topologies,
together with K. Mitrokotsa and N. Cheng, who co-supervised the
PEP-LCA work [87].

**WP4 — Agents as hypermedia clients (M12–M54).** Method: design and
comparative evaluation. We build the island's agent gateway, which
exposes capabilities as state-dependent affordances made perceivable
through *signifiers* [109]. The gateway is a hypermedia-driven layer
[48] over MCP-class agent protocols [52]. It explains *why* an
action is currently valid and gives explicit ordering guarantees for
dependent state-changing calls. Each affordance carries the WP1 link
class of the resource it exposes, so that an agent can tell a Verified
citation from a Classic Jumplink before acting on it. The gateway is
also the border crossing for agent clients. An agent's first
affordance is the acceptance of the island's NFP set, together with a
verifiable credential that states on whose behalf the agent acts, and
identity and obligations hence bind before any state-changing call.<!-- was: affordance is the acceptance of the island's NFP set, and identity and
obligations hence bind before any state-changing call. --> WP4 extends our
work on signifiers [50, 51, 91] towards standardization in the
W3C Autonomous Agents on the Web Community Group.<!-- was: W3C Web Agents Community Group. --> We compare task success, safety
violations, evolvability, and latency under (a) statically linked
tool catalogues, (b) our affordance layer, (c) hybrids, and (d) Static
Links over binary protocol bindings, in scenarios drawn from WP5 and
from fixed installations in building automation (Siemens) and edge
computing (AFarEdge). We expect affordance-scoped exposure to
outperform statically linked catalogues on safety and evolvability
without loss of task success, and Static Links to outperform both on
latency where the installation does not change. The measurements
thereby locate, for each scenario, the link time the calculus should
recommend.<!-- was: violations, and evolvability under (a) static tool catalogues, (b) our
affordance layer, and (c) hybrids, in scenarios drawn from WP5. We
expect affordance-scoped exposure to outperform static catalogues on
safety and evolvability without loss of task success. -->

**WP5 — Validation islands and stakeholder incentives (M12–M60).**
Method: three case studies and a mixed-methods incentive
analysis.<!-- was: Method: two full-depth case studies and a mixed-methods incentive
analysis. --> *Island L (legal citation)* is an
end-to-end pilot in which the citations in a working corpus (e.g., a
law journal's editorial pipeline or a moot-court record) become
span-level, version-pinned, and verifiable, anchored to ECLI and ELI
identifiers where these exist [29, 30]. We measure the
citation-integrity failures made structurally impossible, the
editorial cost compared to Perma-style manual archiving [31], and
practitioner acceptance. Island L also instantiates the *attribution*
NFP. It weighs verified authorship, which makes fabrication
sanctionable, against pseudonymous regimes, which may shield sensitive
filings. Our legal partner is Prof. Tamò-Larrieux (Lausanne), whose
group's doctoral work on chilling effects grounds the anonymity side,
and Island L docks onto the PI's running law/technology projects
(SNSF CoCoDa; *Access to Justice*). *Island S (supply chain)* extends
the running PEP-LCA deployment [87, 88] into a full island with
confidential references and agent-mediated onboarding, together with
its industrial partners (Empa, Siemens). We test it against the
disclosure duties of the EU battery passport and the Carbon Border
Adjustment Mechanism, which require emissions data from upstream
suppliers, including installations outside the EU [28, 110]. Since
CBAM requires actual emission values to be checked by accredited
verifiers [111], Island S also tests Credentialed Links that
carry the verifier's attestation together with the confidential
value. *Island M (social media)* gathers public-interest publishers
(e.g., public broadcasters, election authorities, and newsrooms) on a
federated network [67]. Their posts become version-pinned
and attributed, edits and deletions become superseding records, and
Credentialed Links state who stands behind an account, which a
purchasable badge does not [13]. *Purpose-Bound Links* carry the
terms under which model providers may use the posts, an alternative to
the login wall with which Reddit now protects its content [24].
Vetted researchers resolve
Cryptographic Links to exposure statistics that instance operators
compute jointly over interaction data that none of them discloses.
Island M thereby tests confidential references against the
researcher data access of the DSA [11] and against the gap between
released and seen data that we documented [16, 17]. We measure the
survival of posts and links compared to platform baselines [7], the
share of research queries answered without raw-data transfer, and
acceptance by publishers and researchers.

The *incentive analysis* studies each class of actor (hyperscaler,
legacy industry, OSS/privacy community, browser vendor, platform,
public record-keeper) through interviews, institutional analysis of
funding models, the RFC 9518 mitigation checklist [9], and the W3C
TAG's societal-impact self-review, which asks about power dynamics and
points of centralization [112]. For each
class, it asks whether an island changes the actor's incentive to
centralize. It also asks whether an island can be configured so that
the guarantee-respecting path is the actor's least costly one, since a guarantee that no actor has an incentive to keep<!-- was: the actor's cheapest one, since a guarantee that no actor is paid to keep --> is one the theory should
decline to promise. The analysis thereby delivers the stakeholder half
of O1's decision procedures. It builds on our platform-audit work
[16, 17], our working relationship with Solid's steward (the ODI,
a CoCoDa partner), and the PI's seat on the European VLOP-auditing
oversight board.

**Integration and openness.** Annual integration milestones bind the
WP2–WP4 prototypes into one architecture, which WP5 then evaluates.
All software is open source, and all publications are open access.
All specifications go to the W3C groups that maintain the protocols
islands build on, or to their successors: the Linked Web Storage
Working Group (reference layer), the Social Web Working and Community
Groups (Island M), the Verifiable Credentials and Federated Identity
Working Groups (admission), the Web of Things Working Group (Static
Links), and the Autonomous Agents on the Web Community Group (agent
layer). Each specification first passes the TAG's societal-impact
self-review [112].<!-- was: All software is open source, all specifications go to open fora
(e.g., a W3C Community Group or the IETF, as WP1 informs), and all
publications are open access. -->

