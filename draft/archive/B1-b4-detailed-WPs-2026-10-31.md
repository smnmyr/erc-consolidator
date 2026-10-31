# B1 b.4 with detailed work packages, replaced by a half-page overview on 2026-10-31 (PI request)

### b.4 Research strategy and methods (~1.75 pages)

The work packages follow the order of the argument. WP1 establishes
the *islands* that society requires. WP2 and WP3 run in parallel and
derive what these islands need: the *link classes* inside an island
(WP2) and the translations at its border (WP3). WP4 builds the
technologies that the islands require, and WP5 validates them with
their communities.

**WP1 — Societally required islands (M1–M18, revised annually).**
Method: stakeholder-based requirements analysis and design-science
iteration. WP1 does not start from a blank page. This synopsis already
sketches four islands (Figure 1), each grounded in a domain in which
our team works. *Island L* serves legal citation and copyright: it
needs persistence, span addressing, backlinks, attribution, and
credentials, and copyright disputes need the attribution trails of
reuse that the Web never recorded [18, 36, 37]. *Island S* serves
industrial supply chains under the disclosure duties of the battery
passport and CBAM [28, 93]: it needs confidential references,
credentials of accredited verifiers [94], *purpose binding*,
persistence, and agent-mediated onboarding. *Island M* serves
platforms and the public sphere against misinformation and
manipulation: it needs persistent and attributed posts, credentials
that state who stands behind an account [13], confidential research
access under the DSA [11], and purpose binding for the use of posts
by AI models [24]. *Island F* is the downgrade island. It serves
fixed, high-speed installations and deliberately violates the Web's
uniform interface [48] with binary interfaces bound at design time
(*Static Links*), yet it stays compatible with the Web architecture:
its resources keep URIs, are described in Web of Things Thing
Descriptions [95], and are reachable through the uniform interface
at its border.

WP1 solidifies these drafts with the actors that would run and use
them. Through semi-structured interviews with each class of actor
(hyperscaler, legacy industry, OSS/privacy community, browser vendor,
platform, public record-keeper), institutional analysis of funding
models, the RFC 9518 mitigation checklist [9], and the W3C TAG's
societal-impact self-review, which asks about power dynamics and
points of centralization [96], it asks which NFP bundle each
community needs, which actor would keep each guarantee, and whether
an island changes that actor's incentive to centralize. A guarantee
that no actor has an incentive to keep is one the theory should
decline to promise. The result is an account of the societally
required islands, each stated as an NFP bundle with its community,
stakes, and threat model. Its counterpart is an *architectural
decision record* of what ISLANDS does not do. Candidates for exclusion
are islands that need Web-wide coordination (e.g., a global registry
that replaces DNS), islands without a path back to the open Web, and
islands that enforce usage on devices their members do not control.
Both documents are revised at each annual integration milestone.

**WP2 — Link classes and the theory of chosen guarantees (M6–M60,
continuous).** Method: formal modeling and design-science iteration.
WP2 isolates the link classes that the WP1 islands require and
develops a *guarantee calculus*, i.e., a lattice of guarantee bundles
ordered by strength. We formalize the bundles as labels in the
information-flow control tradition [97, 98] and extend these
labels with persistence and attribution components. Each bundle
carries its minimal coordination requirements (e.g., registration,
replication, identity, availability coupling) and its admissible
threat models. Here we draw on distributed-systems impossibility
results [99, 100], simulation-based security definitions [101],
and RFC 9518's centralization vocabulary [9]. Some guarantees cannot
be enforced once a reference has resolved, but compliance with them
can be made incentive-compatible. The calculus hence also scores each
bundle by the margin by which compliance is less costly than
defection for the actor able to defect. This is the mechanism that
transcopyright used for reuse [102] and that current data-economy
proposals use for derived insights [43].

