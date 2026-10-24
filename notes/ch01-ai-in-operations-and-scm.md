# Ch 1 — Introduction to AI in Operations & SCM (Session 1)
**Syllabus unit 1 📘:** *Introduction to AI in Operations & SCM — agentic systems such as Amazon Kiva robots; platforms such as Azure AI, AWS AI.* **Session 1 📘:** "The evolution of intelligent supply chain systems — and an evidence-based look at what AI has (and has not) changed." Opening case: **NorthStar Foods — Forecasting Fix or Something Else?**

> **Exam use:** this chapter gives you the **Four-Question Claim Audit**, the **Q vs S** logic and the **rain-forecast** idea — the tools behind Trishul A1. Every vendor % claim in a case should be put through them.

---

## 1. A working taxonomy: from rules to agents ⭐⭐⭐
| Layer | What it is | SCM use |
|---|---|---|
| **Rule-based systems** | if-then logic, MRP run rules, reorder points; deterministic, auditable, brittle | still runs most of the world's ERP transactions |
| **Machine learning** | learns patterns from data: regression, trees, SVM, k-means, neural nets | demand sensing, risk scoring, quality inspection |
| **Deep learning** | multi-layer neural nets (CNN, RNN, LSTM, transformers); excels at perception | images, text, sequences, sensor streams |
| **Predictive (analytical) AI** | forecasts and classifies from history | demand, delays, failures, fraud — "the workhorse of supply chain analytics today" |
| **Generative AI** | creates new content: text, scenarios, code, designs (LLMs: GPT, Claude, Gemini) | scenario generation, drafting, design-to-shelf |
| **Agentic AI** | **acts autonomously toward goals with minimal human intervention: perceives, plans, uses tools, executes within guardrails** — "this course's focus" | negotiation, replenishment, routing, robot fleets |
**Precise vocabulary is your first defence against agent-washing** 📘. Class Q 1.1: software that reads supplier emails, drafts replies and — once approved — **posts confirmed delivery dates into the ERP** = **an agentic AI system** (perceives, reasons, acts on systems of record); approval-gating puts it **low on the autonomy scale**. A copilot stops at drafting; RPA follows fixed rules without reasoning over language.

**What AI actually is** 📘: **weak (narrow) AI** is all we have — it does one job (classify, recommend, forecast); strong AI remains science fiction. Its real talent is **pattern-matching** at scale (chess, Jeopardy, Go). The frontier is **learning over memorising** (a system shown eight dogs must generalise to a ninth). **Fit test:** work that runs on set rules and heavy pattern-matching benefits first; creativity or sparse-data judgement keeps a human in charge. AI has **seasons** (winters and summers) — judge capability, not the weather.

## 2. Technology timeline — from paved roads to agentic AI 📘
1. **Physical backbone** — paved roads, standardised containers (1956), combustion engine → cheap transport enabled large networks and global sourcing.
2. **Data capture** — barcodes (1974), EDI, RFID → transactions become machine-readable; visibility begins.
3. **Transactional systems** — MRP (1960s–70s), MRP II, ERP (1990s) → one database of record.
4. **Planning intelligence** — APS (late 1990s): optimisation and hierarchical planning on ERP.
5. **Learning systems** — e-commerce, IoT, cloud, ML forecasting and DRL (2010s).
6. **Generative & agentic** — LLMs (2022–), copilots, autonomous agents (2024–): systems that converse, reason and act.
**The test for each generation:** did it merely speed up existing tasks, or **enable supply chains that operate in fundamentally new ways**?

## 3. What APS already did — and where AI adds 📘
| Planning task | APS approach (1998–2015) | What AI/agents change |
|---|---|---|
| Demand planning | statistical time series + judgment | ML with external signals; continuous demand sensing |
| Master / S&OP planning | LP/MILP runs weekly–monthly | always-on re-planning; scenarios in minutes |
| Production scheduling | heuristics, finite-capacity schedulers | reinforcement learning; self-adjusting schedules |
| Distribution & transport | batch route optimisation | dynamic re-routing on live telematics and traffic |
| Available-to-promise | rule-based allocation from ERP | conversational, LLM-mediated commitments with reasoning |

