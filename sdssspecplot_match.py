import os

import numpy as np
from astropy.io import fits
#testspec=fits.open('/Users/jeffreyburggraf/Documents/SDSS/spec-1234-55555-555.fits')
from cv2 import cv2
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from tqdm import tqdm
import pandas as pd
from tqdm import trange
filepath="G:\\fits1\\sdss"
matchfile="E:\学习资料\天文\作业五\sdss光谱\matchspec.csv"
df=pd.read_csv(matchfile)
print(len(df['ra']))
#df['ra']=df['ra'].apply(lambda x:float(x))
for i in trange(len(df['ra'])):
    if df['plate'][i]>=2427:
        fileName='spec-'+str(df['plate'][i])+'-'+str(df['mjd'][i])+'-'+str(df['fiberid'][i]).zfill(4)+'.fits'
        cur_path = os.path.join(filepath, fileName)
        if os.path.exists(cur_path):
            testspec = fits.open(cur_path)
            # print(type(testspec))
            # print(testspec.info())
            # for i in range(18):
            # print("testspec[0].header")
            # print(testspec[0].header)
            fileName1 = fileName.replace(".fits", "")

            # print(type(testspec[1].data[0][0]))
            # print('len(testspec)=' + str(len(testspec)))
            for j in range(len(testspec)):
                if testspec[j].data is not None:
                    if len(testspec[j].data.columns) == 8:
                        plt_x = np.empty(len(testspec[j].data))
                        plt_y = np.empty(len(testspec[j].data))
                        for i in range(len(testspec[j].data)):
                            plt_y[i] = testspec[j].data[i][0]
                            plt_x[i] = pow(10, testspec[j].data[i][1])
                        dst = cv2.GaussianBlur(src=plt_y, ksize=(29, 29), sigmaX=5)
                        plt_y = np.clip(dst, -80, 80)
                        plt.plot(plt_x, dst, color='black', linewidth=0.5)
                        plt.vlines(6708, ymin=min(plt_y), ymax=max(plt_y), colors="c", linestyles="solid", label='Li',
                                   linewidth=0.2)
                        plt.vlines(8183.8, ymin=min(plt_y), ymax=max(plt_y), colors="c", linestyles="solid", label='Na',
                                   linewidth=0.2)
                        plt.vlines(7000, ymin=min(plt_y), ymax=max(plt_y), colors="c", linestyles="solid", label='K',
                                   linewidth=0.2)
                        #plt.ylim(-500, 500)
                        plt.title(fileName1 + '-table' + str(j))
                        plt.xlabel('wavelength/Angstrom')
                        plt.ylabel('flux')
                        x_major_locator = MultipleLocator(500)
                        ax = plt.gca()
                        # ax为两条坐标轴的实例
                        ax.xaxis.set_major_locator(x_major_locator)
                        # 把x轴的主刻度设置为100的倍数
                        plt.tick_params(labelsize=5)
                        plt.rcParams['savefig.dpi'] = 300  # 图片像素
                        plt.rcParams['figure.dpi'] = 300  # 分辨率
                        plt.savefig('match/' + fileName1 + '-table' + str(j) + '.png')
                        #plt.show()
                        plt.close()
        # else:break

# file_list = os.listdir(filepath)
# count1=0
# for fileName in tqdm(file_list):
# #for fileName in file_list:
#     if fileName.endswith(".fits"):
#         # print(fileName)
#         cur_path = os.path.join(filepath, fileName)
#         # print(cur_path)

print("end")