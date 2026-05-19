# AGENTS.md

**Type:** Static site (Jekyll/GitHub Pages)

## Project

Personal blog + presentations + CV. Content written by engineering director.

## Structure

```
docs/
├── _config.yml         # Jekyll configuration
├── _posts/             # Blog posts (YYYY-MM-DD-title.md)
├── _drafts/            # Unpublished drafts
├── _presentations/     # HTML presentations (Jekyll collection)
├── _includes/          # Reusable fragments (e.g. cv_body.md)
├── presentations/      # Static assets for presentations
├── assets/             # Static files (PDFs, scss, js)
├── cv.md               # CV page wrapper (renders /cv/)
├── _site/              # Generated site (gitignored)
└── vendor/             # Bundler dependencies (gitignored)
cv/
├── resume.yaml         # RenderCV source-of-truth
└── README.md           # Render + publish ritual
```

## Commands

```bash
docker-compose up                                    # Jekyll dev server at localhost:4000
docker run --rm --entrypoint rendercv \
  -v "$PWD":/work -w /work rendercv/rendercv \
  render resume.yaml                                 # CV render (from cv/)
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
- Categories: `work`, `personal`, `tech`

### Presentations
- Location: `docs/_presentations/` (HTML with Reveal.js)
- Assets: `docs/presentations/[presentation-name]/`

### CV
- Source: `cv/resume.yaml` (RenderCV, `engineeringresumes` theme).
- Render produces `docs/assets/Konstantinos_Chatzinikolakis_CV.pdf` + `docs/_includes/cv_body.md`.
- Page wrapper: `docs/cv.md`. See `cv/README.md` for publish ritual.

## Theme & Deployment

- Theme: Minima with custom navigation (`header_pages` in `_config.yml`).
- Deployment: automatic on push to `main` → https://chatzinikolakisk.github.io
- GitHub Pages compatible gems only.
