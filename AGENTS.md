# AGENTS.md

**Type:** Static site (Jekyll/GitHub Pages)

## Project

Personal blog + presentations + CV. Content written by engineering director.

## Structure

```
docs/
├── _config.yml         # Jekyll configuration
├── _posts/             # Blog posts (YYYY-MM-DD-title.md)
├── _drafts/            # Unpublished drafts (gitignored)
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
  date: YYYY-MM-DD 10:00:00 +0000
  categories: category-name
  ---
  ```
- Categories: `work`, `personal`, `tech` (single lowercase word, not an array).
- Structure: use `##` for section headings (5-7 sections max) and `---` before footer attributions.
- Voice: load the `writing-voice` skill before writing or editing posts. Use `docs/_posts/2025-12-01-engineering-hiring-journey.md` and `docs/_posts/2026-04-05-permission-to-explore.md` as voice references.
- Privacy: no real names in posts or drafts, write generic from the first draft. Map people to role or count (e.g. "the Integrations lead", "two of my engineers"); also genericize employer, vendors, and internal team/role names. Do not rely on a later cleanup pass.

### Presentations
- Source: `docs/_presentations/<slug>.html` (Reveal.js HTML with `layout: null` and `permalink: /presentations/<slug>/` or `/presentations/<slug>/<slug>.html`).
- Assets: `docs/presentations/<slug>/`; shared logos in `docs/presentations/assets/` (`logo.png` bottom-left, `upskill-tech.svg` bottom-right).
- Design system: warm parchment theme (`--bg-deep: #f9f3e5`, `--bg-card: #ffffff`), `Plus Jakarta Sans` + `JetBrains Mono`, 1280x720 fade transition, speaker notes in `<aside class="notes">`. See `docs/_presentations/tdd-for-tech-leads.html` for reusable CSS components (`.tag`, `.card`, `.two-col`, `.three-col`, `.sep`, `.stat`, `.cycle`).

### CV
- Source: `cv/resume.yaml` (RenderCV, `classic` theme; sole canonical source).
- Render produces `docs/assets/Konstantinos_Chatzinikolakis_CV.pdf` (canonical artifact).
- No HTML CV page: PDF linked from homepage CTA and footer.

## Theme & Deployment

- Theme: Minima with custom navigation (`header_pages` in `_config.yml`).
- Deployment: automatic on push to `main` -> https://chatzinikolakisk.github.io
- GitHub Pages compatible gems only.
