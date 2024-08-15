from pub_ready_plots.pub_ready_plots import get_context, get_mpl_rcParams
import numpy as np


def test_correct_func():
    nrows, ncols = 3, 2
    with get_context(0.5, 0.15, nrows, ncols, "iclr") as (fig, axs):
        real_rc_params, fig_width_in, fig_height_in = get_mpl_rcParams(
            0.5, 0.15, "iclr"
        )

        assert np.allclose(
            fig.get_size_inches(), (fig_width_in, fig_height_in), atol=0.001
        )
        assert isinstance(axs, np.ndarray)
        assert axs.shape == (nrows, ncols)
