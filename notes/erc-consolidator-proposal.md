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

## Why the trade-off is worth revisiting now

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
stay manageable. Solid's **"last mile" problem** is that it lacks email's
free ride — most people don't run their own mail servers, but Solid pods
still need someone with an independent reason to host them.

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
