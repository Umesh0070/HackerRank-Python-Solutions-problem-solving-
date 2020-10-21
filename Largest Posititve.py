arr = 'AAABBBBBCCCDDD'
unique = {}

def uniqueChar(arr):
    for letter in arr:
        if letter in unique:
            unique[letter] += 1
        else:
            unique[letter] = 1
    for k,v in unique.items():
        print(f"{k}{v}")
uniqueChar(arr)
    
# arr = 'AAABBBBBCCCDDD'
# unique = {}

# for letter in arr:
#     if letter in unique:
#         unique[letter] += 0
#     else:
#         unique[letter] = 1
# for k,v in unique.items():
#     print(k)
# print(unique)

