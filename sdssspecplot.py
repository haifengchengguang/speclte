import os

import numpy as np
from astropy.io import fits
#testspec=fits.open('/Users/jeffreyburggraf/Documents/SDSS/spec-1234-55555-555.fits')
from matplotlib import pyplot as plt

filepath="G:\\fits1\\sdss"
file_list = os.listdir(filepath)
count1=0
for fileName in file_list:
    if count1<=3:
        count1+=1
        if fileName.endswith(".fits"):
            # print(fileName)
            cur_path = os.path.join(filepath, fileName)
            # print(cur_path)
            testspec = fits.open(cur_path)
            #print(type(testspec))
            print(testspec.info())
            #for i in range(18):
            print("testspec[0].header")
            print(testspec[0].header)
            fileName1=fileName.replace(".fits","")
            print(type(testspec[1].data[0][0]))
            plt_x=np.empty(len(testspec[1].data))
            plt_y=np.empty(len(testspec[1].data))
            for i in range(len(testspec[1].data)):
                plt_y[i]=testspec[1].data[i][0]
                plt_x[i]=pow(10,testspec[1].data[i][1])
            plt.plot(plt_x,plt_y, color='black',label=fileName1,linewidth=0.1)
            #plt.xlim(2980, 11230)
            plt.xlabel('wavelength/Angstrom')
            plt.ylabel('flux')
            plt.rcParams['savefig.dpi'] = 300  # 图片像素
            plt.rcParams['figure.dpi'] = 300  # 分辨率
            plt.savefig('sdsslatem6/'+fileName1+'table01'+'.png')
            plt.show()
            #plt.close()
            #plt.clf()
            #plt.cla()
            #plt.close()
            #plt.clf()
            #plt.cla()
            #plt.close()
            #plt.clf()
            #plt.cla()
            #plt.close()
            #plt.clf()
            #plt.cla()
            #plt.close()
            #plt.clf()
            #plt.cla()
            #plt.close()
            #plt.clf()
            #plt.cla()
            #plt.close()
            #plt.clf()
            #plt.cla()
            #plt.close()
            #plt.clf()
            #plt.cla()
            #plt.close()
            #plt.clf()
            #plt.cla()
            #plt.close()
            #plt.clf()
            #plt.cla()
            #plt.close()
            #plt.clf()
            #plt.cla()
            #plt.close()
            #plt.clf()
            #plt.cla()
            #plt.close()
            #plt.clf()
            #plt.cla()
            #plt.close()
            #plt.clf()
            #plt.cla()
            #plt.close()
            #plt.clf()
            #plt.cla()
    else:break

print("end")