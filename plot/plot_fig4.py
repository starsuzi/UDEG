import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams.update({"font.size": 14})

labels = ["BM25", "BM25+RM3", "QL", "QL+RM3"]

base = [0.2118, 0.2121, 0.1728, 0.1504]
mc = [0.2386, 0.2344, 0.2306, 0.2121]
topk = [0.2189, 0.217, 0.2201, 0.1998]


x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots(figsize=(7.2, 4.5))
rects1 = ax.bar(
    x,
    base,
    width,
    label="No Expan.",
    color="green",
    edgecolor="black",
)
rects2 = ax.bar(
    x + width,
    mc,
    width,
    label="MC dropout",
    hatch="\\",
    color="red",
    edgecolor="black",
)
rects3 = ax.bar(
    x + width * 2,
    topk,
    width,
    label="Top-K",
    color="blue",
    hatch="//",
    edgecolor="black",
)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("MAP")
# ax.set_title('Scores by group and gender')
ax.set_ylim([0.1, 0.26])
ax.set_xticks(x + 0.25)
ax.set_xticklabels(labels)
ax.legend(fontsize=12)


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

fig.tight_layout()

plt.show()

plt.savefig("./output/fig4.pdf", bbox_inches="tight", pad_inches=0)
plt.savefig("./output/fig4.png", bbox_inches="tight", pad_inches=0)
