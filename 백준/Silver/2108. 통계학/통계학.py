n = int(input())

lst = []
v = [0]*8001
total = 0
for _ in range(n):
    num = int(input())
    total += num
    v[num+4000] += 1
    lst.append(num)

max_num = max(v)
lst2 = []
for i in range(len(v)):
    if v[i] == max_num:
        lst2.append(i-4000)

lst.sort()

if n == 1:
    print(lst[0])
    print(lst[0])
    print(lst[0])
    print(0)
else:
    print(round(total / n))
    print(lst[int(len(lst)/2)])
    if len(lst2) >= 2:
        print(lst2[1])
    else:
        print(lst2[0])
    print(lst[-1]-lst[0])