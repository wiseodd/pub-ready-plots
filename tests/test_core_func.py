import matplotlib as plt
import pytest

from pub_ready_plots import get_mpl_rcParams

LAYOUTS = ["icml", "iclr", "neurips", "jmlr", "poster-portrait", "poster-landscape"]


@pytest.mark.parametrize("layout", LAYOUTS)
def test_correct_func(layout):
    rc_params, width_in, height_in = get_mpl_rcParams(1, 0.15, layout)
    plt.rcParams.update(rc_params)


def test_incorrect_width():
    with pytest.raises(ValueError):
        _, _, _ = get_mpl_rcParams(12, 0.1, "iclr")

    with pytest.raises(ValueError):
        _, _, _ = get_mpl_rcParams(0, 0.1, "iclr")

    with pytest.raises(ValueError):
        _, _, _ = get_mpl_rcParams(-3.2, 0.1, "iclr")


def test_incorrect_height():
    with pytest.raises(ValueError):
        _, _, _ = get_mpl_rcParams(0.15, 12, "iclr")

    with pytest.raises(ValueError):
        _, _, _ = get_mpl_rcParams(0.15, 0, "iclr")

    with pytest.raises(ValueError):
        _, _, _ = get_mpl_rcParams(0.15, -1.2, "iclr")


def test_incorrect_layout():
    with pytest.raises(ValueError):
        _, _, _ = get_mpl_rcParams(1, 1, "predatory_journal")
