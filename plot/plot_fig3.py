import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.font_manager._rebuild()


# font = {'family' : 'Times New Roman',
#        'size'   : 14}
plt.rcParams["font.family"] = "Times New Roman"

MAP_QL_LINE = [0.2078, 0.2125, 0.2224, 0.2306, 0.2364]
MAP_BM25_LINE = [0.2308, 0.2307, 0.2334, 0.2386, 0.2341]
baseline_ql_value = 0.1728
baseline_bm25_value = 0.2118

x1 = [1, 2, 3, 4, 5]

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)


plt.axhline(
    y=baseline_bm25_value, color="g", linestyle="-", label="No Expan.(BM25)"
)

plt.axhline(
    y=baseline_ql_value, color="c", linestyle="--", label="No Expan.(QL)"
)

plt.plot(x1, MAP_BM25_LINE, "b*-", label="Ours(BM25)")

plt.plot(x1, MAP_QL_LINE, "ro-", label="Ours(QL)")


# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')    # 설명 참고
axes = plt.axes()
axes.set_ylim([0.15, 0.25])

plt.xlabel("Number of generated sentences", fontsize=14)
plt.ylabel("MAP", fontsize=14)
plt.legend(loc=4)

plt.xticks(x1)

plt.show()


plt.savefig("./output/fig3.pdf", bbox_inches="tight", pad_inches=0)
plt.savefig("./output/fig3.png", bbox_inches="tight", pad_inches=0)
