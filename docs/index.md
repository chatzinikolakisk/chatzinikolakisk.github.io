---
layout: default
title: Home
---

# Welcome

Hi, I'm Konstantinos Chatzinikolakis, a software engineer passionate about technology and sharing knowledge.

## Recent Blog Posts

{% for post in site.posts limit:3 %}
- [{{ post.title }}]({{ post.url }}) - {{ post.date | date: "%B %d, %Y" }}
{% endfor %}

[View all posts →](/blog/)

## Latest Presentations

{% for presentation in site.presentations limit:2 %}
- [{{ presentation.title }}]({{ presentation.url }})
{% endfor %}

[View all presentations →](/presentations/)

---

*Built with Jekyll and hosted on GitHub Pages*