import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.font_manager._rebuild()


# font = {'family' : 'Times New Roman',
#        'size'   : 14}
plt.rcParams["font.family"] = "Times New Roman"

topk_uniq_ratio = [
    0.9448207394,
    0.6942415745,
    0.5678619075,
    0.4889799775,
    0.4338080769,
]
mcdrop_uniq_ratio = [
    0.9406453566,
    0.7846631325,
    0.6860012474,
    0.6173860755,
    0.5657457197,
]


x1 = [1, 2, 3, 4, 5]
plt.grid()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.plot(x1, mcdrop_uniq_ratio, "r^--", label="MCdrop")
plt.plot(x1, topk_uniq_ratio, "b*--", label="top-k")


# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')    # 설명 참고
axes = plt.axes()
# axes.set_ylim([0.16, 0.25])

plt.xlabel("Number of generated sentences", fontsize=18)
plt.ylabel("Lexical Diversity", fontsize=18)
plt.legend(loc="best", fontsize=18)

plt.xticks(x1)

#plt.show()


plt.savefig("./output/fig5.pdf", bbox_inches="tight", pad_inches=0)
plt.savefig("./output/fig5.png", bbox_inches="tight", pad_inches=0)
