# Ch 2 — AI Readiness I: Data & Technology Foundations (Session 2)
**Session 2 📘:** "Data quality, master data, systems integration and the technical stack that decides whether AI creates value or amplifies chaos." Opening case: **Meridian Apparel — Are We Ready for AI?** (the CEO wants a Zara-style trend-detection pilot now; problems: duplicate SKUs, 24-hour data latency, no GPU budget, unknown API inventory; the e-commerce division is clean and API-first).

> **Exam use:** this is the chapter behind **Trishul A2 and A3** (duplicate vendor records, stale report, 26-hour latency, phished credentials) and the readiness profile **[2,2,3,3,4]** in the case stem. Whenever a case gives you a readiness score or a systems exhibit, read it with this chapter's scorecard and requirements-delta table.

---

## 1. The core thesis
"AI's effectiveness in the supply chain hinges on access to accurate, timely, and integrated data … Without high-quality, accessible data, AI cannot deliver reliable predictions or real-time insights." (Robinson, core reading 📘). Readiness is **the variable that flips project expected value**: ~95% of unready GenAI pilots fail, while ready deployments report **10–20% cost reduction and 10–15% service improvement** (McKinsey) 📘.

## 2. Four categories of readiness barriers 📘
| Category | Covered |
|---|---|
| **Data & technology infrastructure** (today) | data quality & accessibility; legacy systems & integration; security & privacy |
| **Cost & sustainability** | high implementation cost; regulatory volatility (EU AI Act, China labelling, Canada AIDA); energy & water footprint |
| **Talent & organisational capability** (S3) | skills gaps, citizen data scientists, resistance, complacency, de-skilling risk |
| **Strategy, leadership & collaboration** (S3) | executive expectations, silver-bullet mentality, no AI strategy, functional silos |

## 3. Six dimensions of data quality — SCM edition ⭐⭐⭐
| Dimension | Definition | Supply chain failure example 📘 |
|---|---|---|
| **Accuracy** | values reflect reality | system says 240 on hand; count finds 175 → phantom inventory → false replenishment |
| **Completeness** | no critical gaps | lead time blank for 40% of SKUs → planning defaults to 14 days |
| **Timeliness** | fresh enough for the decision | weekly POS for a daily demand-sensing model → "the AI just smooths stale data" |
| **Consistency** | same fact, same value everywhere | 8801-A (ERP) / 8801A (WMS) / "8801 A" (portal) → three products |
| **Uniqueness** | one record per entity | same vendor 6 times with different terms → spend analytics undercounts by 60% |
| **Validity** | values conform to rules | negative lead times, 1900-01-01 dates → silently skew training |
(Standard **DAMA** dimensions applied to SCM.) **Class Q 2.2:** a "real-time" demand-sensing pilot when 70% of sales arrive by overnight batch → **timeliness is binding — the data is too stale for the promise**. Quality dimensions are **per-use-case requirements**: 24-hour data is fine for weekly planning, fatal for real-time sensing. "Diagnose the binding dimension before the model, not after the disappointment."
*Trishul mapping:* uniqueness (2,890 vendor records for ~2,410 suppliers), consistency (11% SKU attribute conflicts ERP vs portal), timeliness (26-hour batch on 71% of revenue), and an **accuracy** problem with the *reports themselves* (a 14-month-old "under 2%" claim).

## 4. Master data — "where AI projects go to die" ⭐⭐⭐
- **What it is:** the slow-changing reference backbone — item, vendor, customer, location masters, BOMs, routings. Transactions inherit whatever the masters say.
- **Why AI amplifies MDM debt:** a human planner recognises the duplicate vendor and mentally corrects; **a model — and worse, an autonomous agent — takes the data literally and acts on it at machine speed and scale**.
- **Self-learning makes it worse:** "existing process and data flaws are AMPLIFIED, not averaged away."
- **The governance answer:** data ownership and stewardship roles, golden-record policies, dedup and validation pipelines, measured data-quality KPIs — "boring, decisive, and a prerequisite to everything".
- **Field evidence:** SAP-ecosystem guides converge — clean, governed material and vendor masters unlock planning accuracy, visibility and reliable AI; enterprises now run formal "data readiness assessments".
- **Class Q 2.1:** largest supplier shows 4% of spend but is duplicated across six records → analytics **measured record-keeping, not true concentration**. "Data defects compound at machine speed."

