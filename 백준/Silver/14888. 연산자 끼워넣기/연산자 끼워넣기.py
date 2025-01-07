from itertools import permutations
import sys

def opr(operator, a, cnt):
    global max_num, min_num
    if cnt == N - 1:
        if a > max_num:
            max_num = a
        if a < min_num:
            min_num = a
        return
    b = A[cnt + 1]
    if operator[cnt] == 0:
        opr(operator, a + b, cnt + 1)
    elif operator[cnt] == 1:
        opr(operator, a - b, cnt + 1)
    elif operator[cnt] == 2:
        opr(operator, a * b, cnt + 1)
    elif operator[cnt] == 3:
        if a < 0:
            a = abs(a)
            opr(operator, int(a/b) * -1, cnt + 1)
        else:
            opr(operator, int(a/b), cnt + 1)

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
p, mi, mu, di = map(int, sys.stdin.readline().strip().split())

plus = [0] * p
minus = [1] * mi
mul = [2] * mu
div = [3] * di

operators = list(set(permutations(plus + minus + mul + div, N - 1)))
max_num = -1000000000
min_num = 1000000000

for operator in operators:
    opr(operator, A[0], 0)
    
print(max_num, min_num)