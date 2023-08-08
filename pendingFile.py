import os

path = "C:\\Program Files\\AspenTech\\AeBRS"  # 手动输入文件夹路径，注意文件夹之间用“\\”最后要有个“\\”
need_to_overwrite = True  # 是否覆盖旧文件，若否，则生成一个新文件
new_file_suffix = '-new'  # 若生成新文件，则以此为后缀名

all_files_path = []  # 不用手动输入，由 read_file() 生成的所有文件的完整路径名


def read_file(path):
    for root, dirs, files in os.walk(path, topdown=True):
        # print('root:',root)
        # print('dirs:',dirs)
        # print('files:',files)
        # print('\n')
        if (len(files) > 0):
            each_folder_files = [os.path.join(root, x) for x in files]
            all_files_path.extend(each_folder_files)

        for dir in dirs:
            read_file(os.path.join(root, dir))
        return


def replace_text_in_file(current_file_path, search_string, replace_string):
    need_to_replace = False
    file_name, file_extension = os.path.splitext(current_file_path)  # 将路径下的文件名和后缀分开并保存
    # if(file_name == 'Key words')                     # 按文件名的关键字筛选需要操作的文件
    if (file_extension == '.m2r_cfg' or file_extension == '.INI' or file_extension == '.xml' or file_extension == '.m2r_cfg_old'):  # 按文件后缀筛选需要操作的文件
        with open(current_file_path, 'r+', encoding='ANSI') as f:  # 此打开方式不需要f.close()
            lines = f.readlines()  # 打开文件按行读，将每一行的内容存储在列表“lines”中
            flen = len(lines)  # 得到列表“lines”的长度
            for i in range(flen):  # 遍历列表“lines”，寻找有无需要替换的内容
                if (search_string in lines[i]):  # 判断列表“lines”的第i行是否有需要替换的内容
                    need_to_replace = True
                    lines[i] = lines[i].replace(search_string, replace_string)

            if (need_to_replace):
                if (need_to_overwrite):
                    f.seek(0)  # 指针回到文件内容的起始位置
                    f.truncate()  # 从指针指的地方开始删除内容
                    f.writelines(lines)  # 将更新后的列表“lines”重新写入文件
                else:
                    with open(file_name + new_file_suffix + file_extension, "w", encoding='ANSI') as nf:
                        nf.seek(0)  # 指针回到文件内容的起始位置
                        nf.truncate()  # 从指针指的地方开始删除内容
                        nf.writelines(lines)  # 将列表“lines”写入新文件


read_file(path)

for current_file_path in all_files_path:
    replace_text_in_file(
        current_file_path,
        'MVT-GEN-C-D11',  # 查找文本
        'APEM-C-D7'  # 替换文本
    )
# C:\Program Files\AspenTech\AeBRS\cfg_source\codify_all.cmd
os.chdir("C:\\Program Files\\AspenTech\\AeBRS\\cfg_source")
command1 = 'codify_all.cmd'
os.system(command1)

