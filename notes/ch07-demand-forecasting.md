# Ch 7 — AI-Driven Demand Forecasting (Sessions 8, 9, 11, 12)
**Syllabus unit 3 📘:** *Demand Forecasting Using Agentic AI — auto-updating models using IoT and reinforcement learning; Excel vs. Prophet vs. SageMaker.*
**Session 8 📘:** "Probability forecasting, demand sensing with IoT and external signals, and the planning paradigm that stops worshipping the forecast." Case: **Nandini Beverages — Three Forecasting Pitches Before the Monsoon**.
**Session 9 📘 (lab):** "One dataset, three tool tiers, one verdict." Case: **Trident Distributors — Which Tier Fits?**
**Session 11 📘:** a recap of the S8 ideas that led straight into **Chain Reaction Round 1 (Onboarding)**.
**Session 12 📘:** "Buy the tool the workload deserves." It covers the four tiers including LSTM, the M5 footnote and the bake-off ladder, and led into **Round 2 (Forecasting bake-off)**.

> **Exam use:** demand-forecasting questions in a case almost never ask "which algorithm?". They ask one of four things.
> (1) **Point vs distribution**: is the safety stock reading the uncertainty?
> (2) **Signal audit**: is the new data worth buying?
> (3) **Tier match**: Excel, Prophet, AutoML or LSTM, given volume, readiness, skills and governance?
> (4) **Update vs execute**: is the "autonomous forecasting agent" actually an autonomy grant?
> Kaveri Motors' Claim 4 ("the forecast is good, so we can cut the buffer") is a forecasting question in disguise: **forecasting attacks safety stock only, never cycle stock (Q vs S).**

---

## 1. Probability forecasting — "the quantile IS the decision" ⭐⭐⭐
- **From number to distribution.** A probability forecast gives the full range of outcomes with their likelihoods (mean, spread, tails) for each SKU, location and period. The point forecast is only one summary of it, and rarely the useful one.
- **A service level is a quantile choice.** Stocking to a 95% service level means holding the **95th percentile of demand over the lead time**. Put that way, safety stock stops being folklore and becomes a **costed choice on an explicit curve**.
- **Newsvendor logic generalises it.** When over-stocking and under-stocking cost different amounts, the optimal order is the **critical quantile**:
  - **CR = Cu / (Cu + Co)**, where Cu is the cost of one unit short (lost margin and goodwill) and Co is the cost of one unit left over (holding, markdown, obsolescence).
  - Example: margin ₹60 lost per short unit and ₹20 lost per unsold unit gives CR = 60/80 = 0.75, so stock the **75th percentile**. Fashion and perishables have low CR; high-margin spares have high CR.
- **Evaluation changes too.** Distribution forecasts are scored with **quantile (pinball) loss** and **calibration checks** ("do 90% of actuals fall inside the 90% band?"), not MAPE alone. The **M5 uncertainty track** exists because this is where planning value concentrates.
- **Point forecasts force a workaround.** Planners have to bolt the uncertainty back on with rules of thumb such as "weeks of supply". Distributions let safety stock read straight off the data.

**Worked numeric (exam style).** Assume normal demand with a weekly mean of 1,000 and σ = 200, a lead time of 4 weeks and a 95% service level (z = 1.645).
- σ over the lead time = 200 × √4 = **400**.
- **SS = 1.645 × 400 ≈ 658**.
- Reorder point = 4,000 + 658 = **4,658**.
- If a better forecast cuts σ to 150, SS becomes 1.645 × 300 ≈ **494**. That is 164 units less safety stock, and **cycle stock (Q/2) is unchanged**.

### Class Q 8.2 / 11-1.1 — two SKUs, same forecast ⭐⭐⭐
Both SKUs forecast 1,000. SKU A is steady (±50) and SKU B is wild (±400). The rule is "forecast + 2 weeks of supply" for both.
**Answer: A, the rule ignores demand uncertainty.** Identical means with different variances need different buffers.
- The rule overstocks A (its buffer is far larger than ±50 needs).
- It strands service on B (its buffer is far smaller than ±400 needs).
- The fix information is **the distribution (σ or quantiles) for each SKU**, not a better point forecast.
- *Lesson: forecast the distribution, not the number.*

## 2. Regression, accuracy metrics and the confusion-matrix trap ⭐⭐
- **Regression is the forecasting workhorse.** It finds relationships ("squeeze an independent variable and the dependent one bulges, like twisting a balloon animal"). It predicts **how many**, whereas classification predicts **which class**.
  - **Features must lead, not lag.** A card issuer spotted trouble early when groceries and utilities appeared on a card previously used for electronics.
  - **Outliers distort the line.** A festival day or a promotion pulls the trend; more and cleaner data steadies it.
