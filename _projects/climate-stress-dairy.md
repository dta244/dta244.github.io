---
title: "Climate Stress and U.S. Dairy Production"
collection: projects
date: 2026-01-01
status: "In progress"
role: "Sole author"
stack: "Python, double/debiased machine learning, panel data"
question: "How much production does heat stress cost U.S. dairy operations, and which herds absorb it worst?"
summary: "Applies double/debiased machine learning to multi-year panel data to separate the causal effect of climate stress on milk output from the many confounders that move with weather, allowing flexible controls without hand-specifying functional form."
---

{% include base_path %}

## Interactive dashboard

[![Overview tab of the U.S. Dairy Heat-Stress Dashboard, with headline heat and cold effects on milk yield and fat content]({{ base_path }}/images/projects/dairy-dashboard-preview.jpg)]({{ base_path }}/dashboards/dairy-heat-stress/)

[Open the interactive dashboard]({{ base_path }}/dashboards/dairy-heat-stress/){: .btn .btn--info .btn--large}

The dashboard covers 2003 to 2025. It shows the estimated effects of heat and cold stress on milk yield and fat
content, the resulting production and dollar losses nationally and for each of the 48 contiguous states, and
how the effects shift from year to year. These are preliminary results from a dated snapshot and may change
before the paper is published.

## The decision

Heat stress lowers milk yield, but the size of the effect drives real decisions: how much cooling
infrastructure is worth installing, how insurers should price weather exposure, and where adaptation support
does the most good. Point estimates that ignore confounding or impose the wrong functional form give
misleading guidance on all three.

## Approach

Double/debiased machine learning lets flexible learners absorb high-dimensional controls while preserving
valid inference on the treatment effect. The panel structure supports temporal validation, and the
specification is compared against a transparent baseline so the gain from the more complex method is visible
rather than assumed.

## Status

Analysis in progress, as the working paper *Estimating impacts of climate stress on US milk production: a
panel data with debiased machine learning approach*. The dashboard above shows the current estimates. This
page will add the reproducible code repository, a data dictionary, full validation results, and stated
limitations once the work is complete.
