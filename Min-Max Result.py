n = 10
scores = [3, 4, 21 ,36, 10 ,28 ,35, 5, 24, 42]

firstScore = scores[0]
maxResult = []
minResult = []
for score in scores[1:]:
    if score > firstScore:
        maxResult.append(score)
    if score < firstScore:
        minResult.append(score)
print(len(set(maxResult)))
print(len(set(minResult)))