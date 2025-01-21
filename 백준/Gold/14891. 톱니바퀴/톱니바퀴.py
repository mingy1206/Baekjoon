# 톱니바퀴가 돌아가는 함수 만들기
# 톱니바퀴가 돌아가기 전에 주변 톱니바퀴의 상태에 따라서, 각 톱니바퀴를 queue에 넣어 전체 톱니바퀴가 돌아가는 매커니즘을 구현
# 반복문으로 각 case 실행
import sys
from collections import deque
def rotation(num, direction):
    arr = []
    if direction < 0:
        cogwheel[num] = cogwheel[num][1:] + [cogwheel[num][0]]
    elif direction > 0:
        cogwheel[num] = [cogwheel[num][-1]] + cogwheel[num][:-1]

# side를 추가하지 않으면 side effect로 인해 주변 톱니바퀴에 영향을 줌
# a톱니바퀴로 인해서 돌아가는 b 톱니바퀴가 a톱니바퀴에게 영향을 줌
# a -> b 로 끝나야 하는데 a -> b -> a 순서로 다시 영향을 줌
def side_effect(num, direction, side):
    global queue
    # 얘를 함수로 만들기
    if num == 0:
        if cogwheel[num][right] != cogwheel[num+1][left] and side != num+1:
            queue.append([num+1, direction*-1, num])
    elif num == 1 or num == 2:
        if cogwheel[num][left] != cogwheel[num-1][right] and side != num-1:
            queue.append([num-1, direction*-1, num])
        if cogwheel[num][right] != cogwheel[num+1][left] and side != num+1:
            queue.append([num+1, direction*-1, num])
    elif num == 3:
        if cogwheel[num][left] != cogwheel[num-1][right] and side != num-1:
            queue.append([num-1, direction*-1, num])

cogwheel = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(4)]
K = int(sys.stdin.readline().rstrip())
case = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(K)]
queue = deque()

right = 2
left = 6
ans = 0



for a,b in case:
    queue.append([a-1, b, -1])
    while queue:
        num, direction, side = queue.popleft()
        side_effect(num, direction, side)
        rotation(num, direction)

cnt = 1
for i in range(4):
    ans += cogwheel[i][0] * cnt
    cnt *= 2


print(ans)