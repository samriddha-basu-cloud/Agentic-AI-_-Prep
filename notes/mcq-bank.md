# MCQ Bank — every class question, plus exam-style extras
Your faculty asked **"one question at a time"** in every session 📘, and those class questions are the best predictor of how the case questions will be judged. **Part A** reproduces **all class questions from Sessions 1–20** with the official answer and the one-line WHY. **Part B** adds **exam-style questions** on numericals, SCM basics and Chain Reaction. Turn on **Self-test** (top bar or press `T`) to hide the answers and reveal them one by one.

> The exam itself is case-based, not MCQ. But each class question is a mini-case: the reasoning in the WHY lines is exactly what earns marks in a long answer.

---

## Part A — Class questions, Sessions 1–20 📘

### Session 1 — AI in operations: claims, Q vs S, decisions

**Q1. A vendor demo shows software that reads supplier emails, drafts replies and, once approved, posts confirmed delivery dates into your ERP. In precise course vocabulary it is: (a) A predictive AI model (b) A generative AI copilot (c) An agentic AI system (d) Robotic process automation**
**Answer: (c) An agentic AI system** — it perceives, reasons and ACTS on systems of record. Approval-gated action puts it low on the autonomy scale. A copilot stops at drafting; RPA follows fixed rules. *Precise vocabulary is the first defence against agent-washing.*

**Q2. A distributor holds ₹8 cr cycle stock (weekly truckloads) and ₹2 cr safety stock. A vendor claims its forecasting AI will cut total inventory 30%. Which single calculation kills or saves the claim? (a) Size the safety-stock share of total inventory (b) Compare the vendor's price to savings (c) Check the model's accuracy benchmark (d) Compute total logistics cost**
**Answer: (a) Size the safety-stock share** — forecasting attacks S, not Q. S = 2/10 = 20% < 30%, so the claim fails arithmetic before any question of model quality arises. *Follow the cost pool, not the technology.*

**Q3. Forecast error improves from ±40 to ±15 units, but orders must still be placed in full pallets of 240. Most likely business impact? (a) Large inventory savings (b) Better customer service (c) Little to no business impact (d) Lower transport cost**
**Answer: (c) Little to no business impact** — decisions are discrete. Accuracy pays only until the decision stops changing. *Precision pays only when a decision changes.*

**Q4. A CEO proposes replacing the planning department with "a thousand small agents" next quarter. Strongest reason it fails TODAY, even if each agent works? (a) Agents are too expensive (b) Regulators would prohibit it (c) Agents amplify each other's actions (d) Planners would strike**
**Answer: (c) Agents amplify each other's actions** — decentralisation needs bounded scopes and coordination structure (shared signals, circuit breakers). *Stability is mechanism design, not intelligence.*

**Q5. A consultant says you are "behind": 44% of companies deploy supply-chain AI and the agentic market will hit $53B by 2030. Correct executive response? (a) Approve, the market has spoken (b) Wait for the market to mature (c) Reject AI entirely (d) Ask which adopters show measurable value**
**Answer: (d) Ask which adopters show measurable value** — only about 30% of adopters advance beyond copilots, and about 95% of GenAI pilots show no P&L impact. Adoption measures purchasing, not value.

**Q6. A vendor's AI "learns your business and answers any question". The soundest first test is: (a) Which decision it changes, and its benchmark (b) Training-set size (c) Whether it uses deep learning (d) Vendor's customer count**
**Answer: (a) Which decision it changes, and its benchmark** — capability is proven by the decision it moves and the naive benchmark it beats. *Judge mechanism and benchmark, not momentum.*

### Session 2 — Readiness I: data and technology

**Q7. A pilot promises "real-time response to demand shifts", but 70% of sales data arrives by overnight batch. Which data-quality dimension binds? (a) Accuracy (b) Validity (c) Timeliness (d) Uniqueness**
**Answer: (c) Timeliness** — quality dimensions are per use case. 24-hour-old data is fine for weekly planning and fatal for real-time sensing.

