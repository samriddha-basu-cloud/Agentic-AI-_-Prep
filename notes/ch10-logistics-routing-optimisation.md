# Ch 10 — Logistics, Routing & Optimisation: The Mandate Is the Lesson (Sessions 14–15)
**Syllabus unit 6 📘:** *AI in Logistics: Route Optimization, Vehicle Scheduling — tools: Google OR-Tools, OptaPlanner, Q-learning-based routing.*
**Session 14 📘:** "Routing, Rerouting, Reality: Why a Network Needs a Brain." It led into **Round 4: The Network Opens**.
**Session 15 📘:** "Optimization in Practice: The Mandate Is the Lesson." It covered min-cost flow and the AI–OR symbiosis, and led into **Round 5: Setting the Mandate**.

> **Exam use:** this is the heart of the **Kaveri Motors** paper and of the Chain Reaction emphasis. Four habits answer almost every logistics question.
> (1) The decision object is the **mode mix under capacity**, not "the best route".
> (2) Under a shock, **split the shipment** (urgent part fast, bulk cheap).
> (3) The solver does exactly what you tell it: **strategy lives in the objective function** (service floors, cost weights).
> (4) **Agents operate optimisers, they don't replace them**: write the **Mandate Card**.

---

## 1. The network in the game (and in Kaveri) ⭐⭐⭐
- **3 plants → 4 RDCs → 7 dealer zones**, with three products (HATCH, SUV, EV) and three transport modes.
- There are more feasible flow patterns than any planner could compare by hand in time, so **nobody hands the network a lane-by-lane plan**. You set **coverage, safety stock, front-loading and rail eligibility**, and the engine builds the flows.

| Mode | Cost | Speed | Constraint | Use |
|---|---|---|---|---|
| **Rail** | cheapest (**≈25% below road** in the game) | slow (multi-day lead) | **slot-constrained; booked a month ahead; charged whether used or not** | stable, predictable base volume |
| **Road** | mid | flexible | lane capacity (shocks cut it) | **the default workhorse; the lane the engine auto-pushes** |
| **Trailer-express** | most expensive | fastest | capacity-limited | urgent, high-value, stockout-risk volume |

**Distribution dials:**
- **distCover:** cover target, i.e. how many days or weeks of demand to position at the RDCs and zones.
- **distSafety:** the safety buffer on top of cover.
- **distFront:** **SPREAD** distributes evenly; **FRONT** front-loads the stock early.
- **distMode:** **ROAD** (all road), or **MIX** (rail in the mix). **MIX stays locked until tech maturity 3.**

## 2. What AI adds to moving things ⭐⭐⭐
- **Classical dispatch optimises a snapshot:** fixed lead times, average demand, one route plan. It is followed until it visibly breaks, with **no correction mid-transit**.
- **AI-driven logistics:**
  - **re-routes dynamically**;
  - **predicts delays early** (ETA models on traffic, weather, port congestion);
  - lets **fleets self-coordinate locally**.
  - It changes the **speed and granularity** of the mode trade-off (every lane, every hour, not weekly), and **it matters most when something breaks**.
- **Every shipment is still a mode choice under capacity and cost tension.**

### Class Q 4.1 (S14) — the capacity shock ⭐⭐⭐
The situation:
- road lane capacity is −40%;
- West RDC has full HATCH stock;
- the Mumbai zone is about to stock out;
- trailer-express is open but costly;
- rail has slots but a 2-day lead time you don't have.

**Answer: B, split the shipment.** Send part via trailer-express now and the remainder via rail as backfill.
- The urgent portion protects service where the stockout risk is highest.
- The bulk of the cost shifts to the cheaper, slower mode.
- *Under a capacity shock the right answer is rarely "pick one mode"; it is rebalancing the mix in real time.*

