
nod, edg = 6, 9
edges_arr = {0: [0, 1, 2], 9: [1, 0, 2], 1: [0, 4, 6],
             10: [4, 0, 6], 2: [1, 5, 7], 11: [5, 1, 7],
             3: [5, 4, 8], 12: [4, 5, 8], 4: [5, 2, 1],
             13: [2, 5, 1], 5: [5, 3, 3], 14: [3, 5, 3],
             6: [4, 3, 4], 15: [3, 4, 4], 7: [3, 2, 9], 16: [2, 3, 9],
             8: [1, 2, 5], 17: [2, 1, 5]}

nodes_arr = {0: [0, 1], 1: [0, 2, 7], 2: [6, 7, 8], 3: [4, 5, 8], 4: [1, 3, 4], 5: [2, 3, 5, 6]}

minimum_spanning_tree = []  # Рёбра, составляющие MST.
added = set()  # Множество вершин, уже добавленных в остов.
not_added = set(range(nod))  # Множество вершины, ещё не добавленных в остов.
edges = set()  # Массив рёбер, исходящих из остовного дерева.


def add_vertex(v):
    added.add(v)
    not_added.discard(v)
    edges_tmp=list(filter(lambda x:
                          (edges_arr[x][0] == v and edges_arr[x][1] in not_added) or
                          (edges_arr[x][1] == v and edges_arr[x][0] in not_added), edges_arr))
    for i in edges_tmp:
        edges.add(i)


def extract_minimum():
    current_minimum = float('inf')
    current_minimum_edge = None
    for v in edges:
        if edges_arr[v][2] < current_minimum:
            current_minimum = edges_arr[v][2]
            current_minimum_edge = v
    edges.discard(current_minimum_edge)
    return current_minimum_edge


def find_MST():
    v = 0
    add_vertex(v)
    while not_added and edges:
        # Подразумеваем, что extract_minimum извлекает минимальное ребро
        # из массива рёбер и больше данного ребра в массива не будет.
        e = extract_minimum()

        if edges_arr[e][1] in not_added:
            minimum_spanning_tree.append(e)
            add_vertex(edges_arr[e][1])

    if not_added:
        print('Oops! I did it again')
    else:
        print(minimum_spanning_tree)


# nod, edg = (int(i) for i in input().split(' '))
# e = []
#
# edges_arr = dict()
# nodes_arr = dict()

# for i in range(nod):
#     nodes_arr[i]=[]
#
# count = 0
# for i in range(edg):
#     start, end, w = (int(i)-1 for i in input().split(' '))
#     nodes_arr[start].append(count)
#     nodes_arr[end].append(count)
#     edges_arr[count] = [start, end, w+1]
#     edges_arr[count+edg] = [end, start, w+1]
#     count+=1

find_MST()
add_vertex(5)
print(edges)



