import json
from pathlib import Path

import numpy as np
from matplotlib.axes import Axes

import pub_ready_plots as prp

########################################################################################
# Shared style file, e.g. for many slide figures
########################################################################################
# Load the rcParams overrides once; reuse them in every plotting script
with open(Path(__file__).parent / "plotstyle.json", "r") as f:
    rc_params = json.load(f)

with prp.get_context(
    layout=prp.Layout.TUOYING_169,
    width_frac=0.382,
    height_frac=0.8,
    override_rc_params=rc_params,  # Applied last, so these override the layout
) as (fig, ax):
    assert isinstance(ax, Axes)

    x = np.linspace(-1, 1, 100)

    ax.plot(x, np.sin(x), label=r"$\mathrm{sin}(x)$")
    ax.plot(x, np.cos(x), label=r"$\mathrm{cos}(x)$")
    ax.set_xlabel(r"$x$")
    ax.legend()

    fig.savefig("style_file.pdf")
