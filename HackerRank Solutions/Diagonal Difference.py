n = int(input().strip())
arr = []
for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
def difference(arr, n): 
    firstDia,secondDia = 0,0
    for ir in range(0, n): 
        firstDia += arr[ir][ir] 
        print(f"firstDia is value {arr[0][1]} ") 
        secondDia += arr[ir][n - ir - 1]   
        print(f"secondDia value {arr[ir][n - ir - 1]} ") 
    return abs(firstDia - secondDia)         
print(difference(arr, n)) 