import sys
N = int(sys.stdin.readline())
minus = 9 * len(str(N))
if N > minus:
    start = N - minus
else: start = 1
ans = 0

while start < N:
    st_list = list(map(int, str(start)))
    temp = start + sum(st_list)
    if temp == N:
        ans = start
        break
    start += 1
print(ans)

