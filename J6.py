import sys
sys.setrecursionlimit(200000)

class Stack():
    def __init__(self):
        self.values = []
        self.colors = 0
        self.final=dict()

    def pop(self):
        return self.values.pop()

    def push(self, value):
        self.values.append(value)

    def is_empty(self):
        return len(self.values)


v = [int(i) for i in input().split(' ')]
color = [-1] * (v[0] + 1)

graph = dict()
for i in range(v[1]):
    e = [int(i) for i in input().split(' ')]
    if e[0] in graph:
        graph[e[0]].append(e[1])
    else:
        graph[e[0]] = [e[1]]

    if e[1] in graph:
        graph[e[1]].append(e[0])
    else:
        graph[e[1]] = [e[0]]


def TopSort(v):
    color[v] = 0
    if v in graph:
        for w in graph[v]:
            if color[w] == -1:
                TopSort(w)
    color[v] = order.colors
    if order.colors not in order.final:
        order.final[order.colors]=[v]
    else:
        order.final[order.colors].append(v)
    order.push(v)  # Кладём обработанную вершину в стек.


def MainTopSort():
    for i in range(1, v[0]+1):
        if color[i] == -1:
            order.colors +=1
            TopSort(i)

order = Stack()  # В этом стеке будет записан порядок обхода.
MainTopSort()
print(order.colors)
for i in order.final:
    order.final[i].sort()
    print(*order.final[i])