## 4. The "modest impact so far" argument (Cachon, core reading) ⭐⭐
- **The claim:** AI has not yet made supply chains operate in fundamentally different ways or satisfy new customer needs.
- **The benchmark:** the Internet + mobile DID transform — Amazon's third-party marketplace abandoned the three classic retail tasks (location, assortment, pricing) — built **without** extensive AI.
- **The concession:** AI is young (ChatGPT barely four years old); judgement may be premature.
- **The pattern-recognition caveat:** classification works brilliantly (product ID, fraud) — useful, but it does not change supply chain design.
- **Discussion:** agree 2–3 observable tests of transformation (new operating model, structural cost change, new customer promise) and apply them to every case.

## 5. Why forecasting disappoints — two structural reasons ⭐⭐⭐
**1. Forecasting touches only part of cost.** Inventory is a **saw-tooth**: cycle stock from batch quantity **Q** + safety stock **S** against uncertainty. **A perfect forecast eliminates only S.** Most inventory sits in Q, driven by physical constraints (pallets, trucks, MOQs). In delivery routing, the out-and-back line-haul distance dominates; better forecasts barely shorten it, and matter less as volume scales.
**2. Diminishing returns to accuracy.** **Archery reward** (every gain pays) vs **rain-forecast reward** (80% vs 95% chance of rain → same umbrella decision). Supply chains are mostly rain-forecast settings: "124 vs 159 units forecast — either way you ship one 240-unit pallet." First gains are real; last increments map to the **same decision**.
- **Class Q 1.2 ⭐⭐⭐:** ₹8 cr cycle + ₹2 cr safety; vendor claims 30% cut → the single calculation is **size the safety-stock share of total inventory** (20% max). "Follow the cost pool, not the technology."
- **Class Q 1.3:** error ±40 → ±15 with full 240-unit pallets → **little to no business impact**. "Precision pays only when a decision changes."

## 6. The Campbell Soup lesson ⭐⭐⭐
A classic study of Campbell Soup's continuous-replenishment programme: the industry assumed sharing retail sales data would improve forecasts and therefore inventory. **Finding: improved forecasts had LIMITED impact; the real gains came from using the same technology to cut order-processing lead times and to order more frequently — reducing the inbound batch quantity Q, the true driver of inventory.** General lesson: ask which lever a technology actually moves — the glamorous one in the pitch, or the structural one in the physics.
*(NorthStar Foods, the opening case, poses exactly this choice: ML forecasting upgrade vs lead-time/order-frequency initiative; finance says order-size-driven stock costs ~4× the uncertainty buffer → Q is 4× S → fund the lead-time/frequency initiative first.)*

## 7. Where the real leverage is — three transformative candidates 📘
1. **Transportation economics** — everything that made transport radically cheaper restructured supply chains; autonomous vehicles would replace the driver's variable cost with engineering's fixed cost. 2016 MBA classes predicted majority-autonomous roads by 2026 — wrong; but Waymo runs commercially and freight pilots (Aurora, Kodiak, Gatik, Nuro) expand corridor by corridor. Manage with **options thinking and staged bets**.
2. **Strategic forecasting & counterfactuals** — a Walmart-scale chain runs on hundreds of separate systems nobody fully understands; ML can estimate counterfactuals of your *own* organisation ("what if we add a cross-dock layer?") and evaluate hundreds of structural ideas a year. Tactical forecasting optimises within the system; strategic forecasting redesigns it.
3. **Radical decentralisation — millions of virtual employees** — "Because an LLM speaks both 'human' and 'computer', it can act as the translator." Replace a few over-guarded mega-systems with millions of narrow LLM agents (e.g. one per product family) instructed in plain language; many OK decisions taken quickly, each with bounded risk, can beat one slow best decision — **kaizen applied to information systems**. **Class Q 1.4:** why it fails *today* even if each agent works → **agents amplify each other's actions** (bullwhip); robustness comes from coordination design, not agent count.

