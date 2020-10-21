arr1 = [1,2,3,4,5,6,7]
arr2 = [3,2,5,1,6,4,4]

unique = {}
dupes = {}
def finder (arr1,arr2):
    if len(arr1) != len(arr2):
        for num in arr1:
            if num in unique:
                unique[num] += 1
            else:
                unique[num] = 1
        for num in arr2:
            if num in unique:
                unique[num] -=1
            else:
                unique[num] = 1
    for k,v in unique.items():
        if v == 1:
            print(f"{k} is the missing number")
    print("No missing number")
finder(arr1,arr2)