To make the calculus checkable, we name each bundle as a *link class*
that a reference can declare and a client can enforce, much as link
relations [103] or HTTP status codes do at lower stakes. The core is
a ladder of persistence and integrity. *Classic Jumplinks* are the
Web default (location-addressed, no guarantee) and the fallback
outside any *island*. *Archived Links* stay resolvable through
redundancy, as with Memento and Perma.cc [31, 60], but are not
verified. *Trusted Links* are registered in the island and tracked
bidirectionally, which makes them accountable but not
cryptographically checked [58]. *Verified Links* are span-level,
version-pinned, and content-addressed, so that resolution matches the
cited bytes exactly or fails visibly. *Cryptographic Links* are
resolved through SMPC or zero-knowledge proofs (WP4) and return a
verified derivation from data the client never sees. Further axes cut
across the ladder. *Attribution* is non-monotone, since binding
actions to identities trades accountability against chilling effects
[104, 105]; European courts have weighed this balance since the
census judgment [106] and for anonymous online comment [107].
Attribution is hence a pair (*Attributed* versus *Anonymous/Pseudonymous
Links* [45]), which we evaluate against island governance as well as
coordination cost. *Trust* adds *Endorsed Links*, whose resolution
carries a decay-bounded, Sybil-resistant [108] score over retractable
endorsements, and *Credentialed Links*, whose resolution returns a
*verifiable credential* about the source together with its current
revocation status [14]. Endorsements aggregate the judgment of
peers; credentials rest on the authority of an issuer, and the island
decides which issuers it accepts. *Usage* adds *Purpose-Bound Links*,
whose terms (recipient, purpose, window) travel with the reference, so
that an expired derivation is re-resolved instead of reused. Since no
substrate can prevent retention [80], we assess this class by its
compliance margin. *Modality* adds *Capability Links* (the
state-dependent *affordances* of WP4), to which every rung applies as
it does to content. *Link time* records when a reference is resolved,
in the sense of program linkers [109]. Capability Links bind as late
as possible, at each interaction. *Static Links* bind at design time,
in a fixed binary encoding, as Web of Things descriptions already
allow for protocols such as Modbus [95]. They give up the
evolvability that a uniform interface provides and regain the
efficiency it sacrifices [48], which suits Island F. Like
attribution, *link time* is non-monotone: the calculus assesses it by
when the coordination cost is incurred, once at design time or
incrementally at every interaction.

A declared class is a falsifiable claim with two proof obligations.
*Realizability* requires that, under its coordination requirements
and threat model, a conforming implementation returns the class's
guarantee or fails visibly, and never downgrades silently. *Necessity*
requires that dropping any one requirement admits an execution that
violates the guarantee undetected, i.e., that no rung can be attained
at lower coordination cost. For an island of given size, stake, and
threat model, the calculus then predicts the highest class it can
sustain and at what cost. We develop the calculus iteratively against
the WP3 and WP4 designs and test it against WP5 measurements: every
architectural choice in these work packages should be derivable from
the theory or force a revision of it. Deliverables are the formal
model, the link-class taxonomy, design decision procedures, and a
published island design handbook.

**WP3 — Border checks: translating NFPs at island borders (M6–M48, in
parallel with WP2).** Method: protocol design with formal
verification and conformance testing. Information that enters or
leaves an island crosses a border at which its NFPs, and the concepts
that support them, must be translated. Inbound, an *admission
protocol* (the *border crossing*) lets a client discover the island's
NFP set and bind to it. The binding is a *credible commitment* in the
sense of the W3C TAG [23]: the client's user agent restricts the use
of the island's content, and nothing beyond it, and keeps that
restriction loyally after admission, e.g., by re-resolving a
Purpose-Bound Link once its terms expire. Here the island applies its
attribution regime (e.g., by asking the client to present verifiable
credentials, with selective disclosure [89], or by issuing one).
References can also be upgraded at admission: a Classic Jumplink
becomes a Verified Link once its target is snapshotted, hashed, and
registered, and a claim becomes a Credentialed Link once an issuer
that the island accepts has attested it. Outbound, references are
downgraded: a Verified or Cryptographic Link becomes a Classic Jumplink
for a non-member client, carrying a text fragment [64] that keeps the
cited passage addressable where the page still contains it, and
interoperates with Memento [60] and robust hyperlinks [61]; a
Cryptographic Link releases only its derived value; and a
Purpose-Bound Link carries its terms with it. Island F's border
translates between binary bindings and the uniform interface, so that
its Static Links appear on the open Web as ordinary resources.
Between two islands, translation maps one bundle onto another, e.g.,
whether Island L accepts a credential issued in Island M, based on the
issuer lists and usage vocabularies that each island publishes. For
each NFP and each direction, WP3 determines whether a translation is
an upgrade, a downgrade, or impossible, and it requires every
downgrade to be visible, so that no reference loses a guarantee
silently. Deliverables are a translation table for all link classes
and NFP-supporting concepts, the admission protocol, border gateways
for each island, and a conformance test suite.

