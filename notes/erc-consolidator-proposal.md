# ERC Consolidator Grant Proposal — Notes

## Core idea

A new Web that borrows the World Wide Web's architecture for scaling up,
but for smaller islands/pockets that require a different nonfunctional
trade-off, moves closer to Xanadu.

## Background: why the Web went one way and Xanadu the other

The Web's linking model won adoption precisely because it dropped the
requirements Xanadu insisted on:

- **No global mechanism for stable, persistent identities for document
  fragments.** The Web addresses whole resources by (mutable) location,
  not immutable, addressable spans. This is the root cause of link rot and
  content drift, and it is what makes reliable bidirectional linking
  infeasible at Web scale.
- **No global coordination for link registration or back-link tracking.**
  This is a feature, not a bug: it is what let the Web grow without
  central coordination.

Xanadu's transclusion model instead assumes:

- Immutable versioning — once created, a document version never changes,
  so anything that references it stays valid and verifiable over time.
- Addressable spans — specific byte ranges of a document are addressable,
  not just the document as a whole, which is what makes fine-grained
  transclusion (reuse of a precise portion of a source, with a persistent
  reference back to it) possible.

Together these give guarantees the Web cannot offer natively: stable
references, provenance, and traceable reuse, at the cost of requiring
global coordination and infrastructure the early Web could not assume.

## Motivation: why the trade-off is worth revisiting now

The WWW's original design favored simplicity, decentralization, and low
coordination overhead, which enabled explosive adoption but sacrificed
stable references, built-in versioning, and native bidirectional linking.
As requirements shifted toward durability, verifiability, and
accountability, the case for Xanadu-style guarantees (persistent
citation, traceable reuse, integrity) becomes architecturally more
attractive, at the cost of the coordination overhead the Web originally
avoided.

That shift is no longer hypothetical — it is visible, right now, as a
series of very public failures of the Web's own linking model, and the
legal system is where the failures land hardest, because law is the
field where a reference's stability *is* the substance of the claim it
supports. Four 2025/2026 developments make the case concretely:

- **Link rot has become a documented failure mode of legal citation
  itself.** More than 50% of URLs cited in U.S. Supreme Court opinions,
  and over 70% of URLs in Harvard Law Review and similar journals, no
  longer resolve to the material they cite — not a hypothetical risk but
  a measured, ongoing erosion of the record courts and scholars build
  precedent on. The profession's response, Harvard's Perma.cc archiving
  service, is exactly the coordination overhead the Web avoided in 1991,
  now being reconstructed by hand, one citation at a time, because the
  underlying architecture never gave references a stable identity to
  begin with.
- **The AI-hallucinated-citation crisis of 2025/2026 is link rot's more
  aggressive successor: citations that were never real, and no
  architectural way to check.** By early 2026, Charlotin's AI Hallucination
  Cases database had documented over 1,200 court decisions worldwide in
  which fabricated AI-generated material was submitted to courts — up from
  roughly 200 a year earlier, and rising to ~1,490 by May 2026 (more than
  1,000 of them in the US) — a substantial share submitted by licensed
  attorneys. Sanctions have escalated sharply — from a $5,000 fine in 2023
  to five-figure per-attorney penalties — and in March 2026 the Sixth
  Circuit sanctioned two Tennessee attorneys in *Whiting v. City of
  Athens* over two dozen fake or misrepresented citations in appellate
  briefing ($15,000 each in punitive sanctions plus opponents' fees and
  double costs, the stiffest penalty available under Rule 38); a month
  later, the Nebraska Supreme Court suspended an Omaha attorney after 57
  of 63 citations in a single brief turned out to be defective. Courts
  have held attorneys to a non-delegable duty to verify every citation
  regardless of source. A citation architecture with Xanadu-style persistent,
  verifiable transclusion — where a reference either resolves to the
  exact cited passage of an existing, immutable document or fails
  visibly — makes an entire category of these filings structurally
  impossible, rather than relying on individual verification discipline
  under professional-conduct rules.
- **Content-provenance standards are being bolted onto hardware and law
  because the Web has no native integrity guarantee.** With deepfake
  volume growing at a reported ~900% annually (an estimated 500,000
  shared in 2023, ~8 million in 2025), camera makers now sign images
  with hardware-rooted keys under the C2PA standard (Sony, Nikon, and
  Leica ship C2PA-enabled models; Canon is rolling them out), and the EU
  AI Act's Article 50 transparency/provenance obligations apply from
  August 2026 alongside a proposed U.S. federal rule of evidence
  (FRE 707) governing AI-generated evidence (public comment closed
  February 2026; effective December 2027 at the earliest). This is,
  functionally, an attempt to retrofit Xanadu's integrity and provenance
  guarantees onto Web-distributed media after the fact, at the hardware
  and statutory layers, precisely because the transport layer never
  provided them.
