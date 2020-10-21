n = int(input())
ar = list(map(int, input().rstrip().split()))

def sockMerchant(n, ar):
    seen = {}
    duplicates = []
    pairs = []
    firstUniquePair = []
    for i in ar:
        if i not in seen:
            seen[i] = 1
        else:
            if seen[i] == 1:
                duplicates.append(i)
            seen[i] += 1
    values = seen.values()
    for allValues in values:
        if allValues >= 2:
            pairs.append(allValues)
    for allPairs in pairs:
        firstUniquePair.append(int(allPairs//2))
    
    finalResult = sum(firstUniquePair)
    print (finalResult)


sockMerchant(n, ar)

