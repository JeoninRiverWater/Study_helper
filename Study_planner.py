# 공부 기간, 하루 동안 공부 가능한 시간, 공부하려는 과목과 범위 등을 입력받아서 엑셀 형식으로 작성해주는 프로그램
# 집중 모드, 계획표 진행 확인or점검, 계획표 따라서 알림, youtube를 이용한 음악 재생 등 추가 기능

import tkinter as tk

def get_subject() : # 공부 종목과 각각의 공부 시간 데이터
    global subject_entries_value
    global time_entries_value
    def add_subject() :
        add_button.grid(row=len(subject_entries) + 2, column=0)
        delete_button.grid(row=len(subject_entries) + 2, column=1)
        get_button.grid(row=len(subject_entries) + 3, column=0)

        subject_entry = tk.Entry(window)
        subject_entry.grid(row=len(subject_entries) + 1, column=0)
        subject_entries.append(subject_entry.get())
        
        time_entry = tk.Entry(window)
        time_entry.grid(row=len(time_entries) + 1, column=1)
        time_entries.append(time_entry.get())
        

    def delete_subject():
        if len(subject_entries) != 0 and len(time_entries) != 0 :   
            subject_entries.pop()
            time_entries.pop()

            widget = window.grid_slaves(row=len(subject_entries) + 1, column=0)[0]
            widget.grid_forget()

            widget = window.grid_slaves(row=len(time_entries) + 1, column=1)[0]
            widget.grid_forget()
            
            add_button.grid(row=len(subject_entries) + 2, column=0)
            delete_button.grid(row=len(subject_entries) + 2, column=1)

    def get_subject() :
        global subject_entries_value
        global time_entries_value
        for i in range(1, len(subject_entries) + 1) :
            subject_entries_value.append(window.grid_slaves(row=i, column=0)[0].get())
            time_entries_value.append(window.grid_slaves(row=i, column=1)[0].get())
        window.quit()

    window = tk.Tk()

    subject_entries = []
    time_entries = []

    subject_entries_value = []
    time_entries_value = []

    label1 = tk.Label(window, text = '과목')
    label1.grid(row = 0, column = 0)

    label2 = tk.Label(window, text = '시간')
    label2.grid(row = 0, column = 1)

    add_button = tk.Button(window, text="추가", command=add_subject)
    add_button.grid(row=len(subject_entries) + 1, column=0)

    delete_button = tk.Button(window, text="삭제", command=delete_subject)
    delete_button.grid(row=len(subject_entries) + 1, column=1)

    get_button = tk.Button(window, text="완료", command=get_subject)
    get_button.grid(row=len(subject_entries) + 2, column=0)

    add_subject()

    window.mainloop()

get_subject()
print(subject_entries_value, time_entries_value)


def get_data() : # 일당/주당 공부 가능 시간 데이터
    window = tk.Tk()
    # 1. 일주일 시간표를 보여주며 가능한 시간대를 선택


def make_study_plan() : # 시간 계획표 작성 및 엑셀/한글/txt 등의 파일 공유
    pass


"""
분할 정복 기법: 공부 종목과 시간을 입력받아서 전체 공부 기간을 분할하여 계획표를 생성하는 방법입니다. 예를 들어, 입력받은 총 공부 시간을 일주일로 나누고, 각 주차에 공부할 과목과 시간을 할당하는 방식입니다. 이를 통해 전체 계획을 작은 단위로 분할하여 구체적인 일정을 설정할 수 있습니다.

우선순위 알고리즘: 입력받은 공부 종목을 우선순위에 따라 정렬하고, 시간을 할당하는 방법입니다. 각 과목의 우선순위를 사용자에게 입력받거나, 알고리즘을 통해 자동으로 판단할 수 있습니다. 우선순위에 따라 공부할 과목에 더 많은 시간을 할당하여 중요한 과목에 집중할 수 있습니다.

기간 대비 비율 할당: 사용자로부터 총 공부 기간과 각 공부 종목의 예상 필요 시간을 입력받아, 해당 비율에 따라 계획표를 생성하는 방법입니다. 예를 들어, 총 공부 기간이 4주이고 어떤 과목이 전체 공부 시간의 30%를 차지해야 한다면, 해당 과목에는 4주 중 1.2주를 할당하는 식입니다.

학습 계획 자동 조정: 계획표를 초기에 생성한 후, 사용자의 진행 상황이나 성취도를 계속해서 모니터링하고 분석하여 계획을 자동으로 조정하는 방법입니다. 예를 들어, 과목별로 예상 시간과 실제 공부 시간을 비교하고, 지연된 과목에 추가 시간을 할당하거나, 진도에 따라 자동으로 계획을 업데이트하는 것입니다.
"""
"""
1. 공부 종목과 시간 입력(완) get_data() 함수
2. 공부 가능한 날짜와 시간, 공부 기간 등 입력
3. 입력받은 데이터를 토대로 계획표 작성(위의 방법을 따라감)
ㄴ  여러 가지 제안 중 사용자가 마음에 드는 것을 선택하는 방식을 사용
4. 사용자의 추가적인 수정
5. 계획표 데이터 저장, 이후 원할 때 불러오기가 가능하도록 제작
"""