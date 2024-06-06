from typing import Any

import matplotlib as mpl
import matplotlib.font_manager as font_manager

cmfont = font_manager.FontProperties(fname=mpl.get_data_path() + "/fonts/ttf/cmr10.ttf")
FONT_NAME_CM = cmfont.get_name()
FONT_NAME_TNR = "Times New Roman"
FONT_NAME_AVENIR = "Avenir Next Condensed"

PAPER_FORMATS = {
    "icml": {
        "text_width": 6.00117,
        "col_width": 3.25063,
        "text_height": 8.50166,
        "font_name": FONT_NAME_TNR,
        "footnote_size": 8,
        "script_size": 7,
        "linewidth": 1.25,
        "tick_size": 1,
        "tick_width": 1,
    },
    "neurips": {
        "text_width": 5.50107,
        "col_width": 5.50107,
        "text_height": 9.00177,
        "font_name": FONT_NAME_TNR,
        "footnote_size": 8,
        "script_size": 7,
        "linewidth": 1.25,
        "tick_size": 1,
        "tick_width": 1,
    },
    "iclr": {
        "text_width": 5.50107,
        "col_width": 5.50107,
        "text_height": 9.00177,
        "font_name": FONT_NAME_TNR,
        "footnote_size": 8,
        "script_size": 7,
        "linewidth": 1.25,
        "tick_size": 1,
        "tick_width": 1,
    },
    "jmlr": {
        "text_width": 6.00117,
        "col_width": 6.00117,
        "text_height": 8.50166,
        "font_name": FONT_NAME_CM,
        "footnote_size": 8,
        "script_size": 7,
        "linewidth": 1.25,
        "tick_size": 1,
        "tick_width": 1,
    },
    "poster-landscape": {
        "text_width": 6.00117,
        "col_width": 6.00117,
        "text_height": 8.50166,
        "font_name": FONT_NAME_AVENIR,
        "footnote_size": 30,
        "script_size": 23,
        "linewidth": 3,
        "tick_size": 4,
        "tick_width": 2,
    },
    "poster-portrait": {
        "text_width": 6.00117,
        "col_width": 6.00117,
        "text_height": 8.50166,
        "font_name": FONT_NAME_AVENIR,
        "footnote_size": 10,
        "script_size": 8,
        "linewidth": 1,
        "tick_size": 1,
        "tick_width": 1,
    },
}


def get_mpl_rcParams(
    width_frac: float,
    height_frac: float,
    layout: str = "neurips",
    single_col: bool = False,
) -> tuple[dict[str, Any], float, float]:
    """Get matplotlib rcParams dict and fig width & height in inches, depending on the
    chosen layout and fractional width and height. Fractional here in the sense that
    The resulting fig width/height in inches is calculated as `width_frac\\linewidth` and
    `height_frac\\textheight` in LaTeX. Usage:

    ```python
        rc_params, fig_width_in, fig_height_in = pub_ready_plots.get_mpl_rcParams(
            width=fig_width_frac, height=fig_height_frac, layout="icml"
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

    if layout not in ["icml"] and single_col:
        raise ValueError("Double-column is only supported for ICML.")

    format = PAPER_FORMATS[layout]
    is_poster = "poster" in layout

    rc_params = {
        "text.usetex": False,
        "font.size": format["footnote_size"],
        "font.family": "serif",
        "font.serif": format["font_name"],
        "mathtext.fontset": "stixsans" if is_poster else "cm",
        "lines.linewidth": format["linewidth"],
        "axes.linewidth": 1,
        "axes.titlesize": format["footnote_size"],
        "axes.labelsize": format["script_size"],
        "axes.unicode_minus": False,
        "axes.formatter.use_mathtext": True,
        "legend.fontsize": format["script_size"],
        "xtick.major.size": format["tick_size"],
        "ytick.major.size": format["tick_size"],
        "xtick.major.width": format["tick_width"],
        "ytick.major.width": format["tick_width"],
    }

    w = width_frac * (format["col_width"] if single_col else format["text_width"])
    h = height_frac * format["text_height"]

    return rc_params, w, h
