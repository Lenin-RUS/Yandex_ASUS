v = [int(i) for i in input().split(' ')]
e = []
graph = dict()
for i in range(v[1]):
    e = [int(i) for i in input().split(' ')]
    if e[0] in graph:
        graph[e[0]][e[1] - 1] = 1
    else:
        graph[e[0]] = [0] * v[0]
        graph[e[0]][e[1] - 1] = 1

for i in range(1, v[0] + 1):
    if i in graph:
        print(*graph[i])
    else:
        print("0 " * v[0])
