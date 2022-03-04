import os
import shutil

dispath=r'F:\Downloads\apogeedown1\dr17\apogee_all'
def show_files(path, all_files, all_filename):
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files, all_filename)
        elif file.endswith('.fits'):
            all_files.append(cur_path)
            all_filename.append(file)
            shutil.copy(cur_path, dispath)
    return all_files, all_filename
path = r'F:\Downloads\apogeedown1\dr17\apogee'
all_files, all_filename = show_files(path, [], [])
print('end')