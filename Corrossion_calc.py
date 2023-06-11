from tkinter import *
from tkinter import ttk


def mm_to_M(mm: float):
    m = float(mm) / 1000
    return m


def year_to_sec(year: float):
    sec = float(year) * 31557600
    return sec


def mm_y_to_m_s(mm_y):
    mm_per_m = 1000
    sec_per_y = 31557600
    m_s = (mm_y / mm_per_m) / sec_per_y
    return m_s


def calc_Uk1(tnom, tf1, tsl):
    uk1_entry.focus_set()
    #uk1 = str((mm_to_M(tnom) - mm_to_M(tf1)) / year_to_sec(tsl))
    uk1 = (tnom - tf1) / tsl
    return uk1


def calc_Uk2(tf1, tf2, tpr):
    uk2_entry.focus_set()
    #uk2 = str((mm_to_M(tf1) - mm_to_M(tf2)) / year_to_sec(tpr))
    uk2 = (tf1 - tf2) / tpr
    return uk2


def calc_t_prog_ob1(tf2, totb, Uk1):
    t_prog_ob1_entry.focus_set()
    t_prog_ob1 = (tf2 - totb) / Uk1
    return t_prog_ob1


def calc_t_prog_ob2(tf2, totb, uk2):
    t_prog_ob1_entry.focus_set()
    t_prog_ob2 = (tf2 - totb) / uk2
    return t_prog_ob2

def calc_ak(uk2, uk1, tpr):
    ak_entry.focus_set()
    ak = mm_to_M((uk2 - uk1)) / year_to_sec(tpr)
    return ak

def calc_t_usk1(ak, tf2, totb, uk2):
    t_usk1_entry.focus_set()
    t_usk1 = ((((2*ak * mm_to_M(tf2 - totb) + mm_y_to_m_s(uk2) ** 2) ** 0.5) - mm_y_to_m_s(uk2))) / ak
    return t_usk1


def finish():
    window.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")


"""Параметры окна"""
window = Tk()
window.title("Калькулятор коррозии")
window.geometry('1300x700')
window.resizable(width=False, height=False)
window.protocol("WM_DELETE_WINDOW", finish)

"""Вкладки"""
notebook = ttk.Notebook(window)

# создание фрейма для первой вкладки
tab1 = Frame(notebook)
tab1.grid(row=0, column=0, sticky="nsew")

"""Лейбл Расчет скорости коррозии"""
lbl_Uk1_name = Label(tab1, text="Расчет скорости коррозии:",
                     width=85, font=("Arial", 14), anchor="w", padx=1, pady=1)
lbl_Uk1_name.grid(column=0, row=0, sticky="W")

