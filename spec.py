import numpy as np
import matplotlib.pyplot as plt
from cv2 import cv2
from astropy.io import fits


def readphx(filename):
    lines = open(filename)
    wave, flux = [], []
    for line in lines:
        data = ' '.join(line.split())
        data = data.split(' ')
        wave.append(float(data[0].replace('D', 'E')))
        flux.append(10 ** (float(data[1].replace('D', 'E')) - 8.E0))
    spec = np.array([wave, flux])
    sorted_spec = spec.T[np.lexsort(spec[0, None])].T
    return sorted_spec[0], sorted_spec[1]


x = readphx('lte030-5.0-0.0a+0.2.BT-Settl.spec.7')[0]
# print(x)
y = readphx('lte030-5.0-0.0a+0.2.BT-Settl.spec.7')[1]
dst = cv2.GaussianBlur(src=y, ksize=(25, 25), sigmaX=6)

camera = fits.open('filter_curves.fits')
camera_g = camera[2].data
camera_g_flux = camera_g.field(1)
camera_g_wavelength = camera_g.field(0)
i = 0
r_mag = 0
#print(dst[11230])
#print(type(x))
# for i in range(100):
#     print(dst[i])
while True:
    if i>=len(camera_g_wavelength): break
    waveint=int(camera_g_wavelength[i])
    x_index=int(np.argwhere(x==waveint))
    #print(waveint)
    #print()
    #print(camera_g_flux[i])
    #print(dst[waveint])
    #print(x_index)
    r_mag+=camera_g_flux[i]*dst[x_index]*25
    i+=1
for i in range(3630,4000):
    waveint_1=int(np.argwhere(x==i))
    print(dst[waveint_1])

fl_g=r_mag/(max(camera_g_wavelength)-min(camera_g_wavelength))
#result=-2.5*math.log(fl_r,10)-(-2.5*math.log(fl_g,10))
print(fl_g)
# # print(dst)
# plt.plot(x, dst, '', color='black', label="SPEC", linewidth=0.1)  # o-:圆形
# plt.xlim(2980, 11230)
# plt.rcParams['savefig.dpi'] = 300  # 图片像素
# plt.rcParams['figure.dpi'] = 300  # 分辨率
# # l1=plt.plot(x1,y1,'r--',label='type1')
# # plt.plot(x1,y1,'ro-')
# # plt.title('spec-55859-F5902_sp01-008.fits')
# plt.xlabel('wavelength')
# plt.ylabel('flux')
# plt.legend()
# plt.savefig('./spec01-8-0_1.png')
# plt.show()
