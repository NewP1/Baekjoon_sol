import sys
T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    if round(N % H) != 0:
        hund = round(N % H)
        print(hund * 100 + (int(N / H) + 1))
    else:
        print(H * 100 + int(N / H))