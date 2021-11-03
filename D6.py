class Stack():
    def __init__(self):
        self.values = []
        self.colors = dict()

    def pop(self):
        return self.values.pop()

    def push(self, value):
        self.values.append(value)

    def is_empty(self):
        return len(self.values)

v = [int(i) for i in input().split(' ')]
e = []
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
start_vertex = int(input())


# Длины массивов равны числу вершин|V|.
color = [white, white, ...]
previous = [None, None, ...]
distance = [None, None, ...]

функция BFS(s):
    # Создадим очередь вершин и положим туда стартовую вершину.
    planned = Queue()
    planned.push(s)
    color[s] = gray
    distance[s] = 0
    пока очередь planned не пуста:
        u = planned.pop() # Возьмём вершину из очереди.
        для каждого ребра (u,v), исходящего из u:
            возьмём вершину v
            if color[v] == white: # Серые и чёрные вершины уже
                                  # либо в очереди, либо обработаны.
                distance[v] = distance[u] + 1
                previous[v] = u
                color[v] = gray
                planned.push(v) # Запланируем посещение вершины.
        color[u] = black # Теперь вершина считается обработанной.

функция ShortestPath(v): # Кратчайший путь от s до v.
    # Класть вершины будем в стек, тогда
    # стартовая вершина окажется наверху стека
    # и порядок следования от s до v будет соответствовать
    # порядку извлечения вершин из стека.
    path = Stack()
    current_vertex = v
    while current_vertex != None: # Предшественник вершины s равен None.
        path.push(current_vertex)
        current_vertex = previous[current_vertex]
    return path