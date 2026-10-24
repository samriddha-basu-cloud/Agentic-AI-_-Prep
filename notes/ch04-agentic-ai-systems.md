# Ch 4 — Agentic AI Systems & Smart Agents (Session 4)
**Session 4 📘:** "Inside the agent: architectures, autonomy levels, multi-agent coordination — and the deployments already negotiating, routing and replenishing." Opening case: **Vantage Logistics — Which Pilot Do You Scale?** (routing agent 14% gain with driver-safety concerns; picking robots 18% gain with a hardware backlog; delay rebooking 6% gain with the highest satisfaction).

> **Exam use:** the **autonomy ladder L1–L5**, the **agentic suitability screen**, the **governance stack** ("guardrails live outside the model") and the **mandate/envelope** idea are demanded in every Section B ("starting autonomy level, justified", "escalation trigger", "named owner"). This is the most-quoted chapter in both model answers.

---

## 1. Five generations of "automation" ⭐⭐
| # | Generation | What it does | Human role |
|---|---|---|---|
| 1 | **Scripts & macros** | fixed keystroke replay; breaks when anything changes | builds and fixes |
| 2 | **RPA** | rule-based bots on structured digital tasks — PO creation, invoice matching, compliance checks | designs rules |
| 3 | **ML-assisted** | predictions embedded in workflows — risk scores, forecasts, anomaly flags | **decides** |
| 4 | **GenAI copilots** | conversational assistance, drafting, summarising, what-if querying | **initiates every action** |
| 5 | **Agentic AI** | goal-directed systems that **perceive, plan, act through tools, and learn** with minimal intervention, inside guardrails | governs the envelope |
**The step-change at stage 5: the system OWNS a goal and a decision loop, not just a task** — which is why it demands the readiness of Sessions 2–3.

**Agent-washing detection ⭐⭐⭐ (Class Q 4.1):** "Our AI agent reviews your inventory dashboard every morning and emails your planner a prioritised action list" → **not an agent — it only recommends; nothing is executed.** Test: **goal ownership + tool-mediated action within an envelope.** Naming discipline matters commercially: agent-grade governance costs money — don't pay copilot problems with agent budgets (or vice versa).

## 2. Inside an agent — six building blocks ⭐⭐
| Block | Function | Enterprise reality |
|---|---|---|
| **SENSE · Perception** | interfaces to the world | ERP/WMS/TMS records, IoT telemetry, EDI, email, market feeds — "sensing is mostly reading systems of record" |
| **THINK · Reasoning engine** | decides what to do next | typically an LLM with **ReAct** (reason + act) and chain-of-thought |
| **THINK · Planning** | decomposes goals into steps | sequences tool calls; replans when observations contradict expectations |
| **REMEMBER · Memory** | short- and long-term | context window + vector DBs, **RAG** over policies and history |
| **ACT · Tool use** | the agent's hands | APIs, databases, **optimisation solvers**, web search, code — standardised via **MCP** |
| **GOVERN · Guardrails & orchestration** | bounds and coordination | permissions, spend limits, policy checks, escalation, audit logs; orchestration across agents and humans |

## 3. Design patterns 📘
- **Reflection** — the agent critiques and revises its output before acting (cheap accuracy, slower cycles).
- **Tool use** — math to solvers, facts to databases, execution to APIs; "the LLM routes and interprets rather than computes".
- **Planning / orchestrator–worker** — a planner decomposes the goal and dispatches specialists (data-pull, forecast, negotiation agents).
- **Multi-agent collaboration** — peer agents with distinct roles negotiate or vote (mirrors S&OP teams).
- **Human-in-the-loop vs on-the-loop** — IN: approves each consequential action; ON: monitors exceptions while the agent executes. Chosen **per decision class** by the autonomy ladder.
**Lineage:** multi-agent supply chains were proposed in **1998** (Swaminathan, Smith & Sadeh) — "a sci-fi world at that time; the future is here". LLMs supplied cheap, linguistically competent agents that read contracts and talk to planners.

