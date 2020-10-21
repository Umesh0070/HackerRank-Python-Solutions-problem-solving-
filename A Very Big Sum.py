ar_count = int(input())

ar = map(int,input().rstrip().split())

print(sum([x for x in ar]))