import pub_ready_plots
import numpy as np

with pub_ready_plots.get_context(
    width_frac=1,  # between 0 and 1
    height_frac=0.15,  # between 0 and 1
    nrows=1,  # depending on your subplots
    ncols=2,  # depending on your subplots
    layout="iclr",  # or "iclr", "neurips", "poster-portrait", "poster-landscape"
    single_col=False,  # only works for the "icml" layout
    sharey=True,  # Additional keyword args for `plt.subplots`
) as (fig, axs):
    x = np.linspace(-1, 1, 100)

    axs[0].plot(x, np.sin(x))
    axs[0].set_title("Sine")
    axs[0].set_xlabel(r"$x$")
    axs[0].set_ylabel(r"$\mathrm{sin}(x)$")

    axs[1].plot(x, np.cos(x))
    axs[1].set_title("Cosine")
    axs[1].set_xlabel(r"$x$")
    axs[1].set_ylabel(r"$\mathrm{cos}(x)$")

    fig.savefig("simple_plot.pdf")
