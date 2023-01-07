import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dict = {}

for i in range(1, N+1):
    tmp = input().rstrip()
    dict[i] = tmp
    dict[tmp] = i

for i in range(M):
    tmp = input().rstrip()
    if tmp.isdigit():
        print(dict[int(tmp)])
    else:
        print(dict[tmp])