- **Copyright and AI-training litigation is a dispute about traceable
  reuse at civilizational scale.** *The New York Times v. OpenAI* (surviving
  motions to dismiss since March 2025, with a November 2025 order
  compelling production of 20 million de-identified ChatGPT logs) is one
  of over fifty active AI-copyright suits as of late 2025, and all of them
  turn on the same unanswered architectural question: which sources were
  actually consumed, in what form, and with what attribution trail. That
  question is only this expensive to litigate because nothing in the
  original reuse — scraping Web pages — carried a persistent, traceable
  reference back to its source; discovery is reconstructing after the
  fact what fine-grained transclusion would have recorded natively.

Across all four cases, the pattern is the same: the coordination cost the
Web avoided in the 1990s has not disappeared, it has been deferred and
re-billed — to archivists maintaining Perma.cc by hand, to bar
disciplinary committees, to hardware manufacturers and legislators
drafting provenance mandates, and to courts running years-long discovery
disputes. A system that designs stable references, integrity, and
traceable reuse in from the start, even only within smaller
tightly-coordinated "islands," is a bet that paying some of that cost
architecturally, upfront, is cheaper than continuing to pay it downstream,
per incident, through litigation and disciplinary process.

Non-functional requirements for global information systems have shifted
substantially since the early 1990s:

- **Persistence, integrity, accountability.** The Web now carries legally
  and societally consequential information; ephemeral, mutable references
  are increasingly a liability rather than a convenience.
- **Intellectual property and micropayments.** There is now much stronger
  emphasis on content monetization, attribution, and copyright
  enforcement — exactly what fine-grained, persistent transclusion was
  designed to support.
- **Scalability and performance at planetary scale**, which the original
  Web architecture was optimized for and Xanadu-style designs were not.

The Web's original priorities — simplicity, decentralization, low
coordination overhead, ease of implementation — enabled explosive
adoption but sacrificed stable references, built-in versioning, and
native bidirectional linking. A system targeting today's requirements can
reasonably shift back toward the Xanadu side of that trade-off, at least
for the smaller, more tightly-coordinated "islands" where the coordination
cost is affordable.

## Why now: enabling technology that didn't exist in the 1990s

This is possible today because several key technologies exist that were
not available in the 1980s/1990s:

- **Distributed version control.** Systems like Git natively provide
  immutable, content-addressed commits, full version history, and
  distributed replication — directly satisfying Xanadu's requirement for
  immutable versioning and content-addressable integrity, without
  centralized control.
- **Content distribution networks.** Fine-grained transclusion requires
  that referenced spans stay reliably and efficiently retrievable
  worldwide. Modern CDNs provide global caching, low-latency delivery, and
  automatic replication, which removes most of the performance/
  availability objections that made frequent transclusion impractical in
  the 1990s.
- Other candidates to evaluate: decentralized identity systems (for
  stable, portable identities behind addressable references) and
  content-addressed storage more broadly. **Solid** (below) is a concrete,
  already-deployed example of this category, worth treating as a case
  study rather than just a candidate technology.

## The hybrid system: agents as a new hypermedia client class

The Web-vs-Xanadu hard-coding argument above (stable, addressable
references vs. mutable, location-based pointers) turns out to have a
direct, present-day analogue in how LLM agents are wired up to APIs — and
it points at the concrete "hybrid" architecture worth prototyping for
this proposal: not just a hybrid of Web- and Xanadu-style addressing, but
a hybrid where the agent-facing layer inherits HATEOAS's dynamic-
discovery property instead of repeating the CRUD-over-HTTP hard-coding
mistake one level up.

- **The same hard-coding problem, one abstraction level up.** A CRUD-over-
  HTTP client is hard-coded against fixed URIs, methods, and a bespoke
  JSON schema; a semantic hypermedia client instead follows links/
  affordances that a server exposes dynamically, conditioned on current
  state (HATEOAS), interpreted via link relations and a shared media
  type. Handing an LLM agent a full OpenAPI spec (or a static MCP tool
  list) as one large, out-of-band catalogue is structurally the same
  hard-coding move: the agent has no way to discover what it can do next
  except from a static list baked into its context, regardless of
  whether the underlying business state actually permits that action.
- **What a HATEOAS-style MCP layer would change.** Instead of a fixed
  tool catalogue, tool/resource availability would be state-dependent and
  discovered at runtime — after invoking one tool, the response would
  expose only the next *valid* actions, annotated with link-relation-like
  semantics (why this tool is relevant now) and interpreted through a
  shared, media-type-like schema for tool descriptions. This gives agents
  the same decoupling and evolvability benefits hypermedia APIs give human
  -facing clients, instead of requiring a new static tool list every time
  the underlying API changes.
- **Recommended shape: hybrid, not replacement.** Keep the existing
  OpenAPI surface for human developers and conventional tooling, and add
  a curated, dynamically-discoverable MCP gateway on top for agents — the
  gateway both reduces the "paradox of choice" a flat 80+-endpoint spec
  creates for an LLM and lets the server shape/restrict what an agent can
  do based on state, mirroring how a hypermedia API's affordances encode
  business rules (e.g., a "cancel" link only appears while cancellation is
  still free) instead of requiring the client to re-implement the rule.