**Q8. Spend analytics shows the largest supplier at 4% of spend, but a master-data audit finds it duplicated across six vendor records. What did the analytics measure? (a) Nothing wrong (b) The supplier should be dropped (c) A minor finance issue (d) Record-keeping, not true concentration**
**Answer: (d) Record-keeping, not true concentration** — humans merge duplicates mentally; models take records literally and agents transact on them (uniqueness). *Data defects compound at machine speed.*

**Q9. Two firms buy the same demand-sensing model. Firm A has one owner per data domain and nightly DQ reports; Firm B has neither. Best predictor of success? (a) Firm A's data governance and accessibility (b) Vendor's benchmark accuracy (c) GPU capacity (d) Firm size**
**Answer: (a) Firm A's data governance** — identical technology, opposite outcomes. *Foundations before intelligence; semantic before agentic.*

**Q10. One vendor-facing API credential was phished last year, there is no inventory of which systems talk to which, and the CIO proposes purchasing agents with ERP write access. Verdict? (a) Approve (b) Approve with a "be careful" prompt (c) Block until API inventory and access controls exist (d) Outsource security review**
**Answer: (c) Block until API inventory and access controls exist** — write-capable agents extend the attack surface, and prompts are not controls. *Autonomy raises every bar.*

**Q11. One firm deployed an LLM planning assistant over unified data and existing optimisation models (success); another bolted it onto fragmented spreadsheets (pilot death). The difference? (a) Model quality (b) Prompt skill (c) Prior foundations in place (d) Budget**
**Answer: (c) Prior foundations** — data preparation consumes 60–80% of successful projects.

**Q12. Scorecard [Data 2, Masters 1, Architecture 3, Security 2, Compute 5]. Ambition ceiling and first move? (a) Deploy agents (b) Hire data scientists (c) Freeze AI for two years (d) Predictive pilot on the cleanest domain first**
**Answer: (d) Predictive pilot on the cleanest domain** — masters at 1 poison everything and security at 2 forbids write access. Compute 5 is a stranded asset. *The scorecard sets the ceiling.*

### Session 3 — Readiness II: process and organisation

**Q13. Match to decision level and AI posture: (a) 5-year network redesign; (b) AI-assisted S&OP scenarios; (c) autonomous reorder of spares under ₹50,000. (a) a-operational/automate, b-strategic/augment, c-tactical/delegate (b) a-strategic/input-only, b-tactical/augment, c-operational/delegate (c) all strategic (d) a-tactical, b-operational, c-strategic**
**Answer: (b)** — strategic = input only; tactical = augment; operational, frequent and reversible = the delegation frontier.

**Q14. Before scoping any model to "add AI to procurement", a structured method insists you first: (a) Pick a cloud vendor (b) Map the process (c) Hire a data scientist (d) Estimate accuracy**
**Answer: (b) Map the process first** — *standardise the process, preserve the judgement.*

**Q15. Design A shows planners the back-tested record and allows ±15% adjustments with reasons; Design B mandates unmodified use. Behavioural evidence predicts: (a) B wins (b) A wins, bounded control keeps trust (c) No difference (d) Both fail**
**Answer: (b) A wins** — algorithm aversion is reduced by slight modifiability. *Trust is designed, not demanded.*

**Q16. Each planner will supervise 12 agent workstreams, "checking anything odd". Research says: (a) Fail, vigilance and skills decay (b) Works well (c) Only if salaries rise (d) Works if agents rarely err**
**Answer: (a) Fail** — the ironies of automation (+14% mental effort, +19% overload for close monitors). Oversight is not a safety net; hard guardrails are.

**Q17. Planners are paid on service and turns; corporate adds "recommendation adherence". Rational behaviour? (a) Full adoption (b) Resignations (c) Rebellion (d) Adherence tied to their metrics**
**Answer: (d)** — when a measure becomes a target it stops measuring. *Incentives eat algorithms.*

**Q18. A business case promises "25% inventory reduction in 6 months, company-wide", set before any diagnostic. Gate-compatible rewrite? (a) Keep it (b) Remove targets (c) Cut to 20% (d) Scoped, baselined and evidence-gated**
**Answer: (d)** — *transform in survivable doses* (the Continental Parts lesson).

