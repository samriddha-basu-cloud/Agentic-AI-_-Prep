# Glossary — Agentic AI in Ops & SCM, A–Z
One- or two-line, exam-ready definitions of the terms used across the 20 sessions, the Chain Reaction simulation and basic SCM. 📘 = the term comes from your sessions or syllabus; 📗 = a standard SCM/AI definition added for completeness. The **Flashcards** and **Quiz** views are built from this page.

## A
- **ACAP governance checklist** 📘: Five-check self-test for any agent. S19: Accountability, Capability boundaries, Alignment, Process oversight (+ coordination mechanism). S20: Accountability, Capability limits, Auditability, Proportionality, Post-incident learning.
- **Adaptive forecasting loop** 📘: Continuous re-estimation as new data arrives (weights update, the plan refreshes) at a deliberate cadence that balances responsiveness against plan nervousness.
- **Agent-washing** 📘: Marketing a recommender, copilot or script as an "agent". The test is goal ownership plus tool-mediated action within an envelope.
- **Agentic AI** 📘: AI that perceives, reasons and ACTS on systems of record toward a goal, using tools within a bounded envelope (e.g. posts delivery dates into the ERP or closes a negotiation).
- **Agentic suitability screen** 📘: A five-factor score (frequency, reversibility, data/feedback, rule clarity, stakes). 20+ = strong candidate; 12–19 = bounded pilot; < 12 = human-led.
- **AI–OR symbiosis** 📘: Agents operate optimisation solvers (deciding when to re-solve and what to optimise) rather than replacing them. JD.com's dual engine is the paradigm.
- **Algorithm aversion** 📘: People abandon algorithms faster than humans after the same errors. Slight modifiability (e.g. ±15% overrides) restores use and trust.
- **Antifragility** 📘: A design goal of gaining from disruption, not just surviving it (e.g. flex capacity that captures a rival's stranded demand).
- **Auditability** 📘: Logs detailed enough to reconstruct what an agent did and why, after the fact.
- **Autonomy ladder (L1–L5)** 📘: L1 inform → L2 recommend (human approves) → L3 act within bounds and escalate exceptions → L4 autonomous with monitoring → L5 fully autonomous. Autonomy is granted per decision.
- **AWS SageMaker** 📘: Amazon's cloud ML build/train/deploy service (with the no-code Canvas variant), the Tier-3 forecasting option. Amazon trained DeepFleet on it.
- **Azure AI** 📘: Microsoft's AI platform (Azure OpenAI, AI Foundry, Copilot Studio). It fits Microsoft-centric estates by data gravity and skills.

## B
- **Bake-off ladder** 📘: Count it, audit readiness, name the skill, check governance, bake it off on your own data, all before buying a forecasting tier.
- **Basestock policy** 📗: Order up to a target level set by the demand distribution over the lead time. Auditable and near-optimal when tuned.
- **Below-gate build** 📘: A Chain Reaction agent built under its D·P·T foundation gate. It runs at full cost for a fraction of the effect, with cut build odds (e.g. 12%, 20%).
- **Blue/green deployment** 📘: Run two environments and switch traffic to the new one after QA, with no downtime.
- **Building is not operating** 📘: Season lesson 2. Estate size never predicted rank; operating it (booking rail, filing distribution plans, right-sizing the chip book) did.
- **Bullwhip effect** 📗: Order variability amplifying upstream. Caused by demand-signal processing, batching, price swings and shortage gaming. Measured as Var(orders)/Var(demand).
- **Bus factor** 📘: The number of people whose absence kills a capability. A notebook only one analyst can run has a bus factor of 1.

## C
- **Calibration** 📘: Whether stated probabilities match reality (e.g. 90% of actuals fall inside the 90% band). Used to score distribution forecasts.
- **Capability checklist** 📘: Reproducible, monitored, owned, documented fallback, versioned data and model, permissions and logging. It separates a capability from a demo.
- **Chain Reaction** 📘: The course's ten-round supply-chain simulation (3 plants, 4 RDCs, 7 zones; HATCH/SUV/EV), scored as value = profit × reputation × trust.
- **Champion–challenger by segment** 📘: Deploy each method where it demonstrably wins (model on staples, naive on promotions) and revisit as data accrues.
- **Claim audit (Four-Question)** 📘: Test every AI claim: what baseline, measured how, which stock/cost pool, and what decision changes? (S1)
- **Clause-stakes checklist** 📘: List the clauses, name the decision each feeds, set the bar by error cost, pick the tier (general vs domain-tuned), name the never-automate exception.
- **Collaboration paradox** 📘: Smarter individual agents with no coordination make system oscillation (bullwhip) worse, because they overreact to each other faster.
- **Command Your Agent** 📘: The July class game (Session 10) where 20 teams' agents produced a live bullwhip blow-up.
- **Company value (Chain Reaction)** 📘: Profit × reputation × trust. Governance is the multiplier you feel late.
- **Compounders** 📘: The winning archetype. They built capability on foundations actually laid and kept operating (B12-Titans #1, A7-Kimi K3 #2).
- **Confusion matrix** 📘: TP/FP/FN/TN counts behind every accuracy claim. Precision, recall and F1 derive from it.
- **Critical ratio (newsvendor)** 📗: Cu/(Cu + Co). The optimal stocking quantile when under- and over-stocking costs differ.
- **Cycle stock (Q/2)** 📘: Inventory created by order batch size. Forecasting does not reduce it; order frequency and MOQ changes do.

## D
- **D·P·T foundations** 📘: Data, Process and Tech maturity ladders (L1–L5) in Chain Reaction. Each agent has a gate (e.g. D3·P3·T3).
- **Data leakage** 📘: Using a feature unknown at decision time (e.g. goods-receipt date). It flatters backtests and collapses in production.
- **Data quality: six dimensions** 📘: Accuracy, completeness, consistency, timeliness, uniqueness, validity. They are judged per use case.
- **Decision-focused learning** 📘: Training models with the decision's cost as the loss, rather than symmetric prediction error.
- **Decision levels** 📘: Strategic (AI as input only), tactical (augment), operational (delegate where frequent and reversible).
- **DeepFleet** 📘: Amazon's 2025 generative foundation model coordinating 1M+ warehouse robots; robot travel time −10%.
- **Demand sensing** 📘: Short-horizon forecasting from leading signals (POS, weather, promotions, IoT installed base) rather than history alone.
- **Deployer (EU AI Act)** 📘: The organisation using an AI system. It owns human oversight, use per instructions, monitoring and logs.
- **Digital twin** 📘: A live virtual replica, fed by real data, on which you test interventions before committing. Build it to fidelity-for-purpose.
- **distCover / distSafety / distFront / distMode** 📘: Chain Reaction's four distribution dials: coverage, safety stock, SPREAD/FRONT loading, ROAD/MIX mode (MIX locked until tech maturity 3).
- **DRL (deep reinforcement learning)** 📘: A neural policy learned by acting in a simulator (state → action → reward). Powerful but brittle off-regime.

## E
- **Efficiency-capture gap** 📘: Agentic procurement gave 20–30% staff efficiency but only 1–3% bottom-line capture (McKinsey). Efficiency is not margin.
- **EOQ** 📗: Economic order quantity √(2DS/H), which balances ordering and holding cost (1913). Still right for stable demand.
- **EU AI Act** 📘: EU regulation with high-risk obligations (conformity assessment, CE marking, registration) split across providers, importers, distributors and deployers. Now enforceable.

## F
- **F1 score** 📘: The harmonic mean of precision and recall. A single comparison number and the baseline for improvement.
- **Fidelity-for-purpose** 📘: Build a twin only detailed enough to answer the one question asked.
- **Fill rate** 📗: Units (or lines) delivered on time ÷ demanded. Weight by volume, never a simple average of locations.
- **Foundations without operations** 📘: The losing archetype that laid deep ground and never ran on it (A4-Sapiens #20).
- **Frozen baseline** 📘: A pre-pilot performance snapshot plus a control group, against which gate metrics are judged.

## G
- **Gate (roadmap)** 📘: An evidence checkpoint (success metric + counter-metric + owner + demotion trigger) between Crawl, Walk and Run phases.
- **Generative AI** 📘: Models that create content (text, scenarios, designs). In SCM: RFx drafting, scenario engines, product concepts.
- **Google OR-Tools** 📘: Google's open-source optimisation suite (LP/MIP, CP-SAT, vehicle routing, min-cost flow).
- **Governance stack** 📘: Per-agent identity, scoped permissions, spend caps in code, action logs, escalation paths and kill switches. Guardrails live outside the model.
- **Guardrailed pilot** 📘: Six design elements for any learned policy: scope, bounds, fallback, evaluation, trust loop, ownership.
- **Guardrails live outside the model** 📘: Enforceable limits sit in the surrounding system, not in prompts or weights.

## H
- **Hugging Face** 📘: A hub of open transformer models that can be fine-tuned in-house (e.g. legal-domain models for clause risk).

## I
- **Installed-base signal** 📘: Machines in the field, their utilisation and maintenance schedules as leading indicators of spare-parts demand. It produced the 77 → 85% fill.
- **Intermittent demand** 📘: Mostly zero sales with occasional lumps (spare parts). It breaks point forecasts and MAPE.
- **Ironies of automation** 📘: The more reliable automation is, the worse humans get at monitoring it. Oversight is not a safety net.

## J
- **JD.com dual engine** 📘: An AI sensing layer on top of a classical solver for national routing and inventory placement. The AI decides when and what to re-solve.

## K
- **k-Means** 📘: Unsupervised clustering into k groups around centroids (SKU or customer segmentation). Validated by usefulness, not "accuracy".
- **Kiva robots** 📘: Amazon's goods-to-person mobile robots (Kiva acquired in 2012), which carry shelving pods to pickers. Physical automation, the precursor of DeepFleet.

## L
- **Lean operators** 📘: An archetype with minimal transformation, deep foundations and excellent execution (A8-The Odyssey #3 on six agents).
- **LSTM** 📘: A recurrent neural network with memory gates for long sequences. The Tier-4 forecaster; needs Data Maturity 3+ and long history.

## M
- **Mandate Card** 📘: Service floor, cost ceiling, mode priority, shock trigger, review cadence, set before handing flow to an agent.
- **MAPE** 📗: Mean absolute percentage error. Undefined on zero actuals, so unsuitable for intermittent demand.
- **Master data** 📘: Slow-changing reference data (item, vendor, customer, location, BOM). "Where AI projects go to die."
- **MEIO** 📗: Multi-echelon inventory optimisation under uncertainty (700+ Global 2000 deployments).
- **Min-cost flow** 📘: An LP that finds the cheapest flow over a network of nodes and capacitated lanes meeting demand. It optimises exactly the objective it is given.
- **MIX mode** 📘: Rail in the distribution mix in Chain Reaction (~25% cheaper than road), unlocked at tech maturity 3.
- **Multi-agent coordination fixes** 📘: Shared demand signal, rate limits and order smoothing, trained or consensus coordination.
- **M5 competition** 📘: The Walmart-data forecasting contest (42,840 series). ML won overall, but simple methods stayed competitive at SKU-store level.

## N
- **Naive benchmark** 📘: A simple rule (same as last week, seasonal naive) every model must beat on the same holdout.
- **Newsvendor model** 📗: A single-period stocking model. Order the critical-ratio quantile of demand.
- **Non-stationarity** 📘: Shifting demand regimes (promotions, 2020) that silently degrade history-trained models.

## O
- **One-step planning** 📘: Learning the decision function directly from features, constraints and KPIs, skipping the standalone forecast (Fortune 150: fill 77 → 85%).
- **OpenAI API** 📘: A metered general-purpose LLM API, used for auto-RFx drafting and summarisation and billed per token.
- **OptaPlanner** 📘: An open-source Java constraint-satisfaction planning engine (metaheuristics with hard and soft scores) for rostering, routing and scheduling.
- **Optimizer Mandate Checklist** 📘: Service targets per zone, cost weights by strategic priority, review rule (L2/L3/L4), re-solve trigger, verify the fit.

## P
- **Pactum** 📘: The autonomous negotiation platform behind Walmart's tail-spend agent: ~3% savings, +35-day terms, 64–68% close rate, inside manager-set bounds.
- **Pilot-selection matrix** 📘: Ranks pilots on value, feasibility and blast radius (reversibility). Used in Trishul B1.
- **Pinball (quantile) loss** 📘: The error metric for quantile forecasts. It penalises under- and over-forecasts asymmetrically at the chosen quantile.
- **Platform filters (six, in order)** 📘: Use-case fit, data gravity, skills/ecosystem, governance fit, TCO including consumption, exit/lock-in. Governance comes before features.
- **Precision** 📘: TP/(TP + FP). When the model flags, how often is it right?
- **Predictive maintenance** 📘: Using sensor data to predict failure or remaining useful life and schedule repair before breakdown.
- **Prescriptive maintenance** 📘: Predictive maintenance plus the recommended action (when, which part, which crew, where to stock it).
- **Probability forecast** 📘: A full demand distribution (mean, spread, tails) rather than a point. "The quantile IS the decision."
- **Prophet** 📘: Meta's open-source forecasting library (trend, seasonality, holidays by default). The Tier-2 forecaster.
- **Provider (EU AI Act)** 📘: The developer of an AI system. It owns conformity assessment, CE marking, registration and technical documentation.

## Q
- **Q vs S** 📘: Cycle stock (Q/2) vs safety stock (S). Forecasting attacks S only; check the S share before believing an inventory claim.
- **Q-learning** 📘: RL that learns Q(state, action) values from reward: Q ← Q + α[r + γ·max Q′ − Q]. Used for reordering and routing.

## R
- **RapidMiner** 📘: A visual, low-code data-science platform (drag-and-drop workflows) named in the syllabus ML tools.
- **Recall** 📘: TP/(TP + FN). Of the real events, how many did the model catch?
- **Regime change** 📘: A structural break (e.g. 2020 lockdowns) under which history-trained models fail. It requires monitoring and human override.
- **Reinforcement learning** 📘: Learning a policy by trial and reward rather than labels.
- **Re-solve trigger** 📘: A named event (capacity loss, cost shock, demand spike) that forces the optimiser to re-plan.
- **Readiness scorecard (five pillars)** 📘: Data quality, master data, architecture/integration, security, compute, scored 1–5. It sets the ambition ceiling.
- **RFx automation** 📘: NLP reading bids and requisitions, auto-filling comparison matrices and drafting RFQs/RFPs.
- **RUL (remaining useful life)** 📘: The hours or days a machine has left. A better target than a binary failure alarm.

## S
- **Safety stock** 📗: z × σ × √L. A buffer against demand and lead-time uncertainty; the only stock forecasting reduces.
- **Scenario Portfolio Checklist** 📘: Generate wide, label honestly (plausible/stretch/implausible), select two, specify survival, guard the label.
- **Sequence beats speed** 📘: Season lesson 1. Build agents on foundations you have laid; below-gate builds waste tokens.
- **Shared demand signal** 📘: Every tier and agent sees real end-customer demand. The single biggest bullwhip fix.
- **Signal audit** 📘: Lead time, mechanism, decision test, cost vs value, weight check, before buying any data.
- **Spend classification** 📘: NLP tagging every transaction into a category taxonomy instead of guessing from GL codes.
- **Split shipment** 📘: Under a capacity shock, send the urgent part by fast mode and backfill the rest by the cheap mode.
- **SVM** 📘: Support vector machine. A classifier that finds the widest-margin boundary between classes (e.g. late vs on-time supplier orders).

## T
- **Tier matching** 📘: Spreadsheet → open-source (Prophet) → cloud AutoML (SageMaker) → LSTM, chosen by volume, readiness, skills and governance.
- **Token economics** 📘: Consumption billing per call or token. The agent bill is a live operating cost; the cost model is a snapshot.
- **Tokens (Chain Reaction)** 📘: 24 decision tokens per month; plan = 2, regenerate = 1; upkeep 1–4 per agent; termination = 2; max 4 transformation actions per round.
- **Trailer-express** 📘: The fast, expensive, capacity-limited mode for urgent top-ups.
- **Transformation theatre** 📘: An archetype that built the most agents on the least foundation ("activity mistaken for outcome"), finishing 8th–18th.
- **Trust design** 📘: Showing the track record, allowing bounded overrides with reason capture and explaining recommendations, so adoption is designed rather than demanded.
- **Tune-or-retire** 📘: Measure cost per decision and value per decision, compare them, tune first (context, cache, batch, tier), and retire only if it still fails.
- **Twin-now / Twin-later test** 📘: Decision-changing? Failure cost? Data readiness? Fidelity needed? Then a verdict.

## U
- **Update vs execute** 📘: The clarifying question for any "autonomous forecasting" claim. Executing orders is an autonomy grant.

## V
- **VAE + multi-objective optimiser** 📘: A 2025 design architecture. A variational autoencoder generates demand scenarios; an optimiser searches the cost-vs-CO₂ frontier across them.
- **Value-per-decision** 📘: The ₹ impact of an agent's decisions ÷ the number of decisions. Compared with cost-per-decision in tune-or-retire.
- **VRP** 📗: Vehicle routing problem. Serve customers with capacity-limited vehicles at minimum cost within time windows (NP-hard; OR-Tools, OptaPlanner).

## W
- **Walmart Trend-to-Product** 📘: A GenAI product-design loop that cut up to about 18 weeks from design-to-shelf.

## Z
- **Zero-weight finding** 📘: A Fortune 150 OEM's planning system gave retail partners' own forecasts zero weight. Signals earn their weights.
- **Zillow Offers** 📘: A 2021 failure in which ML price forecasts auto-bought houses (>$500M write-down). The decision defines the model.
