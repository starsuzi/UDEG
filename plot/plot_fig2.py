import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams.update({'font.size': 14})

labels = ['BM25', 'BM25+RM3', 'QL', 'QL+RM3']
bart = [0.4528,0.4536, 0.4107,0.3513]
pegasus = [0.4751, 0.4707, 0.418, 0.3302]



x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, bart, width, label='BART')
rects2 = ax.bar(x + width/2, pegasus, width, label='PEGASUS')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('NDCG@3')
#ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


#autolabel(rects1)
#autolabel(rects2)

fig.tight_layout()

plt.show()

plt.savefig('./output/fig2.pdf', bbox_inches='tight', pad_inches=0)
plt.savefig('./output/fig2.png', bbox_inches='tight', pad_inches=0)