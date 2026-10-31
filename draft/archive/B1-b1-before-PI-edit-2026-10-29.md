# b.1 paragraphs 1-4 before the PI's edit in B1.docx (2026-10-29)

The World Wide Web's original design favored simplicity,
decentralization, and low coordination overhead, which enabled
explosive adoption but sacrificed stable references, built-in
versioning, and native bidirectional linking. This was a deliberate
choice: Berners-Lee's 1989 proposal required that the system "allow
existing systems to be linked together without requiring any central
control or coordination" [1], and Fielding and Taylor later clarified the trade-offs
that the resulting architecture yields:<!-- was: Fielding and Taylor later named what the resulting architecture buys: (PI edit in B1.docx) --> scalable component
interactions, general interfaces, independently deployable
components, and intermediaries that can be inserted anywhere [2].
These priorities suited a document-sharing system for physicists.
They do not suit the Web of today, which parliaments and courts cite,
through which regulators audit platforms, over which supply chains
report emissions, and on which software agents act. These uses need
references that stay stable and verifiable, authorship that can be
held accountable, data that can be computed over without being
disclosed, and interfaces through which agents discover what they are
permitted to do.

Where the architecture lacks such properties, platforms supply them.
Accounts, persistent storage, search, reputation, payment, and a
consistent shared state do not exist between independent Web sites;
platforms provide them inside proprietary stores into which they draw
the Web's content and interactions [3, 4, 5], and they extend
into the rest of the Web through APIs and plug-ins on their own terms
[6]. Users then rebuild continuity themselves through reposts,
screenshots, and off-platform link hubs [7]. Berners-Lee warned in
2010 that social networks were walling off the information their
users posted [8], and RFC 9518 describes the general mechanism:
functions built on open protocols still centralize through network
effects and switching costs [9]. The consequences reach the public
sphere. Engagement-optimized ranking amplifies some political content
over other content [10], and the EU's Digital Services Act now
obliges the largest platforms to assess such systemic risks and to
open their data to vetted researchers [11]. The Commission's first
fine under the Act, €120 million against X in December 2025, concerned
a "verified" badge that anyone could buy without an identity check and
terms that barred researchers from public data [12]. The Web itself
authenticates domains through TLS certificates, but it offers no
native way to state verifiably who stands behind a document or an
account, or what qualifies them [13]. Even the data that platforms
do release differs from what their users see [14, 15].<!-- was: terms that barred researchers from public data [12], and even the
data that platforms do release differs from what their users see
[14, 15]. --> Legal scholarship treats such architectural choices as
regulation in their own right [16, 17, 18]. Generative AI
repeats the pattern: answer engines and agentic browsers return
answers in place of links and so control access to the Web's content
[19], and the Court of Justice of the EU must now decide whether a
chatbot's summaries of press articles infringe the publisher's rights
[20]. The properties that high-stakes communities need are thus
available today, but each inside one platform and under its control.

Society pays for these omissions, mostly outside any courtroom. In
2007 the UK government found that more than half of the roughly 4,000
URLs ministers had given in answers to Parliamentary Questions since
1997 no longer resolved, and built a redirect service into its
national Web archive in response [21]; one in five scholarly
articles cites Web content that has since rotted [22]. Two days
before Slovakia's 2023 election, a fabricated recording of a party
leader discussing vote-rigging circulated with no provenance that
voters could check [23]. From February 2027, batteries sold in the
EU must carry a digital passport with carbon-footprint and
due-diligence data assembled from suppliers along the chain [24].
Law shows the cost most sharply, because there a reference's
stability is part of the claim it supports. The EU has given
judgments and legislation persistent identifiers [25, 26], but
these name documents, not cited passages or versions; half the URLs
cited in U.S. Supreme Court opinions no longer resolve, and Perma.cc
archives cited pages one citation at a time [27]. By early 2026,
more than 1,200 court decisions worldwide concerned AI-fabricated
citations [28], and the High Court of England and Wales warned that
citing fabricated authorities may lead to referral to the regulator or
to contempt proceedings [29]. Content provenance is being moved into
camera hardware [30] and into EU law [31, 11], and the Munich
Regional Court held in November 2025 that a language model's
memorization of song lyrics infringes copyright [32], a question
*The New York Times v. OpenAI* is litigating in the U.S.
[33, 34]. In each case the coordination cost the Web avoided was
deferred, not eliminated, and society now pays it one incident at a
time; courts see only the share that becomes litigation.

