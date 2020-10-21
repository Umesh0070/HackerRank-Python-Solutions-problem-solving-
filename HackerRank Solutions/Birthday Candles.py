ar_count = int(input())
ar = list(map(int, input().rstrip().split()))

unique = {}
def finder (ar_count,ar):
    for num in ar:
        if num in unique:
            unique[num] += 1
        else:
            unique[num] = 1
    maxVal = max(unique.keys())
    finalR = (value for (key, value) in unique.items() if key == maxVal)
    for result in finalR:
        print(result)
    print(finalR)
           


finder(ar_count,ar)
