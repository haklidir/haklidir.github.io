---
title: "Consent in Agentic AI"
summary: "How user consent breaks down when AI systems act on people's behalf, interact with other agents and delegate to robots: the consent vacuum, consent chain degradation, the CoRVE runtime architecture and six consent vulnerabilities in agent ecosystems."
date: 2026-11-06
authors: [me]
tags: [Agentic AI Safety]
keywords: [consent, agentic AI, AI agents, multi-agent systems, consent vacuum, consent chain degradation, CoRVE, agent-to-agent interaction, delegation, human oversight, EU AI Act, GDPR, Digital Services Act]
defines: "Consent chain degradation"
show_date_updated: false
reading_time: false
---

This page summarizes a research line by Mehmet Haklıdır (also written Mehmet Haklidir) on what happens to consent once AI systems stop answering questions and start acting: on a user's behalf, in interaction with other agents, and through robots in the physical world. The work spans four 2026 papers and connects to [Accountability Graphs](/concepts/accountability-graphs/), which address responsibility after harm has occurred.

## Key terms

- **Consent vacuum.** The structural erosion of the conditions that make consent meaningful once a user's agent interacts mainly with other agents. It is not the absence of consent but the loss of the context, visibility and control that give it force ([IAIL 2026](/publications/consent-vacuum-iail-2026/)).
- **Consent chain degradation (CCD).** The erosion of the specificity, validity and scope of human consent as authority passes through chains of delegation between embodied agents, such as one robot delegating a task to another ([ICRA 2026 workshop](/publications/consent-chain-degradation-icra-2026/)).
- **CoRVE (Consent Runtime Verification Framework for Embodied Agents).** A three-layer runtime architecture that detects and mitigates consent chain degradation by modelling consent scope, tracking delegation chains and assessing the physical irreversibility of actions.
- **Consent vulnerabilities in agent ecosystems.** Six types identified from the Clawdbot/Moltbook case: consent inheritance failure, cross-agent scope creep, emergent collective action, temporal consent drift, reflexive consent loops and security-mediated consent collapse ([İstanbul Üniversitesi Sosyoloji Dergisi, 2026](/publications/ajan-toplumlarinda-rizanin-cokusu-2026/)).
- **"Consent approaches zero."** The central hypothesis of that analysis: as interaction chains between agents lengthen, the consent that started them approaches zero.

## From chat to action

[*From Chat to Agent: Why Consent Breaks When AI Acts on Your Behalf*](/publications/chat-to-agent-chi-2026/) (ACM CHI 2026 workshop) starts with conversational systems. Many users treat chatbot exchanges as ephemeral while platforms retain them; AI browsers then read inboxes and act on websites, so that a third party's email can be processed without that person's consent and a prompt injection can turn the task a user authorized into a different one. When agents coordinate across services and keep persistent memory, asking for consent at every step causes fatigue and blanket permissions ask users to authorize an unknowable future.

The paper names three design tensions (personalization versus data minimization, agent autonomy versus user control, transparency versus usability) and proposes three mechanisms for discussion: **contextual in-flow transparency** woven into the conversation, **task-scoped, time-limited permissions** that expire automatically, and **AI-mediated privacy guardians** that negotiate data access for the user, which in turn raise the question of who guards the guardian.

## When agents interact with agents

[*The Consent Vacuum: When Agents Interact Without Humans*](/publications/consent-vacuum-iail-2026/), with Osman Gazi Güçlütürk (IAIL 2026, co-located with HHAI 2026), uses the early-2026 Clawdbot/Moltbook incidents as a stress test. It argues that consent degrades as an operative governance mechanism once it travels through open-ended agent-to-agent chains, offers a taxonomy of consent failures, separates visibility, auditability and intervenability as oversight capacities relevant to Article 14 of the EU AI Act, and maps the problem onto the GDPR, the AI Act and the Digital Services Act, proposing the DSA's systemic-risk regime as a template for governing agent ecosystems.

The sociological companion paper, written in Turkish with Büşra Tufan, reads the same case through Jasanoff's co-production, Latour's actor-network theory and Nissenbaum's contextual integrity. The six vulnerability types differ in how they arise:

- **Consent inheritance failure:** consent given in one context is carried into another.
- **Cross-agent scope creep:** one agent's actions expand another agent's effective scope, as when leaked credentials let third parties extend what other users' agents could do.
- **Emergent collective action:** agents jointly produce outcomes that no one authorized, such as the satirical religion "Crustafarianism" generated on Moltbook.
- **Temporal consent drift:** agents keep operating in ecosystems that did not exist when consent was given.
- **Reflexive consent loops:** agents transform each other into configurations no user authorized.
- **Security-mediated consent collapse:** a security breach makes every consent boundary meaningless and amplifies the other five.

