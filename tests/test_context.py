import numpy as np
import pytest
from matplotlib.axes import Axes

from pub_ready_plots import Layout, get_context, get_mpl_rcParams


def test_single_subplot() -> None:
    with get_context(width_frac=0.5, height_frac=0.15, layout=Layout.ICLR) as (
        fig,
        axs,
    ):
        real_rc_params, fig_width_in, fig_height_in = get_mpl_rcParams(
            width_frac=0.5, height_frac=0.15, layout=Layout.ICLR
        )

        assert np.allclose(
            fig.get_size_inches(), (fig_width_in, fig_height_in), atol=0.001
        )
        assert isinstance(axs, Axes)


def test_multi_subplots() -> None:
    nrows, ncols = 3, 2
    with get_context(
        width_frac=0.5, height_frac=0.15, nrows=nrows, ncols=ncols, layout=Layout.ICLR
    ) as (fig, axs):
        real_rc_params, fig_width_in, fig_height_in = get_mpl_rcParams(
            width_frac=0.5, height_frac=0.15, layout=Layout.ICLR
        )

        assert np.allclose(
            fig.get_size_inches(), (fig_width_in, fig_height_in), atol=0.001
        )
        assert isinstance(axs, np.ndarray)
        assert axs.shape == (nrows, ncols)


def test_override_rcparams() -> None:
    LINE_WIDTH: float = 8.2329232

    with get_context(
        width_frac=0.5,
        height_frac=0.15,
        layout=Layout.ICLR,
        override_rc_params={"lines.linewidth": LINE_WIDTH},
    ) as (fig, ax):
        assert isinstance(ax, Axes)

        x = np.linspace(-1, 1, 100)
        obj = ax.plot(x, np.tanh(x))
        assert np.allclose(obj[0].get_linewidth(), LINE_WIDTH)


def test_mosaic() -> None:
    with get_context(
        width_frac=0.5, height_frac=0.15, mosaic="AAB;CCB", layout=Layout.ICLR
    ) as (fig, axs):
        real_rc_params, fig_width_in, fig_height_in = get_mpl_rcParams(
            width_frac=0.5, height_frac=0.15, layout=Layout.ICLR
        )

        assert np.allclose(
            fig.get_size_inches(), (fig_width_in, fig_height_in), atol=0.001
        )
        assert isinstance(axs, dict)
        assert sorted(axs) == ["A", "B", "C"]
        assert all(isinstance(ax, Axes) for ax in axs.values())


def test_mosaic_ignores_nrows_ncols() -> None:
    with pytest.warns(UserWarning, match="ignored"):
        with get_context(layout=Layout.ICLR, mosaic="AB", nrows=2) as (fig, axs):
            assert isinstance(axs, dict)
            assert sorted(axs) == ["A", "B"]