## 5. Data architecture generations ⭐
**1 Data warehouse** (curated, batch; great for BI, too rigid for ML) → **2 Data lake** (cheap raw storage; often a "data swamp") → **3 Lakehouse + streaming** (lake economics, warehouse discipline; Kafka-style real-time pipelines) → **4 Semantic / knowledge layer** (ontologies and knowledge graphs define "customer", "on-time", "lead time" ONCE) → **5 Agent-ready data products** (governed, documented, API-accessible products agents can query autonomously, with permissions, lineage and audit trails). Firms that treat data pipelines, ontologies and stewardship as long-term investments — **on par with warehouses and ERP** — convert AI experiments into enterprise value.

## 6. Outside-in data — external signals
Modern planning should **start from market signals** (channel demand, weather, geolocation, reviews, social trends), not internal order history. Zara (real-time trend detection), Danone (ML across countries and horizons). IoT/telemetry creates the perception layer for agents. **The catch:** every new source multiplies quality, integration and privacy questions — **external data is a force multiplier only on top of clean internal data.**

## 7. Where training data comes from 📘
**Own it, license it, or make it** (most systems use all three). Ground truth is the truth the model learns; keep a validation slice. **Balanced vs proportional** sampling: match class frequencies to reality except for rare events (fraud, defects) where you over-sample. Licensing levers: model-use vs display, derived vs raw, scale, recency. **The 60–80% rule:** successful deployments spend most effort finding, cleaning, labelling and consolidating data — not modelling. **Class Q 2.6:** identical demand-sensing model at two firms → the predictor of success is **Firm A's data governance and accessibility** (one owner per domain, nightly DQ reports). "Foundations before intelligence; semantic before agentic."

## 8. The real enterprise stack
The "spaghetti reality": a single ERP plus dozens of modules, best-of-breed planning/WMS/TMS, stitched by patchwork upgrades, mergers and tactical fixes — plus the **shadow layer** of Excel macros and Access databases running mission-critical processes; point-to-point interfaces, overnight batch jobs, undocumented dependencies. Lack of GPU access or modern architecture forces clunky side projects. **"AI bolted onto a fractured stack inherits every fracture — at machine speed."** (Board sketch: one ERP box, ringed by best-of-breed tools, ringed by spreadsheets — where does planning really happen? Almost always the spreadsheet ring. Trishul: **61%** of planning decisions in spreadsheets.)

