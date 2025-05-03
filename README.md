# Agustinus' _Very_ Opiniated Publication-Ready Plotting Library

<div align="center">

[![PyPI version](https://badge.fury.io/py/pub-ready-plots.svg)](https://badge.fury.io/py/pub-ready-plots)
[![codecov](https://codecov.io/github/wiseodd/pub-ready-plots/graph/badge.svg?token=N2I020J0RR)](https://codecov.io/github/wiseodd/pub-ready-plots)
![pytest](https://github.com/wiseodd/pub-ready-plots/actions/workflows/pytest.yml/badge.svg)
![mypy-lint](https://github.com/wiseodd/pub-ready-plots/actions/workflows/lint-mypy.yml/badge.svg)
![ruff-lint](https://github.com/wiseodd/pub-ready-plots/actions/workflows/lint-ruff.yml/badge.svg)
![ruff-format](https://github.com/wiseodd/pub-ready-plots/actions/workflows/format-ruff.yml/badge.svg)

</div>

<br />

I love TikZ (btw). I love [tikzplotlib](https://github.com/nschloe/tikzplotlib). I've been an
advocate for the latter ([proof](https://agustinus.kristia.de/blog/plotting/)). However, tikzplotlib is [as good as dead](https://github.com/nschloe/tikzplotlib/commits/main/). I need to move on.

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
import pub_ready_plots as prp

...

prp.get_context(
-   layout=prp.Layout.ICML,
+   layout=prp.Layout.POSTER_LANDSCAPE,

...
```

## Installation

Still with me? Still want to use this library? Here's how:

```bash
pip install --upgrade pub-ready-plots
```

## Quick usage

Wrap you current plotting script with the following `with` statement.
By default, this will create a full-width, `0.15\textheight` figure that conforms
to the specified template.

By doing this, your figure is guaranteed to have the correct scaling, dimensions,
font faces, and font sizes. All in all, this makes your figure "blends" with
the target venue's main template---your paper overall will look more professional!

```python
import pub_ready_plots as prp

with prp.get_context(layout=prp.Layout.ICLR) as (fig, axs):
    # Do whatever you want with `fig` and `axs`, e.g.:
    x = np.linspace(-1, 1)
    axs.plot(x, np.cos(x))

    # Once your done, save it, but do NOT set `tight_layout=True`!
    fig.savefig("filename.pdf")
```

Then in your LaTeX file, include the plot as follows:

```tex
\includegraphics[width=\linewidth]{filename.pdf}
```

The argument `width=\linewidth` is **crucial**! Also, do not specify the `height`
option! Otherwise, your plot is distorted. (All measurements have been done in
`pub-ready-plots`.)

If you set the `width_frac` argument when you call `prp.get_context()`, you need
to put the same scaling factor in your LaTeX code. E.g., if you call
`prp.get_context(..., width_frac=0.5, ...)`, then you include it via
`\includegraphics[width=0.5\linewidth]{...}`.

> [!WARNING]
> If you want to have multiple subplots in a single figure in your paper,
> **DO NOT** create multiple pdf files! Instead, follow
> [this example](#creating-subplots), while keeping
> `\includegraphics[width=\linewidth]` without a scaling factor.

That's it! But you should use TikZ more.
Anyway, see the full, runnable example in [`examples/simple_plot.py`](https://github.com/wiseodd/pub-ready-plots/blob/master/examples/simple_plot.py)
See [here](#all-available-options) for available options for `get_context()`!

> [!TIP]
> I recommend using this library in conjunction with
> [pypalettes](https://github.com/JosephBARBIERDARNAL/pypalettes)
> to avoid the generic blue-orange Matplotlib colors.
> Distinguish your plots from others!

## Advanced usages

### Creating a figure with multiple subplots

To create a figure with multiple subplots do the following.
Note that in your LaTeX doc, you still include the pdf via
`\includegraphics[width=\linewidth]`, without any scaling factor.

```python
with prp.get_context(
    layout=prp.Layout.NEURIPS,
    width_frac=1,
    height_frac=0.15,
    nrows=1,
    ncols=2,
    sharey=True,
) as (fig, axs):
    # As an example, we plot sine and cosine functions
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

    fig.savefig("subplots.pdf")
```

### Creating plots for `\wrapfigure`

Say we want to have an inline figure of size `0.4\textwidth` and
height `0.15\textheight` in our NeurIPS paper.
Then all we have to do is the following:

```python
import pub_ready_plots as prp

with prp.get_context(
    layout=prp.Layout.NEURIPS, width_frac=0.4, height_frac=0.15,
) as (fig, axs):
    # Your plot here!
    ...
    fig.savefig("mywrapfigure.pdf")
```

In our LaTeX doc, we can then use the `wrapfig` package and do the following:

```tex
Some paragraph.

\begin{wrapfigure}[11]{r}{0.4\textwidth}
  \centering
  \includegraphics[width=\linewidth]{mywrapfigure.pdf}
  ...
\end{wrapfigure}

Some other paragraph.
```

> [!IMPORTANT]
> In the `\begin{wrapfigure}` statement, specify the correct figure size
> (in our case, `0.4\textwidth`). Then, in the `\includegraphics` statement,
> **_always_** specify `width=\linewidth` _without_ specifying the height.

### Usage with Seaborn

This library is compatible with Seaborn, see [example](https://github.com/wiseodd/pub-ready-plots/blob/master/examples/with_seaborn.py).
The most important thing to remember is to always pass the axis returned by
`prp.get_context()` to Seaborn's plotting functions. Example:

```python
import seaborn as sns
import pub_ready_plots as prp

with prp.get_context(layout=prp.Layout.SLIDES_196) as (fig, ax):
    sns.histplot(
        data=sns.load_dataset("planets"), x="distance", log_scale=True
        ax=ax  # !! IMPORTANT !!
    )
```

### Fonts too bold?

You might encounter this problem on MacOS, e.g., when using Avenir Next Condensed font.
On MacOS, the font format is `.ttc` and Matplotlib has issue with it.
So, please install the more standard `.ttf` or `.otf` version.

You can also easily change the font, e.g.:

```python
import pub_ready_plots as prp

with prp.get_context(
    ...
    override_rc_params={"font.sans-serif": "YOUR_FONT_NAME"},
    ...
) as (fig, axs):
    ...
```

### All available options

```python
import pub_ready_plots as prp

with prp.get_context(
    layout=prp.Layout.ICML,  # check `Layout` for all available layouts
    width_frac=1,  # multiplier for `\linewidth`
    height_frac=0.15,  # multiplier for `\textheight`
    single_col=False,  # only works for the ICML, UAI, AISTATS layouts
    nrows=1,  # depending on your subplots, default = 1
    ncols=2,  # depending on your subplots, default = 1
    override_rc_params={"lines.linewidth": 4.123},  # Overriding rcParams
    sharey=True,  # Additional keyword args for `plt.subplots`
) as (fig, axs):
    ...

    fig.savefig("filename.pdf")
```

### Using your own styles

Two options:

1. Use this library and update the resulting `rc_params` dict with your styles.
   - See [`examples/advanced_usage.py`](https://github.com/wiseodd/pub-ready-plots/blob/master/examples/advanced_usage.py)
2. Fork this repo and modify things as you wish.

## Other libraries

Check out [tueplots](https://github.com/pnkraemer/tueplots) if you want a more complex
library. My library is designed to achieve what **_I_** want in **_my_** papers and
posters, with as little code as possible. Because of this, it is very forkable and hackable.
