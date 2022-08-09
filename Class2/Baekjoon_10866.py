import sys
from collections import deque
input = sys.stdin.readline

def process(command):
    if command[0] == "push_front":
        q.appendleft(command[1])

    elif command[0] == "push_back":
        q.append(command[1])

    elif command[0] == "pop_front":
        if not q:
            print(-1)
        else:
            print(q.popleft())

    elif command[0] == "pop_back":
        if not q:
            print(-1)
        else:
            print(q.pop())

    elif command[0] == "size":
        print(len(q))

    elif command[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)

    elif command[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    else:
        if not q:
            print(-1)
        else:
            print(q[-1])

N = int(input())
q = deque()

for i in range(N):
    command = input().split()
    process(command)