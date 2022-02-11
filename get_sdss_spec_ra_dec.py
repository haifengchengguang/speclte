import numpy as np
# from astropy.io.fits import tabledump
import pandas as pd
from astroquery.sdss import SDSS
# specs = SDSS.get_spectra(plate=328, mjd=52282,fiberID=254,data_release=17)
from tqdm import tqdm
from astropy import units as u
from astropy.coordinates import SkyCoord

fileName="E:\\学习资料\\天文\\作业五\\20211123_150w_match_simbad\\200wLmore15.csv"
#Lmore15=np.loadtxt(fileName,delimiter=',',dtype=int,usecols=np.arange(3),skiprows=1)   #跳过第4938行
Lmore15=pd.read_csv(r"E:\\学习资料\\天文\\作业五\\20211123_150w_match_simbad\\200wLmore15.csv")
#print(Lmore15)
# #tabledump('321020868929021952.fits',specs)   #将获取的数据写入文件
# specs[0].writeto('test.fits')
from astropy.io import fits
# testspec=fits.open('test.fits')      #读取文件
for everyrow in tqdm(Lmore15.iterrows()):
    #print('ra=',everyrow[1][0],'dec=',everyrow[1][1])

    ra=everyrow[1][0]
    dec=everyrow[1][1]
    #print(dec)
    objid=everyrow[1][2]
    c = SkyCoord(ra=ra * u.degree, dec=dec * u.degree, frame='icrs')
    #print(plate,mjd,fiberid)

    specs = SDSS.get_spectra(coordinates=c,radius=(1/1200)*u.degree,data_release=17)    #获取每一行的数据

    if specs is None:
        print()
    else:
        specs[0].writeto('G:\sdss光谱\match1\spec_'+str(objid)+'.fits')
        print('ra:', ra, 'dec:', dec, 'objid:', objid)
#     #specs[0].writeto('E:\学习资料\天文\作业五\sdss光谱\spec_'+str(plate)+'_'+str(mjd)+'_'+str(fiberid)+'.fits')

#     #print(specs[0])
#     #print(specs[0].header)
#     #print(specs[0].data)
#     #print(specs[0].header['OBJID'])
#     #print(specs[0].header['PLATE'])
#     #print(specs[0].header['MJD'])
#     #print(specs[0].header['FIBERID'])
#     #print(specs[0].header['RA'])
#     #print(specs[0].header['DEC'])
#     #print(specs[0].header['Z'])
#     #print(specs[0].header['ZWARNING'])
#     #print(specs[0].header['SPECZ'])
#     #print(specs[0].header['SPECZ_IVAR'])
#     #print(specs[0].header['SPECZ_EW'])
#     #print(specs[0].header['SPECZ_EW_IVAR'])
#     #print(specs[0].header['SPECZ_RCHI2'])
#     #print(specs[0].header['SPECZ_RCHI2_IVAR'])
#     #print(specs[0].header['SPECZ_RCHI2_R'])
#     #print(specs[0].header['SPECZ_RCHI2_R_IVAR'])
    #specs[0].writeto('sdss_fits/plate'+str(plate)+'_mjd'+str(mjd)+'_fiberid'+str(fiberid)+'.fits')
