

def add_vertex(v):
    added.add(v)
    not_added.discard(v)
    edges += graph.edges.filter(start == v, end in not_added)

def extract_minimum():
    current_minimum = float('inf')
    current_minimum_vertex = None

    for v in graph:
        if (visited[v]==False) and (dist[v] < current_minimum):
            current_minimum = dist[v]
            current_minimum_vertex = v
    return current_minimum_vertex


def find_MST():
    v = 0
    add_vertex(v)
    while not not_added and not edges:
        # Подразумеваем, что extract_minimum извлекает минимальное ребро
        # из массива рёбер и больше данного ребра в массива не будет.
        e = extract_minimum(edges)
        если
        e.end in not_added, то:
        minimum_spanning_tree += e
        add_vertex(e.end)

    если     not_added     не     пуст, то
        верни     ошибку
    "Исходный граф несвязный"
    иначе     верни
        minimum_spanning_tree

v=[6, 9]
graph={0: [[4, 6], [1, 2]],
       1: [[0, 2], [5, 7], [2, 5]],
       2: [[5, 1], [1, 5], [3, 9]],
       3: [[4, 4], [5, 3], [2, 9]],
       4: [[0, 6], [5, 8], [3, 4]],
       5: [[1, 7], [4, 8], [3, 3], [2, 1]]}

minimum_spanning_tree = []  # Рёбра, составляющие MST.
added = set()  # Множество вершин, уже добавленных в остов.
not_added = set(range(v[0]))  # Множество вершины, ещё не добавленных в остов.
edges = []  # Массив рёбер, исходящих из остовного дерева.