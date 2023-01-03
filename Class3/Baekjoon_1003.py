import sys
input = sys.stdin.readline


N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(input()))

cnt_0 = [1, 0]
cnt_1 = [0, 1]

for num in num_list:
    if num > 1:
        for i in range(num-1):
            cnt_0.append(cnt_1[-1])
            cnt_1.append(cnt_0[-2] + cnt_1[-1])

    print(cnt_0[num], cnt_1[num])