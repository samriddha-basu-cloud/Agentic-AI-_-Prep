# Ch 13 — Responsible AI: Closing the Loop (Session 20 + the course synthesis)
**Syllabus unit 9 📘:** *Ethical, Legal and Social Implications of AI in SCM — case law examples, AI bias in vendor selection, fairness audits.*
**Session 20 📘:** "Closing the Loop: Responsible AI as the Last Mile of Operations." It covers the course synthesis, a governance core, your season's post-incident review, and **how all twenty teams actually played Chain Reaction** (the season debrief).

> **Exam use:** the last part of almost every case answer. After you recommend an agent, show **who answers for it**: a named owner, an autonomy level, an audit log, proportional oversight, and a post-incident loop (**ACAP**).
> The ethics question in a case is usually **bias in the data foundation** (an under-represented market, region or supplier group), the **EU AI Act duty split** (provider vs deployer), or **"disclose now vs after the board meeting"**. The answer is always to **use the guardrail when it costs you something**.

---

## 1. Ten rounds, one system — what the course was actually teaching ⭐⭐⭐
1. **Autonomy ladder (L1–L5):** how many decision rights you hand an agent.
   - L1: inform. L2: recommend, a human approves. L3: act within bounds and escalate exceptions. L4: autonomous with monitoring. L5: fully autonomous.
2. **Guardrails live outside the model:** control sits in process and organisation design, not in the weights.
3. **Claim-audit discipline:** check turn by turn whether outputs deserved the autonomy given.
4. **AI–OR symbiosis:** agentic AI augments optimisation and human judgement and replaces neither.
5. **Data foundations before intelligence:** the constraint underneath everything else.

**Put together:** autonomy is **a dial you set deliberately**, and guardrails and audits keep it honest. The closing question is **who answers for it, and can you prove it?**

## 2. Class Q 10.1 (S20) — the bias found two days before the board ⭐⭐⭐
The situation:
- the forecasting agent has run at **L4** all season and outperformed manual;
- the training data **under-represents the fastest-growing regional market**;
- allocation has likely been skewed away from that market for months;
- the board review is in two days.

**Answer: C.** Drop the agent to **L2**, **disclose the bias and its likely impact in the incident log**, and bring both to the board **as a governance finding**.
- (A) "say nothing" and (D) "wait for the audit" protect the meeting, not the operation.
- (B) "quietly patch" hides the prior harm and breaks auditability.
- *Guardrails only count as guardrails if you use them when it costs you something.*

**Model write-up (assumptions format).**
1. *Assume* the skew lowered allocation to Region R by roughly x% for n months.
2. *Assume* lost sales can be estimated as the gap between R's demand trend and its allocation.

Then:
- **Act now:** step down to L2 (planner approves allocations).
- **Quantify:** estimate the lost sales and the margin forgone.
- **Fix the foundation:** re-weight or re-sample the training data, and add a fairness/representation check by region.
- **Disclose:** an incident log entry plus a board paper.
- **Re-promote** only after a holdout shows parity across regions.

## 3. Bias, sustainability, governance — the trio you answer for ⭐⭐⭐
- **Bias = an unrepresentative data foundation.**
  - Under-represented regions, suppliers, customer segments or time periods.
  - It shows up as **skewed allocation, unfair supplier scoring or vendor selection** (e.g. a supplier-risk model penalising small or minority-owned suppliers because they have thin histories), and as **service inequity** across zones.