### Session 4 — Agentic AI systems

**Q19. "Our AI agent reviews your inventory dashboard every morning and emails a prioritised action list." Is it an agent? (a) Yes, it acts autonomously (b) No, it only recommends; nothing is executed (c) Yes, if the emails are good (d) No, because it runs on a schedule**
**Answer: (b)** — an agent needs goal ownership plus tool-mediated action within an envelope. This one is a recommender (agent-washing).

**Q20. A negotiation agent closes deals with 2,400 tail suppliers inside category-manager mandates. The manager's job now is: (a) Gone (b) Reviewing every deal (c) Designing the envelope and auditing outcomes (d) Negotiating the big deals only**
**Answer: (c)** — *the mandate IS the management.* Reviewing every deal would delete the economics.

**Q21. Your replenishment agent and your distributor's ordering agent react to each other's orders. Prediction? (a) Order oscillation, unless signals are shared (b) Stable efficiency (c) Deadlock (d) Nothing**
**Answer: (a)** — decentralised LLM agents mostly amplify bullwhip.

**Q22. A system prompt says "Never exceed ₹5 lakh per order; never order from unapproved suppliers". Sufficient control? (a) Yes (b) Yes, if long enough (c) No, prompts are not enforceable controls (d) Agents can't be controlled**
**Answer: (c)** — *guardrails live outside the model.* Hard limits belong in the surrounding system.

**Q23. Rank for agentic suitability: (a) strategic partnership negotiation; (b) tail-spend reorders; (c) robot routing in your own warehouse. (a) a>b>c (b) equal (c) b>a>c (d) c>b>a**
**Answer: (d) c > b > a** — the five-factor screen: frequency, reversibility, data/feedback, rule clarity, stakes.

**Q24. Where should a human sit in an "autonomous" returns agent? (a) Nowhere (b) On every case (c) On low-confidence, high-impact cases only (d) Only after failure**
**Answer: (c)** — an engineered escalation path.

### Session 5 — AI platforms

**Q25. A multi-month GPU waitlist in your region; two vendors blame each other. Response? (a) Pick whoever promises faster (b) Sequence around the shared constraint (c) Cancel (d) Build a data centre**
**Answer: (b)** — upstream physics binds every hyperscaler. *Every platform is a supply chain.*

**Q26. An average CPG firm wants to build its own planning platform "like the famous 24-hour retailer". Build vs buy is decided by: (a) Budget (b) Engineering pride (c) Real differentiation only (d) Vendor relationships**
**Answer: (c)** — *own the differentiating loop; rent the rest.*

**Q27. Copilot token spend is 3.2× forecast after six months. Was the platform wrong? (a) No, fix usage discipline (b) Yes, switch (c) Ban the copilot (d) Ignore it**
**Answer: (a)** — FinOps for AI. TCO includes consumption governance.

**Q28. Before building a custom OCR pipeline for invoices, ask: (a) Which DL framework (b) Does a good service already exist? (c) How many GPUs (d) Project name**
**Answer: (b)** — commodity capabilities are mature APIs.

**Q29. A cheaper, feature-rich platform can't enforce per-agent spend limits or produce complete action logs, and you plan an L4 procurement agent. Verdict? (a) Buy it (b) Buy and add governance later (c) Disqualified, no envelope enforcement (d) Negotiate a discount**
**Answer: (c)** — *filters in order; governance before features.*

**Q30. Supplier-risk scores feed EU-plant renewals; the vendor says compliance "is handled by the platform". You must verify: (a) Nothing (b) ISO certificates (c) Data residency only (d) The provider/deployer duty split, which is yours**
**Answer: (d)** — oversight of your USE is yours by law (EU AI Act). This underpins Trishul A4.

### Session 6 — ML foundations

**Q31. You're asked to validate a k-means customer clustering's accuracy. What's wrong? (a) There's no ground truth to be accurate against (b) k-means is outdated (c) Too little data (d) Use supervised only**
**Answer: (a)** — *the decision, not a metric, validates unsupervised work.*

