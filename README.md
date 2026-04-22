# Personal Website - Konstantinos Chatzinikolakis

Personal website featuring blog posts and technical presentations, built with Jekyll and hosted on GitHub Pages.

## 🚀 Quick Start

### Local Development with Docker

1. **Prerequisites**: Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

2. **Run locally**:
   ```bash
   docker-compose up
   ```

3. **View site**: Open http://localhost:4000

4. **Live reload**: Files update automatically when you save changes

### Adding Content

#### Blog Posts
Create new posts in `docs/_posts/` using this format:
```
docs/_posts/YYYY-MM-DD-title.md
```

Example front matter:
```yaml
---
layout: post
title: "Your Post Title"
date: 2025-01-15 10:00:00 +0000
categories: tech
---

Your content here...
```

#### Presentations
Add presentations to `docs/presentations/` directory. Existing presentations use Reveal.js.

## 🏗️ Structure

```
docs/
├── _config.yml          # Jekyll configuration
├── index.md             # Homepage
├── blog.md              # Blog listing page
├── presentations.md     # Presentations listing
├── _posts/              # Blog posts
│   └── YYYY-MM-DD-title.md
├── _presentations/      # Presentation source HTML (Reveal.js)
│   ├── day-in-life.html
│   └── tdd-for-tech-leads.html
└── presentations/       # Presentation assets (images, logos)
    ├── assets/          # Shared logos (logo.png, upskill-tech.svg)
    └── day-in-life/     # Day-in-life specific assets
```

## 🚀 Deployment

Automatically deployed to GitHub Pages on push to `main` branch.

View live site: https://chatzinikolakisk.github.io

## 🛠️ Tech Stack

- **Jekyll** - Static site generator
- **GitHub Pages** - Hosting
- **Reveal.js** - Presentations
- **Docker** - Local development
- **Markdown** - Content authoring

## 📝 Development Notes

- Jekyll uses the Minima theme
- Blog posts support categories and tags
- Live reload enabled for development
- GitHub Pages builds automatically





