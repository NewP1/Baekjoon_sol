import sys
N = int(sys.stdin.readline())
plist = []
anslist = [1 for _ in range(N)]
for _ in range(N):
    plist.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if plist[i][0] < plist[j][0]:
            if plist[i][1] < plist[j][1]:
                anslist[i] += 1
for x in anslist:
    print(x, end = ' ')