**Q32. You have three years of sales but no stockout-corrected true-demand field. Core difficulty? (a) Algorithm choice (b) Cloud vendor (c) GPUs (d) The label you need doesn't exist yet**
**Answer: (d)** — frame the decision and construct the label first.

**Q33. An 87%-accurate price model: Team 1 displays predictions; Team 2 auto-buys inventory. What decides whether 87% is enough? (a) Industry standard (b) Architecture (c) The decision's cost and reversibility (d) Training-set size**
**Answer: (c)** — the Zillow lesson.

**Q34. A delay model's backtest is stellar, but one feature is goods-receipt date. What happened? (a) Nothing (b) Weight it higher (c) More data (d) Data leakage, the feature isn't knowable in time**
**Answer: (d)** — the most common cause of the demo-to-production cliff.

**Q35. A model scores 92%, the naive rule 90.5%, and orders come in full-truck multiples. Verdict? (a) Excellent (b) Unproven, barely beats naive (c) Failure (d) Needs deep learning**
**Answer: (b)** — *no model without a naive benchmark.*

### Session 7 — Tools lab

**Q36. A model beats naive by 6% overall, wins on staples, loses on promotions and new items. Deploy: (a) Everywhere (b) Nowhere (c) Where it wins; keep naive elsewhere (d) Retrain until it wins everywhere**
**Answer: (c)** — champion–challenger by segment.

**Q37. An analyst's model beats the incumbent by 8% but runs from manual exports on her laptop. What does the firm own? (a) Little durable, a one-person demo (b) A capability (c) An 8% cost reduction (d) A deployable API**
**Answer: (a)** — *a model in a notebook is not a capability.*

**Q38. A churn model shows 99% accuracy and only 3% churn. Most likely problem? (a) Excellent (b) Accuracy is misleading; check for leakage (c) Too few features (d) Wrong language**
**Answer: (b)** — "never churn" already scores 97%.

### Sessions 8 & 11 — Demand forecasting

**Q39. Two SKUs both forecast 1,000; A swings ±50, B ±400; the rule stocks forecast + 2 weeks of supply for both. What is wrong? (a) The rule ignores demand uncertainty (b) Nothing (c) B needs a better point forecast (d) Discontinue A**
**Answer: (a)** — *forecast the distribution, not the number; the quantile IS the decision.*

**Q40. Pitch C: "Our autonomous agent retrains and adjusts forecasts in real time with zero planner effort." Most clarifying question? (a) Which DL architecture? (b) Does it update forecasts, or execute orders? (c) Customer count? (d) Is it GenAI?**
**Answer: (b)** — execution is an autonomy grant (S4 ladder), not a forecasting feature.

**Q41. Model X has lower average error; Model Y is worse on average but far better at flagging pre-promotion spikes. For safety-stock and promo readiness choose: (a) X (b) Moving average (c) Whichever trains faster (d) Y**
**Answer: (d) Y** — the metric must match the decision; the decision lives in the tail.

**Q42. A politically important partner's forecasts mislead the model. What should the system do? (a) Use them anyway (b) Average them (c) Exclude all external data (d) Weight them by measured contribution**
**Answer: (d)** — the zero-weight finding. *Signals earn their weights; politics are managed, not obeyed.*

### Sessions 9 & 12 — Forecasting tiers

**Q43. Cloud AutoML beats Prophet by 2% on Trident's data at 6× the cost, with skills Trident lacks. Verdict? (a) Prophet tier wins today (b) Cloud wins (c) Excel wins (d) Run both forever**
**Answer: (a)** — the verdict is multi-column; name the flip condition.

**Q44. A 12-SKU bakery asks whether to move from Excel to cloud ML "to modernise". Honest advice? (a) Yes (b) A spreadsheet already fits this (c) Only SageMaker (d) No forecasting needed**
**Answer: (b)** — tiers are workload matches, not maturity badges.

