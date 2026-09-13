# dta244.github.io

Personal academic website for Duong Phuc Ta, published at <https://dta244.github.io>.

Built with Jekyll on the [Academic Pages](https://github.com/academicpages/academicpages.github.io)
template and deployed by GitHub Pages from `master`.

## Layout

| Path | Contents |
| --- | --- |
| `_pages/about.md` | Homepage |
| `_pages/research.html` | Research index, renders `_publications` grouped by category |
| `_pages/projects.html` | Projects index, renders `_projects` as cards (card CSS lives in this file) |
| `_pages/teaching.md` | Teaching philosophy, experience, course readiness |
| `_pages/cv.md` | HTML CV, links `files/CV_DuongTa.pdf` and `files/Resume_DuongTa.pdf` |
| `_publications/` | One file per paper or presentation |
| `_projects/` | One file per applied project |
| `_config.yml` | Site settings, author profile, `publication_category` |
| `_data/navigation.yml` | Header menu |

## Adding a publication

Create a file in `_publications/` with front matter only. `category` must match a key in
`publication_category` in `_config.yml` (`JMP`, `WP`, `JA`, `JAV`, `CONF`); the display order of
sections follows the order of those keys.

```yaml
---
title: "Paper title"
collection: publications
category: WP
permalink: /publication/2027-short-slug
date: 2027-06-01
venue: 'Working paper'
paperurl: 'https://doi.org/...'
citation: 'Ta, Duong Phuc. 2027. "Paper title." Working paper.'
---
```

Optional keys: `slidesurl`, `bibtexurl`, `excerpt`. Anything below the front matter renders as the
paper's own page, which is where an abstract goes.

## Adding a project

Create a file in `_projects/`. The URL comes from the filename, so `_projects/my-thing.md` publishes at
`/projects/my-thing/`. Lead with the decision the work informs, not the method.

```yaml
---
title: "Project name"
collection: projects
date: 2027-03-01
status: "In progress"
role: "Sole author"
stack: "Python, Google Earth Engine"
question: "The decision a reader would make differently because of this work."
summary: "Two sentences on data and approach."
repourl: 'https://github.com/...'
dashboardurl: 'https://...'
paperurl: 'https://...'
---
```

The three URL keys are optional and the links row is hidden when all are absent. Body content becomes the
project's own page: the decision, the approach, what the analysis does and does not support.

Prefer static dashboards deployed in this repo over hosted apps on sleeping free tiers. A dead link reads
worse than no link.

## Local preview

Requires Ruby and Bundler.

```
bundle install
bundle exec jekyll serve -l -H localhost
```

`_config.yml` is not hot-reloaded, so restart the server after editing it.
