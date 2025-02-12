# 1과 2의 위치를 따로 저장
# 재귀문을 이용해서 치킨집 조합 케이스별 각 집에서 치킨거리 값의 최소를 구함
# 그때그때 도시의 치킨 거리를 구해서 가장 작은 값을 result에   저장
# 마지막에 result를 반환
# (각 치킨집에 대한 집들의 치킨거리 값 구하고 도시의 치킨 거리 구하고 저장)
# 정렬 해서 구하기

import sys

N,M = map(int, sys.stdin.readline().rstrip().split())
city = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
house_num = 0
chicken_num = 0
house = []
chicken = []
result = sys.maxsize

for y in range(N):
    for x in range(N):
        if city[y][x] == 1:
            house.append((x,y))
            house_num += 1
        elif city[y][x] == 2:
            chicken.append((x,y))
            chicken_num += 1

distance = [[0]*house_num for _ in range(M)]




def calculate(tlst):
    global result
    sum_temp = 0

    for hx,hy in house:
        temp = sys.maxsize
        for cx,cy in tlst:
            temp = min(temp, abs(cx-hx)+abs(cy-hy))
        sum_temp += temp
    return sum_temp

def search(tlst, cnt):
    global result
    if cnt == chicken_num:
        if len(tlst) == M:
            result = min(result, calculate(tlst))
        return
    search(tlst+[chicken[cnt]], cnt+1)
    search(tlst, cnt+1)
search([],0)
print(result)