- **WebSub as an existing precedent for this kind of runtime discovery.**
  WebSub's subscriber/publisher/hub model already demonstrates the
  pattern at the protocol level: a subscriber discovers a publisher's hub
  dynamically via an advertised `rel="hub"` link rather than a
  pre-configured endpoint, then the hub handles verification and fan-out.
  It is a working example of loosely-coupled, link-driven eventing that
  the agent-facing MCP layer above would need to generalize from simple
  content updates to arbitrary state-dependent tool discovery.
- **A caution from the transport layer.** The gRPC/HTTP-2 ordering
  discussion is a reminder that "hybrid" is not automatically better:
  HTTP/2's multiplexing drops HTTP/1.1's FIFO guarantee to avoid head-of-
  line blocking, but this shifts responsibility for correct ordering
  (where it matters, e.g., dependent state-changing calls) to the
  application layer. A HATEOAS-style MCP layer buys discoverability and
  evolvability, but it does not remove the need to design explicitly for
  ordering/consistency in whatever transport carries agent-tool calls.

Framed this way, the "islands" architecture this proposal targets is not
only about how *documents* are addressed (Xanadu-style spans vs. Web
URLs), but about how *capabilities* are exposed to an increasingly
important new class of client — autonomous agents — and the same
loose-coupling argument applies to both.

## Solid as a relevant precedent

