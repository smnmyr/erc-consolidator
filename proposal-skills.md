# Proposal-Writing Skills

General lessons about writing (research) grant proposals, distilled from four drafting
efforts. Sections 1-8 come from the ERC Consolidator 2027 "islands" proposal (sources:
SwissNCP CoG webinar, Giacomo Indiveri's CoG-winner retrospective, official ERC
documentation, and the drafting process itself). Sections 9-12 come from the TANDEM
Health Forward start-up proposal (HSG/OKS, Aug 2026), which prepares a later Innosuisse
submission and was drafted directly in Word. Sections 13-16 come from the SoSy 27 event
funding effort (Sep 2026): three parallel applications for one symposium, to the SNSF,
the HSG Research Committee and the Swiss Informatics Foundation. Sections 17-18 come from
the SNSF project funding proposal on cognitive interoperability (Sep 2026), a LaTeX source
in git that the PI and the assistant edited in turns. Written to be reusable beyond any of
these schemes.

Section numbers are stable; new material is appended rather than interleaved, so notes
elsewhere that cite "§7" keep pointing at the same thing.

1. Evaluation mechanics · 2. Ambition · 3. Structure and craft · 4. Facts and citations ·
5. Team and institutions · 6. Process · 7. Writing like a person · 8. Naming ·
9. Preparatory and two-stage schemes · 10. Verifying the funder's rules ·
11. Writing for a mixed panel · 12. Editing the document programmatically ·
13. Splitting one project across several funders · 14. Filling official forms ·
15. Events, and what the money actually buys · 16. Keeping the source and the submission in step ·
17. Cutting to a character limit with the author · 18. Co-editing a LaTeX source in turns

## 1. Know the evaluation mechanics before writing a word

- **Write for how the document is read, not just what it must contain.** ERC B1 is
  evaluated *alone* at Step 1, so it must be self-sufficient, with no forward
  references to the implementation part. Any funding scheme has an equivalent
  structure; find out which parts are read by whom, when, and in isolation.
- **Identify the sole (or dominant) criterion and serve it.** For ERC it is
  scientific excellence: not feasibility, not consortium quality, not host
  institution. Every paragraph that doesn't argue excellence in a Step-1 document
  is wasted space.
- **Different audiences per stage**: "Impress non-experts in B1, convince experts
  in B2." The early-stage document is for generalist panelists (concise, clear,
  no insider jargon); the later-stage document is for domain experts (technically
  dense, complementary rather than redundant).
- **Follow the instructions to the letter**, and mirror the funder's own vocabulary
  ("transformative", "high-risk/high-gain", "innovation potential"). The Work
  Programme's evaluation questions are literally the questions reviewers answer;
  structure the text so the answers are findable.
- **Study the panel and precedent.** Learn panel members' research areas; search
  the funder's database of previously funded projects in the field. Choose the
  panel deliberately rather than by default.
