from typing import Sequence

import matplotlib as plt
import pytest

import pub_ready_plots as prp

LAYOUTS: Sequence[prp.Layout] = list(prp.Layout.__members__.values())


@pytest.mark.parametrize("layout", LAYOUTS)
def test_correct_func(layout: prp.Layout) -> None:
    rc_params, width_in, height_in = prp.get_mpl_rcParams(
        width_frac=1, height_frac=0.15, layout=layout
    )
    plt.rcParams.update(rc_params)


def test_incorrect_width() -> None:
    with pytest.raises(ValueError):
        _, _, _ = prp.get_mpl_rcParams(
            width_frac=12, height_frac=0.1, layout=prp.Layout.ICLR
        )

    with pytest.raises(ValueError):
        _, _, _ = prp.get_mpl_rcParams(
            width_frac=0, height_frac=0.1, layout=prp.Layout.ICLR
        )

    with pytest.raises(ValueError):
        _, _, _ = prp.get_mpl_rcParams(
            width_frac=-3.2, height_frac=0.1, layout=prp.Layout.ICLR
        )


def test_incorrect_height() -> None:
    with pytest.raises(ValueError):
        _, _, _ = prp.get_mpl_rcParams(
            width_frac=0.15, height_frac=12, layout=prp.Layout.ICLR
        )

    with pytest.raises(ValueError):
        _, _, _ = prp.get_mpl_rcParams(
            width_frac=0.15, height_frac=0, layout=prp.Layout.ICLR
        )

    with pytest.raises(ValueError):
        _, _, _ = prp.get_mpl_rcParams(
            width_frac=0.15, height_frac=-1.2, layout=prp.Layout.ICLR
        )


@pytest.mark.parametrize("layout", LAYOUTS)
def test_double_column(layout: prp.Layout) -> None:
    if layout in [
        prp.Layout.ICML,
        prp.Layout.AISTATS,
        prp.Layout.UAI,
        prp.Layout.POSTER_PORTRAIT,
        prp.Layout.POSTER_LANDSCAPE,
    ]:
        _ = prp.get_mpl_rcParams(
            width_frac=1, height_frac=0.1, layout=layout, single_col=False
        )

        _ = prp.get_mpl_rcParams(
            width_frac=1, height_frac=0.1, layout=layout, single_col=True
        )
    else:
        _ = prp.get_mpl_rcParams(
            width_frac=1, height_frac=0.1, layout=layout, single_col=False
        )

        with pytest.raises(ValueError):
            _ = prp.get_mpl_rcParams(
                width_frac=1, height_frac=0.1, layout=layout, single_col=True
            )
