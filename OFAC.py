import os
import xml.etree.ElementTree as ET
print('Добро пожаловать в программу по очистке данных из оригинальной офаки')
treepath = input(r'Введите путь к файлу sdn.xml. Ожидаемый формат - C:\Users\Igor\Desktop\sdn\in\sdn.xml'
                 '\n')
outpath = input(r'Введите путь к папке, где будем получать результат. Ожидаемый формат - C:\Users\Igor\Desktop\sdn\out'
                '\n')

#Описываю функцию, которая убирает lastName из файла.
def lastName():
    tree2 = ET.parse(treepath)
    root2 = tree2.getroot()
    removepath = input(r'Введите путь к файлу из которого будем удалять lastName. Ожидаемый формат - C:\Users\Igor\Desktop\sdn\out\delete.txt' '\n')
    print('Процесс удаления слов запущен, как закончу сообщу.')
    removes = open(removepath, 'r+')
    print ('Открываю файл для удаления слов')
    removeses = removes.read().splitlines()
    print ('Ищу совпадения')
    for listoffirstnames in root2.findall('.//{http://tempuri.org/sdnList.xsd}lastName'):
        print (f'Вижу имя {listoffirstnames.text}')
        if listoffirstnames.text in removeses:
            print(f'Нашёл совпадение, удаляю')
            listoffirstnames.text = ' '
            tree2.write(f'{outpath}\dump.xml')
    print ('Почти готово, записываю получившийся файл')
    text_file = open(f'{outpath}\dump.xml', 'r+')
    text_file2 = open(f'{outpath}\sdn.xml', 'w+')
    text_file3 = open(f'{outpath}\dump2.xml', 'w+')
    filesdn = text_file.read()
    filewrite = text_file2.read()

    text_file2.write(
        "<?xml version=\"1.0\" standalone=\"yes\"?>\n<sdnList xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns=\"http://tempuri.org/sdnList.xsd\">\n")
    for r in (('ns0:', ''), (':ns0', '')):
        filesdn = filesdn.replace(*r)
    text_file3.write(filesdn[49:])
    text_file3.close()
    itog = open(f'{outpath}\dump2.xml', 'r+')
    filesdn2 = itog.read()
    text_file2.write(filesdn2)
    text_file.close()
    text_file2.close()
    os.remove(f'{outpath}\dump.xml')
    removes.close()
    itog.close()
    os.remove(f'{outpath}\dump2.xml')

#Описываю функцию, которая убирает firstName из файла.
def firstName():

    tree2 = ET.parse(treepath)
    root2 = tree2.getroot()
    removepath = input(r'Введите путь к файлу из которого будем удалять имена. Ожидаемый формат - C:\Users\Igor\Desktop\sdn\out\delete.txt' '\n')
    print('Процесс удаления слов запущен, как закончу сообщу.')
    removes = open(removepath, 'r+')
    print('Открываю файл для удаления слов')
    removeses = removes.read().splitlines()
    print('Ищу совпадения')
    for listoffirstnames in root2.findall('.//{http://tempuri.org/sdnList.xsd}firstName'):
        print(f'Вижу имя {listoffirstnames.text}')
        if listoffirstnames.text in removeses:
            print(f'Нашёл совпадение, удаляю')
            listoffirstnames.text = ' '
            tree2.write(f'{outpath}\dump.xml')
    print('Почти готово, записываю получившийся файл')
    text_file = open(f'{outpath}\dump.xml', 'r+')
    text_file2 = open(f'{outpath}\sdn.xml', 'w+')
    text_file3 = open(f'{outpath}\dump2.xml', 'w+')
    filesdn = text_file.read()
    filewrite = text_file2.read()

    text_file2.write(
        "<?xml version=\"1.0\" standalone=\"yes\"?>\n<sdnList xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns=\"http://tempuri.org/sdnList.xsd\">\n")
    for r in (('ns0:', ''), (':ns0', '')):
        filesdn = filesdn.replace(*r)
    text_file3.write(filesdn[49:])
    text_file3.close()
    itog = open(f'{outpath}\dump2.xml', 'r+')
    filesdn2 = itog.read()
    text_file2.write(filesdn2)
    text_file.close()
    text_file2.close()
    os.remove(f'{outpath}\dump.xml')
    removes.close()
    itog.close()
    os.remove(f'{outpath}\dump2.xml')

