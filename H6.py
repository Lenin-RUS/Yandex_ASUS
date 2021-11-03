import sys
sys.setrecursionlimit(200000)


class Stack():
    def __init__(self):
        self.values = []
        self.time = -1

    def pop(self):
        return self.values.pop()

    def push(self, value):
        self.values.append(value)

    def is_empty(self):
        return len(self.values)


def DFS(v):
    stack.push(v)
    stack.time += 1  # При входе в вершину время (номер шага) увеличивается.
    entry[v] = stack.time  # Запишем время входа.
    color[v] = 'gray'
    if v in graph:
        for w in graph[v]:
            if color[w] == 'white':
                DFS(w)
    stack.time += 1
    exit[v] = stack.time
    color[v] = 'black'


stack = Stack()

v = [int(i) for i in input().split(' ')]
color = ['white'] * (v[0] + 1)
entry = [None] * (v[0] + 1)
exit = [None] * (v[0] + 1)

graph = dict()
for i in range(v[1]):
    e = [int(i) for i in input().split(' ')]
    if e[0] in graph:
        graph[e[0]].append(e[1])
    else:
        graph[e[0]] = [e[1]]

start_vertex = 1

for i in graph:
    graph[i].sort()

DFS(start_vertex)

for i in range(v[0]):
    print(entry[i + 1], exit[i + 1])
