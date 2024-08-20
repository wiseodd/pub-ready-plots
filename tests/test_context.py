import numpy as np
from matplotlib.axes import Axes

from pub_ready_plots.pub_ready_plots import get_context, get_mpl_rcParams


def test_single_subplot():
    with get_context(width_frac=0.5, height_frac=0.15, layout="iclr") as (fig, axs):
        real_rc_params, fig_width_in, fig_height_in = get_mpl_rcParams(
            width_frac=0.5, height_frac=0.15, layout="iclr"
        )

        assert np.allclose(
            fig.get_size_inches(), (fig_width_in, fig_height_in), atol=0.001
        )
        assert isinstance(axs, Axes)


def test_multi_subplots():
    nrows, ncols = 3, 2
    with get_context(
        width_frac=0.5, height_frac=0.15, nrows=nrows, ncols=ncols, layout="iclr"
    ) as (fig, axs):
        real_rc_params, fig_width_in, fig_height_in = get_mpl_rcParams(
            width_frac=0.5, height_frac=0.15, layout="iclr"
        )

        assert np.allclose(
            fig.get_size_inches(), (fig_width_in, fig_height_in), atol=0.001
        )
        assert isinstance(axs, np.ndarray)
        assert axs.shape == (nrows, ncols)


def test_override_rcparams():
    LINE_WIDTH: float = 8.2329232

    with get_context(
        width_frac=0.5,
        height_frac=0.15,
        layout="iclr",
        override_rc_params={"lines.linewidth": LINE_WIDTH},
    ) as (fig, ax):
        assert isinstance(ax, Axes)

        x: np.ndarray = np.linspace(-1, 1, 100)
        obj = ax.plot(x, np.tanh(x))
        assert np.allclose(obj[0].get_linewidth(), LINE_WIDTH)
