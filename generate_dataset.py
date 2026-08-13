import pandas as pd
import random

data = []

for _ in range(500):
    attendance = random.randint(50, 100)
    study_hours = random.randint(1, 10)
    previous_marks = random.randint(30, 95)
    assignment_marks = random.randint(40, 100)
    internal_marks = random.randint(35, 100)

    final_marks = (
        attendance * 0.15
        + study_hours * 3
        + previous_marks * 0.30
        + assignment_marks * 0.20
        + internal_marks * 0.25
    )

    final_marks = round(min(100, max(0, final_marks)), 2)

    data.append([
        attendance,
        study_hours,
        previous_marks,
        assignment_marks,
        internal_marks,
        final_marks
    ])

df = pd.DataFrame(data, columns=[
    "Attendance",
    "Study_Hours",
    "Previous_Marks",
    "Assignment_Marks",
    "Internal_Marks",
    "Final_Marks"
])

df.to_csv("data/student_performance.csv", index=False)

print("Dataset created successfully!")
print("Total students:", len(df))