[Solid](https://solidproject.org) (Social Linked Data) is Tim
Berners-Lee's decentralization project, standardized through a W3C
Community Group and now stewarded by the Open Data Institute (since
October 2024, after MIT and then Inrupt-led development). It is directly
relevant to the proposal's "islands" framing: Solid is essentially an
attempt to carve out smaller, coordinated pockets of the Web — personal
or institutional **pods** — where stronger guarantees (user-controlled
storage, fine-grained access control, portable identity) are enforced,
without requiring the whole Web to adopt them.

Architecture, in brief:

- **Pods** — personal online data stores; a user/institution can run
  many, for different data domains (profile, financial, health, etc.),
  hosted wherever they choose.
- **WebID** — a URI-based, portable, decentralized identity, used for
  authentication independent of any single platform.
- **Linked Data (RDF)** — data within pods is addressed and structured
  as Linked Data, giving apps a common, interoperable data model instead
  of bespoke per-app schemas/APIs.
- **Access control** — apps request access to specific data with
  explicit, revocable user permission; the mechanism for expressing
  those permissions is itself contested (WAC vs. ACP, see below).

This is a useful comparison point for the Xanadu/Web trade-off above:
Solid keeps the Web's location-addressed, mutable-resource model rather
than adopting Xanadu-style immutable, span-addressable versioning — its
"island" strategy is about relocating *control and access*, not about
solving link rot or persistent addressability. A Xanadu-leaning system
and a Solid-style system are attacking different parts of the same
underlying problem (Web-scale coordination assumed too little structure
for high-stakes use) and could plausibly be complementary: Solid-style
pods as the trust/control boundary, Xanadu-style addressing/versioning
as the reference layer within or across pods.

## The cybersecurity angle: confidentiality-preserving islands

The sections above frame the islands mostly around *durability* guarantees
— persistence, integrity, provenance, traceable reuse. There is a second,
orthogonal guarantee an island can offer that the open Web structurally
cannot: **confidentiality of the data behind a reference, even while the
reference is shared and computed over.** This turns out to be the property
that decides whether high-stakes actors will actually put data into a
tightly-coordinated island at all, and two pieces of our own group's work
show it is buildable today, not just desirable.

**The confidentiality–transparency conundrum.** In any island that spans
more than one organization, two requirements pull against each other: the
island only has value if members can *reference and reuse* each other's
data (transparency, traceable reuse — the whole point of the Xanadu-style
reference layer), but members will not *expose* that data because it
carries competitive value (confidentiality). On the open Web this is a
hard either/or — you publish a resource or you don't. The interesting
claim is that inside a coordinated island the trade-off dissolves: modern
cryptography lets a reference resolve to a *verifiable computation over*
data that its holder never discloses. The reference layer stops being
"pointer to bytes you can read" and becomes "pointer to a value you can
verify was correctly derived from bytes you are not allowed to read."

**A concrete, already-built instance (Grau, MSc thesis, 2025; Grau,
Maftun, Garcia & Mayer, Solid Symposium 2026).** The group's PEP-LCA work
implements exactly this for cross-supply-chain Life Cycle Assessment — a
high-stakes setting where every firm's emissions data is both legally
demanded (Scope 3 reporting) and commercially sensitive (it leaks
production volumes, supplier relationships, margins). The design is a
clean template for the islands architecture:

- **Solid pods as the confidentiality boundary.** Each organization keeps
  its data in its own pod as the single source of truth and never ships
  raw values; this is the same "pod as trust/control boundary" point from
  the Solid section above, made cryptographically load-bearing rather than
  just access-controlled.
- **Secure Multi-Party Computation (SMPC) as the reference-resolution
  mechanism.** Using replicated / Shamir secret sharing under a
  (2,3)-threshold scheme, computation servers jointly evaluate the LCA
  result over secret-shared inputs; no single server ever reconstructs any
  participant's data. One firm's directly-controlled (Scope 1) emissions
  become "just a link away" from being the input to another firm's
  footprint — traceable reuse without disclosure. Notably it scales:
  the thesis reports calculations over ~20,000 participants in the time
  prior methods needed for ~15, and runs to 50,000-participant networks.
- **Security enforced at the data-access layer, not only in the compute
  protocol.** Because share *generation* happens inside the pod and
  Solid's access control then discloses each share to a different
  computation server (Server A sees only Share 1, etc.), the core SMPC
  guarantee is anchored at the reference/access layer itself — precisely
  the layer this proposal is redesigning.
- **WASM-sandboxed transformation plugins** (WebAssembly Component Model)
  let each pod expose data through a narrow, host-controlled `fetch`
  interface: a plugin can transform and retrieve *authorized* resources
  and nothing more. This is the same capability-confinement idea as the
  agent/HATEOAS-MCP section above — the host shapes and bounds what a
  visiting piece of code can reach — now applied to code that runs against
  the confidential reference layer.

**Integrity without disclosure ties back to the legal motivation.** The
thesis is explicit that its current honest-but-curious, (2,3)-threshold
model is a floor, not a ceiling: extending to malicious adversaries via
**verifiable secret sharing** and **zero-knowledge proofs** would let a
participant *prove a referenced value was correctly derived* without
revealing the source data. That is the confidentiality-preserving analogue
of Xanadu's traceable transclusion, and it closes a gap the Motivation
section left open — the C2PA / AI-provenance / AI-training-litigation
cases all want integrity and traceable reuse, but several of them
(trade-secret-laden training corpora, sealed evidence, competitive supply
data) *also* require that the source not be openly readable. An island
whose reference layer offers "verifiable but not disclosed" serves the
high-stakes cases the plain-persistence framing cannot.

**This sharpens the stakeholder analysis rather than sidestepping it.**
The choice of threat model is itself a stakeholder question: honest-but-
curious is adequate for a cooperative consortium but not for mutually
distrustful competitors or a regulator-facing deployment, where malicious-
secure protocols (with their added cost) become necessary. The proposal
should state, per island and per actor, which adversary model it assumes —
the security guarantee, like the coordination cost, is something an island
chooses deliberately rather than inherits. Two further limitations from
the thesis are worth carrying forward honestly: strong availability
coupling (the protocol currently needs all N participants live, a real
operational fragility at island scale) and the residual trust that inputs
are *honest* (addressed only partially, via verifiable-computation
extensions) — both are open problems the islands design inherits, not
ones it has solved.

## Scaling Solid without hyperfinancialization

A concrete risk case study for the proposal's stakeholder-incentive
analysis (see stakeholder list above): what happens to an open protocol
when it needs to scale, and who captures the value.

**The core risk.** Not any single company acting in bad faith, but the
generic *platform trap*: an open protocol where one commercial actor
(here, Inrupt, Berners-Lee's own startup) accumulates enough network
effects, enterprise contracts, and tooling dominance that the "open"
spec becomes nominal while real control stays private. Precedents: XMPP
died as a consumer protocol once Google Talk absorbed and then abandoned
it; LinkedIn captures "professional identity" while nominally being just
one website among many that could implement an open protocol.

**What stayed open, and why.** Email (SMTP/IMAP) is the canonical
counter-example: it scaled globally, nobody got hyperrich from the
protocol itself, and it stayed federated — because it piggybacked on
organizational server infrastructure (ISPs, employers) that already
existed for other reasons, not on a VC growth story. ActivityPub/Mastodon
shows the same pattern more recently: imperfect, but federated social
infrastructure can exist without financialization if hosting economics
stay manageable. Wikipedia is a related but distinct case: it stayed open
by never adopting an ad-funded, engagement-maximizing business model in
the first place — non-commercial, ad-free, funded by donations rather
than advertising, so its content isn't shaped by the same
click-optimizing incentives as most of what people see online. It's a
useful limit case for the stakeholder analysis below: an information
commons that avoided the platform trap through funding model rather than
through protocol architecture. Solid's **"last mile" problem** is that it
lacks email's free ride — most people don't run their own mail servers,
but Solid pods still need someone with an independent reason to host
them.

Six mechanisms for keeping Solid on the open-protocol path, relevant to
where this proposal's "islands" could plausibly sit institutionally:

1. **Public sector as the primary scaling engine.** The Solid Advisory
   Committee has voted to prioritize Health, Public Administration, and
   Education — sectors where municipalities, national health services,
   and universities can run pod infrastructure as a public utility, the
   way they run libraries or sewage systems. Belgium's **Athumi**
   (formerly Digipolis Vlaanderen) already runs Solid as civic
   infrastructure at regional (Flanders) scale — state as host, citizen
   as owner. The EU regulatory context (GDPR, the Data Act, data-spaces
   initiatives like Gaia-X and iSHARE) pulls in the same direction.
2. **Data cooperatives for consumer hosting.** MIDATA (Switzerland) and
   similar cooperatives offer pod-like hosting under member governance:
   users are members, not customers, and surplus returns to members, not
   shareholders. The MyData movement's certified-operator model
   (Viivi Lähteenoja) — operators accountable to users rather than
   investors — could be formalized as a Solid pod-operator standard.
3. **Keep the Community Solid Server (CSS) healthy.** Ruben Verborgh's
   team at imec/KU Leuven built the CSS as a genuinely open, modular
   reference implementation — strategically important because it stops
   Inrupt's Enterprise Solid Server from becoming the de facto standard
   through tooling lock-in even while the spec stays open. The Advisory
   Committee's choice not to invest €3M in an enterprise server, opting
   for free licenses instead, kept the ecosystem from consolidating
   around one commercial implementation.
4. **Resist ACP winning by default.** The WAC (Web Access Control) vs.
   ACP (Access Control Policy) dispute has a rarely-stated
   financialization dimension: ACP is more expressive and
   enterprise-friendly, which favors Inrupt's commercial products (more
   complex access control → more need for sophisticated tooling → more
   need for Inrupt). WAC is simpler, more accessible to community
   implementations, and less of a moat. Resolving this in favor of
   genuine interoperability, rather than whichever system Inrupt
   implements best, matters for keeping the ecosystem open.
5. **Grant funding for core infrastructure, not just research.** NLnet
   Foundation, EU Horizon, national research councils, and civic-tech
   funders already support Solid-adjacent work, but grants fund research
   and rarely fund the unglamorous ongoing maintenance of shared
   infrastructure (the solidcommunity.net problem). Dedicated
   infrastructure grants, modeled on how the Linux Foundation or Apache
   Software Foundation operate, would reduce reliance on Inrupt to fill
   that gap by default.
6. **Separate the stack: commons vs. services.** The protocol, pod
   server software, and core specs are commons and should be publicly
   funded and governed; value-added services (apps, analytics,
   enterprise integrations, convenience features) can be commercial. The
   problem occurs when one commercial actor controls both layers. The
   ODI stewardship transition is an attempt to structurally separate
   them and needs to be defended and deepened.

**The hard truth.** The public-sector route (governments serving
citizens, universities serving students, health systems serving
patients) is the most promising non-financialized scaling path for
Solid, but it requires demonstrating value to procurement officers, not
just developers — a different kind of work than the community has
historically done, and likely where the tension between grassroots
contributors and institutional actors (ODI, Inrupt) is currently most
acute. For this proposal, it also sharpens the stakeholder-analysis
question above: a Xanadu-like "islands" architecture faces the identical
choice between public-institutional hosting and commercial
platformization, and should state upfront which path it assumes.

## RFC 9518: a framework for the centralization risk

Mark Nottingham, *Centralization, Decentralization, and Internet
Standards*, RFC 9518 (IETF, September 2023),
<https://datatracker.ietf.org/doc/rfc9518/>.
Directly relevant to the "platform trap" discussion above and to the
stakeholder analysis below: it is the standards-track articulation of
the same problem — what a protocol's technical design can and cannot
do to keep power distributed once the protocol succeeds.

Its core move is to define the terms precisely rather than treat
"decentralized" as a self-evident virtue:

- **Centralization** is "the state in which a single entity or a small
  group of entities can observe, capture, control, or extract rent
  from the operation or use of an Internet function exclusively."
- **Decentralization** is necessary but not sufficient to prevent this
  — a function can be nominally decentralized (open protocol, many
  implementers) while still centralizing in practice through market
  dynamics. This is exactly the Solid/Inrupt and XMPP/Google Talk
  pattern described above: an open spec did not stop the practical
  capture.

RFC 9518 attributes centralization mostly to forces standards cannot
reach directly — economies of scale, network effects, switching costs,
and the purely voluntary nature of standards adoption — which means a
Xanadu-leaning "islands" design faces the same limits Solid does: the
protocol can make centralization *harder*, not prevent it. Where it
gives more direct traction is its list of design-level mitigations,
which map onto this proposal's own six mechanisms above:

- Standardizing functions that would otherwise stay proprietary (→
  parallels keeping the Community Solid Server, mechanism 3, healthy
  as a genuinely open reference implementation).
- Designing explicitly for switching between providers/implementations
  (→ parallels resisting ACP winning by default, mechanism 4, since a
  simpler access-control model is also a lower switching-cost one).
- Constraining intermediary power through protocol design and
  layer boundaries, rather than assuming goodwill (→ parallels
  separating commons from services, mechanism 6).
- Reusing proven decentralization mechanisms instead of inventing new
  coordination points (→ an argument for building the "islands" idea
  on Git/CDN primitives, as in the "why now" section above, rather
  than a bespoke registry).

For the proposal, RFC 9518 is useful less as a source of new mitigations
and more as an independent, standards-body-level confirmation that
"open protocol" and "resistant to centralization" are different
properties — reinforcing that the stakeholder analysis below needs to
ask, for each actor, whether the islands architecture changes their
*incentive* to centralize, not just whether the spec is open.

## Nanopublications: a deployed precedent for statement-level islands

Source: `sources/ISWC_2026_paper_75.pdf` — *A Robust Decentralized
Infrastructure for Trust-Aware Open Knowledge Sharing* (anonymized ISWC
2026 submission; the Knowledge Pixels / nanopublications line of work).

The paper presents a second-generation nanopublication ecosystem:
knowledge shared as small, **immutable, uniquely identified,
cryptographically signed RDF records** (nanopublications) whose
identifiers are **Trusty URIs** — content-derived hashes embedded in the
URI so every reference and retrieval is self-verifying. Architecture:
federated **Nanopub Registries** (ingest/validate/replicate, sharded by
signing key and by declared type) and **Nanopub Query** services
(SPARQL/REST over materialized per-agent and per-type repositories),
with clients like Nanodash on top. Evaluation: type-sharded replication
roughly doubles cluster ingestion capacity and halves query latency vs.
full replication (~6,900 queries/s at ~2.3 ms across a corpus growing to
400k nanopubs / ~13M triples); a live deployed network exists.

Two contributions matter most for this proposal:

- **IDEBT trust algorithm** — seed-rooted, decay-bounded, deterministic
  trust propagation over signed, *retractable* identity-to-key bindings
  and endorsements (themselves nanopublications). Sybil-resistant by
  ratio conservation; the resulting trust state is itself a
  content-addressable artifact any peer can mirror and re-verify. This
  fills a dimension the islands architecture had not yet named: **trust
  and reputation *within and between* islands, computed without a
  central operator** — a "chosen guarantee" alongside persistence,
  integrity, and confidentiality.
- **A sustainability model that answers RFC 9518 economically**: open
  Registries serve the long tail under IDEBT-bounded quotas; heavy
  institutional/commercial publishers must run or commission their own
  coverage-restricted nodes, paying for their own capacity. Same
  codebase serves open community nodes and self-funded private nodes —
  a concrete mechanism for the "commons vs. services" separation
  (mechanism 6 above) and a direct input to the funding-model analysis.

Positioning for the proposal: nanopublications are a *working,
deployed* island-like infrastructure at the granularity of individual
semantic statements — immutability, content addressing, per-statement
provenance, decentralized trust. What they do not provide is exactly
what the islands architecture adds: span-level addressing over
arbitrary (non-RDF) content, transclusion semantics, confidentiality-
preserving resolution (SMPC), agent-facing affordance discovery, and
the guarantee-vs-coordination-cost theory. Treat the ecosystem as a
candidate substrate/component for the reference layer (WP2) and the
trust layer, and cite it in prior work; the Trusty URI mechanism is the
statement-level analogue of the span-level identifiers the proposal
needs.

## Further motivation facets (from sources/Idea.txt)

- **AI as full intermediary — "controlling the front door."** The Web's
  access pattern is shifting massively: from Read→Navigate→Read to
  Ask→Response. AI companies increasingly control the front door to the
  Web's content. This is a *new centralization vector* (RFC 9518's
  vocabulary: intermediation) that neither the Web's original threat
  model nor Solid's addresses — and it strengthens the agent-layer
  argument: if agents are becoming the dominant client class, then the
  architecture that exposes content and capabilities to them decides
  who holds the front door. Islands with native agent affordances are a
  counterweight: the island, not the intermediary, shapes what agents
  can see and do.
