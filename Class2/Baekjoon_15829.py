import sys

input = sys.stdin.readline

L = int(input())
alpha_list = input()
tot = 0

for i in range(L):
    tot += (ord(alpha_list[i]) - 96) * pow(31, i)

if tot > 1234567891:
    print(tot % 1234567891)
else:
    print(tot)