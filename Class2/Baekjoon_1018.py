N, M = map(int, input().split())
board = []
b_cut = []

for i in range(N):
    board.append(input())

for a in range(N-7):
    for b in range(M-7):
        idxW = 0
        idxB = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        idxW += 1
                    if board[i][j] != 'B':
                        idxB += 1
                else:
                    if board[i][j] != 'B':
                        idxW += 1
                    if board[i][j] != 'W':
                        idxB += 1
        b_cut.append(idxB)
        b_cut.append(idxW)
print(min(b_cut))