import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cnt = 0
coin_list = []

for _ in range(n):
    coin_list.insert(0, int(input()))
for coin in coin_list:
    cnt += k // coin
    k = k % coin

print(cnt)