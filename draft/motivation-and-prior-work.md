# ERC Consolidator Grant 2027 — Draft: Motivation & Prior Work

**Working title:** ISLANDS — Bounded Information Spaces with Chosen
Guarantees: Rebalancing the Web/Xanadu Trade-off for High-Stakes
Information

> **How this draft maps to the ERC 2027 application structure.** From the
> 2026/2027 Work Programmes onward, Part B1 carries the *idea* (1-page
> abstract + 5-page extended synopsis + 4-page CV; evaluated alone at
> Step 1, where feasibility is *not* assessed), and Part B2 carries the
> implementation (state of the art & objectives + methodology, max. 14
> pages for sections a+b; evaluated at Step 2). The **Motivation** below
> is written to be compressed into the B1 extended synopsis and to open
> B2 section (a); the **Prior Work** section is the state-of-the-art
> core of B2 section (a). Cross-references from B1 to B2 must be
> avoided in the final text (Step 1 panels do not see B2).
> Sole evaluation criterion: excellence — ground-breaking nature,
> ambition, and (Step 2 only) feasibility.

---

## 1. Motivation

### 1.1 A forty-year-old architectural decision

Every reference on today's Web is a bet that someone else will keep a
promise they never made. A URL asserts nothing about what it will
resolve to tomorrow, whether the content behind it has changed, who may
verify it, or whether the cited passage still exists at all. This is
the founding trade-off of the World Wide Web, not an accident of
implementation: its original design favored simplicity, decentralization, and
low coordination overhead, which enabled explosive adoption but
sacrificed stable references, built-in versioning, and native
bidirectional linking. The Web addresses whole resources by (mutable)
location; it has no global mechanism for persistent identities of
document *fragments*, and no coordination layer for link registration or
back-link tracking. These omissions were features: they are precisely
what let the Web grow without central coordination [BernersLee1989,
Fielding2000].

The road not taken is equally well documented. Project Xanadu
[Nelson1981, Nelson1999] insisted on the opposite guarantees: immutable
versioning (a document version, once created, never changes, so
everything that references it stays valid and verifiable), addressable
spans (specific ranges of a document are first-class referents, not just
the document as a whole), and fine-grained *transclusion*: reuse of a
precise portion of a source that carries a persistent, bidirectional
reference back to it. Together these yield stable references,
provenance, and traceable reuse, at the cost of global coordination and
infrastructure the early Web could not assume and therefore, rationally,
refused.

This proposal starts from a simple observation: **that refusal was
correct in 1991 and is increasingly incorrect in 2027 — but only in
places.** As requirements have shifted toward durability, verifiability,
and accountability, the case for Xanadu-style guarantees (persistent
citation, traceable reuse, integrity) becomes architecturally more
attractive, at the cost of the coordination overhead the Web originally
avoided. That cost remains unaffordable at planetary scale. It is,
however, now affordable, and worth paying, inside smaller,
tightly-coordinated *islands*: bounded information spaces (a legal
citation ecosystem, a supply chain, a health-data federation, a
scientific-record community) whose members share stakes high enough to
justify coordination. The research question of this project is what a
principled architecture for such islands looks like: one that borrows
the Web's proven mechanisms for growth and interoperation *between*
islands while providing Xanadu-grade guarantees *within* them. Going
beyond both Xanadu and the Web, the architecture extends those
guarantees to references whose targets must remain confidential, and
to a new class of client (autonomous agents) that neither
architecture anticipated.

### 1.2 The deferred cost has come due, and the legal system is paying it

The coordination cost the Web avoided in the 1990s was deferred, not
eliminated, and it is now being re-billed, per incident, to whoever
happens to stand downstream. Nowhere is this more visible than in law,
because law is the field where a reference's stability *is* the
substance of the claim it supports. Four developments from 2025/2026
make the case concrete:

