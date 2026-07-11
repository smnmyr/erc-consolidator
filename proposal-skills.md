# Proposal-Writing Skills

General lessons about writing (research) grant proposals, distilled from drafting the
ERC Consolidator 2027 "islands" proposal (sources: SwissNCP CoG webinar, Giacomo
Indiveri's CoG-winner retrospective, official ERC documentation, and the drafting
process itself). Written to be reusable beyond ERC.

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
- Verify eligibility rules against the **current** call documents; rules change
  between calls (the ERC PhD window widened from 7–12 to 5–15 years for 2027; an
  older slide deck would have wrongly excluded the PI).

## 2. Lead with ambition; anchor it in a felt problem

- **Vision first, competence second.** The primary question at stage one is "is
  this a great idea worth pursuing?", not "can this person do it?". Indiveri's
  structure works: **WHY (vision) → HOW (methods) → WHAT (results) → WOW (impact)**.
- **Open with a sentence a non-expert remembers.** ("Every reference on today's
  Web is a bet that someone else will keep a promise they never made.") One
  crisp, quotable framing beats three paragraphs of context.
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
  cheapest to grep for.
