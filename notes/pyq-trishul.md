# Past Paper 1 — Trishul Consumer Products (questions + model answers)
This is the **class-test / past-paper case** from your uploads 📘, typed out in full, followed by **fully worked model answers** in the mandatory format. Read the question block first, try it yourself for 25 minutes, then compare. Every answer opens with a numbered **Assumptions line**, shows **units and arithmetic**, and names the course framework it uses.

> **How the marks work (from the paper's own instructions 📘):** "Any answer that makes a recommendation, ranking, verdict, or go/no-go call must open with a numbered assumptions line in the form *Assumptions: A1. … A2. … A3. …* An unstated assumption that your answer depends on **costs** marks; a stated one **earns** them." And: "Show units and arithmetic. **One clean calculation beats three vague ones.**"

---

## The question paper (verbatim)

### Instructions to candidates
- **Assumptions line (mandatory).** Any answer that makes a recommendation, ranking, verdict, or go/no-go call must open with a numbered assumptions line in the form: *Assumptions: A1. … A2. … A3. …* An unstated assumption that your answer depends on costs marks; a stated one earns them.
- **Show units and arithmetic.** One clean calculation beats three vague ones.

### The Case: Trishul Consumer Products
Trishul Consumer Products manufactures personal-care goods at three plants (Baddi, Vapi, Mysuru), selling through 1,900 distributors across India and, increasingly, to EU retailers (12% of revenue, growing ~30% annually). An internal readiness assessment scored the firm **[Data quality 2, Master data 2, Architecture 3, Security 3, Compute 4]**. The board has approved an "AI acceleration" budget of **₹6 crore per year**. Three proposals compete for it — the exhibits below contain the data the steering committee assembled. As in real steering packs, NOT everything in the exhibits matters.

- **Proposal 1 — ML demand forecasting platform** — ₹1.6 crore/yr subscription + ₹0.9 crore integration. Vendor claim: "30% inventory reduction and 50% fewer stockouts," citing a European reference customer.
- **Proposal 2 — Autonomous procurement agent for indirect/MRO tail spend** — ₹1.1 crore/yr. Negotiates with small suppliers inside category-manager mandates. Vendor cites well-known retail deployments.
- **Proposal 3 — Supplier-risk scoring model** — ₹0.8 crore/yr. Scores would automatically influence contract renewals, including for the EU-serving plants. The CEO wants at least one proposal live in six months and has asked what "the agent decides" would mean, legally and managerially, for each.

### Exhibit 1 — Operations & finance extract (annual, consolidated)
| Item | Value |
|---|---|
| Revenue | ₹1,240 crore |
| Marketing & brand spend | ₹86 crore |
| Average cycle stock (Q/2) | ₹11.0 crore |
| Average safety stock (S) | ₹2.6 crore |
| Inventory carrying rate | 19% |
| Estimated stockout revenue loss | ₹7.8 crore/yr |
| Order quantities | full-truck multiples (freight economics) |
| Replenishment frequency | weekly to all 4 regional DCs |
| Direct materials spend | ₹410 crore (78 suppliers) |
| Indirect/MRO tail spend | ₹64 crore (2,410 suppliers) |
| Tail spend currently negotiated | ~9% of tail suppliers |
| Corporate office lease | ₹4.2 crore/yr |
| New product launches last year | 14 |
| CSR programme budget | ₹3.1 crore |
| Distributor count | 1,900 |
| Average distributor payment terms | 21 days |

### Exhibit 2 — Systems & data landscape
- ERP: single instance, 11 years old; **61% of planning decisions executed in spreadsheets** alongside it
- **Vendor master: 2,890 records for ~2,410 real suppliers (~18% duplicates); no named owner**
- Item master: attribute conflicts on 11% of SKUs between ERP and the distributor portal
- Distributor portal: legacy; sales data arrives via **overnight batch (up to 26h latency); covers 71% of revenue**
- E-commerce & modern trade feeds: API-based, near-real-time; 29% of revenue
- Cloud & compute: modern tenant, data-science team of 6, GPU credits unused
- **API inventory: last audited 14 months ago; two vendor-facing credentials rotated after a phishing attempt**
- Employee engagement survey: 74% favourable (up 3 points); IT helpdesk CSAT 4.1/5
- Website relaunch: completed last quarter, ₹1.8 crore, bounce rate down 22%

### Exhibit 3 — Supplier & EU exposure extract
- Tail-spend supplier profile: **median annual spend ₹1.9 lakh; 84% single-quoted at renewal; median payment terms 30 days**
- Direct-material supplier concentration: top 10 = 62% of direct spend; dual-sourced on 7 of 10
- EU retailer contracts: 3 chains, renewal decisions quarterly; supplier-risk scores would feed these from Q3
- **EU regulatory note (legal memo): high-risk AI obligations enforceable Aug 2026; duty split between provider and deployer; human oversight of scored decisions required**
- Fleet & logistics: own fleet age 6.2 years; diesel price hedge expires in Q4
- Plant canteen contract: renewed for 3 years, ₹0.6 crore/yr
- Warehouse solar installation: 2.1 MW, commissioned last year, 31% of DC power

### Exhibit 4 — Supplementary extract (circulated by the steering committee two days before the meeting)
- **Working-capital note (finance): total average inventory ₹15.2 crore, comprising cycle stock ₹11.0 crore, safety stock ₹2.6 crore and in-transit stock ₹1.2 crore**
- **Vendor-master health (IT status report, dated 14 months ago): "duplicate supplier records resolved to under 2%"**
- Distributor mobile app: 41,000 downloads; average rating 4.3 stars
- GST e-invoicing compliance: 99.2% of invoices cleared without error last quarter
- Plant workforce attrition: 7.9%, against an industry benchmark of 11%

### Section A — Case Diagnostics (5 marks: A2 carries 2 marks, all others 1 mark)
**A1.** Proposal 1 claims a 30% inventory reduction. Using the exhibits, show the ONE calculation that best tests the claim, state your verdict, and open with a numbered assumptions line (at least two assumptions your calculation depends on). Be explicit about which supplied inventory figure you used as your base, and why.

**A2. (2 marks) Data triage and reliability.** Which supplied data items are irrelevant or unreliable for the three proposal decisions? Across Exhibits 1–4: (a) name at least THREE such items, with one line each on why; (b) at least one supplied figure is defective — identify it and show the arithmetic or the contradiction that exposes it; (c) state in one line what the corrected figure does (or does not do) to your A1 verdict.

**A3.** Using Exhibits 1 and 3, size the value pool Proposal 2 attacks (show the calculation), state the break-even savings rate the agent must achieve, and name the single readiness fix (Exhibit 2) that must precede it — with the concrete failure if skipped.

**A4.** Using Exhibit 3, state the regulatory consequence for Proposal 3 and ONE design obligation it imposes on Trishul (not the vendor).

### Section B — Design & Recommendation Task (5 marks)
**B1.** Rank the three proposals for the six-month deadline using pilot-selection logic (value, feasibility, blast radius). Your answer must contain, in order:
- a numbered assumptions line (*Assumptions: A1. … A2. … A3. …*) — the assumptions your ranking depends on;
- the ranking with one line of justification for your #1;
- the Phase 1 → Phase 2 gate for your #1: frozen baseline, two success metrics with thresholds, one guarded counter-metric, the starting autonomy level for any agentic component, and who decides;
- one sentence on what evidence at the gate would make you DEMOTE your #1 — i.e., the result that would change your mind.

---

## What the paper is really testing (read this before the answers)
| Question | Course tool it tests | Session |
|---|---|---|
| A1 | **Forecasting attacks S, not Q** — size the reachable pool first (Class Q 1.2 is almost the same question) | S1 📘 |
| A2 | **Data triage** — six data-quality dimensions; uniqueness (duplicates); stale reports; vanity metrics; "steering packs contain noise" | S2 📘 |
| A3 | **Value pool & break-even**; Walmart–Pactum tail-spend evidence; **master data before agents**; API security before write-access agents | S1, S2, S4 📘 |
| A4 | **EU AI Act provider/deployer duty split**; human oversight cannot be delegated to the vendor (Class Q 5.5) | S2, S5, S20 📘 |
| B1 | **Pilot-selection matrix** (value × feasibility × blast radius), **phased roadmap gate** (frozen baseline, guarded metrics), **autonomy ladder L1–L5**, named owner | S3, S4, S10 📘 |

> **The trap list for this paper:** (1) taking the vendor's 30% at face value; (2) using the ₹15.2 cr total without checking it adds up; (3) believing the 14-month-old "under 2% duplicates" report over the live 2,890-vs-2,410 count; (4) letting Proposal 3 "decide" renewals automatically when the law requires human oversight; (5) ranking Proposal 1 first because forecasting "sounds strategic".

---

## A1 — Model answer (1 mark)

**Assumptions:** A1. A forecasting platform reduces only **safety stock (S)**; **cycle stock (Q/2)** is set by full-truck order multiples and the weekly replenishment cadence, which Proposal 1 does not change. A2. The vendor's "30%" is measured on **on-hand inventory (cycle + safety)**, the stock an ordering policy controls. A3. In-transit stock (₹1.2 cr) is driven by lead time and transport, not forecast accuracy, so it is excluded from the base. A4. All figures are annual averages valued at cost, so they can be added. A5. The carrying rate of 19% applies to all inventory.

**Base used and why:** ₹13.6 crore = cycle ₹11.0 cr + safety ₹2.6 cr (Exhibit 1). I do **not** use Exhibit 4's ₹15.2 cr because (i) it includes in-transit stock that forecasting cannot touch and (ii) it does not even add up (11.0 + 2.6 + 1.2 = 14.8, not 15.2 — see A2).

**The one calculation (the reachable pool):**

| Step | Arithmetic | Result |
|---|---|---|
| Inventory reduction claimed | 30% × ₹13.6 cr | **₹4.08 cr** |
| Maximum a perfect forecast can remove (all of S) | ₹2.6 cr | **₹2.6 cr** |
| Ceiling as a share of the base | 2.6 ÷ 13.6 | **19.1%** |
| Gap | 4.08 − 2.6 | ₹1.48 cr that cannot exist |

**Verdict: the 30% claim fails on arithmetic before model quality is even discussed.** Even a perfect forecast (zero error → zero safety stock, which is impossible) caps the reduction at **19.1%**. Realistically, a better forecast trims part of S — say a 20–30% cut in forecast error → roughly ₹0.5–0.8 cr, i.e. **about 4–6%** of on-hand inventory. In money: the whole safety-stock pool is worth only 2.6 × 19% = **₹0.49 cr/yr** in carrying cost, against a **₹1.6 cr/yr** subscription (plus ₹0.9 cr integration). The inventory leg of the business case cannot pay for the tool; if Trishul wants a big inventory cut, the lever is **Q** — smaller, more frequent orders and shorter lead times (the **Campbell Soup lesson** 📘), not forecast precision. The "50% fewer stockouts" leg (worth at most a share of the ₹7.8 cr revenue loss, i.e. only its margin) must be tested separately on Trishul's own data.

> **Why this is the "ONE calculation":** Session 1 Class Q 1.2 — *"₹8 crore cycle stock, ₹2 crore safety stock, vendor claims 30% cut. What single calculation kills or saves this claim? → Size the safety-stock share of total inventory."* 📘 The lesson: **follow the cost pool, not the technology.**

---

## A2 — Model answer (2 marks)

### (a) Irrelevant or unreliable items (name at least three)
| # | Item (exhibit) | Irrelevant or unreliable? | One-line reason |
|---|---|---|---|
| 1 | Marketing & brand spend ₹86 cr (Ex 1) | Irrelevant | None of the three proposals touches marketing; it is not part of any cost pool being attacked. |
| 2 | Corporate lease ₹4.2 cr, CSR ₹3.1 cr (Ex 1), canteen ₹0.6 cr, solar 2.1 MW (Ex 3) | Irrelevant | Fixed overheads and sustainability facts with no link to inventory, tail spend or supplier risk. |
| 3 | Website relaunch ₹1.8 cr, bounce rate −22% (Ex 2) | Irrelevant (vanity) | A marketing-site metric; says nothing about planning data, vendor data or API security. |
| 4 | Distributor app 41,000 downloads, 4.3 stars (Ex 4) | Irrelevant (vanity/activity) | Measures adoption and sentiment, not the 26-hour data latency that actually limits forecasting. |
| 5 | Employee engagement 74%, helpdesk CSAT 4.1, attrition 7.9% vs 11% (Ex 2, Ex 4) | Irrelevant | Healthy HR/IT-service signals, but none is a readiness pillar for these decisions. |
| 6 | GST e-invoicing 99.2% (Ex 4) | Irrelevant / misleading | Shows invoice *compliance*, not vendor-master *uniqueness*; easily misread as "our data is clean". |
| 7 | Fleet age 6.2 years, diesel hedge expiring Q4 (Ex 3) | Irrelevant | Logistics cost facts; no proposal is a fleet or fuel decision. |
| 8 | Vendor's "European reference customer" (P1) | Unreliable | Another firm's data, different readiness and context — evidence laundering, not mechanism proof. |
| 9 | IT status report "duplicates under 2%" (Ex 4) | Unreliable (stale and contradicted) | 14 months old; the live count in Exhibit 2 shows ~18%. |
| 10 | Total average inventory ₹15.2 cr (Ex 4) | Unreliable (defective) | Its own components do not add up — see (b). |

### (b) The defective figure(s) — show the arithmetic
**Defect 1 — the working-capital total does not add up.**
Cycle ₹11.0 cr + safety ₹2.6 cr + in-transit ₹1.2 cr = **₹14.8 cr**, but the note states **₹15.2 cr** → ₹0.4 cr (≈2.7%) is unexplained. Either a component is missing or the total is wrong; it cannot be used as stated.

**Defect 2 — the vendor-master "under 2% duplicates" claim is contradicted.**
Exhibit 2: 2,890 records for ~2,410 real suppliers → 2,890 − 2,410 = **480 surplus records**. 480 ÷ 2,890 = **16.6% of records are duplicates** (or 480 ÷ 2,410 = 19.9% over the true count) — about 18%, i.e. **8–10× the "under 2%" claimed**. The report is 14 months old, and the vendor master has **no named owner**, so nobody maintained it after the clean-up. (A data-quality *uniqueness* failure — Session 2's six dimensions 📘.)

### (c) Effect of the corrected figure on the A1 verdict (one line)
Using the corrected total ₹14.8 cr, safety stock is 2.6 ÷ 14.8 = **17.6%** of inventory (and 30% of 14.8 = ₹4.44 cr, still far above the ₹2.6 cr pool), so **the correction does not rescue the claim — it lowers the ceiling further and the verdict "30% is unreachable" stands.**

> Examiner tip: part (c) rewards saying **"does not change the verdict"** when that is true. Do not invent a change.

---

## A3 — Model answer (1 mark)

**Assumptions:** A1. Tail spend is spread roughly evenly across suppliers (mean ₹64 cr ÷ 2,410 = ₹2.66 lakh vs median ₹1.9 lakh — mildly right-skewed, so this is a fair first cut). A2. The ~9% already-negotiated suppliers are excluded from the pool (the agent's value is on suppliers nobody negotiates with). A3. The ₹1.1 cr/yr fee is the full annual cost of the agent (no separate integration fee is quoted). A4. Savings are measured as recurring annual price reductions on renewed spend.

**Value pool (Exhibits 1 and 3):**

| Step | Arithmetic | Result |
|---|---|---|
| Total tail spend | given | ₹64.0 cr across 2,410 suppliers |
| Share not negotiated today | 100% − 9% | 91% |
| Un-negotiated suppliers | 2,410 × 0.91 | ≈ 2,193 suppliers |
| **Addressable value pool** | ₹64 cr × 0.91 | **≈ ₹58.2 cr/yr** |
| Supporting signal | 84% single-quoted at renewal; median terms 30 days | Little competitive pressure today → negotiable |

**Break-even savings rate:**
₹1.1 cr ÷ ₹58.2 cr = **1.89% ≈ 1.9%** of addressable spend. (On the full ₹64 cr it would be 1.1 ÷ 64 = 1.72%.)
*Sensitivity:* if the agent closes only about 65% of negotiations (Walmart–Pactum's 64–68% close rate 📘), the effective pool is 58.2 × 0.65 = ₹37.8 cr and break-even rises to 1.1 ÷ 37.8 = **2.9%** — right at Pactum's ~3% average savings. So the case is **positive but thin**, and the pilot must measure realised savings, not quoted ones.
*Upside not in the break-even:* Pactum also extended payment terms by ~35 days 📘. On ₹58.2 cr, 35 extra days frees 58.2 × 35/365 = **₹5.6 cr of working capital** (worth ≈ ₹0.56 cr/yr at an assumed 10% cost of capital).

**The single readiness fix that must come first: de-duplicate the vendor master and give it a named owner (golden record per supplier).**
**Concrete failure if skipped:** 2,890 records for 2,410 suppliers means the agent negotiates with the **same supplier under several records** — it opens parallel negotiations, agrees **different prices and payment terms on duplicate records**, under-states Trishul's real volume with that supplier (so it negotiates from a weaker position), and **double-counts savings**. A human buyer mentally merges duplicates; **an agent transacts on them at machine speed** 📘 (Session 2: "data defects compound at machine speed"; Class Q 2.1).

> Also say in one line (it earns credit): **write-access to vendors must wait for an API inventory and per-agent credentials** — two vendor-facing credentials were just rotated after phishing and the API inventory is 14 months old (Class Q 2.3: "Block until API inventory and access controls exist" 📘). If the examiner's intended answer is "security", this line covers you; but the *single* fix the vendor-master data most directly blocks is dedup, because the agent's counterparties *are* vendor-master records.

---

## A4 — Model answer (1 mark)

**Regulatory consequence:** Because Proposal 3's scores would **automatically influence contract renewals for EU-serving plants and the 3 EU retail chains from Q3**, the legal memo puts it under the **EU AI Act high-risk obligations, which became enforceable in August 2026 — i.e. they already apply** 📘. Duties are **split between the provider (the vendor) and the deployer (Trishul)**, and **human oversight of scored decisions is mandatory**. Therefore "the agent decides" is **not legally available**: the model may *score and recommend* (autonomy **L2**), but it may not automatically renew or drop a supplier.

**ONE design obligation on Trishul (the deployer, not the vendor): build the human-oversight workflow.** A named, trained Trishul reviewer (for example the category head for EU-serving plants) must see each score with its main drivers, be able to **override it before any renewal decision executes**, and the decision and rationale must be **logged** for audit. Compliance "handled by the platform" is not enough — the vendor carries provider duties, but **oversight of Trishul's use is Trishul's by law** and cannot be delegated (Class Q 5.5 📘). Put the responsibility matrix in the contract.

*(Other acceptable deployer obligations, if you want a second line: keep usage logs; use the system per the provider's instructions; monitor it and report serious incidents; check the input data is relevant and representative — e.g. that the duplicate vendor records do not distort scores.)* 📗

---

## B1 — Model answer (5 marks)

**Assumptions:** A1. "Live in six months" means a real pilot making real decisions on a bounded scope, not a full roll-out. A2. Readiness scores [Data 2, Masters 2, Architecture 3, Security 3, Compute 4] are accurate; the unused GPU credits (Compute 4) do not offset weak data — compute is a stranded asset until foundations catch up 📘. A3. Vendor-master dedup (≈480 records) and rotation/inventory of vendor-facing API credentials can be completed in the first 6–8 weeks (Phase 0) by a named owner. A4. Tail spend is reachable as calculated in A3 (₹58.2 cr; break-even ≈1.9%) and Walmart–Pactum-like results (~3% savings, 64–68% close) are a ceiling, not a promise. A5. Gross margin on lost revenue is unknown, so the ₹7.8 cr stockout loss is revenue, not profit. A6. Proposal 3 under the EU AI Act can only run at L2 (human decides).

### Scoring with the pilot-selection matrix 📘
| Criterion | P1 ML forecasting | P2 Tail-spend agent | P3 Supplier-risk scoring |
|---|---|---|---|
| **Value at stake** | Inventory leg capped at ₹0.49 cr/yr carrying cost vs ₹2.5 cr year-1 cost; stockout leg unproven → **Low** | ₹58.2 cr pool; ~3% → ≈₹1.7 cr/yr vs ₹1.1 cr; plus term extension → **Medium-High** | Protects EU business (12% × ₹1,240 cr = **₹148.8 cr** revenue, growing 30%) and direct supply (top 10 = 62% × ₹410 cr = ₹254 cr) — real but hard to quantify → **Medium** |
| **Data feasibility** | 71% of sales arrive by 26-hour batch (timeliness binds), 11% SKU conflicts, 61% planning in spreadsheets → **Low** | Needs vendor-master dedup (fixable in weeks) and credential hygiene → **Medium** | Needs supplier data (duplicates distort scores) + human-oversight design → **Medium** |
| **Decision impact** | Full-truck multiples: forecast gains often map to the same order (rain-forecast reward) → **Low** | Every closed negotiation changes a price/term → **High** | Changes renewals — but quarterly → slow feedback |
| **Blast radius** | Wrong forecasts hit 1,900 distributors' supply → Medium | Median deal ₹1.9 lakh, reversible, bounded by mandate → **Low** | Wrong score could drop a key EU-serving supplier; regulatory exposure → **High** |
| **Agentic suitability screen** (frequency, reversibility, feedback, rule clarity, stakes) | Not agentic (predictive) | High frequency, reversible, fast feedback, clear mandate, low stakes → **≈21–23/25 → L3–L4 candidate** | Low frequency, low reversibility, slow feedback, politically loaded → **≈10–12/25 → keep human** |
| **Sponsor & learning value** | Builds forecasting data pipeline — useful later | Builds clean vendor master + agent governance — reusable | Builds compliance capability |

### Ranking
**#1 Proposal 2 (tail-spend negotiation agent), #2 Proposal 3 (as L2 decision support only), #3 Proposal 1.**

**One-line justification for #1:** P2 is the only proposal with a **material, measurable pool (₹58.2 cr) whose break-even (≈1.9%) sits below published evidence (~3%)**, the **lowest blast radius** (median ₹1.9 lakh, reversible, mandate-bounded) and a **readiness gap that can be closed inside the six months** — high value × feasible × low blast radius, exactly the Phase-1 profile 📘.

*(Why P1 is last: its headline claim fails A1's arithmetic, its data is the least ready (26-hour latency on 71% of revenue), and its decisions are rain-forecast-shaped. Why P3 is second: cheap at ₹0.8 cr and strategically important for the EU channel, but the law forbids autonomous renewals, so it can only be a recommend-and-review tool — fine as a parallel L2 pilot once the vendor master is clean.)*

### Phase 1 → Phase 2 gate for Proposal 2
| Gate element | Specification |
|---|---|
| **Scope of Phase 1** | 3 MRO categories (e.g. packaging consumables, maintenance spares, lab supplies) ≈ 600 de-duplicated suppliers, ≈ ₹15 cr spend; 4–6 months. |
| **Frozen baseline** | Frozen **before** go-live: last 12 months' price per item and payment terms per supplier for in-scope categories (median terms **30 days**; **84%** single-quoted; **9%** negotiated), plus supplier OTIF for the same period. Hold out a **randomly chosen control group** of comparable suppliers that the agent does not touch, so savings are measured against a counterfactual, not a moving baseline. |
| **Success metric 1** | **Realised (invoice-verified) net savings ≥ 2.5%** of renewed spend vs frozen baseline — above the 1.9% break-even with margin for error. |
| **Success metric 2** | **Median payment terms extended from 30 to ≥ 45 days** on closed deals (or close rate ≥ 40% of negotiations opened). |
| **Guarded counter-metric** | **Supplier OTIF and quality on in-scope MRO items must not fall by more than 2 percentage points** vs baseline (and no maintenance downtime caused by a supplier walking away) — savings bought by worse service do not count. |
| **Starting autonomy** | **L3 — act with approval gates.** The agent negotiates and closes inside the category-manager mandate (tradable levers, walk-away price, max term, approved-supplier list) for deals **under ₹5 lakh/yr**; anything above, any mandate edge case, or any non-standard clause is escalated. **Hard limits live outside the model** (spend caps and supplier allow-list in code, per-agent credentials, full action log, kill switch) 📘. Not L4 yet: no track record at Trishul and masters were just cleaned. |
| **Who decides** | The **CPO (named business owner)** decides promotion at a gate review, with **finance (CFO's nominee) certifying the savings** against the frozen baseline; the head of indirect procurement owns the agent day to day. |

### Demotion evidence (one sentence)
**If, at the gate, invoice-verified savings are below the 1.9% break-even (or are achieved only with an OTIF drop of more than 2 points, or any transaction is executed on a duplicate or unapproved vendor record), I demote Proposal 2 and promote Proposal 3's L2 pilot to #1.**

---

## Quick-revision summary of this paper
- **A1:** base = cycle + safety = ₹13.6 cr; 30% = ₹4.08 cr > S = ₹2.6 cr; ceiling 19.1% → claim fails; carrying-cost pool ₹0.49 cr/yr vs ₹1.6 cr/yr fee.
- **A2:** irrelevant = marketing, lease, CSR, canteen, solar, website, app, GST, HR metrics, fleet; defective = 11.0 + 2.6 + 1.2 = 14.8 ≠ 15.2; "<2% duplicates" vs 480/2,890 = 16.6%; correction → 17.6% ceiling, verdict unchanged.
- **A3:** pool = 64 × 0.91 = ₹58.2 cr; break-even = 1.1 ÷ 58.2 = 1.9%; fix = vendor-master dedup + named owner (else duplicate negotiations/terms/double-counted savings); plus API-credential gate.
- **A4:** EU AI Act high-risk, already enforceable; provider/deployer split; human oversight mandatory → L2 only; Trishul must build the oversight workflow (named reviewer, override before execution, logging).
- **B1:** P2 > P3 > P1; L3 start; frozen baseline + control group; savings ≥ 2.5% and terms ≥ 45 days; OTIF guard; CPO decides with finance; demote if savings < 1.9%.