## 4. Agents in the field ⭐⭐⭐
### Physical — warehouse autonomy (Amazon, JD.com, BMW)
Amazon's newest FCs (MQY1, SHV1) run AI-coordinated robots moving inventory pods and optimising human–robot collaboration; **DeepFleet (2025)** — a generative foundation model that plans, learns and orchestrates **1M+ robots**, "an intelligent traffic-management system" (10% travel-time gain). **JD.com** runs some of the world's most automated FCs (sort, pack, move with minimal humans). **BMW × Figure AI** humanoids for materials retrieval and machine tending. Researchers call this "**smart execution of work**".

### Transactional — Walmart × Pactum autonomous negotiation ⭐⭐⭐
Walmart hands **tail-spend** negotiations to Pactum's AI: the agent emails/chats with suppliers, negotiates **payment terms, discounts and clauses** against a **mandate set by category managers**, and closes agreements without human involvement.
- **Why tail spend?** Thousands of suppliers Walmart could never negotiate with individually — the agent negotiates with **all** of them in parallel.
- **The mandate (walk-away points, tradable levers) is the guardrail**; the agent optimises within it.
- **Results:** **~3% average savings**; **64–68% close rate** (vs a 20% pilot target); **~11-day turnaround**; **35-day average payment-term extension**; **83%** of suppliers found it easy, ~¾ preferred negotiating with the bot. Maersk runs similar deployments.
- **Class Q 4.2:** the agent closes deals with 2,400 tail suppliers inside mandates → the manager's job is now **designing the envelope and auditing outcomes** — not reviewing every deal (that would delete the economics). "**The mandate IS the management.**"

### The wider agentic portfolio 📘
Walmart **Trend-to-Product** (lead times −18 weeks) · **ThredUp** recommerce classification and matching · **IBM Food Trust** — freshness indices on blockchain trigger automated payments ("blockchain newsvendor" — automating contract **enforcement**) · **predictive 3D printing** of spares triggered by IoT condition · **adaptive pricing & ordering** (DDPO) for perishables under non-stationarity.
**Market:** agentic AI in SC & logistics **$8.7B (2025) → ~$16.8B (2030)**; **40%** of enterprise apps to embed task-specific agents by end-2026 (from <5%); agentic and physical AI top Gartner's 2026 trends; McKinsey: **$2.6–4.4T** annual value potential.

### Plumbing — protocols and platforms 📘
**Model Context Protocol (MCP)** — open standard connecting AI to tools/data ("the USB port of agent tool use"); **agent-to-agent (A2A)** standards for cross-vendor negotiation; enterprise agent platforms (Microsoft Dynamics 365 agents & Copilot Studio, AWS Bedrock AgentCore, SAP Joule agents across Ariba/Fieldglass, GA June 2026). **Microsoft's Supplier Communications Agent** handles order confirmations, schedule changes and document requests — an **L3–L4 agent shipped as product**. "Protocol choices are supply chain design choices now."

### Radical decentralisation, revisited
The pieces exist (LLM reasoning, MCP, per-agent identity, orchestration — Pactum and DeepFleet are L4 fragments). **Still missing:** cross-enterprise incentive agreements, system-level stability guarantees, accountability law, organisations restructured around exceptions. "The gradient from L1 to L5 is where strategy lives for the next decade."

## 5. The problems agents create ⭐⭐
- **Agent-washing** — copilots and RPA sold as agents (a leading driver of the predicted 40% cancellations).
- **Unearned autonomy** — L4 granted on demo evidence; the overridden cases where humans were quietly catching expensive errors are discovered only after the humans are gone.
- **Interaction instability** — excellent agents amplifying each other into machine-speed oscillation (bullwhip at silicon speed).
- **Unbounded commitments** — agents whose words legally bind the firm, governed only by prompt-level politeness.

### The agentic cautionary file (2023–25) ⭐⭐⭐
| Case | What happened | Lesson |
|---|---|---|
| **Air Canada chatbot (2024)** — LIABILITY | a tribunal held the airline liable after its chatbot **invented a bereavement-fare policy**, rejecting the argument that the bot was "a separate legal entity" | the agent's word binds the firm — **grounding and envelopes are legal controls** |
| **The $1 Chevy Tahoe (2023)** — INJECTION | a dealership chatbot was **prompt-injected** into "agreeing" to sell a ~$76,000 SUV for $1 ("no takesies backsies") | instructions in prompts are suggestions — **hard limits must live outside the model** |
| **McDonald's AI drive-thru (2021–24)** — EXIT GATE | after a 100+ restaurant pilot, ended following viral order errors (bacon on ice cream; 260 nuggets) | the positive lesson: **bounded rollout, honest feedback and a working exit gate** |

