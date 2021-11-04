def q_is_empty():
    return len(list(filter(lambda x: x == True, visited))) == len(list(filter(lambda x: x < float('inf'), dist)))

def relax(u, v, w):
    # Проверяем, не получился ли путь короче найденного ранее.
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        previous[v] = u


def get_min_dist_not_visited_vertex():
    current_minimum = float('inf')
    current_minimum_vertex = None

    for v in graph:
        if (visited[v]==False) and (dist[v] < current_minimum):
            current_minimum = dist[v]
            current_minimum_vertex = v
    return current_minimum_vertex


def Dijkstra(s):
    dist[s] = 0 # Расстояние от вершины до самой себя 0
    # visited[s] = True
    while not q_is_empty():
        u = get_min_dist_not_visited_vertex()
        visited[u] = True
        for i in graph[u]:
            relax(u, i[0], i[1])


v = [int(i) for i in input().split(' ')]
e = []
graph = dict()

for i in range(v[0]):
    graph[i]=[]
for i in range(v[1]):
    e = [int(i)-1 for i in input().split(' ')]
    graph[e[0]].append([e[1], e[2]+1])
    graph[e[1]].append([e[0], e[2]+1])



# graph = {0: [[1, 1], [3, 2]], 1: [[0, 1], [2, 3]], 2: [[1, 3], [3, 5]], 3: [[2, 5], [0, 2]], 4: []}
# v=[5,4]

for i in range(v[0]):
    dist = [float('inf')] * v[0]     # Задаём расстояние по умолчанию.
    previous = [None] * v[0]     # Задаём предшественника для восстановления SPT.
    visited = [False] * v[0]
    all_not_visited = v[0]
    Dijkstra(i)
    for i in dist:
        if i==float('inf'):
            print(-1, end=' ')
        else:
            print(i, end=' ')
    print()