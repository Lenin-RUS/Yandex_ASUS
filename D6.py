class Stack:
    def __init__(self):
        self.values = []
        self.colors = dict()

    def pop(self):
        return self.values.pop()

    def push(self, value):
        self.values.append(value)

    def is_empty(self):
        return len(self.values)


class Queue:
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        self.queue.append(x)
        self.tail += 1
        self.size += 1

    def pop(self):
        x = self.queue[self.head]
        # self.queue[self.head] = None
        self.head += 1
        self.size -= 1
        return x


def BFS(s):
    planned = Queue()
    planned.push(s)
    color[s] = 'gray'
    distance[s]=0
    while not planned.is_empty():
        u = planned.pop()  # Возьмём вершину из очереди.
        if u in graph:
            for v in graph[u]:
                if color[v] == 'white':  # Серые и чёрные вершины уже
                    distance[v] = distance[u] + 1
                    previous[v] = u
                    color[v] = 'gray'
                    planned.push(v)  # Запланируем посещение вершины.
            color[u] = 'black'  # Теперь вершина считается обработанной.
    return planned.queue


def ShortestPath(v):  # Кратчайший путь от s до v.
    path = Stack()
    current_vertex = v
    while current_vertex != None:  # Предшественник вершины s равен None.
        path.push(current_vertex)
        current_vertex = previous[current_vertex]
    return path

graph = dict()

v = [int(i) for i in input().split(' ')]
e = []

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
start_vertex = int(input())

# v=[6,6]
# graph = {4: [2, 1], 2: [4, 3, 6], 1: [4, 5], 5: [1, 6], 3: [2], 6: [5, 2]}
# start_vertex = 6

for i in graph:
    graph[i].sort()

color = ['white'] * (v[0]+1)
previous = [None] * (v[0]+1)
distance = [None] * (v[0]+1)


final_dist = BFS(start_vertex)
print(*final_dist)

