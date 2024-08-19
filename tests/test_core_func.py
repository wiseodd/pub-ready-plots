import matplotlib as plt
import pytest

from pub_ready_plots import get_mpl_rcParams

LAYOUTS = ["icml", "iclr", "neurips", "jmlr", "poster-portrait", "poster-landscape"]


@pytest.mark.parametrize("layout", LAYOUTS)
def test_correct_func(layout):
    rc_params, width_in, height_in = get_mpl_rcParams(
        width_frac=1, height_frac=0.15, layout=layout
    )
    plt.rcParams.update(rc_params)


def test_incorrect_width():
    with pytest.raises(ValueError):
        _, _, _ = get_mpl_rcParams(width_frac=12, height_frac=0.1, layout="iclr")

    with pytest.raises(ValueError):
        _, _, _ = get_mpl_rcParams(width_frac=0, height_frac=0.1, layout="iclr")

    with pytest.raises(ValueError):
        _, _, _ = get_mpl_rcParams(width_frac=-3.2, height_frac=0.1, layout="iclr")


def test_incorrect_height():
    with pytest.raises(ValueError):
        _, _, _ = get_mpl_rcParams(width_frac=0.15, height_frac=12, layout="iclr")

    with pytest.raises(ValueError):
        _, _, _ = get_mpl_rcParams(width_frac=0.15, height_frac=0, layout="iclr")

    with pytest.raises(ValueError):
        _, _, _ = get_mpl_rcParams(width_frac=0.15, height_frac=-1.2, layout="iclr")


def test_incorrect_layout():
    with pytest.raises(ValueError):
        _, _, _ = get_mpl_rcParams(
            width_frac=0.5, height_frac=0.5, layout="predatory_journal"
        )
