import sys
T = int(sys.stdin.readline())

for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    floor = [x for x in range(1, n+1)]
    for j in range(k):
        for m in range(1, n):
            floor[m] += floor[m-1]
    print(floor[-1])