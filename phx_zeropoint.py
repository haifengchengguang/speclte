import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
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

def show_files(path, all_files,all_filename):
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files,all_filename)
        elif file.endswith('.7'):
            all_files.append(cur_path)
            all_filename.append(file)
    return all_files,all_filename
path=r"H:\理论光谱"
phxpath,phxpath_name=show_files(path,[],[])

camera = fits.open('filter_curves.fits')

camera_r = camera[3].data
camera_r_flux = camera_r.field(1)
camera_r_wavelength = camera_r.field(0)

camera_i = camera[4].data
camera_i_flux = camera_i.field(1)
camera_i_wavelength = camera_i.field(0)

camera_z = camera[5].data
camera_z_flux = camera_z.field(1)
camera_z_wavelength = camera_z.field(0)


camera_J=pd.read_csv(r'E:\学习资料\天文\作业五\20211219_光谱响应曲线卷积\2massJ.csv')
camera_J_flux=camera_J['flux']
camera_J_wavelength=camera_J['wavelength']

camera_H=pd.read_csv(r'E:\学习资料\天文\作业五\20211219_光谱响应曲线卷积\2massH.csv')
camera_H_flux=camera_H['flux']
camera_H_wavelength=camera_H['wavelength']

camera_K=pd.read_csv(r'E:\学习资料\天文\作业五\20211219_光谱响应曲线卷积\2massK.csv')
camera_K_flux=camera_K['flux']
camera_K_wavelength=camera_K['wavelength']

camera_W1=pd.read_csv(r'E:\学习资料\天文\作业五\20211219_光谱响应曲线卷积\RSR-W1.csv')
camera_W1_flux=camera_W1['RSR']
camera_W1_wavelength=camera_W1['W']

camera_W2=pd.read_csv(r'E:\学习资料\天文\作业五\20211219_光谱响应曲线卷积\RSR-W2.csv')
camera_W2_flux=camera_W2['RSR']
camera_W2_wavelength=camera_W2['W']

camera_W3=pd.read_csv(r'E:\学习资料\天文\作业五\20211219_光谱响应曲线卷积\RSR-W3.csv')
camera_W3_flux=camera_W3['RSR']
camera_W3_wavelength=camera_W3['W']

camera_W4=pd.read_csv(r'E:\学习资料\天文\作业五\20211219_光谱响应曲线卷积\RSR-W4.csv')
camera_W4_flux=camera_W4['RSR']
camera_W4_wavelength=camera_W4['W']

