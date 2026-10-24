# Numericals — every calculation type, fully worked
The faculty said the numericals will be **"straightforward calculations without requiring any additional formulas"** 📘 — i.e. arithmetic on the exhibit, not derivations. The past papers prove it: every number in them is a share, a sum, a difference, a ratio, a weighted average or a break-even. Part A covers the **case-numerical patterns** from the papers and class questions; Part B covers the **basic SCM numericals** you may need for "basic concepts of SCM". Each problem shows the **assumptions, arithmetic with units, and the one-line meaning**.

> Exam habit: write each calculation as **What → Arithmetic → Result (units) → So what**. Always open a verdict with *Assumptions: A1 … A2 …*.

---

# Part A — Case numericals (the patterns the papers use)

## A1. The reachable-pool test (forecasting attacks S, not Q) ⭐⭐⭐
**Q1. A distributor holds ₹8 crore of cycle stock (weekly truckload deliveries) and ₹2 crore of safety stock. A vendor claims its forecasting AI will cut total inventory 30%. Test the claim.** 📘 (S1 Class Q 1.2)
*Assumptions:* A1. Forecast accuracy affects only safety stock; truckload size and weekly frequency (cycle stock) are unchanged. A2. Figures are average inventory at cost.
- Claimed cut: 30% × (8 + 2) = **₹3.0 cr**.
- Maximum possible: all of S = **₹2.0 cr** → ceiling = 2 ÷ 10 = **20%**.
- **Verdict:** the 30% claim is arithmetically impossible from forecasting; even a perfect forecast reaches 20%. The bigger lever is Q (smaller, more frequent deliveries, shorter lead times — the Campbell Soup lesson).

**Q2. Same firm: what is the claim worth in money if forecasting halves safety stock, at a 20% carrying rate?**
- Inventory freed = 50% × ₹2.0 cr = ₹1.0 cr (10% of total, not 30%).
- Annual carrying saving = ₹1.0 cr × 20% = **₹0.2 cr/yr** (plus a one-off ₹1.0 cr cash release).
- Compare with the tool's annual fee — if the fee is above ₹0.2 cr/yr, the inventory case alone does not pay.

**Q3 (Trishul A1).** Cycle ₹11.0 cr, safety ₹2.6 cr, carrying 19%, subscription ₹1.6 cr/yr. → 30% × 13.6 = ₹4.08 cr vs S = ₹2.6 cr; ceiling 19.1%; carrying value of the entire S pool = 2.6 × 0.19 = **₹0.49 cr/yr < ₹1.6 cr/yr**. Claim fails. See [Trishul paper](pyq-trishul.md).

## A2. "Precision pays only when a decision changes" (rain-forecast reward) ⭐⭐
**Q4. Your forecast error improves from ±40 to ±15 units; orders must be placed in full pallets of 240 units. Demand forecast for next week moves from 159 to 124. What changes?** 📘 (S1 Class Q 1.3)
- Pallets needed at 159 = ⌈159 ÷ 240⌉ = 1 pallet; at 124 = ⌈124 ÷ 240⌉ = 1 pallet.
- **Same decision → little to no business impact.** Accuracy pays only up to the point where the decision stops changing.
- *When would it pay?* Only if demand sits near a threshold, e.g. 230 vs 250 → 1 vs 2 pallets.

## A3. Value pool and break-even savings rate ⭐⭐⭐
**Q5 (Trishul A3).** Tail spend ₹64 cr over 2,410 suppliers; 9% of suppliers already negotiated; agent costs ₹1.1 cr/yr.
| Step | Arithmetic | Result |
|---|---|---|
| Un-negotiated share | 100% − 9% | 91% |
| Addressable pool | 64 × 0.91 | **₹58.2 cr** |
| Break-even rate | 1.1 ÷ 58.2 | **1.89%** |
| With 65% close rate | 1.1 ÷ (58.2 × 0.65 = 37.8) | **2.9%** |
| Expected savings at Pactum's ~3% (all closed) | 58.2 × 0.03 | ₹1.75 cr/yr → net +₹0.65 cr |
*So what:* break-even below published evidence → worth a pilot, but thin once close rates are applied → measure realised savings.

