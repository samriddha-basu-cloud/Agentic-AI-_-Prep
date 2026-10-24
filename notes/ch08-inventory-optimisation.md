# Ch 8 — AI Inventory Optimisation: From EOQ to Learned Policies (Session 10)
**Syllabus unit 4 📘:** *Inventory Optimisation with AI (EOQ, Dynamic Models) — AI dynamic modelling using RNN, LSTM; differentiate with real-time reordering examples.*
**Session 10 📘:** "Classical policies, deep reinforcement learning, and the one-step paradigm, with the guardrails the evidence demands." It was delivered experientially through the **Command Your Agent** game; the deck is the self-study reference.
**Case: Krishna AgroMachinery — The 20% Claim.**

> **Exam use:** whenever a case says "AI will cut inventory X%" or "the agent will take over ordering", answer with three tools.
> (1) **Q vs S**: which stock does it touch?
> (2) **The benchmark ceiling**: a myopic rule sits within about 5% of optimal, so 20% needs explaining.
> (3) **The Guardrailed Pilot**: scope, bounds, fallback, evaluation, trust loop, ownership.
> Learned policies wear proven guardrails.

---

## 0. The inventory basics you must compute (straightforward numericals) ⭐⭐⭐
| Item | Formula | Note |
|---|---|---|
| **EOQ** | √(2DS/H) | D = annual demand, S = cost per order, H = holding cost per unit per year (= i × unit cost) |
| Orders per year | D/Q | |
| Annual ordering cost | (D/Q) × S | equals holding cost at EOQ |
| Annual holding cost (cycle) | (Q/2) × H | |
| **Cycle stock** | Q/2 | driven by batch size, **untouched by forecasting** |
| **Safety stock** | z × σ_d × √L | z: 90% → 1.28, 95% → 1.645, 97.5% → 1.96, 99% → 2.33 |
| **Reorder point** | d × L + SS | |
| **Average inventory** | Q/2 + SS | |
| **Inventory turns** | annual COGS / average inventory value | days of inventory = 365 / turns |
| **Fill rate** | units shipped on time / units demanded | **weight by volume, not a simple average** |
| **Newsvendor critical ratio** | Cu/(Cu+Co) | the order is that quantile of demand |

**Worked example.**
- Inputs: D = 12,000 units, S = ₹1,500 per order, unit cost ₹500, i = 20% so H = ₹100.
- EOQ = √(2 × 12,000 × 1,500 / 100) = √360,000 = **600 units**.
- That means 20 orders per year, with ordering cost = holding cost = ₹30,000 each, a total of ₹60,000.
- With weekly σ = 40, L = 2 weeks and 95% service: SS = 1.645 × 40 × √2 = **93 units**.
- ROP = (12,000/52) × 2 + 93 ≈ 462 + 93 = **555**.
- Average inventory = 300 + 93 = **393 units**.
- If AI forecasting cuts σ by 25%, SS becomes 70, and average inventory falls from 393 to 370, a fall of **5.9%, not 25%**. This is the Q vs S lesson.

## 1. The Inventory Policy Ladder ⭐⭐⭐ (framework)
| Generation | Logic | Strengths | Where it strains |
|---|---|---|---|
| **EOQ (1913)** | batch size from the order-vs-holding cost trade-off | transparent; still right for stable demand | assumes steady demand and static costs |
| **Basestock / (s,S) + service levels** | order up to a target set by the demand distribution over lead time | decades of theory; auditable; near-optimal when tuned | complex networks, dual sourcing, lost sales |
| **Stochastic optimisation / MEIO** | multi-echelon optimisation under uncertainty (**700+ Global 2000 deployments**) | network-aware; proven at enterprise scale | static parameters; slow to absorb new signals |
| **DRL policies** | neural policy learned by acting in a simulator: state → action, for reward | handles complexity no formula covers; millisecond inference | data- and tuning-hungry; **brittle off-regime**; opaque |
| **One-step (data-to-decision)** | learn the decision FUNCTION from features, constraints and KPIs directly | skips forecast errors; interpretable weights; deployed at Fortune 150 scale | needs the **digital twin + data architecture** beneath it |

