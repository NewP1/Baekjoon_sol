N = int(input())
word_list = []
for i in range(N):
    word_list.append(input())

arr = list(set(word_list))
arr.sort()
arr.sort(key=len)

for x in arr:
    print(x)