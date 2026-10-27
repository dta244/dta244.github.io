---
title: "Climate Stress and U.S. Dairy Production"
collection: projects
date: 2026-01-01
status: "Unpublished Working Paper"
role: "Lead author"
stack: "Python, panel econometrics, debiased machine learning, simulation"
dashboardurl: "/dashboards/dairy-heat-stress/"
paperurl: "/files/DAIRY_PAPER_v1.5_2026-10-20.pdf"
question: "How much milk production is lost to heat and cold stress, and what do the estimates imply for adaptation investments?"
summary: "Links monthly milk yield and fat content in 21 major U.S. dairy states (2003–2025) to hourly weather. Synthetic-data simulations select a cubic regression for heat and a debiased neural network for cold; estimated losses depend on the assumed response function."
---

{% include base_path %}

## Job market paper

*Estimating the Economic Impacts of Climate Stress on U.S. Dairy Production: Evidence from Debiased
Machine Learning and Simulation-Based Estimator Choice*, with Mario Ortez, Bradford Mills, and Michael Cary.
Draft v1.5, last updated October 19, 2026. Funded by The Dairy Alliance.

[Read the paper]({{ base_path }}/files/DAIRY_PAPER_v1.5_2026-10-20.pdf) · [Abstract and citation]({{ base_path }}/publication/2026-climate-stress-milk-production)

## Main findings

An additional 24-hour-equivalent day at a temperature-humidity index (THI) of at least 69 lowers milk per
cow by 0.29 percent over the exposure month and three lags. The cold estimate is −0.22 percent per day
below THI 39, with a 95 percent interval that includes zero. Heat lowers milk fat content, while cold raises it.

Removing heat stress would have raised production by about 1.7 percent; removing both heat and cold would
have raised it by 2.9 percent. Applying the joint share uniformly to 2003–2024 production in the 48 contiguous
states gives an illustrative value of $23.9 billion, or $1.09 billion per year. These magnitudes depend on
the assumed response function, which the data cannot pin down. Evidence of adaptation is suggestive and
sensitive to specification.

## Interactive dashboard: earlier snapshot

[![Overview tab of the U.S. Dairy Heat-Stress Dashboard, with headline heat and cold effects on milk yield and fat content]({{ base_path }}/images/projects/dairy-dashboard-preview.jpg)]({{ base_path }}/dashboards/dairy-heat-stress/)

[Open the interactive dashboard]({{ base_path }}/dashboards/dairy-heat-stress/){: .btn .btn--info .btn--large}

The dashboard is an August 31, 2026 snapshot covering 2003–2025. It predates draft v1.5 and uses different
estimator choices and valuation calculations. Its charts and dollar losses do not represent the current
paper's results. Use the paper linked above for current estimates and their limitations.

## The decision

The scale and geographic distribution of climate-related production losses help inform cooling
infrastructure and adaptation support. The paper estimates production responses and illustrates their
economic scale; evaluating a particular investment also requires its costs and effectiveness.

## Approach

USDA NASS outcomes for 21 major dairy states are matched to hourly ERA5-Land weather aggregated using
county milk-cow inventory weights. State-by-calendar-month fixed effects absorb state seasonal cycles,
and year-month fixed effects absorb national monthly shocks.

The analysis compares linear and cubic regressions with LASSO and neural-network learners, with and
without automatic debiasing. Synthetic-data simulations guide estimator choice separately for heat and
cold, selecting a cubic regression for heat and a debiased neural network for cold. Both use two-way
clustered intervals. A break search finds no detectable change in yield responses, while the heat effect
on fat content weakens after the mid-2010s.

## Status

The current working paper is available above. The interactive dashboard remains available as an earlier
snapshot and has not been rebuilt to match this draft.
