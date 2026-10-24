# Practice Cases — three full mock papers with model answers
These are **new cases written in the exact style of the two past papers**: a company, exhibits with deliberate noise and defects, Section A diagnostics and Section B design. Each one recombines the course frameworks the way the real exam will. Attempt each paper for **30–35 minutes** before reading the model answers. Every answer follows the mandatory format: **Assumptions: A1. … A2. …**, then units and arithmetic, then the framework named, then the verdict.

> All numbers below are checked. Where a model answer depends on a reading of the exhibits, that reading is stated as an assumption, exactly as you should do in the exam.

---

# Mock Paper 1 — Meru Pharma Distributors
*(Tests: Claim audit, Q vs S, fill-rate weighting, data triage, Twin-Now test, autonomy and mandate, pilot ranking.)*

### The case
Meru Pharma Distributors moves branded and generic medicines from **6 distribution centres (DCs)** to about **9,000 pharmacies and 420 hospitals** across western and central India. Revenue is **₹2,400 crore**. A readiness self-assessment scored **[Data quality 3, Master data 2, Architecture 3, Security 4, Compute 3]**. The board approved **₹5 crore per year** for "AI in operations". Three proposals compete:

- **Proposal 1: AI demand-forecasting suite.** ₹2.2 crore/yr subscription plus ₹1.0 crore one-time integration. Vendor claim: "**35% lower inventory and 91% network fill rate within a year**."
- **Proposal 2: Predictive maintenance for cold rooms.** IoT vibration and temperature sensors plus an RUL model on the **40 cold-room compressors** (vaccines, insulin, biologics). ₹45 lakh one-time plus ₹15 lakh/yr.
- **Proposal 3: Emergency-delivery routing agent.** It decides, **without human sign-off (L4)**, whether hospital emergency orders go by courier-express or the next scheduled road run, and which DC ships. ₹0.9 crore/yr.

### Exhibit 1 — Operations & finance (annual)
| Item | Value |
|---|---|
| Average cycle stock (Q/2) | ₹48 crore |
| Average safety stock | ₹16 crore |
| Inventory carrying rate | 18% |
| Order quantities | supplier MOQ / full-truck multiples |
| Corporate brand campaign | ₹22 crore |
| Head-office renovation (one-time) | ₹6 crore |
| Hospital emergency orders | ~3,100 per year |
| Cold-room compressor failures | 20 per year (0.5 per compressor) |
| Average stock spoiled per failure | ₹6 lakh |
| Emergency repair per failure | ₹1 lakh |
| Current maintenance | **quarterly** preventive service |

