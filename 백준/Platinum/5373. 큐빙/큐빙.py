# 3차원 배열 만들기
# 큐브 돌리기 모듈화
# 윗면 출력
import sys
def cubing(position, direction):
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    if position == 'U':
        if direction == '+':
            temp1 = cube[1][0]
            temp2 = cube[5][0]
            temp3 = [cube[3][2][2], cube[3][2][1], cube[3][2][0]]
            temp4 = cube[4][0]

            cube[4][0] = temp1
            cube[1][0] = temp2
            cube[5][0] = temp3
            cube[3][2][2] = temp4[0]
            cube[3][2][1] = temp4[1]
            cube[3][2][0] = temp4[2]

            # 바라보는 면 회전
            temp1 = [cube[0][2][0], cube[0][1][0], cube[0][0][0]]
            temp2 = [cube[0][2][1], cube[0][1][1], cube[0][0][1]]
            temp3 = [cube[0][2][2], cube[0][1][2], cube[0][0][2]]
            cube[0][0] = temp1
            cube[0][1] = temp2
            cube[0][2] = temp3
        elif direction == '-':
            temp1 = cube[1][0]
            temp2 = cube[5][0]
            temp3 = [cube[3][2][2], cube[3][2][1], cube[3][2][0]]
            temp4 = cube[4][0]

            cube[5][0] = temp1
            cube[3][2][2] = temp2[0]
            cube[3][2][1] = temp2[1]
            cube[3][2][0] = temp2[2]
            cube[4][0] = temp3
            cube[1][0] = temp4

            # 바라보는 면 회전
            temp1 = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
            temp2 = [cube[0][0][1], cube[0][1][1], cube[0][2][1]]
            temp3 = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
            cube[0][0] = temp3
            cube[0][1] = temp2
            cube[0][2] = temp1
    elif position == 'D':
        if direction == '+':
            temp1 = cube[1][2]
            temp2 = cube[5][2]
            temp3 = [cube[3][0][2], cube[3][0][1], cube[3][0][0]]
            temp4 = cube[4][2]

            cube[5][2] = temp1
            cube[3][0][2] = temp2[0]
            cube[3][0][1] = temp2[1]
            cube[3][0][0] = temp2[2]
            cube[4][2] = temp3
            cube[1][2] = temp4

            # 바라보는 면 회전
            temp1 = [cube[2][2][0], cube[2][1][0], cube[2][0][0]]
            temp2 = [cube[2][2][1], cube[2][1][1], cube[2][0][1]]
            temp3 = [cube[2][2][2], cube[2][1][2], cube[2][0][2]]
            cube[2][0] = temp1
            cube[2][1] = temp2
            cube[2][2] = temp3
        elif direction == '-':
            temp1 = cube[1][2]
            temp2 = cube[5][2]
            temp3 = [cube[3][0][2], cube[3][0][1], cube[3][0][0]]
            temp4 = cube[4][2]

            cube[4][2] = temp1
            cube[1][2] = temp2
            cube[5][2] = temp3
            cube[3][0][2] = temp4[0]
            cube[3][0][1] = temp4[1]
            cube[3][0][0] = temp4[2]

            # 바라보는 면 회전
            temp1 = [cube[2][0][0], cube[2][1][0], cube[2][2][0]]
            temp2 = [cube[2][0][1], cube[2][1][1], cube[2][2][1]]
            temp3 = [cube[2][0][2], cube[2][1][2], cube[2][2][2]]
            cube[2][0] = temp3
            cube[2][1] = temp2
            cube[2][2] = temp1
    elif position == 'F':
        if direction == '+':
            temp1 = cube[0][2]
            temp2 = [cube[4][2][2], cube[4][1][2], cube[4][0][2]]
            temp3 = cube[2][0]
            temp4 = [cube[5][2][0], cube[5][1][0], cube[5][0][0]]

            cube[0][2] = temp2
            cube[2][0] = temp4
            cube[4][0][2] = temp3[0]
            cube[4][1][2] = temp3[1]
            cube[4][2][2] = temp3[2]
            cube[5][0][0] = temp1[0]
            cube[5][1][0] = temp1[1]
            cube[5][2][0] = temp1[2]

            # 바라보는 면 회전
            temp1 = [cube[1][2][0], cube[1][1][0], cube[1][0][0]]
            temp2 = [cube[1][2][1], cube[1][1][1], cube[1][0][1]]
            temp3 = [cube[1][2][2], cube[1][1][2], cube[1][0][2]]
            cube[1][0] = temp1
            cube[1][1] = temp2
            cube[1][2] = temp3
        elif direction == '-':
            temp1 = cube[0][2]
            temp2 = [cube[4][0][2], cube[4][1][2], cube[4][2][2]]
            temp3 = cube[2][0]
            temp4 = [cube[5][0][0], cube[5][1][0], cube[5][2][0]]

            cube[0][2] = temp4
            cube[2][0] = temp2
            cube[4][2][2] = temp1[0]
            cube[4][1][2] = temp1[1]
            cube[4][0][2] = temp1[2]
            cube[5][2][0] = temp3[0]
            cube[5][1][0] = temp3[1]
            cube[5][0][0] = temp3[2]

            # 바라보는 면 회전
            temp1 = [cube[1][0][0], cube[1][1][0], cube[1][2][0]]
            temp2 = [cube[1][0][1], cube[1][1][1], cube[1][2][1]]
            temp3 = [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
            cube[1][0] = temp3
            cube[1][1] = temp2
            cube[1][2] = temp1
    elif position == 'B':
        if direction == '+':
            temp1 = cube[0][0]
            temp2 = [cube[4][0][0], cube[4][1][0], cube[4][2][0]]
            temp3 = cube[2][2]
            temp4 = [cube[5][0][2], cube[5][1][2], cube[5][2][2]]

            cube[0][0] = temp4
            cube[2][2] = temp2
            cube[4][2][0] = temp1[0]
            cube[4][1][0] = temp1[1]
            cube[4][0][0] = temp1[2]
            cube[5][2][2] = temp3[0]
            cube[5][1][2] = temp3[1]
            cube[5][0][2] = temp3[2]

            # 바라보는 면 회전
            temp1 = [cube[3][2][2], cube[3][1][2], cube[3][0][2]]
            temp2 = [cube[3][2][1], cube[3][1][1], cube[3][0][1]]
            temp3 = [cube[3][2][0], cube[3][1][0], cube[3][0][0]]
            cube[3][2] = temp1
            cube[3][1] = temp2
            cube[3][0] = temp3
        elif direction == '-':
            temp1 = cube[0][0]
            temp2 = [cube[4][2][0], cube[4][1][0], cube[4][0][0]]
            temp3 = cube[2][2]
            temp4 = [cube[5][2][2], cube[5][1][2], cube[5][0][2]]

            cube[0][0] = temp2
            cube[2][2] = temp4
            cube[4][0][0] = temp3[0]
            cube[4][1][0] = temp3[1]
            cube[4][2][0] = temp3[2]
            cube[5][0][2] = temp1[0]
            cube[5][1][2] = temp1[1]
            cube[5][2][2] = temp1[2]

            # 바라보는 면 회전
            temp1 = [cube[3][0][0], cube[3][1][0], cube[3][2][0]]
            temp2 = [cube[3][0][1], cube[3][1][1], cube[3][2][1]]
            temp3 = [cube[3][0][2], cube[3][1][2], cube[3][2][2]]
            cube[3][0] = temp3
            cube[3][1] = temp2
            cube[3][2] = temp1
    elif position == 'L':
        temp1 = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
        temp2 = [cube[1][0][0], cube[1][1][0], cube[1][2][0]]
        temp3 = [cube[2][0][0], cube[2][1][0], cube[2][2][0]]
        temp4 = [cube[3][0][0], cube[3][1][0], cube[3][2][0]]
        if direction == '+':
            cube[0][0][0] = temp4[0]
            cube[0][1][0] = temp4[1]
            cube[0][2][0] = temp4[2]
            cube[1][0][0] = temp1[0]
            cube[1][1][0] = temp1[1]
            cube[1][2][0] = temp1[2]
            cube[2][0][0] = temp2[0]
            cube[2][1][0] = temp2[1]
            cube[2][2][0] = temp2[2]
            cube[3][0][0] = temp3[0]
            cube[3][1][0] = temp3[1]
            cube[3][2][0] = temp3[2]

            # 바라보는 면 회전
            temp1 = [cube[4][2][0], cube[4][1][0], cube[4][0][0]]
            temp2 = [cube[4][2][1], cube[4][1][1], cube[4][0][1]]
            temp3 = [cube[4][2][2], cube[4][1][2], cube[4][0][2]]
            cube[4][0] = temp1
            cube[4][1] = temp2
            cube[4][2] = temp3
        elif direction == '-':
            cube[0][0][0] = temp2[0]
            cube[0][1][0] = temp2[1]
            cube[0][2][0] = temp2[2]
            cube[1][0][0] = temp3[0]
            cube[1][1][0] = temp3[1]
            cube[1][2][0] = temp3[2]
            cube[2][0][0] = temp4[0]
            cube[2][1][0] = temp4[1]
            cube[2][2][0] = temp4[2]
            cube[3][0][0] = temp1[0]
            cube[3][1][0] = temp1[1]
            cube[3][2][0] = temp1[2]

            # 바라보는 면 회전
            temp1 = [cube[4][0][0], cube[4][1][0], cube[4][2][0]]
            temp2 = [cube[4][0][1], cube[4][1][1], cube[4][2][1]]
            temp3 = [cube[4][0][2], cube[4][1][2], cube[4][2][2]]
            cube[4][0] = temp3
            cube[4][1] = temp2
            cube[4][2] = temp1
    elif position == 'R':
        temp1 = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
        temp2 = [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
        temp3 = [cube[2][0][2], cube[2][1][2], cube[2][2][2]]
        temp4 = [cube[3][0][2], cube[3][1][2], cube[3][2][2]]
        if direction == '+':
            cube[0][0][2] = temp2[0]
            cube[0][1][2] = temp2[1]
            cube[0][2][2] = temp2[2]
            cube[1][0][2] = temp3[0]
            cube[1][1][2] = temp3[1]
            cube[1][2][2] = temp3[2]
            cube[2][0][2] = temp4[0]
            cube[2][1][2] = temp4[1]
            cube[2][2][2] = temp4[2]
            cube[3][0][2] = temp1[0]
            cube[3][1][2] = temp1[1]
            cube[3][2][2] = temp1[2]

            # 바라보는 면 회전
            temp1 = [cube[5][2][0], cube[5][1][0], cube[5][0][0]]
            temp2 = [cube[5][2][1], cube[5][1][1], cube[5][0][1]]
            temp3 = [cube[5][2][2], cube[5][1][2], cube[5][0][2]]
            cube[5][0] = temp1
            cube[5][1] = temp2
            cube[5][2] = temp3
        elif direction == '-':
            cube[0][0][2] = temp4[0]
            cube[0][1][2] = temp4[1]
            cube[0][2][2] = temp4[2]
            cube[1][0][2] = temp1[0]
            cube[1][1][2] = temp1[1]
            cube[1][2][2] = temp1[2]
            cube[2][0][2] = temp2[0]
            cube[2][1][2] = temp2[1]
            cube[2][2][2] = temp2[2]
            cube[3][0][2] = temp3[0]
            cube[3][1][2] = temp3[1]
            cube[3][2][2] = temp3[2]

            # 바라보는 면 회전
            temp1 = [cube[5][0][0], cube[5][1][0], cube[5][2][0]]
            temp2 = [cube[5][0][1], cube[5][1][1], cube[5][2][1]]
            temp3 = [cube[5][0][2], cube[5][1][2], cube[5][2][2]]
            cube[5][0] = temp3
            cube[5][1] = temp2
            cube[5][2] = temp1

tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    cube = [[['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']], # 흰색
             [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],# 빨강색
             [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],# 노란색
             [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],# 오렌지색
             [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],# 초록색
             [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]]# 파란색

    n = int(sys.stdin.readline().rstrip())
    case = list(map(str, sys.stdin.readline().rstrip().split()))

    for i in range(n):
        cubing(case[i][0], case[i][1])

    for i in range(3):
        for j in range(3):
            print(cube[0][i][j],end='')
        print()
