---
layout: default
title: Books
permalink: /books/
---

# Books

Favourites from my [Goodreads shelf]({{ site.data.books.profile }}).

{%- if site.data.books.currently_reading.size > 0 %}

## Currently reading

<div class="book-strip">
{%- for book in site.data.books.currently_reading %}
  {%- assign title = book.english_title | default: book.title %}
  <a class="book-mini" href="{{ book.url }}" title="{{ title }} by {{ book.author }}">
    <img src="{{ book.cover }}" alt="Cover of {{ title }}" loading="lazy">
    <span class="book-mini-text">
      <span class="book-title">{{ title }}</span>
      <span class="book-author">{{ book.author }}</span>
    </span>
  </a>
{%- endfor %}
</div>
{%- endif %}

## Favourites

<div class="book-grid">
{%- for book in site.data.books.favorites %}
  {%- assign title = book.english_title | default: book.title %}
  <a class="book-card" href="{{ book.url }}" title="{{ title }} by {{ book.author }}">
    <img src="{{ book.cover }}" alt="Cover of {{ title }}" loading="lazy">
    <span class="book-title">{{ title }}</span>
    <span class="book-author">{{ book.author }}</span>
  </a>
{%- endfor %}
</div>
