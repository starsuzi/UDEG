import numpy as np     
import matplotlib.pyplot as plt
import matplotlib

matplotlib.font_manager._rebuild()


#font = {'family' : 'Times New Roman',
#        'size'   : 14}
plt.rcParams["font.family"] = "Times New Roman"

y1 = [0.3566,0.4271, 0.4294, 0.4429, 0.4713, 0.4662]
x1 = [0,1,2,3,4,5]

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

#fig = plt.figure(figsize=(6, 6))
plt.plot(x1, y1, '--D')

#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')    # 설명 참고

plt.xlabel('Number of generated sentences',fontsize=14)
plt.ylabel('NDCG@3',fontsize=14)

#plt.axis('square')

plt.xticks(x1)

plt.show()



plt.savefig('./output/fig3.pdf', bbox_inches='tight', pad_inches=0)
plt.savefig('./output/fig3.png', bbox_inches='tight', pad_inches=0)