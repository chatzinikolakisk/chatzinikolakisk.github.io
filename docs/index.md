---
layout: default
title: Konstantinos Chatzinikolakis
---

# Konstantinos Chatzinikolakis

Engineering director at Epignosis. Backend by trade. Eight years from IC to
director, modernizing platforms and growing engineers along the way.

I write about engineering leadership, legacy modernization, and the human side
of building software.

[Download CV (PDF)](/assets/Konstantinos_Chatzinikolakis_CV.pdf) ·
[Email](mailto:chatzinikolakisk@gmail.com) ·
[LinkedIn](https://www.linkedin.com/in/chatzinikolakisk) ·
[GitHub](https://github.com/chatzinikolakisk)

## Recent posts

{% for post in site.posts limit:3 %}
- [{{ post.title }}]({{ post.url }}) — {{ post.date | date: "%b %d, %Y" }}
{% endfor %}

[All posts →](/blog/)

## Recent talks

{% for presentation in site.presentations limit:3 %}
- [{{ presentation.title }}]({{ presentation.url }})
{% endfor %}

[All talks →](/presentations/)
