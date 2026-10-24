# Ch 0 — SCM Fundamentals (the basics the exam assumes)
Your faculty's note: **"Basic Concepts of SCM will also be required."** 📘 The cases sit on top of ordinary supply chain logic — cycle vs safety stock, service level, bullwhip, mode choice, network flows, procurement. This chapter is the refresher, written so that every concept is tied to where it appears in the AI course and the past papers. Concepts not in the decks are marked 📗 (standard SCM texts: Chopra & Meindl, Simchi-Levi, Fisher, Stadtler & Kilger).

---

## 1. What a supply chain is
- **Supply chain** 📗: all parties involved, directly or indirectly, in fulfilling a customer request — suppliers, manufacturers, distributors (RDCs), retailers/dealers, customers — linked by **three flows**: **product** (downstream), **information** (both ways) and **funds** (upstream).
- **Supply chain management** 📗: managing those flows to maximise total supply-chain surplus (customer value − total supply chain cost).
- **The core problem never changed** 📘: "matching supply and demand under uncertainty remains the discipline's core" (OM community vision, S1) — AI reshapes the *practice*, not the problem.
- **Chain Reaction's chain** 📘: chip suppliers → 3 plants → 4 RDCs → 7 dealer zones → customers, with rail/road/trailer-express links.

## 2. Decision levels (and where AI fits) ⭐⭐
| Level | Horizon | Examples | AI posture (S3 📘) |
|---|---|---|---|
| **Strategic (design)** | years | network design, sourcing strategy, make/buy, capacity, MTS/MTO/ATO, postponement | input only |
| **Tactical (planning)** | months–quarters | S&OP/SIOP, aggregate production plan, inventory policy, transport contracts | augment planners |
| **Operational** | days–hours | order promising (ATP), scheduling, replenishment, routing, dispatch | delegate (within envelopes) |
**The supply chain planning matrix** (Stadtler & Kilger, the course e-book 📘): long-term strategic network planning; mid-term master planning; short-term demand planning, production planning & scheduling, distribution & transport planning, purchasing & materials requirement planning, demand fulfilment & ATP. APS (Advanced Planning Systems, late 1990s) layered LP/MILP optimisation and hierarchical planning on ERP; AI adds always-on re-planning, ML with external signals, RL scheduling and dynamic re-routing (S1 table 📘).

## 3. Strategic fit — Fisher (1997) and the Triple-A chain ⭐⭐
| | **Functional products** (stable, predictable, low margin — e.g. HATCH, toothpaste) | **Innovative products** (volatile, short life, high margin — e.g. fashion, new EVs) |
|---|---|---|
| Right chain | **Efficient** (cost-focused: full trucks, high utilisation, low inventory) | **Responsive** (speed and flexibility: buffer capacity, postponement, sensing) |
- **Lee's Triple-A (2004)** 📗: **Agility** (respond to short-term changes), **Adaptability** (adjust design to structural shifts), **Alignment** (align incentives across partners). The course mentions the "agility-adaptability-alignment triad" and a 2026 "digital super-agility" recalibration 📘.
- *Course link:* Zara's ML trend detection serves a **responsive** chain design — "the tool matched the chain" (S6 📘). A tool that does not match the chain's strategy is wasted.

## 4. Drivers of supply chain performance 📗
**Facilities** (plants, RDCs — location, capacity), **inventory** (cycle, safety, seasonal, pipeline), **transportation** (mode, route, network), **information** (visibility, forecasts, coordination), **sourcing** (in-house vs outsourced, supplier selection), **pricing** (price and promotion levers). Each trades **responsiveness vs efficiency**.

