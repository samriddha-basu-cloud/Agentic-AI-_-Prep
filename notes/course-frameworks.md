# Course Frameworks — every tool from the 20 sessions, ready to apply
Your faculty: **"Please go through all the frameworks covered during the sessions"** 📘. Each session ended with "The tools you take with you" — this page collects **every one of them** in the order taught, with the steps, when to use it, scoring rules, and a one-paragraph applied example in exam style. The [Exam Playbook](exam-playbook.md) has the "if the case asks X, use Y" picker.

> Quick index: 1 Four-Question Claim Audit · 2 AI Adoption Roadmap (6 stages) · 3 Readiness barriers (4 categories) · 4 Six data-quality dimensions · 5 Data & Tech Readiness Scorecard · 6 Predictive vs Agentic requirements delta · 7 Three decision levels · 8 Process readiness agenda · 9 Three non-negotiables · 10 Phased roadmap with gates · 11 Pilot-selection matrix · 12 Scoping methods (design, systems, scenario, Delphi, BSC) · 13 Five generations of automation · 14 Six building blocks of an agent · 15 Design patterns · 16 Autonomy ladder L1–L5 · 17 Governance stack · 18 Agentic suitability screen · 19 AI stack (5 layers) · 20 Build vs buy vs blend · 21 Six platform filters · 22 Learning taxonomy · 23 ML framing canvas · 24 Seven-step ML workflow + capability checklist · 25 Probability forecasting & newsvendor · 26 Signal audit · 27 Tier matching & bake-off ladder · 28 Inventory policy ladder · 29 Guardrailed pilot · 30 Twin-now/twin-later · 31 Mandate card · 32 Optimizer mandate checklist · 33 Clause-stakes checklist · 34 Tune-or-retire · 35 Scenario portfolio · 36 Multi-agent stability fixes · 37 ACAP governance

---

