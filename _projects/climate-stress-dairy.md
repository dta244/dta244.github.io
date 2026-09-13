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
panel data with debiased machine learning approach*. This page will carry the reproducible code repository,
a data dictionary, validation results, and stated limitations once the work is complete.