**The ladder is cumulative.** The classical rungs supply the **guardrails** (floors, ceilings, safety stock) for the learned ones.

## 2. What deep RL actually learns — in operations language ⭐⭐⭐
- **The loop:**
  - **STATE**: stock position, pipeline, demand signals;
  - **ACTION**: order quantity;
  - **REWARD**: −(holding + shortage + ordering costs).
  - It repeats across **simulated years** until the policy maps states to profitable actions.
- **Q-learning:** the agent learns a quality score **Q(state, action)** for each action in each state. It updates the score with the reward received plus the discounted best future value, then picks the highest-Q action. Learning is **by reward, not labels**. The agent **creates its own data** by trial and error (a famous system reached super-human Go in about 70 hours of self-play).
- **Why it can win:**
  - No closed-form policy exists for realistic networks (lost sales + dual sourcing + capacity).
  - Neural policies approximate what formulas cannot express, and infer in **milliseconds** once trained, which enables **real-time reordering**.
  - It **optimises the decision directly**: the output is a replenishment policy, not a forecast handed to a separate optimiser, so there are fewer places for error to hide.
- **Why it can lose:**
  - **It learns the simulator, not the world.** Mis-specified dynamics, unseen regimes and tuning sensitivity produce the **15–20%-behind pattern**.
  - Training is expensive, and retraining is a discipline.
- **The craft frontier:** differentiable simulators for stable training; **reward shaping from known heuristics**; restricting policies to sensible families. In every case, **classical theory steers the learner** (AI–OR symbiosis).

### RNN / LSTM in inventory 📘
Recurrent networks read **sequences**: demand history, lead-time history and sensor streams. **LSTM** (long short-term memory) gates let them remember long patterns such as seasonality and promotion after-effects. Uses:
- (a) **sequence demand forecasting** feeding the policy;
- (b) **end-to-end deep inventory models** (data straight to order quantities, validated in production at a major retailer).

The caveat is the same as in Ch 7: they need **long history and Data Maturity 3+**, and at SKU-week granularity simple methods stay competitive.

### Real-time reordering and dynamic safety stock 📘
A learned policy re-evaluates the state continuously (stock, in-transit, live POS, supplier ETA) and triggers orders the moment the position crosses a learned threshold. Safety stock becomes **dynamic**: it recomputes as forecast uncertainty and lead-time variance change, instead of a static "2 weeks of cover".
- **Guard against nervousness:** set a deliberate re-plan cadence (the one-step system re-computed weekly) and use frozen zones.

### Class Q 10.5 — RL beats the classical policy by 18% in simulation ⭐⭐⭐
The 18% was measured on two years of stable demand.
**Answer: B, cage it with a benchmark and guardrails.**
- Learned policies are brittle on regimes they never trained on (intermittent demand, shocks, promotions).
- The safeguard is a naive benchmark, **classical guardrails outside the policy** and a human escalation path, not a bigger model.
- *Learned policies wear proven guardrails.*

## 3. One-step planning — where Module 2 meets Module 3 ⭐⭐⭐
- **The diagnosis (S8):** firms hold multiple distorted forecasts, then convert them to stock with crude rules, so **accuracy gains die downstream**.
- **The repair:** learn the **DECISION function** directly.
  - Stocking levels are computed as a learned, weighted function of **demand features** (sales history, promotions, installed base) and **supply features** (lead times, capacity).
  - It is trained so the decisions optimise **KPIs** (fill rate, profit) under real constraints.
  - The standalone forecast **disappears**, and each signal is priced by its contribution to the DECISION (the zero-weight customer forecasts).