**The idea.** We propose to build these properties into the Web
itself, for the communities that need them. ISLANDS introduces the
*island*: a bounded networked information space, such as a
legal-citation community, a supply chain, or a community of
public-interest publishers on social media, whose members share
stakes high enough to justify the cost of coordination<!-- was: stakes high enough to afford coordination -->. Each island selects the
*non-functional properties* (NFPs) its stakes demand and provides them
jointly, and islands interoperate with one another and with the open
Web through the Web's existing low-coordination mechanisms. Within an
island, references are span-level, version-pinned, bidirectional, and
verifiable, as Xanadu specified [35, 36]; across the boundary
they degrade to ordinary Web links, so that every island remains
backwards-compatible with today's Web.<!-- was: *island*: a bounded information space, such as a legal-citation
community or a supply chain, whose members share stakes high enough
to afford coordination. Each island selects the *non-functional
properties* (NFPs) its stakes demand and provides them jointly, and
islands interoperate with one another and with the open Web through
the Web's existing low-coordination mechanisms. Within an island,
references are span-level, version-pinned, bidirectional, and
verifiable, as Xanadu specified [35, 36]; across the boundary
they degrade to ordinary Web links. --> Islands can also move away from
the Web in the opposite direction: an island of fixed, high-speed
installations may bind its interfaces once, at design time, in a
binary encoding, much as a linker resolves a program's symbols when
it builds the program [37, 38]. Entering an island is an explicit
admission step: a client, human or agent, is shown the island's NFP
set and accepts the obligations of membership, and this is where the
island applies its attribution regime. Islands also provide NFPs that
neither the Web nor Xanadu offered. *Confidentiality-preserving
references* resolve to a value that members can verify was correctly
derived from data they may not read; they generalize secure
multi-party computation (SMPC), which has run in production since
2008 [39, 40], including in our own system for supply-chain
assessment [41, 42]. *Purpose binding* attaches the terms of a
disclosure (recipient, purpose, validity window) to the reference, so
that a reference is re-resolved when its terms expire [43].
*Attribution* binds a reference to an accountable author or, through
anonymous credentials and the pseudonyms the European Digital
Identity Wallet must support, to an eligible but unidentified one
[44, 45, 46]. *Verifiable credentials* let a reference carry an
issuer's attested claim about its source, e.g., that a filing was
signed by a member of the bar or that an emissions figure was checked
by an accredited verifier [13, 47]. *Capability discovery* shows agents, after each
interaction, only the actions currently valid, in the hypermedia style
of REST [37] as extended to multi-agent systems [48, 49, 50];
current LLM agents instead receive statically linked tool
catalogues [51, 52].<!-- was: current LLM agents instead receive static tool catalogues
[51, 52]. --> The unifying scientific contribution is a **theory of
chosen guarantees**: a formal account of which NFP bundles an island
can provide, at which coordination cost, under which threat model,
and for which stakeholders. Neither hypertext research nor Web
engineering offers such an account (b.2).



# Figure 1 (ASCII architecture schematic) before its replacement on 2026-10-30

Figure 1 shows the resulting architecture: a guarantee stack that an
island assembles over a content-addressed substrate, with the theory
(O1) selecting the attainable bundle<!-- was: (O1) selecting the affordable bundle --> and the open Web reached through
a low-coordination boundary.

```
   +----------------------------- ISLAND -----------------------------+
   |  a bounded networked information space (e.g., social media)       |
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
   |       given size, stake, and threat model can sustain, at what    |
   |       coordination cost, and for which stakeholders.              |
   +-------------------------------------------------------------------+
      |  ^   inward: cross the border, accept the island's NFP set       
      |  |   (attribution regime applied); outward: low-coordination     
      v  |   interop, references degrade gracefully (Memento/robust)     
    open Web                                                           

   O5  instantiated and measured in three high-stakes islands:
       Island L (legal citation) . Island S (supply chain)
       Island M (social media)
```