## 6. The research frontier — agent behaviour ⭐⭐⭐
- **LLM agents can AMPLIFY bullwhip** — beer-game experiments (2024–26): in decentralised settings most LLM agents create **more** order instability than simple baseline policies.
- **Structure stabilises, intelligence does not** — a centralised orchestrator or communication constraints restore stability; **multi-agent learning with trained coordination** beats single agents on cost AND produces less bullwhip.
- **Consensus-seeking agents** (2025) automate routine inter-company coordination and lower SME entry barriers.
- **Institutional governance** — WEF "AI Agents in Action" (2026) introduces **ACAP**, a per-agent capability & authorisation profile.
**The design law: stability is a property of MECHANISM DESIGN — shared signals, constraints, orchestration — not of agent intelligence. "Smarter agents without structure fail faster."** **Class Q 4.4:** your replenishment agent and your distributor's ordering agent react to each other → **order oscillation, unless signals are shared**.

## 7. The Five-Level Autonomy Ladder ⭐⭐⭐
| Level | Agent does | Human does | SCM example |
|---|---|---|---|
| **L1 · Assist** | retrieves, summarises, drafts | decides and acts | copilot drafts a supplier email; planner edits and sends |
| **L2 · Recommend** | analyses, proposes ranked actions | approves each action | reorder proposals with reasons; planner clicks approve |
| **L3 · Act with approval gates** | executes routine cases end-to-end | approves exceptions & thresholds | **auto-PO under ₹5 L within contract; above → human** |
| **L4 · Bounded autonomy** | owns the decision inside an envelope | monitors, audits, tunes the envelope | **Pactum negotiations inside mandate; DeepFleet routing** |
| **L5 · Self-improving** | learns, adapts policy, coordinates peers | governs goals, ethics, kill switch | autonomous planning networks (**mostly aspirational, 2026**) |
"Autonomy is a managerial choice **per decision class**: climb the ladder **on evidence**, capped by **readiness and blast radius**."
*Chain Reaction rule:* "**L2 specialist first, L3 only as an upgrade on top of it**" (S13 round brief 📘). *Kaveri trap:* an **L5 closed-loop repricing agent commissioned below gate** on a board that could not place its stock.

## 8. The governance stack ⭐⭐⭐
1. **Hard constraints** — spend limits, approved-supplier lists, contract envelopes, rate limits, forbidden actions — **enforced OUTSIDE the model, in code and permissions, not in the prompt**.
2. **Identity & least privilege** — each agent its own credentials scoped to the minimum ("an agent with tool access is an attack vector with a budget" — prompt-injection defence).
3. **Observability** — decision traces, action logs, explanation on demand, override mechanisms — "AI should enhance, not obscure, accountability".
4. **Escalation & kill switch** — confidence and anomaly thresholds route to humans; every autonomous loop has a documented stop.
5. **Accountability assignment** — **name the human owner** of every agent's outcomes **before** go-live.
**Risk registers:** agentic ecosystems risk loss of oversight, emergent systemic failures, accountability gaps; agents in fragile processes add unpredictability. "**Governance is the product, not the paperwork.**"
**Class Q 4.3 ⭐⭐⭐:** a system prompt says "Never exceed ₹5 lakh per order. Never order from unapproved suppliers." Sufficient? → **No — prompts alone are not enforceable controls.** "The prompt shapes behaviour; the envelope bounds it." "**Guardrails live outside the model.**"

