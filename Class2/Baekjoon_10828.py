import sys
input = sys.stdin.readline

def process(command):
    if command[0] == "push":
        num_list.append(command[1])
    elif command[0] == "pop":
        if not num_list:
            print(-1)
        else:
            print(num_list.pop())
    elif command[0] == "size":
        print(len(num_list))
    elif command[0] == "empty":
        if not num_list:
            print(1)
        else:
            print(0)
    else:
        if not num_list:
            print(-1)
        else:
            print(num_list[-1])


N = int(input())
com_list = []
num_list = []

for i in range(N):
    command = list(map(str, input().split()))
    com_list.append(command)

for command in com_list:
    process(command)