**Q45. A notebook must run nightly for 40,000 SKUs and feed planning by 6 a.m. The critical production question is: (a) Chart library (b) R-squared (c) Rewrite in a new language (d) Whether it runs reliably on schedule**
**Answer: (d)** — the SLA is the product.

**Q46. 60 SKUs, 4 dealerships, an Excel-only analyst, lenders want an auditable rationale; an LSTM demo shows bullwhip charts. Buy: (a) LSTM tier (b) AutoML regardless of skills (c) Spreadsheet/smoothing tier (d) Prophet always**
**Answer: (c)** — the LSTM needs Data Maturity 3+ and gives the opaque output a lender won't accept.

### Session 10 — Inventory optimisation

**Q47. A vendor's backtest shows DRL beating your tuned basestock by 20%; a myopic rule is known to be within about 5% of optimal. The 20% most likely contains: (a) A breakthrough (b) Overfitting or a weak baseline (c) Proof to replace planners (d) Nothing verifiable**
**Answer: (b)** — the maximum headroom is about 5%. *Benchmarks with a theory-informed ceiling.*

**Q48. A spare part sells 0,0,0,4,0,0,2,0 units. Judging models by weekly MAPE is broken because: (a) MAPE is undefined on zero actuals (b) It's fine (c) Use daily MAPE (d) Use R²**
**Answer: (a)** — use calibrated distributions and service per rupee of inventory.

**Q49. Option (a): improve forecasts 15% and keep the weeks-of-supply rule. Option (b): keep forecasts and optimise the policy on the distribution and costs. More valuable? (a) a (b) Buy DRL (c) Equal (d) b, the conversion step is where value dies**
**Answer: (d)** — *optimise the policy, not the forecast.*

**Q50. Vendor plan: "shadow mode 4 weeks, then full control of spare-parts ordering". Missing? (a) Nothing (b) Bounds, fallback and a real evaluation (c) Longer shadow only (d) More data**
**Answer: (b)** — four weeks of intermittent demand is statistically empty.

**Q51. An RL agent beats the classical policy by 18% in simulation on two years of stable demand. Essential safeguard? (a) Deploy now (b) Cage it with a benchmark and guardrails (c) More layers (d) Switch cloud**
**Answer: (b)** — *learned policies wear proven guardrails.*

### Session 13 — Predictive maintenance

**Q52. A model flags a bearing at 68% failure risk within 2 weeks, but every bearing is inspected weekly and replaced if worn. Act? (a) Yes, always above 50% (b) No, the weekly inspection already catches it; the prediction doesn't change the decision (c) Daily inspections until 90% (d) Ignore models entirely**
**Answer: (b)** — a prediction earns its keep only when it changes what or when you decide.

### Session 14 — Logistics

**Q53. A road lane loses 40% capacity, the Mumbai zone is about to stock out, express is costly and rail is too slow. Do: (a) Hold and wait (b) Split: express now, rail as backfill (c) Reroute everything via another RDC (d) Cancel and reallocate**
**Answer: (b)** — rebalance the mix in real time.

### Session 15 — Optimisation

**Q54. Identical cost weights for all zones; the solver routes nearly all by rail and fill slips in the zone with 40% of premium-margin sales. What went wrong? (a) Solver error (b) A higher cost weight or service floor for the high-value zone was needed before solving (c) Override lane by lane (d) Unavoidable**
**Answer: (b)** — *a perfectly solved LP with the wrong mandate gives a perfectly wrong plan.*

### Session 16 — NLP procurement

**Q55. A fixed tuning budget can push one clause type to the top accuracy tier: (a) Payment terms (b) Address formatting (c) Penalty and indemnification (d) Contact details**
**Answer: (c)** — misreads create uncapped exposure. *The accuracy bar scales with what the clause decides.*

### Session 17 — Token economics

**Q56. A negotiation agent's run cost doubles after repricing; quality unchanged. Do: (a) Keep as-is (b) Retire now (c) Compare value-per-decision with cost-per-decision, then tune or retire (d) Hope prices fall**
**Answer: (c)** — tune before you retire.

### Session 18 — GenAI scenarios

