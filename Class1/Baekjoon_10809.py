word = list(input())
abc = list('abcdefghijklmnopqrstuvwxyz')
arr = [-1 for i in range(26)]

for i in range(len(word)):
    if arr[abc.index(word[i])] == -1:
        arr[abc.index(word[i])] = i
for i in range(len(abc)):
    print(arr[i],end=' ')

"""
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x))) 
    """