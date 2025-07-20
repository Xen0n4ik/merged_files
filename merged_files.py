import tkinter as tk
from tkinter import END, Text, Button
import os


def combine_files():
    try:
        with open('1.txt', 'r') as f1, open('2.txt', 'r') as f2:
            lines1 = f1.read().splitlines()
            lines2 = f2.read().splitlines()

        if len(lines1) != len(lines2):
            text.insert(END, "Ошибка: файлы имеют разное количество строк\n")
            return

        combined = '\n'.join(f"{l1}{l2}" for l1, l2 in zip(lines1, lines2))

        with open('3.txt', 'w') as f3:
            f3.write(combined)

        text.delete(1.0, END)
        text.insert(END, combined)
        os.startfile('3.txt')

    except FileNotFoundError:
        text.insert(END, "Ошибка: один или оба файла не найдены\n")
    except Exception as e:
        text.insert(END, f"Произошла ошибка: {str(e)}\n")


root = tk.Tk()
root.title('Складывание строк')

text = Text(root)
but1 = Button(root, text='ОК', command=combine_files)

but1.pack()
text.pack()
root.mainloop()