*Figure 1. The ISLANDS reference architecture. Layers map to objectives
O2–O4 over a content-addressed substrate; O1 is the cross-cutting theory
that decides which layers a given island can sustain;<!-- was: which layers a given island can afford; --> O5 validates the
whole in three domains.<!-- was: whole in two domains. --> To be redrawn as a vector figure in the template.*


# b.2 paragraphs 1-2 before the PI comments of 2026-10-30

Hypertext research assumed rich, versioned, span-anchored links from
the start [36, 51, 52], and its agenda included versioning and
computed structure [53]. Open-hypermedia systems implemented
bidirectional links and referential integrity at workgroup scale
[54, 55]; link rot had hence been addressed before the Web made it
endemic. The Web dropped these guarantees in order to scale
[1, 45]. Remedial infrastructure (e.g., persistent identifiers,
Web archives, Memento [56], Perma.cc [28], and robust hyperlinks
[57]) keeps the mutable substrate and builds compensating archives
beside it. It thereby neither prevents drift nor verifies integrity,
and it reintroduces central coordination points. W3C specifications
address passages and backlinks on the open Web: Web Annotation
selectors [58] and text fragments [59] identify a passage
of a page, and Webmention [60] and Linked Data Notifications
[61], which the W3C Social Web Working Group maintains together with
ActivityPub [62], deliver opt-in backlinks. None of them pins
a version or verifies what it points to. Services assemble
bespoke NFP profiles in the same way, e.g., persistence via Perma.cc,
provenance via C2PA [31], and identity and notarization via DOIs or
blockchains. We read these profiles as evidence of demand for chosen
guarantees, but each serves one silo and none can be shared or
composed. Content-addressed and versioned storage (Git; IPFS [63];
Software Heritage identifiers [64]) and provenance attestation
[31, 65] supply the substrate that Xanadu lacked. They are,
however, storage and signing primitives without span semantics, a
link layer, or a governance model. Nanopublications come closest
[66, 67]. They form a deployed, federated network of immutable,
signed semantic statements with self-verifying identifiers, i.e., an
island at statement granularity, and may become a component of ours;
they do not, however, offer span addressing over arbitrary content,
transclusion, or confidentiality-preserving resolution.



# b.2 before the PI restructuring saved in B1.docx at 11:25 on 2026-10-30

<!-- was: b.2 paragraphs 1-2 before the PI's edits and comments of 2026-10-30; full text in draft/archive/B1-b1-before-PI-edit-2026-10-29.md -->
Hypertext research in its beginnings assumed rich, versioned,
span-anchored links (e.g., [38, 53, 54]), and its agenda included
versioning and computed structure (e.g., [55]). Open-hypermedia
systems implemented bidirectional links and referential integrity at
workgroup scale [56, 57]; link rot had thus been addressed even before
the Web made it endemic. The Web dropped these guarantees in order to
scale [1, 47], and this was a sensible and pragmatic choice at the
time. Since the 1990s, remedial infrastructure (e.g., persistent
identifiers, Web archives, Memento [58], Perma.cc [30], and robust
hyperlinks [59]) has kept the *mutable architecture* and compensated
for its drawbacks, such as link rot and misattribution, e.g., through
Web archives with permanent links such as the Internet Archive's
Wayback Machine. In research, we know the problem well, since link rot
undermines reproducibility [25], and it gave rise to repositories such
as Zenodo [60]. Such compensation did not touch the architectural
principles of the Web, since changing them might fragment what the
W3C's Ethical Web Principles call "one web" [15]. W3C specifications
address passages and backlinks on the open Web: Web Annotation
selectors [61] and text fragments [62] identify a passage of a page,
and Webmention [63] and Linked Data Notifications [64], which the W3C
Social Web Working Group maintains together with ActivityPub [65],
deliver opt-in backlinks. None of them, however, pins a version or
verifies what it points to. Dedicated services assemble specific NFP
profiles as well, e.g., persistence via Perma.cc or Zenodo, provenance
via C2PA [33], and identity and notarization via DOIs or blockchains.
Solid [66] assembles a profile around the individual: *data
sovereignty*, since users keep their data in personal stores of their
choice; *privacy and access control*, since each application reads
only what the user grants it; and *portability*, since the data
outlives the application that wrote it. These developments are
evidence of the demand for chosen guarantees that extend beyond those
of the basic Web architecture, but each provides one fixed profile,
and none can be shared or composed with another.

