import sys
input = sys.stdin.readline

S = set()

M = int(input())

for i in range(M):
    c_line = input().split()

    if c_line[0] == "add":
        S.add(int(c_line[1]))

    elif c_line[0] == "remove":
        S.discard(int(c_line[1]))

    elif c_line[0] == "check":
        if int(c_line[1]) in S:
            print("1")
        else:
            print("0")

    elif c_line[0] == "toggle":
        if int(c_line[1]) in S:
            S.discard(int(c_line[1]))
        else:
            S.add(int(c_line[1]))

    elif c_line[0] == "all":
        S = set(x for x in range(1, 21))

    elif c_line[0] == "empty":
        S = set()

