import os
import time
from win10toast import ToastNotifier

toaster = ToastNotifier()

banned_list = {'메모장' : "notepad.exe"}

while True :
    for i in range(len(banned_list)):
        if (os.system(f'taskkill /f /im {list(banned_list.values())[i]}')) == 0 :    
            toaster.show_toast("프로그램 감지", f"{list(banned_list.keys())[i]} 사용이 감지되었습니다")
    time.sleep(1)