**Q6. Payment-term extension value.** The agent extends median terms from 30 to 65 days (+35 days, Pactum's average) on ₹58.2 cr of annual spend; cost of capital 10%.
- Working capital released = 58.2 × 35 ÷ 365 = **₹5.58 cr** (one-off).
- Annual value = 5.58 × 10% = **₹0.56 cr/yr** — nearly half the agent's fee from terms alone.

**Q7. Mean vs median check.** ₹64 cr ÷ 2,410 = **₹2.66 lakh mean** vs ₹1.9 lakh median → mean > median → spend is right-skewed (a few larger suppliers). If the 9% negotiated suppliers are the large ones, the un-negotiated *spend* share is below 91% — state that as an assumption.

## A4. Duplicate-record arithmetic (data quality: uniqueness) ⭐⭐
**Q8 (Trishul A2).** Vendor master 2,890 records for ~2,410 real suppliers; an old report says "duplicates < 2%".
- Surplus records = 2,890 − 2,410 = **480**.
- As a share of records = 480 ÷ 2,890 = **16.6%**; as a share of real suppliers = 480 ÷ 2,410 = **19.9%** (≈ "18%").
- **8–10× the claimed 2%** → the report is stale and contradicted.
**Q9 (S2 Class Q 2.1).** Your largest supplier shows 4% of spend, but it is duplicated across six vendor records of equal size. True share = 6 × 4% = **24%** → analytics measured record-keeping, not concentration.

## A5. Do the exhibit numbers add up? (reconciliation) ⭐⭐⭐
**Q10 (Trishul Ex 4).** "Total average inventory ₹15.2 cr = cycle 11.0 + safety 2.6 + in-transit 1.2." → 11.0 + 2.6 + 1.2 = **14.8 ≠ 15.2** → ₹0.4 cr unexplained → defective. With 14.8, S share = 2.6 ÷ 14.8 = **17.6%** (verdict on a 30% claim unchanged).
**Q11 (Kaveri Ex 1) — cash roll-forward.** 6.3 → 6.3 − 5.8 = 0.5 → 0.5 − 15.6 = −15.1 → −15.1 + 3.6 = −11.5 → −11.5 − 1.9 = −13.4 ≈ −13.3 ✓.
**Q12 (Kaveri) — implied overheads.** Revenue − production cost − profit: M1 47.0 − 27.2 − 6.3 = 13.5; M5 36.4 − 25.1 − (−1.9) = 13.2 → consistent with the stated ₹12.6–13.2 cr band (plus freight) → the profit lines are credible.

## A6. Simple vs weighted averages — exposing a hidden trend ⭐⭐⭐
**Q13 (Kaveri A1).** Monthly fill 86.0, 85.9, 73.8, 64.5, 58.2% with sold 435, 397, 259, 342, 374 and lost 71, 65, 92, 188, 269.
- Simple average = 368.4 ÷ 5 = **73.7%** (the memo's figure).
- Volume-weighted = Σsold ÷ Σdemand = 1,807 ÷ (1,807 + 685) = 1,807 ÷ 2,492 = **72.5%**.
- Current month = **58.2%** — 15.5 points below the average; five consecutive declines; lost sales ×3.8 (71 → 269).
*So what:* the average is arithmetically right and decision-wise misleading.

**Q14. Fill check.** Fill = sold ÷ (sold + lost): M4 = 342 ÷ 530 = **64.5%** ✓.

## A7. Contribution forgone on lost sales (with a mix assumption) ⭐⭐⭐
**Q15 (Kaveri A2b).** 269 lost sales; M5 sales mix 219 HATCH · 96 SUV · 59 EV; prices ₹6.05 / 15.50 / 14.05 L; unit costs ₹3.85 / 8.30 / 8.00 L.
*Assumptions:* A1. Lost mix = sales mix. A2. Contribution = price − unit production cost (overheads fixed).
| | HATCH | SUV | EV | Total |
|---|---|---|---|---|
| Unit contribution (₹ L) | 2.20 | 7.20 | 6.05 | |
| Lost units (269 × 219/374, 96/374, 59/374) | 157.5 | 69.0 | 42.4 | 269 |
| Contribution forgone (₹ L) | 346.5 | 497.1 | 256.7 | **1,100 L = ₹11.0 cr** |
- Ratio to the reported loss: 11.0 ÷ 1.9 = **5.8×**; to the ₹60 L congestion charge: 1,100 ÷ 60 = **18×**.
- Revenue on the lost sales (cars already in stock): avg price 3,641.9 ÷ 374 = ₹9.74 L × 269 = **₹26.2 cr**.

**Q16. Weighted contribution shortcut.** (219 × 2.20 + 96 × 7.20 + 59 × 6.05) ÷ 374 = 1,529.95 ÷ 374 = **₹4.09 L per car**.

**Q17. Cost of an unrestored price cut (Kaveri).** List 6.40 / 16.00 / 14.50 vs M5 6.05 / 15.50 / 14.05 → cuts of 0.35 / 0.50 / 0.45 L × 219 / 96 / 59 = 76.65 + 48.0 + 26.55 = **₹151.2 L ≈ ₹1.5 cr per month** given away.

**Q18. Was the "profitable month" a recovery?** (Kaveri M4) Production cost fell from ₹26.4 cr (M3) to ₹16.8 cr (M4) = **−₹9.6 cr**, because chip allocation cut production to 462 sets. Profit +₹3.6 cr = revenue 33.8 − production 16.8 − overheads ≈13.4 → the "recovery" is a forced production cut (cherry-picked month).

## A8. Net value of a "live" agent ⭐
**Q19 (Kaveri Ex 3).** Mode & Routing agent: ₹1.5 L freight saved, ₹4.1 L missed → net = 1.5 − 4.1 = **−₹2.6 L** → it destroys value until planned flows exist.

## A9. Token economics — cost per decision vs value per decision ⭐⭐⭐
**Q20.** A negotiation agent costs ₹3.0 L a month to run and makes 1,500 decisions; each closed decision is worth on average ₹1,200 of margin. The platform doubles its price. Keep, tune or retire?
- Cost per decision before = 3,00,000 ÷ 1,500 = **₹200**; after = **₹400**.
- Value per decision = **₹1,200** → ratio 3.0× after the price rise (6× before).
- **Verdict:** still clearly positive → keep, and tune (shorter context, caching, cheaper tier) to win back margin. "A price shock is a signal to re-run the math, not a verdict."
**Q21.** Same agent, but each decision is worth ₹300. After repricing, cost ₹400 > value ₹300 → **tune first**; if a tuned version (say ₹250/decision) still cannot clear ₹300 with margin, **retire** and fall back to the next-best option.
**Q22 (Chain Reaction tokens).** 24 tokens/month; plan 2 tokens; four agents with upkeep 1 + 2 + 3 + 4 = 10 → remaining for transformation = 24 − 2 − 10 = **12 tokens** (and at most 4 transformation actions). Terminating one 4-token-upkeep agent costs 2 tokens once and saves 4 a month → pays back in month 1 if its value per decision no longer clears cost.

**Q23. Efficiency-capture gap (McKinsey, S17 📘).** Agentic procurement gave 20–30% staff-efficiency gains but only 1–3% bottom-line capture. If procurement staff cost ₹10 cr/yr: efficiency "value" 25% × 10 = ₹2.5 cr, but realised P&L ≈ 1–3% of the relevant base — always compare **captured margin**, not efficiency, to the run cost.

## A10. Accuracy claims vs naive benchmarks ⭐⭐
**Q24 (S6 Class Q 6.4).** New model 92% accurate; naive "same as last week" 90.5%; orders in full-truck multiples.
- Gain = 1.5 points; error falls from 9.5% to 8.0% → relative error reduction = 1.5 ÷ 9.5 = **15.8%**.
- With full-truck ordering, much of that maps to the same truck → **unproven** until priced in decisions changed.
**Q25 (S7 Class Q 7.3).** Churn is 3% of customers; a model shows 99% accuracy. The trivial "never churns" rule scores **97%** → the model's real edge is 2 points at most, and 99% often signals leakage.
**Q26. Confusion matrix.** 1,000 weeks; model flags demand spikes: TP 40, FP 20, FN 10, TN 930.
- Accuracy = (40 + 930) ÷ 1,000 = **97%** (looks great).
- Precision = 40 ÷ (40 + 20) = **66.7%**; Recall = 40 ÷ (40 + 10) = **80%**; F1 = 2 × 0.667 × 0.8 ÷ (0.667 + 0.8) = **0.727**.
- "Always predict no spike" would score 950 ÷ 1,000 = 95% accuracy with 0% recall → accuracy on a skewed problem is misleading; use precision/recall/F1.

## A11. The DRL "20% better" claim vs the theory ceiling ⭐⭐
**Q27 (S10 Class Q 10.1).** A simple myopic policy is known to be within ~5% of optimal cost; your tuned basestock policy is at least as good. A vendor claims its DRL cuts cost 20% vs your incumbent.
- Incumbent cost ≤ 1.05 × optimal → best possible improvement = 1 − 1/1.05 = **4.8%**.
- A 20% claim would put the DRL policy **below the optimum** → impossible → the backtest most likely contains **overfitting or a weak baseline**. Fund only a guardrailed pilot.

## A12. Fill rate at constant inventory vs inventory released ⭐
**Q28 (S8/S10 📘).** One-step planning at a Fortune 150 spare-parts business lifted fill from **77% to 85% at constant inventory**, *or* released **~$20M of inventory at constant service**. If a planner has 10,000 order lines a month: 85% − 77% = 8 points → **800 more lines filled a month** at the same inventory — "the frontier shifted, not just a point on it".

## A13. Mode economics — rail floor vs road ⭐⭐
**Q29.** Base load of 300 cars/month on a lane; road costs ₹12,000 per car; rail is ~25% cheaper (₹9,000) but slots are booked a month ahead and charged whether used or not.
- All road: 300 × 12,000 = **₹36.0 L**.
- Book a rail floor of 250 slots + 50 by road: 250 × 9,000 + 50 × 12,000 = 22.5 + 6.0 = **₹28.5 L** → saves ₹7.5 L/month.
- Worst case: only 200 of the 250 slots used, 100 cars by road: 250 × 9,000 (paid regardless) + 100 × 12,000 = 22.5 + 12.0 = **₹34.5 L** → *still cheaper than all-road*.
- Break-even utilisation of a slot: pay 9,000 for a slot that saves 12,000 if used → worth booking if P(used) > 9,000 ÷ 12,000 = **75%**. Size the floor to the base load you are ≥ 75% sure of.
*So what:* "rail's book-ahead charge is money spent on capacity we may never use" (Kaveri Claim 4) argues insurance backwards — a floor sized to base load pays even when partly unused, and protects you when road congests.

**Q30 (S14 Class Q 4.1). Split shipment.** Zone needs 120 cars within 1 day; trailer-express ₹30,000/car (1 day), rail ₹9,000/car (2 days). Urgent need 50 cars (stock covers the rest for 2 days) → 50 × 30,000 + 70 × 9,000 = 15.0 + 6.3 = **₹21.3 L** vs all express 120 × 30,000 = **₹36.0 L** → split saves ₹14.7 L and still protects service.

## A14. Scoring frameworks as numericals ⭐⭐
**Q31. Agentic suitability screen.** Robot routing in your own warehouse: frequency 5, reversibility 4, feedback 5, rule clarity 4, stakes 5 = **23 → L3–L4**. Tail-spend reorder: 5, 4, 4, 4, 4 = **21 → L3–L4**. Strategic supplier partnership: 1, 1, 2, 2, 1 = **7 → keep human**. Rank c > b > a (S4 Class Q 4.5).
**Q32. Readiness profile.** [Data 2, Masters 1, Architecture 3, Security 2, Compute 5]: mean = 13 ÷ 5 = 2.6, but **the weakest pillar (masters = 1) sets the ceiling**, not the mean → predictive pilot on the cleanest domain; no write-access agents (S2 Class Q 2.5).

## A15. Gate thresholds from a break-even ⭐
**Q33.** Agent break-even = 1.9%; measurement error on savings ±0.5 point → set the success threshold at **≥ 2.5%** (break-even + margin) and the demotion trigger at **< 1.9%**. Always pair with a counter-metric (e.g. supplier OTIF not down > 2 points).

## A16. Revenue at risk and exposure sizing ⭐
**Q34 (Trishul).** EU revenue = 12% × ₹1,240 cr = **₹148.8 cr**, growing 30% → next year ≈ 148.8 × 1.3 = **₹193 cr**. Direct-material concentration: top 10 suppliers = 62% × ₹410 cr = **₹254 cr**; dual-sourced on 7 of 10 → 3 single-sourced top suppliers. Use these to argue P3's strategic value (and its high blast radius).
**Q35.** Stockout revenue loss ₹7.8 cr/yr; "50% fewer stockouts" → ₹3.9 cr revenue recovered; at an assumed 40% gross margin = **₹1.56 cr contribution** — revenue is not profit.

---

# Part B — Basic SCM numericals (refresher)
These use the standard SCM relationships you already know; the exam may give the formula or expect simple arithmetic. See [SCM Fundamentals](ch00-scm-fundamentals.md).

## B1. EOQ and cycle stock
**Q36.** Annual demand D = 12,000 units; ordering cost S = ₹1,500/order; holding cost H = ₹20/unit/yr.
- EOQ = √(2DS ÷ H) = √(2 × 12,000 × 1,500 ÷ 20) = √1,800,000 = **1,342 units**.
- Orders/yr = 12,000 ÷ 1,342 = **8.9**; average cycle stock = Q/2 = **671 units**.
- Annual ordering cost = 8.94 × 1,500 = ₹13,410; holding = 671 × 20 = ₹13,420 → equal at EOQ (check ✓).
*Course link:* if a truck holds 2,000 units and you must ship full trucks, Q is set by the truck, not EOQ — this is why forecasting cannot touch cycle stock.

## B2. Safety stock and reorder point
**Q37.** Daily demand d = 40 units (σ = 10/day); lead time L = 9 days; service level 95% (z = 1.65).
- Safety stock = z × σ × √L = 1.65 × 10 × 3 = **49.5 ≈ 50 units**.
- Reorder point = d × L + SS = 40 × 9 + 50 = **410 units**.
- *"The quantile IS the decision":* a 95% cycle service level = holding the 95th percentile of lead-time demand. Halving σ (better forecast) halves SS to ~25 — but cycle stock (Q/2) is untouched.

**Q38. Same mean, different variance (S8 Class Q 8.2).** SKU A ±50, SKU B ±400 on a forecast of 1,000 (z = 1.65): SS_A = 82.5, SS_B = 660 → "forecast + 2 weeks of supply" for both is wrong for both.

## B3. Newsvendor — critical ratio
**Q39.** A seasonal item costs ₹60, sells for ₹100, leftovers salvage at ₹20.
- Cost of under-stocking Cu = 100 − 60 = ₹40; over-stocking Co = 60 − 20 = ₹40.
- Critical ratio = Cu ÷ (Cu + Co) = 40 ÷ 80 = **0.50** → order the median of demand.
- If salvage rises to ₹50 → Co = 10 → CR = 40 ÷ 50 = **0.80** → order the 80th percentile. *Asymmetric costs → order a quantile, not the mean* (decision-focused learning, S6/S8).

## B4. Inventory turns, days of supply, cash-to-cash
**Q40.** COGS ₹96 cr/yr; average inventory ₹12 cr.
- Turns = 96 ÷ 12 = **8×/yr**; days of supply = 12 ÷ (96/365) = **45.6 days**.
**Q41.** DIO 45 days, DSO 30 days (distributors pay in 30), DPO 40 days → cash-to-cash = 45 + 30 − 40 = **35 days**. Extending supplier terms by 35 days (Pactum) cuts it to **0 days**.

## B5. Fill rate, service level, OTIF
**Q42.** 1,000 order lines; 930 shipped complete and on time; 40 complete but late; 30 short. Line fill rate = (930 + 40) ÷ 1,000 = **97%**; OTIF = 930 ÷ 1,000 = **93%**.

## B6. Forecast error metrics
**Q43.** Actual 100, 120, 90, 110; forecast 110, 100, 100, 100.
- Errors (A − F): −10, +20, −10, +10 → **MAD = 50 ÷ 4 = 12.5**; **MAPE** = (10/100 + 20/120 + 10/90 + 10/110) ÷ 4 = **11.7%**; **bias** (sum of errors) = **+10** (slight under-forecast).
- MAPE fails on zeros (intermittent spares 0,0,0,4,0,0,2,0 → undefined) — use distribution/quantile metrics instead (S10 Class Q 10.2).
**Q44. Exponential smoothing (α = 0.3).** F₁ = 500; demand 520, 480, 560 → F₂ = 500 + 0.3 × 20 = **506**; F₃ = 506 + 0.3 × (−26) = **498.2**; F₄ = 498.2 + 0.3 × 61.8 = **516.7**. (Tier-1 spreadsheet method — S9 lab.)

## B7. Bullwhip ratio
**Q45.** Variance of retail demand = 100; variance of distributor orders = 400; factory orders = 1,600. Bullwhip ratio = 400 ÷ 100 = **4** at the distributor and 1,600 ÷ 400 = **4** again upstream (cumulative **16×**). *Fix (S19):* shared end-customer demand, order smoothing, trained coordination — not faster agents.

## B8. Risk pooling
**Q46.** Four DCs each face demand σ = 100; safety stock at z = 1.65 → 4 × 165 = **660 units**. Centralising (independent demand) → σ = 100 × √4 = 200 → SS = **330 units** (50% less). Trade-off: longer last-mile distance — the Kaveri physics (zones pull only from their own RDC) means pooling only works if flows are planned.

## B9. Maintenance economics (predictive vs reactive)
**Q47.** A press fails on average once a quarter; unplanned failure costs ₹8 L (downtime + rush part); planned replacement costs ₹2 L. A predictive model catches 75% of failures early; the sensor kit costs ₹6 L/yr.
- Reactive cost/yr = 4 × 8 = **₹32 L**.
- Predictive: 3 caught × 2 + 1 missed × 8 = **₹14 L** + ₹6 L sensors = ₹20 L → saves **₹12 L/yr**.
- *But* (S13 Class Q 3.1): if a weekly inspect-and-replace routine already catches the wear, the model changes no decision → value ≈ 0.
**Q48. OEE.** Availability 90% × performance 95% × quality 98% = **83.8%**.

## B10. Landed cost / TCO for sourcing
**Q49.** Supplier A quotes ₹100/unit, lead time 30 days, 2% defects; Supplier B ₹96/unit, lead time 75 days, 5% defects; defect cost ₹50/unit; holding 20%/yr on pipeline stock.
- A: 100 + 0.02 × 50 + 100 × 0.20 × 30/365 = 100 + 1.0 + 1.64 = **₹102.6**.
- B: 96 + 0.05 × 50 + 96 × 0.20 × 75/365 = 96 + 2.5 + 3.95 = **₹102.5** → near-tie on TCO; B's longer lead time also adds safety stock and risk → **A preferred** once risk is counted. *(Use for supplier-risk scoring cases.)*

## B11. Little's Law
**Q50.** An RDC ships 600 cars/month and holds 662 cars on average → time in system = 662 ÷ 600 ≈ **1.1 months**. If fill is falling at the same time, the stock is in the wrong place (Kaveri).

---

## One-page formula reminder (in case the paper gives them)
| Quantity | Relationship |
|---|---|
| Average inventory | cycle stock (Q/2) + safety stock (S) (+ in-transit) |
| EOQ | √(2DS/H) |
| Safety stock | z × σ_d × √L |
| Reorder point | d × L + SS |
| Critical ratio (newsvendor) | Cu ÷ (Cu + Co) |
| Fill rate | units (or lines) delivered ÷ units demanded = sold ÷ (sold + lost) |
| Turns / days of supply | COGS ÷ avg inventory; avg inventory ÷ daily COGS |
| Cash-to-cash | DIO + DSO − DPO |
| Contribution | price − variable (unit) cost |
| Break-even savings rate | annual cost ÷ addressable pool |
| Working capital from terms | annual spend × extra days ÷ 365 |
| Cost per decision | run cost ÷ decisions made |
| Precision / recall | TP ÷ (TP + FP) / TP ÷ (TP + FN) |
| Bullwhip ratio | var(orders) ÷ var(demand) |