## 1. The Four-Question AI Claim Audit ⭐⭐⭐ (S1) 📘
"Apply this audit to every vendor pitch, case study and headline for the rest of the course."
| # | Question | Ask |
|---|---|---|
| 1 | **Mechanism?** | What exactly does the AI do differently — and is there a well-grounded reason it should work here? |
| 2 | **Cost pool?** | Which cost/revenue pool does it touch, and how big is that pool? (**Q vs S logic — "is there juice in this lemon?"**) |
| 3 | **Decision changed?** | Does the output change an actual decision, or map to the same action as before? (**Rain-forecast reward function**) |
| 4 | **Evidence?** | Named deployment, independent numbers — does it survive **out-of-sample and out-of-pilot**? (MIT's 95% warning) |

**Applied (Trishul P1):** Mechanism — better forecasts shrink safety stock. Pool — S = ₹2.6 cr of ₹13.6 cr (19.1%), carrying value ₹0.49 cr/yr. Decision — full-truck multiples mean many forecast gains map to the same truck. Evidence — a European reference customer, not Trishul's data. → **Claim fails at Q2 before Q4 is even needed.**

**The two structural limits of forecasting (S1):** (1) forecasting touches only part of cost — inventory = cycle stock from batch Q + safety stock S; a perfect forecast removes only S; most inventory sits in Q, driven by pallets, trucks, MOQs. (2) Diminishing returns — **archery reward** (every gain pays) vs **rain-forecast reward** (80% vs 95% rain → same umbrella). "124 vs 159 units forecast — either way you ship one 240-unit pallet."

## 2. AI Adoption Roadmap — six stages (S1) 📘
**1 Ideation → 2 Defining the project → 3 Data curation & governance → 4 Prototyping → 5 Production → 6 Thriving with the AI lifecycle.** Ideation asks: *What problem are we solving? How do we operate today? How could AI benefit us?* Value is proven by small, recoverable failures — **"fail quickly, fail regularly, fail tiny."** (Sessions 2–3 = stage 3 and the organisation; Sessions 6–10 = ML and deployment stages.)

## 3. Four categories of readiness barriers (S2) 📘
| Category | Contents |
|---|---|
| **Data & technology infrastructure** | data quality and accessibility; legacy systems and integration; security and privacy |
| **Cost & sustainability** | high implementation cost; regulatory volatility (EU AI Act, China labelling, Canada AIDA); energy and water footprint |
| **Talent & organisational capability** | skills gaps, citizen data scientists, resistance to change, complacency and de-skilling risk |
| **Strategy, leadership & collaboration** | executive expectations, silver-bullet mentality, missing AI strategy, functional silos |

## 4. Six dimensions of data quality — SCM edition ⭐⭐⭐ (S2) 📘
| Dimension | Definition | SCM failure example |
|---|---|---|
| **Accuracy** | values reflect reality | system says 240 on hand, cycle count finds 175 → phantom inventory triggers false replenishment |
| **Completeness** | no critical gaps | lead-time field blank for 40% of SKUs → planning falls back to a 14-day default |
| **Timeliness** | fresh enough for the decision | POS arrives weekly; demand sensing needs daily — "the AI just smooths stale data" |
| **Consistency** | same fact, same value everywhere | 8801-A in ERP, 8801A in WMS, "8801 A" in the supplier portal = three products |
| **Uniqueness** | one record per entity | same vendor six times with different terms → spend analytics undercounts by 60% |
| **Validity** | values conform to rules | negative lead times and 1900-01-01 dates silently skew the model |

**Rule:** quality dimensions are **per-use-case requirements** — 24-hour-old data is fine for weekly planning and fatal for real-time sensing. **Diagnose the binding dimension before the model.** (Trishul: timeliness binds P1 — 71% of revenue on a 26-hour batch; uniqueness binds P2 — 18% duplicate vendors.)

## 5. Data & Technology Readiness Scorecard — five pillars ⭐⭐⭐ (S2) 📘
| Pillar | Evidence to score 1–5 |
|---|---|
| **1 Data quality** | six dimensions on critical entities (items, vendors, customers, lead times); profiling stats, cycle-count accuracy |
| **2 Master data & governance** | ownership assigned? golden records? dedup rate? DQ KPIs on a dashboard someone is paid to watch? |
| **3 Architecture & integration** | batch vs streaming; API coverage of core systems; % of planning still in spreadsheets; lineage documented? |
| **4 Security & compliance** | API/model attack surface managed; access controls; readiness for EU AI Act / DPDP-class regulation |
| **5 Compute & tooling** | cloud/GPU in the standard workflow; MLOps maturity; can a model reach production without heroics? |

**Read the profile as a roadmap.** [2,1,3,2,3] → masters first, architecture second, no autonomous agents yet. Class Q 2.5: **[Data 2, Masters 1, Architecture 3, Security 2, Compute 5] → "predictive pilot on the cleanest domain first"** — masters at 1 poisons everything; security at 2 forbids write access; compute 5 is a **stranded asset**. "The scorecard sets the ceiling; money cannot shortcut discipline." (Trishul's [2,2,3,3,4] → same reading: predictive/narrow pilots, fix masters before any write-access agent.)

## 6. Predictive vs Agentic — the requirements delta (S2) 📘
| Requirement | Predictive model (e.g. forecast) | Autonomous agent (e.g. replenishment agent) |
|---|---|---|
| Data freshness | batch (daily/weekly) often fine | streaming / near-real-time — agent acts on current state |
| Data access | read-only extracts | governed **read AND write** APIs into systems of record |
| Integration | one-way pipeline to dashboards | two-way: MCP-style tool connections, transaction posting |
| Identity & permissions | data-science team credentials | **per-agent identity, least-privilege scopes, spend limits** |
| Observability | model accuracy monitoring | full action logs, decision traces, rollback paths, **kill switch** |
| Failure mode | wrong number on a screen | **wrong purchase order in the ERP — errors are transactions** |
"**Autonomy raises every bar.**" Use this table as the go/no-go tool for any agent proposal.

## 7. Three levels of supply chain decisions — and AI fit ⭐⭐ (S3) 📘
| Level | Examples | Cadence & owner | Realistic AI role today |
|---|---|---|---|
| **Strategic** | network design, NPI, portfolio & pricing, MTS/MTO/ATO, postponement | quarterly–annual; executives | **auxiliary insight / input only** — futures unlike the past defeat history-trained models |
| **Tactical** | S&OP/SIOP, seasonal capacity & logistics planning, production planning | weekly–monthly; planning orgs | **useful assistant — augment planners**, don't automate them away |
| **Operational** | dynamic procurement, lead-time quotation, inventory setting, order fulfilment & shipment | daily–hourly; front line + systems | **strongest fit — delegate** (frequent, repetitive, data-rich), but noisy environments demand robustness |
Class Q 3.1: AI network redesign = strategic/input-only; AI-assisted S&OP = tactical/augment; autonomous reorder of spares < ₹50,000 = operational/delegate.

## 8. The process-readiness agenda (S3) 📘
1. **Map reality, not the SOP** (process mining on event logs; "you cannot hand an agent a process you cannot describe").
2. **Standardize where variation is waste** (harmonize O2C, P2P variants first).
3. **Redesign, then automate** — no lift-and-shift; self-learning AI **amplifies** existing limitations.
4. **Respect embedded expertise** — codify the WHY, not just the flow.
5. **Decide what agents inherit** — per step: **automate** (rules), **augment** (AI recommends, human decides), or **delegate** (agent acts within an envelope).
Also: Who/What/How/Why process interviews; **before/after information-flow** diagrams; idea bank; score each process against five stakeholders (customers, vendors, employees, investors, governments) — low customer-value, high-effort steps are automation targets; rank ideas by **impact × effort** (capital > 20% of profit = large).

## 9. Three non-negotiables of successful transformations (S3) 📘
1. **Senior executive sponsorship plus multi-functional resources** (named executives with skin in the game).
2. **Enforced data management and process adherence** — "governance with teeth".
3. **Phased rollout with active stakeholder participation** inside and outside the enterprise.

## 10. Phased AI adoption: Crawl, Walk, Run — with gates ⭐⭐⭐ (S3) 📘
| Phase | Duration | Content |
|---|---|---|
| **Phase 0 · Foundation** | 0–6 months | data & process readiness fixes on ONE value stream; governance stood up; **baseline metrics frozen**; talent assessment; quick BI wins fund credibility |
| **Phase 1 · Pilot** | 3–9 months | 1–2 use cases: **HIGH feasibility × HIGH value × LOW blast radius**; predictive/augmenting first, human-in-the-loop; success gate measured against the **frozen baseline** |
| **Phase 2 · Scale** | 9–24 months | winning pilots → adjacent categories, sites, regions; industrialize (MLOps, retraining, adoption KPIs in scorecards, reskilling) |
| **Phase 3 · Transform** | 18 months + | redesign the operating model around proven capability; autonomy envelopes widen; org restructures around exceptions |
**Each gate = value evidence + readiness re-score + explicit autonomy decision.** "Skipping gates is how you join the predicted 40% of cancelled agentic projects." Class Q 3.5: a board-deck target ("25% inventory cut in 6 months, company-wide") must be rewritten as **scoped, baselined and evidence-gated** — and guarded against gaming (cut inventory, buy stockouts).

## 11. Pilot-selection matrix ⭐⭐⭐ (S3) 📘
| Criterion | Ask | Green flag | Red flag |
|---|---|---|---|
| **Value at stake** | which cost/revenue pool, how big? | material pool, measurable baseline | vanity metric, no baseline |
| **Data feasibility** | Session 2 scorecard on THIS use case | clean, owned, streaming where needed | masters dirty, data political |
| **Decision impact** | does output change real decisions? | clear action mapping | rain-forecast redundancy |
| **Blast radius** | worst case if it is wrong? | reversible, bounded, low-value transactions | irreversible, customer-facing |
| **Sponsor & adoption** | who owns it, who must use it? | named sponsor, users co-design | orphaned, imposed on users |
| **Learning value** | what capability does it build? | reusable data products, skills | dead-end point solution |
The Trishul paper calls this "**pilot-selection logic (value, feasibility, blast radius)**".

## 12. Scoping methods (S3) 📘
- **Design thinking** for the new: persona → what they do/think/feel/say → user stories "*As a <role> I want <feature> so that <benefit>*".
- **Systems thinking** for the existing: boundaries (input/output/stress), subsystems aligned to the whole.
- **Scenario planning** for the uncertain: scan **STEEP** (Social, Technological, Economic, Environmental, Political), ~7 scenarios → four in a 2×2.
- **Delphi**: anonymous multi-round expert surveys defuse the loudest-voice bias.
- **Balanced Scorecard**: Financial, Customer, Internal Process, Learning & Growth — so one metric is not maximised to another's ruin.

## 13. Five generations of "automation" (S4) 📘
**1 Scripts & macros** (fixed keystroke replay) → **2 RPA** (rule-based bots on structured tasks: PO creation, invoice matching) → **3 ML-assisted** (predictions embedded in workflows; human decides) → **4 GenAI copilots** (drafting, summarising, what-if; human initiates every action) → **5 Agentic AI** (goal-directed: perceive, plan, act through tools, learn — inside guardrails). "The step-change at stage 5: the system **owns a goal and a decision loop**, not just a task."
**Agent-washing test (Class Q 4.1):** goal ownership + tool-mediated action within an envelope. "Emails your planner a prioritized action list" = **not an agent** (only recommends). Reads supplier emails, drafts replies and **posts confirmed dates into ERP once approved** = **an agentic system** low on the autonomy scale (Class Q 1.1).

## 14. Inside an agent — six building blocks (S4) 📘
**SENSE** Perception (ERP/WMS/TMS, IoT, EDI, email, market feeds) · **THINK** Reasoning engine (LLM with ReAct, chain-of-thought) · **THINK** Planning (decompose goals, sequence tool calls, replan) · **REMEMBER** Memory (short-term context + long-term stores, vector DBs, RAG) · **ACT** Tool use (APIs, databases, solvers, code; standardised via **MCP**) · **GOVERN** Guardrails & orchestration (permissions, spend limits, policy checks, escalation, audit logs, orchestration layer).

## 15. Agent design patterns (S4) 📘
**Reflection** (self-critique before acting) · **Tool use** (math to solvers, facts to databases) · **Planning / orchestrator-worker** (planner dispatches specialist workers) · **Multi-agent collaboration** (peer roles negotiate/vote) · **Human-in-the-loop** (approves each action) vs **human-on-the-loop** (monitors exceptions while the agent executes) — chosen per decision class by the autonomy ladder.

## 16. The Five-Level Autonomy Ladder ⭐⭐⭐ (S4) 📘
| Level | Agent does | Human does | SCM example |
|---|---|---|---|
| **L1 · Assist** | retrieves, summarizes, drafts | decides and acts | copilot drafts a supplier email; planner edits and sends |
| **L2 · Recommend** | analyses and proposes ranked actions | approves each action | reorder proposals with reasons; planner clicks approve |
| **L3 · Act with approval gates** | executes routine cases end-to-end | approves exceptions & thresholds | auto-PO under ₹5 L within contract; above → human |
| **L4 · Bounded autonomy** | owns the decision inside an envelope | monitors dashboards, audits, tunes envelope | Pactum negotiations inside mandate; DeepFleet routing |
| **L5 · Self-improving** | learns, adapts policy, coordinates peers | governs goals, ethics, kill switch | autonomous planning networks (mostly aspirational, 2026) |
"Autonomy is a managerial choice per decision-class: climb on evidence, capped by readiness and blast radius." Bounded override is the **adoption mechanism** (algorithm aversion remedy: let users adjust ±10–15%) — "what L2–L3 should feel like".

## 17. The governance stack for autonomous agents ⭐⭐⭐ (S4) 📘
1. **Hard constraints** — spend limits, approved-supplier lists, contract envelopes, rate limits, forbidden actions — **enforced outside the model, in code and permissions, not in the prompt**.
2. **Identity & least privilege** — each agent has its own credentials; "an agent with tool access is an attack vector with a budget".
3. **Observability** — decision traces, action logs, explanation on demand, override mechanisms.
4. **Escalation & kill switch** — confidence and anomaly thresholds route to humans; every loop has a documented stop.
5. **Accountability assignment** — name the human owner of every agent's outcomes **before** go-live ("it's not me, it's the machine").
Class Q 4.3: a system prompt saying "never exceed ₹5 lakh, never use unapproved suppliers" is **not sufficient** — prompts are not enforceable controls ("the prompt shapes behaviour; the envelope bounds it"). Cautionary file: **Air Canada** chatbot (invented policy, airline liable), **$1 Chevy Tahoe** (prompt injection), **McDonald's AI drive-thru** (bounded pilot with a working exit gate).

## 18. The Agentic Suitability Screen ⭐⭐⭐ (S4) 📘
Score 1–5 each:
| Factor | High score when… |
|---|---|
| **Frequency & volume** | high-frequency, high-volume decisions amortise the agent investment |
| **Reversibility** | a wrong action can be undone cheaply (low blast radius) |
| **Data & feedback** | rich state visibility and **fast** outcome feedback |
| **Rule clarity** | the mandate can be specified (limits, levers, walk-aways) — "if experts cannot state the envelope, the agent cannot inherit it" |
| **Stakes & politics** | low stakes; strategic, irreversible, politically loaded decisions stay human |
**Total: 20+ = strong agentic candidate (start L3–L4); 12–19 = augment (L1–L2); below 12 = keep human, revisit later.** Class Q 4.5: warehouse robot routing > tail-spend reorder > strategic supplier negotiation ("physical autonomy first, transactional next, strategic never — so far").
*Worked scoring (Trishul):* P2 tail spend — frequency 5, reversibility 4, feedback 4, rule clarity 5, stakes 5 (low) = **23 → L3–L4**. P3 risk-scored EU renewals — frequency 2 (quarterly), reversibility 2, feedback 2, rule clarity 3, stakes 2 = **11 → keep human (L2 at most)**.

## 19. The AI technology stack — five layers (S5) 📘
**1 Silicon & hardware** (NVIDIA GPUs, TSMC >60% of fab, ASML sole EUV supplier, ~70% rare-earth processing in China) → **2 Infrastructure** (hyperscale data centres, power, cooling, GW-scale demand) → **3 Foundation models** (GPT, Claude, Gemini, Llama — rented via API) → **4 Platform & orchestration** (Azure AI Foundry, AWS Bedrock/SageMaker, Vertex AI; agent runtimes, guardrails, MLOps) → **5 Applications** (SAP, Oracle, Dynamics; Blue Yonder, Kinaxis, o9; Pactum, ToolsGroup). "Most SCM organisations buy at layers 4–5 — but power, cost and risk cascade down from layers 1–2." **Every platform is a supply chain; audit it like a supplier.**

## 20. Build vs Buy vs Blend (S5) 📘
- **Buy** (suite features, SaaS agents): fastest; vendor carries model risk; best when the use case is common and differentiation LOW; costs: subscription creep, roadmap dependency.
- **Build** (custom agents on hyperscaler platforms): exactly your process; best when the decision IS your edge (DeepFleet, JD.com) and talent exists; costs: talent scarcity, MLOps burden, you own every failure.
- **Blend** — "buy the backbone, build the edge". **"Own the differentiating loop; rent the rest."** First ask: **does a good service already exist?** (Class Q 5.6). Build-vs-buy is decided by **real differentiation only** (Class Q 5.3). Platform fates: TradeLens shut down (no industry collaboration), Walmart Element (build for control), Ocado Smart Platform (build until it becomes the product).

## 21. Choosing a platform — six filters IN ORDER ⭐⭐ (S5) 📘
**1 Use-case fit** (start from roadmap pilots) → **2 Data gravity** (compute near systems of record) → **3 Governance fit** (agent identity, guardrails, audit, regional compliance — can it enforce YOUR autonomy ladder?) → **4 Ecosystem & skills** (Microsoft shop vs AWS-native vs SAP country) → **5 TCO & pricing risk** (licences + tokens + integration + change; price volatility; exit costs) → **6 Lock-in & optionality** (MCP, model-agnostic runtimes, egress terms).
Class Q 5.2: a cheaper feature-rich platform that cannot enforce per-agent spend limits or produce complete action logs is **disqualified** for an L4 procurement agent — "governance before features". Class Q 5.4: token spend 3.2× forecast → **fix usage discipline (FinOps)**, not the platform.

## 22. The learning taxonomy (S6) 📘
| Paradigm | Needs | Answers | OSCM examples |
|---|---|---|---|
| **Supervised** | labelled history | "given these features, predict this value/class" | demand forecasting (regression); supplier default/delay (classification: **SVM**, boosted trees) |
| **Unsupervised** | unlabelled data | "what structure hides here?" | SKU/customer segmentation (**k-means**), anomaly detection, store clustering |
| **Semi-supervised** | few labels + much unlabelled | | when labels are expensive |
| **Reinforcement** | environment + reward | "what POLICY maximises long-run reward?" | dynamic reordering, robot routing, dynamic pricing (**Q-learning**) |
| **Decision-focused** | decision cost as the loss | trains on what you actually pay | newsvendor quantile, not the mean |
Class Q 6.3: k-means clusters have **no ground truth** to be "accurate" against — validate by whether segments produce different, profitable treatments.

## 23. The ML Framing Canvas — five boxes before any model ⭐⭐⭐ (S6) 📘
| Box | Question |
|---|---|
| **1 Decision** | who acts, at what cadence, within what constraints? **No owner, no project.** |
| **2 Target** | the variable to predict at **decision granularity** (SKU-store-week, not national-month) |
| **3 Features** | inputs that pass the test: **knowable at decision time; no leakage** |
| **4 Benchmark** | the **naive rule** and the incumbent the model must beat — priced in decisions |
| **5 Loss** | training objective that mirrors decision costs — **asymmetric where the business is asymmetric** |
Four ways operations ML goes wrong: no decision owner; **accuracy theatre** ("92%" with no naive benchmark — Class Q 6.4: 92% vs naive 90.5% = **unproven**); **leakage** ("goods-receipt date" known only after delivery — Class Q 6.2); asymmetric costs ignored (Zillow). Class Q 6.1: whether 87% accuracy is good enough depends on **the decision's cost and reversibility**.

## 24. Seven-step operations ML workflow + capability checklist (S7) 📘
**1 Frame** (canvas) → **2 Profile** (six DQ dimensions in code) → **3 Benchmark** (fit the naive rule FIRST) → **4 Model** (simplest credible first) → **5 Evaluate** (honest holdout; error AND decisions changed; **slice by segment** — averages hide failures) → **6 Deploy** (pipeline, not laptop) → **7 Monitor** (drift alerts, retraining cadence, named owner, documented fallback).
**Capability checklist:** reproducible, monitored, owned, documented fallback, someone on call. "A model in a notebook is not a capability" (Class Q 7.1). Class Q 7.2: model wins on staples, loses on promo/new items → **deploy where it wins, keep naive elsewhere** (champion–challenger by segment). Class Q 7.3: 99% accuracy on a 3%-churn problem → accuracy is misleading; check leakage.

## 25. Probability forecasting — "the quantile IS the decision" ⭐⭐ (S8/S11) 📘
- A probability forecast gives mean, spread and tails per SKU-location-period; the point forecast is only a summary.
- **Service level = which quantile you hold**: a 95% service level = stocking the 95th percentile of lead-time demand. Safety stock becomes a **costed choice on an explicit curve**.
- **Newsvendor:** when over- and under-stocking costs differ, the optimal order is the **critical quantile = Cu ÷ (Cu + Co)**.
- Evaluate with **quantile (pinball) loss and calibration**, not MAPE alone; MAPE is **undefined on zero actuals** (intermittent spares — Class Q 10.2).
- Class Q 8.2: two SKUs forecast 1,000 (±50 vs ±400) with the same "forecast + 2 weeks" rule → **the rule ignores demand uncertainty**.

## 26. The Signal Audit — five steps before any data purchase ⭐⭐⭐ (S8/S11) 📘
| Step | Test |
|---|---|
| **1 Lead time** | does the signal arrive before the decision must be made — by enough to act? |
| **2 Mechanism** | is there an honest causal story, or a correlation mined from one training window? |
| **3 Decision test** | does the improved prediction cross an order/capacity threshold? |
| **4 Cost vs value** | acquisition + integration cost against the decisions actually changed |
| **5 Weight check** | after deployment: what weight did the model LEARN? demote or drop losers ruthlessly |
Signal verdicts (S8 table): weather (buy IF horizon matches order lead time) · promotions calendar (mandatory: signal + history repair) · POS/sell-through (bullwhip antidote) · installed base & utilisation (spare-parts winner) · social/search (test rigorously) · **customer forecasts (incentive-laden — learned weight ZERO at the Fortune 150 OEM)**.

## 27. Forecasting tiers & the Bake-Off Ladder ⭐⭐ (S9/S12) 📘
| | Tier 1 Spreadsheet | Tier 2 Open-source (Prophet, scikit-learn) | Tier 3 Cloud AutoML (SageMaker-class) | (LSTM / sequence models) |
|---|---|---|---|---|
| Volume | tens–hundreds of series | thousands (scripted) | tens of thousands + | long history, rich data |
| Skills | spreadsheet literacy | Python + statistics | cloud admin + data eng + FinOps | data maturity 3+ |
| Readiness | clean-enough extracts | pipeline discipline | governed data platform (S2 ≥ 3.5) | high |
| Explainability | total | high | variable, often opaque | low |
| Cost shape | hidden (hours, errors) | skills + maintenance | subscription + consumption | |
**Four deciding questions in order: volume, readiness, skills, governance** — accuracy joins the table but does not chair it. **Bake-off ladder: 1 Count it → 2 Audit readiness → 3 Name the skill → 4 Check governance → 5 Bake it off on your own data.** Class Q 9.1: 12-SKU bakery → spreadsheet. Class Q 9.2: AutoML +2% accuracy at 6× cost without the skills → **Prophet tier wins today** (name the condition that flips it). Class Q 9.3: production readiness = **does it run reliably on schedule** (40,000 SKUs by 6 a.m.).

## 28. The inventory policy ladder (S10) 📘
| Generation | Logic | Strength | Where it strains |
|---|---|---|---|
| **EOQ (1913)** | batch size from order-vs-holding trade-off | transparent; right for stable demand | assumes steady demand, static costs |
| **Basestock / (s,S) + service levels** | order up to a target set by the lead-time demand distribution | decades of theory; auditable; near-optimal when tuned | complex networks, dual sourcing, lost sales |
| **Stochastic optimisation / EIO** | multi-echelon under uncertainty (700+ deployments in Global 2000) | network-aware; proven | static parameters; slow to absorb signals |
| **DRL policies** | neural policy learned in a simulator: state → action for reward | handles complexity; ms inference | data/tuning hungry; brittle off-regime; opaque |
| **One-step (data-to-decision)** | learn the decision function from features, constraints, KPIs | skips forecast errors; interpretable weights; Fortune 150 scale | needs the digital twin + data layer |
"**Optimize the policy, not the forecast**" (Class Q 10.3: replacing the weeks-of-supply rule beats a 15% forecast gain).

## 29. The Guardrailed Pilot — six design elements ⭐⭐⭐ (S10) 📘
| # | Element | Content |
|---|---|---|
| 1 | **Scope** | one category, honest volume, long enough for intermittent statistics (quarters, not weeks) |
| 2 | **Bounds** | basestock floors/ceilings from the trusted incumbent; spend envelopes; no unbounded orders |
| 3 | **Fallback** | drift and anomaly triggers that **auto-revert to the incumbent policy** — tested before go-live |
| 4 | **Evaluation** | **randomised or matched-control vs incumbent AND naive benchmark**; decision-frontier metrics (service per rupee) |
| 5 | **Trust loop** | interpretable recommendations; bounded planner override with reason capture feeding retraining |
| 6 | **Ownership** | named expert owner for the policy; named business owner for outcomes; review cadence with widen/narrow/revert decision |
"This design IS the honest answer to every '20% better' pitch: fund the pilot, on these terms." Theory ceiling: a simple **myopic policy sits within ~5% of optimal**, so a 20% backtest win over a tuned basestock policy most likely contains **overfitting or a weak baseline** (Class Q 10.1); freshly trained DRL often runs **15–20% behind** the myopic policy. Class Q 10.4: "4 weeks shadow, then full control" is missing **bounds, fallback and a real evaluation**.

## 30. The Twin-Now / Twin-Later Test (S13) 📘
**1 Decision-changing** (would a better prediction change what you'd do, or when? If no, stop) → **2 Failure cost** (downtime, safety, warranty high enough?) → **3 Data readiness** (sensor stream exists, or instrumentation from zero?) → **4 Fidelity needed** (can a lightweight simulation of the relevant subsystem answer the what-if?) → **5 Verdict: twin-now (build), twin-later (park), or simulation-lite substitute.** Target **Remaining Useful Life (RUL)**, not a binary alarm. "Fidelity-for-purpose, not maximum realism."

## 31. The Mandate Card — set before you hand flow to any agent ⭐⭐⭐ (S14) 📘
| # | Field | Decide |
|---|---|---|
| 1 | **Service floor** | the zones/segments where a stockout is unacceptable and must be protected first |
| 2 | **Cost ceiling** | maximum acceptable cost-per-unit-delivered, by mode |
| 3 | **Mode priority** | default cost-vs-speed preference (the agent's tiebreaker) |
| 4 | **Shock trigger** | what capacity or demand shift forces a full re-plan vs a local patch |
| 5 | **Review cadence** | how often a human re-checks the agent's allocation against outcomes |
"Agents operate the model, they don't replace it — the mandate is yours, execution at scale is the agent's."

## 32. The Optimizer Mandate Checklist (S15) 📘
**1 Service targets** (per zone, not one network-wide number) → **2 Cost weights** (reflect strategic priority, not just unit economics) → **3 Review rule** (human sign-off L2, exception-based escalation L3, or fully autonomous L4) → **4 Re-solve trigger** (cost shock, capacity loss, demand spike) → **5 Verify the fit** (check the returned plan against the service floor before it executes — "optimal is not automatically right").
Min-cost-flow: plants, RDCs, zones = nodes; lanes = edges with capacity and cost; the solver finds the lowest-cost flow meeting demand under constraints. **AI-OR symbiosis:** agents decide **when** to invoke the solver, **what** to optimise for and **how much autonomy** its plan gets — JD.com's "dual engine".

## 33. The Clause-Stakes Specification Checklist (S16) 📘
**1 List the clauses** (payment terms, renewal windows, liability caps, penalty triggers, termination, indemnification) → **2 Name the decision** each feeds → **3 Set the bar** per clause by the cost of being wrong → **4 Pick the tier** (general extraction fine for logistics/contact fields; **domain-tuned for anything touching liability** — 94.7% vs 79.3%) → **5 Name the exception** — the one clause type you will never fully automate the interpretation of (penalty/indemnification).

## 34. The Tune-or-Retire Checklist (S17) 📘
**1 Measure cost** = total run-cost (tokens, calls, compute) ÷ decisions made → **2 Measure value** = money/margin impact of those decisions over the same window → **3 Compare the ratio** (value per decision comfortably > cost per decision → no action) → **4 Tune first** (cut context, cache, batch calls, downgrade model tier; re-measure) → **5 Retire if it still fails** (fall back to the next-best option rather than run at a loss on principle). Spend caps belong **in code**, not in prompts.

## 35. The Scenario Portfolio Checklist (S18) 📘
**1 Generate wide** (GenAI for structurally diverse scenarios) → **2 Label honestly** (plausible / stretch / implausible by mechanism and precedent, not detail) → **3 Select your two** (one plausible, one high-impact stretch) → **4 Specify survival** (the capability each requires — flex capacity, dual sourcing, buffer — and its cost) → **5 Guard the label** (name the mechanism connecting the scenario to your business; if you can't, it's a story). "The generator proposes; the optimizer disposes." Design goal: **antifragility** — gain from disruption.

## 36. Restoring multi-agent stability (S19) 📘
1. **Shared demand signals** — every agent sees real end-customer demand, not a neighbour's order (removes most of the amplification loop).
2. **Rate limits and order smoothing** — cap or dampen how much an order can move per period.
3. **Trained coordination** — agents trained jointly on one shared objective; **consensus-seeking** orchestration makes agents reconcile before acting.
Evidence: decentralised LLM agents **amplify bullwhip** in beer-game experiments (the "collaboration paradox"); jointly trained agents beat both a central agent and uncoordinated agents **on cost AND variability** (POM 2025). "**Stability is mechanism design, not intelligence.**"

## 37. ACAP governance — the self-check (S19) and final checklist (S20) ⭐⭐⭐ 📘
| S19 self-check for an agent design | S20 checklist "one last time" |
|---|---|
| **Accountability** — who owns a decision the agent makes; traceable to a person? | **Accountability** — a named human owner, not just a team |
| **Capability boundaries** — what the agent is and is not authorised to decide alone | **Capability limits** — scope and autonomy level explicitly bounded to its ladder rung |
| **Alignment** — does it optimise the same objective as the humans/agents around it? | **Auditability** — a log detailed enough to reconstruct what it did and why |
| **Process oversight** — a checkpoint **before** high-impact actions execute | **Proportionality** — oversight scales with real-world stakes |
| **Coordination mechanism** — what stops agents amplifying each other's noise | **Post-incident learning** — does an incident change the next deployment? |
(The WEF "AI Agents in Action" playbook (2026) introduced **ACAP — a per-agent capability & authorization profile** covering delegation policy, system design and oversight 📘.)