### Exhibit 2 — DC fill rates (last quarter)
| DC | Order lines ('000) | Fill rate |
|---|---|---|
| Pune | 5,200 | 95% |
| Nagpur | 2,100 | 93% |
| Hyderabad | 4,800 | 81% |
| Indore | 1,500 | 96% |
| Raipur | 900 | 97% |
| Surat | 3,500 | 84% |
| **Total (as reported)** | **18,500** | **"Network fill 91%"** |

### Exhibit 3 — Supplementary
- The vendor's reference customer is a European OTC retailer with weekly replenishment and **no cold chain**.
- The PdM vendor's pilot elsewhere caught **70%** of compressor failures **at least 5 days ahead**. A planned repair then costs **₹1.2 lakh** with no spoilage.
- The ESG team notes a **14% reduction in fleet diesel use** since EV vans were introduced.

### Questions
**Section A (5 marks)**
- **A1.** Test Proposal 1's inventory claim with ONE calculation. Name your base and open with numbered assumptions.
- **A2 (2 marks).** Data triage:
  - (a) name three items that are irrelevant or unreliable for the decisions;
  - (b) find the defective figure(s) in Exhibit 2 and show the arithmetic;
  - (c) say what the correction does to the vendor's fill claim.
- **A3.** Size the annual value of Proposal 2 and its payback, and run the Twin-Now / Twin-Later test.
- **A4.** What is wrong with Proposal 3's autonomy level? State the governance design it needs.

**Section B (5 marks)**
- **B1.** Rank the three proposals for a 6-month go-live. For the top-ranked proposal give: the gate metrics (success + counter-metric), the owner, and the demotion trigger. For Proposal 3 give a Mandate Card.

---

## Mock 1 — Model answers

### A1 (1 mark)
**Assumptions:**
- A1. Inventory = cycle stock + safety stock = ₹48 + ₹16 = **₹64 cr**, which is the base for "35% lower inventory".
- A2. Order quantities are set by supplier MOQs and full trucks (Exhibit 1), so forecasting cannot change Q.
- A3. A realistic forecast gain cuts forecast-error σ by about 25%.

**Calculation (Q vs S):**
- Claim = 35% × 64 = **₹22.4 cr**. But all safety stock is only ₹16 cr. **Even a perfect forecast (S → 0) removes at most 16/64 = 25%.**
- The claim is **impossible** through forecasting alone.
- Realistic: S falls 25% → ₹4 cr = **6.25%** of inventory. Carrying saving = 4 × 18% = **₹0.72 cr/yr**, against a **₹2.2 cr/yr** fee (plus ₹1 cr one-time).

**Verdict:** the claim fails the Four-Question Claim Audit:
- the baseline is a different business (a European OTC retailer, no cold chain, weekly replenishment);
- it attacks the wrong stock (Q is MOQ-driven).

Fund it only if stockout or service benefits close the ₹1.5 cr/yr gap. Reshape it as a distribution-based safety-stock policy on volatile SKUs.

### A2 (2 marks)
**(a) Irrelevant or unreliable items:**
1. **Brand campaign ₹22 cr:** a marketing spend that no proposal affects.
2. **Head-office renovation ₹6 cr:** one-time and unrelated.
3. **ESG note on EV vans (−14% diesel):** true, perhaps, but it doesn't bear on any of the three proposals.
4. **The vendor's European reference:** unreliable as a baseline (different channel, no cold chain).

**(b) Defects in Exhibit 2:**
- **The total is wrong:** 5,200 + 2,100 + 4,800 + 1,500 + 900 + 3,500 = **18,000**, not 18,500.
- **"Network fill 91%" is a simple average** of six DC fill rates ((95 + 93 + 81 + 96 + 97 + 84)/6 = 91.0%).
- The **volume-weighted** fill = Σ(lines × fill) / Σ lines = 16,034 / 18,000 = **89.1%**.
- Unfilled lines = **1,966 thousand**, concentrated in **Hyderabad (912k) and Surat (560k)**, the two biggest DCs after Pune.

**(c) Effect of the correction:** the real network fill is 89.1%. The vendor's "91% within a year" is roughly the **current simple average**, i.e. **no improvement at all** on its own metric. Measure success on weighted fill and on the Hyderabad and Surat DCs.

### A3 (1 mark)
**Assumptions:**
- A1. Failures stay at 20 per year.
- A2. PdM catches 70% (14) at least 5 days ahead; the other 30% (6) fail as today.
- A3. Quarterly preventive service doesn't catch these failures (they occur between services).

**Today:** 20 × (₹6 L spoilage + ₹1 L repair) = **₹140 L/yr**.
**With PdM:**
- caught: 14 × ₹1.2 L = ₹16.8 L;
- missed: 6 × ₹7 L = ₹42 L;
- total **₹58.8 L**.

**Saving** = ₹81.2 L/yr. Net of ₹15 L running cost = **₹66.2 L/yr**. **Payback = 45 / 66.2 ≈ 0.68 years (about 8 months).**

**Twin-Now test:**
1. Decision-changing: **yes**, because the quarterly service can't see a failure developing in week 6.
2. Failure cost: **high**, given spoiled biologics and patient-safety risk.
3. Data readiness: sensors must be installed (an infrastructure bet), but it is a small fleet of 40.
4. Fidelity: an asset-level RUL model is enough, with no full twin.
5. **Verdict: twin-now (simulation-lite, asset level).** Keep the quarterly service as the fallback.

### A4 (1 mark)
**What's wrong:** L4 (no sign-off) on a decision whose error can harm patients is **disproportionate**. Hospital emergencies have **asymmetric error costs**: a late critical drug is far worse than an unnecessary courier.

**Design (ACAP):**
- **Accountability:** a named owner (Head of Hospital Supply).
- **Capability limits:** **L3**. The agent routes routine emergencies within bounds, and any order flagged *critical-to-life* defaults to the fastest mode, with no cost optimisation.
- **Auditability:** log every routing decision with its reason.
- **Proportionality:** a human approves diversions to a non-home DC above a ₹ threshold.
- **Post-incident learning:** every late critical order triggers a review.

Guardrails (service floor, cost ceiling) **live outside the model**.

### B1 (5 marks)
**Assumptions:**
- A1. The 6-month deadline means a live pilot, not full scale.
- A2. Sensor installation takes about 8 weeks.
- A3. Hospital emergency orders are about 3,100 per year, i.e. enough volume for a 3-month L3 pilot.

**Pilot-selection matrix (value, feasibility, blast radius):**
| Proposal | Value | Feasibility (6 months) | Blast radius | Rank |
|---|---|---|---|---|
| P2 PdM cold rooms | ₹66 L/yr net, payback about 8 months, plus safety | high (40 assets, simple model) | low (fallback = quarterly service) | **1** |
| P3 emergency routing | moderate (courier cost and service) | medium | **high at L4**, low at L3 | **2 (at L3 only)** |
| P1 forecasting suite | **₹0.72 cr/yr realistic vs ₹2.2 cr fee** | medium (MDM score 2) | medium | **3, reshape** |

**Gate for P2 (Phase 1 → 2):**
- **Success:** at least 60% of failures caught ≥ 3 days ahead **and** spoilage down at least 50% vs the same quarter last year (frozen baseline).
- **Counter-metric:** false-alarm swaps no more than 2 per month (technician trust).
- **Owner:** Head of Engineering, with Quality.
- **Demote** (back to time-based plus monthly checks) if the catch rate stays below 40% after two quarters.

**Mandate Card for P3 (L3):**
1. **Service floor:** critical-to-life SKUs are never routed by the slower mode, and hospital emergency on-time ≥ 98%.
2. **Cost ceiling:** courier ≤ ₹X per order for non-critical items; above it, escalate.
3. **Mode priority:** for non-critical orders the default is the next scheduled road run if it arrives within the SLA; otherwise courier.
4. **Shock trigger:** a DC outage or road disruption over 24 hours triggers a full re-plan with human approval.
5. **Review cadence:** weekly review of late orders and courier spend.

**P1 reshaped:** don't buy the suite. Replace weeks-of-cover rules with **quantile-based safety stock** on the volatile SKUs at Hyderabad and Surat (the 89.1% problem). Revisit a platform once master data reaches 3+.

---

# Mock Paper 2 — Brahmaputra Electronics
*(Tests: average-hides-trend, contribution forgone vs visible charge, split shipment, bullwhip ratio, LP mandate, clause stakes, tune-or-retire, bias and ACAP.)*

### The case
Brahmaputra Electronics assembles **LED TVs** at **2 plants** (Noida, Sriperumbudur) and ships through **3 regional DCs** to **3 dealer zones**:
- **Z1 metro premium**: contribution **₹2,400/unit**;
- **Z2 urban**: **₹1,100/unit**;
- **Z3 tier-2/3**: **₹900/unit**.

Last quarter the operations team deployed a **flow optimiser** with **identical cost weights for all zones**, a **procurement agent** for display-panel and chip contracts, and a **supplier-news monitoring agent**. This month's review deck claims success.

### Exhibit 1 — Zone performance (this month)
| Zone | Demand (units) | Fill rate |
|---|---|---|
| Z1 metro premium | 18,000 | 72% |
| Z2 urban | 12,000 | 90% |
| Z3 tier-2/3 | 9,000 | 93% |
| **Deck headline** | | **"Network fill 85%, in line with target"** |

Other figures:
- Express (air/expedite) charge this month: **₹22 lakh**, presented as "the cost of the monsoon".
- Freight cost per unit is down 9% vs last month: "optimiser success".

### Exhibit 2 — Modes (per unit to Z1)
| Mode | Cost | Lead time | Constraint |
|---|---|---|---|
| Road | ₹180 | 2 days | capacity cut to **1,500 units / 3 days** (flooded corridor) |
| Rail | ₹135 | 6 days | slots available; booked monthly, charged whether used or not |
| Express | ₹420 | 1 day | available |

Z1 needs **6,000 units in the next 10 days**, of which **2,400 must arrive within 3 days** (festival launch).

### Exhibit 3 — Order variance up the chain (weekly, units²)
| Tier | Variance |
|---|---|
| Dealer sell-out (consumer demand) | 400 |
| Dealer orders to DCs | 900 |
| DC orders to plants | 2,500 |
| Plant orders for panels/chips | 7,200 |

### Exhibit 4 — Agent run costs (after the vendor repriced)
| Agent | Run cost/month | Decisions/month | Avg value per decision |
|---|---|---|---|
| Procurement agent | ₹6.0 L (was ₹2.5 L) | 1,500 POs | ₹1,100 saved per PO |
| Supplier-news agent | ₹4.0 L | 30 alerts acted on | ₹8,000 per acted alert |

### Exhibit 5 — Incident note
An analyst found that the **credit-limit agent**, which sets dealer credit at L4, used two years of history in which tier-2/3 dealers had **no digital payment records**. It approves tier-2/3 dealers at **half the rate** of metro dealers with similar sales. The board meets in three days.

### Questions
**Section A (5 marks)**
- **A1.** Audit the deck's two success claims ("network fill 85%", "freight per unit −9%").
- **A2 (2 marks).** Size the contribution forgone this month. Compare it with the ₹22 L "cost of the monsoon", and explain *why* the optimiser produced this plan.
- **A3.** Design the shipment for Z1's next 10 days, with costs.
- **A4.** Compute the bullwhip amplification and name the single highest-leverage fix.

**Section B (5 marks)**
- **B1.** Rewrite the optimiser's mandate (Optimizer Mandate Checklist).
- **B2.** Tune-or-retire each agent in Exhibit 4.
- **B3.** For the coming panel contract, list the clause stakes and the one clause you'll never fully automate.
- **B4.** What do you do about Exhibit 5 before the board meeting?

---

## Mock 2 — Model answers

### A1 (1 mark)
**Assumptions:**
- A1. Fill = units delivered / units demanded per zone.
- A2. The deck averaged the three zone fill rates.

**Calculation:**
- The simple average is (72 + 90 + 93)/3 = **85.0%**.
- **Volume-weighted** fill is (18,000 × 0.72 + 12,000 × 0.90 + 9,000 × 0.93) / 39,000 = 32,130 / 39,000 = **82.4%**.
- The average **hides the problem**: the **biggest and most profitable** zone is the worst served.

**Freight −9%:** this is **activity, not outcome**. Freight fell because the optimiser chose cheap lanes and **didn't ship** to Z1. A lower cost per unit shipped, combined with lost premium sales, is a worse business.

**Verdict:** both claims fail the claim audit (an average hiding the mix; an activity metric presented as an outcome).

### A2 (2 marks)
**Assumptions:**
- A1. Unfilled units are lost sales (no backorders in a festival month).
- A2. Contribution per unit is as given.

**Lost units:**
- Z1: 18,000 × 28% = **5,040**.
- Z2: 12,000 × 10% = 1,200.
- Z3: 9,000 × 7% = 630.

**Contribution forgone:**
- Z1: 5,040 × ₹2,400 = **₹120.96 L**.
- Z2: 1,200 × ₹1,100 = ₹13.2 L.
- Z3: 630 × ₹900 = ₹5.67 L.
- **Total ≈ ₹139.8 L (₹1.40 cr)**.

That is **6.4× the ₹22 L "monsoon" charge**. Z1 alone is 87% of the loss.

**Why:** the optimiser **did exactly what it was told**. With **identical cost weights** and **no service floor**, minimising cost means starving the costliest-to-serve lane (Z1 via the flooded road). The plan is **technically optimal and strategically wrong**. Strategy lives in the objective function. The monsoon was the trigger; the **mandate** was the cause.

### A3 (1 mark)
**Assumptions:**
- A1. The road capacity cap (1,500 units per 3 days) holds.
- A2. Rail's 6-day lead time fits the 7 days left after the urgent window.
- A3. Express capacity is sufficient.

**Split shipment:**
- **Urgent 2,400 in 3 days:** road 1,500 × ₹180 = ₹2.70 L, plus express 900 × ₹420 = ₹3.78 L.
- **Remaining 3,600 within 10 days:** rail 3,600 × ₹135 = ₹4.86 L. Book it now (it is charged whether used or not, so book only the 3,600 you need).
- **Total ₹11.34 L.**
- All by express would be 6,000 × ₹420 = **₹25.2 L**, so the split saves **₹13.86 L (55%)** with no festival stockout.
- Hold back one buffer: if road slips, convert part of the rail portion to express (the trigger).

### A4 (1 mark)
**Calculation:**
- Ratios: dealer 900/400 = 2.25; DC 2,500/900 = 2.78; plant 7,200/2,500 = 2.88.
- **Total = 7,200/400 = 18× amplification.**

**Fix:** give every tier, and every agent, the **same real end-customer sell-out signal (dealer POS)** instead of the next tier's orders. Add order smoothing (e.g. weekly change ≤ ±10%), and name one owner of the shared plan.

This is the **collaboration paradox**: smarter local agents reacting to orders amplify noise faster.

### B1 — the optimiser mandate (Optimizer Mandate Checklist)
**Assumptions:**
- A1. Z1's premium margin and brand matter strategically.
- A2. Rail (MIX) is available.

1. **Service targets per zone:** Z1 ≥ 95% in festival months; Z2 ≥ 90%; Z3 ≥ 88%.
2. **Cost weights:** put a lost-sales penalty equal to contribution into the objective (₹2,400 / ₹1,100 / ₹900 per unit short), so the solver "sees" the premium.
3. **Review rule:** **L3**. The plan executes automatically within the floors; exceptions (a floor breach forecast, or express > ₹10 L/week) escalate to the CSCO.
4. **Re-solve triggers:** lane capacity loss > 20%; any zone's forecast fill < floor − 5 points; demand spike > 25%.
5. **Verify the fit:** before execution, check the plan's projected fill by zone against the floors. Optimal ≠ right.
- Also: book rail only for base load, keep road and express for the variable tail, and front-load (FRONT) before the festival.

### B2 — tune-or-retire
**Procurement agent:**
- Cost per decision = ₹6.0 L / 1,500 = **₹400**; value = ₹1,100. Ratio **2.75×**, so **keep**.
- Tune anyway: cache supplier histories, batch the low-value POs, and use a cheaper model tier for routine re-orders.
- (Before repricing it was ₹167/decision, 6.6×. The shock is a signal to re-run the math, not a verdict.)

**Supplier-news agent:**
- Cost per acted decision = ₹4.0 L / 30 = **₹13,333**; value ₹8,000. Ratio **0.6×**, so it is **under water. Tune first:**
  - scan daily instead of hourly;
  - restrict to the top 50 suppliers;
  - use a cheaper tier.
- If cost halves to ₹6,667 (ratio 1.2×), keep it on watch.
- If it can't get below about ₹6,000, **retire** it and fall back to a weekly analyst review plus the free alerts.
- **Spend caps in code** for both.

### B3 — clause stakes for the panel contract
| Clause | Decision it feeds | Bar | Tier | Human |
|---|---|---|---|---|
| **Allocation priority in shortage / force majeure** | supply continuity in a shortage | very high | domain-tuned | **always (never fully automated)** |
| Liability cap, penalties, indemnity | financial exposure | very high | domain-tuned | always |
| Volume commitment and take-or-pay | inventory and cash (fees on the full book) | high | domain-tuned | review |
| Price index / escalation | cost model | high | domain-tuned | review |
| Payment terms | cash plan | medium | general | spot-check |
| Delivery address, contacts | logistics admin | low | general | no |

Size the volume commitment to **real demand** (the Chain Reaction lesson: fees are charged on the full book).

### B4 — the credit-limit bias (ACAP)
**Assumptions:**
- A1. The approval-rate gap is driven by missing digital records, not by repayment performance.
- A2. The decisions are reversible (credit limits can be re-set).

**Action now:**
- **Step the agent down from L4 to L2**: a credit manager approves tier-2/3 decisions.
- Log the incident.
- Quantify the impact: the selection-rate ratio is about **0.5, below the 0.8 rule of thumb**, and estimate the lost Z3 sales.
- **Disclose it to the board as a governance finding.** Do not wait, and do not patch quietly.

**Fix:**
- Add alternative data (sales history, GST filings) for thin-file dealers.
- Run a parity test by region before re-promotion.
- Name an owner.

*Guardrails count only when you use them when it costs you something.*

---

# Mock Paper 3 — Chain Reaction mid-season (the simulation as an exam case)
*(Tests: foundation gates, token economics, build speed, distribution dials, operating vs building, the value multiplier.)*

### The case
Your team runs **Ganga Motors** in Chain Reaction. It is the **start of Round 6**.
- **Foundations:** **Data 2 · Process 3 · Tech 2**.
- **Owned agents (monthly upkeep):** Forecasting agent L2 (2 tokens), Distribution Planning Agent (2), Predictive Maintenance L2 (1), Pricing agent (3).
- **Last month:**
  - you regenerated the operating plan **twice**;
  - fill in the 3 premium zones was 71%;
  - 410 cars auto-pushed to the home RDC of Plant 1;
  - your rail booking was **zero** (distMode = ROAD);
  - the chip book was contracted at **130%** of the demand plan.
- **Company value** = profit 150 × reputation 0.84 × trust 0.95.
- Your CTO wants to build the **Network-Intelligence Orchestrator** (gate **D3·P3·T3**) this round "to catch up with the leaders".

### Questions
1. Compute this month's token budget if you keep everything and generate one plan plus one regeneration. How many tokens remain for builds and foundations?
2. Should you build the orchestrator this round? Use the season lessons.
3. Which three operating moves fix last month's results, and which dial does each touch?
4. A rival has profit 170, reputation 0.78 and trust 0.85. Who is worth more, and what does that teach?
5. The pricing agent's upkeep is 3 tokens/month and it changed prices twice last month for about ₹0.8 cr of extra contribution. Tune or retire?

## Mock 3 — Model answers
**Assumptions:**
- A1. 24 tokens per month; plan = 2 tokens, regeneration = 1; termination = 2 tokens.
- A2. Below-gate builds have cut odds and deliver a fraction of the effect.
- A3. 5 rounds remain.

1. **Tokens:** upkeep 2 + 2 + 1 + 3 = **8**, plus plan 2 + regeneration 1 = **11**. **13 tokens remain.** (Last month's two regenerations cost an extra token. Regenerate only on a real trigger.)
2. **Don't build the orchestrator yet. It is below gate on D (2 < 3) and T (2 < 3).**
   - A below-gate agent runs **at full cost for a fraction of the effect**, with cut odds. B14-Six Sigma's and B11-Dream11's orchestrators **failed at 12% and 20% odds**.
   - **Sequence beats speed.** Spend the 13 tokens raising **Tech to 3** first: it also **unlocks MIX (rail)**. Then raise Data to 3, and build the orchestrator once at gate (A7-Kimi K3: zero below-gate builds all season, #2).
3. **Operating moves (building is not operating):**
   - (a) **Raise Tech to 3, then set distMode = MIX** and book rail for the predictable base volume: about 25% cheaper per car, booked a month ahead and charged whether used or not, so book base load only.
   - (b) **Stop the auto-push.** File a distribution plan with **distFront = FRONT** before peak months and **distSafety weighted to the premium zones**. The 410 cars piled at Plant 1's RDC are A2-Doomsday's 338-car mistake.
   - (c) **Resize the chip book to about 100–105% of the demand plan** in the Round 6 negotiation. Fees are charged on the full book, so 130% pays for 25–30% idle volume.
4. **Value:**
   - You: 150 × 0.84 × 0.95 = **119.7**.
   - Rival: 170 × 0.78 × 0.85 = **112.7**.
   - **You are worth more despite 12% less profit.** Governance (reputation and trust) is the multiplier you feel late. Protect it by avoiding guardrail breaches and filing honest incident reviews.
5. **Pricing agent:** about ₹0.8 cr extra contribution per month for 3 tokens. Compare value per token with the next-best use of a token (raising Tech to unlock rail saves far more).
   - **Tune first:** limit it to the two products with real price elasticity, or drop to a lower tier if the catalogue allows.
   - **Retire** only if tokens are binding on gate-raising this round and its value per token is the lowest in the estate.
   - Retiring costs 2 tokens and saves 3 per month, so it **pays back in 1 month**.
   - Decide on **cost-per-decision vs value-per-decision**, not the size of the bill.