- **The archival/context problem of the AI era.** Even if old models
  are archived, their *training context* is not: the Web they consumed
  is unversioned and has since drifted. A Xanadu-style versioned Web
  would have made "what did the model see?" answerable by
  construction. This is a fifth motivation case (alongside the four
  legal ones): reproducibility and auditability of AI systems require
  versioned reference infrastructure that did not matter in 1990.
- **From user-centric to societally-centric Web (UCD → SCD).** The PI's
  research-statement argument that user-centered design misses negative
  societal externalities scales up to Web architecture: the islands
  proposal is architecture-level SCD — explicitly bounded information
  spaces with *chosen*, disclosed guarantees rather than
  platform-optimized defaults.
- **Facets to keep visible** in the proposal narrative: (i)
  architecture, (ii) cybersecurity & transclusion, (iii) geopolitical
  ramifications (EU↔US: who operates reference infrastructure is a
  sovereignty question — connects to Gaia-X/data-spaces context and to
  the EU-regulatory motivation).
- **Foundations to draw on**: Web architecture; economics/network
  effects; psychology of deferral (the Web's cost-deferral pattern as a
  behavioral, not just technical, phenomenon); VLOP empirics (Bekavac);
  Habermas' *New Structural Transformation of the Public Sphere*
  (platform-mediated publics) as the social-theory frame for what an
  "island" is.