- **Deployed results (Fortune 150, spare parts):**
  - fill rate **~77% → ~85% at constant inventory**, or **~$20M inventory released at constant service**;
  - **interpretable weights** let planners see exactly why each recommendation moved.
  - **"The frontier shifted, not just a point on it."**
- **The architecture beneath it:** the digital twin and end-to-end data layer (S2, S13).
- **1 step:** data → decision replaces predict-then-optimise's error-compounding two steps.

### Class Q 10.3 — forecast +15% or a better policy? ⭐⭐⭐
- (a) Improve forecast accuracy by 15% and keep the weeks-of-supply rule.
- (b) Keep the forecasts and replace the rule with a policy optimised on the demand distribution and costs.

**Answer: D, (b). The conversion step is where value dies.**
- The failure chain (multiple forecasts → crude rules) wastes accuracy before it reaches the shelf.
- Zero-heavy demand limits forecastability anyway.
- *Optimise the policy, not the forecast.*

## 4. The evidence — both sides of the ledger ⭐⭐⭐
### The gold standard: randomised trials
- A **major global e-commerce player** trained a deep policy on its own simulator ("**direct backpropagation through the simulator**"). It reported substantial inventory-cost reductions **in randomised evaluation**, and the approach now underpins production replenishment.
- A published **field study at a large Asian marketplace** (Alibaba) ran automated ML replenishment **vs experienced human buyers**: better in-stock rates and turnover on randomised categories.
- A **third large retailer** published an **end-to-end deep model** (data straight to order quantities) in a top management journal, validated in production.
- **Common architecture:** learned policy inside, **hard bounds and fallback rules outside**, and **EVALUATION BY EXPERIMENT, not backtest theatre**.

### The sobering record
- **The 15–20% surprise:** freshly trained DRL models often run **15–20% BEHIND a simple myopic policy**, which itself sits **within about 5% of optimal**.
- **Two stalled pilots:** two established firms' DRL pilots died before production. The teams could not **interpret outputs, navigate convergence or manage retraining**; the barrier was missing deep technical expertise, not the AI (the notebook-to-production cliff, at policy scale).
- **Enterprise inventory optimisation's long game:** 700+ Global 2000 deployments, so the bar any learner must clear is "high, tuned and trusted".
- **Zillow's shadow:** a learned model writing irreversible purchases without proportionate guardrails carries existential tail risk. Inventory cheques are smaller, but the architecture lesson is identical.

### Class Q 10.1 — the vendor's 20% backtest ⭐⭐⭐
The incumbent is a tuned basestock policy, and a myopic rule is known to sit within about 5% of optimal.
**Answer: B, likely overfitting or a weak baseline.**
- If the incumbent is within about 5% of optimal, **no policy can beat it by 20%**: the maximum possible gain is about 5%.
- Ask what the incumbent in the test actually was, on whose data, and with what holdout.
- *Benchmarks with a theory-informed ceiling.*

**Numeric framing.** Incumbent cost = 100 and optimal ≥ 100/1.05 ≈ 95.2, so the **maximum saving is about 4.8%**. A "20% saving" implies cost 80, which is below optimal and impossible against a properly tuned incumbent. So the backtest compared against a weaker baseline, or overfitted.

## 5. Explainability vs optimality — when the better answer loses ⭐⭐
- A **1990s black-box supply-chain solver** gave objectively better schedules, but planners accountable for results could not understand or fix odd answers.
- A **constraint-based, steepest-descent "clean-up" solver** was widely preferred, even though its solutions were **provably less optimal**.
- **Lesson:** when a human must own the decision, **a transparent, slightly-worse answer can beat an opaque optimum**. Optimise the policy, but keep it legible: explainable guardrails and a documented reason for each recommendation.
- **Automated vs intuitive:** automate the routine reorder where data is rich. Keep human judgement for **the shock, the new SKU and the regime the model never saw**.