A widely applicable architectural shift is possible today, which it
was not when the Web emerged in the 1990s. Content-addressed and
versioned storage (Git; IPFS [67]; Software Heritage identifiers [68])
and provenance attestation [33, 69] now supply, at Web scale, the
substrate that Xanadu lacked. They are, however, storage and signing
primitives without span semantics, a link layer, or a governance
model. Nanopublications come closest [70, 71]. They form a deployed,
federated network of immutable, signed semantic statements with
self-verifying identifiers, i.e., an *island* at statement granularity,
and may become a component of ours; they do not, however, offer span
addressing over arbitrary content, *transclusion*, or
confidentiality-preserving resolution.

Re-decentralization efforts relocate *control* and leave
*addressability* as it was. Solid's pods keep location-addressed,
mutable resources [66], and data spaces relocate contracts and
governance [72]. Federated social media follows the same line:
ActivityPub distributes servers but keeps posts location-addressed and
mutable [65], and Bluesky's AT Protocol signs and
content-addresses each user's repository [73] but leaves
references between posts unverified and offers one fixed set of
guarantees to all communities. EU data law follows the same line: the Data Act and
the portability rights of the GDPR and the DMA move copies of data
between holders [74], and the Solid deployments that implement them
(cf. our own [75, 76]) leave references location-addressed.
Verborgh argues that raw-data transfer cannot sustain a market and
proposes trading purpose-bound derivations whose terms limit their
shelf life and use [42]. No reference layer can yet name such a
derivation, pin it to a version, or carry its terms. Usage control
formalized such terms [77, 78], and sticky policies bind them to
the data [79]. Enforcement after release, however, requires a
trusted monitor at the recipient or falls back on detection after the
fact [78]. RFC 9518 explains why open specifications alone do not
prevent centralization, and we adopt the design-level mitigations it
lists [9]. Network architecture faced the same question one layer
below. Clark et al. argued that an Internet embedded in society must
leave room for the *tussle* between stakeholders with conflicting
interests, and proposed design for change and controlled transparency
as its tenets [80, 81]. Plutarch argued for heterogeneous
network contexts joined by translating functions at their borders
[82]. These positions state principles but predict no outcome,
and they concern packets and addresses, not references.

SMPC has run in production since the Danish sugar-beet auction of
2008 [40] and in Estonian government statistics [41], and
general-purpose protocols and implementations such as SPDZ [83] and
MP-SPDZ [84] make arbitrary computations practical. Our PEP-LCA
protocol computes joint supply-chain assessments across up to 50,000
participants without a trusted third party [85], and a follow-on
system anchors share disclosure in Solid's access-control layer
[86]. Each of these deployments is, however, a bespoke application,
and none exposes its result as a reference that others can cite and
re-resolve. <!-- moved to B2 §2.1 on 2026-10-30 (PI request): Information-flow control approached the problem from
programming languages. The decentralized label model [92] and
Fabric [removed: n88] let mutually distrusting principals share persistent
objects under confidentiality and integrity labels. They enforce these
labels by placing cleartext only on trusted nodes, over mutable,
store-identified objects, and they do not quantify what sustaining a
policy costs. -->Verifiable credentials address a further part of the
problem: the W3C data model [14], selective-disclosure formats such
as SD-JWT [87], and the European Digital Identity Wallet [45] let
a holder prove an issuer's claim (e.g., a professional licence)
without revealing more than needed [46, 88]. They are,
however, presented to one verifier within one session, and they are
not bound to the references that the claim concerns. Hypermedia multi-agent systems research argues for
run-time *affordance* discovery [48, 89]. Current LLM-agent
practice, in contrast, uses statically linked tool lists
[51, 52], which<!-- was: uses static tool lists [51, 52], which -->
indirect prompt injection turns into an attack surface [90], and no
existing design connects *capability discovery* to a verifiable
reference layer.

**The gap.** We are not aware of any system that composes
immutability, span-level verifiable addressing, transclusion,
confidentiality-preserving resolution, and agent-facing affordance
discovery into one reference architecture. We are also not aware of
a theory that predicts which of these guarantees an island of a given size, stake, and threat model can sustain.<!-- was: an island of a given size, stake, and threat model can afford. -->

