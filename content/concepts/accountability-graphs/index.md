---
title: "Accountability Graphs"
summary: "A framework for attributing responsibility in conversational AI agent chains: agent chains are modelled as directed acyclic graphs with provenance metadata and causal responsibility semantics, and harm is traced backwards to graded responsibility scores."
date: 2026-11-06
authors: [me]
tags: [Agentic AI Safety]
keywords: [Accountability Graphs, responsibility attribution, multi-agent systems, conversational AI, causal responsibility, provenance, agentic AI governance, accountability surface, EU AI Act]
defines: "Accountability Graph"
paper_doi: "10.1145/3816046.3816264"
paper_url: /publications/accountability-graphs-cui-2026/
show_date_updated: false
reading_time: false
---

**Accountability Graphs** is a framework for deciding who is responsible when a conversational AI system built from several agents produces a harmful or misleading answer. It was introduced by Mehmet Haklıdır (also written Mehmet Haklidir) in [*Who Is Accountable When the Agent Speaks? Toward Accountability Graphs for Conversational AI Chains*](/publications/accountability-graphs-cui-2026/), presented at the ACM Conference on Conversational User Interfaces (CUI '26) in Bremen, Germany, in July 2026 ([doi:10.1145/3816046.3816264](https://doi.org/10.1145/3816046.3816264)).

## In brief

- **Problem.** Conversational assistants increasingly delegate work to sub-agents, external APIs and third-party tools. The user sees one assistant, but each answer is produced by a chain of components that may belong to different organizations. When the answer causes harm, blaming either the visible interface or the system developer misses how responsibility is spread across the chain.
- **Idea.** Model each agent chain as a directed acyclic graph whose nodes are decisions, whose edges are information or control flow, and which carries provenance records and a harm propagation function. Responsibility is then computed by tracing backwards from the harm, rather than asserted.
- **Basis.** The framework unifies three research threads that had developed separately: structural mapping of AI ecosystems, formal causal responsibility theory (Halpern and Pearl's actual causation; Chockler and Halpern's degree of responsibility) and operational provenance tracking.
- **Output.** Graded responsibility scores for chain components, plus an *accountability surface*: a user-facing explanation of what went wrong and who is responsible, with a path to contest the attribution.
- **Status.** A conceptual work-in-progress paper with a worked example. Full formalization and empirical evaluation are ongoing.

## Why conversational agent chains need it

Work on trust, transparency and explainability in conversational AI asks whether users rely on a system, whether they can see what it does and why it produced an output. None of these answers who bears responsibility when an output causes harm. Agent chains make this harder in three ways:

- **An illusion of singularity.** The interface presents one persona, while several technical and organizational actors jointly produce each utterance. This is the "many hands" problem described by Helen Nissenbaum, amplified by a conversational facade.
- **Real-time dialogue.** Decisions are made and compounded within a single conversational turn, which makes post-hoc tracing difficult.
- **Dynamic delegation.** The orchestrating agent decides at runtime which sub-agents to call, so the accountability structure emerges during the conversation instead of being fixed at design time.

## The framework

An Accountability Graph for a conversational agent chain is a tuple **AG = (N, E, P, H)**:

- **N, decision nodes.** Points where a component makes a choice that influences the output, such as intent classification, agent delegation, tool invocation or response generation. A node can be an entire agent, a single tool call or one decision inside a component; finer nodes give more precise attribution but need more detailed logging.
- **E, directed causal edges.** Dataflow edges carry information between steps; configuration edges represent design-time settings, such as an orchestrator configuring a sub-agent's policy.
- **P, provenance function.** Maps each node to a record of the responsible component, its degree of decision autonomy, the information available at decision time, the temporal context and any contractual or design obligations.
- **H, harm propagation function.** Maps each node to a value between 0 and 1 that captures how a harm detected at a terminal node relates to upstream decisions, following Halpern and Pearl's structural-model approach to actual causation.

The paper adapts the framework to five conversational settings: temporal proximity weighting for real-time dialogue, the accountability surface for user-facing accountability, contextual provenance tracking for multi-turn context, modality-aware node types for voice versus text, and runtime graph construction for dynamic delegation.

## Backward responsibility propagation

Responsibility is assigned by traversing the graph from the harm towards its sources:

1. **Harm localization.** Identify the terminal node or nodes where the harm appears in the conversational output.
2. **Causal backtracking.** Walk the edges backwards and test, at each node, whether it is an actual cause of the harm in Halpern and Pearl's sense.
3. **Provenance-weighted scoring.** For each causal node, combine its degree of responsibility with provenance factors (decision autonomy, information availability, temporal proximity, scope of obligations) into a graded score.
4. **Counterfactual validation.** For the highest-scoring nodes, check the attribution by asking whether the harm would have occurred had that node decided otherwise.

The graph traversal itself is linear in the size of the graph; the cost lies in the counterfactual evaluation at each candidate node.

## Worked example: an airline bereavement fare agent

The paper starts from *Moffatt v. Air Canada* (2024), in which a Canadian tribunal held an airline liable after its customer-service chatbot misrepresented its bereavement fare policy. That case could be resolved because the system was monolithic. The paper imagines the same airline running a seven-node agent chain: intent parser, orchestrator, policy retrieval agent, a third-party knowledge base API, a synthesis agent, an empathy filter and delivery.

![Accountability Graph for the bereavement fare scenario. The knowledge base API (n4) and the synthesis agent (n5) carry primary responsibility, the orchestrator (n2) secondary responsibility, and the harm appears at delivery (n7). The dashed edge is the orchestrator's configuration of the synthesis agent.](accountability-graph-example.png)

Facing a structured fare rule and an outdated FAQ passage that contradict each other, the synthesis agent picks the FAQ and tells a grieving user that a refund can be claimed after travel. It cannot. Backward propagation identifies the synthesis agent and the knowledge base API as primary contributors and the orchestrator as a secondary one. With illustrative provenance weights, the synthesis agent, which had full autonomy and access to both sources, scores 0.97; the knowledge base API, a retrieval service operating under prescribed parameters, scores 0.80; and the orchestrator, which configured the synthesis step, scores 0.43. The weights are examples; in deployment they could be set by designers, elicited from stakeholders or learned from incident data.

## Accountability surfaces

The accountability surface translates the internal graph into explanations for people. End users need short, actionable explanations and a remedy; auditors and regulators need the full provenance trail and formal scores; support staff need something in between. One graph can serve all three. In sensitive situations such as bereavement, the explanation has to draw on conversational repair and empathic response design, and voice interfaces need shorter explanations than text. Accountability surfaces should also support contestability: a clear way to challenge the attribution, request a remedy or reach a human.

## Regulatory alignment

As a preliminary interpretive mapping, not a formal legal analysis, the paper links the framework to the EU AI Act: node-level provenance to risk management (Article 9), runtime graph construction to logging (Article 12), and the accountability surface to disclosure obligations towards natural persons (Article 50), extended from disclosing that a system is an AI to disclosing who is responsible. The provider and deployer roles (Articles 16 and 26) map to responsibility weights for nodes maintained by different organizations.

## Accountability and consent

Accountability Graphs belong to a research line on consent and responsibility in agentic AI. Consent concerns the *before*: was permission obtained? Accountability concerns the *after*: who bears responsibility? Together they form a governance loop, and the conversational interface is both the consent mechanism and the accountability surface. Related papers:

- [From Chat to Agent: Why Consent Breaks When AI Acts on Your Behalf](/publications/chat-to-agent-chi-2026/) (CHI 2026 workshop)
- [The Consent Vacuum: When Agents Interact Without Humans](/publications/consent-vacuum-iail-2026/) (IAIL 2026), on consent in agent-to-agent interaction
- [Consent Chain Degradation in Embodied Multi-Agent Systems](/publications/consent-chain-degradation-icra-2026/) (ICRA 2026 workshop), on consent when actions are physical and irreversible

## How it relates to other approaches

- **Ecosystem graphs** (Bommasani et al.) map asset-level dependencies across the foundation model ecosystem but perform no causal analysis and attribute no responsibility.
- **Actual causation and degree of responsibility** (Halpern and Pearl; Chockler and Halpern) provide the formal machinery, but had been applied to model-internal questions rather than to pipelines or agent chains.
- **Provenance and documentation** (data provenance audits, model cards, datasheets, accountability metrics catalogues) record decisions and lineage but do not compute responsibility from that record. Accountability Graphs add causal responsibility semantics on top of provenance, which also distinguishes them from purely provenance-based responsibility tracing or accountability chains in multi-agent systems.
- **Responsibility and control gaps** (Santoni de Sio and Mecacci; Hindriks and Veluwenkamp) describe situations in which no single agent has enough control to be held responsible, a framing that applies directly to agent chains.

## Limitations and next steps

The framework is diagnostic, not normative: it shows where failures occurred, not what legal consequences should follow. Graded scores could be misused to shift blame onto third-party providers or users, so the paper suggests a minimum accountability floor for whoever controls the orchestrator. Users are not yet represented as nodes, proprietary black-box components can only be assessed by their inputs, outputs and contracts, and accountability norms differ across cultures and jurisdictions. A prototype that builds Accountability Graphs at runtime from LangChain callback hooks is in development, followed by a think-aloud study with conversational interface designers and a user study comparing accountability-surface explanations with standard error messages.

## How to cite

Mehmet Haklidir. 2026. Who Is Accountable When the Agent Speaks? Toward Accountability Graphs for Conversational AI Chains. In *Proceedings of the 8th ACM Conference on Conversational User Interfaces (CUI '26)*, Bremen, Germany. ACM, 56:1–56:5. https://doi.org/10.1145/3816046.3816264

```bibtex
@inproceedings{haklidir2026accountable,
  title     = {Who Is Accountable When the Agent Speaks? Toward Accountability Graphs for Conversational AI Chains},
  author    = {Haklidir, Mehmet},
  booktitle = {Proceedings of the 8th ACM Conference on Conversational User Interfaces (CUI '26)},
  pages     = {56:1--56:5},
  year      = {2026},
  publisher = {ACM},
  address   = {Bremen, Germany},
  doi       = {10.1145/3816046.3816264}
}
```

[Paper page and PDF](/publications/accountability-graphs-cui-2026/) · [ACM Digital Library](https://doi.org/10.1145/3816046.3816264)