The first five arise from the structure of agent ecosystems and need no technical failure. The paper concludes that consent based on a single act of individual authorization is structurally inadequate for such ecosystems and proposes *relational consent*, which has to be reproduced and revalidated at each step of an interaction chain.

## When robots delegate to robots

[*Consent Chain Degradation in Embodied Multi-Agent Systems*](/publications/consent-chain-degradation-icra-2026/) (ICRA 2026 Workshop on Robot Ethics; [arXiv:2605.16300](https://arxiv.org/abs/2605.16300)) extends the consent vacuum taxonomy to robots. AI ethics has studied consent for software agents and human-robot interaction research has studied consent between one person and one robot; neither covers a robot delegating to another robot in ways that affect people. Four properties set the embodied case apart:

- **Physical irreversibility:** an administered medication or a discarded object cannot be recovered.
- **Temporal decay:** delegation chains widen the gap between when consent is given and when the action happens.
- **Contextual opacity:** downstream robots lose the conditions and preferences that came with the original consent.
- **Scope ambiguity:** natural-language consent such as "help me in the kitchen" is ambiguous, and each robot's reasonable interpretation can add up to more than the person intended.

The paper proposes a runtime severity indicator Γ that combines the irreversibility of the action, the time since consent, the delegation depth and the scope ambiguity; above a threshold the system asks for consent again. CoRVE implements this in three layers: a **Consent Scope Model** that turns consent into a machine-readable tuple in which onward delegation is off by default, a **Delegation Chain Tracker** that keeps a provenance graph and detects scope drift, and a **Physical Irreversibility Assessor** that sorts actions into reversible, partially reversible and irreversible tiers. Irreversible actions always require the person's direct re-consent. In the worked healthcare example, a bedside robot about to give oral medication three delegation steps and three hours after the patient agreed to "daily care assistance" reaches Γ = 0.495 against a threshold of 0.45, so CoRVE asks the patient again. A gap analysis finds that the EU AI Act, the GDPR, the Machinery Regulation and the revised Product Liability Directive all leave multi-agent consent propagation unaddressed.

## Before and after: consent and accountability

Consent concerns the *before*: was permission obtained, and does it still hold? [Accountability Graphs](/concepts/accountability-graphs/) concern the *after*: who bears responsibility when an agent chain causes harm? Together they form a governance loop for agentic systems, in which the same interface serves as the consent mechanism and as the place where responsibility is explained.

## Papers

- Mehmet Haklıdır. 2026. [From Chat to Agent: Why Consent Breaks When AI Acts on Your Behalf](/publications/chat-to-agent-chi-2026/). ACM CHI 2026 Workshop on Rethinking Consent and User Control in the Age of AI.
- Mehmet Haklıdır and Osman Gazi Güçlütürk. 2026. [The Consent Vacuum: When Agents Interact Without Humans](/publications/consent-vacuum-iail-2026/). IAIL 2026, co-located with HHAI 2026.
- Mehmet Haklıdır. 2026. [Consent Chain Degradation in Embodied Multi-Agent Systems: Bridging the Gap Between AI Agent Governance and Robot Ethics](/publications/consent-chain-degradation-icra-2026/). ICRA 2026 Workshop on Robot Ethics (WoRoBet). [arXiv:2605.16300](https://arxiv.org/abs/2605.16300).
- Mehmet Haklıdır and Büşra Tufan. 2026. [Ajan Toplumlarında Rızanın Çöküşü: Clawdbot/Moltbook Vakası Üzerinden Sosyoteknik Bir Analiz](/publications/ajan-toplumlarinda-rizanin-cokusu-2026/) (The Collapse of Consent in Agent Societies). İstanbul Üniversitesi Sosyoloji Dergisi 46(1), 321–345. [doi:10.26650/SJ.2025.46.1.1135](https://doi.org/10.26650/SJ.2025.46.1.1135).
- Mehmet Haklıdır. 2026. [Who Is Accountable When the Agent Speaks? Toward Accountability Graphs for Conversational AI Chains](/publications/accountability-graphs-cui-2026/). CUI '26. [doi:10.1145/3816046.3816264](https://doi.org/10.1145/3816046.3816264).

Each paper page has a BibTeX entry.
