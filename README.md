# dta244.github.io

Personal academic website for Duong Phuc Ta, published at <https://dta244.github.io>.

Built with Jekyll on the [Academic Pages](https://github.com/academicpages/academicpages.github.io)
template and deployed by GitHub Pages from `master`.

## Layout

| Path | Contents |
| --- | --- |
| `_pages/about.md` | Homepage |
| `_pages/research.html` | Research index, renders `_publications` grouped by category |
| `_pages/teaching.md` | Teaching philosophy, experience, course readiness |
| `_pages/cv.md` | HTML CV, links the PDF at `files/CV_DuongTa.pdf` |
| `_publications/` | One file per paper or presentation |
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

## Local preview

Requires Ruby and Bundler.

```
bundle install
bundle exec jekyll serve -l -H localhost
```

`_config.yml` is not hot-reloaded, so restart the server after editing it.
