from tkinter import *
import os
import xml.etree.ElementTree as ET


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.photo = PhotoImage(file="./ofac.png")
        self.image = Label(self, image=self.photo).grid(row = 1, column = 0, sticky = W)

    def create_widgets(self):
        Label(self,
              text = 'Добро пожаловать в программу по очистке данных из оригинального списка OFAC SDN List', font=("Arial", 12)
              ).grid(row = 0, column = 0, sticky = W)

        Label(self,
              text = r'Введите путь к файлу sdn.xml. Ожидаемый формат - C:\Users\Igor\Desktop\sdn\in\sdn.xml'
              ).grid(row = 2, column = 0, sticky = W)
        self.treepath = Text(self, width = 50, height = 1, wrap = NONE)
        self.treepath.grid(row=3, column=0, sticky=W, columnspan=2)

        Label(self,
              text=r'Введите путь к папке, где будем получать результат. Ожидаемый формат - C:\Users\Igor\Desktop\sdn\out'
              ).grid(row=4, column=0, sticky=W)
        self.outpath = Text(self, width = 50, height = 1, wrap = NONE)
        self.outpath.grid(row=5, column=0, sticky=W)

        Label(self,
              text=r'Выберите необходимый вариант удаления значений из файла'
              ).grid(row=6, column=0, sticky=W)

        self.rbut = StringVar()
        self.rbut.set(None)
        Radiobutton(self,
                    text = 'Удаление LastName',
                    variable=self.rbut,
                    value = '1',
                    command = self.radiobutton_logic,
                    state = 'active'
                    ).grid(row=7, column=0, sticky=W)
        Radiobutton(self,
                    variable=self.rbut,
                    value = '2',
                    command = self.radiobutton_logic,
                    state = 'active',
                    text='Удаление FirstName').grid(row=8, column=0, sticky=W)
        Radiobutton(self,
                    variable=self.rbut,
                    value = '3',
                    command = self.radiobutton_logic,
                    state = 'active',
                    text='Удаление целого SdnEntry').grid(row=9, column=0, sticky=W)


        Label(self,
              text=r'Здесь будет отображён результат работы программы по её завершению'
              ).grid(row=21, column=0, sticky=W)

        self.info_text = Text(self, width = 90, height = 20, wrap = WORD)
        self.info_text.grid(row = 22, column = 0, sticky=W)


    def radiobutton_logic(self):
        if self.rbut.get() == '1':
            self.lastName_radiobuttion()
            Button(self,
                   text='Запустить выполнение программы',
                   command=lambda: self.lastName()
                   ).grid(row=20, column=0, sticky=W)
        elif self.rbut.get() == '2':
            self.firstName_radiobutton()
            Button(self,
                   text='Запустить выполнение программы',
                   command=lambda: self.firstName()
                   ).grid(row=20, column=0, sticky=W)
        elif self.rbut.get() == '3':
            self.sdnEntry_radiobutton()
            Button(self,
                   text='Запустить выполнение программы',
                   command =lambda: self.sdnEntry()
                   ).grid(row=20, column=0, sticky=W)

    def firstName_radiobutton(self):
        self.info_text.delete(0.0, END)
        Label(self,
              text=r'Введите путь к файлу из которого будем удалять имена. Ожидаемый формат - C:\Users\Igor\Desktop\sdn\out\delete.txt'
              ).grid(row=10, column=0, sticky=W)
        self.removepath = Text(self, width=50, height=1, wrap=WORD)
        self.removepath.grid(row=11, column=0, sticky=W)
    def lastName_radiobuttion(self):
        self.info_text.delete(0.0, END)
        Label(self,
              text=r'Введите путь к файлу из которого будем удалять lastName. Ожидаемый формат - C:\Users\Igor\Desktop\sdn\out\delete.txt'
              ).grid(row=10, column=0, sticky=W)
        self.removepath = Text(self, width=50, height=1, wrap=WORD)
        self.removepath.grid(row=11, column=0, sticky=W)
    def sdnEntry_radiobutton(self):
        self.info_text.delete(0.0, END)
        Label(self,
              text=r'Введите путь к файлу из которого будем удалять имена. Ожидаемый формат - C:\Users\Igor\Desktop\sdn\out\delete.txt'
              ).grid(row=10, column=0, sticky=W)
        self.removepath = Text(self, width=50, height=1, wrap=WORD)
        self.removepath.grid(row=11, column=0, sticky=W)

    def lastName(self):
        try:
            treepath_uncode = self.treepath.get("1.0", END)
            tree2 = ET.parse(treepath_uncode.removesuffix('\n'))
            root2 = tree2.getroot()
            removepath_uncode = self.removepath.get("1.0", END)
            removepath = removepath_uncode.removesuffix('\n')
            outpath_uncode = self.outpath.get("1.0", END)
            outpath = outpath_uncode.removesuffix('\n')
            self.info_text.insert(END,'Процесс удаления слов запущен, как закончу сообщу.' + '\n')
            removes = open(removepath, 'r+')
            self.info_text.insert(END,'Открываю файл для удаления слов'+ '\n')
            removeses = removes.read().splitlines()
            self.info_text.insert(END,'Ищу совпадения'+ '\n')
            for listoffirstnames in root2.findall('.//{http://tempuri.org/sdnList.xsd}lastName'):
                if listoffirstnames.text in removeses:
                    self.info_text.insert(END, f'Вижу имя {listoffirstnames.text}'+ '\n')
                    self.info_text.insert(END,f'Нашёл совпадение, удаляю'+ '\n')
                    listoffirstnames.text = ' '
                    tree2.write(f'{outpath}\dump.xml')
            self.info_text.insert(END,'Почти готово, записываю получившийся файл'+ '\n')
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
            self.info_text.insert(END, 'Всё готово, можно проверять' + '\n')
        except:
            self.info_text.insert(0.0,'Введён некорректный путь, программа не сработает'+'\n')


    def firstName(self):
        try:
            treepath_uncode = self.treepath.get("1.0", END)
            tree2 = ET.parse(treepath_uncode.removesuffix('\n'))
            root2 = tree2.getroot()
            removepath_uncode = self.removepath.get("1.0", END)
            removepath = removepath_uncode.removesuffix('\n')
            outpath_uncode = self.outpath.get("1.0", END)
            outpath = outpath_uncode.removesuffix('\n')
            self.info_text.insert(END, 'Процесс удаления слов запущен, как закончу сообщу.' + '\n')
            removes = open(removepath, 'r+')
            self.info_text.insert(END, 'Открываю файл для удаления слов' + '\n')
            removeses = removes.read().splitlines()
            self.info_text.insert(END, 'Ищу совпадения' + '\n')
            for listoffirstnames in root2.findall('.//{http://tempuri.org/sdnList.xsd}firstName'):
                if listoffirstnames.text in removeses:
                    self.info_text.insert(END, f'Вижу имя {listoffirstnames.text}'+ '\n')
                    self.info_text.insert(END, f'Нашёл совпадение, удаляю' + '\n')
                    listoffirstnames.text = ' '
                    tree2.write(f'{outpath}\dump.xml')
            self.info_text.insert(END, 'Почти готово, записываю получившийся файл' + '\n')
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
            self.info_text.insert(END, 'Всё готово, можно проверять' + '\n')
        except:
            self.info_text.insert(0.0, 'Введён некорректный путь, программа не сработает' + '\n')

    def sdnEntry(self):
        treepath_uncode = self.treepath.get("1.0", END)
        tree2 = ET.parse(treepath_uncode.removesuffix('\n'))
        root2 = tree2.getroot()
        removepath_uncode = self.removepath.get("1.0", END)
        removepath = removepath_uncode.removesuffix('\n')
        outpath_uncode = self.outpath.get("1.0", END)
        outpath = outpath_uncode.removesuffix('\n')
        self.info_text.insert(END, 'Процесс удаления слов запущен, как закончу сообщу.' + '\n')
        removes = open(removepath, 'r+')
        self.info_text.insert(END, 'Открываю файл для удаления слов' + '\n')
        removeses = removes.read().splitlines()
        i = -1
        self.info_text.insert(END, 'Ищу совпадения' + '\n')
        a1 = root2.findall('.//{http://tempuri.org/sdnList.xsd}sdnEntry')
        summa = sum(1 for line in a1)
        for list in a1:
            i+=1
            if int(i) == int(summa - 1):
                self.info_text.insert(END,'Дошёл до конца файла'+ '\n')
                break
            if a1[i][1].text in removeses:
                self.info_text.insert(END,f'Вижу имя {a1[i][1].text}'+ '\n')
                self.info_text.insert(END,f'Нашёл совпадение, удаляю'+ '\n')
                a1[i].clear()
                tree2.write(f'{outpath}\dump.xml')
        self.info_text.insert(END,'Почти готово, записываю получившийся файл'+ '\n')
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
        self.info_text.insert(END, 'Всё готово, можно проверять' + '\n')

def main():
    root = Tk()
    root.title('OFAC SDN LIST PARSER')
    root.geometry('800x800')
    app = Application(root)
    app.mainloop()

main()
