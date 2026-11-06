---
title: "AI for Geothermal Energy: Validation and Deployment Readiness"
summary: "What a systematic evidence map of 626 peer-reviewed studies shows about AI in geothermal energy systems: how far methods have been validated beyond their development data, the E0–E4 evidence-readiness scale, and why transferability and deployment do not advance together."
date: 2026-11-06
authors: [me]
tags: [AI for Geoscience]
keywords: [geothermal energy, artificial intelligence, machine learning, systematic evidence map, PRISMA, external validation, transferability, deployment readiness, evidence-readiness level, reservoir management, predictive maintenance]
defines: "Evidence-readiness level (E0–E4)"
paper_doi: "10.1007/s12145-026-02268-7"
paper_url: /publications/geothermal-ai-evidence-map-esi-2026/
show_date_updated: false
reading_time: false
---

Artificial intelligence has been applied to almost every part of geothermal energy, from exploration and reservoir management to plant control and maintenance. Füsun S. Tut Haklıdır and Mehmet Haklıdır (also written Haklidir) asked a different question from most of that literature: not whether the methods work, but how far the published evidence has moved from the data each method was developed on, and whether any of it has reached an operating plant. The answer comes from a PRISMA-guided systematic evidence map published in [*Earth Science Informatics* (2026)](/publications/geothermal-ai-evidence-map-esi-2026/) ([doi:10.1007/s12145-026-02268-7](https://doi.org/10.1007/s12145-026-02268-7)).

## Key findings

- **Corpus.** Searches of Scopus and Web of Science returned 8,113 records; 626 peer-reviewed journal articles published between 1987 and 2026 were included, resolving to 620 independent evidence units. Each article was coded from full text, with a page or section locator for every value reported quantitatively.
- **Mostly offline evidence.** Two thirds of the classifiable corpus is evaluated on simulation, synthetic or laboratory data, or on field data without a meaningful held-out design. About one third reaches evaluation on real geothermal field data.
- **Little external validation.** Evaluation on data external to the development set is reported in 42 of the 614 articles for which this could be determined.
- **Almost no deployment.** Three articles report a controlled pilot; none reports shadow operation or routine deployment in the peer-reviewed literature. Grey and industry literature was not searched, so deployments that exist without publication are not excluded.
- **Maturity depends on the stage.** Surface conversion contributes 179 articles, of which four reach field evaluation; exploration contributes 183, more than half of which do.
- **Transfer and deployment diverge.** Predictive maintenance holds two of the three controlled pilots and no externally validated study, while geophysical inversion and induced-seismicity detection hold the transfer evidence and no pilot.
- **Data access is spreading faster than demonstrated transfer.** The share of articles reaching field evaluation rose from 13 per cent in 2018 to 43 per cent in 2025, while externally validated studies stayed in single figures each year.
- **Reporting is the binding constraint.** Among codable articles, 493 report no uncertainty estimate and 536 provide no access to code; for roughly a third, the paper does not establish whether performance was measured on unseen data.

## How readiness was measured

Validation and deployment evidence were coded on three independent axes:

- **Boundary separation:** whether the test data are separated from the training data by time or by space (well, site or field) rather than at random.
- **Strict external validation:** evaluation on data genuinely external to the development dataset. A careful split inside one dataset does not count.
- **Operational integration:** an ordered ladder from offline study, conceptual architecture and offline prototype to controlled pilot, shadow or parallel operation, and routine deployment, coded from what a paper reports rather than how it describes itself.

From these fields the review derives an **evidence-readiness level** by a fixed rule, so that every assignment can be recomputed from the supplementary data:

| Level | Meaning |
|---|---|
| E4 | Operational integration: controlled pilot, shadow or parallel operation, or routine deployment |
| E3 | Demonstrated transferability: strict external validation |
| E2 | Field evaluation with a boundary-separated or held-out design that falls short of strict external validation |
| E1 | Original evaluation without external evidence: simulation, synthetic or laboratory data, or field data without a meaningful held-out design |
| E0 | No original evaluation |

The highest qualifying level applies, so a study can reach E4 through a pilot without any external validation. The scale describes the published evidence about a method, not the maturity of the technology: it is not a Technology Readiness Level, not a risk-management framework such as the NIST AI RMF, and not a reporting guideline such as TRIPOD+AI. Because transferability and operational integration do not move together, the review reports them on separate axes and uses the E-level only as a summary.

## What follows

The authors' conservative reading is not that geothermal AI has failed to mature, but that its maturity has been reported in a form that makes verification difficult. Transferability should be tested rather than assumed and reported on the axis actually tested, since evaluation across wells in one field and evaluation against an independent dataset are different claims. The few studies that move from an offline prototype to an operating setting carry disproportionate weight.

## Data and related work

The record-level coding dataset, data dictionary, derivation rules and reproducibility scripts are archived on Zenodo ([doi:10.5281/zenodo.21938792](https://doi.org/10.5281/zenodo.21938792); data under CC BY 4.0, scripts under MIT).

Related studies by the same authors:

- [Predicting dissolved lithium in geothermal fluids from routine hydrogeochemistry](/publications/lithium-prediction-uq-esi-2026/) (*Earth Science Informatics*, 2026): grouped cross-validation over 26 locations and calibrated prediction intervals; code on [GitHub](https://github.com/haklidir/geothermal-lithium-ml).
- [Advancing geothermal reservoir temperature prediction using synthetic hydrogeochemical data from rank–Gaussian copulas](/publications/copula-synthetic-data-reservoir-temperature-geothermics-2026/) (*Geothermics*, 2026); code on [GitHub](https://github.com/haklidir/rgc-dnn-ngboost-geothermal-temperature).
- [Prediction of reservoir temperatures using hydrogeochemical data in Western Anatolia: a machine learning approach](/publications/reservoir-temperature-ml-nrr-2020/) (*Natural Resources Research*, 2020).

## How to cite

Füsun S. Tut Haklidir and Mehmet Haklidir. 2026. Artificial intelligence for geothermal energy systems: a systematic evidence map of validation, transferability and deployment readiness. *Earth Science Informatics* 19, 211. https://doi.org/10.1007/s12145-026-02268-7

The [paper page](/publications/geothermal-ai-evidence-map-esi-2026/) has a BibTeX entry.
