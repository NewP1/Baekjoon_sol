import sys
input = sys.stdin.readline

N = int(input())

dot_list = []

for i in range(N):
    dot_list.append(list(map(int, input().split())))

dot_list.sort()

for dot in dot_list:
    print(f"{dot[0]} {dot[1]} ")