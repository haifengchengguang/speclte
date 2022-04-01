import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from pylab import mpl
from scipy.stats import gaussian_kde, stats
import seaborn as sns

mpl.rcParams['font.sans-serif']=['SimHei'] #黑体
mpl.rcParams['axes.unicode_minus']=False
allcbd=pd.read_csv(r"E:\学习资料\天文\作业五\20211123_150w_match_simbad\allL_notrepeat_wise.csv")
Jmag=allcbd['Jmag']
Hmag=allcbd['Hmag']
Kmag=allcbd['Kmag']
W1mag_W2mag=allcbd['W1mag-W2mag']
W2mag_W3mag=allcbd['W2mag-W3mag']
Jmag_Kmag=Jmag-Kmag
x=W2mag_W3mag
y=W1mag_W2mag
z=Jmag_Kmag
# xy = np.vstack([x, y])
# z = gaussian_kde(xy)(xy)
#
# # Sort the points by density, so that the densest points are plotted last
# idx = z.argsort()
# x, y, z = np.array(x)[idx], np.array(y)[idx], np.array(z)[idx]
#
# fig, ax = plt.subplots()
# plt.scatter(x, y, c=z, s=0.5, cmap='Spectral')
# plt.scatter(W2mag_W3mag, W1mag_W2mag,z=[],cmap='Spectral')
# plt.title('wise双色图')
# plt.xlabel('W2mag_W3mag')
# plt.ylabel('W1mag_W2mag')
# plt.rcParams['savefig.dpi'] = 300  # 图片像素
# plt.rcParams['figure.dpi'] = 300  # 分辨率
# plt.show()
# 上面的多总体hist 还是独立作图, 并没有将二者结合,
# 使用jointplot就能作出联合分布图形, 即, x总体和y总体的笛卡尔积分布
# 不过jointplot要限于两个等量总体.

# jointplot还是非常实用的, 对于两个连续型变量的分布情况, 集中趋势能非常简单的给出.
# 比如下面这个例子

with sns.axes_style("dark"):
    sns.jointplot(x=x, y=y,shade=True, kind="kde")
    #plt.vlines(0)
    plt.show()
    #plt.savefig("LTY_two_color.png")

# sns.set(style = "darkgrid")
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')
#
# ax.set_xlabel("W2mag-W3mag")
# ax.set_ylabel("W1mag-W2mag")
# ax.set_zlabel("Jmag-Kmag")
# ax.scatter(x, y, z)
#
# plt.show()
print("W1mag-W2mag:μ-3σ")
print(W1mag_W2mag.mean()-3*W1mag_W2mag.std())
print("W1mag-W2mag:μ+3σ")
print(W1mag_W2mag.mean()+3*W1mag_W2mag.std())
print("W2mag-W3mag:μ-3σ")
print(W2mag_W3mag.mean()-3*W2mag_W3mag.std())
print("W2mag-W3mag:μ+3σ")
print(W2mag_W3mag.mean()+3*W2mag_W3mag.std())
print("Jmag-Kmag:μ-3σ")
print(Jmag_Kmag.mean()-3*Jmag_Kmag.std())
print("Jmag-Kmag:μ+3σ")
print(Jmag_Kmag.mean()+3*Jmag_Kmag.std())

