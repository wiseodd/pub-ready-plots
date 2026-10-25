from pathlib import Path
from typing import Sequence

import matplotlib as plt
import numpy as np
import pytest
from pypdf import PdfReader

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


@pytest.mark.parametrize("layout", LAYOUTS)
def test_no_type3_fonts(layout: prp.Layout, tmp_path: Path) -> None:
    FNAME = tmp_path / "temp.pdf"

    with prp.get_context(
        width_frac=0.5,
        height_frac=0.15,
        layout=layout,
    ) as (fig, ax):
        x = np.linspace(-1, 1)
        fx = np.sin(x)
        ax.plot(x, fx)
        fig.savefig(FNAME)

    font_subtypes = [
        font.get_object()["/Subtype"]
        for page in PdfReader(FNAME).pages
        for font in page["/Resources"]["/Font"].values()
    ]
    assert font_subtypes
    assert "/Type3" not in font_subtypes


SANS_LAYOUTS: Sequence[prp.Layout] = [
    prp.Layout.POSTER_LANDSCAPE,
    prp.Layout.POSTER_PORTRAIT,
    prp.Layout.SLIDES_169,
    prp.Layout.SLIDES_TUOYING_169,
]


@pytest.mark.parametrize("layout", SANS_LAYOUTS)
def test_sans_serif_layouts(layout: prp.Layout) -> None:
    rc_params, _, _ = prp.get_mpl_rcParams(layout=layout)
    assert rc_params["font.family"] == "sans-serif"
    assert rc_params["mathtext.fontset"] == "stixsans"


@pytest.mark.parametrize("layout", [x for x in LAYOUTS if x not in SANS_LAYOUTS])
def test_serif_layouts(layout: prp.Layout) -> None:
    rc_params, _, _ = prp.get_mpl_rcParams(layout=layout)
    assert rc_params["font.family"] == "serif"
    assert rc_params["mathtext.fontset"] == "cm"
