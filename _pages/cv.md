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

[Download résumé (PDF)]({{ base_path }}/files/Resume_DuongTa.pdf)

Fields
======
* **Primary:** Applied Econometrics, Agricultural Economics
* **Secondary:** Environmental and Resource Economics

Education
======
* Ph.D. in Agricultural and Applied Economics, Virginia Tech, 2023 to expected May 2028
* M.Sc. in Business and Financial Economics, University of Greenwich, 2015
* B.A. in Economics, National Economics University, Vietnam, 2008

Work Experience
======
* **Graduate Research Assistant**, Virginia Tech, 2023 to present
  * Department of Agricultural and Applied Economics, Blacksburg, VA
* **Research Assistant and Data Analyst**, International Center for Tropical Agriculture (CIAT), Asia Hub, 2018 to 2022
  * Hanoi, Vietnam, held concurrently with the VIE research post
  * Contributed to salinity-intrusion impact assessment in the Mekong Delta (2019 to 2022) and cassava production and value-chain research in Vietnam (2019 to 2021)
  * Developed questionnaires and CSPro survey programs, supervised data collection, cleaned and analyzed data, and contributed to co-authored research
* **Researcher**, Vietnam Institute of Economics, 2010 to 2023
  * Hanoi, Vietnam
  * Led projects on the dynamics of farm and non-farm employment in Vietnam's rural economy (2022) and agricultural structure under climate change in the Mekong Delta (2021), from proposal development through analysis and final reports
  * Contributed to research on household economic functions, labour productivity, structural transformation, agricultural value chains, and farm-firm linkages

Research
======
{% for category in site.publication_category %}{% assign shown = false %}{% for post in site.publications reversed %}{% if post.category != category[0] %}{% continue %}{% endif %}{% unless shown %}<h3>{{ category[1].title }}</h3><ul>{% assign shown = true %}{% endunless %}{% include archive-single-cv.html %}{% endfor %}{% if shown %}</ul>{% endif %}{% endfor %}

Teaching
======
Graduate Teaching Assistant, Virginia Tech, 2023 to present. See the
[teaching page]({{ base_path }}/teaching/) for teaching philosophy and course readiness.

Skills
======
* **Statistical and econometric software:** Stata, R, Python, MATLAB, SQL, LaTeX
* **Geospatial and remote sensing:** Google Earth Engine
* **Machine learning and data science:** scikit-learn, TensorFlow, Keras
* **Reproducibility and collaboration:** Git, GitHub, Quarto, VS Code
* **Research methods:** Econometrics, causal inference, microeconomic methods, cost-benefit analysis, machine learning, survey design, experimental design, data management, data visualization
* **Additional training:** Machine Learning Specialization, Stanford University via Coursera (3 courses), 2025

Professional Membership
======
* Agricultural and Applied Economics Association (AAEA)

Languages
======
* Vietnamese (native), English (fluent)
