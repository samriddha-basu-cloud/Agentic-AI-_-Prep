# Rapid Revision — the night before the exam
Everything high-yield on one page: the answer method, the frameworks by trigger, the numbers to quote, the formulas and the Chain Reaction lessons. Each row points to the full explanation.

## ⭐⭐⭐ The exam in one box 📘
- **Format:** a case study with exhibits (some irrelevant, some defective). **Section A** is diagnostics (calculations, data triage, exposing claims). **Section B** is design (rank, choose, mandate, gate). There is **no standalone theory**; numericals are straightforward; basic SCM concepts are required; **Chain Reaction** gets emphasis.
- **Rule 1:** every verdict, ranking or recommendation **opens with "Assumptions: A1. … A2. … A3. …"**. An unstated assumption costs marks; a stated one earns them.
- **Rule 2:** **show units and arithmetic.** One clean calculation beats three vague ones.
- **Skeleton (A-N-V-C-D-T):** Assumptions → Number → Verdict → Confront the strongest counter-evidence → Design (mandate or gate: metric, constraint, trigger, L-level, owner) → Test (frozen baseline, success threshold, counter-metric, demotion trigger).
- **Defect patterns to expose:**
  - cherry-picked month;
  - trend hidden in an average;
  - activity reported as outcome;
  - insurance logic run backwards;
  - totals that don't add up;
  - stale or contradicted figures;
  - vanity items;
  - evidence laundering (another firm's results).

See the [Exam playbook](#/exam-playbook).

## ⭐⭐⭐ Trigger → framework (the picker)
| If the case says… | Reach for | Chapter |
|---|---|---|
| "AI will cut inventory X%" | **Q vs S** (S share caps the claim) + **Four-Question Claim Audit** | [Ch 1](#/ch01-ai-in-operations-and-scm) |
| "more accurate forecast" | **Precision pays only when a decision changes** (pallets, trucks) | Ch 1 |
| duplicates, latency, missing fields | **Six DQ dimensions**; binding dimension per use case | [Ch 2](#/ch02-ai-readiness-data-technology) |
| a readiness score [x,x,x,x,x] | **Five-pillar scorecard sets the ambition ceiling**; predictive first on the cleanest domain | Ch 2 |
| planners override or rebel; a board-deck target | **Trust design** (±15% with reasons); **phased roadmap with gates**; incentives | [Ch 3](#/ch03-ai-readiness-process-organisation) |
| choose between pilots | **Pilot-selection matrix** (value, feasibility, blast radius) | Ch 3 |
| "agent", "autonomous" | **Agent-washing test**, **autonomy ladder L1–L5**, **suitability screen**, **guardrails outside the model** | [Ch 4](#/ch04-agentic-ai-systems) |
| platform choice, GPU shortage, token overrun | **Six filters in order**, build/buy/blend, FinOps | [Ch 5](#/ch05-ai-platforms) |
| "92% accurate model" | **ML Framing Canvas**, naive benchmark, leakage, error cost both ways | [Ch 6](#/ch06-machine-learning-for-operations) |
| new data (weather, POS, IoT) | **Signal audit** (lead, mechanism, decision, cost, weight) | [Ch 7](#/ch07-demand-forecasting) |
| "autonomous forecasting agent" | **Update or execute?** | Ch 7 |
| Excel vs Prophet vs SageMaker vs LSTM | **Tier matching / bake-off ladder** | Ch 7 |
| "DRL beats our policy by 20%" | **~5% theory ceiling** + **guardrailed pilot (6 elements)** | [Ch 8](#/ch08-inventory-optimisation) |
| sensors, RUL, digital twin | **Does it change the decision?** + **Twin-now / twin-later** | [Ch 9](#/ch09-predictive-maintenance-digital-twins) |
| lane shock, mode choice | **Split shipment**; mode mix under capacity | [Ch 10](#/ch10-logistics-routing-optimisation) |
| optimiser starved a zone | **Strategy lives in the objective** → **Optimizer Mandate Checklist** / **Mandate Card** | Ch 10 |
| contract NLP, negotiation agent | **Clause-stakes checklist**; bounded autonomy (Pactum) | [Ch 11](#/ch11-nlp-procurement-token-economics) |
| agent bill spiked | **Tune-or-retire**; caps in code; efficiency-capture gap | Ch 11 |
| GenAI scenarios | **Scenario portfolio checklist**; GenAI for range + OR for rigour; antifragility | [Ch 12](#/ch12-genai-design-multi-agent) |
| agents reacting to each other | **Collaboration paradox** → shared signal, smoothing, trained coordination | Ch 12 |
| bias, EU AI Act, "who answers?" | **ACAP**; provider vs deployer; step down and disclose | [Ch 13](#/ch13-responsible-ai-ethics) |

## ⭐⭐⭐ Numbers to quote (with the source session)
| Number | Meaning | Session |
|---|---|---|
| **~30% / ~95%** | of AI adopters move beyond copilots / of GenAI pilots show no P&L impact | S1 |
| **60–80%** | of effort in successful AI projects is data preparation and pipeline | S2, S7 |
| **61%** | of planning decisions executed in spreadsheets beside an 11-year-old ERP | S2 |
| **+14% / +19%** | mental effort / overload for close AI monitors (ironies of automation) | S3 |
| **±15%** | bounded override that keeps trust | S3 |
| **3.2×** | token spend vs forecast (FinOps) | S5 |
| **42,840** | M5 series; ML won overall, simple methods competitive at SKU-store level | S6 |
| **>$500M, ~25%** | Zillow write-down, staff cut | S6 |
| **0** | weight learned on retail partners' forecasts | S8 |
| **77% → 85%** | fill at constant inventory (~$20M released), 50,000 spare-part SKUs | S8, S10 |
| **15–20% behind / within ~5% of optimal** | fresh DRL vs a myopic rule / myopic rule vs optimal | S10 |
| **700+** | Global 2000 firms running enterprise inventory optimisation | S10 |
| **~70 hours** | self-play to super-human Go (RL creates its own data) | S10 |
| **FAST 0.85×/−18 · STANDARD 1.0× · CAREFUL 1.25×/+6** | Chain Reaction build options | S12 |
| **~20% above peak / ~3 min** | load-test margin / auto-scale lag | S9 |
| **~25%** | rail cheaper than road (Chain Reaction) | S14 |
| **94.7% vs 79.3%** | domain-tuned vs general LLM on clause risk | S16 |
| **~80%** | CPOs planning GenAI within 3 years (EY) | S16 |
| **~3%, +35 days, 64–68%** | Walmart–Pactum savings, term extension, close rate | S1, S16 |
| **20–30% vs 1–3%** | efficiency vs captured value (McKinsey) | S17 |
| **24 / 2 / 1 / 1–4 / 2 / 4** | tokens per month / plan / regenerate / upkeep / terminate / actions per round | S17 |
| **~18 weeks** | Walmart Trend-to-Product design-to-shelf cut | S18 |
| **~20%** | firms with governance mature enough for autonomous agents | S20 |
| **10%** | DeepFleet robot travel-time cut; 1M robots | S1, S14 |

## ⭐⭐⭐ Formulas (all "straightforward")
| What | Formula |
|---|---|
| Inventory | **Q/2 + SS**; forecasting changes only SS |
| Max forecasting saving | **SS ÷ (Q/2 + SS)** |
| Safety stock | **z·σ·√L** (z: 90% 1.28, 95% 1.645, 97.5% 1.96, 99% 2.33) |
| Reorder point | **d·L + SS** |
| EOQ | **√(2DS/H)**; at EOQ ordering cost = holding cost |
| Newsvendor | **CR = Cu/(Cu + Co)** → stock that quantile |
| Carrying saving | **Δinventory × carrying rate** |
| Weighted fill | **Σ(volume × fill) / Σ volume** |
| Contribution forgone | **lost units × (price − variable cost)** |
| Break-even saving rate | **annual cost ÷ addressable pool** |
| Precision / recall / F1 | **TP/(TP+FP); TP/(TP+FN); 2PR/(P+R)** |
| Bullwhip ratio | **Var(orders) / Var(demand)**, compounding by tier |
| Act-on-alarm threshold | **p > Co/(Co + Cu)** (early-action cost ÷ total) |
| Cost per decision | **run cost ÷ decisions**, compared with value per decision |
| Chain Reaction value | **profit × reputation × trust** |
| Q-learning | **Q ← Q + α[r + γ·maxQ′ − Q]** |

## ⭐⭐⭐ The 12 frameworks you must be able to write from memory
1. **Four-Question Claim Audit**: what baseline? measured how? which cost pool? what decision changes?
2. **Six DQ dimensions**: accuracy, completeness, consistency, timeliness, uniqueness, validity.
3. **Five-pillar readiness**: data quality, master data, architecture, security, compute (1–5).
4. **Pilot-selection matrix**: value × feasibility × blast radius. **Gate**: success metric + counter-metric + owner + demotion trigger + frozen baseline.
5. **Autonomy ladder**: L1 inform · L2 recommend · L3 bounded act + escalate · L4 autonomous + monitor · L5 full.
6. **Suitability screen**: frequency, reversibility, data/feedback, rule clarity, stakes (20+ / 12–19 / < 12).
7. **ML Framing Canvas**: decision, target, data and features (known at decision time), error costs, baseline.
8. **Signal audit**: lead time, mechanism, decision test, cost vs value, weight check.
9. **Guardrailed pilot**: scope, bounds, fallback, evaluation, trust loop, ownership.
10. **Mandate Card**: service floor, cost ceiling, mode priority, shock trigger, review cadence (plus the **Optimizer checklist**: service targets per zone, cost weights, review rule, re-solve trigger, verify the fit).
11. **Tune-or-retire**: measure cost, measure value, compare, tune, retire. **Clause stakes**: list, decision, bar, tier, exception.
12. **ACAP**: Accountability, Capability limits, Auditability, Proportionality, Post-incident learning (S19: Alignment, Process oversight, Coordination).

Plus: **Twin-now test** (decision-changing, failure cost, data readiness, fidelity, verdict) and the **Scenario portfolio** (generate wide, label, select two, specify survival, guard the label). Full set in [Course frameworks](#/course-frameworks).

## ⭐⭐⭐ Chain Reaction in ten lines
1. **Network:** 3 plants → 4 RDCs → 7 zones; HATCH/SUV/EV.
2. **Physics:** unrouted stock **auto-pushes to the plant's home RDC by road**, and zones pull only from their own RDC. **File a distribution plan.**
3. **Modes:**
   - **rail** is ~25% cheaper, booked a month ahead and charged whether used or not, so book base load;
   - **road** is the default;
   - **express** is for urgent top-ups.
   - **MIX is locked until Tech 3.**
4. **Dials:** distCover, distSafety, distFront (SPREAD/FRONT), distMode (ROAD/MIX). **Set policy, not flows.**
5. **Tokens:** 24 per month; plan 2, regenerate 1; upkeep 1–4 per agent; terminate 2; max 4 actions per round. Decide on **cost per decision**.
6. **Foundations D·P·T** gate every agent. **Below gate = full cost, a fraction of the effect, cut odds.**
7. **Chips** are allocated against contracted volume, with **fees on the full book**. Size the book to real demand.
8. **Value = profit × reputation × trust.** Breaches and incidents hit the multipliers.
9. **Archetypes:**
   - **Compounders won**: B12-Titans #1 (21 agents, rail every round, trust 110); A7-Kimi K3 #2 (zero below-gate).
   - **Lean operators**: A8 #3 on 6 agents.
   - **Transformation theatre** (8th–18th) and **foundations not run** (11th–20th) trailed.
10. **Lessons:** **sequence beats speed · building is not operating · governance is the multiplier you feel late · efficiency is a real strategy.**

Full detail in the [Chain Reaction playbook](#/chain-reaction-playbook).

## ⭐⭐ Past papers in six lines
- **Trishul A1:** base 13.6 cr; the 30% claim = 4.08 > S of 2.6, so it fails; ceiling 19.1%; carrying value 0.49 vs a 1.6 cr fee.
- **Trishul A2:** 11.0 + 2.6 + 1.2 = 14.8 ≠ 15.2; 480/2,890 = 16.6% duplicates, not "< 2%".
- **Trishul A3/B1:** pool 58.2 cr, break-even 1.9%; vendor-master dedup first; ranking P2 > P3 > P1; L3; EU AI Act deployer oversight on P3.
- **Kaveri A1:** the simple average 73.7% hides a slide to 58.2% (weighted 72.5%); M4 cherry-picked; "foundations L4" is activity; no-rail is insurance logic backwards.
- **Kaveri A2:** the loss is physics, not luck. Forgone contribution ≈ ₹11 cr (5.8× the reported loss, 18× the congestion charge).
- **Kaveri B1:** Distribution Planning Agent at L3, fill objective, cash ≥ −15 cr, triggers, CSCO owner, 60-day review vs the M5 baseline.

Full answers: [Trishul](#/pyq-trishul) · [Kaveri](#/pyq-kaveri).

## ⭐⭐ Basic SCM you must not miss
- **Bullwhip** causes: demand-signal processing, batching, price swings, shortage gaming. **Cures:** POS sharing, VMI/CPFR, smaller batches, EDLP, allocation by past sales.
- **Push vs pull; efficient vs responsive** (Fisher: functional products need efficient chains; innovative products need responsive ones).
- **Inventory types:** cycle, safety, pipeline (in transit = d × L), seasonal, anticipation.
- **KPIs:** fill rate (weighted), OTIF, inventory turns and days, cash-to-cash, perfect order, forecast accuracy/bias, cost-to-serve.
- **SCOR:** Plan, Source, Make, Deliver, Return, Enable.
- **S&OP:** one consensus number linking demand, supply and finance monthly. This is the cure for "multiple forecasts with agendas".

See [Ch 0: SCM fundamentals](#/ch00-scm-fundamentals).

## ⭐ Phrases that score
- "Forecasting attacks safety stock, not cycle stock."
- "Precision pays only when a decision changes."
- "Foundations before intelligence."
- "Trust is designed, not demanded."
- "Guardrails live outside the model."
- "Autonomy is granted per decision."
- "The mandate is the management."
- "A perfectly solved LP with the wrong mandate gives a perfectly wrong plan."
- "Optimise the policy, not the forecast."
- "Learned policies wear proven guardrails."
- "Signals earn their weights."
- "The accuracy bar scales with what the clause decides."
- "Tune before you retire."
- "Label before you act."
- "Coordination beats speed."
- "Guardrails only count when you use them when it costs you something."
- "Sequence beats speed; building is not operating."
