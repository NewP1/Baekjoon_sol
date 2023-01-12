import sys
input = sys.stdin.readline

cnt = 0

n, r, c = map(int, input().split())

while n != 0:
    n -= 1
    tmp = pow(2, n)

    if c < tmp and r < tmp:
        continue
    elif r < tmp and c >= tmp:
        cnt += pow(tmp , 2)
        c -= tmp
    elif r >= tmp and c < tmp:
        cnt += pow(tmp , 2) * 2
        r -= tmp
    else:
        cnt += 3 * pow(tmp , 2)
        r -= tmp
        c -= tmp

print(cnt)