## 5. Inventory — types and why they exist ⭐⭐⭐
| Type | Why it exists | Driven by | What reduces it |
|---|---|---|---|
| **Cycle stock (Q/2)** | ordering/producing in batches (economies of scale) | batch size Q: trucks, pallets, MOQs, set-ups | smaller, more frequent orders; lower set-up/order cost; shorter lead times |
| **Safety stock (S)** | buffer against demand and supply uncertainty | σ of demand over lead time, service level, lead-time variability | **better forecasts**, shorter/less variable lead times, pooling |
| **Pipeline / in-transit** | goods moving between nodes | lead time × flow rate | faster modes, shorter distances |
| **Seasonal / anticipation** | build ahead of peaks | capacity vs seasonal demand | flexible capacity |
| **Decoupling / WIP** | buffers between stages | process variability | flow, lean |
**The course's key point (S1 📘):** inventory follows a **saw-tooth** — cycle stock from batch Q plus safety stock S. **A perfect forecast eliminates only S**; most inventory sits in Q, driven by physical constraints. → Forecasting AI attacks S, not Q (Trishul A1; Class Q 1.2). **Campbell Soup:** sharing POS data to improve forecasts gave marginal benefit; **cutting order-processing lead time and ordering more often (Q↓) was the big win**.

## 6. Inventory policies ⭐⭐
- **EOQ** (Harris, 1913): Q* = √(2DS/H) balances ordering and holding cost; right for stable demand (S10 📘).
- **Continuous review (s, Q)**: when inventory position hits the reorder point s (= d × L + SS), order Q.
- **Periodic review / basestock (order-up-to S)**: every period, order up to a target set by the demand distribution over (review + lead time). "Decades of theory; auditable; near-optimal when tuned" (S10 📘).
- **(s, S)**: review; if below s, order up to S.
- **Multi-echelon inventory optimisation (MEIO/EIO)**: sets buffers jointly across echelons; 700+ Global 2000 deployments (S10 📘).
- **Service level**: **cycle service level** (probability of no stockout in a cycle) vs **fill rate** (share of demand met from stock). "Service level = which quantile you hold" (S8 📘).
- **Weeks-of-supply rules** convert forecasts crudely into stock — "the damage happens AFTER the forecast" (S8 📘): inflated forecast → excess; conservative → shortages; identical means with different variances get identical stock.
- **Intermittent demand** (spares: 0,0,0,4,0,0,2,0): point forecasts near-meaningless; use distributions, pooled signals (installed base); MAPE undefined on zeros (S10 📘).

## 7. Forecasting basics ⭐⭐
- **Components**: level, trend, seasonality, noise; causal drivers (price, promotions, weather, installed base).
- **Methods**: naive ("same as last week/year"), moving average, exponential smoothing (Holt-Winters), regression with features, ML (gradient boosting won the M5), Prophet (trend + seasonality + holidays by default), LSTM/transformers (long histories, high maturity).
- **Error metrics**: MAD, MAPE (fails at zero), RMSE, **bias** (systematic over/under), **forecast value added (FVA)** vs naive; **quantile/pinball loss and calibration** for probability forecasts.
- **Principles**: forecasts are always wrong; aggregate forecasts are more accurate than disaggregate; shorter horizons are more accurate; **forecast the distribution, not the number** (S8 📘); **no model without a naive benchmark** (S6 📘).
- **Organisational reality** (S8 📘): many competing forecasts (sales in ₹ monthly, planning in units weekly, each partner separately), each a negotiating position — sales inflates, planning deflates. A deployed system gave the **customers' own forecasts zero weight**.

