# Exam Q&A Bank — application questions with model answers
The exam has **no standalone theory**. Every question below is therefore phrased the way the paper phrases things: a situation, a number or a decision. Each answer is a compact model answer that uses the **Assumptions → Calculation → Framework → Verdict** pattern where a call is made. Turn on **Self-test** to hide the answers.

> Grouped by syllabus unit. For full-length solved papers see [Trishul](#/pyq-trishul), [Kaveri Motors](#/pyq-kaveri) and the [mock papers](#/practice-cases).

---

## Unit 1 — AI in Operations & SCM: claims, value pools, vocabulary

**Q1. A vendor claims its AI will cut your inventory 30%. Your inventory is ₹20 cr, of which ₹15 cr is cycle stock driven by full-truck ordering. Test the claim.**
- **Assumptions:** A1. Inventory = Q/2 + S = 15 + 5. A2. Order sizes are fixed by truck economics, so forecasting can't change Q.
- **Calculation:** the claim is 30% × 20 = ₹6 cr. But S = ₹5 cr, so even a perfect forecast removes at most **25%**. A realistic 25% σ cut removes about ₹1.25 cr (6.25%).
- **Framework:** Q vs S; Four-Question Claim Audit.
- **Verdict:** the claim fails arithmetically. Ask for the vendor's baseline business and holdout. Real inventory levers are order frequency and lead time.

**Q2. Distinguish predictive, generative and agentic AI using one procurement example each.**
- **Predictive:** a model scores supplier-delay risk for each PO.
- **Generative:** an LLM drafts an RFQ from a requisition.
- **Agentic:** an agent negotiates tail-spend terms and posts the PO within a manager-set mandate.

The tell is **goal ownership plus action on systems of record within an envelope**.

**Q3. "44% of firms already deploy supply-chain AI, so we are behind." How should a COO respond?**
Ask which adopters show measurable value and by what mechanism. Only about 30% move beyond copilots, and about 95% of GenAI pilots show no P&L impact. Adoption measures purchasing, not value. Fund mechanism-level cases with a baseline.

**Q4. Forecast error falls from ±40 to ±15, but you order in pallets of 240. What is the value?**
Near zero unless the better forecast changes the number of pallets ordered. Map predictions to decision thresholds before buying accuracy: precision pays only when a decision changes.

**Q5. Explain why Amazon's DeepFleet is "agentic" while the original Kiva robots were "automation".**
Kiva executes centrally assigned moves along floor markers. DeepFleet is a learned generative policy that coordinates a million robots' traffic toward a goal (−10% travel time), adapting continuously within a physical envelope.

## Unit 2 — Readiness: data, technology, process, organisation

**Q6. A firm scores [Data 2, Master data 1, Architecture 3, Security 2, Compute 5]. The CEO wants a purchasing agent with ERP write access in 3 months. Advise.**
- **Assumptions:** A1. Write access requires per-agent identity, scopes and logs. A2. Master data at 1 means duplicate vendors and items.
- **Verdict:** not yet.
  - Masters at 1 poison every downstream decision (duplicate vendors mean wrong concentration figures and payments to duplicates).
  - Security at 2 forbids write access.
  - Compute 5 is a stranded asset.
- **Plan:** a predictive pilot on the cleanest domain now, plus vendor-master dedup with a named owner, plus an API inventory. Gate write access on security ≥ 3 and master data ≥ 3.

**Q7. Which of the six data-quality dimensions binds for (a) real-time demand sensing, (b) spend concentration analysis, (c) a supplier-delay model?**
- (a) **Timeliness** (overnight batches kill real-time).
- (b) **Uniqueness** (duplicate vendor records split spend).
- (c) **Completeness/accuracy** of receipt dates and lead times, plus the leakage test (the feature must be known at decision time).

**Q8. Plants that ignored the AI tool avoided stockouts; plants that obeyed stocked out. What do you conclude and do?**
The model's data foundation is missing something (at Continental Parts, the 15% of demand arriving by phone). The rebels were right. Capture the missing channel, re-baseline, allow bounded overrides with reasons (±15%), and gate scaling on a frozen baseline. Don't punish overrides; mine them.

**Q9. Rewrite "25% inventory reduction in 6 months, company-wide" into a gate-compatible target.**
"In the pilot region (2 DCs, top 300 SKUs), reduce safety stock ≥ 10% vs the frozen Q1 baseline **while keeping weighted fill ≥ 95%** (counter-metric), measured against a control region at month 4. Scale to Phase 2 only if both hold." It is scoped, baselined, has a counter-metric and is evidence-gated.

**Q10. Why does adding "recommendation adherence" to planners' KPIs backfire?**
A measure that becomes a target stops measuring: planners will follow the tool even when they know it's wrong, which hides the cases where human judgement mattered. Align incentives with outcomes (service, turns, forecast value added, quality of exception handling), not with compliance.

## Unit 2b — Agentic systems and platforms

**Q11. Design the autonomy level and guardrails for an agent that reorders MRO consumables under ₹50,000.**
- **Level:** L3, acting within bounds and escalating exceptions. The decision is frequent, reversible and low-stakes, with fast feedback.
- **Guardrails (outside the model):** per-order ₹ cap and monthly spend cap **in code**; approved-supplier list enforced by the system; anomaly triggers (price > +10% vs last, quantity > 2× average) escalate to the buyer; full action log; a named owner (category manager); monthly review with a demote trigger.

**Q12. Score three use cases on the agentic suitability screen: strategic supplier negotiation, tail-spend reorders, warehouse robot routing.**
- **Robot routing** scores highest (20+): very high frequency, reversible, rich feedback, clear rules, own premises.
- **Tail-spend reorders** come next (12–19): frequent, moderate stakes, so L3.
- **Strategic negotiation** is lowest (< 12): rare, high stakes, ambiguous rules, so human-led with AI input.

**Q13. A feature-rich, cheaper platform can't enforce per-agent spend caps or full logs. Your roadmap has an L4 procurement agent. Decide.**
Disqualify it. In the six-filter order, governance comes before features and price. At L4, a governance gap is unbounded financial exposure.

**Q14. Copilot token spend is 3.2× forecast. Does that make the platform choice wrong?**
No. It is a usage-governance (FinOps) problem: per-team budgets, caps in code, caching, model tiering, quarterly review. Revisit the platform only if governed consumption still breaks the business case.

**Q15. When should an operations firm build rather than buy its AI platform?**
Only where the capability is the firm's real differentiation and the firm has unified data and engineering depth. Otherwise **own the differentiating loop, rent the rest**, and check whether a commodity service already exists (OCR, classification).

## Unit 3 — ML, forecasting, inventory, maintenance

**Q16. "Our demand model is 92% accurate." Naive scores 90.5%, and orders come in full-truck multiples. Verdict?**
Unproven. It barely beats naive and may not change any truck-level order. Report accuracy against naive on an honest time-based holdout, at decision granularity, and price the decisions changed.

**Q17. A model wins on staples but loses on promotions and new items. Deploy?**
Deploy by segment: the model on staples, naive or incumbent on promotions and new items (champion–challenger). Revisit the map quarterly.

**Q18. SKU A: mean 1,000, σ 50. SKU B: mean 1,000, σ 400. L = 1 week, 95% service. Safety stock for each, and what is wrong with a "2 weeks of supply" rule?**
- SS(A) = 1.645 × 50 ≈ **82**. SS(B) = 1.645 × 400 ≈ **658**.
- "2 weeks of supply" gives both 2,000 units of buffer: it massively overstocks A and is still a blunt instrument for B.
- Forecast the distribution; the quantile is the decision.

**Q19. Nandini (monsoon drives 40% of variance) is offered weather data. Apply the signal audit.**
1. **Lead time:** does the forecast horizon (e.g. 2–3 weeks) cover the bottling and dispatch lead time?
2. **Mechanism:** heat and rain drive consumption, which is honest.
3. **Decision test:** does it change production or dispatch in the monsoon-transition weeks where fill fails?
4. **Cost vs value:** subscription plus integration vs stockouts avoided in those weeks.
5. **Weight check:** after a season, keep it only if the model learned material weight.

**Q20. A forecasting vendor says its agent "adjusts in real time with zero planner effort". What do you ask, and why?**
"Does it update forecasts, or execute orders?" Updating is a feature to bake off. Executing is an autonomy grant needing the ladder, bounds, fallback, owner and readiness.

**Q21. Trident: 8,000 SKU-locations weekly, two analysts (one knows some Python), readiness [3,2,3,3,3], ₹25 L. Which forecasting tier?**
- **Tier 2 (Prophet-class), scripted and scheduled**, with the spreadsheet as benchmark and fallback.
- Cloud AutoML assumes a governed platform (T ≥ 3.5), data engineering and FinOps. LSTM needs Data Maturity 3+ and long histories.
- **Flip condition:** T ≥ 3.5, a data engineer, volumes in the tens of thousands, and a bake-off showing decision value that covers the cost.

**Q22. A DRL vendor claims 20% lower spare-parts inventory vs your tuned basestock (89% fill) "in our backtest". Respond as COO.**
- **Assumptions:** A1. A tuned basestock or myopic policy is within about 5% of optimal. A2. Demand is intermittent.
- **Analysis:** 20% exceeds the headroom, so it is likely a weak baseline or overfitting. Four weeks of shadow mode is statistically empty.
- **Decision:** fund a **guardrailed pilot**:
  - scope: one parts family for 2 quarters;
  - bounds: incumbent floors and ceilings plus a spend cap;
  - fallback: auto-revert if fill < 87% for 2 weeks;
  - evaluation: matched control, service per rupee;
  - trust loop: overrides with reasons;
  - owners: named.

**Q23. Planners override 30% of the system's recommendations. Problem or information?**
Information. Log the reasons, test which overrides beat the system, feed them into retraining, and keep a bounded override band. Banning overrides breeds shadow spreadsheets (Continental Parts).

**Q24. Why is improving forecast accuracy often worth less than replacing the weeks-of-supply rule?**
The value dies in the conversion step: multiple distorted forecasts get turned into stock by crude rules. A policy optimised on the demand distribution and the cost structure attacks the leak directly. Optimise the policy, not the forecast.

**Q25. A compressor fails twice a year at ₹31 L per failure; PdM would catch 70% and cost ₹22 L plus ₹5 L/yr; a planned repair costs ₹7 L. Fund it?**
- Today: 2 × 31 = ₹62 L/yr.
- With PdM: 1.4 × 7 + 0.6 × 31 = 9.8 + 18.6 = ₹28.4 L.
- Saving ₹33.6 L; net of running cost ₹28.6 L/yr; **payback ≈ 0.8 yr**.
- Twin test: it changes the decision (yes), failure cost is high (yes), instrumentation must be built, and asset-level fidelity suffices. **Twin-now.**

**Q26. When should you NOT act on a high failure-probability flag?**
When the existing protocol already catches the failure in time (e.g. weekly inspect-and-replace). The prediction doesn't change the decision or its timing, so it is informationally idle.

## Unit 4 — Logistics, optimisation, procurement NLP, token economics

**Q27. A lane loses 40% capacity before a festival; the premium zone needs 2,000 cars, 800 within 3 days. Express ₹9,000/car, road ₹4,000, rail ₹3,000 with a 6-day lead; road can carry 500 in 3 days. Plan it.**
- Urgent 800: road 500 = ₹20 L, plus express 300 = ₹27 L.
- Remaining 1,200 by rail = ₹36 L.
- **Total ₹83 L**, vs all express 2,000 × 9,000 = **₹180 L**, a saving of ₹97 L (54%).
- **Framework:** split shipment; the mode mix under capacity.

**Q28. Your optimiser used identical cost weights and starved the premium zone. Fix it with the Optimizer Mandate Checklist.**
1. **Service targets per zone** (premium ≥ 95%).
2. **Cost weights** = a lost-sales penalty equal to unit contribution.
3. **Review rule:** L3 with exception escalation.
4. **Re-solve triggers:** > 20% capacity loss, a forecast floor breach, demand spike > 25%.
5. **Verify the plan against the floors before execution.**

The solver was right for the objective; the objective was wrong.

**Q29. Write a Mandate Card for a distribution agent in a 3-plant, 4-RDC, 7-zone network.**
- **Service floor:** zones 1–3 (premium) ≥ 95%; others ≥ 88%.
- **Cost ceiling:** ₹/car by mode.
- **Mode priority:** rail for base load (once MIX is unlocked), road default, express only for stockout risk.
- **Shock trigger:** a lane capacity loss > 20% or a zone forecast below its floor forces a full re-plan; smaller deviations get a local patch.
- **Review cadence:** weekly human review of zone fill vs cost; monthly mandate review.

**Q30. Why is "agents operate optimisers, they don't replace them" the right design (AI–OR symbiosis)?**
The solver does the constrained math optimally for one snapshot. The agent senses when to re-solve, translates goals into weights and constraints, and governs execution (L2/L3/L4). JD.com's dual engine is the model. Neither layer works alone.

**Q31. Your procurement NLP system extracts payment terms, addresses, penalty clauses and contacts. Where do you put the accuracy budget and the human?**
On penalty, liability and indemnity clauses: a domain-tuned model (94.7% vs 79.3% for general LLMs), high recall, and a human always reviewing. Interpretation of those clauses is never fully automated. Contacts and addresses can use a general model.

**Q32. Walmart–Pactum negotiates with thousands of suppliers. What is the category manager's job now?**
Designing the envelope (tradable levers, walk-away limits, escalation triggers) and auditing outcomes. Not reviewing every deal, which would destroy the economics. The mandate is the management.

**Q33. An agent costs ₹5 L/month for 2,500 decisions; each decision saves about ₹150. Tune or retire?**
- Cost per decision = ₹200 vs value ₹150, a ratio of 0.75×.
- **Tune first:** cache, shorten context, batch, use a cheaper tier, call less often.
- If cost falls below about ₹120 per decision, keep it. If not, **retire** to the next-best process. Enforce the spend cap in code.

**Q34. A procurement pilot shows 25% staff-efficiency gains, but the CFO sees no P&L change. Explain and fix.**
This is the efficiency-capture gap (McKinsey: 20–30% efficiency, only 1–3% captured). Freed time wasn't redeployed and savings weren't banked. Fix it with a capture plan: redeploy freed hours to strategic sourcing, bake negotiated savings into budgets, and track realised ₹ against run cost monthly.

## Unit 5 — GenAI design, multi-agent, responsible AI

**Q35. GenAI produced 30 disruption scenarios for your network redesign. How do you turn them into a design decision?**
Apply the Scenario Portfolio Checklist:
1. **Generate wide.**
2. **Label** each plausible, stretch or implausible by mechanism and precedent.
3. **Select two to survive** (one plausible, one high-impact stretch).
4. **Specify the capability and its cost** (flex capacity, dual sourcing, buffer).
5. **Guard the label:** name the mechanism before committing capital.

Then run a multi-objective optimiser (cost vs CO₂) across the scenarios: GenAI for range, OR for rigour.

**Q36. What is the collaboration paradox, and which design fixes it?**
Smarter individual agents with no coordination make system-wide oscillation (bullwhip) worse, because they overreact to each other's orders faster. The fixes:
- a **shared end-customer demand signal**;
- **rate limits and order smoothing**;
- **trained coordination or consensus-seeking orchestration**.

Jointly trained agents beat both central and uncoordinated agents on cost and variability (POM 2025).

**Q37. Retail demand variance is 250, wholesaler orders 600, factory orders 1,800. Compute the bullwhip and recommend.**
- Ratios: 2.4 and 3.0, a total of **7.2×**.
- Share POS data with every tier and agent, smooth orders (e.g. ±10% per week), reduce batching, and name one owner of the shared plan.

**Q38. Apply ACAP to a credit-limit agent running at L4 for dealers.**
- **Accountability:** a named owner (Head of Credit).
- **Capability limits:** L4 only within ±20% of the prior limit; anything larger goes to L2 approval.
- **Auditability:** every decision is logged with its features and reasons.
- **Proportionality:** a human reviews limit cuts for dealers with more than ₹X outstanding.
- **Post-incident learning:** each wrongful cut triggers a review and model update.

**Q39. Under the EU AI Act, your vendor says "compliance is handled by the platform". What is still yours?**
The deployer duties: use the system per its instructions, assign competent **human oversight** (often meaning L2 for high-risk decisions), check input-data relevance, monitor it, keep logs and report incidents. The provider owns conformity assessment, CE marking, registration and documentation. Write the duty split into the contract.

**Q40. Two days before the board, you discover your L4 forecasting agent's data under-represents your fastest-growing region. What do you do?**
- Step it down to **L2**.
- Log the incident.
- Quantify the likely allocation skew and lost sales.
- **Disclose it to the board as a governance finding.**
- Fix the data (re-weighting, representation checks), test for parity on a holdout, then re-promote.

Guardrails only count when you use them when it costs you something.

## Chain Reaction — strategy questions

**Q41. Your team wants to build an orchestrator with gate D3·P3·T3; you are at D2·P3·T2. Advise.**
Don't build yet. A below-gate build runs at full cost for a fraction of the effect, with cut odds (B14's orchestrator failed at 12%, B11's at 20%). Raise Tech to 3 first, which also unlocks MIX (rail), then Data. **Sequence beats speed** (A7-Kimi K3: zero below-gate builds, #2).

**Q42. Why did "transformation theatre" teams with 12–13 agents finish 15th–18th while A8 finished 3rd on six agents?**
**Building is not operating.** Theatre teams built below gate and didn't run the estate (rail, distribution plans, a right-sized chip book), so failures and breaches hit reputation and trust. A8 had all foundations at L5, so a small estate was amplified. Value = profit × reputation × trust.

**Q43. Kaveri lost money in a congestion month and blamed bad luck. Give the physics explanation.**
Unrouted plant stock auto-pushes to the home RDC by road, and zones pull only from their own region's RDC. With no rail booked and no distribution plan, stock piled near the plants while distant premium zones stocked out. The congestion charge was the visible cost; the **contribution forgone** on unfilled premium demand (₹11 cr) was the real one. Fix: a Distribution Planning Agent under a mandate, with a rail floor. See [Kaveri](#/pyq-kaveri).

**Q44. You have 24 tokens. Upkeep is 9; you generate one plan and regenerate twice. How many tokens remain, and what discipline follows?**
9 + 2 + 2 = 13, so **11 remain**. Regenerate only on a real trigger. Retire agents whose value per token is lowest (termination costs 2 and saves their upkeep from the next month). Never leave a gate-raising action unfunded for a low-value agent.

**Q45. What four lessons did the faculty draw from the season?**
1. Sequence beats speed (build on the D·P·T foundations you have laid).
2. Building is not operating (book rail, file distribution plans, size the chip book to real demand).
3. Governance is the multiplier you feel late (value = profit × reputation × trust).
4. Efficiency is a real strategy (lean works if you still buy the insurance).
