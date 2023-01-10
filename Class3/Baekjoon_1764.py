import sys
input = sys.stdin.readline

n, m = map(int, input().split())

see = set()
hear = set()

for _ in range(n):
    see.add(input().rstrip())
for _ in range(m):
    hear.add(input().rstrip())

see_hear = sorted(list(see & hear))
print(len(see_hear))
for name in see_hear:
    print(name)
