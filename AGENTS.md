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
├── _includes/          # Reusable fragments + minima overrides (e.g. footer.html)
├── presentations/      # Static assets for presentations
├── assets/             # Static files (PDFs, scss, js)
├── _site/              # Generated site (gitignored)
└── vendor/             # Bundler dependencies (gitignored)
cv/
└── resume.yaml         # RenderCV source-of-truth
```

## Commands

```bash
docker-compose up                                    # Jekyll dev server at localhost:4000

# CV render + publish (run from cv/; needs Docker daemon running, e.g. OrbStack)
docker run --rm --entrypoint rendercv \
  -v "$PWD":/work -w /work rendercv/rendercv \
  render resume.yaml
cp rendercv_output/*.pdf ../docs/assets/Konstantinos_Chatzinikolakis_CV.pdf

# CV watch mode (re-renders on save; rendercv_output/ is gitignored)
docker run --rm -it --entrypoint rendercv \
  -v "$PWD":/work -w /work rendercv/rendercv \
  render resume.yaml --watch
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
- Source: `cv/resume.yaml` (RenderCV, `classic` theme; sole canonical source).
- Render produces `docs/assets/Konstantinos_Chatzinikolakis_CV.pdf` (canonical artifact).
- No HTML CV page — PDF linked from homepage CTA and footer.

## Theme & Deployment

- Theme: Minima with custom navigation (`header_pages` in `_config.yml`).
- Deployment: automatic on push to `main` → https://chatzinikolakisk.github.io
- GitHub Pages compatible gems only.
