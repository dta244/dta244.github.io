---
title: "Estimating the Economic Impacts of Climate Stress on U.S. Dairy Production: Evidence from Debiased Machine Learning and Simulation-Based Estimator Choice"
collection: publications
category: JMP
permalink: /publication/2026-climate-stress-milk-production
date: 2026-10-19
venue: 'Unpublished Working Paper'
paperurl: '/files/DAIRY_PAPER_v1.5_2026-10-20.pdf'
excerpt: 'Monthly data from 21 major U.S. dairy states link heat and cold exposure to milk yield and fat content. Synthetic-data simulations guide estimator choice; heat reduces yield, while the cold estimate is imprecise and magnitudes depend on the response function.'
citation: 'Ta, Duong, Mario Ortez, Bradford Mills, and Michael Cary. 2026. "Estimating the Economic Impacts of Climate Stress on U.S. Dairy Production: Evidence from Debiased Machine Learning and Simulation-Based Estimator Choice." Working paper, draft v1.5, October 19.'
---

{% include base_path %}

**Authors:** Duong Ta, Mario Ortez, Bradford Mills, and Michael Cary

Department of Agricultural and Applied Economics, Virginia Tech

**Draft v1.5, last updated October 19, 2026.** Funded by The Dairy Alliance.

## Abstract

We estimate how heat and cold exposure affect milk yield and fat content in a monthly
panel of 21 major U.S. dairy states from 2003 through 2025. USDA NASS outcomes are
matched to hourly ERA5-Land weather aggregated with county milk-cow inventory weights.
State × calendar-month fixed effects absorb each state's seasonal cycle and year-month
fixed effects absorb national monthly shocks, so responses are identified from differences in
weather across states within the same month. We compare linear and cubic regressions with
LASSO and neural-network learners, with and without automatic debiasing, and select the
reported estimator for each stress tail based on its performance in synthetic-data simulations:
the cubic regression for heat and the debiased neural network for cold, both with two-way
clustered intervals. An additional 24-hour-equivalent day at or above THI 69 lowers milk per
cow by 0.29 percent, cumulated over the exposure month and three lags. The cold estimate,
−0.22 percent per day below THI 39, has a 95 percent interval that includes zero. Removing
heat stress would have raised production by about 1.7 percent, and removing both tails by
2.9 percent. The size of these effects depends on the functional form of the response, which
the data cannot pin down. Applied uniformly to 2003–2024 production in the 48 contiguous
states, the joint share is worth about $23.9 billion, or $1.09 billion per year. Evaluated at
each state's exposure, the heat share ranges from 0.7 percent of production in Oregon to 4.5
percent in Florida. Heat lowers and cold raises milk fat content. A break search finds no
detectable change in the yield responses, but the heat effect on fat content weakens after the
mid-2010s. Climate-normal diagnostics give suggestive but specification-sensitive evidence
of adaptation.

[About the project and its earlier dashboard snapshot]({{ base_path }}/projects/climate-stress-dairy/)
