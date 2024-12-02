import copy
def move(board, direction):
    # 오른쪽 이동
    if direction == 0:
        for i in range(n):
            temp = [board[i][j] for j in range(n) if board[i][j] != 0]
            for j in range(len(temp)-1, 0, -1):
                if temp[j] == temp[j-1]:
                    temp[j] *= 2
                    temp[j-1] = 0
            temp = [x for x in temp if x != 0]

            for j in range(n):
                board[i][-1-j] = temp[-1-j] if j < len(temp) else 0

    # 왼쪽 이동
    elif direction == 1:
        for i in range(n):
            temp = [board[i][j] for j in range(n) if board[i][j] != 0]
            for j in range(len(temp)-1):
                if temp[j] == temp[j+1]:
                    temp[j] *= 2
                    temp[j+1] = 0
            temp = [x for x in temp if x != 0]

            for j in range(n):
                board[i][j] = temp[j] if j < len(temp) else 0
    # 아래쪽 이동
    if direction == 2:
        for i in range(n):
            temp = [board[j][i] for j in range(n) if board[j][i] != 0]
            for j in range(len(temp)-1, 0, -1):
                if temp[j] == temp[j-1]:
                    temp[j] *= 2
                    temp[j-1] = 0
            temp = [x for x in temp if x != 0]

            for j in range(n):
                board[-1-j][i] = temp[-1-j] if j < len(temp)  else 0
    # 위쪽 이동
    elif direction == 3:
        for i in range(n):
            temp = [board[j][i] for j in range(n) if board[j][i] != 0]
            for j in range(len(temp)-1):
                if temp[j] == temp[j+1]:
                    temp[j] *= 2
                    temp[j+1] = 0
            temp = [x for x in temp if x != 0]

            for j in range(n):
                board[j][i] = temp[j] if j < len(temp) else 0
    return board

def simulation(board, cnt):

    if cnt == 5:
        return max(map(max, board))

    max_value = 0

    for directions in range(4):
        copy_board = copy.deepcopy(board)
        move_board = move(copy_board, directions)
        max_value = max(max_value, simulation(move_board, cnt + 1))

    return max_value

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

print(simulation(board, 0))