**Link rot is now a documented failure mode of legal citation itself.**
The foundational study by Zittrain, Albert, and Lessig found that
roughly half of the URLs cited in U.S. Supreme Court opinions, and more
than 70% of URLs in the Harvard Law Review and similar journals, no
longer resolve to the material they cite [Zittrain2014]; parallel
studies document "reference rot" in about one in five scientific
articles [Klein2014]. This is not hypothetical risk but measured,
ongoing erosion of the record on which courts and scholars build
precedent. The profession's remedy, Harvard's Perma.cc archiving
service [Perma], is exactly the coordination infrastructure the Web
declined to build in 1991, now being reconstructed by hand, one citation
at a time, because the underlying architecture never gave references a
stable identity.

**The AI-hallucinated-citation crisis is link rot's more aggressive
successor: citations that were never real, and no architectural way to
check.** By early 2026, the leading tracking database had documented
over 1,200 court decisions worldwide in which AI-fabricated material
was submitted to courts (up from roughly 200 a year earlier, and
rising to ~1,490 by May 2026, more than 1,000 of them in the United
States), a substantial share submitted by licensed attorneys
[Charlotin2026]. Sanctions have escalated from a $5,000 fine in 2023 to
five-figure per-attorney penalties: in March 2026 the Sixth Circuit
sanctioned two Tennessee attorneys in *Whiting v. City of Athens* over
two dozen fake or misrepresented citations in appellate briefing
($15,000 each plus opponents' fees and double costs), and a month later
the Nebraska Supreme Court suspended an Omaha attorney after 57 of 63
citations in a single brief proved defective. Courts have responded by
imposing a non-delegable duty to verify every citation regardless of
source — that is, by regulating *behavior* because the *architecture*
offers nothing to regulate. A citation infrastructure with Xanadu-style
persistent, verifiable transclusion (where a reference either resolves
to the exact cited passage of an existing, immutable document or fails
visibly) makes this entire category of filings structurally impossible,
rather than leaving integrity to individual discipline under
professional-conduct rules.

**Content-provenance guarantees are being retrofitted at the hardware
and statutory layers because the transport layer never provided them.**
With deepfake volume growing at a reported ~900% annually (an estimated
500,000 shared in 2023, ~8 million in 2025), camera manufacturers now
sign images with hardware-rooted keys under the C2PA standard (Sony,
Nikon, and Leica ship C2PA-enabled models, with Canon rolling them out
[C2PA]); the EU AI Act's Article 50 transparency and provenance
obligations apply from August 2026 [AIAct]; and a proposed U.S. Federal
Rule of Evidence 707 would govern AI-generated evidence (public comment
closed February 2026; effective December 2027 at the earliest). Functionally, this is an attempt to bolt Xanadu's
integrity and provenance guarantees onto Web-distributed media after the
fact — in silicon and in statute, the two most expensive places to put
them.

**AI-training copyright litigation is a dispute about traceable reuse
at the scale of the whole Web.** *The New York Times v. OpenAI*
(surviving motions to dismiss since March 2025, with a November 2025
order compelling production of 20 million de-identified ChatGPT logs,
affirmed in January 2026) is one
of more than fifty active AI-copyright suits as of late 2025, and all of
them turn on the same unanswered architectural question: which sources
were actually consumed, in what form, and with what attribution trail.
That question is only this expensive to litigate because nothing in the
original act of reuse (scraping Web pages) carried a persistent,
traceable reference back to its source. Discovery is reconstructing,
after the fact and at extraordinary cost, exactly what fine-grained
transclusion would have recorded natively.

Across all four cases the pattern is identical. The Web's avoided
coordination cost has been reassigned: to archivists maintaining
Perma.cc by hand, to bar disciplinary committees, to camera makers and
legislators drafting provenance mandates, and to courts running
years-long discovery disputes. **The architectural bet of this proposal
is that paying part of that cost upfront, by design, inside bounded
islands, is decisively cheaper than continuing to pay it downstream, per
incident, through litigation and disciplinary process.**

### 1.3 Why now: the requirements have inverted and the substrate exists

Two things have changed since the trade-off was struck, and both are
necessary for this project to be timely rather than merely nostalgic.

*The non-functional requirements have inverted.* The Web now carries
legally and societally consequential information for which ephemeral,
mutable references are a liability, not a convenience; attribution,
content monetization, and copyright enforcement (exactly what
fine-grained persistent transclusion was designed to support) have
moved from fringe concerns to regulatory mandates (CSRD-style
sustainability reporting, DSA data-access obligations, AI Act
provenance duties).

*The enabling substrate Xanadu lacked now exists.* Distributed version
control (Git) provides immutable, content-addressed versions, complete
history, and replication without central control — satisfying Xanadu's
immutability requirement with commodity tooling. Content-delivery
networks remove the performance and availability objections that made
frequent transclusion impractical in the 1990s. Content-addressed
storage and intrinsic persistent identifiers are deployed at scale
(IPFS; Software Heritage's SWHIDs, recently ISO-standardized).
Decentralized identity and access-control stacks (Solid's WebID and
pods) are running in production as civic infrastructure. And practical
secure multi-party computation, the piece neither Nelson nor
Berners-Lee could have assumed, now makes it possible for a reference to
resolve to a *verifiable computation over data its holder never
discloses* (Section 1.4). None of these components is ours to invent;
the ground-breaking step is the architecture that composes them into a
coherent reference layer with explicitly chosen guarantees, and the
theory of which guarantees an island can afford at which coordination
cost.

### 1.4 Beyond Xanadu: references into data that must stay confidential

Durability guarantees (persistence, integrity, provenance) are only
half of what high-stakes islands need. The other half is a guarantee
neither the open Web nor Xanadu ever contemplated: **confidentiality of
the data behind a reference, even while the reference is shared,
resolved, and computed over.** In any island spanning more than one
organization, two requirements pull against each other: the island has
value only if members can reference and reuse each other's data
(transparency, the entire point of a transclusion layer), yet members
will not expose that data because it carries competitive or legal value
(confidentiality). On the open Web this is a hard either/or: you publish
a resource or you don't.

Our own recent work shows the trade-off dissolves inside a coordinated
island. In the PEP-LCA line of research [Grau2025, Grau2026], supply
chain members compute joint carbon footprints (one firm's directly
controlled Scope 1 emissions are "one link away" from being another
firm's Scope 3 input) via secure multi-party computation over
secret-shared values, with Solid pods as the confidentiality boundary
and share disclosure enforced at the access-control layer itself. No
participant's raw data is ever revealed, yet the derived result is
jointly computed and, with verifiable-secret-sharing and zero-knowledge
extensions, provably correct. The reference layer stops being "a pointer
to bytes you may read" and becomes "a pointer to a value you can verify
was correctly derived from bytes you may not read." This is the
confidentiality-preserving analogue of Xanadu's traceable transclusion,
and it addresses the cases the plain-persistence framing cannot:
trade-secret-laden training corpora, sealed evidence, competitive supply
data. These settings need integrity and traceable reuse *and* an
unreadable source. To our knowledge, no existing architecture treats
such verifiable-but-undisclosed references as a first-class addressing
primitive; making them one is a central scientific ambition of this
proposal.

### 1.5 A new client class forces the architectural question again

The Web's access pattern is shifting massively: from
Read→Navigate→Read to Ask→Response, with AI intermediaries
increasingly controlling the front door to the Web's content: a new
centralization vector (in RFC 9518's vocabulary: intermediation) that
neither the Web's original design nor today's re-decentralization
efforts address. And the same era adds an archival failure the 1990s
could not have foreseen: even where old AI models are preserved, the
Web they were trained on is unversioned and has since drifted, so
"what did this model actually see?" is unanswerable by construction;
a versioned, Xanadu-style substrate would answer it natively.
Both developments converge on the same architectural question: the
Web-vs-Xanadu choice (hard-coded, out-of-band knowledge versus
dynamically discovered structure) is currently being answered
*wrongly* a second time, one abstraction level up, in how LLM-based
agents are wired to services. Handing an agent a static tool catalogue (a full
OpenAPI spec, a fixed MCP tool list) repeats the CRUD-over-HTTP
hard-coding mistake: the agent cannot discover what it can do next
except from a list baked into its context, regardless of what the
current state of the world actually permits. The hypermedia answer
(HATEOAS, where the server exposes only the currently valid affordances,
annotated with machine-interpretable relations [Fielding2000,
Ciortea2019]) transfers directly: after each interaction, an
agent-facing gateway would expose only the next *valid* actions,
shaped by state and by the island's business rules. The islands
architecture we propose is therefore not only about how *documents* are
addressed but about how *capabilities* are exposed to an increasingly
important new client class, and the same loose-coupling argument
governs both. An island whose reference layer offers stable,
verifiable, span-level addressing *and* whose action layer offers
state-dependent affordance discovery is, we argue, the natural habitat
for trustworthy autonomous agents; no such environment exists
today.

### 1.6 The core idea and its stakes

We propose to design, formalize, and empirically validate the
**island**: a bounded information space that (i) provides Xanadu-grade
guarantees internally (immutable versioning, span-level addressing,
bidirectional links, traceable transclusion); (ii) extends them with
confidentiality-preserving, verifiable references built on secure
multi-party computation; (iii) exposes capabilities to human and agent
clients through state-dependent, hypermedia-style affordance discovery;
and (iv) interoperates with other islands and with the open Web through
the Web's own proven, low-coordination mechanisms. The scientific core
is a *theory of chosen guarantees*: a rigorous account of which
guarantee bundles an island can provide at which coordination cost,
under which threat model, and for which stakeholders, validated in at
least two high-stakes domains where our team has documented experience
and running systems: legal citation infrastructure and
cross-organizational supply chain data.

The risk is real: the project bets that a coordination cost two
generations of architects deemed prohibitive can be made affordable at
island scale, that cryptographic reference resolution can be made fast
enough for interactive use, and that stakeholders whose incentives
diverge (Section 2.6) will adopt shared guarantees at all. The gain is
commensurate: a validated architectural alternative for exactly those
parts of the information ecosystem (the legal record, the scientific
record, regulated industrial data) where the Web's founding trade-off
now demonstrably fails, with per-incident costs measured in sanctions,
suspended licenses, statutory retrofits, and years-long litigation.

---

## 2. Prior Work / State of the Art

### 2.1 Hypertext's two lineages and the Web's constraint set

The intellectual history is well charted: from Bush's Memex [Bush1945]
through Engelbart's NLS [Engelbart1968] to Nelson's Xanadu [Nelson1981],
hypertext research assumed rich links — typed, bidirectional, versioned,
span-anchored. Pre-Web systems (NoteCards, Intermedia, Microcosm,
HyperCard) and the open hypermedia community implemented many of these
guarantees at workgroup scale. The Web [BernersLee1989] discarded them
deliberately, and Fielding's REST [Fielding2000] later formalized the
constraint set that made planetary scale possible: statelessness,
uniform interface, hypermedia as the engine of application state.
Nelson's own retrospective argument that "xanalogical structure" is
"needed now more than ever" [Nelson1999] anticipated our motivation but
proposed no path that preserves the Web's scaling properties. The gap
this project addresses is precisely the *composition*: no prior work
provides an architecture in which Xanadu-grade guarantees hold locally
while Web-grade scaling holds globally, with a principled boundary
between the two.

### 2.2 Repairing references on the existing Web

A substantial engineering literature attacks link rot within the Web's
own model. Persistent-identifier systems (DOI, ARK, PURL) interpose a
resolvable indirection layer but depend on registrar diligence and
address whole resources, not spans. Web archiving (Internet Archive,
LOCKSS [Maniatis2005], Perma.cc [Perma]) preserves snapshots; the
Memento protocol [RFC7089] standardizes time-based access to them;
"robust links" and anchoring approaches [Klein2014, VanDeSompel] attach
archival copies and text anchors to citations. Browser-level Text
Fragments (the `#:~:text=` syntax) show mainstream demand for span
addressing, but they bind to mutable content, so anchors decay. All of
these are *remedial*: they accept the mutable, location-addressed
substrate and build compensating archives beside it. They neither
prevent drift nor provide verifiable integrity, bidirectional links, or
transclusion; and each adds exactly the kind of centralized
coordination point (a registrar, an archive) whose risks RFC 9518
catalogues (Section 2.6). We build on their lessons, particularly
Memento's versioned-access vocabulary, but relocate the guarantees
into the addressing layer itself.

### 2.3 Content addressing, versioning, and verifiable data structures

Content-addressed and versioned storage supplies the substrate Xanadu
lacked. Git's Merkle-DAG model provides immutable, hash-identified
versions with distributed replication; IPFS [Benet2014] generalizes
content addressing to a global namespace; Dat/Hypercore and similar
P2P logs add append-only verifiable histories; Software Heritage
demonstrates intrinsic identifiers (SWHIDs, ISO/IEC 18670:2025) over
the largest existing corpus of versioned source artifacts. Blockchain
systems add decentralized timestamping and ordering where needed.
W3C PROV [PROV] standardizes provenance vocabularies, and C2PA [C2PA]
binds signed provenance manifests to media assets, increasingly rooted
in capture hardware. The most complete existing composition is the
**nanopublication ecosystem** [ISWC2026]: knowledge shared as small,
immutable, signed RDF records whose Trusty-URI identifiers embed a
content hash (every reference self-verifying), served by a federated,
deployed network of registries and query services, with a
decentralized, Sybil-resistant trust-propagation algorithm (IDEBT)
whose computed trust state is itself content-addressable, and a
sustainability model in which heavy publishers must fund their own
coverage-restricted nodes. This is, in effect, a working island at the
granularity of individual semantic statements, and both its
self-verifying identifiers and its trust layer are candidate
components for our reference layer. Yet none of these systems provide
(i) span-level addressing and transclusion semantics over arbitrary
(non-RDF) content, (ii) a bidirectional link layer, (iii)
confidentiality-preserving resolution, or (iv) a theory of which
guarantee bundles an island can afford. They are storage,
attestation, and statement-publishing primitives, not general
reference architectures. We treat them as components deliberately (per
RFC 9518's advice to reuse proven decentralized mechanisms rather than
invent new coordination points).

### 2.4 Re-decentralization efforts: Solid, data spaces, federations

Solid [Sambra2016, SolidProtocol, Verborgh2024] is the most developed
attempt to carve stronger guarantees out of the existing Web: personal
or institutional pods, WebID identity, Linked Data interfaces, and
fine-grained access control, standardized through a W3C Community Group
and stewarded by the Open Data Institute since 2024, with
production civic deployments (Flanders' Athumi). Solid is an "islands"
strategy for *control and access*, not for *addressability*: it
retains location-addressed, mutable resources, so link rot, content
drift, and provenance remain out of scope. European data-space
initiatives (Gaia-X, iSHARE, sectoral spaces under the Data Act) and
exchange frameworks such as WBCSD PACT similarly relocate governance
and contracts, not reference semantics; federated social protocols
(ActivityPub) demonstrate island-to-island interoperation but with
ephemeral, unverifiable content. Our architecture is complementary and
composes with these: Solid-style pods as the trust and confidentiality
boundary, data-space governance as the institutional wrapper,
Xanadu-style addressing and versioning as the missing reference layer
within and across them. Team-adjacent empirical work sharpens this
positioning: audits of DSA Article 40(12) data access [BekavacMayer2026]
show that *mandated* openness does not by itself produce practical
accountability. Architectural guarantees and legal guarantees are
different instruments, and this project supplies the former where the
latter demonstrably underdeliver.

### 2.5 Confidential collaboration: secure computation across organizations

Secure multi-party computation has matured from theory to deployed
systems, with documented growth in large-scale applications since 2012.
Our own PEP-LCA protocol [Grau2025] demonstrates decentralized life
cycle assessment over replicated secret sharing with no trusted third
party, scaling to 50,000-participant supply chains (computing in ~150
seconds what prior approaches could only do for handfuls of
participants), and the follow-on system [Grau2026] integrates SMPC with
Solid pods and WebAssembly Component-Model plugins, enforcing the
no-single-server-sees-the-data guarantee at the access-control layer
itself and confining data-transformation code to capability-scoped
sandboxes. Related verifiable-computation work shows how participants
can prove input correctness without disclosure. What is missing, and
what this project contributes, is the elevation of these mechanisms
from bespoke application protocols to an *addressing primitive*: a
reference type whose resolution is a verifiable computation over
undisclosed sources, with explicit threat-model semantics
(honest-but-curious versus malicious-secure) chosen per island. The
open problems our own prior work honestly documents (availability
coupling across N participants, trust in input honesty, the
privacy-performance frontier) become research objectives here rather
than limitations.

### 2.6 Centralization, incentives, and why open specs are not enough

RFC 9518 [Nottingham2023] provides the standards-level frame: a
function can be nominally decentralized (open protocol, many
implementers) yet centralize in practice through economies of scale,
network effects, and switching costs (the XMPP/Google Talk and
Solid/Inrupt patterns). Its design-level mitigations (standardize what
would stay proprietary; design for switching; constrain intermediaries
structurally; reuse proven decentralization mechanisms) directly inform
our architecture, and its central lesson, that "open" and
"centralization-resistant" are different properties, motivates a
stakeholder-incentive analysis as a first-class research task: for each
actor class (hyperscaler, legacy industry, OSS/privacy community,
browser vendor, platform), does an island change the *incentive* to
centralize, not merely the license of the spec? Empirical grounding
comes from team members' published work on platform information control
[Bekavac2024, Strecker2025] and on integrity-by-design reference
mechanisms [BekavacQR2024]; from the PI's decade-long law/technology
co-design line (automatically processable regulation; the Routledge
book *AI and Law* [Guitton2025]; a computational-science
perspective on the legal system in Nature Computational Science
[TamoLarrieux2025]); and from two structural assets: the PI's seat on
the European oversight board for Very Large Online Platform auditing,
and a direct working relationship with the Open Data Institute, the
current steward of the Solid project, through the SNSF CoCoDa project
(2025–2029), connecting the incentive analysis to live protocol
governance. Funding-model precedents (email's infrastructure
piggybacking, Wikipedia's non-commercial model, public-sector Solid
hosting, data cooperatives) supply the comparative cases for which
institutional homes can sustain islands without platformization.

### 2.7 Agents as hypermedia clients

Research on Web-based multi-agent systems has long argued that agents
should inhabit hypermedia environments and discover affordances at
runtime rather than be hard-coded against APIs [Ciortea2019], and
W3C Web of Things work, which the PI's own research helped ground and
standardize, supplies machine-interpretable interaction descriptions.
The PI's group has made this concrete: signifiers as first-class
abstractions in hypermedia multi-agent systems [Vachtsevanou2023],
run-time adaptation of an agent's exposed action repertoire
[Vachtsevanou2024], and formalized contextual signifier exposure
across agent architectures (BDI, RL, Soar, LLM-based) [Lemee2024],
with the W3C Web Agents Community Group (PI: founding member) as the
standardization channel. Current LLM-agent practice runs opposite to this: static
tool catalogues (OpenAPI dumps, fixed MCP tool lists) recreate the
tight coupling REST was designed to avoid, and early evidence on
tool-count confusion ("paradox of choice" in large tool sets) shows the
practical cost. Protocol precedents for runtime discovery exist
(WebSub's `rel="hub"` advertisement is a deployed example of link-driven
dynamic binding), but no existing agent framework offers
state-dependent affordance exposure with hypermedia semantics, and none
connects capability discovery to a verifiable reference layer. The
transport-layer literature (e.g., HTTP/2's abandonment of FIFO
ordering) cautions that hybrid layerings shift correctness obligations
upward; our design treats ordering and consistency for agent-issued,
state-changing actions as an explicit architectural concern rather than
an afterthought.

### 2.8 Synthesis: the gap

Each guarantee this project needs exists somewhere: immutability and
versioning in content-addressed storage; archival persistence in the
Memento/Perma ecosystem; provenance attestation in C2PA/PROV; access
sovereignty in Solid and data spaces; confidential joint computation in
SMPC systems including our own; affordance-driven interaction in
hypermedia MAS research. **No existing system composes them into a
reference architecture; no existing theory says which bundle of
guarantees an island of a given size, stake, and threat model can
afford; and no existing infrastructure offers span-level,
version-pinned, verifiable (and, where required,
confidentiality-preserving) references as the default addressing
primitive, for human and agent clients alike.** That composition and that theory are the ground this proposal
breaks.

---

## References (draft keys — to be completed)

- [AIAct] Regulation (EU) 2024/1689 (AI Act), transparency/provenance
  obligations applicable from August 2026.
- [Bekavac2024] Bekavac, Garcia, Strecker, Mayer, Tamo-Larrieux. *From
  Walls to Windows…* CEUR-WS Vol. 3898, 2024.
- [BekavacMayer2026] Bekavac, Mayer. *Platforms' Research API Data
  Access: What Users See vs. What Researchers can Retrieve.* ACM FAccT
  2026 (doi:10.1145/3805689.3812237); preprint: *Auditing Meta and
  TikTok Research API Data Access under Article 40(12) of the DSA*,
  arXiv:2601.12390. ✓ verified 2026-07-09.
- [BekavacQR2024] Bekavac, Mayer, Strecker. *QR-Code Integrity by
  Design.* CHI EA 2024.
- [Benet2014] Benet. *IPFS — Content Addressed, Versioned, P2P File
  System.* 2014.
- [BernersLee1989] Berners-Lee. *Information Management: A Proposal.*
  CERN, 1989.
- [Bush1945] Bush. *As We May Think.* The Atlantic, 1945.
- [C2PA] Coalition for Content Provenance and Authenticity,
  specifications; hardware signing deployments 2024–2026.
- [Charlotin2026] Charlotin. *AI Hallucination Cases* database
  (damiencharlotin.com/hallucinations). ✓ verified 2026-07-09:
  ~1,227 cases by early 2026 (up from ~200 a year earlier), ~1,490 by
  May 2026, >1,000 in the US. Cases: *Whiting v. City of Athens* (6th
  Cir., March 2026: $15k/attorney + fees + double costs); Nebraska
  Supreme Court suspension of Omaha attorney Greg Lake (April 16,
  2026; 57 of 63 citations defective). Re-check counts at submission.
- [Ciortea2019] Ciortea, Mayer, Gandon, Boissier, Ricci, Zimmermann.
  *A Decade in Hindsight: The Missing Bridge Between Multi-Agent Systems
  and the World Wide Web.* AAMAS 2019.
- [Engelbart1968] Engelbart, English. *A Research Center for Augmenting
  Human Intellect.* AFIPS 1968.
- [Fielding2000] Fielding. *Architectural Styles and the Design of
  Network-based Software Architectures.* PhD thesis, UC Irvine, 2000.
- [Guitton2025] Guitton, Tamò-Larrieux, Mayer. *AI and Law: How
  Automation is Changing the Law.* Routledge, 2025.
- [Grau2025] Grau. *Towards Decentralized Privacy-Enhancing Life Cycle
  Assessment.* MSc thesis, University of St. Gallen, June 2025.
- [ISWC2026] *A Robust Decentralized Infrastructure for Trust-Aware
  Open Knowledge Sharing.* ISWC 2026 submission (paper 75; in
  `sources/`). Second-generation nanopublication ecosystem: Trusty
  URIs, IDEBT trust algorithm, federated Nanopub Registry/Query.
  **[TODO: replace with published citation once deanonymized/accepted]**
- [Grau2026] Grau, Maftun, Garcia, Mayer. *Solid and Secure Multi-Party
  Computation for a Circular Economy.* Solid Symposium 2026.
- [Klein2014] Klein, Van de Sompel, et al. *Scholarly Context Not Found:
  One in Five Articles Suffers from Reference Rot.* PLOS ONE 2014.
- [Lemee2024] Lemée, Vachtsevanou, Mayer, Ciortea. *Signifiers for
  Conveying and Exploiting Affordances: From Human-Computer
  Interaction to Multi-Agent Systems.* Annals of Mathematics and
  Artificial Intelligence 92, 2024.
- [Maniatis2005] Maniatis et al. *The LOCKSS Peer-to-Peer Digital
  Preservation System.* ACM TOCS 2005.
- [Nelson1981] Nelson. *Literary Machines.* Mindful Press, 1981.
- [Nelson1999] Nelson. *Xanalogical Structure, Needed Now More than
  Ever.* ACM Computing Surveys, 1999.
- [Nottingham2023] Nottingham. *Centralization, Decentralization, and
  Internet Standards.* RFC 9518, IETF, 2023.
- [Perma] Harvard Library Innovation Lab, Perma.cc.
- [PROV] W3C PROV family of specifications, 2013.
- [RFC7089] Van de Sompel, Nelson, Sanderson. *HTTP Framework for
  Time-Based Access to Resource States — Memento.* RFC 7089, 2013.
- [Sambra2016] Sambra, Mansour, Hawke, Zereba, Greco, Ghanem, Zagidulin,
  Aboulnaga, Berners-Lee. *Solid: A Platform for Decentralized Social
  Applications Based on Linked Data.* 2016.
- [SolidProtocol] Capadisli, Berners-Lee, et al. *Solid Protocol.* W3C
  Solid CG.
- [Strecker2025] Strecker, Bekavac, Bektaş, Mayer. *Change Your
  Perspective, Widen Your Worldview!…* arXiv:2504.10271, 2025.
- [TamoLarrieux2025] Tamò-Larrieux, Guitton, Mayer. *A Computational
  Science Perspective on the Legal System.* Nature Computational
  Science, 2025.
- [Vachtsevanou2023] Vachtsevanou, Ciortea, Mayer, Lemée. *Signifiers
  as a First-class Abstraction in Hypermedia Multi-Agent Systems.*
  AAMAS 2023.
- [Vachtsevanou2024] Vachtsevanou, de Lima, Ciortea, Hübner, Mayer,
  Lemée. *Enabling BDI Agents to Reason on a Dynamic Action Repertoire
  in Hypermedia Environments.* AAMAS 2024.
- [VanDeSompel] Van de Sompel et al., robust links / reference rot line
  of work.
- [Verborgh2024] Van Herwegen, Verborgh. *The Community Solid Server.*
  Semantic Web 15, 2024.
- [Zittrain2014] Zittrain, Albert, Lessig. *Perma: Scoping and
  Addressing the Problem of Link and Reference Rot in Legal Citations.*
  Harvard Law Review Forum / Legal Information Management, 2014.

---

## Open TODOs for this draft

1. ~~Verify all 2025/2026 factual claims~~ **Done 2026-07-09** — all
   verified and corrected in the text: Charlotin counts (~1,227 by early
   2026), Whiting sanctions ($15k each + fees + double costs), Nebraska
   suspension (Greg Lake, Apr 2026, 57/63), deepfake ~900%/yr (500k→8M),
   C2PA cameras (Sony/Nikon/Leica shipping, Canon rolling out; Samsung
   dropped as unconfirmed), NYT v. OpenAI (Nov 2025 order, affirmed Jan
   2026; 51 suits as of Oct 2025, 70+ by mid-2026), SWHID = ISO/IEC
   18670:2025, FRE 707 (comment closed Feb 2026, earliest effect Dec
   2027), AI Act Art. 50 from Aug 2026, Bekavac & Mayer =
   arXiv:2601.12390 + FAccT 2026. Re-check fast-moving counts
   (Charlotin, suit tally) once more at submission time.
2. **Decide the acronym/working title** — "ISLANDS" is a placeholder.
3. **Compress Section 1 to ≤3 pages** for the B1 extended synopsis
   (leaving ~2 pages for objectives/approach sketch); B1 must not
   cross-reference B2.
4. **Add objectives section** (this draft deliberately stops at
   motivation + state of the art; objectives/work packages are the next
   drafting step and, from 2026 rules, all feasibility material goes to
   B2 only).
5. **Stakeholder analysis** (notes §Open questions) still needs to be
   developed and woven into §2.6.
6. **Panel targeting**: likely PE6, cross-panel note in B1 should flag
   the legal/regulatory dimension (SH2?) explicitly.