## 8. Named deployments 2024–26 ⭐⭐
| Company | Application | Reported result | Type |
|---|---|---|---|
| **Amazon** | **DeepFleet** generative-AI coordination of 1M+ warehouse robots (Jun 2025) | **10% cut in robot fleet travel time** | Agentic |
| **Walmart** | **Pactum** autonomous supplier negotiations (tail spend) | **~3% avg savings; 35-day payment-term extension; 64–68% close rate** | Agentic |
| **Unilever** | AI across ~20 global control towers | stockouts −25%; retailer sales +15–35% | Predictive |
| **P&G** | AI control tower across ~110 plants | deadhead trucking −15%; waste down up to 80% on key lines | Predictive |
| **Lenovo** | Blue Yonder demand/supply/factory planning | +5% forecast accuracy; +4% on-time; +10% delivery accuracy | Predictive |
| **Danone** | ML demand planning, multi-country | materially higher forecast accuracy | Predictive |
| **Walmart** | Trend-to-Product GenAI design-to-shelf | lead times cut by up to 18 weeks | Generative |
"Treat vendor-reported numbers with care."

### Amazon — one million robots and a foundation model (and the Kiva lineage) ⭐⭐⭐
- In **June 2025** Amazon deployed its **one-millionth** warehouse robot and launched **DeepFleet**, a generative-AI foundation model that coordinates robot traffic across fulfilment centres, **trained on Amazon's own fleet-movement data using AWS SageMaker** 📘. "An intelligent traffic-management system for a city filled with cars." **10%** less robot travel time; **75%** of Amazon orders touched by robotics.
- **Kiva Systems (syllabus example) 📗:** Amazon bought Kiva in **2012 for ~$775M** and renamed it **Amazon Robotics**. Kiva drive units are squat mobile robots that slide under **inventory pods (shelving units)** and carry them to stationary human pickers — **"goods-to-person"** instead of pickers walking aisles. Each robot follows **fiducial (barcode) markers on the floor**; a central system assigns tasks and paths. Effect: pickers stay put, storage density rises, pick rates rise several-fold and travel time disappears.
- **Why it matters (course framing):** Kiva is **physical automation** with central planning; DeepFleet is **fleet-level agentic coordination** — "not one smart robot, but a learned policy that orchestrates a million of them" 📘. It is Session 1's decentralisation logic **implemented in the physical layer first**, and why the suitability screen ranks **warehouse robot routing as the most agent-suitable** decision (high frequency, reversible, fast feedback, own premises).

### Nike & i2 (2001) — the $400M forecasting lesson ⭐⭐
Nike deployed a state-of-the-art demand-planning system as the centrepiece of a **~$400M** programme; within months it ordered slow-moving shoes and under-ordered hot sellers (implementation shortcuts, mismatched data granularity, untested demand logic). Result: **~$100M** quarterly shortfall, **~20%** share-price fall, and the CEO's line "*This is what you get for $400 million?*" **Lesson:** forecasting systems **amplify** the data and process foundations under them; accuracy claims mean nothing until tested against decisions on your own history.

### What "transformative" looks like 📘
**Ocado** (online grocer → robotics-platform company; tech sold to Kroger, Aeon, Sobeys — the supply chain became the product) · **Cainiao** (asset-light orchestration via electronic waybills; coordination as the product) · **Asian Paints** (demand data drove direct-to-dealer distribution that **removed a distributor tier** — turns ~3–4× peers). All pass the transformation tests: new operating model, structural cost change, new customer promise.
**Across industries** 📘: FANUC (predict robot failures → uptime), H&R Block with IBM Watson (AI surfaces deductions; the professional owns the call — augmentation), BlackRock Aladdin (25,000+ users; two decades of compounding foundations). AI pays off where it moves a **named decision or cost pool** and meets disciplined execution.

## 9. Platforms named in the syllabus — Azure AI and AWS AI (preview of Ch 5)
- **Microsoft Azure** 📘: Azure AI Foundry (OpenAI GPT models, agent service), Azure Machine Learning (MLOps), Microsoft Fabric (lakehouse), Dynamics 365 Supply Chain Management with embedded agents (demand planning with external signals, inventory rebalancing, picking-route optimisation), Supplier Communications Agent, Copilot Studio, Power Automate, Purview, Entra for agent identity. **Best fit: Microsoft-centric estates.**
- **Amazon Web Services** 📘: Amazon Bedrock (multi-model: Claude, Llama, Nova, OpenAI), SageMaker (build/train/deploy — DeepFleet was trained on it), Trainium/Inferentia chips, **Bedrock AgentCore** (model-agnostic agent runtime, MCP tool gateway, Guardrails), **AWS Supply Chain** ("30 years of Amazon operational science" productised). **Best fit: engineering-strong organisations wanting model choice.**

