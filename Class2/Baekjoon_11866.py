N, K = map(int,input().split())

num_list = []
ans_list = []
for i in range(1, N + 1):
    num_list.append(i)

while len(num_list) != 0:
    for i in range(K-1):
        num_list.append(num_list.pop(0))
    ans_list.append(num_list.pop(0))

print(f'<{", ".join(map(str,ans_list))}>') # f-string 포맷팅
