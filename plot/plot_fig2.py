import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams.update({"font.size": 14})

labels = ["BM25", "BM25+RM3", "QL", "QL+RM3"]
baseline = [0.4372, 0.424, 0.3566, 0.277]
bart = [0.4528, 0.4536, 0.4107, 0.3513]
pegasus = [0.4751, 0.4707, 0.418, 0.3302]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots(figsize=(7.2, 4.5))
rects1 = ax.bar(
    x - width,
    baseline,
    width,
    label="No Expan.",
    color="green",
    edgecolor="black",
)
rects2 = ax.bar(
    x, bart, width, label="BART", hatch="\\", color="red", edgecolor="black"
)
rects3 = ax.bar(
    x + width,
    pegasus,
    width,
    label="PEGASUS",
    hatch="//",
    color="blue",
    edgecolor="black",
)


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("MAP")
ax.set_ylim([0.2, 0.5])
# ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            "{}".format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
        )


# autolabel(rects1)
# autolabel(rects2)
# autolabel(rects3)

fig.tight_layout()

# plt.show()

plt.savefig("./output/fig2.pdf", bbox_inches="tight", pad_inches=0)
plt.savefig("./output/fig2.png", bbox_inches="tight", pad_inches=0)
