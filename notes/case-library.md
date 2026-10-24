# Case Library — every course case, resolved in one line and in depth
Every session opened with a case, and the exam is **"a comprehensive, application-based case study covering all concepts"**. This page lets you revise all of them in one sitting. For each case you get the **facts**, the **trap**, the **framework that cracks it** and the **resolution** in exam language. Named real-world deployments and failures follow, as **evidence to cite** in your answers.

> **How to use:** when a new exam case arrives, find the course case it most resembles in the table below and reuse that case's framework and structure. Most exam cases are recombinations of these.

---

## Quick map — case → trap → framework
| # | Case (session) | The trap | Framework that cracks it | Chapter |
|---|---|---|---|---|
| 1 | **NorthStar Foods** (S1) | "better forecasting" proposed when stock is order-size driven | **Q vs S**; Four-Question Claim Audit | [Ch 1](#/ch01-ai-in-operations-and-scm) |
| 2 | **Meridian Apparel** (S2) | AI pilot on dirty, late, siloed data | **Six data-quality dimensions**; **five-pillar readiness scorecard** | [Ch 2](#/ch02-ai-readiness-data-technology) |
| 3 | **Continental Parts** (S3) | model ignores phone orders; an ambitious board-deck target; plants that obeyed stocked out | **Phased roadmap with gates**; pilot-selection matrix; trust design | [Ch 3](#/ch03-ai-readiness-process-organisation) |
| 4 | **Vantage Logistics** (S4) | scaling the pilot with the biggest % gain | **Autonomy ladder**; **agentic suitability screen**; omitted objectives | [Ch 4](#/ch04-agentic-ai-systems) |
| 5 | **Solstice Industrials** (S5) | choosing a platform from a demo under GPU scarcity | **Six platform filters**; build/buy/blend | [Ch 5](#/ch05-ai-platforms) |
| 6 | **SuryaMart** (S6) | "92% accuracy in the PoC" | **ML Framing Canvas**; naive benchmark | [Ch 6](#/ch06-machine-learning-for-operations) |
| 7 | **Meghna Foods** (S7) | a 94% notebook only one analyst can run | **Seven-step workflow**; capability checklist | [Ch 6](#/ch06-machine-learning-for-operations) |
| 8 | **Nandini Beverages** (S8) | buying the "autonomous agent" pitch | **Signal audit**; update vs execute; distribution forecasting | [Ch 7](#/ch07-demand-forecasting) |
| 9 | **Trident Distributors** (S9/S12) | MD wants "what the big retailers have" | **Tier matching / bake-off ladder** | [Ch 7](#/ch07-demand-forecasting) |
| 10 | **Krishna AgroMachinery** (S10) | "20% better in our backtest" | **Benchmark ceiling (~5%)**; **guardrailed pilot** | [Ch 8](#/ch08-inventory-optimisation) |
| 11 | **Bearing / telemetry call** (S13) | acting on a prediction that changes nothing | **Twin-now / twin-later test** | [Ch 9](#/ch09-predictive-maintenance-digital-twins) |
| 12 | **Capacity shock / LP mandate** (S14–15) | single-mode answer; cost-only objective | **Split shipment**; **Mandate Card**; Optimizer Mandate Checklist | [Ch 10](#/ch10-logistics-routing-optimisation) |
| 13 | **Clause budget / chip contract** (S16) | one accuracy bar for all clauses | **Clause-stakes checklist** | [Ch 11](#/ch11-nlp-procurement-token-economics) |
| 14 | **Repriced agent** (S17) | retire or ignore by reflex | **Tune-or-retire** | [Ch 11](#/ch11-nlp-procurement-token-economics) |
| 15 | **Paint-colour scenario** (S18) | vivid = likely | **Scenario portfolio checklist** | [Ch 12](#/ch12-genai-design-multi-agent) |
| 16 | **Command Your Agent bullwhip** (S19) | smart agents reacting to orders | **Shared signal, smoothing, trained coordination; ACAP** | [Ch 12](#/ch12-genai-design-multi-agent) |
| 17 | **Bias before the board** (S20) | hide it until after the meeting | **ACAP**; step down and disclose | [Ch 13](#/ch13-responsible-ai-ethics) |
| PYQ | **Trishul Consumer Products** | vendor % claims, data defects, procurement agent | Claim audit; Q vs S; data triage; autonomy + mandate | [Trishul](#/pyq-trishul) |
| PYQ | **Kaveri Motors** | averages hiding trends, cherry-picked months, physics read as luck | Claim audit; contribution arithmetic; Mandate Card | [Kaveri](#/pyq-kaveri) |

---

## 1. NorthStar Foods — Forecasting fix or something else? (S1) ⭐⭐⭐
- **Facts:** high inventory. Two proposals: an **ML forecasting upgrade** or a **lead-time/order-frequency initiative**. Finance says order-size-driven stock costs **about 4× the uncertainty buffer**.
- **Trap:** assuming that better forecasting cuts all inventory.
- **Framework:** **Q vs S**. Inventory = cycle stock (Q/2, set by batch size and order frequency) + safety stock (z·σ·√L, set by uncertainty and lead time). **Forecasting attacks S only**; lead-time and order-frequency work attacks **both Q and S**.
- **Resolution:**
  - Q ≈ 4 × S, so even a perfect forecast (S → 0) removes only about 20% of inventory.
  - **Fund the lead-time/frequency initiative first.**
  - Pilot forecasting later on volatile SKUs.
- **Numeric:** total inventory ₹50 cr with Q-part ₹40 cr and S-part ₹10 cr.
  - A 30% better forecast gives about −₹3 cr.
  - Halving the order size gives −₹20 cr (Q/2 halves).
  - Halving the lead time cuts S by about 29% (1 − 1/√2), i.e. −₹2.9 cr, on top.

## 2. Meridian Apparel — Are we ready for AI? (S2) ⭐⭐⭐
- **Facts:**
  - The CEO wants a **Zara-style trend-detection pilot now**.
  - Problems: duplicate SKUs, **24-hour data latency**, no GPU budget, an unknown API inventory.
  - The **e-commerce division is clean and API-first**.
- **Trap:** a company-wide AI launch on a broken foundation.
- **Framework:** **six data-quality dimensions** (accuracy, completeness, consistency, timeliness, uniqueness, validity) and the **five-pillar readiness scorecard** (Data, Technology, Process, Organisation, Governance; 1–5 each).
- **Resolution:**
  - Not ready company-wide (uniqueness and timeliness fail, and trend detection needs freshness).
  - **Pilot in the clean e-commerce division** where data is ready.
  - In parallel, run SKU master-data dedup and a latency fix as gates.
  - Spend first on foundations, not GPUs.

## 3. Continental Parts — The roadmap rebellion (S3) ⭐⭐⭐
- **Facts:**
  - **Plants 1–2 ignored** the forecasting tool and avoided stockouts.
  - **Plants 3–4 obeyed**, cut inventory and **stocked out**.
  - The model **missed 15% of demand that arrives by phone**.
  - A **25%-in-six-months** target was set for a board deck.
- **Trap:** blaming the "rebels"; pushing harder for compliance.
- **Framework:** the **phased roadmap with gates and frozen baselines**; **trust design** (overrides are information); process standardisation before automation.
- **Resolution:**
  - The rebels were right: the model's data foundation omitted the phone channel.
  - Capture phone orders, re-baseline, and **reset the target** to an evidence-based gate.
  - Run a bounded-override pilot with reason capture.
  - Scale only after gate metrics hold on a **frozen baseline vs control**.
- **Recurring callback:** "a planner asked to follow unexplainable order quantities re-runs Continental Parts" (S10).

## 4. Vantage Logistics — Which pilot do you scale? (S4) ⭐⭐⭐
- **Facts:**
  - **routing agent +14%**, with driver-safety concerns;
  - **picking robots +18%**, with a hardware backlog;
  - **delay rebooking +6%**, with the highest satisfaction.
- **Trap:** scaling the biggest number.
- **Framework:** the **autonomy ladder L1–L5**, the **agentic suitability screen** (20+ / 12–19 / <12), and "**agents fail on what their objective omits**".
- **Resolution:**
  - **Scale delay rebooking**: low blast radius, reversible, users like it.
  - Fix the routing agent's objective (add safety constraints) before promoting it.
  - Robots are hardware-constrained, so scaling them is a capex timing decision.
  - Before promoting any pilot, ask for the overridden cases, error costs in both directions, the omitted objectives and a frozen baseline.

## 5. Solstice Industrials — Platform choice under constraint (S5) ⭐⭐
- **Facts:**
  - The estate is **Microsoft-centric**.
  - **AWS offers a faster pre-built pilot**.
  - A **GPU shortage delays either choice by a quarter**.
  - The sustainability office asks about emissions.
- **Trap:** deciding from the feature demo, or because of the delay.
- **Framework:** the **six platform filters**, applied in order (use-case fit, data gravity, skills, governance fit, TCO including tokens, exit/lock-in), plus **build/buy/blend**.
- **Resolution:**
  - Data gravity and skills favour Azure.
  - Demand governance evidence from both vendors (per-agent identity, spend caps, logs).
  - The GPU delay changes the **plan**, not the **decision**: sequence low-compute predictive pilots first.
  - Ask for region carbon intensity and PUE.
  - Negotiate exit terms.

## 6. SuryaMart — Three ML pitches, one budget (S6) ⭐⭐
- **Facts:**
  - A: forecasting for 40,000 SKUs.
  - B: customer segmentation.
  - C: supplier-delay early warning.
  - "92% accuracy in the PoC".
- **Framework:** the **ML Framing Canvas** (decision, target, data, error costs, baseline).
- **Resolution:**
  - **Fund C first**: clear owner, fast feedback, priced asymmetric cost.
  - Reshape A with tier matching and a naive benchmark.
  - B needs a decision (what changes per segment?) before it can be validated.

## 7. Meghna Foods — The 94% notebook (S7) ⭐⭐
- **Facts:** only the analyst can run it, from CSVs on her laptop.
- **Framework:** the **seven-step workflow** and the **capability checklist** (reproducible, monitored, owned, fallback, versioned, permissions and logging).
- **Resolution:**
  - Dig, then delay.
  - The 94% needs a naive benchmark, a time-based holdout and evaluation at decision granularity.
  - Production breaks first on the **bus factor** and manual CSV exports.
  - "Done" = a scheduled pipeline feeding planning by cut-off, monitored, owned, with a fallback.

## 8. Nandini Beverages — Three forecasting pitches before the monsoon (S8) ⭐⭐⭐
- **Facts:**
  - **A**: statistical, ₹40 L. **B**: ML + weather/IoT sensing, ₹1.4 cr. **C**: "autonomous agent", ₹2.1 cr.
  - Sales inflates and planning deflates.
  - The **monsoon drives 40% of variance**.
  - Failures cluster in **promo and monsoon-transition weeks**.
- **Resolution:**
  - **Sequence A → targeted B**: benchmark, repair promo history, set a single consensus number, then audit and pilot weather/promo signals on the failing weeks with distribution forecasts.
  - Ask C "**update or execute?**".
  - None of the pitches fixes the incentive politics; that needs architecture and transparency.
  - Full answer in [Ch 7 §8](#/ch07-demand-forecasting).

## 9. Trident Distributors — Which tier fits? (S9, S12) ⭐⭐⭐
- **Facts:**
  - **8,000 SKU-locations**, ordered weekly;
  - 2 analysts (one knows a little Python);
  - readiness **[3,2,3,3,3]**;
  - **₹25 L** budget;
  - the MD saw a cloud demo;
  - 8-year spreadsheet incumbent.
- **Resolution:**
  - **Tier 2 (Prophet-class), scripted**, with the spreadsheet as benchmark and fallback.
  - It must beat the analyst's forecasts on a holdout, per segment, and prove it to the analyst and the MD.
  - Cloud becomes right when T ≥ 3.5, a data engineer is in place, volume is in the tens of thousands and the bake-off uplift pays for 6× the cost.

## 10. Krishna AgroMachinery — The 20% claim (S10) ⭐⭐⭐
- **Facts:**
  - DRL vendor claims **−20% inventory** vs basestock "in our backtest";
  - intermittent demand;
  - the incumbent hits **89% fill**;
  - planners override **~30%**.
- **Resolution:**
  - 20% exceeds the theoretical headroom (myopic ≈ within 5% of optimal), so suspect a **weak baseline or overfitting**.
  - **Fund a guardrailed pilot**: scope = one family for 2 quarters; bounds = incumbent floors/ceilings; fallback = auto-revert; evaluation = randomised/matched control, service per ₹; trust loop = override with reasons; owners named.
  - Mine the overrides.
  - Full answer in [Ch 8 §8](#/ch08-inventory-optimisation).

## 11. The bearing and the telemetry call (S13) ⭐⭐
- **Facts:** a 68% failure flag, but the **weekly inspect-and-replace** protocol already catches the failure.
- **Resolution:**
  - **Don't act.** The prediction doesn't change the decision.
  - Fund telemetry only where the twin-now test passes all of its steps: decision-changing, high failure cost, data readiness, minimal fidelity needed.

## 12. The capacity shock and the LP mandate (S14–S15) ⭐⭐⭐
- **Facts:**
  - The Mumbai zone is about to stock out.
  - The road lane is at −40%.
  - Express is costly; rail is too slow.
  - Separately, a team set **identical cost weights**, and the solver starved the zone that drives **40% of premium-margin sales**.
- **Resolution:**
  - **Split the shipment**: express for the urgent part, rail as backfill.
  - Put zone priority **into the objective** (cost weights or service floors) **before solving**.
  - Write the **Mandate Card**.

## 13. The clause budget and the chip contract (S16) ⭐⭐
- **Resolution:**
  - Tune **penalty and indemnification** extraction first: uncapped exposure, discovered only when the supplier invokes it.
  - Domain-tuned (94.7%) beats general (79.3%).
  - Never fully automate interpreting liability clauses.

## 14. The repriced agent (S17) ⭐⭐
- **Resolution:**
  - Compare **value-per-decision vs cost-per-decision**.
  - Tune first (context, cache, batch, tier), and retire only if it still fails.
  - Spend caps go **in code**.

## 15. The celebrity paint-colour scenario (S18) ⭐⭐
- **Resolution:**
  - Label it **stretch**.
  - Check the mechanism and base rate.
  - Prefer a **cheap, reversible mitigation** over flex capex.

## 16. Command Your Agent — the amplification we made (S19) ⭐⭐⭐
- **Facts:** 20 teams' agents created a textbook bullwhip on the class screen.
- **Resolution:**
  - Use a **shared end-customer demand signal**, order smoothing and trained coordination.
  - Name the coordination mechanism and run **ACAP**.

## 17. Bias before the board (S20) ⭐⭐⭐
- **Resolution:**
  - Step down to **L2**.
  - Log the incident.
  - Disclose to the board as a **governance finding**.
  - Fix the data, verify parity and re-promote.
  - "Guardrails count only when you use them when it costs you something."

---

## Named real-world deployments (evidence to cite) ⭐⭐
| Company | What | Result | Use it to argue |
|---|---|---|---|
| **Amazon (Kiva → Amazon Robotics)** | goods-to-person robots (Kiva bought 2012, ~$775M) | pickers stay put; density and pick rate up | automation vs agentic |
| **Amazon DeepFleet** (Jun 2025) | GenAI foundation model coordinating 1M+ robots, trained on SageMaker | **10% less robot travel time** | fleet-level self-coordination |
| **Walmart × Pactum** | autonomous tail-spend negotiations within manager-set bounds | **~3% savings, +35-day terms, 64–68% close rate** | bounded autonomy (L3/L4) and mandates |
| **Walmart Trend-to-Product** | GenAI product design loop | **up to 18 weeks** off design-to-shelf | GenAI speed in design |
| **Unilever** | AI across ~20 control towers | stockouts −25%, retailer sales +15–35% | predictive control towers |
| **JD.com** | dual engine: AI sensing + classical solver | national-scale routing and placement | AI–OR symbiosis |
| **Fortune 150 OEM** (course text Ch 11) | one-step planning | **retailer forecasts got zero weight** | signals earn weights |
| **Semiconductor spare parts** (course text Ch 11) | installed-base signals, 50,000 SKUs | **fill 77% → 85% at constant inventory (~$20M)** | upstream drivers, one-step |
| **E-commerce RCTs / Alibaba field study** | learned replenishment vs buyers | better in-stock and turnover | evaluate by experiment |
| **Siemens** | digital twins across factories and customers' lines | simulate before touching equipment | fidelity-for-purpose twins |
| **IoT-triggered 3D-printed spares** | print the predicted part | weeks → days | collapse knowing-to-acting |
| **Danone / Zara / Lenovo** | ML planning, trend sensing, +5% forecast accuracy, +4% OTD | measured, incremental | sensing and incremental value |
| **M5 competition** (Walmart data, 42,840 series) | ML beat statistics overall | simple methods competitive at SKU-store | price the gap before paying for clever |
| **McKinsey chemicals pilot** | agentic procurement | **20–30% efficiency, 1–3% captured** | efficiency-capture gap |
| **EY CPO survey** | ~80% of CPOs plan GenAI within 3 years | spend analytics, contracts first | adoption context |

## Named failures (the cautionary tales) ⭐⭐⭐
| Failure | What went wrong | Lesson |
|---|---|---|
| **Nike & i2 (2001)** | ~$400M programme; the planning system over-ordered slow sellers; ~$100M shortfall; −20% share price | systems amplify their data and process foundations; test on your own history |
| **Zillow Offers (2021)** | ML price forecasts bought houses; >$500M write-down, ~25% of staff cut | the decision defines the model; irreversible decisions need proportionate guardrails |
| **2020 demand-model collapse** | history-trained models predicted the vanished world | regime-change fragility; monitoring and override |
| **Two stalled DRL pilots** (course text Ch 10) | teams couldn't interpret outputs, convergence or retraining | expertise and the production cliff |
| **DRL 15–20% behind a myopic rule** | learned the simulator, not the world | benchmark before trust |
| **1990s black-box scheduler** | better but illegible, so rejected | explainability beats an opaque optimum |
| **Air Canada chatbot (2024)** | airline held liable for its bot's wrong answer | the deployer answers for its agent |
| **Chain Reaction theatre teams** | built below gate; B11 and B14 orchestrators failed at 20% and 12% odds | sequence beats speed |
