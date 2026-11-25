---
layout: default
title: Projects
permalink: /projects/
---

# Projects

Games, experiments and ideas I build on the side, mostly vibe coded.

<div class="project-list">
{%- assign projects = site.data.projects | sort: "date" | reverse -%}
{%- for project in projects %}
  <a class="project-card" href="{{ project.url | relative_url }}">
    <div class="project-meta">
      <span class="project-kind">{{ project.kind }}</span>
      <span class="project-status project-status-{{ project.status }}">{{ project.status }}</span>
      <time datetime="{{ project.date | date_to_xmlschema }}">{{ project.date | date: "%b %Y" }}</time>
    </div>
    <h2 class="project-title">{{ project.title }}</h2>
    <p class="project-summary">{{ project.summary }}</p>
    {%- if project.tags %}
    <ul class="project-tags">
      {%- for tag in project.tags %}<li>{{ tag }}</li>{% endfor -%}
    </ul>
    {%- endif %}
  </a>
{%- endfor %}
</div>
