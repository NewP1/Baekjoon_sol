import sys

while 1:
    arr = list(sys.stdin.readline())
    if arr == '.':
        break
    nlist = []
    temp = True

    for c in arr:
        if c == '[' or c == '(':
            nlist.append(c)
        elif c == ']':
            if len(nlist) == 0 or nlist[-1] == '(':
                temp = False
                break
            elif nlist[-1] == '[':
                nlist.pop()
        elif c == ')':
            if len(nlist) == 0 or nlist[-1] == '[':
                temp = False
                break
            elif nlist[-1] == '(':
                nlist.pop()

    if temp and len(nlist) == 0:
        print('yes')
    else: print('no')