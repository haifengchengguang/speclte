import numpy as np
import pandas as pd

params_avg=pd.read_csv(r"E:\学习资料\天文\作业五\sdss5000-5500k\params_avg.csv")
theory=pd.read_csv(r'E:\学习资料\天文\作业五\20211219_光谱响应曲线卷积\theory.csv')
rmag_diff=params_avg['rmag']-theory['rmag']
imag_diff=params_avg['imag']-theory['imag']
zmag_diff=params_avg['zmag']-theory['zmag']
Jmag_diff=params_avg['Jmag']-theory['Jmag']
Hmag_diff=params_avg['Hmag']-theory['Hmag']
Kmag_diff=params_avg['Kmag']-theory['Kmag']
W1mag_diff=params_avg['W1mag']-theory['W1mag']
W2mag_diff=params_avg['W2mag']-theory['W2mag']
W3mag_diff=params_avg['W3mag']-theory['W3mag']
W4mag_diff=params_avg['W4mag']-theory['W4mag']

DIFF_mag = pd.concat(
        [rmag_diff, imag_diff, zmag_diff, Jmag_diff, Hmag_diff, Kmag_diff, W1mag_diff, W2mag_diff, W3mag_diff,W4mag_diff], axis=1)
print(DIFF_mag)
np.savetxt('params_diff.csv',DIFF_mag,fmt="%f",delimiter=',')