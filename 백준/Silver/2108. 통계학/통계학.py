import sys
n = int(sys.stdin.readline())


lst = []
v = [0]*8001
total = 0

for _ in range(n):
    num = int(sys.stdin.readline())
    total += num    # 평균을 위한 값 합산
    v[num+4000] += 1
    lst.append(num)


# 최빈값들 추출 과정
max_num = max(v)
lst2 = []

for i in range(len(v)):
    if v[i] == max_num:
        lst2.append(i-4000)

# 중앙값 처리를 위한 정렬
lst.sort()

# 입력 수의 값이 1일 경우 예외처리
if n == 1:
    # 산술평균
    print(lst[0])
    # 중앙값
    print(lst[0])
    # 최빈값
    print(lst[0])
    # 범위
    print(0)
else:
    # 산술평균
    print(round(total / n))
    # 중앙값
    print(lst[int(len(lst)/2)])
    # 최빈값 (최빈값 예외처리)
    if len(lst2) >= 2:
        print(lst2[1])
    else:
        print(lst2[0])
    # 범위
    print(lst[-1]-lst[0])