for filename in phxpath:
    readspec = readphx(filename)
    x = readspec[0]
    # print(x)
    y = readspec[1]
    r_mag_full=0
    i_mag_full = 0
    z_mag_full = 0
    dst = cv2.GaussianBlur(src=y, ksize=(25, 25), sigmaX=6)
    for i in range(len(camera_r_wavelength)-1):
        waveint = int(camera_r_wavelength[i])
        x_index = int(np.argwhere(x == waveint))
        #print("x_index:",x_index)
        r_mag_full += camera_r_flux[i] * dst[x_index] * 25
    rmag= r_mag_full / (max(camera_r_wavelength) - min(camera_r_wavelength))
    print(filename+"----rmag="+str(rmag))
    for i in range(len(camera_i_wavelength)-1):
        waveint = int(camera_i_wavelength[i])
        x_index = int(np.argwhere(x == waveint))
        #print("x_index:",x_index)
        i_mag_full += camera_i_flux[i] * dst[x_index] * 25
    imag= i_mag_full / (max(camera_i_wavelength) - min(camera_i_wavelength))
    print(filename + "----imag=" + str(imag))
    for i in range(len(camera_z_wavelength)-1):
        waveint = int(camera_z_wavelength[i])
        x_index = int(np.argwhere(x == waveint))
        #print("x_index:",x_index)
        z_mag_full += camera_z_flux[i] * dst[x_index] * 25
    zmag= z_mag_full / (max(camera_z_wavelength) - min(camera_z_wavelength))
    print(filename + "----zmag=" + str(zmag))
    J_mag_full=0
    for i in range(len(camera_J_wavelength)-1):
        waveint = int(camera_J_wavelength[i]*1000000)
        x_index = int(np.argwhere(x == waveint))
        #print("x_index:",x_index)
        J_mag_full += camera_J_flux[i] * dst[x_index] * (camera_J_wavelength[i+1]-camera_J_wavelength[i])
    Jmag= J_mag_full / ((max(camera_J_wavelength) - min(camera_J_wavelength)))
    print(filename + "----Jmag=" + str(Jmag))
    H_mag_full = 0
    for i in range(len(camera_H_wavelength) - 1):
        waveint = int(camera_H_wavelength[i] * 1000000)
        x_index = int(np.argwhere(x == waveint))
        # print("x_index:",x_index)
        H_mag_full += camera_H_flux[i] * dst[x_index] * (camera_H_wavelength[i + 1] - camera_H_wavelength[i])
    Hmag = H_mag_full / ((max(camera_H_wavelength) - min(camera_H_wavelength)))
    print(filename + "----Hmag=" + str(Hmag))
    K_mag_full = 0
    for i in range(len(camera_K_wavelength) - 1):
        waveint = int(camera_K_wavelength[i] * 1000000)
        temp=np.argwhere(x == waveint)
        x_index = temp
        #print("x_index:",x_index)
        if len(x_index)==0:x_index=(np.abs(x-waveint)).argmin()
        x_index = int(x_index)
        K_mag_full += camera_K_flux[i] * dst[x_index] * (camera_K_wavelength[i + 1] - camera_K_wavelength[i])
    Kmag = K_mag_full / ((max(camera_K_wavelength) - min(camera_K_wavelength)))
    print(filename + "----Kmag=" + str(Kmag))
    W1_mag_full = 0
    for i in range(len(camera_W1_wavelength) - 1):
        waveint = int(camera_W1_wavelength[i] * 1000000)
        #print(waveint)
        temp = np.argwhere(x == waveint)
        x_index = temp
        # print("x_index:",x_index)
        if len(x_index) == 0: x_index = (np.abs(x - waveint)).argmin()
        #print("x_index:", x_index)
        x_index=int(x_index)
        W1_mag_full += camera_W1_flux[i] * dst[x_index] * (camera_W1_wavelength[i + 1] - camera_W1_wavelength[i])
    W1mag = W1_mag_full / ((max(camera_W1_wavelength) - min(camera_W1_wavelength)))
    print(filename + "----W1mag=" + str(W1mag))
    W2_mag_full = 0
    for i in range(len(camera_W2_wavelength) - 1):
        waveint = int(camera_W2_wavelength[i] * 1000000)
        temp = np.argwhere(x == waveint)
        x_index = temp
        # print("x_index:",x_index)
        if len(x_index) == 0: x_index = (np.abs(x - waveint)).argmin()
        x_index = int(x_index)
        W2_mag_full += camera_W2_flux[i] * dst[x_index] * (camera_W2_wavelength[i + 1] - camera_W2_wavelength[i])
    W2mag = W2_mag_full / ((max(camera_W2_wavelength) - min(camera_W2_wavelength)))
    print(filename + "----W2mag=" + str(W2mag))
    W3_mag_full = 0
    for i in range(len(camera_W3_wavelength) - 1):
        waveint = int(camera_W3_wavelength[i] * 1000000)
        temp = np.argwhere(x == waveint)
        x_index = temp
        # print("x_index:",x_index)
        if len(x_index) == 0: x_index = (np.abs(x - waveint)).argmin()
        x_index = int(x_index)
        W3_mag_full += camera_W3_flux[i] * dst[x_index] * (camera_W3_wavelength[i + 1] - camera_W3_wavelength[i])
    W3mag = W3_mag_full / ((max(camera_W3_wavelength) - min(camera_W3_wavelength)))
    print(filename + "----W3mag=" + str(W3mag))
    W4_mag_full = 0
    for i in range(len(camera_W4_wavelength) - 1):
        waveint = int(camera_W4_wavelength[i] * 1000000)
        temp = np.argwhere(x == waveint)
        x_index = temp
        # print("x_index:",x_index)
        if len(x_index) == 0: x_index = (np.abs(x - waveint)).argmin()
        x_index = int(x_index)
        W4_mag_full += camera_W4_flux[i] * dst[x_index] * (camera_W4_wavelength[i + 1] - camera_W4_wavelength[i])
    W4mag = W4_mag_full / ((max(camera_W4_wavelength) - min(camera_W4_wavelength)))
    print(filename + "----W4mag=" + str(W4mag))
    break
