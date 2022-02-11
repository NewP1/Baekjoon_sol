import sys
N = int(sys.stdin.readline())
cnt = 0
while N > 0 and N % 5 != 0:
    N -= 3
    cnt += 1
if N < 0:
    print('-1')
else:
    print(round(cnt + (N / 5)))