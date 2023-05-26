import pandas as pd

# Excel 파일 열기
file_path = 'Study_Planner/exam_plan.xlsx'

df = pd.read_excel(file_path)

print(df)
print(df[df.columns[1]])