import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
n_list = list(map(str,input().split()))
M = int(input())
m_list = list(map(str,input().split()))

cnt = Counter(n_list)
ans_list = []

for num in m_list:
    ans_list.append(cnt[num])

print(f'{" ".join(map(str,ans_list))}')
