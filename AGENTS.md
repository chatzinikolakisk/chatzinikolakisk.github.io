# AGENTS.md

**Generated:** 2026-04-22
**Type:** Static site (Jekyll/GitHub Pages)

## Project

Personal blog + presentations. Content written by engineering director.

## Structure

```
docs/
├── _config.yml         # Jekyll configuration
├── _posts/             # Blog posts (YYYY-MM-DD-title.md)
├── _presentations/     # HTML presentations (Jekyll collection)
├── presentations/      # Static assets for presentations
├── _site/             # Generated site (ignored in git)
└── vendor/            # Bundler dependencies (ignored in git)
```

## Commands

```bash
docker-compose up  # Dev server at localhost:4000
```

## Content Patterns

### Blog Posts
- Location: `docs/_posts/YYYY-MM-DD-title.md`
- Front matter:
  ```yaml
  ---
  layout: post
  title: "Post Title"
  date: YYYY-MM-DD HH:MM:SS +0000
  categories: category-name
  ---
  ```
- Categories: work, personal, tech

### Presentations
- Location: `docs/_presentations/` (HTML with Reveal.js)
- Assets: `docs/presentations/[presentation-name]/`

## Theme & Deployment

- Theme: Minima with custom navigation (blog.md, presentations.md)
- Deployment: automatic on push to main → https://chatzinikolakisk.github.io
- Uses GitHub Pages compatible gems only

## User Preferences (How I Work)

- **Be tight on what, silent on how** - define constraints, not methods
- **Create space** - exploratory work should feel brave, not require permission
- **Constraint-based over method-prescriptive** - "every API has contract tests" > "follow these 14 rules"
- **No territorial behavior** - don't gatekeep exploration

## Anti-Patterns (THIS PROJECT)

- Process as control (using governance language to shut down exploration)
- Requiring permission for exploratory code
- Senior unilaterally deciding then enforcing process on others