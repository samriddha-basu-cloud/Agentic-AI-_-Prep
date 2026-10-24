# Ch 11 — NLP for Procurement & Token Economics (Sessions 16–17)
**Syllabus unit 7 📘:** *NLP for Procurement Automation and Contract Analytics — HuggingFace, OpenAI API for auto-RFx generation, compliance monitoring.*
**Session 16 📘:** "NLP for Procurement: Reading the Fine Print at Scale." It led into **Round 6: The Chip Contract Negotiation**.
**Session 17 📘:** "APIs & Token Economics: The Bill Behind the Brain." It led into **Round 7: The Token Economy**.

> **Exam use:** two rules carry this unit.
> (1) **The accuracy bar scales with what the clause decides.** Liability and penalty clauses get domain-tuned models and a human; contact fields get a general model.
> (2) **Tune before you retire.** Compare value-per-decision with cost-per-decision, never the size of the bill alone, and enforce **spend caps in code, not in prompts**.
> The **Trishul** paper's vendor-terms and procurement-agent questions sit here (see [Trishul solution](#/pyq-trishul)).

---

## 1. Three jobs NLP already does in procurement ⭐⭐⭐
| Job | What it does | Payoff |
|---|---|---|
| **RFx automation** | reads incoming bids and requisitions, auto-populates comparison matrices, drafts RFQs/RFPs from requirements (e.g. an **OpenAI API** call generating a structured RFx from a requisition) | "a week of bid-tabbing becomes an afternoon" |
| **Contract clause extraction** | pulls structured fields (price, term length, renewal notice, liability caps, penalty triggers) from unstructured PDFs | risk visibility and renewal alerts across thousands of contracts |
| **Spend classification** | tags every transaction into a category taxonomy (e.g. UNSPSC) instead of guessing from GL codes | spend cubes, maverick-spend detection, sourcing waves |

Further uses in the syllabus:
- **supplier risk monitoring** (news and filings scanned for distress signals);
- **compliance monitoring** (sanctions lists, ESG clauses, invoices checked against contract terms);
- **negotiation agents** (Pactum).

**Hugging Face 📘** hosts open transformer models (BERT-family, legal-domain models). You **fine-tune** them on your labelled contract-risk examples (domain grounding) and run them in your own environment, which keeps confidential contracts in-house. **OpenAI API 📘** is a metered general-purpose LLM: fast to prototype auto-RFx drafting and summarisation, billed per token (see §5).

### The 94.7% vs 79.3% gap ⭐⭐⭐
- **Domain-tuned models reach about 94.7%** accuracy on contract-clause risk classification in published benchmarks.
- **General-purpose LLMs without domain grounding land around 79.3%.**
- The **15-point gap** is why "just point ChatGPT at the contract" is not a procurement strategy.
- **Why the gap exists:** clause-risk classification is **a legal-reasoning task wearing language clothes**. A general LLM can summarise a clause fluently and still miss that **indemnification shifted from mutual to one-sided**, because it never trained on enough labelled contract-risk examples.

**Numeric framing.** 10,000 clauses are reviewed, of which 5% (500) are truly risky.
- At 94.7% accuracy, roughly 530 are misclassified.
- At 79.3%, about 2,070 are.
- Even if errors were spread evenly, the general model would miss about 4× more risky clauses.

**Precision/recall framing for risky clauses.** A model flags 600, of which 450 are truly risky, out of 500 risky in total.
- Recall = 450/500 = **90%**.
- Precision = 450/600 = **75%**.
- The 50 missed are the dangerous ones. For liability clauses, **optimise recall and route flags to a human**.

## 2. Class Q 6.1 (S16) — which clause gets the tuning budget? ⭐⭐⭐
The options are payment terms, address formatting, **penalty/indemnification** and contact details.
**Answer: C, penalty and indemnification.**
- A misread payment term is a scheduling headache: annoying and recoverable.
- A misread penalty or indemnification clause can put the company on the hook for **liability it never knowingly accepted**, discovered only when the supplier invokes it. That is expensive and sometimes irreversible.
- *The accuracy bar isn't one number; it scales with what the clause decides.*

## 3. Audit the claim anyway ⭐⭐
- Domain-tuning a vendor's model means **asking sharper questions, not fewer**.
- A vendor claiming "**~40% fewer disruptions**" is reporting its own number, not one independently audited. You don't know the baseline, the window or how "disruption" was defined.
- Apply the **Four-Question Claim Audit** (Ch 1): what was the baseline, measured how, over what window, and compared with what control?

## 4. Bounded autonomy in production — Walmart × Pactum ⭐⭐⭐
- Walmart runs a **live negotiation agent built with Pactum**, negotiating directly with **small and mid-tier suppliers** (the long tail no buyer has time for).
- It negotiates **price, payment terms and volume commitments**, only **inside boundaries a human category manager sets in advance**.
- The agent can **propose, counter and close within its mandate; it cannot expand that mandate on its own**. That makes it an **L3/L4 bounded-autonomy** pattern.
- **Manager takeaway:** agents execute thousands of bounded negotiations a human would never have time for, while humans retain control over where the boundaries sit.
- **EY survey:** about **80% of global CPOs** plan to deploy GenAI within three years, **led by spend analytics and contract management**.

