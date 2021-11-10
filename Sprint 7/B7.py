lessons = int(input())
time = []
for i in range(lessons):
    start, finish = (float(i) for i in input().split(' '))
    time.append([start, finish])
time.sort(key=lambda x: (x[1], x[0]))
answer = []
answer.append(time[0])

for i in time[1:]:
    if i[0] >= answer[-1][1]:
        answer.append(i)

print(len(answer))
for i in answer:
    print(*i)