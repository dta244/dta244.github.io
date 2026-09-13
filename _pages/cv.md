---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

[Download full CV (PDF)]({{ base_path }}/files/CV_DuongTa.pdf)

<p style="font-size: 0.85em; color: var(--global-text-color-light);">
For non-academic roles, a one-page
<a href="{{ base_path }}/files/Resume_DuongTa.pdf">résumé</a> is also available.
</p>

Education
======
* Ph.D. in Agricultural and Applied Economics, Virginia Tech, 2023 to present
* M.Sc. in Business and Financial Economics, University of Greenwich, 2015
* B.A. in Economics, National Economics University, Vietnam, 2008

Experience
======
* **Graduate Research Assistant and Graduate Teaching Assistant**, Virginia Tech, 2023 to present
  * Department of Agricultural and Applied Economics, Blacksburg, VA
* **Data Analyst and Research Assistant**, International Center for Tropical Agriculture (CIAT), Asia Hub, 2018 to 2022
  * Hanoi, Vietnam
* **Researcher**, Vietnam Institute of Economics, 2010 to 2023
  * Hanoi, Vietnam

Skills
======
* **Programming:** Python, R, Stata, SQL, MATLAB, LaTeX
* **Machine learning:** scikit-learn, TensorFlow, Keras
* **Tools:** Git and GitHub, Google Earth Engine, Quarto, VS Code
* **Methods:** Econometrics and causal inference, experimental and survey design, optimization, cost-benefit analysis, spatial and remote-sensing data, data visualization

Research
======
{% for category in site.publication_category %}{% assign shown = false %}{% for post in site.publications reversed %}{% if post.category != category[0] %}{% continue %}{% endif %}{% unless shown %}<h3>{{ category[1].title }}</h3><ul>{% assign shown = true %}{% endunless %}{% include archive-single-cv.html %}{% endfor %}{% if shown %}</ul>{% endif %}{% endfor %}

Teaching
======
See the [teaching page]({{ base_path }}/teaching/) for teaching philosophy and experience.

Certifications
======
* Advanced Learning Algorithms, Stanford University via Coursera, 2025
* Unsupervised Learning, Recommenders, Reinforcement Learning, Stanford University via Coursera, 2025
* Supervised Machine Learning: Regression and Classification, Stanford University via Coursera, 2025

Professional Membership
======
* Agricultural and Applied Economics Association (AAEA)

Languages
======
* Vietnamese (native), English (fluent)
