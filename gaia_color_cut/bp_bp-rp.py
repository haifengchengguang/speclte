import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from pylab import mpl
from scipy.stats import gaussian_kde, stats
import seaborn as sns

mpl.rcParams['font.sans-serif']=['SimHei'] #黑体
mpl.rcParams['axes.unicode_minus']=False
allcbd=pd.read_csv(r"E:\学习资料\天文\作业五\20211123_150w_match_simbad\LTY\cbdGaiaAbsolute.csv")

bp_rp=allcbd['bp_rp']
bp=allcbd['absolute_bp']
G=allcbd['absolute_G']
rp=allcbd['absolute_rp']
y=rp
x=bp_rp
with sns.axes_style("dark"):
    g=sns.jointplot(x=x, y=y)
    g.plot_joint(sns.kdeplot, color="r", zorder=0, levels=10)
    g.plot_marginals(sns.rugplot, color="r", height=-.15, clip_on=False)
    #plt.vlines(0)
    plt.show()