def anagr(a,b):
    a= a.replace(' ' ,'').lower()
    b= b.replace(' ' ,'').lower()
    
    if len(a) != len(b):
        print('Not anagram')
    
    count = {}

    for letter in a:
        if letter in count:
            count[letter] +=1
        else:
            count[letter] = 1
    for letter in b:
        if letter in count:
            count[letter] -=1
        else:
            count[letter] =1
    for k in count:
        if count[k] !=0:
            print('Not anagram')
    print('anagram')
anagr(input(),input())



















# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# print (pow(a,b)+pow(c,d))


# for i in range(1,int(input())):
#     print ([0, 1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999][i])

# n = int(input())
# integer_list = map(int, input().split())
# print(input()==0 or hash(tuple(map(int,input().strip().split()))))
# print([hash(tup) for tup in tuple])