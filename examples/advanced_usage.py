import pub_ready_plots

import numpy as np
import matplotlib.pyplot as plt

rc_params, fig_width_in, fig_height_in = pub_ready_plots.get_mpl_rcParams(
    width_frac=1,  # between 0 and 1
    height_frac=0.15,  # between 0 and 1
    layout="poster-portrait",  # or "iclr", "neurips", "poster-portrait", "poster-landscape"
    single_col=False,  # only works for the "icml" layout
)
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

fig.savefig("advanced_usage.pdf")
