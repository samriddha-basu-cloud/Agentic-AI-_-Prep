# Ch 9 — Predictive Maintenance & Digital Twins (Session 13)
**Syllabus unit 5 📘:** *Self-adaptive Maintenance using Agentic AI — predictive & prescriptive ML examples using TensorFlow; link with digital twin platforms.*
**Session 13 📘:** "From Vibration to Verdict." Sensor sequences lead to failure prediction, then prescriptive action, then **fidelity-for-purpose** digital twins. It led into **Chain Reaction Round 3: Aftermarket & Maintenance**.

> **Exam use:** two tests decide every maintenance or twin question.
> (1) **Does the prediction change a decision, or its timing?** If not, it is informationally idle.
> (2) **Twin-Now / Twin-Later**: decision-changing, failure cost, data readiness, fidelity needed, then a verdict.
> Sensors and twins are **infrastructure bets made before the model proves its value**.

---

## 1. Sensors are just another sequence ⭐⭐⭐
- **One model, any sequence.** A sequence model trained on demand history can, with **no change to its architecture**, read vibration, temperature or pressure instead, and forecast "how many days until the machine breaks".
- **Telemetry is a time series:** vibration, bearing temperature, oil particulate counts, sampled every few seconds instead of every week.
- **The target is Remaining Useful Life (RUL),** not "will it fail?" but "**how many hours are left?**". A binary alarm gives no room to plan; RUL gives a window to schedule work and position parts.
- **The real gate is infrastructure, not model sophistication.** Demand data already lives in your ERP. Sensor data needs **installing, wiring and streaming**, a cost you take on **before the model helps at all**.
- **Tools 📘:** TensorFlow/Keras LSTM or 1D-CNN models on sliding windows of sensor readings; survival models; anomaly detection (unsupervised) where failures are rare and unlabelled.

### The maintenance maturity ladder 📗
| Type | Trigger | Pros | Cons |
|---|---|---|---|
| **Reactive (run-to-failure)** | breakdown | no planning cost | unplanned downtime, safety risk, expediting |
| **Preventive (time-based)** | calendar or run-hours | simple, plannable | replaces healthy parts; misses early failures |
| **Condition-based** | threshold on a sensor (vibration > x) | acts on the actual state | late warning, single-signal |
| **Predictive** | ML-predicted RUL / failure probability | plans ahead, fewer surprises | needs sensors, data, labels (failures are rare) |
| **Prescriptive** | predicted failure → **recommended action** (when, which part, which crew, where to stock the part) | closes the loop to the decision | needs optimisation and a twin; an autonomy question |

### Class Q 3.1 (S13) — the 68% bearing flag ⭐⭐⭐
The model says 68% failure probability within 2 weeks. The protocol already **inspects every bearing weekly and replaces any showing wear**.
**Answer: B, no. The weekly inspection already catches this, so the prediction doesn't change the decision.**
- *A prediction earns its keep only when it changes what you'd decide, and when, not just what you'd know.*
- This is also the first step of the Twin test.

## 2. From forecast to fix, from sensor to simulation ⭐⭐⭐
- **Predicting RUL is half the job.** What matters is **when to schedule maintenance and where to pre-position the part**, a **scheduling and sourcing problem**, not a forecasting one.
- **Predict-then-optimise vs decision-focused:**
  - Predict-then-optimise forecasts RUL, then hands it to a separate scheduler.
  - **Decision-focused** trains the prediction with the scheduling cost built in. Errors that would cause a missed failure (costly) are weighted more than errors causing an early swap.
- **Digital twins make "then what?" concrete.** A twin is a **live virtual replica** fed by real data, on which you test an intervention **before committing in the real world** (change a schedule, reroute a line, alter a network).
- **Fidelity is the judgement call.** A twin only needs to answer **the ONE question you're asking**; a full physics model of every bolt is usually overkill. Build to **fidelity-for-purpose, not maximum realism**.

### Kinds of digital twin 📗
- **Asset twin:** one machine; RUL and what-ifs.
- **Process / line twin:** throughput and bottlenecks.
- **Network / supply-chain twin:** plants, DCs, lanes. Used for network design and disruption what-ifs, and it sits beneath the one-step paradigm (Ch 8).

## 3. Practice — collapsing the gap between knowing and acting ⭐⭐⭐
- An **IoT-triggered spare-parts network 3D-prints the specific part predicted to fail**, based on sensor data. The gap from "it's about to break" to "the part is on site" shrinks **from weeks to days**.
- **Siemens** runs digital twins across its own factories and customers' lines, simulating changes **before touching physical equipment**.
- **ASCM's 2026 research** named digital twins **the primary enabler of supply-chain resilience**.
- **The payoff is the time collapse**, not the sensor or the model alone. Value = (downtime avoided + parts expediting avoided + inventory of slow spares reduced) − (instrumentation + data + model + process change).

**Inventory link (Ch 7–8).** Installed-base and utilisation signals from the same sensors drove the **77 → 85% fill** in the 50,000-SKU spare-parts deployment. **Predictive maintenance is also a demand signal for spares.**

## 4. The Twin-Now / Twin-Later Test ⭐⭐⭐ (framework)
| # | Step | Question |
|---|---|---|
| 1 | **Decision-changing** | Would a better prediction actually change what you'd do, or when? **If no, stop.** |
| 2 | **Failure cost** | Is the downtime, safety or warranty cost of this failure mode high enough to justify the spend? |
| 3 | **Data readiness** | Do you already have the sensor stream, or are you building instrumentation from zero? |
| 4 | **Fidelity needed** | Can a **lightweight simulation of just the relevant subsystem** answer your what-if? |
| 5 | **Verdict** | **Twin-now** (build it), **twin-later** (park it), or a **simulation-lite substitute**. |

