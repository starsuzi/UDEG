import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.font_manager._rebuild()


# font = {'family' : 'Times New Roman',
#        'size'   : 14}
plt.rcParams["font.family"] = "Times New Roman"

MAP_QL_LINE = [0.1728, 0.2078, 0.2125, 0.2224, 0.2306, 0.2364]
MAP_BM25_LINE = [0.2118, 0.2308, 0.2307, 0.2334, 0.2386, 0.2341]
MAP_QL_TOPK_LINE = [0.1728, 0.2053, 0.2152, 0.2202, 0.2201, 0.2177]
MAP_BM25_TOPK_LINE = [0.2118, 0.2291, 0.2277, 0.2239, 0.2189, 0.2149]


x1 = [0, 1, 2, 3, 4, 5]
plt.grid()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.plot(x1, MAP_BM25_LINE, "b*--", label="MCdrop(BM25)")
plt.plot(x1, MAP_QL_LINE, "r^--", label="MCdrop(QL)")
plt.plot(x1, MAP_BM25_TOPK_LINE, "go:", label="Top-K(BM25)")
plt.plot(x1, MAP_QL_TOPK_LINE, "cs:", label="Top-K(QL)")


# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')    # 설명 참고
axes = plt.axes()
axes.set_ylim([0.16, 0.25])

plt.xlabel("Number of generated sentences", fontsize=18)
plt.ylabel("MAP", fontsize=18)
plt.legend(loc=4, fontsize=18)

plt.xticks(x1)

#plt.show()


plt.savefig("./output/fig3.pdf", bbox_inches="tight", pad_inches=0)
plt.savefig("./output/fig3.png", bbox_inches="tight", pad_inches=0)
