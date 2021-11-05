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

v = [int(i) for i in input().split(' ')]
e = []
graph = dict()

for i in range(v[0]):
    graph[i]=[]
for i in range(v[1]):
    e = [int(i)-1 for i in input().split(' ')]
    graph[e[0]].append(e[1])
    graph[e[1]].append(e[0])
    
start, end = (int(i)-1 for i in input().split(' '))

color = ['white'] * (v[0])
previous = [None] * (v[0])
distance = [None] * (v[0])

if start == end:
    print(0)
else:
    final_dist = BFS(start)
    my_path = ShortestPath(end)

    if len(my_path.values)==1:
        print(-1)
    else:
        print(len(my_path.values)-1)