- **The confusion matrix** has four outcomes (TP, FP, FN, TN).
  - **Precision** = TP/(TP+FP): when it flags a spike, is it right?
  - **Recall** = TP/(TP+FN): of the real spikes, how many did it catch?
  - **F1** is their harmonic mean. Use it as the single comparison number and as the baseline for future improvement.
- **Beware the skew.** On a 1%-event problem, "always predict no" scores 99% accuracy and is useless. **Always beat a naive baseline.**
- **Ensemble the forecast.** Combine a strong average-case model with one tuned for turning points. Bagging and boosting are standard because no single learner wins everywhere.

### Class Q 8.4 — Model X vs Model Y ⭐⭐⭐
X has the lower average error. Y is worse on average but far better at flagging spikes before promotions.
**Answer: D, Model Y. It wins where it matters.**
- Average error rewards the easy middle.
- A safety-stock or promotion-readiness decision lives **in the tail and at turning points**.
- *Match the metric to the decision.* (This is the same logic as Kaveri's "simple average vs volume-weighted fill".)

**Worked numeric.** A spike-detector flags 40 weeks as "spike". 30 of them really were spikes, and there were 50 real spikes in total.
- Precision = 30/40 = **75%**.
- Recall = 30/50 = **60%**.
- F1 = 2 × 0.75 × 0.6 / 1.35 = **66.7%**.

## 3. Demand sensing — audit signals before you buy them ⭐⭐⭐
| Signal | Leads demand by | Mechanism | Verdict pattern |
|---|---|---|---|
| **Weather forecast** | days to weeks | temperature and rain drive consumption directly (beverages, ice cream, fashion) | **buy IF the horizon matches the order lead time** |
| **Promotions calendar** | weeks | price and display causally lift demand, and distort history if unmodelled | **mandatory**: both the signal AND history repair |
| **POS / channel sell-through** | days | end-consumer truth vs distorted orders: **the antidote to the bullwhip** | high value where access is negotiable |
| **Installed base & utilisation** (IoT on machines in the field) | weeks to months | machines in the field drive parts and service demand | **the spare-parts deployment's winning signal** |
| **Social / search trends** | weeks | attention precedes purchase (fashion, launches) | test rigorously; the mechanism is often flimsy |
| **Customer forecasts** | varies | incentive-laden negotiating positions | let the model weight them (recall: **zero**) |

**IoT as a demand signal.** Sensors on installed equipment (run-hours, utilisation, scheduled maintenance) tell you which parts will be consumed **before** an order arrives. That is why IoT turns spare-parts forecasting from guesswork into an engineering estimate. The same sensors feed predictive maintenance (Ch 9).

### The Signal Audit — five steps before any data purchase ⭐⭐⭐ (framework)
1. **Lead time:** does the signal arrive before the decision must be made, early enough to act on?
2. **Mechanism:** is there an honest causal story, or a correlation mined from one training window?
3. **Decision test:** does the improved prediction cross an order or capacity threshold (i.e. change an order)?
4. **Cost vs value:** acquisition plus integration cost, weighed against the decisions actually changed.
5. **Weight check:** after deployment, what weight did the model LEARN? Demote or drop the losers ruthlessly.

**Applied to Nandini's weather data.**
- Lead: weather forecasts must reach 2–3 weeks ahead if the bottling and dispatch lead time is 2–3 weeks; a 5-day forecast cannot change a 3-week order.
- Mechanism: honest (heat drives thirst).
- Decision test: does it move production or dispatch quantities in the monsoon-transition weeks?
- Cost: the subscription plus integration, weighed against the stockouts avoided in those weeks.
- Weight: review after one season.

## 4. Adaptive and "autonomous" forecasting — what the loop really is ⭐⭐⭐
- **The adaptive loop.** New observations arrive, weights update and the plan refreshes. The deployed one-step system recomputed its decision function **in minutes, weekly**. This was a **deliberate cadence** that balances responsiveness against **nervousness** (plans that churn every hour destroy execution).
- **Reinforcement-flavoured forecasting.** Where forecasts feed repeated decisions with observable outcomes (pricing, replenishment), learning can target the **decision reward** directly. Ch 8 completes this thread.
- **The "autonomous forecasting agent" claim, audited.** Strip the label and ask which of three things it is:
  - (a) **adaptive re-estimation**: mature and buyable, a feature;
  - (b) **decision-function learning**: the one-step paradigm;
  - (c) **an agent with write-access to orders**: an **AUTONOMY decision**, governed by the S4 ladder rather than being a forecasting upgrade.
- **The human role that remains.** Regime breaks (2020-class) still need human recognition and override. Guardrails and planner market knowledge are **complements, not rivals**.

### Class Q 8.3 — the most clarifying vendor question ⭐⭐⭐
The Pitch C brochure says: "continuously retrains… adjusts forecasts in real time with zero planner effort."
**Answer: B, "Does it update forecasts, or execute orders?"**
- Updating is a feature.
- Executing is an autonomy grant that needs the ladder (L1–L5), guardrails and the readiness bar.
- "Conflating them is how forecasting upgrades quietly become ungoverned agents."

## 5. The paradigm case — zero weight for the customer's forecast ⭐⭐⭐
**Fortune 150 consumer-electronics OEM** (course text Ch. 11):
- six products, contract-manufactured in Asia;
- sold through about **3,000 stores** via partners such as Walmart and Best Buy;
- deployed the **one-step planning system**, whose learned decision function weighted every input by measured usefulness.

**Headline finding:** the retail partners' own forecasts earned a **weight of ZERO**. They were historically so error-prone that the system learned to ignore them. Seasonality and the OEM's internal signals carried the weight instead.

**The sister deployment** was a semiconductor-equipment maker with **50,000 spare-part SKUs**.
- Its best signals lay **outside the demand history**: installed base, scheduled maintenance and equipment utilisation at customer sites.
- **Fill rate rose from 77% to 85% at constant inventory**, or equivalently about **$20M of inventory released** at the old fill rate.

**Two durable lessons:**
1. Let the system **price every signal by contribution**, including politically important ones.
2. The best predictors of demand are often **upstream drivers of demand**, not demand's own past.

### Class Q 8.1 — the politically important partner ⭐⭐
The partner expects its forecast to be used, but it misleads.
**Answer: D, weight it by measured contribution.**
- The interpretable weight visualisation became the tool that let the OEM **influence its partners' inventory decisions**.
- *"Signals earn their weights; the politics are managed, not obeyed." "Evidence beats etiquette when the evidence is showable."*

## 6. The wider record ⭐⭐
- **Danone / Zara.** Multi-country ML planning, and real-time trend sensing driving production. Both are **signal stories**: channel and trend data that lead demand, feeding decisions fast enough to matter.
- **The 2020 breakdown.** Lockdowns broke history-trained models en masse. Grocery demand doubled overnight in some categories while apparel collapsed, and the models kept predicting the vanished world. This is non-stationarity at planetary scale: **history-only forecasting carries a regime-change fragility** you must design for (monitoring, override, scenario plans).
- **Weather-driven planning** in beverages, ice cream and fashion works because the mechanism is honest and the lead time usable. The test is always the same: **does the signal arrive early enough to change an order?**
- **Probability forecasting in products.** Modern planning platforms (ToolsGroup and others) ship distribution forecasts as the default, so safety stocks and service levels read directly off quantiles.

## 7. Why forecasting disappoints even when accurate — four pathologies ⭐⭐⭐
1. **Multiple competing forecasts.**
   - Sales forecasts monthly in rupees/dollars to secure supply.
   - Planning forecasts weekly in units to avoid obsolescence.
   - Each retail partner forecasts separately.
   - None agree, and none improve as the period approaches. *Which one drives orders?* (Documented verbatim at the OEM.)
2. **Incentive distortion.** Every forecast is also a negotiating position: **sales inflates** (before quota-setting), **planning deflates** (for safety), and customers over-order under allocation. *The numbers carry agendas before they carry information* (Nandini's exhibit).
3. **Heuristic conversion.** "Weeks of supply" rules turn even good forecasts into bad inventory: an inflated forecast gives excess stock and a conservative one gives shortages. **The damage happens AFTER the forecast.**
4. **Point-blindness.** A single number hides the uncertainty the decision needs.

**Fix:** pathologies 1–2 are **organisational**. Accuracy cannot fix incentive distortion; **architecture and transparency** can (a single consensus number, signals weighted by evidence, a visible weight chart). Pathologies 3–4 are fixed by **distribution forecasting and quantile-based policies**.

## 8. Nandini Beverages — the case resolved ⭐⭐⭐
**Facts.** Monsoon season is ahead and three pitches are on the table:
- **Pitch A**: statistical upgrade, ₹40 L.
- **Pitch B**: ML + weather/IoT sensing, ₹1.4 cr.
- **Pitch C**: "autonomous forecasting agent", ₹2.1 cr.

Other facts:
- Sales inflates and planning deflates.
- The monsoon drives **40% of demand variance**.
- Fill-rate failures concentrate in **promo weeks and monsoon-transition weeks**.

**Model answer (numbered assumptions first).**
1. *Assume* the incumbent method has never been benchmarked against a naive (seasonal-naive) forecast on a holdout.
2. *Assume* weather feeds with a 2–3 week horizon are available and that the bottling/dispatch lead time is about 2–3 weeks.
3. *Assume* promo history is not tagged (so it is distorted).

**Analysis.**
- The failure is concentrated in promo and monsoon weeks. **That is where forecast value lives**, not in the average week.
- None of the pitches fixes the inflate/deflate politics, because that is an architecture problem: one consensus number, the model weights the inputs, and a visible weight chart.

**Verdict: a sequenced combination.**
- (i) Run a **Pitch-A-level baseline** and benchmark it, repair promo history and set a single-number S&OP process (cheap; fixes pathologies 1–3).
- (ii) Pilot **Pitch B's** weather and promo signals **only on the monsoon-transition and promo SKUs**, after a **signal audit**, with a distribution forecast feeding quantile safety stocks.
- (iii) Ask Pitch C **"update or execute?"**:
  - if it updates, it is a pricier Pitch B;
  - if it executes, it is an autonomy grant Nandini is not ready for (an L2/L3 discussion later).

**What would change the answer in 12 months:** the weather signal earning material weight and cutting monsoon-week stockouts, plus clean promo data. Then scale B, and consider bounded execution (L3) for replenishment.

## 9. Forecasting tiers — buy the tool the workload deserves (S9, S12) ⭐⭐⭐
### What each tier assumes and delivers
| Dimension | Tier 1 · **Spreadsheet (Excel)** | Tier 2 · **Open-source (Prophet, scikit-learn)** | Tier 3 · **Cloud AutoML (AWS SageMaker / Canvas)** | Tier 4 · **Sequence models (LSTM / transformers)** |
|---|---|---|---|---|
| Comfortable volume | tens to hundreds of series | thousands (scripted) | tens of thousands + | very large, rich, long histories |
| Skills assumed | spreadsheet literacy | Python + statistics | cloud admin + data engineering + FinOps | deep-learning engineering |
| Readiness assumed | clean-enough extracts | pipeline discipline (S7) | governed data platform (S2 ≥ 3.5) | **Data Maturity 3+**, long history |
| Explainability | total (every cell visible) | high (code and models open) | variable, often opaque | low |
| Cost shape | hidden (hours, errors) | skills + maintenance | subscription + consumption | compute + scarce talent |
| Governance/audit | weak (version chaos) | good if engineered | strong tooling, lock-in terms | hard to explain to a lender |

- **Excel:** exponential smoothing (Holt-Winters) is a legitimate, auditable baseline at modest scale. Recall S2: **61% of planning decisions are executed in spreadsheets beside an 11-year-old ERP**.
- **Prophet:** built at Meta to **democratise business forecasting**. It handles trend, seasonality and holidays by default. It fills the gap "between naive methods and deep learning at scale" but does not replace either at SKU level.
- **SageMaker-class AutoML** (including no-code Canvas): scale, automation and integration with the S5 platform world. **Consumption pricing, quota realities and lock-in** come with it.
- **LSTM / transformers:** need long history, rich data and high maturity. At ordinary SKU-location-week granularity, **simple methods stay embarrassingly competitive**. Running one without the pipeline and skills "isn't sophistication, it's over-tiering".
- **The frontier that is NOT yet a tier:** foundation forecasting models ("rent a pretrained forecaster"). 2026 benchmarks call them **promising, not dominant** against tuned simpler methods at operational granularity.
- **Worth watching:** **multi-agent RL coordinating replenishment** across a chain beats one smart agent alone, with **lower cost AND less bullwhip**. Coordination, not a bigger model, is where the next bullwhip gains are.

### The four tier questions (in order) and the Bake-Off Ladder ⭐⭐⭐ (framework)
1. **Count it:** your real SKU × location × frequency volume, not next year's hoped-for volume.
2. **Audit readiness:** can you trace, clean and timestamp the history this tier needs today?
3. **Name the skill:** who will run and explain it in plain words? ("Not 'we'll hire someone'.")
4. **Check governance:** does it give an auditable, explainable number when a lender, board or regulator asks?
5. **Bake it off:** run the candidate tier on your own recent data before signing any subscription.

*Accuracy joins the verdict table but does not chair it.*

**Two failure directions and two buying sins:**
- **Under-tooling at scale:** analysts hand-forecasting thousands of series weekly; error-prone, unauditable and dependent on one person (the bus factor).
- **Over-tooling above readiness:** enterprise ML idling above teams without the pipelines or skills (the [2,1,3,2,5] scorecard as a purchase order).
- **Tool-first buying:** the demo runs on curated data with expert drivers.
- **TCO blindness:** "free" Tier 2 costs skills and maintenance; Tier 3 meters consumption (the **3.2× token overrun**). Price the whole loop: **build + run + retrain + govern**.

### Class questions on tiers ⭐⭐⭐
- **Q 9.1, the 12-SKU bakery:** the answer is **B, a spreadsheet already fits**. Tiers are workload matches, not maturity badges.
- **Q 9.2, cloud AutoML beats Prophet by 2% at 6× cost** with skills Trident lacks: the answer is **A, the Prophet tier wins today**. The verdict is multi-column and should name the **conditions under which it flips**.
- **Q 9.3, a notebook must run nightly for 40,000 SKUs and feed planning by 6 a.m.:** the answer is **D, whether it runs reliably on schedule**.
- **Q 12-2.1, 60 SKUs, 4 dealerships, an Excel-only analyst, and lenders wanting an auditable rationale; an LSTM demo shows bullwhip charts:** the answer is **C, the spreadsheet/smoothing tier**. The LSTM needs Data Maturity 3+ and produces exactly the opaque output a lender does not want.

### Trident Distributors — the case resolved ⭐⭐⭐
**Facts:**
- 8,000 SKU-locations, ordered weekly;
- 2 analysts (one knows some Python);
- readiness [D3, T2, P3, O3, G3];
- ₹25 L tooling budget;
- the MD wants "what the big retailers have";
- the senior analyst's spreadsheets have run the business for 8 years.

**Answer:**
1. 8,000 weekly series is past the comfortable spreadsheet range.
2. The technology score of 2 and a single Python-capable analyst rule out cloud AutoML today (it assumes a governed platform ≥ 3.5, data engineering and FinOps).
3. So the recommendation is **Tier 2 (Prophet-class), scripted and scheduled**, with the spreadsheet kept as the **benchmark and fallback**.
4. The successor must **beat the senior analyst's forecasts on a holdout of Trident's own data**, per segment, and prove it **to the analyst and the MD** (trust design).
5. The MD's demo assumes curated data, expert operators and a governed platform.

**Flip condition (cloud in two years):** a governed data platform (T ≥ 3.5), a data engineer, volumes in the tens of thousands, and a bake-off showing that the uplift **in decisions** pays for 6× the cost.

### Prototype to production (S9) ⭐⭐
- **Promote through environments:** dev → stage ("production-sized, the last line of defence") → prod, with automated **unit, integration and acceptance tests**, plus a **model regression suite** so retraining does not break old skills.
- **Blue/green deployment:** run two environments and re-point traffic once the new one passes QA, so there is no downtime.
- **Design for spikes:** load-test about **20% above peak**, remember that **auto-scale lags about 3 minutes**, and let the **SLA** decide whether the nightly forecast lands by cut-off. "The SLA is the product." "A notebook that cannot hit the 6 a.m. handoff is not a capability."
- **Verify vs validate:**
  - Verification means the code runs.
  - Validation means it does the useful thing (usually a human check).
  - Report accuracy only after a large held-out test.
  - Keep a **model-library entry** (precision/recall/F1, framework, train/validation counts, step size, epochs).
  - Schedule retraining, because outdated models give bad predictions.
- **The major clouds differ** in which capabilities they support (clustering, anomaly detection, recommendation). Choose on the **capability matrix, not the brand**.

### The S9 lab — the three-tier bake-off
1. Tier 1 exponential smoothing in the spreadsheet; score it on a holdout and note the setup time.
2. Tier 2 Prophet on the same series; note what the defaults handled and what needed tuning.
3. Tier 3 AutoML; note its score, configuration surface, pricing basis and what stays opaque.
4. Complete the **verdict table** (accuracy vs naive, setup, cost, explainability, governance), with the **flip condition**.

### The M5 footnote ⭐⭐
ML won on aggregate accuracy, but simple, cheap methods stayed remarkably competitive **at the SKU-store level, where planning decisions are made**. The winning methods ran on **modest infrastructure**. Spreadsheets persist because they match the volume, skills and governance most teams have. "Don't let an aggregate leaderboard sell you an enterprise platform for a 200-SKU business."

## 10. Chain Reaction link — Rounds 1 & 2 ⭐⭐⭐
- **R1 (Onboarding):** manual operations, the first forecast, learning the console. Use the **distribution-not-a-number** habit from the first click.
- **R2 (Forecasting bake-off):** each company builds its own forecasting agent and chooses a build speed.
  - **FAST:** 0.85× cost, quality −18.
  - **STANDARD:** 1.0×.
  - **CAREFUL:** 1.25× cost over two rounds, quality +6.
  - There is **no failure chance** either way.
- Use the four tier questions, not the flashiest option. The trade is speed now vs agent quality for the rest of the season; a −18 quality forecaster compounds into every later planning decision. See the [Chain Reaction playbook](#/chain-reaction-playbook).

## Key takeaways (S8, S9, S11, S12 recaps 📘)
1. The decision consumes a **quantile, not a mean**. Probability forecasting turns safety stock from folklore into a costed choice.
2. The best demand signals are demand's **upstream drivers** (installed base, weather, promotions). Every signal must pass the audit: lead time, mechanism, decision impact.
3. Organisations have **several forecasts, each with an agenda**. Accuracy cannot fix incentive distortion; architecture and transparency can (the zero-weight lesson).
4. History-only models carry **regime-change fragility** (2020). Adaptive loops, monitoring and human override are design requirements.
5. "Autonomous forecasting" claims decompose under one question: **update or execute?**
6. **Tier follows the workload** (volume, readiness, skills, governance), not the demo. Bake-offs beat brochures.
7. LSTMs win with long history and high maturity; at SKU-level granularity simple methods stay competitive. Coordinating multiple agents is where the next bullwhip gains show up.

---

## Self-test
**Q1. A planner says, "Our new ML forecast is 15% more accurate, so we can cut inventory by 15%." Assess it.**
Accuracy gains reduce **σ of forecast error**, which reduces **safety stock only**. Cycle stock (Q/2) depends on the order quantity and is untouched. If safety stock is 30% of the inventory, a 15% cut in σ trims about 15% of SS, i.e. about 4.5% of the total. The claim confuses Q with S.

**Q2. Cu = ₹90, Co = ₹30. Demand ~ Normal(500, 100). What is the optimal order quantity?**
CR = 90/120 = 0.75, and z(0.75) ≈ 0.674. Q* = 500 + 0.674 × 100 ≈ **567 units**.

**Q3. A vendor offers social-media trend data for a B2B industrial-fastener business. Run the signal audit.**
Lead time is unclear. The mechanism is flimsy (fastener buyers don't trend on social media). The decision test fails (it won't cross an order threshold). The cost is a subscription plus integration for no changed decisions. Verdict: don't buy. Installed-base or customer production-schedule data would be better.

**Q4. Why did the OEM's system give the retailers' forecasts zero weight, and what did the OEM do with that?**
The forecasts were historically error-prone and incentive-laden, so the model learned they added nothing. The OEM used the **interpretable weight chart** to influence partners' inventory decisions: evidence beats etiquette.

**Q5. A 300-SKU distributor with one Excel analyst and no data engineer is pitched SageMaker. Recommend.**
Tier 1/2 now: smoothing in Excel, or Prophet if the analyst can script, benchmarked against naive. SageMaker assumes a governed platform, data engineering and FinOps. Flip condition: volume in the thousands-plus, a data platform ≥ 3.5, and a bake-off uplift that pays for the cost in decisions.

**Q6. "Our autonomous forecasting agent adjusts in real time with zero planner effort." What do you ask, and why?**
"Does it update forecasts, or execute orders?" Executing is an autonomy grant (S4 ladder, guardrails, readiness). Updating is a feature to bake off.

**Q7. Give two reasons Model Y (worse on average, better at spikes) can be the right choice.**
Stocking and promo decisions live in the tail; a missed spike costs lost sales and expediting, which outweighs small average errors. The metric must match the decision, e.g. pinball loss at the service quantile, or recall on spikes.

**Q8. How do the four forecasting pathologies split between technology fixes and organisation fixes?**
Multiple forecasts and incentive distortion are organisational: one consensus number, transparent weights. Heuristic conversion and point-blindness are technical/policy: distribution forecasts and quantile safety stock.
