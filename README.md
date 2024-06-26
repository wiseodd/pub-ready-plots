# Agustinus' _Very_ Opiniated Publication-Ready Plotting Library

I love TikZ (btw). I love [tikzplotlib](https://github.com/nschloe/tikzplotlib). I've been an
advocate for the latter ([proof](https://agustinus.kristia.de/techblog/2022/05/01/plotting/)). However, tikzplotlib is [as good as dead](https://github.com/nschloe/tikzplotlib/commits/main/). I need to move on.

> [!IMPORTANT]
> Here's what I use now for all my publication needs. This library is designed to be
> _*very*_ opiniated. Beauty is in the eye of the beholder. Also, it is _very_ simple,
> just a single file and that's it.

> [!NOTE]
> Of course I still use TikZ whenever possible (e.g. Fig. 1 in a paper, diagrams, etc.)

## Examples

**Left:** ICML (letter size), single-column layout. **Right:** A0 landscape poster, 3-column layout.

<div align="center">
    <img src="imgs/example_paper.png" width="40%"> &nbsp &nbsp &nbsp &nbsp <img src="imgs/example_poster.png" width="43.7%">
</div>

<br />

```diff
from pub_ready_plots import get_mpl_rcParams

rc_params, fig_width_in, fig_height_in = get_mpl_rcParams(
    width=1,
    height=0.15,
-   layout="icml",
+   layout="poster-landscape",
)
```

## Installation

Still with me? Still want to use this library? Here's how:

```bash
pip install pub-ready-plots
```

## Usage

```python
rc_params, fig_width_in, fig_height_in = pub_ready_plots.get_mpl_rcParams(
    width=1,  # between 0 and 1
    height=0.1,  # between 0 and 1
    layout="icml"  # or "iclr", "neurips", "poster-portrait", "poster-landscape"
)
plt.rcParams.update(rc_params)

fig, axs = plt.subplots(
    nrows,
    ncols,
    constrained_layout=True, # Important!
)
fig.set_size_inches(fig_width_in, fig_height_in)

# Your plot here!

plt.savefig("filename.pdf")
```

Then in your LaTeX file, include the plot as follows:

```tex
\includegraphics[width=\linewidth]{filename.pdf}
```

> [!IMPORTANT]
> The argument `width=\linewidth` is **crucial**!

> [!TIP]
> That's it! But you should use TikZ more.

## Using your own styles

Two options:

1. Fork this repo and modify things as you wish.
2. Use this library and update the resulting `rc_params` dict with your styles.

## Other libraries

Check out [tueplots](https://github.com/pnkraemer/tueplots) if you want a more complex
library. My library is designed to achieve what **_I_** want in **_my_** papers and
posters, with as little code as possible. Because of this, it is very forkable and hackable.
