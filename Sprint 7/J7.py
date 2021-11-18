n = int(input())
A = [int(i) for i in input().split(' ')]
# n = 5
# A = [4, 2, 9, 1, 13]
prev = [0 for i in range(n)]
d = [0 for i in range(n)]

for i in range(n):
    d[i] = 1
    prev[i] = -1
    for j in range(i):
        if (A[j] < A[i] and d[j] + 1 > d[i]):
            d[i] = d[j] + 1
            prev[i] = j
pos = 0
lenght = d[0]
for i in range(n):
    if d[i] > lenght:
        pos = i
        lenght = d[i]
answer = []
while pos != -1:
    answer.append(pos+1)
    pos = prev[pos]

answer.reverse()
print(lenght)
print(*answer)
