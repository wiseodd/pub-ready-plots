from contextlib import contextmanager
from typing import Any, Generator, Union

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from numpy import ndarray

from .styles import PAPER_FORMATS, Style


@contextmanager
def get_context(
    width_frac: float = 1,
    height_frac: float = 0.15,
    layout: str = "neurips",
    single_col: bool = False,
    nrows: int = 1,
    ncols: int = 1,
    override_rc_params: dict[str, Any] = dict(),
    **kwargs: Any,
) -> Generator[tuple[Figure, Union[Axes, ndarray[Any, Any]]], None, None]:
    rc_params, fig_width_in, fig_height_in = get_mpl_rcParams(
        width_frac, height_frac, layout, single_col
    )
    rc_params.update(override_rc_params)

    with plt.rc_context(rc_params):
        fig, axs = plt.subplots(nrows, ncols, constrained_layout=True, **kwargs)
        fig.set_size_inches(fig_width_in, fig_height_in)
        yield (fig, axs)


def get_mpl_rcParams(
    width_frac: float = 1,
    height_frac: float = 0.15,
    layout: str = "neurips",
    single_col: bool = False,
) -> tuple[dict[str, Any], float, float]:
    """Get matplotlib rcParams dict and fig width & height in inches, depending on the
    chosen layout and fractional width and height. Fractional here in the sense that
    The resulting fig width/height in inches is calculated as `width_frac\\linewidth` and
    `height_frac\\textheight` in LaTeX. Usage:

    ```python
        rc_params, fig_width_in, fig_height_in = pub_ready_plots.get_mpl_rcParams(
            width_frac=fig_width_frac, height_frac=fig_height_frac, layout="icml"
        )
        plt.rcParams.update(rc_params)

        fig, axs = plt.subplots(
            nrows,
            ncols,
            constrained_layout=True, # Important!
        )
        fig.set_size_inches(fig_width_in, fig_height_in)

        # Your plot here!

        plt.savefig("filename.pdf")
    ```

    Then in your LaTeX file, include the plot as follows:

    ```tex
        \\includegraphics[width=\\linewidth]{filename.pdf}
    ```

    The arg. `width=\\linewidth` is important!

    Args:
        width_frac: Fraction of `\\linewidth` as the figure width. Usually set to 1.
        height_frac: Fraction of `\\textheight` as the figure height. Try 0.175.
        layout: The LaTeX template used. Possible values are "icml", "iclr", "neurips",
            "jmlr", "poster-portrait" (A1, 2-column), and "poster-landscape" (A0, 3-col).
        single_col: Whether the plot is single column in a layout that has two columns
            (e.g. ICML). Not supported for any other layout.

    Returns:
        rc_params: Matplotlib key-value rc-params. Use it via
            `plt.rcParams.update(rc_params)`. Note that you can always override/add
            key-values to this dict before applying it.
        fig_width_in: figure width in inches.
        fig_height_in: figure height in inches.
    """
    if (width_frac <= 0 or width_frac > 1) or (height_frac <= 0 or height_frac > 1):
        raise ValueError("Both `width_frac` and `height_frac` must be between 0 and 1.")

    if layout not in PAPER_FORMATS.keys():
        raise ValueError(f"Layout must be in {list(PAPER_FORMATS.keys())}.")

    if layout not in ["icml", "aistats", "uai"] and single_col:
        raise ValueError("Double-column is only supported for ICML, AISTATS, and UAI.")

    format: Style = PAPER_FORMATS[layout]
    is_poster = "poster" in layout

    rc_params = {
        "text.usetex": False,
        "font.size": format.footnote_size,
        "font.family": "serif",
        "font.serif": format.font_name,
        "mathtext.fontset": "stixsans" if is_poster else "cm",
        "lines.linewidth": format.linewidth,
        "axes.linewidth": 0.5,
        "axes.titlesize": format.footnote_size,
        "axes.labelsize": format.script_size,
        "axes.unicode_minus": False,
        "axes.formatter.use_mathtext": True,
        "legend.fontsize": format.script_size,
        "xtick.major.size": format.tick_size,
        "ytick.major.size": format.tick_size,
        "xtick.major.width": format.tick_width,
        "ytick.major.width": format.tick_width,
    }

    w = width_frac * (format.col_width if single_col else format.text_width)
    h = height_frac * format.text_height

    return rc_params, w, h
