import numpy as np
import seaborn as sns

import pub_ready_plots as prp

# Set your seaborn style & palette *outside* of the `with` statement
sns.set_style("whitegrid")
sns.set_palette("pastel")

with prp.get_context(
    layout=prp.Layout.NEURIPS,
    width_frac=1,
    height_frac=0.15,
    nrows=1,
    ncols=2,
    sharey=True,
) as (fig, axs):
    # If `nrows` or `ncols` are not 1, `axs` is a NumPy array containing Axes'
    assert isinstance(axs, np.ndarray)

    x = np.linspace(-1, 1, 100)

    axs[0].plot(x, np.sin(x))
    axs[0].set_title("Sine")
    axs[0].set_xlabel(r"$x$")
    axs[0].set_ylabel(r"$\mathrm{sin}(x)$")

    axs[1].plot(x, np.cos(x))
    axs[1].plot(x, 2 * np.cos(x))
    axs[1].set_title("Cosine")
    axs[1].set_xlabel(r"$x$")
    axs[1].set_ylabel(r"$\mathrm{cos}(x)$")

    fig.savefig("seaborn.pdf")
