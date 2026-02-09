import csv  
import openpyxl
file = open("sample.txt", "w")
file.write("Hello, this is a file handling example")
file.close()

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")