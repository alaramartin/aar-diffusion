import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

models = ["Pre-denoising", "Control", "Physics-informed"]
colors = ["#808080", "#2ecc40", "#e74c3c"]  # grey, green, red

data = {
    "PESQ": {
        "means": [1.97, 1.75, 1.75],
        "stds":  [0.75, 0.42, 0.41],
    },
    "ESTOI": {
        "means": [0.79, 0.73, 0.72],
        "stds":  [0.15, 0.13, 0.13],
    },
    "SI-SDR": {
        "means": [8.4,  11.7, 11.1],
        "stds":  [5.6,   3.7,   3.7],
    },
}

metrics = list(data.keys())
x = np.arange(len(models))
bar_width = 0.6

fig, axes = plt.subplots(1, 3, figsize=(13, 4.5))
fig.suptitle("Model Performance Across Metrics", fontsize=14, fontweight="bold")

for ax, metric in zip(axes, metrics):
    means = data[metric]["means"]
    stds  = data[metric]["stds"]

    bars = ax.bar(
        x,
        means,
        width=bar_width,
        color=colors,
        yerr=stds,
        capsize=5,
        error_kw=dict(elinewidth=1.5, capthick=1.5, ecolor="black"),
        zorder=3,
    )

    ax.set_title(metric, fontsize=12, fontweight="bold")
    ax.set_ylabel("Score", fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(models, fontsize=9)
    ax.tick_params(axis="y", labelsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig("model_performance.png", dpi=150, bbox_inches="tight")
print("Saved to model_performance.png")
plt.show()

