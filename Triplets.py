a = map(int, input().strip().split())
b = map(int, input().strip().split())

aVal = []
bVal = []
finalResult = []

for x in a:
    aVal.append(x)
for y in b:
    bVal.append(y)

aResult = len([i for i, j in zip(aVal, bVal) if i > j])
bResult = len([j for i, j in zip(aVal, bVal) if i < j])
finalResult.append(aResult)
finalResult.append(bResult)
print(finalResult)
