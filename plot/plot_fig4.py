import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams.update({'font.size': 14})

labels = ['BM25', 'BM25+RM3', 'QL', 'QL+RM3']

base = [0.4372,0.424,0.3566,0.277 ]
mc = [0.478,0.4705,0.4713,0.4247]
topk = [0.3093, 0.2882, 0.3143, 0.2843]


x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x , base, width, label='No Expan.')
rects2 = ax.bar(x + width, mc, width, label='MC dropout')
rects3 = ax.bar(x + width*2, topk, width, label='TopK')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('NDCG@3')
#ax.set_title('Scores by group and gender')
ax.set_xticks(x+0.25)
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

plt.savefig('./output/fig4.pdf', bbox_inches='tight', pad_inches=0)
plt.savefig('./output/fig4.png', bbox_inches='tight', pad_inches=0)