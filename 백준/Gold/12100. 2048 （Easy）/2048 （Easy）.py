from copy import deepcopy

def move(board, direction):
    n = len(board)
    if direction == 0:  # 위쪽
        for j in range(n):
            temp = [board[i][j] for i in range(n) if board[i][j] != 0]
            for i in range(1, len(temp)):
                if temp[i] == temp[i-1]:
                    temp[i-1] *= 2
                    temp[i] = 0
            temp = [x for x in temp if x != 0]
            for i in range(n):
                board[i][j] = temp[i] if i < len(temp) else 0
    elif direction == 1:  # 아래쪽
        for j in range(n):
            temp = [board[i][j] for i in range(n) if board[i][j] != 0]
            for i in range(len(temp)-1, 0, -1):
                if temp[i] == temp[i-1]:
                    temp[i] *= 2
                    temp[i-1] = 0
            temp = [x for x in temp if x != 0]
            for i in range(n):
                board[n-1-i][j] = temp[-1-i] if i < len(temp) else 0
    elif direction == 2:  # 왼쪽
        for i in range(n):
            temp = [board[i][j] for j in range(n) if board[i][j] != 0]
            for j in range(1, len(temp)):
                if temp[j] == temp[j-1]:
                    temp[j-1] *= 2
                    temp[j] = 0
            temp = [x for x in temp if x != 0]
            for j in range(n):
                board[i][j] = temp[j] if j < len(temp) else 0
    elif direction == 3:  # 오른쪽
        for i in range(n):
            temp = [board[i][j] for j in range(n) if board[i][j] != 0]
            for j in range(len(temp)-1, 0, -1):
                if temp[j] == temp[j-1]:
                    temp[j] *= 2
                    temp[j-1] = 0
            temp = [x for x in temp if x != 0]
            for j in range(n):
                board[i][n-1-j] = temp[-1-j] if j < len(temp) else 0
    return board

def dfs(board, cnt):
    if cnt == 5:
        return max(map(max, board))
    max_value = 0
    for direction in range(4):
        new_board = deepcopy(board)
        moved_board = move(new_board, direction)
        max_value = max(max_value, dfs(moved_board, cnt + 1))
    return max_value

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

print(dfs(board, 0))