### The Clause-Stakes Specification Checklist ⭐⭐⭐ (framework)
1. **List the clauses:** payment terms, renewal windows, liability caps, penalty triggers, termination, indemnification.
2. **Name the decision** each clause feeds downstream.
3. **Set the bar** per clause from the **cost of being wrong on that decision**, not one blanket target.
4. **Pick the tier:** general-purpose extraction is fine for logistics and contact fields; **domain-tuned models for anything touching liability**.
5. **Name the exception:** flag the one clause type whose interpretation you will **never fully automate**.

**Worked example (Round 6 chip contract).**
| Clause | Decision fed | Bar | Tier | Human? |
|---|---|---|---|---|
| Price/volume tiers | cost model, production plan | high | domain-tuned | review |
| Payment terms | cash plan | medium | general | spot-check |
| **Allocation in shortage / force majeure** | supply continuity | very high | domain-tuned | **always (the exception)** |
| **Liability, penalties, indemnity** | financial exposure | very high | domain-tuned | **always** |
| Delivery address / contacts | logistics admin | low | general | no |

## 5. APIs & token economics — the bill behind the brain ⭐⭐⭐
- **Software used to be free to run twice.** You bought a licence and extra use cost almost nothing.
- **Agentic AI is billed on consumption:** per API call, per token in and out, or tiered usage bands that reset monthly. It is **closer to a utility bill than a software purchase**.
- Cost scales with how much agents **think, read and write**. A verbose agent, or one told to "double-check its work", is quietly a more expensive agent (more tokens, more calls).
- **Prices are volatile.** Vendors cut per-token prices as compute gets cheaper but add premium tiers for stronger models. **A cost model is a snapshot, not a constant.** (Recall the **3.2× token overrun** in the S5 platform case.)

**Token-cost numeric (straightforward).** An RFx agent processes 2,000 bids per month at 6,000 input tokens and 1,500 output tokens per bid. Prices are ₹250 per million input tokens and ₹1,000 per million output tokens.
- Input: 2,000 × 6,000 = 12 M tokens × ₹250 = **₹3,000**.
- Output: 2,000 × 1,500 = 3 M tokens × ₹1,000 = **₹3,000**.
- The total is **₹6,000/month**, or ₹3 per bid.
- If a "double-check" step re-reads each bid (+6,000 input, +500 output), cost rises to 24 M × 250 + 4 M × 1,000 = 6,000 + 4,000 = **₹10,000 (+67%)**.
- If a premium tier costs 5×, the bill is about ₹50,000. Then compare it with **value per bid**.

### Governing the agent bill ⭐⭐⭐
- **A runaway agent bill is a governance failure, not a technology failure.**
- Extend the S4 identity-and-permissions stack to cover **spend**:
  - every agent gets a **per-agent budget cap enforced in code**, a hard ceiling on tokens or ₹ per run, **checked automatically before the call fires**;
  - **not** a system-prompt line asking the agent to "be economical", which it will ignore under pressure. *Guardrails live outside the model.*
- **Tune first:** shrink the context, **cache** repeated calls, **batch** calls, drop to a **cheaper model tier**, reduce call frequency. **Retire** only when a well-tuned version still can't clear its value bar.
- **Design for optionality:** **model-agnostic runtimes and open protocols** (e.g. MCP-style tool interfaces) let you swap models when a vendor's price spikes. "That optionality is priced insurance, not paranoia."

### Class Q 7.1 (S17) — the run cost doubles, quality unchanged ⭐⭐⭐
**Answer: C, check what the agent's decisions are actually worth, then tune or retire based on value-per-decision vs cost-per-decision.**
- A doubled bill on a low-stakes, high-volume decision can wreck margin.
- The same doubled bill on a decision worth 50× its cost barely matters.
- *A price shock is a signal to re-run the math, not a verdict. Tune before you retire.*

### The Tune-or-Retire Checklist ⭐⭐⭐ (framework)
1. **Measure cost:** total run cost (tokens, calls, compute) ÷ the number of decisions the agent actually made.
2. **Measure value:** the ₹ or margin impact of those decisions over the same window.
3. **Compare the ratio:** if value per decision still comfortably exceeds cost per decision, no action is needed.
4. **Tune first:** cut context, cache, batch, downgrade the tier, then re-measure.
5. **Retire if it still fails:** fall back to the next-best option rather than running an agent at a loss on principle.

