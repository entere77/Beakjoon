n, m = map(int, input().split())
board = []
result = [] 
for _ in range(n):
    board.append(input())
 
for i in range(n-7):
    for j in range(m-7):
        count_w = 0
        count_b = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'B':
                        count_w += 1
                    if board[k][l] != 'W':
                        count_b += 1
                else:
                    if board[k][l] != 'W':
                        count_w += 1
                    if board[k][l] != 'B':
                        count_b += 1
 
        result.append(count_w)
        result.append(count_b)
print(min(result))