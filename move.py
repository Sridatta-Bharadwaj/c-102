from distutils import extension
import os
import shutil


source = 'D:\whitehat_jr\C102'
destination = 'D:\whitehat_jr\moved to'

list_of_files = os.listdir(source)
print(list_of_files)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    if extension == "":
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        path1 = source + '/' + file_name
        path2 = destination + '/' + "image_files"
        path3 = destination + '/' + "image_files" + '/' + file_name
        if os.path.exists(path2):
            print("moving" + file_name + "...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving" + file_name + "...")
            shutil.move(path1, path3)

