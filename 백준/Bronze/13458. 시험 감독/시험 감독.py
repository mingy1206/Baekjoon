testing_room_num = int(input())
testing_room = list(map(int, input().split()))
b, c = map(int, input().split())

total = 0
for students in testing_room:
    students -= b
    total += 1
    if students <= 0:
        continue
    if students%c > 0:
        total += int(students/c) + 1
    else:
        total += int(students/c)

print(total)