**Numeric version (exam style).** Mumbai needs 300 cars. 120 are needed within 2 days (stockout risk) and the other 180 can wait 5 days.
- Express costs ₹9,000 per car, road ₹4,000 and rail ₹3,000.
- Road capacity has fallen to 60% of its normal 200, i.e. 120 cars.
- All by express = 300 × 9,000 = **₹27 L**.
- Split: 120 by express = ₹10.8 L, plus 180 by rail = ₹5.4 L, so **₹16.2 L**, saving **₹10.8 L (40%)** with no stockout.
- Alternatively, 120 by road (if road can reach in 2 days) = ₹4.8 L, plus 180 by rail = ₹5.4 L, so **₹10.2 L**.
- Always check timing feasibility against each mode's lead time.

## 3. Agents operate the model, they don't replace it ⭐⭐⭐
- **Core course idea:** agents don't think instead of you. They **operate optimisation models on your behalf**, at a speed and scale you can't match by hand.
- The flow-optimisation model solves the plants → RDCs → zones allocation in seconds. It needs **two things only a human should set**:
  - **service targets** (which zones can't stock out);
  - **cost weights** (transport cost vs a rupee of lost sales).
- **You set policy; the engine executes at scale.** By hand it is combinatorial, error-prone work that humans do badly under pressure.

### Practice: JD.com's dual engine and Amazon DeepFleet ⭐⭐⭐
- **JD.com:**
  - An **AI sensing layer** continuously senses demand and network conditions.
  - It sits on top of a **classical optimisation engine** that solves routing and inventory placement across the national network.
  - **The AI decides when and how to re-trigger the optimiser** and translates shifting priorities into its objective; the optimiser does the constrained math.
  - "Keep the AI pointed at the right target, and make sure the AI itself has the right target."
- **Amazon DeepFleet:** thousands of warehouse robots **re-route around each other in real time**, inside a physical and algorithmic **envelope**, not a fixed central schedule. This is self-coordination.

## 4. What a min-cost-flow optimiser actually does ⭐⭐⭐
- **Nodes** are plants, RDCs and zones. **Edges** are lanes, each with a **capacity** and a **cost per unit**.
- The optimiser finds the **lowest-cost flow on every edge that meets demand, given the constraints**.
- In LP form:
  - **Minimise Σ cᵢⱼ xᵢⱼ**
  - subject to flow balance at each node (supply out = flow in, RDC in = out + stock change, zone in ≥ demand or the service floor);
  - capacities **xᵢⱼ ≤ uᵢⱼ**;
  - **xᵢⱼ ≥ 0**.
- Lost sales can be modelled as a costly "dummy lane" whose **cost weight = margin lost per car**. That is how the cost weight decides whether the solver protects a zone.
- **The solver doesn't get tired or anchor, but it can't decide whether a zone deserves 98% or 90% service.** That call is yours.

**Worked mini-example.** Plant P (supply 500) serves zones Z1 (demand 300, premium margin ₹1.2 L/car) and Z2 (demand 300, margin ₹0.4 L/car).
- Lane costs: P→Z1 rail ₹3k (capacity 150) and road ₹4k (capacity 200); P→Z2 rail ₹3k (capacity 300).
- **Pure cost-minimising** with zero shortage penalty ships the cheapest lanes first: rail 300 to Z2 and rail 150 to Z1, i.e. 450 cars. Z1 gets 150 of 300 (**50% fill**) and the 50 spare go wherever.
- Add a **shortage cost weight = margin** (₹1.2 L for Z1, ₹0.4 L for Z2). The solver now fills Z1 fully (rail 150 + road 150) and sends the remaining 200 to Z2.
- The extra transport cost is about ₹0.15 L for the road leg vs ₹1.2 L × 150 = **₹180 L** of premium margin protected.
- **Strategy lives in the objective function.**

### Class Q 5.1 (S15) — identical cost weights, the premium zone starved ⭐⭐⭐
Every zone was given the same cost weight. The solver routes nearly everything by rail, and fill slips in the zone that drives **40% of premium-margin sales**. The plan was approved without override.
**Answer: B, set a higher cost weight (or a service floor) for the high-value zone before solving.**
- The solver did exactly what it was told. The output is **technically optimal and strategically wrong**.
- The fix belongs **upstream, in the objective and constraints**, not in lane-by-lane second-guessing (C).
- *"A perfectly solved LP with the wrong mandate produces a perfectly wrong plan."*

## 5. The AI–OR symbiosis ⭐⭐⭐
- **A classical solver is static.** Give it a network, objective and constraints, and it returns one answer for one snapshot.
- **An agent wrapped around the solver adds the judgement layer:**
  - it watches for **re-solve triggers**;
  - it **translates goals** ("protect service in our top-margin zone") into **LP weights and constraints**;
  - it decides what happens to the plan: the **L2 / L3 / L4** call between human review and autonomous execution.
- **None of this replaces the solver's math.** What changes is *who decides when to invoke it, what to optimise for and how much autonomy it gets*.
- **Hand-planning fails at scale because of combinatorics, not because humans can't do math.**

## 6. Tools named in the syllabus 📘
| Tool | What it is | Typical use |
|---|---|---|
| **Google OR-Tools** | open-source optimisation suite (LP/MIP, CP-SAT constraint solver, **vehicle routing (VRP) solver**, network-flow algorithms including min-cost flow) | vehicle routing with time windows and capacities, min-cost-flow allocation, scheduling |
| **OptaPlanner** (now Timefold) | open-source Java **constraint-satisfaction / planning engine** using metaheuristics (tabu search, simulated annealing, late acceptance) with hard and soft constraint scores | shift rostering, vehicle routing, job-shop scheduling, where **hard constraints must hold and soft ones are traded** |
| **Q-learning for routing** | RL agent learns Q(state = current node and conditions, action = next hop) from the reward (−travel time, −cost); adapts as congestion changes | dynamic rerouting in changing networks (packet routing, fleet dispatch), warehouse robots |
| **LP/MIP solvers** | exact optimisers behind min-cost flow | network allocation (Chain Reaction's engine) |

**VRP in one line:** visit all customers with a fleet of capacity-limited vehicles, minimising distance or cost, subject to time windows. It is **NP-hard**, so solvers use heuristics plus local search. OR-Tools and OptaPlanner are the two names the syllabus wants you to recognise.

**Q-learning update:**
**Q(s,a) ← Q(s,a) + α [r + γ · maxₐ′ Q(s′,a′) − Q(s,a)]**
- α is the learning rate and γ the discount.
- Mini numeric: Q(s,a) = 10, α = 0.5, r = −4, γ = 0.9, max Q(s′) = 12 → new Q = 10 + 0.5 × (−4 + 10.8 − 10) = 10 + 0.5 × (−3.2) = **8.4**.

## 7. The Mandate Card ⭐⭐⭐ (framework, S14)
Set these before you hand flow to any agent:
1. **Service floor:** name the zones and segments where a stockout is unacceptable and must be protected first.
2. **Cost ceiling:** the maximum acceptable cost per unit delivered, by mode.
3. **Mode priority:** the default cost-vs-speed preference, so the agent has a tiebreaker.
4. **Shock trigger:** what capacity or demand shift forces a **full re-plan** versus a **local patch**.
5. **Review cadence:** how often a human re-checks the agent's flow allocation against outcomes.

## 8. The Optimizer Mandate Checklist ⭐⭐⭐ (framework, S15)
1. **Service targets:** set **per zone**, not one network-wide number. Name which zones can't slip and by how much.
2. **Cost weights:** reflect **strategic priority, not just unit economics**. A high-margin zone shouldn't get the same weight as a cheap-to-serve one.
3. **Review rule:** decide up front between **human sign-off (L2)**, **exception-based escalation (L3)** and **fully autonomous (L4)**.
4. **Re-solve trigger:** name the specific events (cost shock, capacity loss, demand spike) that force a re-plan.
5. **Verify the fit:** check the returned plan against the service floor **before it executes**. Optimal is not automatically right.

### Applying the mandate to Kaveri Motors (the PYQ) ⭐⭐⭐
See the [Kaveri Motors solution](#/pyq-kaveri) for the full answer. In short:
- Kaveri's loss was **physics, not luck**. Road-only, uniformly weighted flows starved the premium zones under a lane shock, and the congestion charge was the visible cost of an invisible **₹11 cr contribution forgone**.
- The fix is a **Distribution Planning Agent at L3** under a written mandate:
  - service floors by zone (zone fill ≥ 60–75%);
  - a cash constraint;
  - a **rail floor (MIX)** once tech maturity allows;
  - re-solve triggers (>20% lane capacity loss, zone fill < 60%, expedite > ₹20 L);
  - a CSCO owner and a monthly review.

## 9. Chain Reaction link — Rounds 4 & 5 ⭐⭐⭐
- **R4, the network opens:** you do not fill a single flow cell. Distribution is set by **distCover, distSafety, distFront (SPREAD/FRONT) and distMode (ROAD/MIX; MIX locked until tech maturity 3)**, and the engine generates the plan. A basic network agent becomes deployable.
- **R5, setting the mandate:** the four dials **are** the objective and the policy the solver executes. Set them, read the generated plan back, and see whether your mandate survives contact with the month.
- **Winning moves:**
  - raise tech maturity early so **MIX (rail)** unlocks and cost falls by about 25% on base volume;
  - book rail for **predictable base load only**, because unused slots are still charged;
  - keep road and express for the variable tail;
  - use **FRONT** before known peaks and **SPREAD** in steady months;
  - set **distSafety** by zone value, not uniformly.
  - See the [Chain Reaction playbook](#/chain-reaction-playbook).

## Key takeaways (S14–S15 recaps 📘)
1. AI in logistics wins by **re-evaluating mode and route trade-offs continuously**, not by picking one smart route.
2. The real decision object is the **mode mix under capacity** (rail, road, trailer-express), not a single "best path".
3. Agents **operate** optimisation models; they don't replace the human-set mandate of service targets and cost weights.
4. A min-cost-flow LP finds the best flow **for the objective you gave it**, nothing more and nothing less.
5. Hand-planning fails at scale because of **combinatorics**, not maths ability.
6. **The mandate (service targets, cost weights, review rule, re-solve trigger) is the real decision.** AI operates OR: it decides when to re-solve and what to optimise for.

---

## Self-test
**Q1. "The optimiser produced the lowest-cost plan, so it must be right." Respond.**
Lowest cost **for the objective given**. With identical cost weights and no service floors, the solver will happily starve a premium zone. Check the plan against service floors, and put zone priority into the cost weights or constraints before solving.

**Q2. Write the five items of a Mandate Card for a 3-RDC FMCG network entering the festival season.**
- Service floor: metro zones ≥ 97% fill.
- Cost ceiling: ₹/case by mode.
- Mode priority: road default, express only for stockout-risk SKUs.
- Shock trigger: >20% lane capacity loss or a demand spike >30% → full re-plan; otherwise local patch.
- Review: weekly human review of fill by zone vs cost.

**Q3. Why is rail "charged whether used or not" a design consideration?**
Rail is a commitment booked a month ahead. Over-booking turns into fixed cost for empty slots, so book rail for the predictable base load and leave the variable tail on road or express.

**Q4. Distinguish OR-Tools and OptaPlanner.**
OR-Tools: Google's suite of LP/MIP, CP-SAT, VRP and network-flow solvers. OptaPlanner: a Java constraint-satisfaction engine using metaheuristics with hard and soft scores, strong in rostering and scheduling. Both are solvers that an agent can operate.

**Q5. What does the agent add on top of the solver (the AI–OR symbiosis)?**
Sensing when to re-solve (triggers), translating business goals into weights and constraints, and governing what happens to the output (L2 review, L3 exceptions, L4 autonomous).

**Q6. In a shock, why split rather than pick one mode?**
Different parts of the order have different urgency and value. Express protects the stockout-risk slice, and rail/road carries the rest cheaply. One mode either overspends (all express) or loses sales (all rail).