**Q57. GenAI outputs "a celebrity post triggers a 400% spike in one paint colour in 72 hours"; someone wants to fund flex capacity now. Do: (a) Fund it (b) Discard all GenAI output (c) Label it stretch, check mechanism and base rate, seek a cheap reversible mitigation (d) Regenerate 100× and take the mode**
**Answer: (c)** — vivid ≠ evidenced. Label before you act.

### Session 19 — Multi-agent coordination

**Q58. One agent orders +15% "to be safe"; two tiers up another doubles its order. Best single preventive change? (a) Faster processors (b) Every agent sees the same real end-customer demand (c) Local negotiation only (d) More watchers**
**Answer: (b)** — *coordination beats speed.*

### Session 20 — Responsible AI

**Q59. An L4 forecasting agent outperformed all season; two days before the board, training data is found to under-represent your fastest-growing market. Do: (a) Say nothing until after (b) Patch quietly (c) Drop to L2, log and disclose, and bring it to the board as a governance finding (d) Wait for next quarter's audit**
**Answer: (c)** — *guardrails only count if you use them when it costs you something.*

---

## Part B — Exam-style extras (numericals, SCM basics, Chain Reaction) 📗

**Q60. Cycle stock ₹30 cr, safety stock ₹10 cr. A vendor claims 40% inventory reduction from forecasting. Maximum possible reduction from forecasting alone: (a) 40% (b) 33% (c) 25% (d) 10%**
**Answer: (c) 25%** — S/(Q/2 + S) = 10/40. A perfect forecast removes only S.

**Q61. D = 10,000/yr, S = ₹500 per order, H = ₹40 per unit per year. EOQ ≈ (a) 354 (b) 500 (c) 250 (d) 1,000**
**Answer: (b) 500** — √(2 × 10,000 × 500 / 40) = √250,000 = 500.

**Q62. σ weekly = 100, L = 4 weeks, z = 1.65. Safety stock ≈ (a) 165 (b) 330 (c) 660 (d) 400**
**Answer: (b) 330** — 1.65 × 100 × √4.

**Q63. Halving lead time (all else equal) cuts safety stock by about: (a) 50% (b) 29% (c) 71% (d) 0%**
**Answer: (b) 29%** — SS ∝ √L, and 1 − 1/√2 ≈ 0.29.

**Q64. Cu = ₹80, Co = ₹20. The newsvendor critical ratio and the stocking quantile: (a) 0.25 (b) 0.5 (c) 0.8 (d) 0.2**
**Answer: (c) 0.8** — 80/(80 + 20). Stock the 80th percentile.

**Q65. Zones: A 10,000 units at 70% fill, B 2,000 at 95%, C 2,000 at 95%. The simple average is 86.7%. The volume-weighted fill is: (a) 86.7% (b) 77.1% (c) 80% (d) 90%**
**Answer: (b) 77.1%** — (7,000 + 1,900 + 1,900)/14,000. *An average can hide the mix.*

**Q66. Variance of consumer demand 200, factory orders 3,000. Bullwhip ratio: (a) 1.5 (b) 15 (c) 6 (d) 0.07**
**Answer: (b) 15.**

**Q67. A spike detector flags 50 weeks, 35 correctly; there were 70 real spikes. Precision and recall: (a) 70%, 50% (b) 50%, 70% (c) 70%, 70% (d) 35%, 50%**
**Answer: (a) Precision 35/50 = 70%; recall 35/70 = 50%.**

**Q68. An agent costs ₹3 L/month for 600 decisions, each worth ₹400. Ratio and action: (a) 0.8×, tune first then retire if still below 1 (b) 1.25×, keep (c) 0.8×, keep (d) 2×, keep**
**Answer: (a)** — cost per decision ₹500 vs value ₹400.

**Q69. A missed failure costs ₹40 L and an unnecessary early repair ₹2 L. Act when failure probability exceeds about: (a) 5% (b) 20% (c) 50% (d) 95%**
**Answer: (a) ≈4.8%** — 2/(2 + 40).