- **Practice signal for the agent layer**: Eclipse LMOS builds on W3C
  WoT Thing Descriptions — industrial uptake of the exact
  affordance-description substrate WP4 extends. Interoperability theory
  thread (Terry Payne, HyperAgents 2025): alignment aggregation /
  repair / negotiation.
- **Pointer**: "Hypernext" SSRN paper
  (https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5735624) — to
  read; possibly related work on Web successor architectures.
- Note: Idea.txt also sketches a *different* project idea (global
  interoperability: AI–AI, AI–human, animal–animal, with
  neuroscience/psychology integration). Out of scope for this proposal
  except where it already overlaps (cognitive interoperability →
  signifier exposure across agent architectures, WP4); keep as a
  separate candidate idea.

## Open questions / stakeholder analysis (to develop further)

Whether a Xanadu-like system helps or hurts depends heavily on which
actor's perspective is taken — worth working through explicitly for the
proposal's motivation section, e.g.:

- Hyperscaler
- Legacy industry company
- OSS / privacy activist
- Browser manufacturer
- Social media platform

Each has different incentives around coordination cost, control over
identity/addressing, and monetization of persistent references; the
proposal should articulate which of these the "islands" are meant to
serve, and why the trade-off favors them specifically.

## Team: how it fits together

**PI (Mayer)** — the EPFL application package (in `sources/`) documents
the two lines the proposal converges: (1) the machine-usable-Web line —
PhD at ETH (2014) on interacting with the Web of Things, contributions
underlying the W3C WoT Thing Description standards (deployed in
industrial products, e.g., Siemens Desigo), hypermedia multi-agent
systems (AAMAS 2019), signifiers as first-class abstractions and
run-time action-repertoire adaptation (AAMAS 2023/2024), founding
member of the W3C Web Agents CG; (2) the law/technology co-design
line — automatically processable regulation (AI & Law journal,
2022–2025), the Routledge book *AI and Law* (2025), *Nature
Computational Science* (2025), member of the European VLOP-auditing
oversight board (only computer scientist), board member of UniSG's
Research Center for Information Law. Running projects that dock onto
the proposal: Innosuisse Flagship WISER (2022–2026; LCA/climate —
supply-chain island), SNSF CoCoDa (2025–2029; VLOP regulation with
Lausanne, Maastricht, and the ODI — which is also Solid's steward),
SNSF/Innosuisse Access to Justice (2026–2030, with Caritas). Dean of
UniSG CS until Feb 2026, stepping down to refocus on research —
supports the ERC ≥40% commitment. Note: EPFL faculty application
pending (Oct 2025) — host-institution decision affects the proposal.

**Luka Bekavac** is a team member, and his existing publication record
with Mayer supplies the empirical/regulatory counterpart to the
architectural argument above — evidence for how platform control over
information actually manifests, rather than treating it as a purely
theoretical concern:

- Bekavac, Garcia, Strecker, Mayer, Tamo-Larrieux, *From Walls to
  Windows: Creating Transparency to Understand Filter Bubbles in Social
  Media* (CEUR-WS Vol. 3898, Oct 2024) — measures how platform
  algorithms narrow the information people are exposed to. Direct
  empirical grounding for the "social media platform" and "hyperscaler"
  stakeholder cases above.
- Bekavac, Mayer, *Auditing Meta and TikTok Research API Data Access
  under Article 40(12) of the Digital Services Act* (arXiv:2601.12390,
  Jan 2026; peer-reviewed version: *Platforms' Research API Data Access:
  What Users See vs. What Researchers can Retrieve*, ACM FAccT 2026) —
  tests whether regulator-mandated data-access APIs actually
  let researchers audit platform behavior. Findings: researchers can
  retrieve only ~75% of TikTok For-You posts and ~50% of Instagram
  Explore posts, with only 17%/42% of metadata parameters surviving. The DSA-era, empirical
  version of the RFC 9518 argument above: a legal requirement for
  openness does not by itself prevent practical centralization of
  control.
- Strecker, Bekavac, Bektaş, Mayer, *Change Your Perspective, Widen Your
  Worldview! Societally Beneficial Perceptual Filter Bubbles in
  Personalized Reality* (arXiv:2504.10271, Apr 2025) — proposes
  deliberately engineered, disclosed filter bubbles, which resonates
  with this proposal's "islands" framing: a smaller, explicitly bounded
  information space with known trade-offs, chosen rather than imposed.
- Bekavac, Mayer, Strecker, *QR-Code Integrity by Design* (CHI EA 2024)
  — integrity/provenance guarantees for a physical-to-digital reference
  mechanism; a narrow but concrete precedent for the kind of
  addressable, tamper-evident referencing this proposal wants at Web
  scale.

**Jan Grau** supplies the cryptographic-systems half — a working prototype
of the confidentiality-preserving reference layer described above, not
just a design. His MSc thesis and the follow-on Solid Symposium paper are
the direct evidence that "verifiable but not disclosed" islands are
buildable:

- Grau, *Towards Decentralized Privacy-Enhancing Life Cycle Assessment*
  (MSc thesis, University of St. Gallen, June 2025; supervised by Mayer &
  Garcia, with Katerina Mitrokotsa and Nan Cheng on the cryptography) —
  the PEP-LCA protocol: decentralized SMPC over replicated secret sharing,
  a two-layer participation/computation architecture with no trusted third
  party, scaling to 50,000-participant supply chains. The concrete
  instance of an island whose reference layer resolves to verifiable
  computation over undisclosed data.
- Grau, Maftun, Garcia, Mayer, *Solid and Secure Multi-Party Computation
  for a Circular Economy* (Solid Symposium 2026) — the same idea wired to
  Solid pods and WASM Component-Model plugins, with per-server share
  disclosure enforced at Solid's access-control layer. Demonstrates the
  pod-as-cryptographic-boundary and capability-confined-plugin patterns
  the cybersecurity section builds on.

The presence of Mitrokotsa (cryptography/security) and Cheng (SMPC) on
this line of work is also what makes the malicious-adversary, verifiable-
secret-sharing, and zero-knowledge extensions flagged above credible as
proposal deliverables rather than aspirations.

Team fit: Bekavac's line of work supplies the empirical/regulatory half
of the argument (how platform control over information actually plays
out, and where mandated openness does or doesn't fix it); Grau's supplies
the cryptographic-systems half (a built, benchmarked confidentiality-
preserving reference layer); and the Xanadu/Solid/RFC 9518 material above
supplies the architectural half (what a system could look like if it
didn't have to route around those incentives). The stakeholder analysis
above should draw on this existing empirical and prototype work rather
than treating platform incentives — or the confidentiality guarantees the
islands can offer — as purely theoretical.

## ERC application intelligence (from sources: SwissNCP webinar 13.10.2025, Indiveri euresearch talk, Idea.txt)

Source inventory: `20251013_ERC Webinar_SwissNCP.pdf` (official CoG
info session, Marilena Plesu, ERC), `Giacomo Indiveri_euresearch25.pdf`
(NeuroAgents CoG-winner retrospective), `Idea.txt` (Mayer's distilled
notes from both + own idea fragments), `The-Solid-Problem.txt` (source
of the "Scaling Solid without hyperfinancialization" section above).

**Administrative facts to build on:**

- **PhD defense date counts: September 12, 2014. Eligibility
  confirmed:** the CoG 2027 window is PhD **5–15 years before
  1.1.2027** (widened from the pre-2027 7–12-year rule) → 12.3 years →
  eligible, no extensions needed.
- PI time commitment ≥40% (CoG); ≥50% of PI working time in EU/AC.
- Parts: A (admin, budget) · B1 = Part I of Scientific Proposal
  (5 pages: idea, objectives, approach/strategy) + CV & Track Record
  (≤4 pages, one structured document, up to 10 outputs + peer
  recognition + context for unusual paths) · **B2 = Part II (7 pages):
  implementation & methodology incl. feasibility, risk assessment,
  mitigation** + Funding ID. Plus host support letter and PhD
  certificate (+ defense-date evidence if needed).
- Host institution is **not an evaluation criterion**, and ERC grants
  are **portable** anywhere in Europe → the pending EPFL question does
  not affect evaluation; negotiate conditions with whichever host.
- Team members outside EU/AC fundable if well justified. Additional
  funding up to €1M (equipment/facilities) available; likely not
  needed.
- Projects shorter than 5 years are welcome (we still plan 60 months).
- Step 2 includes an **interview**: one-page summary slide required;
  prepare speech + answers (Indiveri: euresearch prep event crucial;
  panic is normal).
- Resubmissions have ~1.5× higher success rates; panel feedback is
  useful — failing once is part of the process.

**Writing advice (both talks converge):**

- Primary: **focus on the ambition of the idea**; secondary: show you
  can do it. "Impress non-experts in B1, convince peers and experts in
  B2."
- Step 1 asks: Is this a great idea worth pursuing? Outline current
  state of knowledge; is the idea advancing it; original, creative,
  ambitious? Clear scientific question and objectives; overall
  approach/strategy. **Be concise and clear for generalists.**
- Step 2 asks: can it be implemented realistically, as proposed?
  Complementary to Part I, not redundant.
- Follow ERC document instructions **to the letter**; mirror the Work
  Programme's own language/keywords ("this is *transformative*
  because…", "the *innovation potential* is high because…"); read the
  evaluation questions in the WP and answer them.
- **No unnecessary partners; do not build a consortium** — our
  external collaborators (Tamò-Larrieux, Mitrokotsa/Cheng, Empa,
  Siemens, ODI) stay collaborators, not beneficiaries.
- Study the panel: learn panel members' research areas; choose the
  panel deliberately (primary clearly CS/PE6; secondary panel
  possible).
- Look at funded projects in the field (ERC website search tool).
- Indiveri's structure worth mirroring in the B1 synopsis:
  **Vision (WHY) → Methods (HOW) → Results (WHAT) → Impact (WOW)**;
  his team shape for a CoG: 1 PI, 2 postdocs, 3 PhD students — close
  to our plan (2 postdocs, 3–4 PhDs, 1 engineer).
