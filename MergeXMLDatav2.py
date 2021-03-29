# -*- coding: utf-8 -*-
import os
from lxml import etree as ET
def merge_kpt(url_dir, url_target_kpt):
    os.chdir(url_dir) #переходим в директорию с распакованными КПТ
    main_dir=os.getcwd() #принимаем текущий путь
    objcts=os.listdir(main_dir) #принимаем список объектов в папке
    print(objcts) #выводим список КПТ, можно удалить

    target_XML=open(url_target_kpt, 'a', encoding='utf-8')

    try:
        for elem in objcts: #для каждой КПТ в директории с кпт
            src_XML=ET.parse(elem) #распарсить исходную кпт
            src_block=src_XML.find('.//cadastral_block') #находим квартал
            src_block_str=ET.tostring(src_block, encoding='utf-8', method='xml').decode() 
            target_XML.write('\n'+'  '+src_block_str+'\n')
    except:
        print('ERROR!!! PLEASE CHECK SOURCE DIRECTORY!!!')
    
    target_XML.write('  </cadastral_blocks>'+'\n'+'</extract_cadastral_plan_territory>')
    target_XML.close()
    return 'Successfuly complete!'

print('Введите адрес директории с распакованными XML файлами: ')
url_dir=input()
print('Введите путь к выходному XML файлу: ')
url_target_kpt=input()
merge_kpt(url_dir, url_target_kpt)