import os


def change_file_extension(filepath, old_extension, new_extension):
    """
    :filepath       str:    name of dir, not including '/' in the end
    :old_extension  str:    like '.BMP'
    :new_extension  str:    like '.jpg'
    """
    file_list = list(os.walk(filepath))[0][2]
    for file in file_list:
        # print(file)
        if os.path.splitext(file)[-1] == old_extension:
            # os.chdir(filepath)
            os.renames(filepath+file, filepath +
                       os.path.splitext(file)[0]+new_extension)


print('依次输入文件所在目录、原扩展名、新扩展名，用空格分隔，如“pics .BMP .jpg”：')
input_list = input().split(' ')
filepath, old_extension, new_extension = input_list
change_file_extension(filepath+'/', old_extension, new_extension)
print('Done.')
