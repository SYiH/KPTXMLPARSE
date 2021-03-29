# -*- coding: utf-8 -*-
import os
import shutil
def move_kpt(url_dir,url_dest_dir):
    os.chdir(url_dir) #переходим в директорию с распакованными КПТ
    main_dir=os.getcwd() #принимаем текущий путь
    folders=os.listdir(main_dir) #принимаем список папок
    print(folders) #выводим список папок
    for each_dir in folders: #для каждого названия папки из списка
        os.chdir(main_dir+'/'+each_dir) #меняем текущую директорию на каждую папку
        print(os.getcwd()) #можно удалить
        files_in_dir=os.listdir(os.getcwd()) #получаем список файлов в папке
        os.rename(files_in_dir[0],'kpt '+each_dir[-1:-8:-1]+'.xml') #переименовываем файл репорта
        files_in_dir=os.listdir(os.getcwd()) #обновляем список файлов в директории
        shutil.move(files_in_dir[0],url_dest_dir) #перемещаем файлы в новую директорию
    return print('Task failed successful!!!')

print('Введите адрес директории с распакованными XML файлами: ')
url_dir=input()
print('Введите путь к выходной папке: ')
url_dest_dir=input()
move_kpt(url_dir, url_dest_dir)
