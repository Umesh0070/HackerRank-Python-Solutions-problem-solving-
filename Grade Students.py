grades_count = int(input().strip())
grades = []
finalResult = []
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)
for grade in grades:
    if grade >=38:
        if grade % 5 == 3:
            grade += 2
        elif grade % 5 == 4:
            grade += 1
    finalResult.append(grade)
print(finalResult)