## 9. The Agentic Suitability Screen ⭐⭐⭐
| Factor | Ask |
|---|---|
| **Frequency & volume** | high-frequency, high-volume decisions amortise agent investment; rare ones do not |
| **Reversibility** | can a wrong action be undone cheaply? low blast radius → more autonomy |
| **Data & feedback** | rich state visibility and **fast** outcome feedback (agents learn only when the loop closes quickly) |
| **Rule clarity** | can the mandate be specified (limits, levers, walk-aways)? "If experts cannot state the envelope, the agent cannot inherit it" |
| **Stakes & politics** | strategic, irreversible, politically loaded decisions stay human |
**Score 1–5 each: 20+ = strong candidate (start L3–L4); 12–19 = augment (L1–L2); < 12 = keep human, revisit later.**
**Class Q 4.5:** (a) strategic supplier partnership negotiations, (b) tail-spend reorder of consumables, (c) dynamic robot routing in your own warehouse → **c > b > a** — reproducing the industry sequence: **physical autonomy first, transactional next, strategic never (so far)**.

*Vantage Logistics resolved:* the **delay-rebooking pilot** (6% gain, highest satisfaction) is often the safest to scale — low blast radius, reversible, users like it — while the routing agent's driver-safety issue was **absent from its objective** (agents fail on what their objective omits) and the picking robots are constrained by hardware. Before promoting any pilot to autonomy, demand: the overridden cases, error costs in both directions, the omitted objectives, and a frozen baseline.

## 10. Intelligence vs automation — which do you need? 📘
Automation repeats; intelligence learns (the 1939 exhibition robot blew up balloons on cue but could not decide when). Most "AI" is automation in disguise — RPA copies steps "like a tape recorder". **Automated vs intuitive:** automate where history is rich and rules stable; keep humans where data is thin (in the March-2020 shock data-starved AI faltered and human intuition took over). Ask first: does this task need intelligence, or will disciplined automation do?

## 11. Human-in-the-loop by design ⭐⭐
- **Confidence thresholds gate autonomy** — the agent acts alone above the line and hands off below it.
- **Escalation is architecture** — a production assistant routes low-confidence cases to a person by design.
- **Guide rails** for off-topic asks; route by **tone** as well as words; design for the **80% rule** (agent handles ~80%, humans fill the gaps; reliance on humans falls as it learns from logs).
- "AI = **augmented** intelligence."
**Class Q 4.6:** an "autonomous" returns agent — keep a human **on low-confidence, high-impact cases only**.

## Key takeaways (S4 recap 📘)
1. Agentic AI = goal ownership + a perceive–reason–plan–act loop with tools and memory; name agent-washing.
2. Architecture is composable: reflection, tool use, orchestrator–worker, multi-agent — with OR solvers as power tools, not replacements.
3. Field evidence is sequenced: physical autonomy (DeepFleet, JD.com) → transactional (Pactum) → planning (mostly aspirational).
4. Autonomy is a managerial choice per decision class — climb the ladder on evidence, capped by readiness and blast radius.
5. Governance is engineering: hard constraints outside the model, per-agent identity, observability, kill switches, a named owner.

---

## Self-test
**Q1. Write the starting autonomy level for a tail-spend negotiation agent at a firm whose vendor master was just cleaned, and justify it in one line.**
L3 — it closes routine deals under ₹5 L inside the category-manager mandate and escalates the rest; the decision is reversible and low-value, but there is no track record yet, so L4 must be earned with gate evidence.

**Q2. Your agent's prompt says "never order from unapproved suppliers". The CISO is unhappy. Why, and what do you add?**
Prompts are not enforceable (injection, model updates, edge cases). Add an approved-supplier allow-list and spend caps enforced in code, per-agent credentials with least privilege, full action logs and a kill switch.

**Q3. Score robot routing in your own warehouse on the suitability screen.**
Frequency 5, reversibility 4, data/feedback 5, rule clarity 4, stakes 5 (low) = 23 → strong candidate, start L3–L4 (DeepFleet operates at L4).

**Q4. Two individually excellent agents — yours and your distributor's — start reacting to each other's orders. Predict and prevent.**
Order oscillation (machine-speed bullwhip). Prevent with a shared end-customer demand signal, order smoothing/rate limits, or an orchestrator — stability is mechanism design.

**Q5. What did Air Canada, the $1 Tahoe and McDonald's each teach?**
Air Canada: the bot's words bind the firm (ground it, bound it). Tahoe: prompt injection beats prompt instructions — hard limits outside the model. McDonald's: bounded pilots with an honest exit gate are a success, not a failure.
