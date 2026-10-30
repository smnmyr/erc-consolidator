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
