# AGENTS.md

## Purpose

`pub-ready-plots` is a small, deliberately opinionated matplotlib helper that makes figures
match the dimensions, fonts, and font sizes of ML venue templates (ICML, NeurIPS, ICLR,
AISTATS, UAI, JMLR, TMLR, ProbML), A0/A1 posters, and 16:9 slides (Beamer, Typst Tuoying).
Users wrap their plotting code in `prp.get_context(layout=...)`, save a PDF, and include it in
LaTeX with `\includegraphics[width=\linewidth]{...}` (no height, no extra scaling). Keep it
simple and hackable: the maintainer wants as little code as possible, and the README points
people to `tueplots` if they want something more general.

## Layout

- `pub_ready_plots/styles.py`: the `Layout` enum and `PAPER_FORMATS`, mapping each layout to a
  `Style` (text/column width and text height in inches, font name, font sizes, line and tick
  widths).
- `pub_ready_plots/pub_ready_plots.py`: the public API.
  - `get_mpl_rcParams(layout, width_frac, height_frac, single_col)` returns
    `(rc_params, width_in, height_in)`. Width is `width_frac * text_width` (or `col_width` if
    `single_col`), and height is `height_frac * text_height`.
  - `get_context(...)` is a context manager that applies those rcParams via `plt.rc_context`,
    creates `plt.subplots(nrows, ncols, constrained_layout=True, **kwargs)`, sets the size,
    and yields `(fig, axs)`.
- `pub_ready_plots/__init__.py` exports `get_context`, `get_mpl_rcParams`, and `Layout`.
- `examples/` holds runnable usage scripts, `tests/` the pytest suite, and `imgs/` the README
  images.

## Commands

The project uses [uv](https://docs.astral.sh/uv/) and Python >= 3.11.

```bash
uv sync                 # install deps, including the dev group
make test               # uv run pytest --cov
make ruff               # ruff format + ruff check --fix
make mypy               # strict mypy on pub_ready_plots/ (tests excluded)
make lint               # ruff + mypy
uv run python examples/simple_plot.py
```

All test dependencies are in the `dev` group in `pyproject.toml` (e.g. `pypdf` for the Type 3
font check), so `uv sync` is enough and no system packages are needed. CI (on pull requests)
runs pytest with coverage, `ruff format --check`, `ruff check`, and mypy. All four must pass.

## Conventions

- Fully type-annotate everything in `pub_ready_plots/`, because mypy runs in `strict` mode.
- Ruff rules are `E4, E7, E9, F, I, PLE, PLW`. Imports are sorted by ruff (isort).
- Escape LaTeX backslashes in docstrings (`\\linewidth`).
- Keep the public API small. Prefer adding a `Style` entry or a parameter that gets passed
  through over adding new abstractions.

## Adding or changing a layout

1. Add a member to `Layout` and a matching `Style` in `PAPER_FORMATS` (`styles.py`). Take the
   dimensions in inches from the actual template (e.g. measure `\textwidth`, `\columnwidth`,
   and `\textheight` in LaTeX).
2. If the template has multiple columns, add it to the `single_col` allow-list in
   `get_mpl_rcParams`, and to the matching list in `tests/test_core_func.py::test_double_column`.
3. Posters and slides use sans-serif text and `stixsans` math. Papers use serif text and `cm`
   math. Which one a layout gets depends on whether its **enum name** contains `poster` or
   `slides`, so name new layouts accordingly.
4. Update the "Supported Layouts" list in `README.md` and the `layout` docstring in
   `get_mpl_rcParams`.
5. Tests parametrize over every `Layout` member, so a new layout is picked up automatically.

## Invariants (don't break)

- `"pdf.fonttype": 42` must stay in the rcParams. Venues reject PDFs with Type 3 fonts, and a
  test enforces this.
- `text.usetex` stays `False`, so no LaTeX install is required.
- `get_context` must keep `constrained_layout=True`. Users should not call
  `tight_layout`/`bbox_inches="tight"`, because that changes the figure size and breaks the
  `width=\linewidth` sizing contract.
- `width_frac` and `height_frac` must be in `(0, 1]`, otherwise a `ValueError` is raised.
- `override_rc_params` is applied after the computed rcParams, so user overrides win.

## Releasing

Bump `version` in `pyproject.toml`, then run `make build` and `make publish` (`uv build` /
`uv publish`). Only do this when the maintainer asks.