**Q70. Express ₹500/unit, rail ₹150/unit. 1,000 units are needed, 300 urgently. Cost of the split vs all-express: (a) ₹2.55 L vs ₹5 L (b) ₹5 L vs ₹2.55 L (c) ₹1.5 L vs ₹5 L (d) equal**
**Answer: (a)** — 300 × 500 + 700 × 150 = 1.5 L + 1.05 L = ₹2.55 L.

**Q71. In Chain Reaction, company value is: (a) profit + reputation + trust (b) profit × reputation × trust (c) cash × trust (d) fill × profit**
**Answer: (b)** — governance is the multiplier you feel late.

**Q72. In Chain Reaction, the distMode setting MIX (rail in the mix) is: (a) Always available (b) Locked until tech maturity 3 (c) Only for EVs (d) Available from Round 1**
**Answer: (b).**

**Q73. Monthly decision tokens in Chain Reaction: (a) 12 (b) 24 (c) 48 (d) unlimited — with 2 tokens to generate a plan and 1 to regenerate**
**Answer: (b) 24.**

**Q74. A below-gate agent build in Chain Reaction: (a) is blocked (b) runs at full cost for a fraction of the effect, with cut build odds (c) is free (d) is automatically upgraded**
**Answer: (b)** — sequence beats speed.

**Q75. Which archetype won the Chain Reaction season? (a) Transformation theatre (b) Foundations, not run (c) Compounders (d) Lean operators**
**Answer: (c) Compounders** — B12-Titans (#1) and A7-Kimi K3 (#2) built on laid foundations and kept operating.

**Q76. Unrouted plant stock in Chain Reaction: (a) stays at the plant (b) auto-pushes to the plant's home RDC by road (c) is scrapped (d) goes by rail**
**Answer: (b)** — this is why "file a distribution plan" is an operating must (A2-Doomsday's 338 cars; Kaveri).

**Q77. Rail in Chain Reaction is: (a) ~25% cheaper than road, booked a month ahead, charged whether used or not (b) more expensive than road (c) unlimited (d) same-day**
**Answer: (a).**

**Q78. The FAST build option in Chain Reaction gives: (a) 0.85× cost at quality −18 (b) 1.25× cost at quality +6 (c) no change (d) a failure chance**
**Answer: (a)** — CAREFUL is 1.25× over two rounds at +6; neither option carries a failure chance.

**Q79. The four elements of the Q-learning update include all EXCEPT: (a) learning rate α (b) reward r (c) discount γ (d) the confusion matrix**
**Answer: (d).**

**Q80. Which tool is a Java constraint-satisfaction planning engine using metaheuristics with hard and soft scores? (a) Prophet (b) OptaPlanner (c) RapidMiner (d) SageMaker**
**Answer: (b) OptaPlanner** — OR-Tools is Google's suite of LP/MIP, CP-SAT and VRP solvers.

**Q81. The domain-tuned vs general LLM accuracy on contract-clause risk was: (a) 94.7% vs 79.3% (b) 99% vs 95% (c) 80% vs 60% (d) equal**
**Answer: (a)** — grounding matters more than fluency.

**Q82. McKinsey's agentic-procurement pilot: efficiency gain vs value captured: (a) 20–30% vs 1–3% (b) 5% vs 5% (c) 50% vs 30% (d) 1–3% vs 20–30%**
**Answer: (a)** — the efficiency-capture gap.

**Q83. Share of firms with governance mature enough for autonomous agents (S20): (a) ~20% (b) ~50% (c) ~80% (d) ~95%**
**Answer: (a) ~20%** — "that gap is where incidents live".

**Q84. In the spare-parts deployment, fill rose at constant inventory from: (a) 77% to 85% (b) 85% to 95% (c) 60% to 77% (d) 89% to 91%**
**Answer: (a)** — or about $20M inventory released at constant service.

**Q85. Which is NOT a bullwhip cause (Lee et al.)? (a) Demand-signal processing (b) Order batching (c) Price fluctuations (d) Sharing POS data with suppliers**
**Answer: (d)** — sharing POS is a cure.
