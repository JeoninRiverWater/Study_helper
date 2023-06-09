import tkinter as tk
from tkinter import ttk
import calendar


def get_period_data() : 
    window = tk.Tk()

    combobox1 = ttk.Combobox(window, values = list(range(1, 13)))
    combobox1.grid(row = 0 , column = 0)

    combobox2 = ttk.Combobox(window, values = list(range(1, 32)))
    combobox2.grid(row = 0 , column = 1)

    combobox3 = ttk.Combobox(window, values = list(range(1, 13)))
    combobox3.grid(row = 0 , column = 3)

    combobox4 = ttk.Combobox(window, values = list(range(1, 32)))
    combobox4.grid(row = 0 , column = 4)

    window.mainloop()

get_period_data()