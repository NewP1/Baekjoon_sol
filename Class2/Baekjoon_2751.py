import sys
N = int(sys.stdin.readline())
num_list = []
for i in range(N):
    num_list.append(int(sys.stdin.readline()))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])
    mer = []

    i = 0
    j = 0
    while i < len(L) and j < len(R):
        if L[i] > R[j]:
            mer.append(R[j])
            j += 1
        else:
            mer.append(L[i])
            i += 1
    if i != len(L):
        mer += L[i:]
    if j != len(R):
        mer += R[j:]
    return mer

mer = merge_sort(num_list)
for i in mer:
    print(i)