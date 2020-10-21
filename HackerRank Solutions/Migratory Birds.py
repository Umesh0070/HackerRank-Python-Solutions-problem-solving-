arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))


def migratoryBirds(arr):
    seen = {}
    duplicates = []
    for i in arr:
        if i not in seen:
            seen[i] = 1
        else:
            if seen[i] == 1:
                duplicates.append(i)
            seen[i] += 1
    mostRepeated = max(seen.values())
    listOfKeys = [key for (key, value) in seen.items() if value == mostRepeated]
    finalResult = min(listOfKeys)
    print(finalResult)


migratoryBirds(arr)