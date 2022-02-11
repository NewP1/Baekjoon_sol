import sys
N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
ans = list(map(int, sys.stdin.readline().split()))
card.sort()
left = card[:len(card)//2]
right = card[len(card) // 2:]
print(left, right)
"""
def Search(arr, key):
    cnt = 0
    if len(arr) == 1:
        if arr == key:
            cnt += 1
            return cnt
    left = arr[:len(arr)//2]
    right = arr[len(arr) // 2:]
    cnt = Search(left, key) + Search(right, key)
    return cnt
for x in range(M):
    print(Search(card, x), end = ' ')
    """