**Worked numeric.** A negotiation agent closes 400 deals a month.
- Its run cost was ₹2 L and is now ₹4 L after repricing, so cost per decision has gone from ₹500 to **₹1,000**.
- The average saving per deal vs the manual baseline is ₹3,500, so value per decision is ₹3,500.
- The ratio is 3.5× (it was 7×). The agent **still clears**, so tune it anyway: caching might cut cost by 30% to ₹700 per decision.
- If the average saving were ₹800, the ratio would be 0.8×. Tune first; if tuned cost cannot fall below about ₹600 (a sensible margin below value), **retire** and fall back to the manual or rule-based process.

## 6. The efficiency-capture gap ⭐⭐⭐
- **McKinsey:** a chemicals firm piloting agentic procurement saw real **20–30% staff efficiency gains**, but only **1–3% of that translated into direct bottom-line value capture**.
- **Efficiency is easy to generate; margin on it is thin.** Run cost must be managed as tightly as value created, or the project quietly becomes a wash.
- **Walmart–Pactum** makes the same point from the other side: a live negotiating agent must continuously justify its run cost against the deal value it closes.
- **Ask:** not "did the agent help?" but "**did it help by more than it cost, this month, at this price?**"

**Numeric illustration.** A 50-person procurement team costs ₹10 cr. A 25% efficiency gain is "worth" ₹2.5 cr on paper. If only 2% of it is captured (headcount not redeployed, savings not banked), the realised value is about ₹5 L, which a ₹40 L/yr agent bill wipes out. **Capture plan first**: redeploy freed hours to strategic sourcing, and bank negotiated savings in the budget.

## 7. Chain Reaction link — Rounds 6 & 7 ⭐⭐⭐
- **R6, the chip contract:** your procurement agent negotiates a chip supply contract **under a mandate you set**, much like Walmart–Pactum. Specify the clauses that matter (allocation in shortage, penalties, volume flexibility) **before** it signs.
- **R7, the token economy:**
  - **24 decision tokens per month**;
  - a cap of **4 transformation actions per round**;
  - **2 tokens to generate an operating plan, 1 to regenerate it**;
  - every agent charges **1–4 tokens per month in upkeep**; terminating an agent costs 2.
- Make the tune-or-retire call on **cost-per-decision, not the size of the bill**. Retire low-value agents whose upkeep crowds out plan regeneration, and avoid building agents you can't afford to run. See the [Chain Reaction playbook](#/chain-reaction-playbook).

**Token-budget numeric.** You own 4 agents with upkeep 3 + 2 + 2 + 1 = 8 tokens/month, and you generate one plan (2) and regenerate twice (2). That totals 12, leaving **12 of 24** for builds.
- Retiring the 1-upkeep agent costs 2 now but saves 1 per month, so it **breaks even after 2 months**.
- Retire it only if its decisions are worth less than about 1 token per month and at least 2 months remain.

## Key takeaways (S16–S17 recaps 📘)
1. NLP already does three procurement jobs well: **RFx automation, clause extraction, spend classification**.
2. Domain-tuned models beat general LLMs on contract risk by **about 15 points (94.7 vs 79.3)**. Grounding matters more than fluency.
3. **Audit every vendor accuracy claim.** "40% fewer disruptions" is a claim, not a fact, until checked.
4. **The accuracy bar scales with what the clause decides.** Penalty and indemnification always get the strictest bar and a human in the loop.
5. **Consumption pricing** makes the agent bill a live operating cost. Prices swing quarterly, so a cost model is a snapshot.
6. **Spend caps belong in code**, not prompts. **Tune before you retire.** Mind the **efficiency-capture gap (20–30% vs 1–3%)**.

---

## Self-test
**Q1. A CPO wants one 95% accuracy target for all contract-extraction fields. Critique it.**
One bar ignores stakes. Set the bar per clause from the cost of error. Liability, penalty and indemnity clauses need domain-tuned models, high recall and human review. Contact and address fields can run on a general model at a lower bar. Name the one clause type you never fully automate.

**Q2. Why does a general LLM score 79.3% and a domain model 94.7% on clause risk?**
Clause risk is legal reasoning, not language fluency. The general model lacks labelled contract-risk training, so it misses subtle shifts (mutual → one-sided indemnity).

**Q3. An agent's monthly bill rose from ₹1 L to ₹3 L. What do you do?**
Run tune-or-retire: cost per decision vs value per decision. If value still exceeds cost comfortably, keep it and tune (cache, shorten context, cheaper tier). If not, tune then re-measure, and retire to the next-best option if it still fails.

**Q4. Why must spend caps live in code, not in the system prompt?**
Prompts are requests the model can ignore under pressure. A coded cap is checked before the call fires and cannot be argued with: guardrails live outside the model.

**Q5. Explain the efficiency-capture gap and how a manager closes it.**
Efficiency (20–30% time saved) doesn't automatically become margin (1–3% captured). Close it with a capture plan (redeploy freed capacity, bank savings in budgets), track realised ₹, and keep run costs below captured value.

**Q6. What makes Walmart–Pactum "bounded autonomy"?**
The agent proposes, counters and closes autonomously, but only inside price, terms and volume boundaries set by a human category manager. It cannot expand its mandate.
