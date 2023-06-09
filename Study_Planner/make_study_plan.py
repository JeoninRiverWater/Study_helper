subject_entries_value = ['문학', '수학', '영어', '화학', '생명과학']
time_entries_value = ['10', '10', '10', '10', '10']
checkbox_vars = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1]

def make_study_plan(subjuct_var, time_var, schedule) : 
    available_time = 0
    for i in range(len(checkbox_vars)) : 
        if checkbox_vars[i] == 1 : 
            available_time += 1
    print(available_time)
make_study_plan(subject_entries_value, time_entries_value, checkbox_vars)

# print(study_plan)