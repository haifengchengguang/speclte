import numpy as np
# from astropy.io.fits import tabledump
from astroquery.sdss import SDSS
# specs = SDSS.get_spectra(plate=328, mjd=52282,fiberID=254,data_release=17)
from tqdm import tqdm

fileName="E:\学习资料\天文\作业五\sdss光谱\later_than_m6_sdss_dr17_total_sduss.csv"
later_than_m6_sdss_dr17_total_sduss=np.loadtxt(fileName,delimiter=',',dtype=int,usecols=np.arange(2,5),skiprows=9369)   #跳过第4938行
# #tabledump('321020868929021952.fits',specs)   #将获取的数据写入文件
# specs[0].writeto('test.fits')
from astropy.io import fits
# testspec=fits.open('test.fits')   #读取文件
for everyrow in tqdm(later_than_m6_sdss_dr17_total_sduss):
    plate=everyrow[0]
    mjd=everyrow[1]
    fiberid=everyrow[2]
    #print(plate,mjd,fiberid)
    try:
        specs = SDSS.get_spectra(plate=plate, mjd=mjd, fiberID=fiberid, data_release=17)    #获取每一行的数据
    except:
        continue
    if specs is None:
        print()
    else:
        specs[0].writeto('G:\sdss光谱\spec_'+str(plate)+'_'+str(mjd)+'_'+str(fiberid)+'.fits')
        print('plate:', plate, 'mjd:', mjd, 'fiberid:', fiberid)
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
