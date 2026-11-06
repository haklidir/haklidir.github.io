---
title: "Guided Soft Actor-Critic (GSAC)"
summary: "A deep reinforcement learning method for partially observable problems in which a guiding actor with privileged full-state access distils its policy into a control actor that acts on observation histories; extended in 2026 by Belief-Aware GSAC."
date: 2026-11-06
authors: [me]
tags: [Reinforcement Learning]
keywords: [Guided Soft Actor-Critic, GSAC, BA-GSAC, soft actor-critic, deep reinforcement learning, POMDP, partial observability, privileged learning, teacher-student, policy distillation, autonomous driving, observability blindness]
defines: "Guided Soft Actor-Critic"
paper_doi: "10.1109/ACCESS.2021.3131772"
paper_url: /publications/guided-soft-actor-critic-ieee-access-2021/
show_date_updated: false
reading_time: false
---

**Guided Soft Actor-Critic (GSAC)** is a deep reinforcement learning method for partially observable Markov decision processes (POMDPs), introduced by Mehmet Haklıdır (also written Mehmet Haklidir) and Hakan Temeltaş in [*IEEE Access* (2021)](/publications/guided-soft-actor-critic-ieee-access-2021/) ([doi:10.1109/ACCESS.2021.3131772](https://doi.org/10.1109/ACCESS.2021.3131772), open access) and developed in Haklıdır's [PhD thesis](/publications/phd-thesis-drl-pomdp-2022/) at Istanbul Technical University. A 2026 follow-up, [Belief-Aware GSAC](/publications/adaptive-guidance-cvpr-wad-2026/), studies when adapting the strength of the guidance helps.

## In brief

- **Problem.** Soft Actor-Critic (SAC) performs well in continuous control but assumes the agent sees the full state. Under occlusion, sensor noise or a limited field of view, as in autonomous driving, performance drops.
- **Idea.** Train two actors. A *guiding actor* sees the full state during training; a *control actor* sees only a history of partial observations and learns both from reward and from the guiding actor's behaviour, through a distillation term weighted by a coefficient λ.
- **Deployment.** Training follows centralized training with decentralized execution: the critic and the guiding actor use the full state, while only the control actor, which needs no privileged information, is deployed.
- **Family.** GSAC belongs to privileged or teacher-student learning, alongside learning from a privileged agent in driving and asymmetric actor-critic; it uses a dual-actor reinforcement learning set-up with explicit knowledge distillation.

## How GSAC works

The two actors interact with the environment in alternation. The guiding actor πg optimizes the standard maximum-entropy SAC objective on the full state. The control actor πc acts on an observation history and optimizes the same objective minus a distillation penalty, λ‖πc(h) − D(h)‖², where D is a distillation network that maps observation histories to the guiding actor's actions. Both actors share a twin Q-network that takes the full state during training.

## Belief-Aware GSAC (2026)

In the original method λ is fixed. Fixed guidance can hold back an agent that already understands its situation and can be too weak when the agent is uncertain. [*When Does Adaptive Guidance Help? Belief-Aware Privileged Distillation for Autonomous Driving Under Partial Observability*](/publications/adaptive-guidance-cvpr-wad-2026/) (CVPR 2026 Workshop on Autonomous Driving; [arXiv:2605.26155](https://arxiv.org/abs/2605.26155)) makes λ adaptive. An ensemble of forward models predicts the next observation; their disagreement serves as a proxy for epistemic uncertainty and raises or lowers λ between a minimum and a maximum, with bounds calibrated during a warm-up phase.

Evaluated on Highway-Env across mild, moderate and severe occlusion, the results are mixed and informative:

- Preliminary single-seed runs suggest benefits under mild and moderate partial observability.
- Under severe occlusion the adaptive coefficient collapses to its minimum within about 3,000 steps. The paper calls this **observability blindness**: because the ensemble predicts partial observations, it agrees with itself about what is visible and cannot register what is missing.
- The warm-up phase still stabilizes training (coefficient of variation across seeds 13.3% against 29.8% for a constant λ of 0.01), and a simple linear decay of λ gives the best severe-occlusion results (mean return 116.5, coefficient of variation 8.9%). The benefit comes from scheduling the guidance rather than from the ensemble.
- The proposed remedy, not yet validated, is to train the ensemble on full-state predictions using the guiding actor's privileged access.

The broader lesson is that the prediction target of an uncertainty ensemble is a design choice that matters under partial observability.

## Papers

- Mehmet Haklıdır and Hakan Temeltaş. 2021. [Guided Soft Actor Critic: A Guided Deep Reinforcement Learning Approach for Partially Observable Markov Decision Processes](/publications/guided-soft-actor-critic-ieee-access-2021/). *IEEE Access* 9, 159672–159683. [doi:10.1109/ACCESS.2021.3131772](https://doi.org/10.1109/ACCESS.2021.3131772).
- Mehmet Haklıdır. 2022. [Deep Reinforcement Learning for Partially Observable Markov Decision Processes](/publications/phd-thesis-drl-pomdp-2022/). PhD thesis, Istanbul Technical University.
- Mehmet Haklıdır. 2026. [When Does Adaptive Guidance Help? Belief-Aware Privileged Distillation for Autonomous Driving Under Partial Observability](/publications/adaptive-guidance-cvpr-wad-2026/). CVPR 2026 Workshop on Autonomous Driving. [arXiv:2605.26155](https://arxiv.org/abs/2605.26155).

Each paper page has a BibTeX entry.