## 6. The four hard problems of learned inventory ⭐⭐⭐
1. **Intermittent demand.** Spare parts sell zero most weeks: long strings of zeros punctuated by lumps. Point forecasts are near-meaningless. The workable routes are **distributions** and **pooled/global signals (installed base)**.
2. **Non-stationarity.** Lifecycles, promotions and shocks mean a policy trained on one regime degrades silently in the next. Adaptive retraining helps; monitoring and fallbacks are mandatory.
3. **Delayed, entangled feedback.** Today's order shows its consequences weeks later, entangled with lead times. Learning signals are slow and noisy, so simulators carry the load and **sim-to-real gaps bite**.
4. **Black-box trust.** A planner asked to follow unexplainable order quantities re-runs **Continental Parts**: aversion, overrides, shadow spreadsheets. **Interpretability and bounded override are deployment requirements.**

### Class Q 10.2 — MAPE on 0,0,0,4,0,0,2,0 ⭐⭐⭐
**Answer: A, MAPE is undefined on zero actuals** (you divide by zero).
- **Replace it with** calibrated demand distributions over the lead time, and the **decision frontier: service level achieved per rupee of inventory**.
- Alternatives are MASE or pinball loss.
- *Metrics follow the decision.*

**Numeric aside.** That series has a mean of 6/8 = 0.75 per week; 6 of 8 weeks are zeros (75% zero), so the average demand interval is 8/2 = 4 weeks. Croston-type or distributional methods suit this; MAPE does not.

### Class Q 10.4 — "shadow 4 weeks, then full control" ⭐⭐⭐
**Answer: B, bounds, fallback and a real evaluation are missing.**
- Intermittent demand makes 4 weeks **statistically nearly empty** (e.g. 2 demand events).
- Shadow accuracy is not decision value.
- Unbounded "full control" ignores the stalled-pilot record.
- The leaders ran **RCTs inside guardrails**.

## 7. The Guardrailed Pilot — six design elements ⭐⭐⭐ (framework)
| # | Element | What it means |
|---|---|---|
| 1 | **Scope** | one category, honest volume, **long enough for intermittent statistics (quarters, not weeks)** |
| 2 | **Bounds** | basestock **floors and ceilings from the trusted incumbent**; spend envelopes; no unbounded orders |
| 3 | **Fallback** | **drift and anomaly triggers that auto-revert** to the incumbent policy, **tested before go-live** |
| 4 | **Evaluation** | **randomised or matched-control** vs incumbent AND naive benchmark; decision-frontier metrics (**service per rupee**) |
| 5 | **Trust loop** | interpretable recommendations; **bounded planner override with reason capture** feeding retraining |
| 6 | **Ownership** | named **expert owner** for the policy; named **business owner** for outcomes; review cadence with a **widen / narrow / revert** decision |

"This design IS the honest answer to every '20% better' pitch: **fund the pilot, on these terms**."

## 8. Krishna AgroMachinery — the case resolved ⭐⭐⭐
**Facts:**
- The vendor claims DRL cuts spare-parts inventory by 20% vs basestock, "as proven in our backtest".
- Most SKUs sell zero most weeks.
- The incumbent basestock policy is tuned over years and hits **89% fill**.
- Planners override about **30%** of recommendations.

**Model answer (numbered assumptions first):**
1. *Assume* the vendor's backtest used Krishna's history with no holdout disclosed.
2. *Assume* the incumbent is near the myopic-optimal frontier (within about 5%).
3. *Assume* overrides are logged with reasons.

**Diagnosis:**
- The 20% exceeds the theoretical headroom of about 5%, so it is likely overfitting or a weak baseline.
- Intermittent demand weakens learning from history (few events per SKU) and breaks MAPE.
- The 30% override rate is **information to mine, not a problem to eliminate**. Overrides carry planner knowledge (field campaigns, dealer intel); capture the reasons and feed them back.

