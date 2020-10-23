# As Input Format is A single line of five space-separated integers, we can follow naive solution as below
array = list(map(int, input().rstrip().split()))
firstNumber = sum([x for i,x in enumerate(array) if i!=0])
secondNumber = sum([x for i,x in enumerate(array) if i!=1])
thirdNumber = sum([x for i,x in enumerate(array) if i!=2])
fourthNumber = sum([x for i,x in enumerate(array) if i!=3])
fifthNumber = sum([x for i,x in enumerate(array) if i!=4])
sumOfAllNumbers = [firstNumber,secondNumber,thirdNumber,fourthNumber,fifthNumber]
print(min(sumOfAllNumbers),max(sumOfAllNumbers))