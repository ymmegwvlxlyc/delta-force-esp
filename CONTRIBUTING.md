# Contributing to delta-force-esp

Community PRs welcome — offsets, menu polish, aimbot tuning.

## Ground rules
- No selling builds. No paid features. This is a hobby project.
- Update offsets before opening offset PRs — check `docs/offsets.md`.
- Run `pytest -q` before submitting.
- Keep comments minimal. The code is the doc.

## Adding a new ESP feature
1. Add draw primitive to `delta_force_esp/esp/box_renderer.py`
2. Wire toggle in `delta_force_esp/menu/imenu.py`
3. Add a test under `tests/`

## Reporting broken offsets
Open an issue with your game build string (see `docs/offsets.md`).
Educational purposes only — use at your own risk.