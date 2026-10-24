# Exam Playbook — how to answer the case-based end-sem
Your faculty's note 📘: *"Go through all the frameworks covered during the sessions and refer to the attached question papers. The examination will focus on **case-based applications** and **direct numerical problems**. There will be **no standalone theory questions**, and the numericals will involve **straightforward calculations without requiring any additional formulas**. **Basic concepts of SCM** will also be required. … a comprehensive, application-based case study covering all concepts taught throughout the course, including the integration of AI and SCM … projects, class tests, case studies and the **Chain Reaction simulation** … Revise the case studies and frameworks, with particular emphasis on the **strategies, decisions and management approaches used in the Chain Reaction simulation**."*

So the paper will look like the two past papers ([Trishul](pyq-trishul.md), [Kaveri Motors](pyq-kaveri.md)): a 1½–2 page case with 3–4 exhibits (some deliberately irrelevant or defective), **Section A — diagnostics** (calculations, data triage, exposing a claim) and **Section B — a recommendation/mandate** (rank, choose, design a gate). This page is the method.

---

## 1. The two non-negotiable rules (they are printed on the paper)
### Rule 1 — The Assumptions line ⭐⭐⭐
Any answer that makes a **recommendation, ranking, ruling, verdict or go/no-go call** must **open** with:

> *Assumptions: A1. … A2. … A3. …*

- **Unstated assumption your answer depends on = marks lost. Stated assumption = marks earned.** 📘
- Write **3–6** assumptions, numbered, each one sentence, each one something your answer **actually depends on**. Not filler ("the data is correct") — useful ones ("cycle stock is set by full-truck multiples, so forecasting does not change Q").
- Good assumption types (pick what your calculation or choice leans on):

| Type | Example |
|---|---|
| **Scope / base** | "Base = cycle + safety stock (₹13.6 cr); in-transit excluded because lead time, not forecast, drives it." |
| **Mechanism** | "A better forecast reduces only safety stock; order quantity stays at full-truck multiples." |
| **Mix / allocation** | "Lost-sales mix = month-5 sales mix (219/96/59)." |
| **Cost definition** | "Contribution = price − unit production cost; overheads are fixed and excluded." |
| **Evidence quality** | "Vendor reference results (another firm, another context) are a ceiling, not a forecast." |
| **Readiness / timing** | "Vendor-master dedup can be done in Phase 0 (6–8 weeks) by a named owner." |
| **Regulatory** | "EU AI Act high-risk duties already apply (enforceable Aug 2026)." |
| **Units** | "₹1 crore = 100 lakh; figures are annual averages at cost." |

### Rule 2 — Show units and arithmetic ⭐⭐⭐
"**One clean calculation beats three vague ones.**" 📘 Write the calculation as a small table or a line: *what → arithmetic → result with units*. Then **state what the number means for the decision**. Examiners reward: the right **base**, the right **pool**, the **ratio to the claim**, and a **verdict**.

---

## 2. The universal answer skeleton
Use this for every Section B question and any Section A question that asks for a verdict.

1. **Assumptions:** A1 … A2 … A3 … (numbered, decision-relevant).
2. **The number(s):** one clean calculation with units (pool size, ceiling, break-even, contribution forgone, cost-per-decision…).
3. **The verdict / choice / ranking** in one sentence.
4. **The confrontation:** one line on the strongest evidence *against* your choice, and why it does not change it (Kaveri B1 asks for this explicitly).
5. **The design** (if asked): mandate or gate — objective metric, constraint, escalation trigger, autonomy level (L1–L5) with a one-line justification, named owner.
6. **The test:** frozen baseline → success metric(s) with thresholds → guarded counter-metric → the evidence that would make you **demote / scrap / change your mind**.

> Memory hook: **"A-N-V-C-D-T"** — Assumptions, Number, Verdict, Confront, Design, Test.

---

