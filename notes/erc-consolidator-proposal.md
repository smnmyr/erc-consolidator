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
  content-addressed storage more broadly.

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