## 9. Two honest modernisation strategies ⭐⭐
| Replatform first (purist) | Wrap and modernise (pragmatic) |
|---|---|
| consolidate ERP instances, harmonise masters, build the lakehouse, then deploy AI | leave the core; expose it via APIs/middleware; build a governed data layer alongside; deploy narrow AI use cases that fund the journey |
| **Pro:** AI inherits integrity; nothing built twice | **Pro:** value in quarters; learning compounds; sponsorship survives |
| **Con:** multi-year, politically brutal, benefits late — sponsors may not survive | **Con:** risks permanent scaffolding — needs discipline to retire debt |
Course verdict: **wrap-and-modernise beats big-bang replatforming for most firms, if debt retirement stays disciplined.** (Trishul: the API-based e-commerce/modern-trade feeds — 29% of revenue — are the natural first domain for a predictive pilot, like Meridian's clean e-commerce division.)

## 10. Cloud and scaling realities 📘
Auto-scale has a lag (expect up to **~3 minutes** of inaccessibility while scaling — bites at month-end and promotions); **load-test ~20% above peak**; deployment ladder bare metal → VMs (IaaS) → containers (Docker/Kubernetes, infrastructure as code) → managed AI clouds (pay per execution); **chaos tools** kill random components to expose gaps; the **SLA is a worst-case promise**, not the average.

## 11. Security and privacy — the expanding attack surface ⭐⭐⭐
- Every model endpoint, API connection and pipeline is a new door; **NotPetya cost Maersk ~$300M in 2017** — one unpatched dependency.
- **AI-specific threats:** data poisoning, **prompt injection** against agents, model theft, sensitive-data leakage through outputs.
- **Regulatory volatility:** EU AI Act (risk-based), China's AI-content labelling, Canada's AIDA, **India's DPDP Act** (personal data). Compliance is a **design input**.
- **Privacy-preserving techniques:** federated learning, differential privacy, structured licensing.
- **Cross-tier tension:** traceability needs transparency; suppliers resist exposing quality and sourcing data.
- **Class Q 2.3 ⭐⭐⭐:** an attacker phished a vendor-facing API credential last year; nobody has a complete inventory of which systems talk to which; the CIO proposes purchasing agents with **write access** to the ERP → **Block until API inventory and access controls exist.** Write-capable agents inherit and extend the attack surface; **prompt instructions are not controls**; identity, scopes and audit are preconditions. "**Autonomy raises every bar.**" *(Trishul: API inventory 14 months old; two vendor-facing credentials rotated after phishing → the same verdict for P2's write access.)*

## 12. Predictive vs agentic — the readiness delta ⭐⭐⭐
| Requirement | Predictive model | Autonomous agent |
|---|---|---|
| Data freshness | batch often fine | streaming / near-real-time |
| Data access | read-only extracts | governed read **and write** APIs into systems of record |
| Integration | one-way into dashboards | two-way: MCP-style tools, transaction posting |
| Identity & permissions | data-science credentials | **per-agent identity, least privilege, spend limits** |
| Observability | accuracy monitoring | action logs, decision traces, rollback, **kill switch** |
| Failure mode | wrong number on a screen | **wrong purchase order in the ERP** |
**This is your go/no-go table** for any "agent" proposal.

## 13. Foundations in the field ⭐⭐
**The cautionary canon:**
| Case | What happened | Lesson |
|---|---|---|
| **Target Canada (2013–15)** | item master built under deadline pressure; post-mortems found record accuracy **near 30%** at launch (wrong dimensions, currencies, units); empty shelves beside overflowing DCs; exit cost **C$2B+**, 17,600 jobs | master data is the supply chain's DNA |
| **Lidl + SAP (2011–18)** | seven years and **~€500M**, then cancelled; the new system was forced to mirror a legacy quirk (inventory valued at retail price) | don't lift-and-shift process onto technology |
| **Hershey (1999)** | big-bang ERP + planning + CRM go-live weeks before Halloween; **~$100M** of orders missed; ~8% share fall in a day | the transformation dose exceeded survivable |
**The positive canon:** **Danone** (years of master-data and pipeline work underneath ML), **Walmart Element** (internal model-agnostic ML platform, lock-in avoidance), **Unilever** (~20 control towers on harmonised data: stockouts −25%, retailer sales +15–35% — the semantic layer made real), **Microsoft's cloud supply chain** (production LLM decision support: planners ask what-ifs in natural language — "what happens to deployment dates if the Dublin DC is delayed two weeks?" — the LLM calls existing optimisation models and explains results; it worked because **data was already unified and the OR models already existed** — "the LLM was the last mile").
**Class Q 2.4:** same LLM assistant succeeds on unified data and dies on fragmented spreadsheets → the difference is **prior foundations in place**.

## 14. A practitioner "Are you data ready?" gate 📘
**Collected and sufficient** (labelled history the use case needs) · **Accessible** (not trapped in silos) · **Governed with named ownership** (stewardship and data-scientist role before modelling) · **Feedback loops close** (corrections flow back — readiness is a loop, not a one-time audit).

## 15. Beyond the textbook (2026) 📘
Practitioners: **semantic layer first** — bolting agents onto legacy planning stacks is "AI Stupid". BCG: the ~70% stuck at copilots share fragmented data; the ~30% who advance invested in unified platforms and end-to-end workflow ownership. Academic **TOE/absorptive-capacity** research: technology is consistently the **easiest** dimension. **EU AI Act: readiness becomes law** — high-risk obligations enforce from **2 August 2026**: data-governance duties include **bias examination, provenance tracking and quality protocols**, propagating along supply chains like product compliance.

## 16. Principles for upgrading the stack 📘
Prioritise by strategic vision (not the vendor's demo) · demand transparency and explainability · design for integration and scalability · prefer public cloud where possible (capex → opex, GPUs on demand, hyperscaler security) · mind the energy and water footprint.

## 17. The Data & Technology Readiness Scorecard ⭐⭐⭐
Score each pillar **1–5 with evidence**: **1 Data quality** (six dimensions on critical entities; profiling stats, cycle-count accuracy) · **2 Master data & governance** (owner? golden records? dedup rate? DQ KPIs watched?) · **3 Architecture & integration** (batch vs streaming; API coverage; % planning in spreadsheets; lineage) · **4 Security & compliance** (attack surface, access controls, EU AI Act/DPDP readiness) · **5 Compute & tooling** (cloud/GPU in the workflow; MLOps; production without heroics).
**Read the profile as a roadmap.** **Class Q 2.5:** [Data 2, Masters 1, Architecture 3, Security 2, Compute 5] → **predictive pilot on the cleanest domain first** (masters at 1 poisons everything; security at 2 forbids write access; compute 5 is a stranded asset). "The scorecard sets the ceiling; money cannot shortcut discipline."

### Worked reading — Trishul [Data 2, Masters 2, Architecture 3, Security 3, Compute 4]
| Pillar | Evidence in the exhibits | Implication |
|---|---|---|
| Data quality 2 | 26-hour batch on 71% of revenue; 11% SKU conflicts | P1 demand sensing not feasible on most revenue; pilot on the API-fed 29% |
| Masters 2 | 18% duplicate vendors, no owner; stale "<2%" report | Dedup + named owner before any procurement agent |
| Architecture 3 | single 11-year ERP + 61% spreadsheet planning; modern cloud tenant | wrap-and-modernise; APIs exist for e-com/MT |
| Security 3 | API inventory 14 months old; phishing → credentials rotated | refresh API inventory, per-agent identity before write access |
| Compute 4 | GPU credits unused, DS team of 6 | stranded asset until 1–2 catch up |
**Ceiling:** predictive and bounded-transaction pilots; no high-autonomy write agents until masters and security reach ≥3–4.

## Key takeaways (S2 recap 📘)
1. Readiness flips project expected value: 95% of unready pilots fail; ready ones report 10–20% cost gains.
2. Data quality has six diagnosable dimensions — master data is the highest-leverage, least glamorous fix.
3. Self-learning systems amplify data and process flaws; agents act on them at machine speed. Clean first, automate second.
4. Legacy integration is the structural barrier: wrap-and-modernise beats big-bang for most firms.
5. Agentic AI raises every bar — streaming data, write APIs, per-agent identity, audit trails; the requirements delta is your go/no-go tool.

---

## Self-test
**Q1. A firm wants a real-time demand-sensing agent; 70% of its sales data arrives by overnight batch. Which data-quality dimension binds, and what do you recommend?**
Timeliness. The promise ("real-time") is impossible on stale data; either fix the feed (API/streaming from the legacy POS) or scope the pilot to the channels that are already near-real-time.

**Q2. Why is a 14-month-old IT report saying "duplicates under 2%" not evidence?**
It is stale, no one owns the vendor master to keep it true, and live counts contradict it (2,890 records for 2,410 suppliers ≈ 17–20% duplicates). Prefer current, measured evidence over historical assertions.

**Q3. Give three reasons a write-access purchasing agent must wait at a firm that was just phished.**
No complete API inventory (unknown attack surface); credentials already compromised once (the agent becomes "an attack vector with a budget"); prompt instructions are not controls — you need per-agent identity, least-privilege scopes, spend limits and audit logs first.

**Q4. Compute scores 5, masters score 1. What is the first move?**
A predictive pilot on the cleanest domain, while fixing masters (owner, golden records, dedup). Compute is a stranded asset until foundations catch up; no agents with write access.

**Q5. What did Microsoft's cloud supply chain have that a spreadsheet-based firm did not, when it deployed an LLM planning assistant?**
Unified data and existing optimisation models — the LLM only added a conversational translation layer on top of ready foundations.
