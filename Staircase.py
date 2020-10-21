n = int(input())
print('\n'.join([' '*(n-x)+'#'*x for x in range(1,n+1)]))