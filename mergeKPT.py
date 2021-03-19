import os
import shutil

os.chdir(u'C:/Users/A_Libenko/Documents/temp/volg/kpt_v/kpts') #переходим в директорию с распакованными КПТ
mainDir=os.getcwd() #принимаем текущий путь
folders=os.listdir(mainDir) #принимаем список папок
print(folders) #выводим список папок
for eachDir in folders: #для каждого названия папки из списка
    os.chdir(mainDir+'/'+eachDir) #меняем текущую директорию на каждую папку
    print(os.getcwd()) #можно удалить
    filesInDir=os.listdir(os.getcwd()) #получаем список файлов в папке
    os.rename(filesInDir[0],'kpt '+eachDir[-1:-8:-1]+'.xml') #переименовываем файл репорта
    filesInDir=os.listdir(os.getcwd()) #обновляем список файлов в директории
    destDir=u'C:/Users/A_Libenko/Documents/temp/volg/kpt_v/exit' #целевая директория перемещения
    shutil.move(filesInDir[0],destDir) #перемещаем файлы в новую директорию