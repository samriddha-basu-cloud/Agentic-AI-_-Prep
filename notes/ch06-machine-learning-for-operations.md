# Ch 6 — Machine Learning for Operations (Sessions 6–7)
**Syllabus unit 2 📘:** *Machine Learning for Operations — algorithms such as **SVM, k-Means**; tools like **Python (scikit-learn), RapidMiner**.* **Session 6 📘:** "Supervised, unsupervised and decision-focused learning — framed the way operators need them." Case: **SuryaMart — Three ML Pitches, One Budget** (A: forecasting for 40,000 SKUs; B: customer segmentation; C: supplier-delay early warning; "92% accuracy in the PoC"). **Session 7 📘 (lab):** "From a notebook that impresses to a capability that survives." Case: **Meghna Foods — the 94% Notebook** (only the analyst can run it, from CSVs on her laptop).

> **Exam use:** any accuracy number in a case ("92%", "94%", "87%") must be met with the **ML Framing Canvas**, a **naive benchmark**, the **leakage test**, and the question **"what does an error cost, in each direction?"**

---

## 1. The learning taxonomy — with operations uses ⭐⭐⭐
| Paradigm | Needs | Answers | OSCM examples |
|---|---|---|---|
| **Supervised** | labelled history: inputs + known outcomes | "given these features, predict this value/class" | demand forecasting (regression); supplier default risk, delay prediction (classification — e.g. **SVM**, boosted trees) |
| **Unsupervised** | unlabelled data | "what structure hides in here?" | SKU/customer segmentation (**k-means**), anomaly detection, store clustering for assortment |
| **Semi-supervised** | a little labelled + lots of unlabelled | | when labels are expensive |
| **Reinforcement** | an environment + a reward; learns by acting | "what POLICY maximises long-run reward?" | dynamic reordering, robot routing, dynamic pricing (S10) |
"At bottom, supervised ML is **labelling data at scale** — the scarce input is good labels, not algorithms." **Class Q 6.5:** three years of sales but no "stockout-corrected true demand" field → the core difficulty is that **the label you need doesn't exist yet** (sales ≠ demand when you stocked out). Frame the decision and construct the label before reaching for a model.
**The AI family tree:** deep learning ⊂ machine learning ⊂ AI. ML = "getting computers to do things they weren't specifically programmed to do" (a 1959 checkers program beat its author). Six moving parts: learner, data, algorithm, **parameters** (dials the machine turns), **hyperparameters** (dials a human sets), and the resulting model.

## 2. The algorithm zoo — and the two syllabus algorithms ⭐⭐
| Algorithm | Idea | Ops use |
|---|---|---|
| **Decision tree** | flow-chart of yes/no splits (prune useless branches) | late-delivery rules, credit holds |
| **Naïve Bayes** | conditional probability, predictors treated as independent | text/spend classification |
| **k-Nearest Neighbour** | classify by the majority of the k closest points | similar-SKU demand for new items |
| **k-Means** | cluster into k groups around moving centroids | SKU/customer/supplier segmentation |
| **Regression** | trend line through points → continuous value | **the forecasting workhorse** |
| **SVM** 📗 | finds the boundary (hyperplane) with the **widest margin** between classes; kernels handle non-linear boundaries | supplier-delay / default classification, defect detection |
| **Ensembles** | **bagging** averages many models (cuts variance; random forests); **boosting** reweights hard cases (gradient boosting — won the M5); **stacking** blends via a meta-learner (Netflix-Prize winners stacked 30+ models) | almost all winning forecasters |
**Choose empirically:** decision → tree; classify or cluster → kNN, k-means, naïve Bayes; predict a number → regression — **train two and keep the more accurate**.

