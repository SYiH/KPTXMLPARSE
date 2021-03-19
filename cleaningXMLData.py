# -*- coding: utf-8 -*-
import os
from lxml import etree as ET

os.chdir(u'"""путь к директории с распакованными XML""""') #переходим в директорию с распакованными КПТ
mainDir=os.getcwd() #принимаем текущий путь
objcts=os.listdir(mainDir) #принимаем список объектов в папке
print(objcts) #выводим список КПТ, можно удалить

targetXML=open(u'"""путь к выходному XML""""', 'a', encoding='utf-8') #открываем на дозапись целевую XML, закрывающие тэги  </cadastral_blocks>' и '</extract_cadastral_plan_territory> должны отсутсвовать

for elem in objcts: #для каждой КПТ в директории с кпт
    
    srcXML=ET.parse(elem) #распарсить исходную кпт
    
    srcBlock=srcXML.find('.//cadastral_block') #находим квартал
    mun_bounds=srcXML.find('.//municipal_boundaries') #находим municipal_boundaries
    inh_bounds=srcXML.find('.//inhabited_locality_boundaries') #находим inhabited_locality_boundaries
    zones_and_terrs=srcXML.find('.//zones_and_territories_boundaries') #находим zones_and_territories_boundaries
    
    #чистка мусора
    try:
        mun_bounds.getparent().remove(mun_bounds) #пробуем удалить муниципальные границы
        inh_bounds.getparent().remove(inh_bounds) #пробуем удалить еще какие-то границы
        zones_and_terrs.getparent().remove(zones_and_terrs) #пробуем удалить особые зоны (их особенность сравнима с особенностью автора этого графоманства)
    except AttributeError:  #если возникает ошибка, какой-то из блоков отсутсвует, продолжить скрипт
        pass
    
    srcBlockStr=ET.tostring(srcBlock, encoding='utf-8', method='xml').decode() #преобразуем получившийся, чистый, cadastral_blocks из объекта в строку
    targetXML.write('\n'+'  '+srcBlockStr+'\n')    #дописываем получившееся в целевой XML
    
targetXML.write('  </cadastral_blocks>'+'\n'+'</extract_cadastral_plan_territory>') #дописываем в конец целевого XML закрывающие тэги
targetXML.close()   #закрываем целевой файл
