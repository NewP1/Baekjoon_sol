M, N = map(int, input().split())

def prime(m, n):
    n += 1
    arr = [True] * n
    temp = int(n ** 0.5)
    for i in range(2, temp + 1):
        if arr[i]:
            for j in range(2*i, n, i):
                arr[j] = False

    for i in range(m, n):
        if i > 1 and arr[i]:
            print(i)

prime(M,N)