- **Sustainability = the resource cost at scale.** The **energy and water footprint** of agentic platforms (flagged in S5) still applies: **scale amplifies both value and cost**. Count model compute alongside logistics CO₂ in design trade-offs (Ch 12's cost-vs-CO₂ frontier).
- **Governance = the structure that catches both before they become incidents.**
- **Legal floor: the EU AI Act.**
  - **High-risk obligations**: conformity assessment, **CE marking**, registration, and a duty split across **providers, importers, distributors and deployers**.
  - "As of this month" (the session date) **those obligations are now enforceable**.
  - The **provider** (who builds the system) owns conformity and technical documentation. The **deployer** (who uses it, e.g. Trishul) owns **human oversight**, use according to instructions, input-data relevance, monitoring and logging.
- **The maturity gap:** only **~20% of firms have governance mature enough for autonomous agents**, though most plan to deploy within two years. **That gap is where incidents live.**

### Bias-check numeric (exam style) 📗
A supplier-scoring agent shortlists suppliers.
- Large suppliers: 120 of 200 shortlisted (60%).
- Small suppliers: 30 of 100 (30%).
- **Selection-rate ratio = 30/60 = 0.5.** That is below the common **four-fifths (0.8) rule of thumb**, so it is a red flag.
- Check whether the gap is explained by legitimate performance (on-time %, quality) or by thin-history artefacts. If it is artefacts, adjust (e.g. Bayesian shrinkage for thin histories) and keep a human approver (L2) for small-supplier exclusions.

### Accountability in practice — a named precedent 📗
**Air Canada (2024):** a tribunal held the airline liable for its website chatbot's wrong refund-policy answer and rejected the argument that the bot was "a separate entity". **The deployer answers for what its agent says and does.** For operations, a procurement or customer-service agent's commitments bind the firm, so bound its authority (mandates) and log its actions.

## 4. The ACAP Governance Checklist — one last time (S20 version) ⭐⭐⭐ (framework)
| Check | Question |
|---|---|
| **Accountability** | Is there a **named human owner** for this agent's decisions, not just a team? |
| **Capability limits** | Is the agent's decision scope and autonomy level **explicitly bounded**, matching the ladder rung it operates at? |
| **Auditability** | Is there a **log detailed enough to reconstruct what the agent did and why**, after the fact? |
| **Proportionality** | Does the level of human oversight **scale with the real-world stakes** of the decision? |
| **Post-incident learning** | Does an incident **actually change the next deployment**, or just get filed and forgotten? |

(S19's design-time version reads Accountability, Capability boundaries, Alignment, Process oversight + Coordination mechanism; see [Ch 12](#/ch12-genai-design-multi-agent). In an exam, using either version is fine. Name the five checks and apply each one to the case.)

### Post-incident review template (Round 10 practicum) ⭐⭐
1. **What happened:** facts, timeline, the agent and its autonomy level.
2. **Impact:** ₹, service, trust/reputation.
3. **Root cause:** data, mandate, guardrail, coordination or human factors.
4. **Which guardrail fired, or should have.**
5. **Changes:** autonomy step-down or up, a new bound, a new trigger, a data fix.
6. **Owner and date for each change; verify at the next review.**

Write it honestly and check it against a real framework, every time.

## 5. The Chain Reaction season debrief — how 20 teams actually played ⭐⭐⭐
**Two axes decided the season:** how much AI capability a team **built** (live agents), and how well it **kept operating**. Four archetypes emerged.

| Archetype | Pattern | Examples (rank, value) |
|---|---|---|
| **1. Foundations without operations** (4 teams) | laid deep ground and never ran on it; "bought the platform, didn't operate the business" | A4-Sapiens (#20, 46: fill 92 → 69, **trust 61, last**); B19-Utkarshan (#19, 63; rail near zero); B16-nEYtra (#14, 118); B13-Kolirt (#11, 125; only 5 live agents, ran out of tokens in R10 and shelved builds) |
| **2. Transformation theatre** (7 teams) | **built the most on the least foundation; activity mistaken for outcome** | A1-Tankers (#18, 82; 12 agents, fill 65 → 77); B11-Dream11 (#17, 101; **third orchestrator build FAILED at 20% odds**, below gate); A5-Tokenizer (#16, 107; reputation 0.76); A6-Smooth Ops (#15, 111); B18-Promptplay (#13, 119; a **scheduling agent breached guardrails** in R10, reputation 0.75, the lowest); A10-Decepticons (#10, 132; five below-gate commissions, three build failures); B14-Six Sigma (#8, 153; clean ops but its **R10 orchestrator FAILED at 12% odds, below its D3·P3·T3 gate**) |
| **3. Lean operators** (3 teams) | minimal transformation, deep foundations, excellent execution; **capital-efficient but a lower ceiling and thin cover** | B20-Andromeda (#12, 122; **best reputation 0.92 on a single agent**, but zero governance estate, so trust 78); A9-Skynet (#5, 170); **A8-The Odyssey (#3, 191; 6 agents, all foundations at L5, trust >100, ₹1,181 cr cash)** |
| **4. Compounders** (6 teams) — **WON** | built capability **on foundations they had actually laid** and kept the business running | A3-OpsManiacs (#9, 148); B17-BLTB (#7, 159); B15-Neural 15 (#6, 166); A2-Doomsday (#4, 186; late miss of 338 cars auto-pushed to the nearest RDC); **A7-Kimi K3 (#2, 212; zero below-gate builds all season, rail every round, best cash ₹1,212 cr, highest trust 111; lost by 1.1 points)**; **B12-Titans (#1, 213, CHAMPION; widest estate, 21 agents, rail every round, trust held at 110 through every shock)** |

### What the season taught — the four lessons ⭐⭐⭐
1. **Sequence beats speed.** The top teams built **ON** foundations they had laid; the rest built agents faster than the **D·P·T ground** could support. **A below-gate agent runs at full cost and a fraction of the effect.**
2. **Building is not operating.** Size never predicted rank on its own: #3 ran 6 agents, #12 ran one, and four 12–13-agent estates finished 15th–18th. **Operating** the estate did predict rank: booking rail, filing a distribution plan, sizing the chip book to real demand.
3. **Governance is the multiplier you feel late.** **Company value = profit × reputation × trust.** The champion held trust at 110 through every shock. Teams that skipped the resilience and governance estate watched it collapse (B20 to 78, A4 to 61), and the multiplication did the rest.
4. **Efficiency is a real strategy.** A8 finished #3 on six agents, and B20 held top-tier service on one. Deep foundations amplify a tiny estate. **Lean works, provided you still buy the insurance.**

**Multiplier numeric.** Team X has profit index 200, reputation 0.80 and trust 0.90, so value = **144**. Team Y has a lower profit of 180 but reputation 0.92 and trust 1.10, so value = **182**. Y wins with 10% less profit, because **governance multiplies**.

## Key takeaways (S20 recap 📘)
1. **Autonomy is a dial you set on purpose**, not a default you inherit.
2. Guardrails and audits only matter **the moment they're inconvenient**. That is the whole test.
3. Governance gaps don't close themselves. The **20%-mature** number is a gap you'll be closing in your own career.
4. The habit that outlasts the course: **write the incident down honestly, and check it against a real framework, every time.**

---

## Self-test
**Q1. An allocation agent at L4 is found to under-serve rural zones because training data was urban-heavy. Give the five ACAP checks as they apply.**
- Accountability: the named owner (head of distribution).
- Capability limits: step down to L2 until the fix is made.
- Auditability: reconstruct the allocations from the logs and quantify the shortfall.
- Proportionality: rural allocation changes need human sign-off.
- Post-incident learning: add a representation test to the retraining pipeline before re-promotion.

**Q2. Under the EU AI Act, who owns human oversight when a firm uses a vendor's high-risk AI system?**
The **deployer** (the firm). It must use the system per instructions, assign competent human oversight, monitor it and keep logs. The **provider** owns conformity assessment, CE marking, registration and technical documentation.

**Q3. Why did "transformation theatre" teams score poorly despite building the most agents?**
They built below the foundation gates (full cost, a fraction of the effect, higher failure odds) and didn't operate the estate (rail, distribution plans, demand-sized chip book). Value = profit × reputation × trust, so failures and breaches hit the multipliers.

**Q4. What does "guardrails only count if you use them when it costs you something" mean in practice?**
When a guardrail fires at an inconvenient time (before a board meeting or quarter-end), you still step the agent down and disclose. Skipping it once turns governance into theatre.

**Q5. A supplier-selection agent shortlists 45% of large suppliers and 18% of small ones. Is there a bias concern?**
Ratio = 18/45 = 0.40, well below 0.8, so investigate. Check whether the gap comes from performance or from thin-history artefacts, fix it, and keep a human approver for exclusions.