"""Расчет скорости коррозии за весь срок эксплуатации"""
lbl_uk1_form = Label(tab1, text="Расчет скорости коррозии за весь срок эксплуатации:    uk1 = (tnom - tf1 ) / tsl",
                       width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_uk1_form.grid(column=0, row=1, sticky="W")


"""tnom """
lbl_tnom = Label(tab1, text="Номинальная толщина стенки трубы (tnom) =",
                 width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)

lbl_tnom.grid(column=0, row=2, sticky="W")
tnom_entry = Entry(tab1, width=30, font=("Arial", 12))
tnom_entry.grid(column=1, row=2)

lbl_tnom_si = Label(tab1, text="мм", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_tnom_si.grid(column=2, row=2, sticky="W")


"""tf1  """
lbl_tf1 = Label(tab1, text="Толщина стенки по результатам предыдущих измерений (tf1) =",
                width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_tf1.grid(column=0, row=3, sticky="W")

tf1_value = StringVar()

tf1_entry = Entry(tab1, width=30, textvariable=tf1_value, font=("Arial", 12))
tf1_entry.grid(column=1, row=3)

lbl_tf1_si = Label(tab1, text="мм", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_tf1_si.grid(column=2, row=3, sticky="W")


"""tsl  """
lbl_tsl = Label(tab1, text="Общий срок службы эксплуатации трубопровода до настоящего измерения (tsl) =",
                width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_tsl.grid(column=0, row=4, sticky="W")

tsl_entry = Entry(tab1, width=30, font=("Arial", 12))
tsl_entry.grid(column=1, row=4)

lbl_tsl_si = Label(tab1, text="лет", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_tsl_si.grid(column=2, row=4, sticky="W")


"""Кнопка расчитать Uk1"""
btn_uk1 = Button(tab1, text="Рассчитать >>>", width=85, font=("Arial", 12), command=lambda: result_uk1.
                 set(calc_Uk1(float(tnom_entry.get()), float(tf1_entry.get()), float(tsl_entry.get()))))
btn_uk1.grid(column=0, row=5)

result_uk1 = StringVar()

uk1_entry = Entry(tab1, width=30, textvariable=result_uk1, font=("Arial", 12))
uk1_entry.grid(column=1, row=5)

lbl_Uk1_si = Label(tab1, text="мм/год", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_Uk1_si.grid(column=2, row=5, sticky="W")


"""Расчет скорости коррозии за период между измерениями толщин стенок (uk2)"""
lbl_uk2_name = Label(tab1, text="Расчет скорости коррозии за период между измерениями толщин стенок:",
                     width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_uk2_name.grid(column=0, row=6, sticky="W")
lbl_uk2_form = Label(tab1, text="Uk2 = tf1 -tf2 ) / tpr", width=30, font=("Arial", 12), padx=1, pady=1)
lbl_uk2_form.grid(column=1, row=6, sticky="W")

"""tf1"""
lbl_tf11 = Label(tab1, text="Толщина стенки по результатам предыдущих измерений (tf1) =",
                 width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_tf11.grid(column=0, row=7, sticky="W")

tf11_entry = Entry(tab1, width=30, textvariable=tf1_value, font=("Arial", 12))
tf11_entry.grid(column=1, row=7)

lbl_tf11_si = Label(tab1, text="мм", width=10, anchor="w", font=("Arial", 14), padx=1, pady=1)
lbl_tf11_si.grid(column=2, row=7, sticky="W")


"""tf2"""
lbl_tf2 = Label(tab1, text="Фактическую толщина стенки по результатам настоящих измерений (tf2) =",
                width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_tf2.grid(column=0, row=8, sticky="W")

tf2_value = StringVar()

tf2_entry = Entry(tab1, width=30, textvariable=tf2_value, font=("Arial", 12))
tf2_entry.grid(column=1, row=8)

lbl_tf2_si = Label(tab1, text="мм", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_tf2_si.grid(column=2, row=8, sticky="W")


"""tpr"""
lbl_tpr = Label(tab1, text="Время между настоящим и предыдущим измерениям (tpr) =",
                width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_tpr.grid(column=0, row=9, sticky="W")

tpr_value = StringVar()

tpr_entry = Entry(tab1, width=30, textvariable=tpr_value, font=("Arial", 12))
tpr_entry.grid(column=1, row=9)

lbl_tpr_si = Label(tab1, text="лет", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_tpr_si.grid(column=2, row=9, sticky="W")

"""Кнопка рассчитать Uk2"""
btn_uk2 = Button(tab1, text="Рассчитать >>>", width=85, font=("Arial", 12), command=lambda: result_uk2.
                 set(calc_Uk2(float(tf11_entry.get()), float(tf2_entry.get()), float(tpr_entry.get()))))
btn_uk2.grid(column=0, row=10)

result_uk2 = StringVar()

uk2_entry = Entry(tab1, width=30, textvariable=result_uk2, font=("Arial", 12))
uk2_entry.grid(column=1, row=10)

lbl_uk2_si = Label(tab1, text="мм/год", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_uk2_si.grid(column=2, row=10, sticky="W")


"""_______________________________________ВКЛАДКА_2___________________________________________"""
tab2 = Frame(notebook)

"""Лейбл Расчет прогнозируемого срока службы"""
lbl_name = Label(tab2, text="Расчет прогнозируемого срока службы:",
                 width=85, font=("Arial", 14), anchor="w", padx=1, pady=1)
lbl_name.grid(column=0, row=0, sticky="W")


""" формула 1"""
lbl_t_prog_ob1_name = Label(tab2, text="Расчет остаточного срока службы с учетом скорости коррозии за весь срок "
                                  "эксплуатации:", width=85, font=("Arial", 12), anchor="w", padx=1, pady=1)
lbl_t_prog_ob1_name.grid(column=0, row=1, sticky="W")

lbl_t_prog_ob1_form = Label(tab2, text="t_prog_ob1 = (tf2 - totb ) / uk1",
                      width=30, font=("Arial", 12), anchor="w", padx=1, pady=1)
lbl_t_prog_ob1_form.grid(column=1, row=1, sticky="W")


"""tf21 """
lbl_tf21 = Label(tab2, text="Фактическую толщина стенки по результатам настоящих измерений (tf2) =",
                 width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_tf21.grid(column=0, row=2, sticky="W")

tf21_entry = Entry(tab2, width=30, textvariable=tf2_value, font=("Arial", 12))
tf21_entry.grid(column=1, row=2)

lbl_tf21_si = Label(tab2, text="мм", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_tf21_si.grid(column=2, row=2, sticky="W")


"""totb  """
lbl_totb = Label(tab2, text="Толщина отбраковки стенки по НТД или расчету на прочность (totb) =",
                 width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_totb.grid(column=0, row=3, sticky="W")

totb_value = StringVar()

totb_entry = Entry(tab2, width=30, textvariable=totb_value, font=("Arial", 12))
totb_entry.grid(column=1, row=3)

lbl_totb_si = Label(tab2, text="мм", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_totb_si.grid(column=2, row=3, sticky="W")


"""Uk11  """
lbl_uk11 = Label(tab2, text="Скорость коррозии за весь срок эксплуатации: (uk1) =",
                 width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_uk11.grid(column=0, row=4, sticky="W")

uk11_entry = Entry(tab2, width=30, textvariable=result_uk1, font=("Arial", 12))
uk11_entry.grid(column=1, row=4)

lbl_uk11_si = Label(tab2, text="мм/год", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_uk11_si.grid(column=2, row=4, sticky="W")


"""Кнопка расчитать t_prog_ob1"""
btn_t_prog_ob1 = Button(tab2, text="Рассчитать >>>", width=85, font=("Arial", 12), command=lambda: result_t_prog_ob1.
                 set(calc_t_prog_ob1(float(tf21_entry.get()), float(totb_entry.get()), float(uk11_entry.get()))))
btn_t_prog_ob1.grid(column=0, row=5)

result_t_prog_ob1 = StringVar()

t_prog_ob1_entry = Entry(tab2, width=30, textvariable=result_t_prog_ob1, font=("Arial", 12))
t_prog_ob1_entry.grid(column=1, row=5)

lbl_t_prog_ob1_si = Label(tab2, text="лет", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_t_prog_ob1_si.grid(column=2, row=5, sticky="W")


""" формула 2"""
lbl_t_prog_ob2_name = Label(tab2, text="Расчет остаточного срока службы с учетом скорости коррозии за период м/у "
                                  "последними измерениями:", width=85, font=("Arial", 12), anchor="w", padx=1, pady=1)
lbl_t_prog_ob2_name.grid(column=0, row=6, sticky="W")

lbl_t_prog_ob2_form = Label(tab2, text="t_prog_ob2 = (tf2 - totb) / uk2",
                      width=30, font=("Arial", 12), anchor="w", padx=1, pady=1)
lbl_t_prog_ob2_form.grid(column=1, row=6, sticky="W")


"""tf22 """
lbl_tf22 = Label(tab2, text="Фактическую толщина стенки по результатам настоящих измерений (tf2) =",
                 width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_tf22.grid(column=0, row=7, sticky="W")

tf22_entry = Entry(tab2, width=30, textvariable=tf2_value, font=("Arial", 12))
tf22_entry.grid(column=1, row=7)

lbl_tf22_si = Label(tab2, text="мм", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_tf22_si.grid(column=2, row=7, sticky="W")


"""totb1  """
lbl_totb1 = Label(tab2, text="Толщина отбраковки стенки по НТД или расчету на прочность (totb) =",
                 width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_totb1.grid(column=0, row=8, sticky="W")

totb1_entry = Entry(tab2, width=30, textvariable=totb_value, font=("Arial", 12))
totb1_entry.grid(column=1, row=8)

lbl_totb1_si = Label(tab2, text="мм", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_totb1_si.grid(column=2, row=8, sticky="W")


"""Uk21  """
lbl_uk21 = Label(tab2, text="Cкорость коррозии за период между измерениями толщин стенок (uk2) =",
                 width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_uk21.grid(column=0, row=9, sticky="W")

uk21_entry = Entry(tab2, width=30, textvariable=result_uk2, font=("Arial", 12))
uk21_entry.grid(column=1, row=9)

lbl_uk21_si = Label(tab2, text="мм/год", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_uk21_si.grid(column=2, row=9, sticky="W")


"""Кнопка расчитать t_prog_ob1"""
btn_t_prog_ob2 = Button(tab2, text="Рассчитать >>>", width=85, font=("Arial", 12), command=lambda: result_t_prog_ob2.
                 set(calc_t_prog_ob1(float(tf21_entry.get()), float(totb1_entry.get()), float(uk21_entry.get()))))
btn_t_prog_ob2.grid(column=0, row=10)

result_t_prog_ob2 = StringVar()

t_prog_ob2_entry = Entry(tab2, width=30, textvariable=result_t_prog_ob2, font=("Arial", 12))
t_prog_ob2_entry.grid(column=1, row=10)

lbl_t_prog_ob2_si = Label(tab2, text="лет", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_t_prog_ob2_si.grid(column=2, row=10, sticky="W")


""" формула 3"""
lbl_ak_name = Label(tab2, text="Расчет ускорения скорости коррозии за последний период измерения:",
                       width=85, font=("Arial", 12), anchor="w", padx=1, pady=1)
lbl_ak_name.grid(column=0, row=11, sticky="W")

lbl_ak_form = Label(tab2, text="ak = (uk2 - uk1 ) / tpr", width=30, font=("Arial", 12), anchor="w", padx=1, pady=1)
lbl_ak_form.grid(column=1, row=11, sticky="W")


"""uk22 """
lbl_uk22 = Label(tab2, text="Cкорость коррозии за период между измерениями толщин стенок (uk2) =",
                 width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_uk22.grid(column=0, row=12, sticky="W")

uk22_entry = Entry(tab2, width=30, textvariable=result_uk2, font=("Arial", 12))
uk22_entry.grid(column=1, row=12)

lbl_uk22_si = Label(tab2, text="мм/год", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_uk22_si.grid(column=2, row=12, sticky="W")


"""uk12  """
lbl_uk12 = Label(tab2, text="Скорость коррозии за весь срок эксплуатации: (uk1) =",
                 width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_uk12.grid(column=0, row=13, sticky="W")

uk12_entry = Entry(tab2, width=30, textvariable=result_uk1, font=("Arial", 12))
uk12_entry.grid(column=1, row=13)

lbl_uk12_si = Label(tab2, text="мм/год", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_uk12_si.grid(column=2, row=13, sticky="W")

"""tpr1  """
lbl_tpr1 = Label(tab2, text="Время между настоящим и предыдущим измерениям: (tpr) =",
                width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_tpr1.grid(column=0, row=14, sticky="W")

tpr1_entry = Entry(tab2, width=30, textvariable=tpr_value, font=("Arial", 12))
tpr1_entry.grid(column=1, row=14)

lbl_tpr1_si = Label(tab2, text="лет", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_tpr1_si.grid(column=2, row=14, sticky="W")


"""Кнопка расчитать ak"""
btn_ak = Button(tab2, text="Рассчитать >>>", width=85, font=("Arial", 12), command=lambda: result_ak.
                set(calc_ak(float(uk22_entry.get()), float(uk12_entry.get()), float(tpr1_entry.get()))))
btn_ak.grid(column=0, row=15)

result_ak = StringVar()

ak_entry = Entry(tab2, width=30, textvariable=result_ak, font=("Arial", 12))
ak_entry.grid(column=1, row=15)

lbl_ak_si = Label(tab2, text="м/кв.с", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_ak_si.grid(column=2, row=15, sticky="W")


""" формула 4"""
lbl_t_usk1_name = Label(tab2, text="Расчет остаточного срока с учетом ускорения коррозии:",
                       width=85, font=("Arial", 12), anchor="w", padx=1, pady=1)
lbl_t_usk1_name.grid(column=0, row=16, sticky="W")

lbl_t_usk1_form = Label(tab2, text="t_usk1 = ((((2*ak * (tf2 - totb) + uk2 ** 2) ** 0.5) - uk2)) / ak",
                      width=85, font=("Arial", 12), anchor="center", padx=1, pady=1)
lbl_t_usk1_form.grid(column=0, row=17, sticky="W")


"""ak2 """
lbl_ak2 = Label(tab2, text="Ускорение скорости коррозии за последний период измерения (ak) =",
                 width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_ak2.grid(column=0, row=18, sticky="W")

ak2_entry = Entry(tab2, width=30, textvariable=result_ak, font=("Arial", 12))
ak2_entry.grid(column=1, row=18)

lbl_ak2_si = Label(tab2, text="м/кв.с", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_ak2_si.grid(column=2, row=18, sticky="W")


"""tf22  """
lbl_tf22 = Label(tab2, text="Фактическую толщина стенки по результатам настоящих измерений (tf2) =",
                 width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_tf22.grid(column=0, row=19, sticky="W")

tf22_entry = Entry(tab2, width=30, textvariable=tf2_value, font=("Arial", 12))
tf22_entry.grid(column=1, row=19)

lbl_tf22_si = Label(tab2, text="мм", width=30, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_tf22_si.grid(column=2, row=19, sticky="W")


"""totb2  """
lbl_totb2 = Label(tab2, text="Толщина отбраковки стенки по НТД или расчету на прочность (totb) =",
                width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_totb2.grid(column=0, row=20, sticky="W")

totb2_entry = Entry(tab2, width=30, textvariable=totb_value, font=("Arial", 12))
totb2_entry.grid(column=1, row=20)

lbl_totb2_si = Label(tab2, text="мм", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_totb2_si.grid(column=2, row=20, sticky="W")


"""uk23 """
lbl_uk23 = Label(tab2, text="Cкорость коррозии за период между измерениями толщин стенок (uk2) =",
                 width=85, font=("Arial", 12), anchor="e", padx=1, pady=1)
lbl_uk23.grid(column=0, row=21, sticky="W")

uk23_entry = Entry(tab2, width=30, textvariable=result_uk2, font=("Arial", 12))
uk23_entry.grid(column=1, row=21)

lbl_uk23_si = Label(tab2, text="мм/год", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_uk23_si.grid(column=2, row=21, sticky="W")


"""Кнопка расчитать t_usk1 = calc_t_usk1( ak, tf2, totb, uk2):"""
btn_t_usk1 = Button(tab2, text="Рассчитать >>>", width=85, font=("Arial", 12), command=lambda: result_t_usk1.
                set(calc_t_usk1(float(ak2_entry.get()), float(tf22_entry.get()),
                                float(totb2_entry.get()), float(uk23_entry.get()))))
btn_t_usk1.grid(column=0, row=22)

result_t_usk1 = StringVar()

t_usk1_entry = Entry(tab2, width=30, textvariable=result_t_usk1, font=("Arial", 12))
t_usk1_entry.grid(column=1, row=22)

lbl_t_usk1_si = Label(tab2, text="с", width=10, anchor="w", font=("Arial", 12), padx=1, pady=1)
lbl_t_usk1_si.grid(column=2, row=22, sticky="W")


notebook.add(tab1, text="Скорость коррозии")
notebook.add(tab2, text="Срок службы")


notebook.grid(row=0, column=0, sticky="nsew")

window.mainloop()


#pyinstaller --name==Corrossion_calc Corrossion_calc.py
#pyinstaller Corrossion_calc.spec