**Decision:** do **not** fund as pitched. **Fund a guardrailed pilot**:
- **Scope:** one high-volume parts family for **two quarters**.
- **Bounds:** the incumbent basestock ±X% as floor and ceiling, plus a spend cap.
- **Fallback:** auto-revert if fill drops more than 2 points below 89% for 2 weeks, or on a drift trigger.
- **Evaluation:** matched-control families vs incumbent and naive, measuring fill per rupee of inventory.
- **Trust:** interpretable recommendations, an override band of ±20% with mandatory reasons.
- **Owners:** a named policy owner (vendor + internal analyst) and the parts-business head.

**Widen the envelope if,** after two quarters, the frontier has moved (same fill with less inventory, or higher fill at the same inventory) **in the randomised comparison**, and overrides have fallen because trust grew, not because overrides were banned.

**Alternative worth naming:** the bigger win may be replacing weeks-of-supply rules with **distribution-based basestock using installed-base signals** (Q 10.3), which is cheaper and auditable.

## 9. Chain Reaction link ⭐⭐
- Inventory and replenishment agents follow the same rule: build to the **foundation gate**.
- Pick L2 (recommend) before L3 (bounded act).
- Distribution dials (**distCover, distSafety**) are the in-game equivalents of cycle cover and safety stock. **Raising distSafety buys service with working capital**, and that cost must be visible.
- **Command Your Agent** (the S10 game) taught granting autonomy only with bounds and a revert path. See the [Chain Reaction playbook](#/chain-reaction-playbook).

## Key takeaways (S10 recap 📘)
1. The evidence ceiling is real (randomised-trial wins at the leaders) and so is the floor (15–20% behind a simple policy). **Engineering discipline, not algorithm choice, separates them.**
2. Intermittent demand breaks point thinking: **distributions over lead time and upstream signals (installed base)** are the route for spare parts.
3. The policy ladder is cumulative (EOQ → basestock → MEIO → DRL → one-step), and **classical rungs supply the guardrails** for learned ones.
4. **Optimise the policy, not the forecast.** One-step shifted the service-inventory frontier (77 → 85% fill).
5. The **guardrailed pilot** is your permanent answer to every learned-policy pitch.

---

## Self-test
**Q1. D = 24,000, S = ₹2,000, H = ₹60. Find EOQ, orders per year and total cost.**
EOQ = √(2 × 24,000 × 2,000 / 60) = √1,600,000 ≈ **1,265**. Orders per year ≈ 19. Ordering cost ≈ holding cost ≈ ₹37,950 each, about **₹75,900** in total.

**Q2. A vendor says its RL agent beats your tuned (s,S) policy by 25% in backtest. What is your first question, and why?**
"What exactly was the baseline, on whose data, with what holdout?" A tuned myopic or basestock policy sits within about 5% of optimal, so 25% is beyond the headroom. It signals a weak baseline or overfitting.

**Q3. Why is a 30% planner override rate information, not a problem?**
Overrides encode knowledge the model lacks (dealer campaigns, field failures). Capture the reasons, check which overrides were right, and feed them into retraining. Banning overrides destroys trust and the learning signal.

**Q4. Name the six elements of a guardrailed pilot.**
Scope, bounds, fallback, evaluation, trust loop, ownership.

**Q5. Explain "learned policies wear proven guardrails" with an example.**
A DRL replenishment policy chooses quantities, but floors and ceilings from the incumbent basestock, spend caps, drift-triggered auto-revert and human escalation sit outside it. Guardrails live outside the model.

**Q6. Why can a transparent but slightly worse solver beat an optimal black box?**
The planner who owns the outcome must understand and correct odd answers. Without legibility they override everything or keep shadow spreadsheets, so the "optimal" plan is never executed (the 1990s solver and Continental Parts).

**Q7. Average inventory is 1,000 units, of which SS = 250. AI cuts forecast σ by 40%. What is the new average inventory?**
SS falls to 150, so average inventory = 750 + 150 = **900** (−10%). The cycle stock of 750 is unchanged.
