# -*- coding: utf-8 -*-
import os
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
toMassJ=np.loadtxt("E:\\学习资料\\天文\\作业五\\20211219_光谱响应曲线卷积\\2massJ.csv",delimiter=',',skiprows=1,dtype=float)
toMassH=np.loadtxt("E:\\学习资料\\天文\\作业五\\20211219_光谱响应曲线卷积\\2massH.csv",delimiter=',',skiprows=1,dtype=float)
toMassK=np.loadtxt("E:\\学习资料\\天文\\作业五\\20211219_光谱响应曲线卷积\\2massK.csv",delimiter=',',skiprows=1,dtype=float)
cameraW1=np.loadtxt("E:\\学习资料\\天文\\作业五\\20211219_光谱响应曲线卷积\\RSR-W1.csv",delimiter=',',skiprows=1,dtype=float)
cameraW2=np.loadtxt("E:\\学习资料\\天文\\作业五\\20211219_光谱响应曲线卷积\\RSR-W2.csv",delimiter=',',skiprows=1,dtype=float)
cameraW3=np.loadtxt("E:\\学习资料\\天文\\作业五\\20211219_光谱响应曲线卷积\\RSR-W3.csv",delimiter=',',skiprows=1,dtype=float)
cameraW4=np.loadtxt("E:\\学习资料\\天文\\作业五\\20211219_光谱响应曲线卷积\\RSR-W4.csv",delimiter=',',skiprows=1,dtype=float)
#print(cameraW4[0])
filename= 'lte030-5.0-0.0a+0.2.BT-Settl.spec.7'
readspec= readphx(filename)
specX = readspec[0]
# print(x)
specY = readspec[1]
dst = cv2.GaussianBlur(src=specY, ksize=(25, 25), sigmaX=6)
#i = 0
r_mag = 0
i_mag=0
z_mag=0
J_mag=0
H_mag=0
K_mag=0
W1_mag=0
W2_mag=0
W3_mag=0
W4_mag=0
#print(dst[11230])
#print(type(x))
# for i in range(100):
#     print(dst[i])
for i in range(len(camera_r_wavelength)):
    waveint = int(camera_r_wavelength[i])
    x_index = int(np.argwhere(specX == waveint))
    r_mag += camera_r_flux[i] * dst[x_index] * 25
for i in range(len(camera_i_wavelength)):
    waveint = int(camera_i_wavelength[i])
    x_index = int(np.argwhere(specX == waveint))
    i_mag += camera_i_flux[i] * dst[x_index] * 25
for i in range(len(camera_z_wavelength)):
    waveint = int(camera_z_wavelength[i])
    x_index = int(np.argwhere(specX == waveint))
    z_mag += camera_z_flux[i] * dst[x_index] * 25
# for i in range(3630,4000):
#     waveint_1=int(np.argwhere(x==i))
#     print(dst[waveint_1])
for i in range(len(toMassJ)):
    waveint=int(toMassJ[i][0]*10000+0.5)
    x_index=int(np.argwhere(specX == waveint))
    J_mag+=toMassJ[i][1]*dst[x_index]*((toMassJ[0][0]-toMassJ[1][0])*10000)
for i in range(len(toMassH)):
    waveint=int(toMassH[i][0]*10000+0.5)
    x_index=int(np.argwhere(specX == waveint))
    H_mag+=toMassH[i][1]*dst[x_index]*((toMassH[0][0]-toMassH[1][0])*10000)
for i in range(len(toMassK)):
    waveint=int(toMassK[i][0]*10000+0.5)
    x_index=int(np.argwhere(specX == waveint))
    K_mag+=toMassK[i][1]*dst[x_index]*((toMassK[0][0]-toMassK[1][0])*10000)
for i in range(len(cameraW1)):
    waveint=int(cameraW1[i][0]*10000+0.5)
    #print(type(waveint))
    x_index=int(np.argwhere(specX == waveint))
    W1_mag+=cameraW1[i][1]*dst[x_index]*((cameraW1[0][0]-cameraW1[1][0])*10000)
for i in range(len(cameraW2)):
    waveint=int(cameraW2[i][0]*10000+0.5)
    x_index=int(np.argwhere(specX == waveint))
    W2_mag+=cameraW2[i][1]*dst[x_index]*((cameraW2[0][0]-cameraW2[1][0])*10000)
for i in range(len(cameraW3)):
    waveint=int(cameraW3[i][0]*10000+0.5)
    x_index=int(np.argwhere(specX == waveint))
    W3_mag+=cameraW3[i][1]*dst[x_index]*((cameraW3[0][0]-cameraW3[1][0])*10000)
for i in range(len(cameraW4)):
    waveint=int(cameraW4[i][0]*10000+0.5)
    x_index=int(np.argwhere(specX == waveint))
    W4_mag+=cameraW4[i][1]*dst[x_index]*((cameraW4[0][0]-cameraW4[1][0])*10000)
fl_r=r_mag/(max(camera_r_wavelength)-min(camera_r_wavelength))
fl_i=i_mag/(max(camera_i_wavelength)-min(camera_i_wavelength))
fl_z=z_mag/(max(camera_z_wavelength)-min(camera_z_wavelength))
fl_J=-J_mag/((toMassJ[-1][0]-toMassJ[0][0])*10000)
fl_H=-H_mag/((toMassH[-1][0]-toMassH[0][0])*10000)
fl_K=-K_mag/((toMassK[-1][0]-toMassK[0][0])*10000)
fl_W1=-W1_mag/((cameraW1[-1][0]-cameraW1[0][0])*10000)
fl_W2=-W2_mag/((cameraW2[-1][0]-cameraW2[0][0])*10000)
fl_W3=-W3_mag/((cameraW3[-1][0]-cameraW3[0][0])*10000)
fl_W4=-W4_mag/((cameraW4[-1][0]-cameraW4[0][0])*10000)
print(fl_r,fl_i,fl_z,fl_J,fl_H,fl_K,fl_W1,fl_W2,fl_W3,fl_W4)
#result=-2.5*math.log(fl_r,10)-(-2.5*math.log(fl_g,10))
# print(fl_r)
# print("len(toMassH)="+str(len(toMassH)))
# 传入空的list接收文件名
# contents,contents2 = show_files("G:\spec", [],[])
# # all_filenames = []
# # 循环打印show_files函数返回的文件名列表
# for content in contents:
#     print(content)
# for content in contents2:
#     print(content)
    #all_filenames.append(os.path.basename(content))