### Worked application (exam style)
A bottling line's filler motor fails about twice a year. Each failure costs 18 hours of downtime at ₹1.5 L/hour contribution, plus ₹4 L of emergency parts and labour. The current protocol is a monthly visual check. Instrumentation, platform and model would cost ₹22 L once plus ₹5 L/year.

1. *Assumptions:* failure frequency stays at 2/yr; prediction catches 70% of failures with enough lead to schedule repair in a planned 4-hour window; the planned repair costs ₹1 L of parts.
2. **Cost per failure today** = 18 × 1.5 + 4 = **₹31 L**, so ₹62 L/yr.
3. **With PdM:** caught failures (1.4/yr) cost 4 × 1.5 + 1 = ₹7 L each = ₹9.8 L. Missed failures (0.6/yr) cost ₹31 L each = ₹18.6 L. The total is **₹28.4 L/yr**.
4. **Saving** = 62 − 28.4 = ₹33.6 L/yr; net of running cost it is **₹28.6 L/yr**, so the **payback is ≈ 0.8 year** on ₹22 L.
5. Step 1 passes, because the monthly visual check would not catch the failure in time. Step 2 passes (high cost). Step 3: data has to be built. Step 4: an asset-level model suffices; no full line twin is needed.
6. **Verdict: twin-now at asset level (simulation-lite),** with a 6-month review of catch rate, and keep the monthly check as a fallback.

## 5. Common traps ⭐⭐
- **Predicting what you already catch** (the bearing question): an idle prediction.
- **Rare failures, few labels:** use anomaly detection, physics-informed features, pooled fleets, and judge by **catch rate at a given false-alarm rate** (precision/recall), not accuracy (99% "no failure" is trivial).
- **False alarms erode trust.** Too many early swaps and the technicians ignore the alerts. Set the threshold by the **cost ratio** of a missed failure to an unnecessary swap.
- **Twin gold-plating:** a full physics model when a queue simulation of one subsystem answers the question.
- **Sensors last:** buying the model before wiring the data stream.
- **No action path:** an alert without a scheduled slot, a crew or a part on hand. Prescriptive means the part and the slot are lined up.

**Threshold numeric.** A missed failure costs ₹31 L and an unnecessary early swap costs ₹1.5 L. Act when p(failure) > Co/(Co + Cu) = 1.5/(1.5 + 31) ≈ **4.6%**. The 68% bearing flag would clear that bar, but the decision is already covered by the weekly inspection, so it still doesn't change anything. **Test 1 comes before the cost ratio.**

## 6. Chain Reaction link — Round 3: Aftermarket & Maintenance ⭐⭐⭐
- Your telemetry investment only pays off if it changes a real decision downstream, exactly like the bearing question.
- Two catalogue agents carry it:
  - **PRD_MAINT_2/3**: Predictive & Prescriptive Maintenance (production family).
  - **DIS_NET_2/3**: Network Design & Digital Twin (distribution family).
- **Build the L2 specialist first; L3 only as an upgrade on top of it.**
- Check the **foundation gate (D·P·T)** before building. A below-gate build runs at full cost for a fraction of the effect. See the [Chain Reaction playbook](#/chain-reaction-playbook).

## Key takeaways (S13 recap 📘)
1. Sequence models don't care what the sequence is: demand and vibration are the same problem to the network.
2. RUL prediction only pays off when it **changes a scheduling or sourcing decision**, not just your knowledge.
3. Digital twins should be built to **fidelity-for-purpose**, not maximum realism.
4. Sensors and twins are **infrastructure bets made before the model proves its value**, not after.

---

## Self-test
**Q1. Why is RUL a better target than a binary "will fail" alarm?**
RUL gives a time window to schedule the repair, book the crew and pre-position the part. A binary alarm says only "soon", which leaves no room to plan.

**Q2. A plant replaces every pump seal on a fixed 6-month cycle and has had no seal failures in 5 years. A vendor offers PdM for the seals. Run Twin test step 1–2.**
Step 1: would a prediction change the decision? Possibly yes, if it extended seal life and cut parts cost. Step 2: the failure cost is currently near zero (no failures), so the value lies only in parts and labour saved from longer intervals. It is probably **twin-later**, unless seal costs are material.

**Q3. What does "fidelity-for-purpose" mean? Give an example.**
Model only what the question needs. To decide whether to add a second filler, a queue/throughput simulation of that line is enough. A bolt-level physics twin is overkill.

**Q4. A missed failure costs ₹20 L and an early swap ₹2 L. Above what predicted failure probability should you act?**
Act when p > 2/(2 + 20) ≈ **9.1%**.

**Q5. How does predictive maintenance connect to inventory planning?**
Predicted failures and installed-base utilisation are leading demand signals for spare parts: pre-position the predicted part, cut emergency freight and safety stock, and raise fill (the 77 → 85% deployment, IoT-triggered 3D printing).

**Q6. Why are sensors "an infrastructure bet made before the model proves its value"?**
Unlike demand data in the ERP, sensor data does not exist until you install, wire and stream it. The cost is sunk before any model is trained, so step 3 of the Twin test (data readiness) often decides the timing.
