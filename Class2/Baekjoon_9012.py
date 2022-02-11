import sys
N = int(sys.stdin.readline())
for _ in range(N):
    arr = list(sys.stdin.readline())
    stk = []
    temp = True
    for c in arr:
        if c == '(':
            stk.append(c)
        elif c == ')':
            if len(stk) == 0 or stk[-1] == ')':
                temp = False
                break
            elif stk[-1] == '(':
                stk.pop()

    if temp and len(stk) == 0:
        print('YES')
    else:
        print('NO')