## 10. Why AI investments disappoint — the numbers and the problem set ⭐⭐
**Market context 2026 📘:** SCM software with agentic AI: **$2B → $53B (2025→2030)** (Gartner); **60%** of SCM-software enterprises expected to adopt agentic features by 2030 (from 5%); **55%** of 509 SC leaders expect agentic AI to cut entry-level hiring; **40% of agentic AI projects predicted cancelled by end-2027**. MIT 2025: **~95% of GenAI pilots show no measurable P&L impact**; Melbourne CBA: ~80% of analytics projects fail; BCG 2026: **44%** deploy AI in SC but only **~30%** of those advance beyond copilots ("copilot-stuck"); McKinsey's **"gen AI paradox"**.
**The Session 1 problem set:** **misallocated spend** (glamorous informational levers funded, structural levers unfunded), **phantom accuracy value** (gains that never cross a decision threshold), **hype whiplash** (RFID/blockchain arc), **evidence laundering** (market-size stats and logos standing in for mechanism proof). Class Q 1.5: "44% already deploy, market will hit $53B" → **ask which adopters show measurable value** ("adoption statistics measure purchasing, not value"). Class Q 1.6: the soundest first test of "learns your business and answers any question" → **which decision it changes, and its benchmark**.
**House style:** "pragmatic optimism — open to possibilities, alert to limitations, allergic to hype."

## 11. Principles older than AI 📘
The **cost-structure lens** (cost lives in batch sizes, lead times, network structure); **chain-fit strategy** (Fisher 1997; agility-adaptability-alignment 2004; "digital super-agility" 2026); the **feedback-system lens** (bullwhip governs how AI agents react to each other); the OM community's position (AI reshapes practice; matching supply and demand under uncertainty remains the core). "Vendors sell tools; this course teaches principles. Tools expire quarterly."

## 12. The tools you take with you
- **Four-Question AI Claim Audit**: Mechanism? Cost pool? Decision changed? Evidence? → [Frameworks §1](course-frameworks.md).
- **AI Adoption Roadmap**: Ideation → Defining → Data curation & governance → Prototyping → Production → Thriving with the lifecycle; "fail quickly, fail regularly, fail tiny".

## Key takeaways (S1 recap 📘)
1. AI's supply chain impact to date is real but modest — judge by mechanism, not momentum.
2. Forecasting is structurally limited: it addresses only the safety-stock share, with diminishing returns.
3. The Campbell lesson: the winning lever is often lead time and order frequency (Q), not forecast precision (S).
4. Transformative candidates: autonomous transport, strategic counterfactuals, radical decentralisation via narrow agents.
5. 2026 commits billions while 40% of projects are predicted to fail — the Four-Question Audit is your edge.

---

## Self-test
**Q1. A vendor says its AI "will cut your inventory 30%". Your stock is ₹12 cr cycle and ₹3 cr safety. What do you write?**
Assumptions: forecasting changes S only; Q is set by trucks and cadence. Pool = 3 ÷ 15 = 20% maximum → 30% is impossible from forecasting alone; ask what lever touches Q (lead time, order frequency). Then run the other three audit questions.

**Q2. Why can a big accuracy improvement have almost no business value?**
Because supply chain decisions are discrete (pallets, trucks, MOQs): once a forecast change no longer changes the order, extra precision is decoration — the rain-forecast reward function.

**Q3. Classify: (a) a tool that drafts supplier emails for a planner to send; (b) a tool that emails a prioritised action list each morning; (c) a tool that negotiates and closes tail-spend deals inside a mandate.**
(a) GenAI copilot, L1; (b) not an agent — recommends only (L2-type output, nothing executed); (c) agentic AI at L4 (bounded autonomy, Pactum-style).

**Q4. What makes Amazon's DeepFleet "agentic" when Kiva robots were "automation"?**
Kiva robots execute centrally assigned moves along fixed markers; DeepFleet is a learned, continuously improving generative policy that coordinates a million robots' traffic toward a goal (less travel time) — goal-owning, adaptive orchestration within physical guardrails.

**Q5. A board member says "everyone is doing agentic AI — 44% of firms deploy it". Reply in two lines.**
Adoption measures purchasing, not value: only ~30% of those firms get beyond copilots and ~95% of GenAI pilots show no P&L impact. Show me which adopters in our situation moved a named cost pool, and by how much.
