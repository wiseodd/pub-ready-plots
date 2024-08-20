import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes

import pub_ready_plots

########################################################################################
# User-specified rcParams override
########################################################################################
with pub_ready_plots.get_context(
    width_frac=1,
    height_frac=0.15,
    layout="iclr",
    override_rc_params={"lines.linewidth": 5},  # Pass your style overrides here!
) as (fig, ax):
    assert isinstance(ax, Axes)

    x = np.linspace(-1, 1, 100)

    ax.plot(x, np.sin(x))
    ax.set_title("Sine")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$\mathrm{sin}(x)$")

    fig.savefig("advanced_usage_1.pdf")


########################################################################################
# Manual, most-flexible way to use this library
########################################################################################
rc_params, fig_width_in, fig_height_in = pub_ready_plots.get_mpl_rcParams(
    width_frac=1,
    height_frac=0.15,
    layout="poster-portrait",
    single_col=False,
)

# You can update `rc_params` further before feeding it to `plt`, e.g.
rc_params.update({"axes.linewidth": 1})

# Use the styles globally.
# To make it local, use `with plt.rc_context(rc_params):`
plt.rcParams.update(rc_params)

fig, axs = plt.subplots(1, 2, constrained_layout=True)
fig.set_size_inches(fig_width_in, fig_height_in)

x = np.linspace(-1, 1, 100)

axs[0].plot(x, np.sin(x))
axs[0].set_title("Sine")
axs[0].set_xlabel(r"$x$")
axs[0].set_ylabel(r"$\mathrm{sin}(x)$")

axs[1].plot(x, np.cos(x))
axs[1].set_title("Cosine")
axs[1].set_xlabel(r"$x$")
axs[1].set_ylabel(r"$\mathrm{cos}(x)$")

fig.savefig("advanced_usage_2.pdf")
