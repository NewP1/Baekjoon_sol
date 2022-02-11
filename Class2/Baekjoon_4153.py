
import sys

while 1:
    arr = list(map(int, sys.stdin.readline().split()))
    if sum(arr) == 0:
        break
    m_num = max(arr)
    arr.remove(m_num)
    if arr[0] ** 2 + arr[1] ** 2 == m_num ** 2:
        print("right")
    else:
        print("wrong")
