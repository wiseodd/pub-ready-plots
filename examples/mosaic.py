import numpy as np

import pub_ready_plots as prp

########################################################################################
# Mosaic layout: subplots spanning multiple rows/columns
########################################################################################
# Each string row is a row of the grid; repeating a letter makes that subplot span
# those cells. Here "A" and "C" are wide, and "B" is tall.
with prp.get_context(
    layout=prp.Layout.NEURIPS,
    width_frac=1,  # between 0 and 1
    height_frac=0.25,  # between 0 and 1
    mosaic="AAB;CCB",  # or [["A", "A", "B"], ["C", "C", "B"]]
    width_ratios=[1, 1, 1.5],  # Additional keyword args for `plt.subplot_mosaic`
) as (fig, axs):
    # With `mosaic`, `axs` is a dict mapping each label to its Axes
    assert isinstance(axs, dict)

    x = np.linspace(-1, 1, 100)

    axs["A"].plot(x, np.sin(x))
    axs["A"].set_title("Sine")
    axs["A"].set_ylabel(r"$\mathrm{sin}(x)$")

    axs["C"].plot(x, np.cos(x))
    axs["C"].set_title("Cosine")
    axs["C"].set_xlabel(r"$x$")
    axs["C"].set_ylabel(r"$\mathrm{cos}(x)$")

    axs["B"].plot(x, np.tanh(x))
    axs["B"].set_title("Tanh")
    axs["B"].set_xlabel(r"$x$")
    axs["B"].set_ylabel(r"$\mathrm{tanh}(x)$")

    # Panel labels (a), (b), (c), taken from the mosaic keys. A left-aligned title
    # coexists with the centered one.
    for label, ax in axs.items():
        ax.set_title(f"({label.lower()})", loc="left", fontweight="bold")

    fig.savefig("mosaic.pdf")
