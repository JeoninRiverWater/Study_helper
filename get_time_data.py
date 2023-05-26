# 공부 기간, 하루 동안 공부 가능한 시간, 공부하려는 과목과 범위 등을 입력받아서 엑셀 형식으로 작성해주는 프로그램
# 집중 모드, 계획표 진행 확인or점검, 계획표 따라서 알림, youtube를 이용한 음악 재생 등 추가 기능

import tkinter as tk

window = tk.Tk()

day = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
time = ['4시','5시','6시','7시','8시','9시','10시','11시']

for i in range(len(day)) :
    label = tk.Label(window, text=day[i])
    label.grid(row = 0, column = i+1)

for i in range(len(time)) :
    label = tk.Label(window, text=time[i])
    label.grid(row = i+1, column = 0)

for i in range(1, 9) :
    for j in range(1, 8) :
        checkbox = tk.Checkbutton(window)
        checkbox.grid(row=i, column=j)
    
window.mainloop()