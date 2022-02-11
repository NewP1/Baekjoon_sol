import sys
N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
ans = 0

for i in range(N-2):
    if num_list[i] < M:
        for j in range(i + 1, N - 1):
            if num_list[i] + num_list[j] < M:
                for k in range(j + 1, N):
                    if num_list[i] + num_list[j] + num_list[k] > ans and num_list[i] + num_list[j] + num_list[k] <= M:
                        ans = num_list[i] + num_list[j] + num_list[k]

print(ans)
