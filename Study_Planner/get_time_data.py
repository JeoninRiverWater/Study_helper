import tkinter as tk

window = tk.Tk()

day = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
time = ['4시', '5시', '6시', '7시', '8시', '9시', '10시', '11시']

checkbox_vars = []

for i in range(len(day)):
    label = tk.Label(window, text=day[i])
    label.grid(row=0, column=i + 1)

for i in range(len(time)):
    label = tk.Label(window, text=time[i])
    label.grid(row=i + 1, column=0)

for i in range(1, 9):
    row_vars = []
    for j in range(1, 8):
        checkbox_var = tk.IntVar()
        checkbox = tk.Checkbutton(window, variable=checkbox_var)
        checkbox.grid(row=i, column=j)
        row_vars.append(checkbox_var)
    checkbox_vars.append(row_vars)
window.mainloop()

for i in range(len(checkbox_vars)) : 
    for j in range(len(checkbox_vars[i])) : 
        print(checkbox_vars[i][j].get(), end = " ")
    print()