from tkinter import *
from tkinter.ttk import Combobox


root = Tk()
root.title("Изменение цвета холста")
root.geometry("200x150")

# Функция для изменения цвета холста
def Color(event):
    selected_color = color_combobox.get()  # Вывод выбранного цвета
    canvas.config(bg=selected_color)  # Меняет цвет

# Список
color_combobox = Combobox(root, values=["blue", "yellow", "green"], state="readonly")
color_combobox.set("blue")  # Начальное значение
color_combobox.pack(pady=5)

# Изменение цвета
color_combobox.bind("<<ComboboxSelected>>", Color)

# Создаем холст
canvas = Canvas(root, width=200, height=100, bg="blue")
canvas.pack()


root.mainloop()