## 8. The bullwhip effect ⭐⭐⭐
- **Definition** 📗: order variability **amplifies** as you move upstream (retailer → distributor → manufacturer → supplier), even when consumer demand is stable (Lee, Padmanabhan & Whang 1997; Forrester 1961).
- **Causes**: demand-signal processing (each tier forecasts from the orders it sees), **order batching**, **price fluctuations / promotions** (forward buying), **rationing and shortage gaming** (over-ordering under allocation), long lead times.
- **Classic remedies**: share POS/end-customer demand (information sharing, VMI, CPFR), shorten lead times, smaller more frequent orders, everyday low pricing, allocate on past sales not orders.
- **Course twist ⭐⭐⭐ (S4, S19 📘):** **LLM agents can amplify bullwhip** — in beer-game experiments most decentralised LLM agents created MORE instability than simple baselines ("collaboration paradox"); your own class reproduced it in July's Command Your Agent finale. Fixes: **shared demand signal, order smoothing/rate limits, trained coordination** — "stability is mechanism design, not intelligence". **Inverse bullwhip** (S3 📘): better forecasts at the customer can *increase* variability at the manufacturer under quantity discounts.

## 9. Distribution and network design ⭐⭐
- **Network structures** 📗: direct shipping, via DCs/RDCs, cross-docking, milk runs, hub-and-spoke; **push vs pull** (make-to-stock pushes to RDCs on forecast; pull ships on orders). Chain Reaction's **default auto-push** is a pure push with no plan — the reason stock ended up in the wrong RDCs.
- **Risk pooling** 📗: centralising stock reduces safety stock by ~√n for independent demand, at the cost of longer delivery distance.
- **Postponement** 📗: delay differentiation (paint colour, packaging, final assembly) until demand is known.
- **Network flow optimisation** 📘 (S15): plants, RDCs, zones as nodes; lanes as edges with capacity and cost; a **min-cost-flow LP** finds the cheapest flow meeting demand — but only for the objective (service targets, cost weights) you set.
- **Asian Paints** 📘 (S1): demand data drove direct-to-dealer distribution that removed a distributor tier → turns ~3–4× peers — information transformative because it enabled a **structural** change.

## 10. Transportation ⭐⭐
| Mode | Cost | Speed | Flexibility | Chain Reaction |
|---|---|---|---|---|
| **Rail** | lowest per unit (≈25% below road) | slow | slot-constrained, book ahead | booked a month ahead, charged used or not |
| **Road (FTL/LTL)** | medium | medium | high — door to door | default lane; flexible workhorse |
| **Express / air / trailer-express** | highest | fastest | capacity-limited | urgent top-ups |
| **Sea / container** | very low | very slow | port-dependent | (port jam event) |
- **Economies of scale**: full-truck loads cut cost per unit → large Q (why FTL multiples dominate cycle stock).
- **Mode choice = cost vs speed vs reliability**, made per lane; AI re-evaluates the trade-off "every lane, every hour, not weekly" (S14 📘). Under a shock, **split** across modes.
- **Line-haul dominates routing cost** — better demand forecasts barely shorten the out-and-back distance (S1 📘).
- **Vehicle routing (VRP)** 📗: Google **OR-Tools**, **OptaPlanner** (constraint solver), **Q-learning**-based dynamic routing (syllabus tools 📘).

## 11. Sourcing and procurement ⭐⭐
- **Procure-to-pay (P2P)** 📗: need → requisition → RFx (RFI/RFQ/RFP) → evaluation → negotiation → contract → PO → receipt → invoice → payment.
- **Spend categories**: **direct** (materials in the product — Trishul ₹410 cr, 78 suppliers) vs **indirect/MRO** (maintenance, repair, operations; **tail spend** = the long tail of many small suppliers — Trishul ₹64 cr, 2,410 suppliers, median ₹1.9 L).
- **Kraljic matrix** 📗: profit impact × supply risk → **strategic** (partner), **leverage** (compete/negotiate hard), **bottleneck** (secure supply), **non-critical/routine** (simplify, automate) — *tail spend is mostly non-critical → automate (Pactum); strategic suppliers stay human (S4 Class Q 4.5).*
- **TCO / landed cost** 📗: price + freight + duties + quality cost + inventory carrying + risk.
- **Supplier risk** 📗: concentration (top-10 share), single vs dual sourcing, financial stress, geopolitics, lead-time reliability — feeds supplier-risk scoring (Trishul P3).
- **Contracts**: payment terms (days payable), volume commitments, **penalty/indemnification clauses** (strictest accuracy bar — S16 📘), renewal windows. **Take-or-pay / capacity reservation** (Chain Reaction chip book: fees on the full book used or not).

