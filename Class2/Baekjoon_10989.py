import sys
input = sys.stdin.readline

N = int(input())
cnt_list = [0 for i in range(10000)]

for i in range(N):
    cnt_list[int(input()) - 1] += 1

for i in range(len(cnt_list)):
    if cnt_list[i] != 0:
        for j in range(cnt_list[i]):
            print(i + 1)