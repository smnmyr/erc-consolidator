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
  architectural way to check.** By early 2026, researchers had documented
  over 1,300 court filings containing fabricated case citations generated
  by AI tools, roughly 500 of them submitted by licensed attorneys.
  Sanctions have escalated sharply — from around $5,000 in 2023 to
  $55,000+ by 2025 — and in March 2026 the Sixth Circuit sanctioned two
  Tennessee attorneys in *Whiting v. City of Athens* over two dozen fake
  or misrepresented citations across three appeals; a month later, the
  Nebraska Supreme Court suspended an Omaha attorney after 57 of 63
  citations in a single brief turned out to be defective. Courts have held
  attorneys to a non-delegable duty to verify every citation regardless of
  source. A citation architecture with Xanadu-style persistent,
  verifiable transclusion — where a reference either resolves to the
  exact cited passage of an existing, immutable document or fails
  visibly — makes an entire category of these filings structurally
  impossible, rather than relying on individual verification discipline
  under professional-conduct rules.
- **Content-provenance standards are being bolted onto hardware and law
  because the Web has no native integrity guarantee.** With deepfake
  volume reportedly up roughly 900% between 2023 and 2025, camera makers
  (Sony, Canon, Nikon, Leica, Samsung) now sign images with hardware-rooted
  keys under the C2PA standard, and the EU AI Act's provenance-disclosure
  obligations take effect in August 2026 alongside a proposed U.S. federal
  rule of evidence (FRE 707) governing AI-generated evidence. This is,
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
  Jan 2026) — tests whether regulator-mandated data-access APIs actually
  let researchers audit platform behavior. The DSA-era, empirical
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

Team fit: Bekavac's line of work supplies the empirical/regulatory half
of the argument (how platform control over information actually plays
out, and where mandated openness does or doesn't fix it); the
Xanadu/Solid/RFC 9518 material above supplies the architectural half
(what a system could look like if it didn't have to route around those
incentives). The stakeholder analysis above should draw on this existing
empirical work rather than treating platform incentives as purely
theoretical.
