import sys
N = int(sys.stdin.readline())
i = 1
tot = 1
while True:
    if N == 1:
        print(i)
        break
    if tot >= N:
        print(i)
        break
    else:
        tot = tot + (6 * i)
    i += 1

