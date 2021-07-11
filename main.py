"""
Бег. Пользователь указывает количество км за каждый день в течение
некоторого периода времени. Программа находит общий пробег, среднее
значение в день, наименьшее и наибольшее значения.
"""
from tkinter import *
from tkinter import messagebox
# для вычисления среднего значения
from statistics import mean


class Application(Frame):
    """
    Класс для работы с интерфейсом
    """
    def __init__(self, master):
        """
        Конструктор
        :param master:
        """
        super(Application, self).__init__(master)
        self.grid()
        self.day = 0
        self.qnt_days = None
        self.grid_distance = None
        self.list_distance = []

    def update_day(self):
        """
        Увеличить значение дня
        :return:
        """
        self.day += 1
        day_change = Label(window, text="День " + str(self.day), font=("Arial Bold", 16))
        day_change.grid(column=0, row=0)

    def calculate_result(self):
        """
        Подсчитать результаты и скрыть блоки
        :return:
        """
        lbl1.grid_remove()
        lbl2.grid_remove()
        button2.grid_remove()
        grid_distance.grid_remove()
        results = ''
        for number in self.list_distance:
            results += str(number) + ' '
        lbl3 = Label(window, text="Результаты: " + results, font=("Arial Bold", 18))
        lbl3.grid(column=0, row=0)
        lbl_result = Label(
            window,
            text="Итоговая дистанция = " + str(sum(self.list_distance)),
            font=("Arial Bold", 14)
        )
        lbl_result.grid(column=0, row=1)
        lbl_average = Label(
            window,
            text="Средняя дистанция = " + str(mean(self.list_distance)),
            font=("Arial Bold", 14)
        )
        lbl_average.grid(column=0, row=2)
        lbl_max = Label(
            window,
            text="Максимальная дистанция = " + str(max(self.list_distance)),
            font=("Arial Bold", 14)
        )
        lbl_max.grid(column=0, row=3)
        lbl_min = Label(
            window,
            text="Минимальная дистанция = " + str(min(self.list_distance)),
            font=("Arial Bold", 14)
        )
        lbl_min.grid(column=0, row=4)

    def count_distance(self):
        """
        Подсчитываем дистанцию
        :return:
        """
        try:
            self.list_distance.append(int(self.grid_distance.get()))
        except ValueError:
            messagebox.showerror('Ошибка', 'Введено не число!')
            self.master.destroy()
            exit()
        if self.qnt_days != self.day:
            self.create_fields()
        else:
            self.calculate_result()

    def create_fields(self):
        """
        Создать поля для подсчёта
        :return:
        """
        lbl1.config(text="День " + str(self.day))
        lbl1.grid(column=1, row=0)
        self.update_day()
        lbl2.grid(column=1, row=0)
        grid_distance.grid(column=1, row=1)
        self.grid_distance = grid_distance
        button2.grid(column=1, row=2)

    def preparation(self):
        if self.qnt_days is None:
            try:
                number = int(quantity_days.get())
                if number <= 0:
                    raise ValueError
                self.qnt_days = number
            except ValueError:
                messagebox.showerror('Ошибка', 'Введено недопустимое значение!')
                self.master.destroy()
                exit()
        lbl.grid_remove()
        quantity_days.grid_remove()
        button.grid_remove()
        self.create_fields()


window = Tk()
window.title("Калькулятор")
window.geometry('500x350')
app = Application(window)

lbl1 = Label(window, text="", font=("Arial Bold", 14))
lbl2 = Label(window, text="Введите кол-во км:", font=("Arial Bold", 14))
button2 = Button(window, text="Принять", command=app.count_distance, font=("Arial Bold", 14))
grid_distance = Spinbox(window, from_=1, to=100, font=("Arial Bold", 14))

lbl = Label(window, text="Введите кол-во дней:", font=("Arial Bold", 14))
lbl.grid(column=0, row=1)

quantity_days = Spinbox(window, from_=1, to=100, font=("Arial Bold", 14))
quantity_days.grid(column=1, row=1)

button = Button(window, text="Принять", command=app.preparation, font=("Arial Bold", 14))
button.grid(column=1, row=2)

window.mainloop()



