import sys
from itertools import combinations

N = int(sys.stdin.readline().strip())
S = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

score = float("inf")

for team in combinations(range(N), int(N / 2)):
    # 스타트 팀과 링크 팀 구분
    start_team = list(team)
    link_team = [i for i in range(N) if i not in start_team]

    start_score = 0
    for i, j in combinations(start_team, 2):
        start_score += S[i][j] + S[j][i]

    link_score = 0
    for i, j in combinations(link_team, 2):
        link_score += S[i][j] + S[j][i]

    if abs(start_score - link_score) < score:
        score = abs(start_score - link_score)

print(score)