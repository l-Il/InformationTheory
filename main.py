from tkinter import *
import tkinter.ttk as ttk


class Main:
    def __init__(self):
        self.root = Tk()
        self.string, self.A, self.dictionary = [], [], []
        self.root.geometry('295x380')
        self.root.title('Теория информации')
        self.root.configure(bg='#202020')
        self.text = Text(self.root, wrap=WORD)
        self.text.place(x=10, y=10, width=275, height=100)

        self.grid_frame = Frame(self.root)
        self.columns = ('1', '2', '3', '4')
        self.tree = ttk.Treeview(self.grid_frame, show='headings', columns=self.columns)
        self.tree.heading('1', text='№')
        self.tree.column('1', width=25, stretch=NO)
        self.tree.heading('2', text='Символ')
        self.tree.column('2', width=55, stretch=NO)
        self.tree.heading('3', text='Вероятность')
        self.tree.column('3', width=120, stretch=NO)
        self.tree.heading('4', text='Частота')
        self.tree.column('4', width=55, stretch=NO)
        self.bar = ttk.Scrollbar(self.grid_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.bar.set)
        self.tree.place(x=0, y=0, width=255, height=200)
        self.bar.place(x=254, y=0, width=20, height=200)
        self.grid_frame.place(x=10, y=130, width=275, height=200)
        Button(self.root, text='Анализ', relief=FLAT, border='0', command=lambda: self.add()).place(x=10, y=340)
        self.root.mainloop()

    def add(self):
        for i in self.tree.get_children():  # Удаляем предыдущий результат
            self.tree.delete(i)
        self.string = list(map(lambda _: _.upper(), list(self.text.get(1.0, END).replace('.', '').replace(' ', '').replace(',', '').replace(':', ''))))  # Преобразуем введённое в список из букв верхнего регистра
        del(self.string[-1])  # Удаляем служебный символ '/n'
        # Считаем количество "уникальных" символов
        self.dictionary = {}
        for _ in self.string:
            keys = self.dictionary.keys()
            if _ in keys:
                self.dictionary[_] += 1
            else:
                self.dictionary[_] = 1

        self.A = [['', '', '', ''] for _ in range(len(self.dictionary))]  # Создаём массив для вывода полученного
        # Ввод и вывод полученных данных в таблицу
        x = 0
        for key in self.dictionary:
            self.A[x][0] = x+1
            self.A[x][1] = key
            self.A[x][2] = self.dictionary[key] / len(self.string)
            self.A[x][3] = self.dictionary[key]
            x += 1
        self.A.sort(key=lambda _: _[1])  # Сортировка символов в алфавитном порядке
        self.A.sort(key=lambda _: _[3], reverse=True)
        for _ in range(len(self.A)):
            self.A[_][0] = _+1
        for _ in self.A:
            self.tree.insert('', END, values=_)
        self.root.update()


_ = Main()

