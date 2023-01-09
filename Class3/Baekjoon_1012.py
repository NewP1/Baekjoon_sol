import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())

def bfs(arr, a, b):
    queue = deque()
    queue.append((a, b))
    arr[a][b] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            rx = x + dx[i]
            ry = y + dy[i]
            if rx < 0 or rx >= m or ry < 0 or ry >= n:
                continue
            if arr[ry][rx] == 1:
                arr[ry][rx] = 0
                queue.append((ry, rx))
    return

for _ in range(T):
    cnt = 0
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]

    for _ in range(k):
        tmp_m, tmp_n = map(int, input().split())
        arr[tmp_n][tmp_m] = 1

    for a in range(n):
        for b in range(m):
            if arr[a][b] == 1:
                bfs(arr, a, b)
                cnt += 1
    print(cnt)