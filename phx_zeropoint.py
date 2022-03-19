import math
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

def caculate_mag(camera_wavelength,camera_flux,mag_name):
    mag_full=0
    for i in range(len(camera_wavelength) - 1):
        waveint = int(camera_wavelength[i] * 1000000)
        temp = np.argwhere(x == waveint)
        x_index = temp
        # print("x_index:",x_index)
        if len(x_index) == 0: x_index = (np.abs(x - waveint)).argmin()
        x_index = int(x_index)
        mag_full += camera_flux[i] * dst[x_index] * (camera_wavelength[i + 1] - camera_wavelength[i])
    mag = -2.5 * math.log((mag_full / ((max(camera_wavelength) - min(camera_wavelength)))), 10)
    print(mag,end='')
print("fitsname,rmag,imag,zmag,Jmag,Hmag,Kmag,W1mag,W2mag,W3mag,W4mag")
for filename in phxpath:
    readspec = readphx(filename)
    x = readspec[0]
    # print(x)
    y = readspec[1]
    dst = cv2.GaussianBlur(src=y, ksize=(25, 25), sigmaX=6)
    print(filename,end=',')
    caculate_mag(camera_r_wavelength,camera_r_flux,"rmag")
    print(end=',')
    caculate_mag(camera_i_wavelength, camera_i_flux, "imag")
    print(end=',')
    caculate_mag(camera_z_wavelength, camera_z_flux, "zmag")
    print(end=',')
    caculate_mag(camera_J_wavelength, camera_J_flux, "Jmag")
    print(end=',')
    caculate_mag(camera_H_wavelength, camera_H_flux, "Hmag")
    print(end=',')
    caculate_mag(camera_K_wavelength, camera_K_flux, "Kmag")
    print(end=',')
    caculate_mag(camera_W1_wavelength, camera_W1_flux, "W1mag")
    print(end=',')
    caculate_mag(camera_W2_wavelength, camera_W2_flux, "W2mag")
    print(end=',')
    caculate_mag(camera_W3_wavelength, camera_W3_flux, "W3mag")
    print(end=',')
    caculate_mag(camera_W4_wavelength, camera_W4_flux, "W4mag")
    print()
print("end")
