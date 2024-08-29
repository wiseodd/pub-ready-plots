from dataclasses import dataclass
from enum import Enum

import matplotlib as mpl
import matplotlib.font_manager as font_manager

cmfont = font_manager.FontProperties(fname=mpl.get_data_path() + "/fonts/ttf/cmr10.ttf")
FONT_NAME_CM = cmfont.get_name()
FONT_NAME_TNR = "Times New Roman"
FONT_NAME_AVENIR = "Avenir Next Condensed"


class Layout(Enum):
    ICML = "icml"
    NEURIPS = "neurips"
    ICLR = "iclr"
    JMLR = "jmlr"
    UAI = "uai"
    AISTATS = "aistats"
    TMLR = "tmlr"
    POSTER_LANDSCAPE = "poster-landscape"
    POSTER_PORTRAIT = "poster-portrait"


@dataclass
class Style:
    text_width: float
    col_width: float
    text_height: float
    font_name: str
    footnote_size: int
    script_size: int
    linewidth: float
    tick_size: float
    tick_width: float


PAPER_FORMATS = {
    Layout.ICML: Style(
        text_width=6.00117,
        col_width=3.25063,
        text_height=8.50166,
        font_name=FONT_NAME_TNR,
        footnote_size=8,
        script_size=7,
        linewidth=1.25,
        tick_size=1.5,
        tick_width=0.5,
    ),
    Layout.NEURIPS: Style(
        text_width=5.50107,
        col_width=5.50107,
        text_height=9.00177,
        font_name=FONT_NAME_TNR,
        footnote_size=8,
        script_size=7,
        linewidth=1.25,
        tick_size=1.5,
        tick_width=0.5,
    ),
    Layout.ICLR: Style(
        text_width=5.50107,
        col_width=5.50107,
        text_height=9.00177,
        font_name=FONT_NAME_TNR,
        footnote_size=8,
        script_size=7,
        linewidth=1.25,
        tick_size=1.5,
        tick_width=0.5,
    ),
    Layout.JMLR: Style(
        text_width=6.00117,
        col_width=6.00117,
        text_height=8.50166,
        font_name=FONT_NAME_CM,
        footnote_size=8,
        script_size=7,
        linewidth=1.25,
        tick_size=1.5,
        tick_width=0.5,
    ),
    Layout.AISTATS: Style(
        text_width=6.75133,
        col_width=3.25063,
        text_height=9.25182,
        font_name=FONT_NAME_CM,
        footnote_size=8,
        script_size=7,
        linewidth=1.25,
        tick_size=1.5,
        tick_width=0.5,
    ),
    Layout.UAI: Style(
        text_width=6.75133,
        col_width=3.25063,
        text_height=9.25182,
        font_name=FONT_NAME_TNR,
        footnote_size=8,
        script_size=7,
        linewidth=1.25,
        tick_size=1.5,
        tick_width=0.5,
    ),
    Layout.TMLR: Style(
        text_width=6.50127,
        col_width=6.50127,
        text_height=9.00177,
        font_name=FONT_NAME_CM,
        footnote_size=8,
        script_size=7,
        linewidth=1.25,
        tick_size=1.5,
        tick_width=0.5,
    ),
    Layout.POSTER_LANDSCAPE: Style(
        # I made a conscious decision to set text_width = col_width since
        # posters are almost always per-column basis.
        # In any case, real_text_width=46.03267.
        text_width=12.8838,
        col_width=12.8838,
        text_height=27.04193,
        font_name=FONT_NAME_AVENIR,
        footnote_size=30,
        script_size=23,
        linewidth=3,
        tick_size=4,
        tick_width=2,
    ),
    Layout.POSTER_PORTRAIT: Style(
        # real_text_width=22.60286.
        text_width=9.34645,
        col_width=9.34645,
        text_height=29.10995,
        font_name=FONT_NAME_AVENIR,
        footnote_size=10,
        script_size=8,
        linewidth=1,
        tick_size=1,
        tick_width=1,
    ),
}
