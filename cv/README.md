# CV

Source-of-truth resume. Renders to PDF + Markdown via RenderCV (Docker).

## Files

- `resume.yaml` — canonical source (RenderCV schema, `engineeringresumes` theme).
- Rendered artifacts (committed under `docs/`):
  - `docs/assets/Konstantinos_Chatzinikolakis_CV.pdf` — downloadable from the `/cv/` page.
  - `docs/_includes/cv_body.md` — Markdown body included into `docs/cv.md`.

## Render + publish (run from `cv/`)

```sh
docker run --rm --entrypoint rendercv -v "$PWD":/work -w /work rendercv/rendercv render resume.yaml
cp rendercv_output/*.pdf ../docs/assets/Konstantinos_Chatzinikolakis_CV.pdf
sed -n '/^# Summary/,$p' rendercv_output/*.md > ../docs/_includes/cv_body.md
```

Three artifacts must move together on every publish: `resume.yaml`, `docs/assets/Konstantinos_Chatzinikolakis_CV.pdf`, `docs/_includes/cv_body.md`. Check `git status` before commit.

`rendercv_output/` is gitignored.

## Live reload

Re-renders on save. Open `rendercv_output/*.pdf` in a viewer that auto-reloads (Skim ideal; Preview.app reloads on focus).

```sh
docker run --rm -it --entrypoint rendercv -v "$PWD":/work -w /work rendercv/rendercv render resume.yaml --watch
```

## TODO

- [ ] GitHub Action: on push touching `cv/resume.yaml`, render PDF + trimmed MD, commit artifacts. Closes the drift gap.
- [ ] Resume-Matcher (self-hosted Docker, ATS scoring + JD tailoring): https://github.com/srbhr/Resume-Matcher