#Описываю функцию, которая убирает sdnEntry из файла.
def sdnEntry():
    print ('При полном удалении sdnEntry поиск осуществляется по первому имени фигуранта, поиск по альтернативным именам осуществляться не будет, но они все равно будут удалены вместе с основным именем.')
    print ('Например, если у фигуранта первым идёт FirstName в файле sdn, то указывать в файле для удаления надо именно его, а если первым идёт lastName, то указываем это значение.')
    print ('Если всё ясно, приступаем к работе. \n')
    tree2 = ET.parse(treepath)
    root2 = tree2.getroot()
    removepath = input(
        r'Введите путь к файлу из которого будем удалять имена. Ожидаемый формат - C:\Users\Igor\Desktop\sdn\out\delete.txt' '\n')
    print('Процесс удаления слов запущен, как закончу сообщу.')
    removes = open(removepath, 'r+')
    print('Открываю файл для удаления слов')
    removeses = removes.read().splitlines()
    i = -1

    print('Ищу совпадения')
    a1 = root2.findall('.//{http://tempuri.org/sdnList.xsd}sdnEntry')
    summa = sum(1 for line in a1)
    for list in a1:
        i+=1
        print(f'Вижу имя {a1[i][1].text}')
        if int(i) == int(summa - 1):
            print ('Дошёл до конца файла')
            break
        if a1[i][1].text in removeses:
            print(f'Нашёл совпадение, удаляю')
            a1[i].clear()
            tree2.write(f'{outpath}\dump.xml')
    print('Почти готово, записываю получившийся файл')
    text_file = open(f'{outpath}\dump.xml', 'r+')
    text_file2 = open(f'{outpath}\sdn.xml', 'w+')
    text_file3 = open(f'{outpath}\dump2.xml', 'w+')
    filesdn = text_file.read()
    filewrite = text_file2.read()

    text_file2.write(
        "<?xml version=\"1.0\" standalone=\"yes\"?>\n<sdnList xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns=\"http://tempuri.org/sdnList.xsd\">\n")
    for r in (('ns0:', ''), (':ns0', '')):
        filesdn = filesdn.replace(*r)
    text_file3.write(filesdn[49:])
    text_file3.close()
    itog = open(f'{outpath}\dump2.xml', 'r+')
    filesdn2 = itog.read()
    text_file2.write(filesdn2)
    text_file.close()
    text_file2.close()
    os.remove(f'{outpath}\dump.xml')
    removes.close()
    itog.close()
    os.remove(f'{outpath}\dump2.xml')

print ('Вы обратились в централизованную службу удаления слов из оригинальной офаки. \nДля удаления lastName из файла sdn.xml введите 1. \nДля удаления firstName из файла sdn.xml введите 2.')
print ('Для удаления целого фигуранта (sdnEntry) нажмите 3')
param = input()
print ()
if param == '1':
    print ('Вы выбрали число 1, запрос принят.')
    lastName()
    print('Всё готово, проверяйте')
    print('Обращаю внимание, что если вам требуется удалить другие символы из программы, необходимо полученный файл перенести в место исходного файла и снова запустить программу')
    input('Для выхода из программы нажмите Enter')
elif param == '2':
    print('Вы выбрали число 2, запрос принят.')
    firstName()
    print('Всё готово, проверяйте')
    print('Обращаю внимание, что если вам требуется удалить другие символы из программы, необходимо полученный файл перенести в место исходного файла и снова запустить программу')
    input('Для выхода из программы нажмите Enter')
elif param == '3':
    print('Вы выбрали число 3, запрос принят.')
    sdnEntry()
    print('Всё готово, проверяйте')
    print('Обращаю внимание, что если вам требуется удалить другие символы из программы, необходимо полученный файл перенести в место исходного файла и снова запустить программу')
    input('Для выхода из программы нажмите Enter')
else:
    print ('Кажется вы ошиблись с цифрами. Введите необходимое число ещё раз.')
