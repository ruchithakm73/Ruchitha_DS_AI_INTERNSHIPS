import csv

file_path = r"D:\DS_AI_Internship\src\Day_6_Fundamentals\Student.csv"

with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