## 3. Data triage — the four defect patterns (and how to expose them)
Both papers deliberately plant noise and defects 📘. Treat every exhibit item as one of: **load-bearing**, **irrelevant**, **unreliable (stale/vendor/anecdote)**, or **defective (doesn't add up / contradicted)**.

| Defect pattern (Kaveri paper's own list 📘) | What it looks like | How to expose it (show, don't assert) |
|---|---|---|
| **Cherry-picks its month** | "Month 4 proved we self-correct (+₹3.6 cr)" | Show *why* that month was different (production cut from ₹26.4 to ₹16.8 cr forced by chip allocation) and what the next month did (−₹1.9 cr). |
| **Hides a trend inside an average** | "Season fill averages 73.7%" | List the series (86.0 → 85.9 → 73.8 → 64.5 → 58.2), give the current value and the volume-weighted figure (72.5%). |
| **Reports activity as outcome** | "Foundations L4, six capabilities built or building" | Count what is *working*: 1 of 3 live agents hits its objective; routing agent net −₹2.6 L; key agent NOT BUILT. |
| **Argues insurance logic backwards** | "No rail — road has always sufficed; book-ahead charge is money on capacity we may never use" | Insurance is valued against the bad state: road failed in M5 (₹60 L, 0% cover); rail is ~25% cheaper and the M2 alert flagged 0 slots on 12 lanes. |
| **Doesn't add up** (Trishul) | "Total ₹15.2 cr = 11.0 + 2.6 + 1.2" | 11.0 + 2.6 + 1.2 = 14.8 ≠ 15.2 → ₹0.4 cr unexplained. |
| **Stale and contradicted** (Trishul) | "Duplicates resolved to under 2%" (report 14 months old) | 2,890 − 2,410 = 480 surplus records → 480 ÷ 2,890 = 16.6% (≈18%). |
| **Vanity / irrelevant** | App downloads, website bounce rate, GST compliance, CSR, lease, canteen, solar, HR survey | One line each: "not linked to the cost pool / decision under review". |
| **Evidence laundering** | "European reference customer", "well-known retail deployments", market-size stats | Another firm's data ≠ mechanism proof here; treat as a ceiling (S1: "judge mechanism and benchmark, not momentum" 📘). |

**Part (c) style questions** ("what does the corrected figure do to your verdict?") — answer honestly in one line, including **"it does not change it"** when that is the truth.

**"Which item is load-bearing and must be verified first?"** — pick the item that (1) the next decision rests on, (2) commits money or capacity irreversibly / ahead of time, and (3) is unverified. In Kaveri that is the month-6 materials order + no-rail claim.

---

## 4. Framework picker — "if the question says X, use Y"
| If the case asks you to… | Use this course framework | Where |
|---|---|---|
| Test a vendor's % claim (inventory, stockouts, savings) | **Four-Question AI Claim Audit** (mechanism, cost pool, decision changed, evidence) + **Q vs S pool sizing** | [Frameworks §1](course-frameworks.md), [S1](ch01-ai-in-operations-and-scm.md) |
| Say whether a firm is ready | **Five-pillar Data & Tech Readiness Scorecard** (quality, masters, architecture, security, compute) + **six data-quality dimensions** + **predictive vs agentic requirements delta** | [S2](ch02-ai-readiness-data-technology.md) |
| Choose / rank pilots | **Pilot-selection matrix** (value, data feasibility, decision impact, blast radius, sponsor, learning) | [S3](ch03-ai-readiness-process-organisation.md) |
| Place a decision and set AI posture | **Three decision levels** (strategic = input only; tactical = augment; operational = delegate) | S3 |
| Plan the roll-out | **Phased roadmap with gates** (Phase 0 foundation → 1 pilot → 2 scale → 3 transform; frozen baseline; readiness re-score; explicit autonomy decision) | S3 |
| Decide how much autonomy | **Five-level autonomy ladder** (L1 assist → L5 self-improving) + **Agentic Suitability Screen** (frequency, reversibility, data/feedback, rule clarity, stakes; 20+ = L3–L4) | [S4](ch04-agentic-ai-systems.md) |
| Design controls | **Governance stack** (hard constraints outside the model, identity & least privilege, observability, escalation & kill switch, named owner) | S4 |
| Pick a platform / build vs buy | **Six filters in order** (use-case fit, data gravity, governance fit, ecosystem & skills, TCO & pricing risk, lock-in) + "own the differentiating loop, rent the rest" | [S5](ch05-ai-platforms.md) |
| Supervise an ML model / accuracy claim | **ML Framing Canvas** (decision, target, features, benchmark, loss) + naive benchmark + leakage test | [S6](ch06-machine-learning-for-operations.md) |
| Get a notebook to production | **Seven-step workflow** + **capability checklist** (reproducible, monitored, owner, fallback, on-call) | S7 |
| Buy external data / demand signals | **Five-step Signal Audit** (lead time, mechanism, decision test, cost vs value, weight check) | [S8/S11](ch07-demand-forecasting.md) |
| Choose a forecasting tool tier | **Tier matching / Bake-off ladder** (count it, audit readiness, name the skill, check governance, bake it off) | S9/S12 |
| Evaluate a learned inventory policy (DRL "20% better") | **Guardrailed Pilot — six elements** (scope, bounds, fallback, evaluation, trust loop, ownership) + theory ceiling (myopic within ~5%) | [S10](ch08-inventory-optimisation.md) |
| Fund sensors / a digital twin | **Twin-Now / Twin-Later Test** (decision-changing, failure cost, data readiness, fidelity, verdict) | [S13](ch09-predictive-maintenance-digital-twins.md) |
| Hand logistics/flows to an agent | **Mandate Card** (service floor, cost ceiling, mode priority, shock trigger, review cadence) | [S14](ch10-logistics-routing-optimisation.md) |
| Hand a network to a solver | **Optimizer Mandate Checklist** (service targets per zone, cost weights, review rule L2/L3/L4, re-solve trigger, verify fit) | S15 |
| Spec contract/RFx NLP | **Clause-Stakes Specification Checklist** (list clauses, name decision, set bar per clause, pick tier, name the exception) | [S16](ch11-nlp-procurement-token-economics.md) |
| Agent cost has jumped | **Tune-or-Retire Checklist** (cost per decision, value per decision, ratio, tune first, retire if still failing) | S17 |
| Use GenAI scenarios | **Scenario Portfolio Checklist** (generate wide, label plausible/stretch/implausible, select two, specify survival, guard the label) | [S18](ch12-genai-design-multi-agent.md) |
| Multiple agents interacting / bullwhip | **Shared demand signal, order smoothing/rate limits, trained coordination**; **ACAP self-check** | S19 |
| Bias / incident / who is accountable | **ACAP governance checklist** (accountability, capability limits, auditability, proportionality, post-incident learning) + EU AI Act deployer duties | [S20](ch13-responsible-ai-ethics.md) |

---

## 5. Writing a mandate (the Section B centre-piece)
Every mandate answer has the same seven slots. Learn them as a card:

| Slot | What to write | Good example |
|---|---|---|
| **Objective metric (ONE)** | The single number the agent/initiative is accountable for | "Volume-weighted fill % across all zones" / "invoice-verified net savings %" |
| **Constraint (may not breach)** | A hard limit enforced outside the model | "Month-end cash ≥ −₹15 cr"; "no deal > ₹5 L/yr without approval"; "approved suppliers only" |
| **Escalation trigger** | The event that returns control to humans | "Lane capacity loss > 20%", "zone fill forecast < 60%", "confidence below threshold", "anomaly in order size > 3σ" |
| **Starting autonomy** | L1–L5 with one-line justification | "L3: routine cases end-to-end, exceptions approved — gate met but no track record" |
| **Named owner** | A person/role, not "the team" | "CSCO accountable; Head of Distribution Planning operates" |
| **Frozen baseline** | Values frozen before go-live (ideally with a control group) | "M5: fill 58.2%, lost 269, auto-push 276, rail 0, cash −₹13.3 cr" |
| **Success metric + threshold, guarded counter-metric, kill/demote evidence** | One or two success thresholds; one metric that must NOT get worse; the result that changes your mind | "Fill ≥ 75% in M7; cost/car ≤ M5 +10%; scrap if placed-but-unsold" |

**Choosing the starting autonomy level — a quick rule:**
| Situation | Start at |
|---|---|
| Regulated decision (EU AI Act high-risk, human oversight required), strategic, irreversible | **L1–L2** (recommend; human decides) |
| Routine, reversible, bounded, but no track record / readiness just fixed | **L3** (act with approval gates/thresholds) |
| High-frequency, low-value, reversible, clear mandate, proven in pilot | **L4** (bounded autonomy, monitor and audit) |
| Self-improving, coordinating peers | **L5** — "mostly aspirational, 2026" 📘; never as a starting point (and never below gate — see Kaveri's repricing agent) |

---

## 6. Numericals — the patterns that keep appearing
(All worked in full in [Numericals](numericals.md).)
1. **Reachable-pool test:** claim × base vs the pool the tool can actually touch (S ÷ (Q/2 + S)).
2. **Carrying-cost value:** inventory reduction × carrying rate vs annual fee.
3. **Value pool & break-even rate:** addressable spend = total × un-addressed share; break-even = annual cost ÷ pool.
4. **Contribution forgone:** lost units × mix × (price − unit cost).
5. **Simple vs weighted averages** (fill, accuracy) — expose trends hidden in averages.
6. **Exhibit reconciliation:** do components add to the total? Does the roll-forward (cash, stock) reconcile?
7. **Cost per decision vs value per decision** (token economics).
8. **Fill rate / service level, safety stock, EOQ, reorder point, inventory turns, days of supply** (basic SCM).
9. **Scoring frameworks:** suitability screen totals (20+ / 12–19 / <12), readiness profiles ([2,1,3,2,5] → predictive pilot on the cleanest domain).

---

## 7. Time plan for a 10-mark case (≈ 60 minutes)
| Minutes | Do |
|---|---|
| 0–8 | Read questions first, then the case. Mark every exhibit item L (load-bearing), I (irrelevant), U (unreliable), D (defective). |
| 8–15 | Do the arithmetic on scrap: totals, averages, pools, ratios. Check that every total adds up. |
| 15–35 | Section A answers — each with its calculation table and one-line verdict. |
| 35–55 | Section B — assumptions, choice, confrontation, mandate table, gate table, demotion sentence. |
| 55–60 | Check every verdict has an Assumptions line and every number has units. |

---

## 8. Phrases that earn marks (course vocabulary)
- "Follow the cost pool, not the technology." · "Forecasting attacks S, not Q." · "Precision pays only when a decision changes."
- "Foundations before intelligence; semantic before agentic." · "Data defects compound at machine speed." · "Autonomy raises every bar."
- "Guardrails live outside the model." · "The mandate is the management." · "Autonomy is granted per decision and earned by evidence."
- "Stability is mechanism design, not intelligence." · "Coordination beats speed."
- "No model without a naive benchmark." · "Frame the decision before the model." · "A model in a notebook is not a capability."
- "Optimize the policy, not the forecast." · "Learned policies wear proven guardrails."
- "A perfectly solved LP with the wrong mandate produces a perfectly wrong plan."
- "Tune before you retire." · "Label before you act." · "Sequence beats speed; building is not operating." (Chain Reaction debrief 📘)
- "Guardrails only count as guardrails if you use them when it costs you something."

## 9. Ten mistakes that cost marks
1. No assumptions line on a verdict. 2. Numbers without units. 3. Using a total that doesn't add up. 4. Trusting a stale or vendor figure. 5. Treating revenue loss as profit loss. 6. Recommending L4/L5 for a regulated or irreversible decision. 7. "A human will check it" as the only control (the oversight paradox 📘). 8. Prompt instructions offered as controls. 9. A success metric with no counter-metric (gaming: cut inventory, buy stockouts). 10. No demotion/scrap evidence — a gate that cannot fail is not a gate.
