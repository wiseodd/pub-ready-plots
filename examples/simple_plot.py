import pub_ready_plots

import numpy as np
from matplotlib.axes import Axes

########################################################################################
# Single plot (i.e. no subplots)
########################################################################################
with pub_ready_plots.get_context(
    width_frac=1,  # between 0 and 1
    height_frac=0.15,  # between 0 and 1
    layout="iclr",  # or "iclr", "neurips", "poster-portrait", "poster-landscape"
) as (fig, ax):
    # Just like in `plt.subplots`, `ax` is a matplotlib Axes if
    # nrows & ncols are not specified (both default to 1).
    assert isinstance(ax, Axes)

    x = np.linspace(-1, 1, 100)

    ax.plot(x, np.sin(x))
    ax.set_title("Sine")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$\mathrm{sin}(x)$")

    fig.savefig("simple_plot.pdf")

########################################################################################
# Multiple subplots
########################################################################################
with pub_ready_plots.get_context(
    width_frac=1,  # between 0 and 1
    height_frac=0.15,  # between 0 and 1
    nrows=1,  # depending on your subplots
    ncols=2,  # depending on your subplots
    layout="iclr",  # or "iclr", "neurips", "poster-portrait", "poster-landscape"
    single_col=False,  # only works for the "icml" layout
    sharey=True,  # Additional keyword args for `plt.subplots`
) as (fig, axs):
    # If `nrows` or `ncols` are not 1, `axs` is a NumPy array containing Axes'
    assert isinstance(axs, np.ndarray)

    x = np.linspace(-1, 1, 100)

    axs[0].plot(x, np.sin(x))
    axs[0].set_title("Sine")
    axs[0].set_xlabel(r"$x$")
    axs[0].set_ylabel(r"$\mathrm{sin}(x)$")

    axs[1].plot(x, np.cos(x))
    axs[1].set_title("Cosine")
    axs[1].set_xlabel(r"$x$")
    axs[1].set_ylabel(r"$\mathrm{cos}(x)$")

    fig.savefig("simple_subplots.pdf")
