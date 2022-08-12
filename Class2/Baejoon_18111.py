import sys
from collections import Counter
input = sys.stdin.readline

N, M, B = map(int,input().split())
block = []
for i in range(N):
    block.append(list(map(int,input().split())))


print(block)