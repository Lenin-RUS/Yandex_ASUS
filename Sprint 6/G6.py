class Queue:
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, x):
        self.queue.append(x)
        self.tail += 1
        self.size += 1

    def pop(self):
        x = self.queue[self.head]
        self.head += 1
        self.size -= 1
        return x

def BFS(s):
    planned = Queue()
    planned.push(s)
    color[s] = 'gray'
    distance[s] = 0
    md=0
    while planned.size >0:
        u = planned.pop()  # Возьмём вершину из очереди.
        # if u in graph:
        for v in graph[u]:
            if color[v] == 'white':  # Серые и чёрные вершины уже
                distance[v] = distance[u] + 1
                if md<distance[u] + 1: md = distance[u] + 1
                color[v] = 'gray'
                planned.push(v)  # Запланируем посещение вершины.
        color[u] = 'black'  # Теперь вершина считается обработанной.
    print(md)


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

color = ['white'] * (v[0] + 1)
distance = [None] * (v[0] + 1)
distance[0]=0

if v[1] == 0:
    print(0)
else:
    BFS(start_vertex)
