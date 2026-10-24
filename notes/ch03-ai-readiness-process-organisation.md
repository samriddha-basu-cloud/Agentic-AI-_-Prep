# Ch 3 — AI Readiness II: Process & Organisational Foundations (Session 3)
**Session 3 📘:** "Process standardisation, incentives, politics, people — and a phased roadmap that survives contact with a real organisation." Opening case: **Continental Parts — the Roadmap Rebellion** (Plants 1–2 ignored the forecasting tool and avoided stockouts; Plants 3–4 obeyed, cut inventory and stocked out; the model missed 15% of demand that arrives by phone; a 25%-in-six-months target was set for a board deck).

> **Exam use:** the **pilot-selection matrix**, **phased roadmap with gates**, **frozen baselines**, **guarded metrics** and the **three decision levels** come from here — they are the skeleton of every Section B answer (Trishul B1 "Phase 1 → Phase 2 gate", Kaveri B1 "60-day review").

---

## 1. Organisations meeting AI — the theory
"Genuine transformation requires more than technology: it demands organisational will, cultural change, operational pragmatism, and cross-enterprise agreements — elements that technology alone cannot supply." (Tayur, core reading 📘)
- **No single objective function.** Optimisation assumes one goal; real firms are "a Byzantine maze" of departments with competing incentives and limited visibility.
- **Managers are political actors**, not autonomous agents; different buyer types judge AI on different risk-reward criteria.
- **Capital allocation is political** — supply chain competes with marketing, R&D and finance; AI ranks low until a crisis.
- **Sabotage without villains** — turf wars over data ownership, budget control, bureaucratic inertia.
- **Heterogeneity warning** — manufacturers differ across industries *and* between business units (Caterpillar, Deere); distrust any one-size pitch.

## 2. The agency problem — "what is in it for me?" ⭐⭐
Supply **chains** span enterprises; the most valuable use cases need **other companies' data**. History: ignoring incentives doomed RFID and blockchain at scale (value to one party, costs to another; TradeLens shut down for lack of industry collaboration — S5). **The inverse bullwhip** (Altintas, Erhun & Tayur 2008): forecast improvements at the **customer** can rationally **increase** variability at the manufacturer under quantity discounts — "one firm's AI win is another's planning nightmare". **Design implication:** multi-enterprise AI needs **contract and incentive design** as much as data pipes — who pays, who gains, who carries the risk of acting on shared signals?

## 3. Three levels of decisions — and AI fit ⭐⭐⭐
| Level | Examples | Cadence & owner | Realistic AI role |
|---|---|---|---|
| **Strategic** | network design; NPI; portfolio & pricing; MTS/MTO/ATO; postponement | quarterly–annual; executives | **auxiliary insight only** — futures unlike the past defeat models trained on history |
| **Tactical** | S&OP/SIOP; seasonal capacity & logistics; production planning | weekly–monthly; planners | **useful assistant — augment** planners; plans crumble under disruption |
| **Operational** | dynamic procurement; lead-time quotation; inventory setting; fulfilment & shipment | daily–hourly; front line + systems | **strongest fit — delegate**; localised successes (routing, picking) but noisy environments demand robustness |
**Class Q 3.1:** (a) AI network redesign for the 5-year footprint → **strategic / input-only**; (b) AI-assisted S&OP scenarios → **tactical / augment**; (c) autonomous reorder of spares under ₹50,000 → **operational / delegate**. "Place the use case before choosing the AI."