**WP4 — Island technologies (M12–M54).** Method: systems research,
cryptographic protocol design with proofs, and comparative
evaluation. From the islands of WP1 and the link classes of WP2, we
deduce the technologies that the islands require, in three tasks.

*T4.1 Reference layer.* We design the island addressing model.
Span-level identifiers are pinned to immutable versions in a
Merkle-DAG store, which we build on Git and IPFS primitives [69] and
on SWHIDs [70], following RFC 9518's advice to reuse proven
mechanisms [9]. A bidirectional link registry scoped to the island
makes explicit the coordination that Xanadu wanted globally and the
Web refused [39], and *transclusion* records its provenance [71].
Every reference is typed by its WP2 link class, and the type is
enforced structurally. Resolving a Verified or Cryptographic Link
thereby returns the exact cited span (or a verified derivation of it)
or fails visibly. The registry stores retraction as a superseding
record and deletes nothing. A Verified or Trusted Link can hence honour
a legal erasure request [110] without breaking the immutable history
on which other references depend. We benchmark the reference
implementation per link class for resolution latency, storage
overhead, and link-maintenance cost at island scales of 10² to 10⁵
members.

*T4.2 Confidential references.* We generalize the PEP-LCA results
[87, 88] into a *resolution protocol family*. In this family, a
reference's target is secret-shared across island members, and its
resolution is a joint computation with a verifiable result. Research
arcs: (i) from honest-but-curious to malicious security, using
verifiable secret sharing [111] and zero-knowledge correctness proofs,
which we expect to yield a quantified privacy-performance frontier;
(ii) protocols that tolerate member downtime, which removes the
availability coupling we documented in PEP-LCA [87]; and (iii) input
integrity through committed inputs and attested sources that connect
to hardware-rooted provenance [34]. We prove security in the
simulation-based model [101] and evaluate performance on realistic
island topologies, together with K. Mitrokotsa and N. Cheng, who
co-supervised the PEP-LCA work [87].

*T4.3 Agents and static bindings.* We build the island's agent
gateway, which exposes capabilities as state-dependent affordances
made perceivable through *signifiers* [112]. The gateway is a
hypermedia-driven layer [48] over MCP-class agent protocols [52]. It
explains *why* an action is currently valid and gives explicit
ordering guarantees for dependent state-changing calls. Each
affordance carries the WP2 link class of the resource it exposes, so
that an agent can tell a Verified citation from a Classic Jumplink
before acting on it. An agent crosses the border (WP3) by accepting
the island's NFP set and presenting a verifiable credential that
states on whose behalf it acts, so that identity and obligations bind
before any state-changing call. For Island F, the same descriptions
bind interfaces at design time as Static Links over binary protocol
bindings. We compare task success, safety violations, evolvability,
and latency under (a) statically linked tool catalogues, (b) our
affordance layer, (c) hybrids, and (d) Static Links, in scenarios
drawn from the WP1 islands. We expect affordance-scoped exposure to
outperform statically linked catalogues on safety and evolvability
without loss of task success, and Static Links to outperform both on
latency where the installation does not change. The measurements
thereby locate, for each scenario, the link time the calculus should
recommend. T4.3 extends our work on signifiers [50, 51, 91] towards
standardization in the W3C Autonomous Agents on the Web Community
Group.

**WP5 — Validation islands and incentives (M18–M60).** Method: three
case studies, an industrial demonstrator, and a repeated stakeholder
analysis. *Island L (legal citation)* is an
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
suppliers, including installations outside the EU [28, 93]. Since
CBAM requires actual emission values to be checked by accredited
verifiers [94], Island S also tests Credentialed Links that
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
acceptance by publishers and researchers. *Island F (fixed
installations)* is demonstrated in building automation (Siemens) and
edge computing (AFarEdge), where T4.3's comparison of link times runs
on installations that change rarely and need low latency. In the last
project year, we repeat the WP1 interviews with each class of actor
and measure whether the deployed islands changed their incentive to
centralize. The analysis builds on our platform-audit work [16, 17],
our working relationship with Solid's steward (the ODI, a CoCoDa
partner), and the PI's seat on the European VLOP-auditing oversight
board.