### SVM in operations language 📗
A supplier-delay classifier with features (supplier's past on-time %, order size, lead time, port congestion index). SVM draws the boundary that separates "late" from "on-time" orders with the **maximum margin**, using only the hardest cases near the boundary (**support vectors**). Strengths: works well with many features and modest data; robust. Weaknesses: less interpretable, needs feature scaling, outputs a class not a calibrated probability (needs calibration before you use it for a **cost-weighted** decision). Exam framing: an SVM's "accuracy" means nothing until you price a missed delay vs a false alarm.

### k-Means in operations language 📗
Steps: choose k → place k centroids → assign each SKU to its nearest centroid → move each centroid to the mean of its members → repeat until stable. Choose k with the **elbow method** or by usefulness. Typical features: volume, volatility (coefficient of variation), margin, lead time → segments like "fast-stable", "slow-intermittent", "promo-driven". **Validation is not "accuracy"** — **Class Q 6.3:** "validate the k-means clustering's accuracy" is conceptually wrong — **there's no ground truth**; judge segments by whether they lead to **different, profitable treatments** (different stocking policies, forecasting tiers, service targets). "The decision, not a metric, validates unsupervised work."

## 3. How a neural net learns 📘
A neuron weighs inputs, adds a bias and fires through an activation function (a 25×25 image → 625 inputs → ~13,100 connections). A **cost function** measures wrongness; **gradient descent** rolls downhill to reduce it; **backpropagation** assigns blame backwards. **Bias vs variance:** too simple = consistently wrong (underfit); too complex = inconsistent (overfit). Aim between — capture signal, not noise.

## 4. Training, validation and the overfitting trap ⭐⭐
- **The split is sacred:** train on one slice, validate on another, **test on data the model never influenced** (the M5's authority comes from strict test design).
- **Overfitting in ops terms:** memorising last year — perfect on history, useless next quarter. Complexity buys flexibility AND fragility.
- **Non-stationarity is the ops disease:** promotions, competitors, pandemics shift regimes; models degrade silently → monitoring and retraining are not optional.
- **Features carry the value:** promotion calendars, installed base, lead signals usually beat algorithm choice — "the data groundwork of Session 2 IS the model's ceiling".

## 5. Decision-focused learning ⭐⭐⭐
- **Predict-then-optimise** trains on prediction error (e.g. MSE) then feeds an optimiser — simple and modular, but **misaligned**: the loss the model minimises is not the cost the business pays.
- **Concretely:** a newsvendor's optimal order is a **quantile** of demand, not the mean; over- and under-prediction cost differently; a symmetric loss optimises the wrong target "from the first epoch".
- **Decision-focused learning** trains with the **decision cost as the loss** — errors that would change decisions expensively are penalised more → consistent decision-cost improvements.
- **Where it leads:** S10's **one-step** paradigm learns the decision function itself, skipping the standalone forecast.

## 6. ML in the field ⭐⭐
### The M5 competition — ML wins, with an asterisk ⭐⭐⭐
Walmart's hierarchical retail data — **42,840 daily SKU-store series**, thousands of teams. **For the first time ML (gradient-boosted trees) decisively beat classical statistics; every top entry was ML.** The asterisk: **simple, nearly free methods stayed competitive at the SKU-store level where ordering happens**; the uncertainty track showed **distributional forecasting** is where hard value lives; naive benchmarks embarrassed many sophisticated entries. Twin lessons: ML's real edge AND the stubbornness of simplicity → "**price the gap between clever and simple before paying for clever**".

### Named wins 📘
**Danone** (ML demand planning on years of harmonised data) · **Lenovo** (+5% forecast accuracy, +4% OTD, +10% delivery accuracy — incremental, measured, real) · **Alibaba** published field study (automated ML replenishment vs human buyers — the algorithm won on stockouts and turnover) · **Zara** (real-time trend detection serving a **responsive** chain — "the tool matched the chain").

### Zillow Offers (2021) — when the model writes the cheques ⭐⭐⭐
Zillow used ML price forecasts to **buy houses directly** — an irreversible, capital-intensive decision at scale. Late 2021: unit shut, inventory written down **>$500M**, **~25%** of workforce cut. The same models powered the popular Zestimate (fine as **information**). Failure chain: point forecasts feeding automatic offers in a shifting market (non-stationarity); **asymmetric error costs** (overpaying fatal, underbidding just loses deals); guardrails not proportionate to blast radius. "**The decision defines the model** — an 87%-accurate price model can be excellent for browsing and ruinous for buying." **Class Q 6.1:** whether 87% is good enough depends on **the decision's cost and reversibility**.

## 7. Why operations ML disappoints — four failure modes ⭐⭐⭐
1. **No decision owner** — the model predicts something nobody acts on ("analytics as decoration").
2. **Accuracy theatre** — "92% accuracy" with no naive benchmark, no incumbent comparison, no decision-terms translation. **Class Q 6.4:** 92% vs naive same-as-last-week 90.5%, orders in full trucks → **unproven — barely beats naive**. "No model without a naive benchmark."
3. **Leakage and hindsight** — features unknown at decision time sneak in. **Class Q 6.2:** a supplier-delay model using **goods-receipt date** (known only after delivery) → **data leakage** — the most common cause of the demo-to-production cliff. "Features must pass the 'known at decision time' test."
4. **Asymmetric costs ignored** — symmetric loss while the business bleeds asymmetrically (newsvendor, Zillow).

## 8. The ML Framing Canvas — five boxes before any model ⭐⭐⭐
| Box | Question | SuryaMart Pitch C (supplier-delay warning) |
|---|---|---|
| **1 Decision** | who acts, at what cadence, within what constraints? no owner, no project | buyers expedite or re-source weekly; owner = procurement head |
| **2 Target** | the variable at **decision granularity** | "PO line arrives > 3 days late", per PO line |
| **3 Features** | knowable at decision time; no leakage | supplier history, order size, lead time, port index — **not** goods-receipt date |
| **4 Benchmark** | naive rule + incumbent, priced in decisions | "flag suppliers with < 85% OTD last quarter" |
| **5 Loss** | mirrors decision costs — asymmetric | missed delay (stockout) costs ≫ false alarm (an expedite call) → weight recall |
*SuryaMart resolved:* fund **Pitch C** first (clear decision owner, fast feedback, asymmetric cost you can price); reshape Pitch A (40,000 SKUs needs tier-matching and a naive benchmark — "92%" answers nothing about benchmark, holdout or granularity); Pitch B needs a decision (what treatment changes per segment?) before it can be validated. Ask "which pitch could a simple rule replace?" — that is the naive benchmark.

---

## 9. Session 7 — the workflow that survives ⭐⭐⭐
**Seven steps, in order — skipping one is how projects die:**
1. **Frame** — the S6 canvas.
2. **Profile** — six data-quality dimensions on the actual data, programmatically, before any model.
3. **Benchmark** — fit the **naive rule FIRST**; it is the floor.
4. **Model** — simplest credible model first; complexity only when it pays on the holdout.
5. **Evaluate** — honest holdout; error metrics AND **decisions changed**; **slice by segment** (averages hide failures).
6. **Deploy** — pipeline, not laptop: versioned data in, decisions out, permissions, logging.
7. **Monitor** — drift alerts, retraining cadence, **named owner**, documented **fallback**.
**Class Q 7.2:** the model beats naive by 6% overall but **loses** on promotional and new items → **deploy where it wins; keep naive elsewhere** (champion–challenger by segment).

## 10. The real stack — tools named in the syllabus ⭐⭐
- **Python + scikit-learn** 📘 — "the lingua franca of operations analytics": free, battle-tested, deep hiring market; covers classification, clustering, regression; runs on all major clouds. Typical lab flow 📗: `pandas` to load and profile → `train_test_split` (or a time-based split for forecasting) → a naive baseline → `LinearRegression` and `GradientBoostingRegressor` → score on the same holdout (MAE/MAPE) → slice by category.
- **RapidMiner-class AutoML & visual tools** 📘 — point-and-click model building for citizen data scientists; useful for prototyping and teams without Python depth; "**the tool automates fitting, not judgment**" — the same evaluation discipline applies. (RapidMiner 📗: drag-and-drop "operators" chained into a process — retrieve data, split, train, apply model, measure performance; AutoModel compares algorithms automatically.)
- **Managed ML clouds** 📘 — Amazon SageMaker, Azure ML, IBM Watson ML, Google Cloud AI (differ on clustering, anomaly detection, recommendation support).
- **Language/chatbots** — Dialogflow, Watson Assistant, LUIS, Lex, wit.ai; no-code agents Power Virtual Agents, Teneo.
- **Deep-learning frameworks** — TensorFlow and Keras to start; PyTorch, CNTK.
- **Walmart Element** — what the notebook grows into at scale: a model-agnostic ML platform with pipelines, monitoring and governance.
- "The newest tool is not always the best — sometimes a table, a chart or an expert system answers faster than a neural net." **Data mining ≠ ML:** BI sorts and summarises what you ask for; ML finds patterns you did not know to ask about.

## 11. The demo-to-production cliff ⭐⭐⭐
- **Leakage flattery** — the backtest used information unavailable at decision time (happens in half of first notebooks).
- **Environment drift** — last year's regime, mix, formats; nobody watches; decay is silent.
- **The bus factor** — one author, no documentation, manual steps from memory.
- **No fallback, no owner** — the model misbehaves at 2 a.m. before cut-off: who is called, what rule takes over?
**Class Q 7.1:** a brilliant analyst's model beats the incumbent by 8% in backtest, but she exports data manually, runs cells from memory, and keeps the only copy on her laptop → the firm owns **little durable — a one-person demo**. "A model in a notebook is not a capability." Conversion work is **60–80% of effort**.
**Class Q 7.3:** a churn model shows **99%** accuracy when only 3% churn → **accuracy is misleading; check for leakage** ("never churn" scores 97%).
**Four words of advice for the lab:** don't mix training and test data; don't overstate accuracy; know your algorithm (if you can't explain it you can't defend it); select tools deliberately (capability, cost, integration, skills). **Test in three layers:** unit, integration, acceptance; fix bugs **test-first**.

### The capability checklist
Reproducible (runs without its author) · monitored (drift, accuracy, decisions) · owned (named owner, on call) · documented fallback (rule that takes over) · versioned data and model · permissions and logging. "This is what separates the 5% that produce P&L impact from the 95% that produce slides."

*Meghna Foods resolved:* **dig, then delay** — the 94% needs a naive benchmark, an honest time-based holdout and decision-granularity evaluation; production first breaks on the bus factor and manual CSV exports. "Done" = a scheduled pipeline feeding the planning system by cut-off, monitored, with a named owner and a fallback rule, beating naive on the segments where it is deployed.

## Key takeaways (S6–S7 recaps 📘)
1. ML's victory is real (M5) and so is simplicity's stubbornness — price the gap before paying for clever.
2. The decision defines the model: the same 87% is excellent for information and ruinous for autonomous buying.
3. Supervised predicts, unsupervised structures, reinforcement decides — decision-focused learning trains on the cost you pay.
4. Leakage, overfitting and non-stationarity are why backtests flatter; holdout discipline is management.
5. The framing canvas is your permanent supervision tool. The tools are free and models easy; the capability is neither — 60–80% of effort is pipeline, monitoring and hand-off. Profile first, naive first, slice by segment, and write the honest verdict memo.

---

## Self-test
**Q1. "Our model is 92% accurate." List the three questions that number does not answer.**
Better than what (naive and incumbent on the same holdout)? Measured how (honest time-based holdout, no leakage)? At what granularity and worth what in decisions (does it change orders given full-truck multiples)?

**Q2. Why can't you report the "accuracy" of a k-means segmentation?**
There is no ground truth label; validate by whether segments lead to different, profitable actions (e.g. different stocking policies) that a planner can act on.

**Q3. A delay model's best feature is goods-receipt date. What happened?**
Leakage — the feature is known only after the delivery, so the backtest is flattered and production collapses. Every feature must be knowable at decision time.

**Q4. When would you pick an SVM, and what must you add before using it in a cost-weighted decision?**
For a classification task (late vs on-time, defect vs good) with many features and moderate data; add probability calibration and an asymmetric cost-based threshold, and compare against a naive rule.

**Q5. A model wins overall but loses on promotions. Deploy?**
Deploy it on the segments where it wins (staples) and keep the naive/incumbent method for promotions and new items — champion–challenger by segment, revisited as data accrues.
