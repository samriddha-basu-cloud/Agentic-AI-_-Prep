# Chain Reaction Simulation — strategies, decisions and management approaches
Your faculty asked for **"particular emphasis on the strategies, decisions and management approaches used in the Chain Reaction simulation"** 📘. The Kaveri Motors paper was set *inside* the game. This page rebuilds the game's rules from the session decks and the past paper, lists the decisions you make each round, the strategies that won and lost the season, and the course framework behind each one.

> Sources: Sessions 11–20 "Coming up next" round briefs 📘, the Kaveri Motors paper's physics reminder and exhibits 📘, and the Session 20 season debrief (four archetypes, twenty teams) 📘. Where a mechanic is inferred rather than stated, it is marked 📗.

---

## 1. The world you play in
| Element | What the game uses 📘 |
|---|---|
| **Market** | ~**20 companies (boards)** trading in one market, same physics, same calendar of shocks. Teams were labelled A1–A10 and B11–B20 (e.g. B12-Titans, A7-Kimi K3, A8-The Odyssey). |
| **Your company** | A car maker: **3 plants**, **4 regional distribution centres (RDCs)**, **7 dealer zones**. |
| **Products** | **HATCH, SUV, EV.** Kaveri's unit production costs: HATCH ₹3.85 L · SUV ₹8.30 L · EV ₹8.00 L. List prices ₹6.40 / 16.00 / 14.50 L. |
| **Transport modes** | **Rail** — cheap (~25% cheaper than road), slow, **slot-constrained**, booked **a month ahead** against the demand plan, **charged whether used or not**. **Road** — the flexible workhorse; also the **default lane** for unrouted stock. **Trailer-express** — fast, expensive, capacity-limited (for urgent top-ups). |
| **Physics** | **Unrouted plant stock auto-pushes to the plant's home RDC by road**. **Dealer zones pull only from their own region's RDC.** → if you do not plan flows, stock piles up near the plants and other zones stock out. |
| **Components** | **Chip sets are allocated against contracted volume**; **fees are charged on the full book, used or not** (M4 Kaveri: "contracted volume earned you 462 chip sets; production scaled to match"). |
| **Money** | Monthly profit is after freight, storage and **fixed overheads (~₹12.6–13.2 cr/month)**; cash rolls forward month to month. |
| **Shocks (event calendar)** | M1 Calm · M2 Monsoon + carrier failure · M3 Credit slump + EV surge · M4 Chip allocation · M5 Port jam + corridor congestion (Kaveri's season). Hazards can be insured — "**Cover on this hazard: 0%**" means no insurance was bought. |
| **Attention budget** | **24 decision tokens a month**; **cap of 4 transformation actions a round**; **2 tokens to generate an operating plan, 1 to regenerate it**; **every agent you own charges 1–4 tokens a month in upkeep**; **terminating a capability costs 2 tokens** (its build cost is sunk). |
| **Foundations** | Three foundation ladders — **Data · Process · Tech (D·P·T)** — each from L1 to L5. Raising them costs tokens (Kaveri: 27 tokens across the season to reach L4·L4·L4). |
| **Capabilities (agents)** | Bought from a catalogue in families (demand, production, distribution, pricing, procurement, governance). Each has a **gate** of minimum foundation levels, e.g. Distribution Planning Agent **D2·P1·T1**; Network-Intelligence Orchestrator **D3·P3·T3**. Some have **prerequisites** (Demand Sensing Agent needs the 2-token Demand Signal Desk Agent; Cross-Channel Repricing needs the Price-Setting & Segmentation Agent). |
| **Below-gate builds** | Allowed, but "**build odds cut, and whatever ships delivers a fraction of its designed effect until the gap is closed**" — "**a below-gate agent runs at full cost and a fraction of the effect**." Example odds: 55%, 45%, 20%, 12%. |
| **Build speed** (Round 2) | **FAST 0.85× cost at quality −18 · STANDARD 1.0× · CAREFUL 1.25× over two rounds at quality +6**, no failure chance either way. |
| **Scoring** | **Company value = profit × reputation × trust.** Board confidence, trust and reputation fall after incidents (Kaveri M5: board confidence −5 after the congestion charge). |
| **Distribution dials** (from Round 4) | **distCover** (coverage), **distSafety** (safety stock), **distFront** (SPREAD or FRONT — spread stock across RDCs or front-load it), **distMode** (ROAD or MIX — **MIX, i.e. rail in the mix, locked until tech maturity 3**). The engine builds the flows from these four parameters. |
| **Named catalogue agents** | PRD_MAINT_2/3 Predictive & Prescriptive Maintenance (production family); DIS_NET_2/3 Network Design & Digital Twin; DIS_EXCP_2/3 Dynamic Exception & Re-Routing (distribution family) — "**L2 specialist first, L3 only as an upgrade on top of it**". Others seen in the debrief: Demand Signal Desk, Demand Sensing, Forecast Error/Bias Tracking, Mode & Routing Optimization, Distribution Planning, Price-Setting & Segmentation, Cross-Channel Repricing (L5 closed loop), Production Intelligence Orchestrator, Plant Orchestrator, Scheduling agent, quality agent, data pipeline, network-topology model, Control Tower, Network-Intelligence Orchestrator. |

---

## 2. Round-by-round: what each round tested and the right move
| Round (session) | Theme 📘 | The decision | The winning approach | Course tool |
|---|---|---|---|---|
| **R1 (S11)** | Onboarding: manual ops, first forecast, learn the console | Forecast and plan manually | Forecast a **distribution, not a number** from the first click; stock to a quantile (service level) | Probability forecasting |
| **R2 (S12)** | **Forecasting bake-off** — choose your forecasting-agent tier against your own history; FAST / STANDARD / CAREFUL build | Which tier, which build speed | Pick the tier your **volume, readiness, skills and governance** justify (not the flashiest); CAREFUL when quality matters and you can wait; never FAST on a core capability (−18 quality) | Bake-off ladder; tier matching |
| **R3 (S13)** | **Aftermarket & maintenance** — telemetry investment | Buy PRD_MAINT / DIS_NET? | Fund telemetry **only if it changes a real decision downstream**; **L2 specialist first, L3 as upgrade** | Twin-Now/Twin-Later test |
| **R4 (S14)** | **The network opens** — set distCover, distSafety, distFront, distMode; a basic network agent becomes deployable | Distribution parameters | **Set policy, not flows**; protect high-value zones; plan for mode mix; book rail where eligible (needs tech maturity 3 for MIX) | Mandate card |
| **R5 (S15)** | **Setting the mandate** — the parameters *are* the objective the solver executes | Service targets & cost weights | Differentiate zones (a high-margin zone ≠ a cheap-to-serve one); name re-solve triggers; check the plan against the service floor before it runs | Optimizer mandate checklist |
| **R6 (S16)** | **Chip contract negotiation** — your procurement agent negotiates under a mandate (like Walmart–Pactum) | Contract volume and clauses | Size the chip book to **real** demand (fees on the full book); specify the clauses that matter **before** the agent signs; strictest bar on penalty/liability terms | Clause-stakes checklist |
| **R7 (S17)** | **The token economy** — 24 tokens/month, 4 actions/round, upkeep 1–4 per agent | Keep, tune or retire agents | Decide on **cost-per-decision vs value-per-decision**, not on the size of the bill; tune first, retire only if still under water | Tune-or-retire checklist |
| **R8 (S18)** | **Scenarios** — no scenario/crisis agent exists; nearest are DIS_EXCP and DIS_NET | Which resilience capability | Generate scenarios yourself, **label** them plausible/stretch/implausible, buy the capability that **survives more than one** of them | Scenario portfolio checklist |
| **R9 (S19)** | **Coordination under pressure** | How agents react to each other | **Shared demand signal**, a fast-but-not-panicked reaction (order smoothing), a **clear owner** of the call | Multi-agent fixes; ACAP |
| **R10 (S20)** | **Finale** — file the post-incident review in-game; endgame scoring locks | Honest incident write-up | Disclose, step autonomy down when needed, check against ACAP | ACAP governance checklist |

*(Session 10's "Command Your Agent" game in July was the bullwhip warm-up: twenty teams' agents produced "a textbook bullwhip blowup live on the shared screen" 📘 — the source of Session 19's "amplification we made".)*

---

## 3. How the season played out — the four archetypes (S20 debrief 📘)
Two axes decided the season: **how much AI capability a team built** (live agents) and **how well it kept operating** (operating discipline). Bubble size = final company value.

| Archetype | Teams | Pattern | Result |
|---|---|---|---|
| **Compounders — WON** | 6 (B12-Titans #1, A7-Kimi K3 #2, A2-Doomsday #4, B15-Neural 15 #6, B17-BLTB #7, A3-OpsManiacs #9) | **Built capability on foundations they had actually laid — and kept the business running.** | Top of the table |
| **Lean operators** | 3 (A8-The Odyssey #3, A9-Skynet #5, B20-Andromeda #12) | **Minimal transformation, deep foundations, excellent execution.** Capital-efficient — lower ceiling, thin cover. | #3 on six agents; #12 on one agent |
| **Transformation theatre** | 7 (B14-Six Sigma #8, A10-Decepticons #10, B18-Promptplay #13, A6-Smooth Ops #15, A5-Tokenizer #16, B11-Dream11 #17, A1-Tankers #18) | **Built the most, on the least foundation. Activity mistaken for outcome.** Below-gate builds, build failures (12%, 20% odds), guardrail breaches. | 8th to 18th |
| **Foundations, not run** | 4 (B13-Kolirt #11, B16-nEYtra #14, B19-Utkarshan #19, A4-Sapiens #20) | **Laid deep ground — and never ran on it. Bought the platform, didn't operate the business.** | 11th to 20th |

### Team snapshots worth quoting in an answer
- **B12-Titans — CHAMPION (value 213):** widest estate (21 agents), **rail every round**, **trust held at 110 through every shock**; not flawless (an R10 Control-Tower build failed, fill settled at 79) — "**won on breadth and governance, not perfect execution**".
- **A7-Kimi K3 — #2 (212):** "**the textbook build — ZERO below-gate all season**, deep L5, rail every round, best cash (₹1,212 cr), highest trust (111)"; lost by 1.1 points as fill drifted to 80.
- **A8-The Odyssey — #3 (191) on just 6 agents:** every foundation at L5, trust past 100, ₹1,181 cr cash — "**the efficiency champion**".
- **A2-Doomsday — #4 (186):** gates respected, trust ~100, fill 84 — but "**a late distribution miss (338 cars auto-pushed to the nearest RDC)**" kept it off the podium. *(This is exactly Kaveri's failure.)*
- **B20-Andromeda — #12:** "the purest operator", best reputation (0.92), 95% plan accuracy, fill 85 **on a single agent** — but **zero governance estate → trust bottomed at 78**.
- **B14-Six Sigma — #8:** clean operation, trust 98, fill 76 → 84 — but "**built on sand**": the R10 Network-Intelligence Orchestrator **failed at 12% odds, below its D3·P3·T3 gate**, like every build before it.
- **B18-Promptplay — #13:** a **Scheduling agent breached its guardrails in R10 and was pulled**; lowest reputation (0.75) — "**trust alone never paid**".
- **A6-Smooth Ops — #15:** transit losses to zero, ₹239 cr final-month profit — but 12 agents, several below gate, an earlier governance failure.
- **A1-Tankers — #18:** 12 agents, deep P5 foundations, but **fill never held (65 → 77)** — "scale never became service".
- **A4-Sapiens — #20 (46):** a deep L5 estate, yet **fill 92 → 69, trust 61 (last)**, chip stock depleted.
- **B13-Kolirt — #11:** drove every ladder to L5 but only 5 live agents; in R10 **"attention ran out (24 tokens)" so two builds were shelved** — "kept queuing capability it never operated".
- **A3-OpsManiacs — #9:** disciplined (trust 99, ten well-gated agents) but **R10 attention ran out (25/24 tokens) and rail slots fell short**.

### The four lessons the faculty drew 📘 (memorise — these are the "management approaches")
1. **Sequence beats speed.** The top teams built **on** foundations they had laid; the rest built agents faster than the **D·P·T ground** could support. *A below-gate agent runs at full cost and a fraction of the effect.*
2. **Building is not operating.** Estate size never predicted rank on its own — **operating the estate did: booking rail, filing a distribution plan, sizing the chip book to real demand.** (#3 ran 6 agents, #12 ran one; four 12–13-agent estates finished 15th–18th.)
3. **Governance is the multiplier you feel late.** **Company value = profit × reputation × trust.** The champion held trust at 110 through every shock; teams that skipped the resilience/governance estate watched trust collapse (B20 → 78, A4 → 61) "and the multiplication did the rest".
4. **Efficiency is a real strategy.** A8 finished #3 on six agents and B20 held top-tier service on one — **deep foundations amplified a tiny estate**. Lean works, *provided you still buy the insurance*.

---

## 4. The strategy rulebook — decisions that win (and the trap behind each)
| # | Decision area | Winning rule | The trap (seen in the game / Kaveri) | Course link |
|---|---|---|---|---|
| 1 | **Foundations vs agents** | Raise D·P·T to each agent's **gate before** you commission it; check prerequisites | Commissioning below gate (Kaveri's Demand Sensing at 55% odds, Repricing at 45%); B14's 12% orchestrator | Readiness sets the ceiling (S2); phased gates (S3) |
| 2 | **Distribution** | **File a plan-of-record every month**; route every car against the demand plan; never leave stock unrouted | Default auto-push to the home RDC → stock in the wrong region (Kaveri 276 cars; A2-Doomsday 338 cars) | Mandate card (S14); min-cost flow (S15) |
| 3 | **Rail** | **Book a standing rail floor a month ahead** for base load (cheaper ~25%); road for flex; trailer-express only for urgent splits | "Road has always sufficed" → port jam/congestion with 0% cover; 0 rail slots despite alerts on 12 lanes | Mode-mix judgment (S14 Q4.1); insurance logic |
| 4 | **Mode mix under a shock** | **Split the shipment** — urgent part by trailer-express now, the rest by rail as backfill | Holding, cancelling, or one-mode rerouting | S14 Class Q 4.1 |
| 5 | **Distribution parameters** | Set **per-zone** service floors and cost weights; protect the high-margin zone; MIX once tech ≥ 3 | Identical cost weights → solver routes everything by cheap slow rail and the premium zone's fill slips | S15 Class Q 5.1 |
| 6 | **Chip contract** | Contract volume to **real** production need with clauses specified before signing | Over-booking (fees on the full book) or under-booking (allocation cut → forced production cut, as in Kaveri M4) | S16 clause-stakes; Pactum mandate |
| 7 | **Pricing** | Don't cut price to fix a placement problem; restore toward list when the constraint is distribution | Kaveri cut prices in M3–M4 and never restored them → ≈₹1.5 cr/month given away while lost sales kept rising | Diagnose the binding constraint |
| 8 | **Tokens (attention)** | Budget 24 tokens: keep the **2-token monthly plan**, upkeep, and ≤ 4 transformation actions; tune or retire agents on **value per decision** | Running out of attention in R10 (B13, A3); agents queued but never operated | S17 tune-or-retire |
| 9 | **Autonomy level** | **L2 specialist first, L3 as an upgrade**; L4 only with evidence; never L5 below gate | "Fully autonomous cross-channel repricing (L5 closed loop)" commissioned below gate on a board that cannot place stock | Autonomy ladder (S4) |
| 10 | **Forecasting** | Distribution forecasts; buy the tier you can run; track error/bias (the one Kaveri agent that worked) | Buying sensing before the signal desk exists | S8, S11, S12 |
| 11 | **Coordination** | Every agent sees the **same end-customer demand**; smooth orders; one owner per call | Reacting to each other's orders → bullwhip (Command Your Agent finale) | S19 |
| 12 | **Governance & trust** | Build the resilience/governance estate; disclose incidents; step autonomy down when a guardrail fires | Guardrail breach (B18's Scheduling agent); zero governance estate (B20's trust 78) | S20 ACAP; value = profit × reputation × trust |
| 13 | **Insurance / hazard cover** | Buy cover on hazards the calendar signals (port, congestion) when the expected loss exceeds the premium | 0% cover → full ₹60 L hit + trust loss | "Argues insurance logic backwards" |
| 14 | **Reporting** | Report outcomes (fill, lost sales, cash), not activity (tokens spent, levels reached, agents built) | Kaveri's memo: "six capabilities built or building" while fill fell five months | Claim audit (S1) |

---

## 5. The Kaveri pattern — diagnosing a sick board in five checks
Use these on any Chain Reaction-style exhibit:
1. **Fill vs stock:** is fill falling while finished stock rises? → **placement failure** (zones pull only from their own RDC). Kaveri: fill 86 → 58% while RDC stock 226 → 662.
2. **Auto-push count:** any cars "unrouted, default lane"? → no plan-of-record. Kaveri: 273–479 every month.
3. **Rail slots booked:** zero? → road-only network exposed to congestion; paying ~25% more than needed.
4. **Below-gate builds:** which live/in-build agents are under their D·P·T gate or missing prerequisites? → full cost, fraction of effect.
5. **Profit drivers:** did profit improve because operations improved, or because production was cut (chip allocation) or prices were cut? → don't let a cherry-picked month pass as recovery.

Then compute the **contribution forgone** (lost sales × mix × (price − unit cost)) and compare it with the visible charges — the hidden number is almost always the bigger one (Kaveri: ₹11.0 cr vs ₹60 L).

---

## 6. Practice questions on the simulation (with answers)
**Q1. Your West RDC has full HATCH stock but the Mumbai zone is about to stock out; the only road lane between them just lost 40% capacity; trailer-express is open but costly; rail has slots but a two-day lead time you don't have. What do you do?**
Split the shipment: send the urgent portion by trailer-express now to protect the zone at highest stockout risk, and backfill the remainder by rail. Under a capacity shock the answer is rarely "pick one mode" — it is rebalancing the mode mix in real time (S14 Class Q 4.1 📘).

**Q2. Under time pressure a team sets identical cost weights for every zone; the solver routes nearly everything by rail and the zone driving 40% of premium-margin sales slips badly. What went wrong?**
The mandate, not the solver: they should have set a higher cost weight or a service floor for the high-value zone before solving. "A perfectly solved LP with the wrong mandate produces a perfectly wrong plan" (S15 Class Q 5.1 📘).

**Q3. A negotiation agent's run cost doubles after a platform reprice, but its output quality is unchanged. You have 90 seconds.**
Compare value-per-decision with cost-per-decision, then tune (shorter context, caching, cheaper tier, fewer calls) or retire. A price shock is a signal to re-run the math, not a verdict (S17 Class Q 7.1 📘).

**Q4. Your GenAI scenario tool says a celebrity post will spike one paint colour 400% in 72 hours; a teammate wants to fund paint-shop flex capacity now.**
Label it "stretch", check for a real mechanism and base rate, then look for a cheap reversible mitigation. Vividness is not evidence (S18 Class Q 8.1 📘).

**Q5. One agent orders 15% extra "to be safe"; two tiers up another agent doubles its order in reaction. What single change prevents the amplification?**
Give every agent the same real end-customer demand signal instead of each other's orders — coordination beats speed (S19 Class Q 9.1 📘).

**Q6. Your L4 forecasting agent has quietly beaten the manual process, but two weeks before the board review you find its training data under-represents your fastest-growing region and has skewed allocation for months.**
Drop it to L2, disclose the bias and its likely impact in the incident log, and take both to the board as a governance finding. Guardrails only count if you use them when it costs you something (S20 Class Q 10.1 📘).

**Q7. Your model flags a press bearing at 68% failure probability; your weekly inspect-and-replace protocol already catches this wear.**
Don't act on the flag — it does not change the decision or its timing; the prediction is informationally idle (S13 Class Q 3.1 📘). Fund telemetry only where it changes a decision.

**Q8. 60 SKUs, 4 dealerships, one Excel analyst, lenders need a plain auditable rationale; a vendor shows an LSTM platform. Which tier?**
The spreadsheet/smoothing tier — it matches volume, skills and audit needs; the LSTM needs data maturity 3+ and produces the opaque output lenders don't want (S12 Class Q 2.1 📘).

**Q9. Kaveri's board asks whether to terminate the below-gate repricing agent (7 tokens sunk, 45% odds) or let it land. What reasoning applies?**
Sunk cost is irrelevant: compare the remaining cost (termination 2 tokens vs upkeep plus the risk of an L5 closed-loop pricing agent running at a fraction of effect without its Price-Setting prerequisite) with expected value. With placement the binding constraint and prices already cut, the expected value of autonomous repricing is low; terminating is defensible under a cash-stabilisation mandate, but if you choose the distribution initiative you accept its upkeep for two months and re-decide at the gate.

**Q10. Which is the better predictor of final rank: number of agents built or operating discipline? Give evidence.**
Operating discipline. #3 (A8) ran six agents and #12 (B20) one agent, while four estates of 12–13 agents finished 15th–18th; the champion won on breadth **plus** governance (trust 110), and A7 lost by 1.1 points with zero below-gate builds. Size never predicted rank on its own; booking rail, filing a distribution plan and sizing the chip book did 📘.