- **Map the project across the panel's descriptors deliberately.** A proposal that
  credibly spans several sub-panel codes (here PE6_10 as core, plus PE6_2, PE6_5,
  PE6_7) can present that spread as the contribution ("a composition no single
  sub-field produced") rather than as lack of focus. Name the codes in the
  cross-panel text, commit to one primary and one secondary panel, and state the
  centre of gravity explicitly so the choice reads as deliberate.
- Verify eligibility rules against the **current** call documents; rules change
  between calls (the ERC PhD window widened from 7–12 to 5–15 years for 2027; an
  older slide deck would have wrongly excluded the PI).
- **Re-confirm country association / host eligibility from the current call, not
  memory.** Association to the funding programme moves between calls: Switzerland
  became fully associated to Horizon Europe on 10 Nov 2025 (retroactive to
  01.01.2025), so Swiss hosts are eligible for ERC 2027 with no
  host-in-another-country workaround, superseding the earlier "treated as
  associated" transitional regime. A stale assumption on this axis can invalidate
  the host choice.

## 2. Lead with ambition; anchor it in a felt problem

- **Vision first, competence second.** The primary question at stage one is "is
  this a great idea worth pursuing?", not "can this person do it?". Indiveri's
  structure works: **WHY (vision) → HOW (methods) → WHAT (results) → WOW (impact)**.
- **Open with the founding trade-off, stated fairly, then the thesis.** The
  ERC B1 opening the PI settled on (2026-10-29) runs: the original design
  choice and its rationale, from primary sources (Berners-Lee 1989; Fielding
  and Taylor on REST) -> what that choice enabled (billions of users and
  devices within three decades) -> an explicit thesis ("We argue that the
  Web's trade-offs are however too rigid for today's use cases") -> who needs
  what -> how the gap was filled meanwhile (platforms responded; the
  mitigations are unsatisfactory) -> who pays (dated cases, closed by one
  synthesis sentence) -> the idea. Crediting the existing system before
  criticizing it keeps reviewers who built it on side; a quotable one-liner
  does not replace this arc.
- **State the thesis as a claim of your own.** "We argue that ..." makes the
  position explicit and attackable; letting the reader infer it from the
  evidence reads as hedging.
- **Attach each requirement to the stakeholder that holds it.** "Publishers
  require traceable dereferencing, supply chain management requires
  aggregation over confidential data, courts and parliaments require stable,
  specific citations, users require sovereignty over their data, and society
  requires trusted content and accountable authorship" beats an abstract list
  of what "these uses need".
- **Judge the mitigations you cite.** Say whether the existing remedy works
  ("yielding unsatisfactory mitigation"; DSA researcher access "shown to be
  defunct in principle") and source the judgment. Listing remedies without a
  verdict leaves the gap unproven.
- **Present the project as an extension, not a replacement.** "We propose to
  extend the Web's architecture", islands interoperate "through the Web's
  existing low-coordination mechanisms that permit planetary scaling", and
  stay backwards-compatible. A clean-slate tone invites a panel to defend the
  incumbent system.
- **Let the communities choose; the project supplies the choice.** Frame the
  contribution as enabling stakeholders to select their own configuration ex
  ante ("an ex-ante selected architectural trade-off rather than ex-post
  patching or litigation") instead of prescribing one configuration for all.
- **Introduce a concept through the need it meets, then name it.** "...
  communities select their own property configuration, i.e., a set of desired
  non-functional properties (NFPs). ISLANDS introduces the *island* to capture
  such configured spaces." Define acronyms again in the main text even when
  the abstract already did.
- **In the synopsis, present mechanisms as instances of the design space, and
  new ones as research.** "Within an island, references can for instance be
  defined as span-level, version-pinned ...", "Through ISLANDS, we further
  explore NFPs that have not yet been proposed on an architectural level."
  Fixing one mechanism in B1 narrows the idea and invites attacks on details;
  claiming that islands already "provide" new properties overclaims.
- **Show that a case is a trend.** Extend a single regulatory example to its
  announced scope in a short parenthesis ("batteries sold in the EU (and, soon
  after, products from clothes to detergents) must carry a digital passport").
- **Close a block of cases with one synthesis sentence** that names what they
  share ("What these cases have in common is that ..."), then stop; drop
  side remarks such as "courts see only the share that becomes litigation".
- **Motivate with concrete, recent, verifiable events rather than abstractions.**
  Court sanctions, real dollar amounts, named cases, and dated statistics make an
  infrastructure problem urgent in a way that "link rot is a growing concern"
  never will. Lead the motivation with the most visceral evidence class.
- **State the intellectual core in one phrase** and repeat it as a through-line
  (here: "a theory of chosen guarantees"). Reviewers should be able to reproduce
  the idea to each other in a corridor.
- Frame the gap as a **false dichotomy the proposal dissolves** ("the field treats
  X and Y as an either/or; this project shows they are endpoints of a design
  space"). That is a stronger claim than "we improve on prior work".

## 3. Structure and craft

- **Objectives must be few, named, and testable.** 4–6 objectives, each one line
  of claim plus success criteria; work packages map onto them visibly.
- **Every work package needs a falsifiable output**, not just activity ("we will
  investigate…" is a smell; "we will produce X validated against Y" is not).
- Include the **risk/gain asymmetry explicitly** for high-risk schemes: name what
  could fail, why intermediate results are valuable even then, and why the upside
  justifies it. Reviewers reward candor over invulnerability.
- **Trim by function, not by sentence-shortening.** When cutting to a page limit,
  remove content that belongs in another document (partner justifications belong
  in the CV or implementation part, not the synopsis) rather than compressing
  everything uniformly into unreadability. The trim from 2,337 to roughly 2,140
  words cost nothing of the argument.
- Leave **headroom in page budgets** for a figure and the reference list: a
  synopsis that fills the limit with prose alone reads worse than one with a
  clear architecture diagram.
- **Treat hard character/word ceilings mechanically, and measure before you
  commit.** The ERC abstract caps at ~2,000 characters. Once a verified abstract
  sits at the ceiling, reframing it is editing under a budget, not free writing:
  thread new terminology by *substitution* (swap terms of similar length), offset
  any addition with an equal trim elsewhere, and compute the resulting length
  before writing rather than eyeballing it. A single vocabulary change ("chosen
  guarantees" → "non-functional properties") can silently blow the limit.
- Prior-work sections should read as a **funnel to the gap**: each lineage
  (history, remedial efforts, adjacent fields) ends by stating what it did *not*
  solve, so the gap synthesis at the end feels inevitable.

## 4. Facts, citations, and verification discipline

- **Verify every empirical claim before submission, with dated sources.** In one
  fact-checking pass, roughly a third of the vivid numbers needed correction
  (a "1,300 filings" figure, a "$55,000 sanction", a vendor list). Wrong numbers
  in a motivation section are exactly the kind of thing a hostile reviewer
  spot-checks.
- **Distrust your own error flags too.** An arXiv ID flagged as "malformed"
  turned out to be valid and had a better, peer-reviewed successor version.
  Verification runs in both directions.
- **Mark fast-moving statistics for a re-check at submission time** (litigation
  counts, product announcements). Record the retrieval date next to the claim.
- Prefer the **strongest citable version** of each reference (published venue
  over preprint) and upgrade as papers get accepted during the drafting window.
- **Never attach a citation to a claim its source does not make.** A paper on
  sedation practice in pediatric burn care does not support a statement about
  cost. Either find the source that does, or drop the number and make the
  comparison qualitative by naming the resources involved.
- **Administrative documents are not literature.** The call text, the funder's
  funding conditions, and internal programme provisions belong in the running
  prose by name, not in the bibliography. Removing two such entries meant
  renumbering 53 references; catching it earlier would have cost nothing.
- **Check cited-versus-defined in both directions every pass.** Dangling
  citations are the obvious failure; entries that are defined but never cited
  are the quieter one, and usually mark text that was cut around them.
- **Keep self-citations out of the idea paragraph.** The PI removed "including
  in our own system for supply-chain assessment [41, 42]" from "The idea" in
  B1; the team's own systems belong in the methods and team sections.
- **`[x]` marks a claim that still needs a source.** The PI writes `[x]`
  where a citation is missing; find, verify, and insert the source (or report
  that none supports the claim) before the next build.
- **Use the field's own term, precisely.** "Uniform interface" (the REST
  constraint), not "general interfaces"; "when defining the Representational
  State Transfer (REST) architectural style"; "persistent identifiers through
  ELI". A paraphrase of an established term reads as unfamiliarity with it.
- **When a self-citation is unusually load-bearing, say so in the sentence.**
  That the doctoral researcher the grant would fund is first author of a
  directly relevant paper is worth a clause in the text, not burial inside a
  bracket.
- **Patents count as track record for innovation-agency schemes.** Patent
  registries (Google Patents, Espacenet, WIPO Patentscope) block scripted
  access, so the PI's own scholar profile is the fastest reliable index. Flag
  numbers taken that way for the PI to confirm rather than presenting them as
  verified.

## 5. Team and institutional planning

- **Plan people as a timeline, not a list.** Existing staff have contract end
  dates; design explicit overlap/handover windows between departing members and
  the hires who inherit their threads (here: two departures at ≈M24, each with a
  planned handover to a specific postdoc).
- **Match the team shape to the scheme's norm.** A CoG-scale team is roughly
  1 PI + 2 postdocs + 3–4 PhDs (+ engineer); wildly larger or smaller shapes
  invite feasibility doubts.
- **No unnecessary partners.** For single-PI schemes, external experts stay
  collaborators, never beneficiaries; a consortium reflex actively hurts.
- Know which institutional facts are **not** evaluated (for ERC: host
  institution; grants are portable) so open questions on that axis don't block
  drafting.
- Budget and commitment rules (≥40% PI time, residency requirements, additional
  equipment funding) are constraints to design within from day one, not
  compliance checks at the end.
- **Know the optional-funding levers and default against them.** ERC "additional
  funding" is up to €1M on top of the ceiling (up to €2M for a PI relocating from a
  non-associated third country); it traditionally covers start-up, major
  equipment, large-facility access, and major field/experimental costs, and from
  the 2026 Work Programme may also cover personnel. It must be explicitly
  justified and the panel decides, so an unjustified request reads as padding.
  Default to the clean ceiling ask and reach for the top-up only when a specific
  cost (major compute, an extra hire) is genuinely load-bearing.

## 6. Process lessons (how to run the drafting itself)

- **Separate the layers**: a `sources/` folder for raw inputs, a growing master
  notes file where everything is summarized and cross-linked, and clean `draft/`
  documents that pull from the notes. New material gets folded into notes first,
  then selectively into drafts. This keeps drafts coherent while nothing is lost.
- **Keep a living TODO list inside the draft itself** (eligibility checks,
  support letters, panel research, figures, re-verification), and mark items done
  in place; the draft doubles as the project dashboard.
- **Mine adjacent documents for reusable substance.** A faculty-application
  package (research statement, CV, publication list) is pre-written raw material
  for the track-record section; a winner's retrospective talk is a template; a
  colleague's thesis can supply a whole methodological pillar.
- **Resubmission is part of the process.** ERC resubmissions succeed at ~1.5×
  the base rate and come with panel feedback. Write the first submission well,
  but don't treat rejection as terminal.
- For schemes with interviews: the one-page summary slide and rehearsed answers
  are their own deliverable. Schedule preparation (mock interviews, prep
  events), and expect the stress ("panic is normal").
- **Check file modification times before every editing session, and diff against
  your own last snapshot.** Between sessions the author may edit a different
  file, merge your version into theirs, or rename. Assuming the file you last
  wrote is still the live one risks overwriting a day of their work. In this
  project the author had migrated everything into `_v2` while the assistant was
  still editing `_v3`.
- **Snapshot before every destructive pass**, named for what it precedes
  (`_preShorten`, `_preRenumber`). It makes a later Word compare possible and
  turns "revert and redo differently" into a real option.
- **Agree what a change mark means, and hold the line at its boundary.** "Yellow
  marks new or rewritten text, not text merely trimmed" works until a shortening
  pass rewords 41 of 45 spans. Compression that introduces new words is a
  rewrite. When the rule has been applied too loosely, say so plainly and offer
  the author the choice of remedy instead of picking one quietly.
- **Check the layout before cutting prose.** Two rounds of trimming had been
  paying for a table whose column widths were never applied; fixing the table
  recovered nearly half a page. Find out where the space actually goes before
  rewriting content to save it.

## 7. Write like a person, not like a language model

A proposal drafted with AI assistance inherits AI writing tropes unless they are
edited out, and reviewers increasingly recognize them. A de-troping pass over
this proposal's drafts (2026-07-10, based on the tropes.fyi catalogue) taught
the following:

- **Em-dash density is the biggest tell in otherwise clean text.** The drafts
  had 88 and 75 em-dashes respectively, mostly as paired asides ("X — detail,
  detail — continues"). Convert most to parentheses, commas, colons, or
  sentence breaks; keep a handful of single dashes where the pause genuinely
  earns its emphasis. A human writer uses 2–3 per piece.
- **Ration the rhetorical contrast patterns.** "It's not X, it's Y", "not
  because X but because Y", "chosen, not assumed": one per document can be a
  strong closer; several make the text read as manufactured profundity. Keep
  the single strongest instance (for example the final sentence of the
  ambition section) and rewrite the rest positively.
- **Watch for stakes inflation.** "At civilizational scale" became "at the
  scale of the whole Web": the accurate claim is also the more credible one.
  Grant reviewers punish grandiosity; concrete numbers and named cases inflate
  stakes legitimately.
- **Drop filler signposts.** "— notably —", "importantly", "it's worth
  noting": if a fact matters, its placement and content must show it.
- **Avoid unicode arrows in prose** (A → B → C); spell the sequence out in
  words. Arrows are fine in genuinely notational contexts (Read→Navigate as a
  named access pattern, table cells, planning annexes).
- **Some conventions of the genre are exempt.** Named objectives ("O1 —
  Theory of chosen guarantees"), bolded work-package leads, and structured CV
  entries look like "bold-first bullets" but are standard grant formatting
  that reviewers expect; keep them. The tropes to hunt live in the running
  prose, not the scaffolding.
- **One deliberate use of a device is style; the same device ten times is a
  pattern.** The test is density and variety, not a ban list. Read a full
  section aloud: anything you would not say to a colleague, rewrite.
- Vocabulary tells ("delve", "landscape", "tapestry", "leverage", "robust")
  were absent from these drafts, but check for them anyway; they are the
  easiest to grep for.
- **Use academic, not commercial, vocabulary.** Do not say what an
  architecture "buys", that a design "wins", or that a guarantee is
  "priced", "cheap", "affordable", or "paid for". Write *provides* or
  *induces* (Fielding's term for architectural properties), *attains*,
  *outperforms*, *quantifies*, *assesses*, *sustainable*, *attainable*,
  *less costly*, *incentive-compatible*. Literal economic facts stay (a
  badge that anyone could buy). Grep the body for buy/win/price/cheap/
  afford/undercut/paid before submission (PI instruction, ERC CoG 2027,
  2026-10-29).

## 8. Naming, titles, and framing labels

The acronym, title, and the one technical label the proposal turns on are
positioning tools, not decoration. A naming iteration on this proposal
(2026-07-11) taught the following:

- **The name should encode the scientific claim, and a memorable metaphor that
  matches the core concept beats a tortured backronym.** "ISLANDS" works because
  the project's unit of analysis literally is an island (a bounded information
  space); the name reminds the reader of the idea for free.
- **Prefer an evocative name plus a descriptive subtitle over a strict
  letter-for-letter acronym.** Funders accept evocative names. Force a backronym
  only when the word cooperates: some letters (a terminal Y, an interior U/W) have
  almost no natural technical fillers, and a strained expansion reads worse than
  no expansion. Do not fight the alphabet.
- **Let the name follow the science.** When the differentiator sharpened (from
  "islands" to "islands *bridged* to each other and the open Web"), the name
  search followed it (bridge/weave metaphors). If a candidate name no longer
  matches the current pitch, that is a signal the pitch moved, not just the label.
- **Local/host resonance is a legitimate bonus.** A metaphor that also nods to the
  host's identity (St. Gallen's historic embroidery/textile industry → weave,
  stitch, lace, thread) is a detail a panel registers, provided it still maps
  cleanly onto the technical story.
- **Put the real claim in the tagline's operative words.** "supports non-functional
  properties" is inert; "any NFP *at once*" encodes the actual contribution (no
  forced trade-off among properties). One or two load-bearing words (here *at
  once*, *bridging*) can carry the whole pitch; choose the register deliberately
  ("guarantees" is punchier, "non-functional properties / NFPs" is more precise).
- **Introduce a precise technical label and gloss it once to unify vocabulary.**
  Relabelling "chosen guarantees" as "non-functional properties (NFPs)" and stating
  the equivalence a single time let the new term lead the abstract and framing
  while the body's existing "guarantees" stayed consistent without a full rewrite.
- **Naming is iterative and the PI's call.** Generate candidate names and taglines
  inline, tightest-first with brief rationale, and let the PI steer the metaphor
  family before committing; a fixed multiple-choice prompt is premature while the
  concept is still moving. Record naming decisions (and the direction that
  produced them) in the draft's living TODO list so later passes know the intent.

## 9. Preparatory and two-stage schemes

Schemes that fund work *towards* a later submission (here: HSG Health Forward
start-up financing preparing an Innosuisse innovation project; seed and
proof-of-concept instruments elsewhere) are judged on whether the preparatory
work makes the target submission competitive. That imposes a structure most
drafts get wrong on the first pass.

- **Two projects must be specified, and the boundary between them has to be
  visible at a glance.** Describe the target project and the preparatory project
  as separate parts, and never let an activity appear in both.
- **Diagnostic for a broken boundary**: the same items show up as objectives in
  the target part and again as work packages in the preparatory part. In this
  draft, three "project objectives" in Part A were literally the first three
  items of Part B's list of preliminary work. The fix was to rename Part A's
  objectives as target-project objectives, move every preparatory bullet into
  Part B, and give Part B its own work packages.
- **Use a readiness table with one column per point in time.** Rows are the
  workstreams; columns are *today*, *at submission of the target proposal*, and
  *at the end of the preparatory grant*. A reviewer then sees in one glance what
  the money buys and where the follow-on begins. Define the readiness scale once
  (R1 argued from the literature, no artifact, through R5 running in the real
  setting without the research team present) and use it in every cell.
- **The funded period and the submission milestone are different dates.** An
  18-month grant that submits at month 12 has six months left afterwards; those
  months need stated content, and the column headed "at submission" must not be
  labelled as though it were the end of the grant.
- **State what the preparatory project deliberately does not deliver** (no
  clinical outcome, no certified device, no product; a measured readiness gain
  per workstream instead). It pre-empts the assumption of an over-claim and
  draws the boundary to the follow-on for free.
- **Name the decision the preparatory grant exists to settle.** If the scope of
  the target proposal is genuinely still open (one workstream, or all of them),
  say so and make the scope decision a dated deliverable with the evidence that
  will drive it. Uncertainty presented as a planned decision reads as
  competence; the same uncertainty left implicit reads as vagueness.

## 10. Verifying the funder's rules from primary sources

- **The agency's web pages are marketing; the rules are in the ordinance, the
  law, and the implementation provisions.** For Innosuisse the answers sat in
  the Beitragsverordnung (SR 420.231), the FIFG, and the agency's
  Vollzugsbestimmungen, none of which the overview pages summarize accurately.
  Budget an hour on the legal texts before writing the partner and budget
  sections.
- **Settle the structural questions first, because they can invert the design.**
  "Can our clinical partner receive money from this scheme?" decided whether an
  industrial partner was optional or mandatory, who could draw a salary, and
  which of two instruments to target. Answering it after the partner section was
  written meant rewriting that section twice.
- **Who is a partner and who receives money are different questions.** Many
  schemes pay only one class of participant. Putting an organisation in the
  wrong class silently defunds people the proposal names.
- **Check the independence rules between partner classes.** They constrain which
  named individuals may sit on which side, and therefore who can be paid.
- **Establish whether an eligibility question is scored or gating.** Recognition
  as an eligible research institution was decided inside the application itself,
  re-assessed each time, and a negative finding meant the application was not
  evaluated at all. A gating criterion deserves preparation effort out of all
  proportion to its word count.
- **Look for the agency's own published lists.** A list of institutions that had
  actually received contributions settled in one page what the legal definition
  left ambiguous: hospitals qualify, several of them non-university, and the
  applicant's own hospital was absent and would need first-time recognition.
- Agency PDFs frequently 403 or 404 against scripted fetches, and search-engine
  links to them are often stale. Take download URLs from the live page's own
  document list.

## 11. Writing for a mixed or non-expert panel

Interdisciplinary panels (here: clinicians, computer scientists, and a
research-funding office) punish the ordering a specialist would choose.

- **Order each background subsection by consequence, not by technology.** A
  subsection opening on foundation-model acronyms and speckle artefacts was
  reordered to lead with why the imaging method suits the patient, what goes
  wrong in practice, and how small the effect to be detected is. Only then the
  unfinished technical lines. Same content, different entry point.
- **Gloss each piece of jargon once, inline, in a clause.** "NFC, the
  short-range radio already familiar from contactless payment cards";
  "segmentation, outlining the nerve automatically in every frame". A
  parenthetical gloss costs a line and buys the paragraph.
- **Close each background subsection with one italic take-home sentence.**
  Reviewers skim; the sentence they land on should be the claim, not the last
  technical detail.
- **Answer "is this achievable?" explicitly**, by naming assets already in hand:
  annotated cohorts, a working sensor board, infrastructure already running.
  "The project advances assets in hand; it does not start three lines of work
  from zero."
- **Say what is tested, in what order, with what instrument.** "Characterize the
  system against reference instruments" says nothing. Naming the two things that
  change when a laboratory board becomes a wearable, and the measurement for
  each, turns an activity into evidence.
- **Distinguish welcome additions from dependencies.** For a collaboration not
  yet secured: "an addition we would welcome rather than one the project depends
  on: no work package rests on it". That removes a risk the reviewer would
  otherwise infer.
- **A team section reads as a credential list unless it opens with the division
  of labour.** One sentence naming what each side brings (clinic: the question,
  the patients, the reference data; university: the hardware, the algorithms,
  the study methods) reframes the same names as a working arrangement.
- **Anchor cost claims on one real number and keep the rest honestly bounded.** A
  quoted price for a hundred circuit boards supports both a per-unit estimate
  and a per-iteration budget line. An invented bill of materials would have
  looked more precise and been less defensible.

## 12. Editing the document programmatically

When the deliverable is a Word file the author also edits by hand, the tooling
constraints shape what is safe to attempt.

- **Without a renderer you cannot know the page count, so build a calibrated
  estimator and calibrate it against a number the author reads off their
  screen.** A characters-per-line and line-height model ran 12% high until the
  author reported the true figure; one constant fixed it and made every later
  trim decision quantitative rather than hopeful.
- **Table column widths must be set on both the grid and every cell.** In
  python-docx, `table.columns[i].width` writes the `tblGrid` entry and
  `cell.width` writes each `tcW`. Word reads the grid, so setting only cell
  widths silently does nothing.
- **Runs are fragmented, so never match against a single run's text.** Once
  tracked changes have been accepted, a sentence typically spans a dozen runs
  and a phrase can split mid-word. Operate on the paragraph's concatenated text,
  locate a character span, then rewrite only the runs overlapping it.
- **Table cells are not in `document.paragraphs`.** Every document-wide
  operation needs a separate pass over tables. A reference renumbering that
  skipped them left a citation pointing silently at four different papers.
- **Make edit scripts atomic.** Assert the expected number of matches before
  writing anything, so a failed assertion leaves the document untouched instead
  of half-edited.
- **Verify a global transformation by reconstruction, not by inspection.** For a
  renumbering: apply the mapping to the previously extracted text and require
  character-identical equality with the newly extracted text, then check that
  each reference entry's content moved as the mapping predicts.
- **Keep an extraction script that dumps paragraph text with highlight markers
  and table contents.** It is the only practical way to review a document you
  cannot open, and it doubles as the input to the reference and length checks.
- **Style ids are not style names.** In a German template the ids are
  ASCII-stripped ("berschrift2") while python-docx addresses styles by name
  ("Heading 2"); build on a copy of the original file so styles and section
  setup survive.
- Adding a footnote to a document that has never had one means building the part
  from scratch: content-type override, relationship, `footnotes.xml` with the
  separator entries, and the two footnote styles.


## 13. Splitting one project across several funders

One event, three applications, no shared cost line. The split is the work; the
prose is the easy part.

- **Derive the split from what each scheme forbids, not from what it allows.**
  The exclusions are sharper than the eligibility lists and rarely overlap. SNSF
  Scientific Exchanges pays travel and board for participants from abroad and
  excludes catering, venue, materials and speaker fees; the HSG Research
  Committee pays catering, occupancy and organisation and excludes honoraria,
  publication fees and social side events; the Swiss Informatics Foundation pays
  public outreach. Lay the exclusion lists side by side and the partition falls
  out with no line claimed twice.
- **Redefine the event boundary per application, and say so in each.** The SNSF
  application declares an event of 11-12 May, which keeps the public day of
  10 May outside its scope; the outreach application declares only 10 May. This
  is legitimate as long as each document states its own boundary and the
  boundaries do not overlap. It also protects against the "predominantly
  knowledge transfer" exclusion, since the hackathon and onboarding sessions sit
  outside the declared scientific event.
- **Disclose the parallel applications in every one of them.** Funders expect it,
  and a form with no field for it is not a reason to omit it: a sentence in the
  funding section does the job. Check each submitted form for this explicitly;
  it is the item most easily lost when a form is filled before its siblings
  exist.
- **Write the non-overlap rule down once, in a README next to the proposals, as a
  table of what is *not* requested and why.** During drafting the temptation to
  move a line into whichever application has headroom is constant, and the table
  is what stops it. Include the lines nobody funds, so that a rejection has a
  visible consequence rather than a silent one.
- **Sequence by decision date, not by deadline.** A foundation with two fixed
  rounds a year and a 90-day decision can have an earlier effective deadline
  than a scheme whose formal cut-off is months later, because the next round
  decides after the event. Compute, for each scheme, the last submission whose
  *decision* still lands before the money is needed.
- **A ceiling is a design constraint on the ask, not a target.** Where a scheme
  caps at CHF 15,000 and offers a separate CHF 500 lump sum for organisation,
  claiming both puts the total over the cap. Keep the request on one clean
  category and leave the rest at zero; the arithmetic then needs no explaining.
- **Ask for a fixed contribution rather than a per-head subsidy** when the
  headcount is still an estimate. It makes the request immune to the attendance
  number changing, and it tells the committee that the institution absorbs the
  variance.

## 14. Filling official forms

Most schemes are won or lost in prose, but the form is what gets rejected.

- **Get the real form before writing anything into a reconstruction of it.** A
  programme page may link only to a login-gated intranet; ask the applicant for
  the file rather than rebuilding the form from a sibling programme's version.
  Two forms in the same house style can differ in the one field that matters,
  and a form for a related instrument is not the form.
- **A confusing phrase on the public programme page is often the name of the
  fund, not a typo.** "max. CHF 15,000 je Forschungsgespräch" on a page about
  scientific events looked like a copy-paste error; it was the fund the
  programme is administered through. Resolve such oddities against the form, not
  against intuition.
- **Fill AcroForms by writing both the field value and an appearance stream.**
  Setting `/V` alone relies on the reader honouring `NeedAppearances`; many do
  not, and the applicant sees an empty form. Render the text into an `/AP` form
  XObject with the form's own `/Helv`, and set `/WinAnsiEncoding` on it, or
  every dash and umlaut comes out as the wrong glyph.
- **Auto-shrinking text to fit a box is a bug, not a feature.** If a field
  auto-sizes below about 7 pt, the answer is too long for the space the funder
  allotted; shorten it and move the detail to an attachment. Render the filled
  form to an image and look at it, because a field that reads fine in the
  extracted text can be unreadable on the page.
- **Radio groups are one field with several widgets.** Set `/V` on the field and
  `/AS` on each widget, using the export value the widget actually declares
  (`/Yes`, `/On`, or something else). Read the states out of `/AP /N` rather than
  assuming.
- **Field names are not the labels.** They may be the label text with spaces and
  punctuation stripped, truncated at an arbitrary length, or left as `Text1`.
  Dump the names, the rectangles and the flags before writing the filler, and
  make the filler report which of its answers it failed to place.
- **Read-only fields and tooltips masquerade as answerable fields.** A field with
  the read-only flag set and default text in it is the form's own note to the
  applicant. Leave it alone.
- **Do not keep a form-filling script alongside the filled form once the form has
  been edited by hand.** Two masters diverge silently, and re-running the script
  overwrites the newer document with older text. Either the script is
  regenerated from the current answers or it is deleted; the file that gets sent
  is the master.

## 15. Events, and what the money actually buys

Event schemes are judged on different criteria from research schemes, and the
persuasive core is usually financial rather than intellectual.

- **Name the thing the grant changes for participants.** A contribution towards
  catering is dull; the same contribution described as what allows the
  registration fee to come down, and a reduced-fee category to exist for
  students and for people from small companies and non-profits, is a decision
  the committee can feel the point of. Trace the money through to the person who
  benefits, and keep the chain short and arithmetically checkable (catering is a
  fixed cost of roughly CHF 100 per head; carried by the fee, it is the largest
  component of the fee).
- **Check that the argument is not the thing the scheme forbids.** The SNSF
  explicitly rejects applications that reduce fees for the participants it
  supports instead of reimbursing their costs. The same fee argument that wins
  the catering grant will sink the travel grant. Where the fact still belongs in
  the text, state it with the qualification attached in the same sentence: the
  category is funded from the event's own resources, and supported participants
  pay the ordinary fee.
- **A track record is worth more than a plan.** For a recurring event, the
  previous editions are the only evidence that is already fixed and verifiable.
  Give dates, hosts, submission and acceptance counts, the proceedings volume
  number, and the keynote speakers by name. This carries the feasibility and
  qualifications criteria on its own.
- **Write so the document survives the planning.** Commit only to what will hold
  (an open reviewed call, workshops in parallel, a published volume); give
  everything else as the current plan, with approximate counts, themes rather
  than a fixed line-up, months rather than dates, and partners described by kind
  until they are committed. The test is whether a changed workshop chair or a
  renamed track forces a revision.
- **Distinguish the public character from the scientific programme explicitly**
  when a scheme rewards the first and another scheme excludes it. Saying which
  day is which, and which application pays for it, answers two committees at
  once.

## 16. Keeping the source and the submission in step

- **Declare one master and say so in the file.** When a Markdown source feeds a
  filled .docx or a generated PDF, put a line at the top of the source naming
  which file is actually submitted and stating that changes have to be carried
  both ways. Without it, the version that gets sent is whichever one was touched
  last.
- **When you shorten for a page limit, check the sentences that count things.**
  Merging two of five research questions leaves "five questions" standing in
  three other places. Grep for the numeral after any structural edit.
- **Fill the official template rather than pasting into it.** Insert content
  after each section's answer placeholder, in the template's own paragraph and
  table styles, and delete the placeholder. Match the placeholder on the exact
  character the template uses; an en-space (U+2002) mistyped as a normal space
  matches the heading instead and deletes it, silently and plausibly.
- **The template's own italic question prompts are instructions, not content.**
  Deleting them is usually worth about a third of a page and costs nothing,
  provided the headings stay so the reviewer still sees the structure. Record
  the decision in the submission notes, with what to cut instead if the author
  wants them back.
- **Measure the page count with the template's real metrics.** Font, exact
  leading, text width and height are all in the file; on Windows or WSL the
  actual TTFs are usually available, and a wrapping model over them gets within
  a few percent. Report the number and the headroom, and say plainly that it is
  an estimate and not a Word render.
- **Keep a per-scheme submission-notes file** covering eligibility to confirm,
  the dates in the funder's own vocabulary, what has to be uploaded, the traps,
  and what is due after a grant. It is the file the applicant actually reads
  before opening the funder's portal, and it is where a trim order and a
  "do not cut" list belong.

## 17. Cutting to a character limit with the author

The SNSF limit is 60,000 characters including spaces and footnotes, with the
bibliography excluded, and 15 pages. The draft stood at about 71,300 characters;
a series of reviewed cuts brought it to about 61,100.

- **Measure what the funder counts, from the output, with one script.** Extract
  the PDF text (`pdftotext`), keep everything before the References heading,
  collapse whitespace, count. Run it after every change. The page limit and the
  character limit are separate checks: here the pages were met long before the
  characters.
- **Footnotes count, references do not.** Moving URL footnotes (protocol specs,
  product pages, other projects) into the bibliography saves characters at no
  cost to content. Ask before moving each kind: the author kept links to their
  own grants as footnotes, where a reviewer sees them on the page.
- **Check how new bibliography entries render.** Authorless `@misc` entries in
  the ACM style sort to the front of the list and print "[n. d.]". Decide whether
  that is acceptable before converting a dozen footnotes.
- **Repetition across sections is the cheapest cut.** Team roles restated in the
  team section, the schedule and every work-package intro; the same use-case
  example told in the introduction, the method and the impact section. Give each
  fact one home and point to it with a cross-reference.
- **Merge before you delete.** Two adjacent passages that make the same claim
  (Semantic Web and Web of Things in the background; two sentences in a section
  opening that both say "one model serves agents and humans") shrink more, and
  lose less, as one sentence. When the author asks "can this not be integrated
  better?", that is the answer they wanted for the next cut too.
- **Expected results are outputs, one line each.** Prose that re-describes the
  task under each result duplicates the task text.
- **Propose each cut separately, with before and after text and an estimated
  saving, and wait.** The author declined roughly one proposed cut in five and
  applied several more only in part ("yes, but keep the link to the project",
  "keep the 'based on WP2 and WP3'"). Batch application would have undone those
  decisions silently.
- **Offer options inside a proposal** (a/b/c, full or partial, with or without
  hedge). The author often picked a middle option that no single "apply?" would
  have produced.
- **Estimates run high; report the measured number.** Several savings came in at
  half the estimate once rebuilt. Say so in the next proposal and move on.
- **Keep the kept list.** Cuts the author declined are the reservoir for the last
  few hundred characters. Record each with its estimated saving so the endgame is
  a choice among known options, not a new search.
- **Keep deleted text in the source as a comment** (`% [cut: reason] <old text>`).
  It makes review and restoration trivial and costs nothing in the output.
- **Re-read the neighbours after a cut.** Removing an example sentence left "it"
  and "this agent" without an antecedent in the next sentence; removing a clause
  dropped the only citation of a paper. Check pronouns, cross-references and
  citation keys around every cut.
- **Rewrites during cutting are also fact checks.** Re-verify every number in a
  passage you touch against the primary source (a consortium partner count was
  wrong and was only caught because the sentence was being shortened).
- **Hedge statements about other projects' future outputs.** "Our first results
  should extend AFarEdge's final architecture specification" rather than "will
  extend": the author asked for the hedge, and the reviewer cannot hold the
  proposal to another consortium's schedule.
- **Commit after each tier of cuts**, so each batch can be reverted as a unit.

## 18. Co-editing a LaTeX source in turns

- **Pull before every session and look at what the author changed.** The author
  edits between sessions, sometimes in the very sentences under discussion.
- **Mark new text with a colour macro** (`\claude{}` rendering blue) and let the
  author untag after review. The author also writes instructions to the assistant
  inside the same macro; resolve and remove those first in each session. The
  author decides per change whether it is tagged; mechanical cuts were often
  applied untagged at their request.
- **Do not name a task or result before it is introduced.** A team section that
  says "carries T3.2" or "R3.1" makes the reader look ahead. Keep forward
  pointers at the work-package level, or say in the sentence what the result is.
- **Define staff shorthands once and use them everywhere** (DOC-COG, PD-TRANS,
  RA-HUD). Implement them as macros so a rename is one edit; grep for the full
  names afterwards.
- **A staffing change moves more than the budget.** Adding a second doctoral
  student fixed a gap in the schedule but changed the risk argument, the figure,
  the schedule text and every work-package staff line. List those places before
  agreeing to the change.
- **Check what a partner abroad may be paid for.** The author reported that the
  SNSF funds a research assistant or postdoc at a foreign partner but not a
  doctoral student; verify against the current regulations before relying on it.
- **Keep figures reproducible and expect them to lag.** TikZ sources with the
  render command in their header let the figure be regenerated after a plan
  change. After every structural change, check whether the figures still match
  the text; here they predated a whole use case.
- **Sort citations at package load.** natbib silently ignores `sort` when it is
  passed through `\setcitestyle`; it must be `\usepackage[numbers,sort&compress]{natbib}`.
  Check a multi-reference citation in the PDF afterwards.
- **Tie background sections back to the project goal.** A reviewer reading a long
  related-work section loses the thread. One sentence at the end of each
  subsection saying what it gives the project ("For the project's goal, the Web
  hence already provides...") keeps it, and is cheaper than cutting the section.
- **Text is also heard.** The author asked to have a section read aloud to judge
  how it sounded. There is no text-to-speech here; say so and offer a reading for
  sound (long noun stacks, stacked parentheses, sentences that restate the
  previous one) rather than improvising with the operating system's speech engine.