**Integration and openness.** Annual integration milestones bind the
WP3 and WP4 prototypes into one architecture, which WP5 then
evaluates, and revise the WP1 account and decision record.
All software is open source, and all publications are open access.
All specifications go to the W3C groups that maintain the protocols
islands build on, or to their successors: the Linked Web Storage
Working Group (reference layer), the Social Web Working and Community
Groups (Island M), the Verifiable Credentials and Federated Identity
Working Groups (admission), the Web of Things Working Group (Static
Links), and the Autonomous Agents on the Web Community Group (agent
layer). Each specification first passes the TAG's societal-impact
self-review [96].



# B1 reference list at that time

### References (not counted toward the page limit)

[1] T. Berners-Lee. *Information Management: A Proposal.* CERN, March 1989.
[2] R. T. Fielding, R. N. Taylor. Principled design of the modern Web architecture. *ACM Transactions on Internet Technology* 2(2):115–150, 2002. doi:10.1145/514183.514185
[3] T. Gillespie. The politics of 'platforms'. *New Media & Society* 12(3):347–364, 2010. doi:10.1177/1461444809342738
[4] J.-C. Plantin, C. Lagoze, P. N. Edwards, C. Sandvig. Infrastructure studies meet platform studies in the age of Google and Facebook. *New Media & Society* 20(1):293–310, 2018. doi:10.1177/1461444816661553
[5] J. van Dijck, T. Poell, M. de Waal. *The Platform Society: Public Values in a Connective World.* Oxford University Press, 2018. doi:10.1093/oso/9780190889760.001.0001
[6] A. Helmond. The platformization of the Web: Making Web data platform ready. *Social Media + Society* 1(2), 2015. doi:10.1177/2056305115603080
[7] L. Bekavac, S. Mayer. Broken links and fading stories: How dominant online platforms subvert the hypermedia foundation of the Web. *ACM Web Science Conference (WebSci '26)*, 221–226, 2026. doi:10.1145/3795766.3799767
[8] T. Berners-Lee. Long live the Web. *Scientific American* 303(6):80–85, 2010. doi:10.1038/scientificamerican1210-80
[9] M. Nottingham. *Centralization, Decentralization, and Internet Standards.* RFC 9518, IETF, 2023.
[10] F. Huszár, S. I. Ktena, C. O'Brien, L. Belli, A. Schlaikjer, M. Hardt. Algorithmic amplification of politics on Twitter. *PNAS* 119(1):e2025334119, 2022. doi:10.1073/pnas.2025334119
[11] Regulation (EU) 2022/2065 (Digital Services Act), Arts. 34, 35(1)(k), and 40; Commission Delegated Regulation (EU) 2025/2050 on data access for vetted researchers.
[12] C. Goanta, S. Zannettou, R. Kaushal, J. van de Kerkhof, T. Bertaglia, T. Annabell, H. Gui, G. Spanakis, A. Iamnitchi. The great data standoff: Researchers vs. platforms under the Digital Services Act. *Proceedings of the International AAAI Conference on Web and Social Media (ICWSM)* 20(1):874–888, 2026. doi:10.1609/icwsm.v20i1.42671
[13] European Commission. Commission fines X €120 million under the Digital Services Act. Press release, 5 December 2025.
[14] M. Sporny, T. Thibodeau Jr, I. Herman, G. Cohen, M. B. Jones (eds.). *Verifiable Credentials Data Model v2.0.* W3C Recommendation, 15 May 2025.
[15] D. Appelquist, H. Beeman, A. Guy (eds.). *Ethical Web Principles.* W3C Statement, 12 December 2024.
[16] L. Bekavac, J. Strecker-Bischoff, K. Garcia, S. Mayer, A. Tamò-Larrieux. Scrutinizing systemic risks in personalized recommender systems through sock-puppet auditing of VLOPs. *ACM Transactions on Recommender Systems* 5(1):1–47, 2026. doi:10.1145/3795516
[17] L. Bekavac, S. Mayer. Platforms' research API data access: What users see vs. what researchers can retrieve. *ACM FAccT* 2026. doi:10.1145/3805689.3812237
[18] Cour d'appel de Paris, rulings of 29 October 2026 upholding the July 2026 order of the Autorité de la concurrence against Meta (neighbouring rights of press publishers); reported by AFP, "French court rules Meta must negotiate over rights payments", France 24, 29 October 2026. **[replace with the decision reference once published]**
[19] L. Lessig. *Code and Other Laws of Cyberspace.* Basic Books, 1999.
[20] M. Hildebrandt. *Smart Technologies and the End(s) of Law.* Edward Elgar, 2015. doi:10.4337/9781849808774
[21] A. Tamò-Larrieux, S. Mayer, Z. Zihlmann. Not hardcoding but softcoding data protection. *Technology and Regulation* 2021:17–34, 2021. doi:10.71265/a1wsy445
[22] L. Zard. Internet ozone layer: A vision for reclaiming human freedom in information civilization. Working paper, SSRN 5735624, 2025.
[23] J. Yasskin, S. Capadisli (eds.). *User Agents.* W3C Technical Architecture Group, Group Note, 22 October 2026.
[24] Reddit, Inc. Q3 2026 earnings call, 29 October 2026 (transcript: The Motley Fool, 30 October 2026); reported as "As search traffic dries up, Reddit announces it's shifting to a logged-in experience", TechCrunch, 29 October 2026.
[25] A. Spencer, J. Sheridan, D. Thomas, D. Pullinger. UK government Web continuity: Persisting access through aligning infrastructures. *International Journal of Digital Curation* 4(1):107–124, 2009. doi:10.2218/ijdc.v4i1.82
[26] M. Klein, H. Van de Sompel, R. Sanderson, H. Shankar, L. Balakireva, K. Zhou, R. Tobin. Scholarly context not found: One in five articles suffers from reference rot. *PLoS ONE* 9(12):e115253, 2014. doi:10.1371/journal.pone.0115253
[27] L. de Nadal, P. Jančárik. Beyond the deepfake hype: AI, democracy, and "the Slovak case". *Harvard Kennedy School Misinformation Review* 5(4), 2024. doi:10.37016/mr-2020-153
[28] Regulation (EU) 2023/1542 (Batteries Regulation), Art. 77 and Annex XIII (battery passport, applicable from 18 February 2027).
[29] Council conclusions inviting the introduction of the European Case Law Identifier (ECLI) and a minimum set of uniform metadata for case law. OJ C 127, 29 April 2011.
[30] Council conclusions inviting the introduction of the European Legislation Identifier (ELI). OJ C 325, 26 October 2012.
[31] J. Zittrain, K. Albert, L. Lessig. Perma: Scoping and addressing the problem of link and reference rot in legal citations. *Legal Information Management* 14(2):88–99, 2014. doi:10.1017/S1472669614000255
[32] D. Charlotin. *AI Hallucination Cases* database, damiencharlotin.com/hallucinations, accessed May 2026. **[re-check counts at submission]**
[33] *R (Ayinde) v. London Borough of Haringey; Al-Haroun v. Qatar National Bank* [2025] EWHC 1383 (Admin), Divisional Court, 6 June 2025.
[34] Coalition for Content Provenance and Authenticity. *C2PA Technical Specification*, v2, 2024–2025.
[35] Regulation (EU) 2024/1689 (Artificial Intelligence Act), Art. 50.
[36] Landgericht München I, judgment of 11 November 2025, 42 O 14139/24 (*GEMA v. OpenAI*), not final. **[re-check appeal status at submission]**
[37] *The New York Times Co. v. Microsoft Corp. and OpenAI*, No. 1:23-cv-11195 (S.D.N.Y., filed 27 December 2023).
[38] George Washington University Law School. *Database of AI Litigation (DAIL)*, accessed 2026. **[re-check at submission]**
[39] T. H. Nelson. *Literary Machines.* Mindful Press, 1981.
[40] T. H. Nelson. Xanalogical structure, needed now more than ever. *ACM Computing Surveys* 31(4es), 1999.
[41] P. Bogetoft, D. L. Christensen, I. Damgård, M. Geisler, T. Jakobsen, M. Krøigaard, et al. Secure multiparty computation goes live. *Financial Cryptography and Data Security 2009*, LNCS 5628:325–343. doi:10.1007/978-3-642-03549-4_20
[42] D. Bogdanov, L. Kamm, B. Kubo, R. Rebane, V. Sokk, R. Talviste. Students and taxes: A privacy-preserving study using secure computation. *Proceedings on Privacy Enhancing Technologies* 2016(3):117–135. doi:10.1515/popets-2016-0019
[43] R. Verborgh. Inside the insight economy. ruben.verborgh.org, 12 August 2025.
[44] D. Chaum. Security without identification: Transaction systems to make big brother obsolete. *Communications of the ACM* 28(10):1030–1044, 1985. doi:10.1145/4372.4373
[45] J. Camenisch, A. Lysyanskaya. An efficient system for non-transferable anonymous credentials with optional anonymity revocation. *EUROCRYPT 2001*, LNCS 2045:93–118. doi:10.1007/3-540-44987-6_7
[46] Regulation (EU) 2024/1183 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework.
[47] J. Sedlmeir, R. Smethurst, A. Rieger, G. Fridgen. Digital identities and verifiable credentials. *Business & Information Systems Engineering* 63(5):603–613, 2021. doi:10.1007/s12599-021-00722-y
[48] R. T. Fielding. *Architectural Styles and the Design of Network-based Software Architectures.* PhD thesis, University of California, Irvine, 2000.
[49] A. Ciortea, S. Mayer, F. Gandon, O. Boissier, A. Ricci, A. Zimmermann. A decade in hindsight: The missing bridge between multi-agent systems and the World Wide Web. *AAMAS 2019*, 1659–1663.
[50] D. Vachtsevanou, A. Ciortea, S. Mayer, J. Lemée. Signifiers as a first-class abstraction in hypermedia multi-agent systems. *AAMAS 2023*, 1200–1208.
[51] J. Lemée, D. Vachtsevanou, S. Mayer, A. Ciortea. Signifiers for conveying and exploiting affordances: From human-computer interaction to multi-agent systems. *Annals of Mathematics and Artificial Intelligence* 92(4):815–835, 2024. doi:10.1007/s10472-024-09938-6
[52] *Model Context Protocol Specification*, version 2025-06-18. modelcontextprotocol.io.
[53] T. Schick, J. Dwivedi-Yu, R. Dessì, R. Raileanu, M. Lomeli, E. Hambro, L. Zettlemoyer, N. Cancedda, T. Scialom. Toolformer: Language models can teach themselves to use tools. *NeurIPS 2023*, 68539–68551.
[54] V. Bush. As we may think. *The Atlantic Monthly* 176(1):101–108, 1945.
[55] D. C. Engelbart, W. K. English. A research center for augmenting human intellect. *AFIPS Fall Joint Computer Conference*, 395–410, 1968. doi:10.1145/1476589.1476645
[56] F. G. Halasz. Reflections on NoteCards: Seven issues for the next generation of hypermedia systems. *Communications of the ACM* 31(7):836–852, 1988. doi:10.1145/48511.48514
[57] A. M. Fountain, W. Hall, I. Heath, H. C. Davis. MICROCOSM: An open model for hypermedia with dynamic linking. *ECHT '90*, Cambridge University Press, 298–311, 1990.
[58] H. C. Davis. Referential integrity of links in open hypermedia systems. *ACM Hypertext '98*, 207–216, 1998. doi:10.1145/276627.276650
[59] B. Kahle. Preserving the Internet. *Scientific American* 276(3):82–83, 1997. doi:10.1038/scientificamerican0397-82
[60] H. Van de Sompel, M. Nelson, R. Sanderson. *HTTP Framework for Time-Based Access to Resource States: Memento.* RFC 7089, IETF, 2013.
[61] T. A. Phelps, R. Wilensky. Robust intra-document locations. *Computer Networks* 33(1–6):105–118, 2000. doi:10.1016/S1389-1286(00)00043-8
[62] European Organization for Nuclear Research, OpenAIRE. *Zenodo.* CERN, 2013. doi:10.25495/7GXK-RD71
[63] R. Sanderson, P. Ciccarese, B. Young (eds.). *Web Annotation Data Model.* W3C Recommendation, 23 February 2017.
[64] N. Burris, D. Bokan (eds.). *URL Fragment Text Directives.* W3C WICG Draft Community Group Report, 2023.
[65] A. Parecki (ed.). *Webmention.* W3C Recommendation, 12 January 2017.
[66] S. Capadisli, A. Guy (eds.). *Linked Data Notifications.* W3C Recommendation, 2 May 2017.
[67] C. Lemmer-Webber, J. Tallon, E. Shepherd, A. Guy, E. Prodromou. *ActivityPub.* W3C Recommendation, 23 January 2018.
[68] A. V. Sambra, E. Mansour, S. Hawke, M. Zereba, N. Greco, A. Ghanem, D. Zagidulin, A. Aboulnaga, T. Berners-Lee. Solid: A platform for decentralized social applications based on linked data. Technical report, MIT CSAIL and QCRI, 2016.
[69] J. Benet. IPFS: Content addressed, versioned, P2P file system. arXiv:1407.3561, 2014.
[70] ISO/IEC 18670:2025. *Information technology: SoftWare Hash IDentifier (SWHID) specification.*
[71] L. Moreau, P. Missier (eds.). *PROV-DM: The PROV Data Model.* W3C Recommendation, 2013.
[72] T. Kuhn, M. Dumontier. Trusty URIs: Verifiable, immutable, and permanent digital artifacts for linked data. *ESWC 2014*, LNCS 8465:395–410. doi:10.1007/978-3-319-07443-6_27
[73] T. Kuhn, C. Chichester, M. Krauthammer, N. Queralt-Rosinach, R. Verborgh, et al. Decentralized provenance-aware publishing with nanopublications. *PeerJ Computer Science* 2:e78, 2016.
[74] B. Otto, M. ten Hompel, S. Wrobel (eds.). *Designing Data Spaces: The Ecosystem Approach to Competitive Advantage.* Springer, 2022. doi:10.1007/978-3-030-93975-5
[75] M. Kleppmann, P. Frazee, J. Gold, J. Graber, D. Holmgren, D. Ivy, J. Johnson, B. Newbold, J. Volpert. Bluesky and the AT Protocol: Usable decentralized social media. *ACM CoNEXT Workshop on the Decentralization of the Internet (DIN '24)*, 1–7, 2024. doi:10.1145/3694809.3700740
[76] Regulation (EU) 2023/2854 (Data Act); Regulation (EU) 2016/679 (GDPR), Art. 20; Regulation (EU) 2022/1925 (Digital Markets Act), Art. 6(9).
[77] L. Bekavac. From data portability to data control: Making regulation technically real. *4th Solid Symposium*, London, 2026.
[78] L. K. Seiling, J. Stein, S. Mayer, L. Bekavac. A Solid research infrastructure leveraging DMA data portability. 2026. **[TODO: venue]**
[79] J. Park, R. Sandhu. The UCON_ABC usage control model. *ACM Transactions on Information and System Security* 7(1):128–174, 2004. doi:10.1145/984334.984339
[80] A. Pretschner, M. Hilty, D. Basin. Distributed usage control. *Communications of the ACM* 49(9):39–44, 2006. doi:10.1145/1151030.1151053
[81] S. Pearson, M. Casassa-Mont. Sticky policies: An approach for managing privacy across multiple parties. *IEEE Computer* 44(9):60–68, 2011. doi:10.1109/MC.2011.225
[82] D. D. Clark, J. Wroclawski, K. R. Sollins, R. Braden. Tussle in cyberspace: Defining tomorrow's Internet. *IEEE/ACM Transactions on Networking* 13(3):462–475, 2005. doi:10.1109/TNET.2005.850224
[83] D. D. Clark, K. Sollins, J. Wroclawski, T. Faber. Addressing reality: An architectural response to real-world demands on the evolving Internet. *ACM SIGCOMM FDNA '03*, 247–257, 2003. doi:10.1145/944759.944761
[84] J. Crowcroft, S. Hand, R. Mortier, T. Roscoe, A. Warfield. Plutarch: An argument for network pluralism. *ACM SIGCOMM FDNA '03*, 258–266, 2003. doi:10.1145/944759.944763
[85] I. Damgård, V. Pastro, N. Smart, S. Zakarias. Multiparty computation from somewhat homomorphic encryption. *CRYPTO 2012*, LNCS 7417:643–662. doi:10.1007/978-3-642-32009-5_38
[86] M. Keller. MP-SPDZ: A versatile framework for multi-party computation. *ACM CCS 2020*, 1575–1590. doi:10.1145/3372297.3417872
[87] J. Grau. Towards decentralized privacy-enhancing life cycle assessment. MSc thesis, University of St. Gallen, 2025.
[88] J. Grau, M. Maftun, K. Garcia, S. Mayer. Solid and secure multi-party computation for a circular economy. *Solid Symposium* 2026.
[89] D. Fett, K. Yasuda, B. Campbell. *Selective Disclosure for JSON Web Tokens.* RFC 9901, IETF, 2025.
[90] A. Mühle, A. Grüner, T. Gayvoronskaya, C. Meinel. A survey on essential components of a self-sovereign identity. *Computer Science Review* 30:80–86, 2018. doi:10.1016/j.cosrev.2018.10.002
[91] D. Vachtsevanou, B. de Lima, A. Ciortea, J. F. Hübner, S. Mayer, J. Lemée. Enabling BDI agents to reason on a dynamic action repertoire in hypermedia environments. *AAMAS 2024*, 1856–1864.
[92] K. Greshake, S. Abdelnabi, S. Mishra, C. Endres, T. Holz, M. Fritz. Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection. *ACM AISec '23*, 79–90, 2023. doi:10.1145/3605764.3623985
[93] Regulation (EU) 2023/956 (Carbon Border Adjustment Mechanism), Art. 35 and Annex IV.
[94] Regulation (EU) 2023/956 (CBAM), Arts. 8 and 18; Commission Implementing Regulation (EU) 2025/2546 (verification principles); Commission Delegated Regulation (EU) 2025/2551 (accreditation of verifiers).
[95] S. Kaebisch, M. McCool, E. Korkan (eds.). *Web of Things (WoT) Thing Description 1.1.* W3C Recommendation, 2023.
[96] S. Capadisli, L. Odelola, A. Guy, T. Nitot (eds.). *Self-Review Questionnaire: Societal Impact.* W3C Technical Architecture Group, Group Note, 28 October 2026.
[97] A. C. Myers, B. Liskov. A decentralized model for information flow control. *SOSP 1997*, 129–142.
[98] D. E. Denning. A lattice model of secure information flow. *Communications of the ACM* 19(5):236–243, 1976.
[99] M. J. Fischer, N. A. Lynch, M. S. Paterson. Impossibility of distributed consensus with one faulty process. *Journal of the ACM* 32(2):374–382, 1985. doi:10.1145/3149.214121
[100] S. Gilbert, N. Lynch. Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services. *ACM SIGACT News* 33(2):51–59, 2002. doi:10.1145/564585.564601
[101] R. Canetti. Universally composable security: A new paradigm for cryptographic protocols. *FOCS 2001*, 136–145. doi:10.1109/SFCS.2001.959888
[102] T. H. Nelson. Transcopyright: A simple legal arrangement for sharing, re-use, and republication of copyrighted material on the net. *WWCA '97*, LNCS 1274, Springer, 1997.
[103] M. Nottingham. *Web Linking.* RFC 8288, IETF, 2017.
[104] J. W. Penney. Internet surveillance, regulation, and chilling effects online: A comparative case study. *Internet Policy Review* 6(2), 2017. doi:10.14763/2017.2.692
[105] M. Büchi, E. Fosch-Villaronga, C. Lutz, A. Tamò-Larrieux, S. Velidi, S. Viljoen. The chilling effects of algorithmic profiling: Mapping the issues. *Computer Law & Security Review* 36:105367, 2020. doi:10.1016/j.clsr.2019.105367
[106] Bundesverfassungsgericht, judgment of 15 December 1983, 1 BvR 209/83 (*Volkszählungsurteil*), BVerfGE 65, 1.
[107] European Court of Human Rights (Grand Chamber), *Delfi AS v. Estonia*, no. 64569/09, 16 June 2015.
[108] J. R. Douceur. The Sybil attack. *IPTPS 2002*, LNCS 2429:251–260. doi:10.1007/3-540-45748-8_24
[109] J. R. Levine. *Linkers and Loaders.* Morgan Kaufmann, 2000.
[110] Regulation (EU) 2016/679 (General Data Protection Regulation), Art. 17.
[111] T. P. Pedersen. Non-interactive and information-theoretic secure verifiable secret sharing. *CRYPTO '91*, LNCS 576:129–140.
[112] D. A. Norman. *The Design of Everyday Things.* Revised and expanded edition, Basic Books, 2013.
[113] S. Mayer. *Interacting with the Web of Things.* Doctoral thesis, ETH Zurich, 2014.
[114] L. Bekavac, S. Mayer, J. Strecker. QR-code integrity by design. *Extended Abstracts of CHI 2024*, 1–9. doi:10.1145/3613905.3651006
[115] J. Strecker, S. Mayer, K. Bektaş. Towards societally beneficial personalized realities: A conceptual foundation for responsible ubiquitous personalization systems. *ACM DIS 2025*, 1792–1814. doi:10.1145/3715336.3735709
[116] A. Tamò-Larrieux, C. Guitton, S. Mayer. A computational science perspective on the legal system. *Nature Computational Science* 5(11):990–991, 2025. doi:10.1038/s43588-025-00827-4
[117] C. Guitton, A. Tamò-Larrieux, S. Mayer. *AI and Law: How Automation is Changing the Law.* Routledge, 2025.

---

