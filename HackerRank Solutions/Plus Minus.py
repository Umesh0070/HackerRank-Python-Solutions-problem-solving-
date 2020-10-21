n = int(input())
arr = list(map(int, input().rstrip().split()))

newarr = [x for x in arr]
pos = 0
neg = 0
zero = 0
for operator in newarr:
    if operator > 0:
        pos+=1
    elif operator < 0:
        neg+=1
    else:
        zero+=1
print(str.format('{0:.6f}', pos/n))
print(str.format('{0:.6f}', neg/n))
print(str.format('{0:.6f}', zero/n))