## 4. The process-readiness agenda ⭐⭐
1. **Map reality, not the SOP** — process mining on event logs exposes the workarounds, loops and heroics; "you cannot hand an agent a process you cannot describe".
2. **Standardise where variation is waste** — harmonise O2C and P2P variants before automating; every surviving variant multiplies agent complexity.
3. **Redesign, then automate** — no lift-and-shift; self-learning AI **amplifies** existing limitations.
4. **Respect embedded expertise** — decades-old processes encode judgement; bulldozing tacit knowledge creates fragility — "codify the WHY, not just the flow".
5. **Decide what agents inherit** — for each step: **automate** (rules), **augment** (AI recommends, human decides) or **delegate** (agent acts within an envelope); revisit as trust builds.
**Map before you automate:** flowcharts and SOPs show where a decision actually happens; compare **before-AI and after-AI information flows** (which hand-offs the system removes, which it must preserve); run an **idea bank**; measure with a **balanced scorecard** (service, quality, learning — not only cost). **Class Q 3.6:** "add AI to procurement" → the first step is **map the process**. "Automating a broken process only makes the mess run faster."

## 5. Human–AI collaboration pitfalls (de Véricourt & Gurkan) 📘
**Complementary strengths** (humans frame, machines predict) · **different mistakes** (AI errs in new ways; net quality depends on catching each other's errors) · **the trust dilemma** (between blind trust and algorithm aversion lies **calibrated trust**; "how good is your machine? You may never know" in non-stationary settings) · **speed is not throughput** (bottlenecks move to human verification and exceptions) · **delegation effects** ("it's not me, it's the machine" — reassign accountability explicitly).

## 6. Algorithm aversion and its proven remedy ⭐⭐⭐
**Landmark finding (Dietvorst, Simmons & Massey 2015):** after seeing an algorithm and a human make the **same** errors, people lose confidence in the algorithm far faster and choose inferior human forecasts even when the algorithm outperforms. Error tolerance is **asymmetric** — machines are not forgiven; one visible failure can destroy adoption (Continental Parts).
**Proven remedy (2018):** give forecasters even **slight ability to modify** the output (e.g. ±10%) → dramatically higher use, satisfaction and belief in the algorithm, at trivial accuracy cost. **"Bounded override is not a concession; it is the adoption mechanism"** — what L2–L3 should feel like.
**Class Q 3.3:** Design A (show back-tested record, allow ±15% adjustment with reasons captured) vs Design B (mandate unmodified use) → **A wins — bounded control keeps trust**; B breeds shadow spreadsheets. "Trust is designed, not demanded."

## 7. The oversight paradox — "ironies of automation" ⭐⭐
**Bainbridge (1983):** the better the automation, the less practice humans get — yet the more critical their intervention when it fails. **2026 confirmation:** ~1,500 workers — intensive AI oversight is the most taxing work: **+14% mental effort, +12% fatigue, +19% information overload**. Triple failure mode: **automation bias**, **complacency** (vigilance decay), **skill atrophy**. Design consequence: "a human will check it" is a **constraint to engineer around**, not a safety net — budget skill-maintenance rotations, simulation drills, realistic exception rates; and **hard guardrails outside the model** matter more. **Class Q 3.4:** each planner supervising 12 agent workstreams "checking anything odd" → **fails — vigilance and skills decay**.

## 8. Organisations in the field 📘
**Klarna (2024–25) — fire, then rehire ⭐⭐:** Feb 2024, its AI assistant did the work of **~700** agents (2.3M conversations in month one; resolution 11 → under 2 minutes). Within ~18 months the CEO reversed: "We focused too much on efficiency and cost. The result was lower quality." Rehired into a **hybrid** model (AI for routine volume; guaranteed human access). Theory predicted it: service quality lives at the judgement edges; efficiency metrics invited the outcome they measured; full replacement removed the human capacity needed for exceptions.
**Four retreats:** **Walmart shelf-scanning robots (ended 2020)** — a simpler, cheaper lever (pickers capture the data as a by-product) won · **Adidas Speedfactory (2016–20)** — showcased a trend, not the chain's binding constraint; upgraded Asian suppliers won · **GE Predix (2015–18)** — top-down "platform for everything industrial"; heterogeneity and overreach; dose not survivable · **IBM Watson Health (sold 2022)** — moonshot claims met data and process reality.

## 9. Incentives — the metric misalignment nobody fixes ⭐⭐⭐
- **Front line** judged on OTD, cost, turns — not AI adoption → rationally ignores a tool with a learning curve.
- **Middle management** owns the system AI might replace; champions have "currency in being the smartest person in the room".
- **Executives** expect silver bullets; disappointment triggers abandonment just before the learning curve pays.
- **The fix:** change what success MEANS — adoption and data-quality KPIs in scorecards, recognition for exception-handling skill, protected retraining time.
- **Class Q 3.2:** planners paid on service and turns, now also measured on "recommendation adherence" → **they make adherence fit their metrics** (game it). "When a measure becomes a target, it stops measuring" (Goodhart). Fix: align metrics **before** the tool — exception-handling quality and **forecast value added** in the scorecard.
- **Gartner 2026:** 55% of SC leaders expect agentic AI to reduce entry-level hiring; **86%** say adoption requires new talent-pipeline processes — "if juniors no longer learn by doing routine work, where do future experts come from?"

## 10. Workforce transformation 📘
Role shift from swivel-chair data entry → **automation, exception handling, escalation and improvement**. New skill stack: SCM discipline + financial acumen + communication + citizen-data-scientist literacy (understand models, interpret outputs, **spot hallucinations**). Traits: **adaptability and curiosity**. New roles: **AI steward**, agent supervisors, data-product owners, AI governance leads. **Complacency risk:** letting AI "firefight faster than any human" erodes critical thinking.

## 11. Three non-negotiables ⭐⭐
1. **Senior executive sponsorship + multi-functional resources** (named executives with skin in the game; resources from every affected function — Caterpillar, Deere, processed-food makers).
2. **Enforced data management and process adherence** — including data management *of* the data management.
3. **Phased rollout with active stakeholder participation** inside and outside the enterprise.
Why phased? MIT's successful 5% **embrace friction** as the crucible of adaptation; phasing meets friction in survivable doses.

## 12. Phased AI adoption: Crawl, Walk, Run — with gates ⭐⭐⭐
| Phase | Time | What happens |
|---|---|---|
| **0 Foundation** | 0–6 mo | data & process fixes on ONE value stream; governance stood up; **baseline metrics frozen**; talent assessment; quick BI wins |
| **1 Pilot** | 3–9 mo | 1–2 use cases: **HIGH feasibility × HIGH value × LOW blast radius**; predictive/augmenting first; human-in-the-loop; success gate vs **frozen baseline** |
| **2 Scale** | 9–24 mo | winning pilots → adjacent categories, sites, regions; industrialise (MLOps, retraining, adoption KPIs, reskilling) |
| **3 Transform** | 18 mo+ | redesign the operating model; autonomy envelopes widen; org restructures around exceptions |
**Each gate:** value evidence + readiness re-score + **explicit autonomy decision**. "Skipping gates is how you join the predicted 40% of cancelled agentic projects." **Class Q 3.5:** "25% inventory reduction in 6 months, company-wide", set before any diagnostic → rewrite as **scoped, baselined and evidence-gated** — a board-theatre target cannot govern (moving baseline; single unguarded metric invites gaming — cut inventory, buy stockouts). "Transform in survivable doses."

### How to write a gate (exam template)
| Gate element | What to write |
|---|---|
| Scope | which category/site/lane, how long (long enough for the statistics) |
| **Frozen baseline** | the KPIs at a fixed date before go-live — and ideally a **control group** |
| Success metric(s) + threshold | e.g. savings ≥ 2.5% (above 1.9% break-even); fill ≥ 75% |
| **Guarded counter-metric** | the metric that must not get worse (OTIF, stockouts, cost per unit) |
| Autonomy decision | stay / climb / step down a rung on the ladder |
| Who decides | named business owner (+ finance certifies value) |
| Demote / scrap evidence | the result that changes your mind |

## 13. Pilot selection — scoring candidate use cases ⭐⭐⭐
| Criterion | Ask | Green flag | Red flag |
|---|---|---|---|
| **Value at stake** | which cost/revenue pool, how big? | material pool, measurable baseline | vanity metric, no baseline |
| **Data feasibility** | S2 scorecard on THIS use case | clean, owned, streaming where needed | masters dirty, data political |
| **Decision impact** | does output change real decisions? | clear action mapping | rain-forecast redundancy |
| **Blast radius** | worst case if wrong? | reversible, bounded, low-value txns | irreversible, customer-facing |
| **Sponsor & adoption** | who owns it, who must use it? | named sponsor, users co-design | orphaned, imposed |
| **Learning value** | what capability does it build? | reusable data products, skills | dead-end point solution |
*Worked:* Trishul ranks P2 (₹58 cr pool, ₹1.9 L median deals, mandate-bounded) above P3 (high blast radius, regulated) above P1 (fails the pool test, 26-hour data). See [Trishul B1](pyq-trishul.md).

## 14. Scoping and finding the work to automate 📘
**Design thinking** (persona; user stories "As a <role> I want <feature> so that <benefit>") · **Systems thinking** (boundaries, subsystems aligned to the whole) · **Scenario planning** (STEEP drivers → ~7 scenarios → four in a 2×2) · **Delphi** (anonymous multi-round expert convergence) · **Balanced Scorecard** (Financial, Customer, Internal Process, Learning & Growth). **Idea bank** (cross-department capture and ranking; 20%-time produced Gmail and Maps); **Who/What/How/Why** process interviews, timed to expose bottlenecks; **before/after information-flow** diagrams; **five-stakeholder scoring** (customers, vendors, employees, investors, governments) — low customer-value, high-effort steps are targets; rank by **impact × effort** (time, capital — > 20% of profit = large — risk, how many asked). Never delete a low-priority idea.

## Key takeaways (S3 recap 📘)
1. AI value is gated by organisation, not algorithms — silos, politics and incentives defeat perfect models.
2. Three-level framework: strategic = judgement with AI auxiliary; tactical = augmented planners; operational = automation frontier.
3. Standardise processes before automating — but codify tacit expertise; self-learning AI amplifies what it inherits.
4. Calibrate trust; design confidence displays, overrides and accountability explicitly.
5. Roadmaps are risk instruments: gates with frozen baselines, pilot selection by feasibility × value × blast radius, and the three non-negotiables.

---

## Self-test
**Q1. Continental Parts: Plants 1–2 ignored the tool and avoided stockouts; Plants 3–4 obeyed, cut inventory and stocked out. What do you conclude?**
The planners held information the model lacked (15% of demand arrives by phone — a completeness gap) and a single unguarded metric (inventory) was optimised at service's expense. Don't mandate compliance (algorithm aversion → shadow spreadsheets); fix the data gap, add bounded override with reason capture, and guard inventory targets with a service counter-metric.

**Q2. Rewrite "25% inventory reduction in 6 months, company-wide" as a gate-compatible target.**
Scope: one category at two plants; frozen baseline: last 6 months' inventory and fill by SKU; success: inventory −10% at fill ≥ baseline; counter-metric: stockout days not up; review at month 6 by the COO with finance; widen only on evidence.

**Q3. Why does "each planner will supervise 12 agent workstreams" fail?**
The ironies of automation: oversight is the most taxing work, vigilance decays, skills atrophy; humans become poor monitors. Bound spans, rotate, drill, and put hard limits outside the model.

**Q4. Where does each decision sit, and what AI posture: (a) choose a new RDC location; (b) monthly S&OP capacity plan; (c) daily reorder of packaging under ₹50,000?**
(a) strategic — AI as input only; (b) tactical — augment planners; (c) operational — delegate inside an envelope.

**Q5. Klarna replaced 700 agents with AI and then rehired humans. Which course ideas explain it?**
Efficiency metrics invited the outcome they measured; quality lives at the judgement edges (tacit layer); removing humans removed the capacity for exceptions — the oversight paradox. The fix is a hybrid with guaranteed human access.
