# Ch 5 — AI Platforms for SCM: Azure, AWS and Enterprise Ecosystems (Session 5)
**Syllabus 📘:** platforms such as **Azure AI, AWS AI**. **Session 5 📘:** "The platform landscape from chips to copilots — and the invisible physical supply chain that brings AI itself to life." Opening case: **Solstice Industrials — Platform Choice Under Constraint** (Microsoft-centric estate vs AWS's faster pre-built pilot; a GPU shortage delays either choice by a quarter; the sustainability office asks about emissions).

> **Exam use:** platform questions in a case usually test **data gravity, governance fit and the provider/deployer duty split** (Trishul A4 is exactly Class Q 5.5). Token-cost overruns test **FinOps, not platform switching** (Class Q 5.4).

---

## 1. The AI technology stack — where value and power sit ⭐⭐
| Layer | Contents | Concentration / risk |
|---|---|---|
| **1 Silicon & hardware** | GPUs/accelerators (NVIDIA), fabs (TSMC), lithography (ASML), memory, networking | extreme concentration; geopolitical chokepoints |
| **2 Infrastructure** | hyperscale data centres, power, cooling, connectivity; sovereign/edge | GW-scale power demand |
| **3 Foundation models** | GPT (OpenAI), Claude (Anthropic), Gemini (Google), Llama (Meta), domain models | rented via API, rarely owned |
| **4 Platform & orchestration** | Azure AI Foundry, AWS Bedrock/SageMaker, Vertex AI; agent runtimes, guardrails, MLOps | lock-in terms |
| **5 Applications** | ERP/SCM suites (SAP, Oracle, Dynamics), planning specialists (Blue Yonder, Kinaxis, o9), vertical agents (Pactum, ToolsGroup) | point-solution sprawl |
"Most SCM organisations buy at layers 4–5 and should — but power, cost and risk cascade down from layers 1–2."

### The AI hardware supply chain in five numbers 📘
**>60%** of global chip fabrication controlled by **TSMC** (advanced AI nodes even more concentrated in Taiwan) · **1** supplier of EUV lithography machines (**ASML**, Netherlands) · **~70%** of rare-earth processing in **China** · **GW-scale** new data-centre power demand straining grids — energy is now a binding constraint on AI growth.
**From wafer to warehouse:** accelerators + high-bandwidth memory + InfiniBand-class networking (own shortages and lead times); copper and optical dependencies; a **cooling crunch** (coolant distribution units on the critical path); power contracts (PPAs, even nuclear restarts) are now AI supply-chain decisions; lifecycle and **e-waste**. "When you sign a platform deal, you inherit its upstream risks — evaluate them like any supplier."
**Class Q 5.1:** your cloud region has a multi-month GPU waitlist; two vendors blame each other → **sequence around the shared constraint** (it binds every hyperscaler; contract design and phase sequencing manage it). "**Every platform is a supply chain; audit it like a supplier.**"

## 2. Microsoft Azure — strongest enterprise-workflow integration ⭐⭐⭐
- **Core AI services:** **Azure AI Foundry** (models incl. OpenAI GPT family, agent service), **Azure Machine Learning** (MLOps), **Microsoft Fabric** (data lakehouse), **Dataverse** (unified data layer).
- **SCM-native applications:** **Dynamics 365 Supply Chain Management** with embedded agents — demand planning with external signals, inventory rebalancing, picking-route optimisation.
- **First-party SCM agents (2026):** **Supplier Communications Agent** (order confirmations, schedule changes, document chasing); Copilot monitors external risk (weather, supplier financial stress, geopolitics) and drafts mitigation actions — agents that "reason, decide, and act within governed boundaries".
- **Orchestration & governance:** **Copilot Studio** (custom agents), **Power Automate** (process orchestration), **Purview** (data governance), **Entra** (agent identity).
- **Best fit:** organisations already on Microsoft 365/Dynamics/Teams — agent surfaces live where planners already work.
- **Production proof:** Microsoft's own cloud supply chain runs LLM decision support over unified data and existing optimisation models (S2).

## 3. Amazon Web Services — deepest infrastructure + Amazon's own ops DNA ⭐⭐⭐
- **Core AI services:** **Amazon Bedrock** (multi-model: Anthropic Claude, Meta Llama, Amazon Nova, now OpenAI models), **SageMaker** (build/train/deploy ML; **Canvas** no-code variant), custom silicon **Trainium/Inferentia**.
- **Agent platform:** **Bedrock AgentCore** — model-agnostic agent runtime with an **MCP-based tool gateway**, managed web-search grounding, **Guardrails** screening for prompt injection and sensitive data, and trace-based agent-improvement loops.
- **SCM application layer:** **AWS Supply Chain** — demand planning, inventory visibility and n-tier insights on a unified data lake ("30 years of Amazon operational science" productised); 25+ specialised SC tools in the Connect Decisions suite.
- **Proof at home:** **DeepFleet** trained on SageMaker — Amazon runs its million-robot network on this stack.
- **Best fit:** engineering-strong organisations wanting model choice, custom agents and infrastructure control; retailers wary of Amazon as a vendor may not (competitive tension).

## 4. Google Cloud and the real question 📘
Google Cloud: **Vertex AI** (Gemini, AutoML), **BigQuery**, strong data/ML heritage; supply chain via partners (o9, Blue Yonder on GCP) and **OR-Tools**. **Multi-cloud reality:** large enterprises average 2+ clouds; governance must span them. **The real questions:** where does your **data** already live (gravity)? which ERP/planning suite anchors you (SAP → Azure bias; retail → GCP/Azure; engineering → AWS)? what do your regulators require (sovereignty, EU AI Act)? **Cost discipline:** token/compute pricing is volatile and usage explodes silently — **FinOps for AI** is a 2026 discipline: committed-use discounts and **per-agent budgets** (guardrails again).

## 5. SCM suites and specialists — the 2026 field ⭐⭐
| Platform | Centre of gravity | AI/agentic capability (2026) | Watch for |
|---|---|---|---|
| **SAP (IBP, Ariba)** | ERP-anchored planning & procurement | **Joule agents** GA across Ariba Intake/Contracts and Fieldglass (Jun 2026); "Autonomous Spend Management"; agent runtime free through 2026 | depth vs lock-in; BTP rebuild maturity |
| **Oracle** | ERP + SCM cloud | embedded AI across Fusion SCM; agents rolling out | anchor logic like SAP |
| **Blue Yonder** | retail/mfg planning & fulfilment | cognitive planning, agentic roadmap; **Lenovo: +5% forecast accuracy, +4% OTD, +10% delivery accuracy** | Panasonic-owned; architecture transition |
| **Kinaxis** | concurrent planning (RapidResponse/Maestro) | embedded explainable agentic capability; **Reckitt: schedulers shift from building schedules to analysing scenarios** | best-of-breed integration burden |
| **o9 Solutions** | "digital brain" planning graph | knowledge graph + GenAI planning agents | implementation discipline decides value |
| **Specialists** | narrow, deep agents | **Pactum** (negotiation), **ToolsGroup** (probabilistic planning), Coupa Navi, Zycus GenAI S2P | point-solution sprawl |

## 6. What a platform actually assembles 📘
Language splits three ways — **speech recognition**, **understanding**, **generation** — invest in what your use case leans on; **decision engines** that encode business logic and explain decisions are a distinct tier; frameworks under the services: **TensorFlow, Keras, PyTorch, scikit-learn**. A no-code virtual-agent builder, a managed-ML service and a custom framework build are three different SLAs, costs and skill demands — "pick to fit, not to impress". Retest any benchmark on your own data.

## 7. When a firm builds the whole stack — JD.com's "dual engine" ⭐⭐
JD.com — China's largest retailer by revenue — logistics reaching ~99% of the population, **~90% of orders delivered within 24 hours**, >1,000 million self-operated SKUs — built its own AI supply chain platform. Principle: the **"dual engine" — AI (forecasting, learning, perception) coupled with OR (optimisation, guarantees)** — neither alone. Why build? At JD's scale the supply chain **IS** the product (a new operating model). **Class Q 5.3:** an average CPG firm wants to build its own platform "like the famous 24-hour retailer" → build vs buy is decided by **real differentiation only**; "copying the build without the differentiation copies the cost without the moat". "**Own the differentiating loop; rent the rest.**"

### Three platform fates 📘
**TradeLens (2018–23)** — Maersk–IBM blockchain shipping platform shut down citing the missing "level of industry collaboration" (rivals would not join a competitor's platform — the agency problem) · **Walmart Element** — internal, model-agnostic ML platform built for control and lock-in avoidance · **Ocado Smart Platform** — built until licensing it (Kroger, Aeon, Sobeys) rivals the grocery business. "Platform outcomes track **differentiation and adoption incentives**, not feature lists."

## 8. Build, buy or blend ⭐⭐⭐
| Buy (suite features & SaaS agents) | Build (custom agents on hyperscalers) |
|---|---|
| fastest time-to-value; vendor carries model risk, upgrades, much governance | exactly your process, guardrails, data; reusable data products compound |
| best when the use case is **common** and differentiation **low** (demand planning, supplier comms) | best when the decision **is** your edge (DeepFleet, JD.com) and talent exists |
| costs: subscription creep, roadmap dependency, shallow fit at the edges | costs: talent scarcity, MLOps burden, you own every failure |
**Most firms should BLEND: buy the backbone, build the edge.** Ask first: **does a good service already exist?** (Class Q 5.6: before building a custom OCR/document-classification pipeline for invoices). Compose with APIs and microservices; **rent scarce talent for the build, own it for the loop**; select tools on a **capability × cost × integration × skills** matrix; keep a **model library**; **read the SLA like a supplier contract** (latency, uptime, exit terms are the real product).

## 9. The 2026 adoption economics 📘
**74%** of manufacturers plan agentic AI within two years — only **~1 in 5** has mature governance for autonomous agents (Deloitte) · **55%** of SC leaders raising tech investment; 60% of them budget >$1M, 19% >$10M (MHI + Deloitte) · **44% → 30%**: firms deploying AI in SCM vs those advancing beyond copilots (BCG) — "the copilot trap in two numbers" · **Time-series foundation models** ("rent your forecasting") remain promising but **not dominant** vs tuned models in operational benchmarks.
**Class Q 5.4:** six months in, copilot token spend is **3.2× forecast**; was the platform wrong? → **No — fix usage discipline.** Token spend grows silently; that is FinOps territory (like freight overruns not invalidating a warehouse location). Revisit the platform only if **governed** consumption still breaks the case. "TCO includes consumption governance, reviewed quarterly."

## 10. Choosing a platform — six filters in order ⭐⭐⭐
| # | Filter | Question |
|---|---|---|
| 1 | **Use-case fit** | start from the roadmap pilots (S3) — suite feature, custom agent, or both? |
| 2 | **Data gravity** | moving data is cost, latency and risk — prefer compute near systems of record |
| 3 | **Governance fit** | agent identity, guardrails, audit, regional compliance (EU AI Act, DPDP) — **can the platform enforce YOUR autonomy ladder?** |
| 4 | **Ecosystem & skills** | what can your team (and hiring market) actually run — Microsoft shop vs AWS-native vs SAP country? |
| 5 | **TCO & pricing risk** | licences + tokens + integration + change management; model price volatility; exit costs |
| 6 | **Lock-in & optionality** | open standards (MCP), model-agnostic runtimes, data-egress terms — keep the ability to switch models mid-decade |
**Class Q 5.2:** a cheaper, feature-rich platform cannot enforce per-agent spend limits or produce complete action logs, and your roadmap has an L4 procurement agent next year → **disqualified — no envelope enforcement**. "Filters in order; governance before features."

## 11. Duties that cannot be delegated — the EU AI Act provider/deployer split ⭐⭐⭐
**Class Q 5.5:** your supplier-risk model's scores feed **contract renewals for EU-serving plants**; the vendor says compliance "is handled by the platform" → you must verify **the provider/deployer duty split, which is yours**. High-risk AI duties are allocated along the AI supply chain: the **vendor carries provider duties**; **oversight of your USE of the system is yours by law**. Write the **responsibility matrix into the contract** and **design the human-oversight workflow now**. "Platform contracts must allocate regulatory duties explicitly." → This is **Trishul A4** almost word for word.

### Solstice Industrials resolved (sketch)
Assumptions: the estate is Microsoft-centric (data gravity, skills); the GPU shortage hits every hyperscaler. Decision: **filters in order** — use-case fit and data gravity favour Azure/Dynamics; governance fit must be proven by both vendors (per-agent identity, spend caps, logs); the GPU delay changes the **plan** (sequence predictive pilots that need less compute first), not the **decision**. Emissions: ask both vendors for region-level carbon intensity and PUE; choose regions and model tiers accordingly. Refuse to decide this week on feature demos; demand governance evidence, TCO including tokens, and exit terms.

## Key takeaways (S5 recap 📘)
1. The AI stack is a supply chain: silicon → infrastructure → models → platforms → applications; power concentrates upstream; risk flows into your contracts.
2. Energy, cooling and hardware lifecycles are binding constraints that platform prices and quotas carry.
3. Hyperscalers converge on capability; choose by data gravity, governance fit, skills and lock-in.
4. The application layer is where SCM context lives — suites for the backbone, custom agents for edge cases, specialists for sharp edges.
5. Module 1 arc: impact realism (S1) → data/tech readiness (S2) → process/org readiness (S3) → agentic machinery (S4) → platform economics (S5).

---

## Self-test
**Q1. A vendor says its platform "handles EU AI Act compliance" for your supplier-risk scoring. Reply.**
It can carry provider duties, but as deployer we own human oversight of how scores are used; we will write a responsibility matrix into the contract and design a review-before-renewal workflow with logging.

**Q2. Token spend is 3.2× forecast. Switch platforms?**
No. Fix consumption governance first: per-agent budgets in code, caching, shorter contexts, cheaper model tiers, committed-use discounts. Revisit the platform only if governed consumption still breaks the case.

**Q3. Why might a cheaper, more feature-rich platform be disqualified?**
If it cannot enforce per-agent spend limits and complete action logs, it fails the governance filter, which comes before cost and features — at L4 that gap is unbounded financial exposure.

**Q4. When is "build" right?**
When the decision is your differentiation (the supply chain is the product, as at JD.com or Amazon), you have unified data and engineering depth, and the economics justify owning every failure. Otherwise buy the backbone and build only the differentiating loop.

**Q5. Name the Azure and AWS components you would use for (a) custom agent identity and governance, (b) model training, (c) an agent runtime with prompt-injection screening.**
(a) Azure: Entra (identity), Purview (data governance), Copilot Studio; (b) Azure Machine Learning / AWS SageMaker; (c) AWS Bedrock AgentCore with Guardrails (Azure equivalent: AI Foundry agent service).
