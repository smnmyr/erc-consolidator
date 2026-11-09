# B2 Section 5 before contingency strategies were added (2026-11-09)

## Section 5 — Risk assessment and mitigation (~1 page)

| # | Risk | L | I | Mitigation |
|---|---|---|---|---|
| R1 | Coordination cost exceeds what islands of realistic size can sustain, so the top link classes are unreachable in practice | M | H | WP2 can return "not attainable" as a result, so this outcome is itself a finding. The lattice degrades gracefully: a negative result at the top rung still yields a validated boundary of attainable bundles, which is publishable. T4.1's coordination instrumentation detects the problem early, at I1. |
| R2 | SMPC resolution latency stays too high for interactive use | M | H | The deliverable is the privacy-performance frontier (D4.3), so the result stands either way. Asynchronous and precomputed-randomness designs (T4.2 ii), using the preprocessing model of SPDZ/MP-SPDZ, are the primary mitigation; Island S's batch workloads remain viable even if interactive resolution does not. |
| R3 | The malicious-secure arc does not close within budget | M | M | The arc has intermediate publishable states (static, then adaptive adversary). Honest-but-curious results (D4.2) already go beyond the deployed state of the art and stand alone. |
| R4 | **Purpose binding is not technically enforceable after resolution** | H | M | We accept this by design. WP2 scores the guarantee by the margin by which re-requesting is less costly than hoarding, and documents the class as an economic guarantee, the mechanism on which transcopyright and current data-economy proposals both rely. The failure mode is a guarantee that the theory declines to promise for a given actor, which the calculus can express. |
| R5 | Loss of a validation site (editorial partner withdraws; industrial partner reorganizes) | M | H | Four islands in unrelated sectors with separate partners, so no single withdrawal ends WP5. Island L has alternative corpora (law journal, moot-court record, and the *Access to Justice* corpus) **[TODO: secure a written second option]**. Island S sits inside a running deployment. |
| R6 | The agent-layer comparison returns a negative or null result | M | L | Pre-registered hypothesis and analysis plan. We expect a null result on task success with a positive result on safety and evolvability, which is publishable; the evaluation is informative in either direction. |
| R7 | The applied-cryptography postdoc cannot be recruited (hardest profile) | M | H | The search opens at the Step 2 result (scheduled for 17 December 2027), about four months before M1, and is international: an ERC grant attracts applicants worldwide, and we advertise at the cryptography and security venues (e.g., the IACR job board, CRYPTO, Eurocrypt, ACM CCS) and through the networks of Mitrokotsa and Cheng. Grau's SMPC expertise covers T4.2's first arc regardless. Fallback: two PhD positions with more advisory time from Mitrokotsa and Cheng. |
| R8 | Standardization uptake does not materialize | M | M | The W3C groups are named per work package (§1), and the PI's specifications have reached shipped products before (WoT TDs). The reference implementation and artifacts stand on their own, independent of adoption. |
| R9 | Legal exposure from the Island L corpus (personal data in citations) | L | M | Retraction is designed in as a superseding record, which reconciles immutability with GDPR Art. 17; DPIA at island scoping; legal partner embedded in WP5 **[TODO: confirm USG ethics/DPIA route]**. |
| R10 | WP1 finds that society requires islands beyond the five drafts, or that a draft is not required | M | M | The account and the decision record are revised annually by design, and WP2's calculus is stated over NFP bundles, not over the five drafts. A dropped draft is recorded in the decision record with its reason, which is itself a result. |
| R11 | Some NFPs cannot be translated at a border without loss | H | L | This is an expected outcome: WP3 records such entries as refusals or visible downgrades, and the visibility rule ensures that no reference loses a guarantee silently. The table of untranslatable entries bounds what islands can promise across borders. |

In R1, R4, R6, and R11 the likely failure is a bounded negative
result, and we design each work package to deliver that result as a
finding, as fits a project whose core contribution is a theory of what
is attainable.

