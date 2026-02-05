marks = {"math": 80, "science": 75, "english": 85}

print(marks.get("math"))
print(marks.get("history", 0))
marks.update({"science": 78, "history": 90})
marks.pop("english")  #Remove the 'english' entry

for subject, score in marks.items():
    print(subject, score)