## 12. S&OP / IBP 📗
Monthly cross-functional cycle: **data gathering → demand review (consensus forecast) → supply review (capacity) → pre-S&OP reconciliation → executive S&OP** — one plan for sales, operations and finance. AI role: scenario generation in minutes, always-on re-planning (S1 table 📘); still **tactical → augment** (S3 📘).

## 13. Performance metrics ⭐⭐
| Area | KPI |
|---|---|
| Service | **fill rate**, cycle service level, **OTIF**, order cycle time, lost sales, backorders |
| Inventory | **turns**, days of supply (DOS/DIO), inventory value, obsolescence |
| Cost | cost to serve, freight cost per unit, carrying cost (rate × value), landed cost |
| Cash | **cash-to-cash cycle** = DIO + DSO − DPO; working capital |
| Forecast | MAPE/WMAPE, bias, forecast value added |
| Procurement | savings %, spend under management, negotiated share, payment terms |
| Assets | OEE (availability × performance × quality), utilisation, uptime |
| Balanced view | **Balanced Scorecard** (financial, customer, internal process, learning & growth — S3 📘) |
**Guarded metrics** (course rule): every success metric needs a counter-metric — inventory cut must not buy stockouts; savings must not buy worse supplier OTIF; fill must not be bought with expedites.

## 14. Supply chain risk and resilience 📗
- **Risk types**: demand (EV surge, credit slump), supply (chip allocation), logistics (port jam, corridor congestion, carrier failure), environmental (monsoon), cyber (NotPetya cost Maersk ~$300M in 2017 📘), regulatory.
- **Resilience levers**: buffers (inventory, capacity), redundancy (dual sourcing, multiple modes), flexibility (postponement, flexible plants), visibility (control towers — Unilever ~20, P&G ~110 plants 📘), insurance/hedges (hazard cover, diesel hedge), scenario planning (GenAI scenario engines — S18 📘), **digital twins** ("primary enabler of resilience", ASCM 2026 📘).
- **Antifragility** 📘: design that gets stronger because the shock happened.

## 15. IT systems in the supply chain ⭐
**ERP** (one database of record: materials, orders, money — MRP 1960s–70s → MRP II → ERP 1990s) · **APS** (optimisation over ERP) · **WMS** (warehouse) · **TMS** (transport) · **MES** (shop floor) · **EDI / APIs / RFID / barcodes** (data capture) · **control towers** (end-to-end visibility) · **data warehouse → lake → lakehouse + streaming → semantic layer → agent-ready data products** (S2 📘). **The spreadsheet ring**: 61% of Trishul's planning decisions run in spreadsheets beside an 11-year-old ERP 📘.

## 16. Quick SCM-to-AI concept map
| Basic SCM concept | AI course application |
|---|---|
| Cycle vs safety stock | Forecasting AI attacks S only → size the pool first (S1) |
| Service level & quantiles | Probability forecasting; newsvendor critical ratio (S8) |
| Bullwhip | LLM agents amplify it; shared signals fix it (S4, S19) |
| Network flows | Min-cost-flow LP operated by an agent under a human mandate (S15) |
| Mode choice | AI re-evaluates mode mix per lane per hour; split under shocks (S14) |
| Tail spend & Kraljic | Autonomous negotiation (Walmart–Pactum) inside mandates (S4, S16) |
| Supplier risk | Risk scoring under EU AI Act human oversight (S5, S20) |
| Maintenance | RUL prediction, digital twins, twin-now/twin-later (S13) |
| S&OP | GenAI scenarios + optimiser; augment planners (S3, S18) |
| KPIs & guarded metrics | Frozen baselines, counter-metrics, gates (S3, S10) |
