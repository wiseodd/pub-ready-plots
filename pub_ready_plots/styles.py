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
        "tick_size": 1.5,
        "tick_width": 0.5,
    },
    "neurips": {
        "text_width": 5.50107,
        "col_width": 5.50107,
        "text_height": 9.00177,
        "font_name": FONT_NAME_TNR,
        "footnote_size": 8,
        "script_size": 7,
        "linewidth": 1.25,
        "tick_size": 1.5,
        "tick_width": 0.5,
    },
    "iclr": {
        "text_width": 5.50107,
        "col_width": 5.50107,
        "text_height": 9.00177,
        "font_name": FONT_NAME_TNR,
        "footnote_size": 8,
        "script_size": 7,
        "linewidth": 1.25,
        "tick_size": 1.5,
        "tick_width": 0.5,
    },
    "jmlr": {
        "text_width": 6.00117,
        "col_width": 6.00117,
        "text_height": 8.50166,
        "font_name": FONT_NAME_CM,
        "footnote_size": 8,
        "script_size": 7,
        "linewidth": 1.25,
        "tick_size": 1.5,
        "tick_width": 0.5,
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
        "tick_size": 1.5,
        "tick_width": 0.5,
    },
}
