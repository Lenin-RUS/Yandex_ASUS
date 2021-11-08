import sys


# sys.setrecursionlimit(2000)

def heap_create_and_sort(heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and edges_arr[edges[left_child]][2] < edges_arr[edges[largest]][2]:
        largest = left_child

    if right_child < heap_size and edges_arr[edges[right_child]][2] < edges_arr[edges[largest]][2]:
        largest = right_child

    if largest != root_index:
        edges[root_index], edges[largest] = edges[largest], edges[root_index]
        heap_create_and_sort(heap_size, largest)


def heapsort():
    n = len(edges)
    for i in range(n, -1, -1):  # Тут мы создаем бинарную кучу
        heap_create_and_sort(n, i)
    for i in range(n - 1, -1, -1):
        edges[i], edges[0] = edges[0], edges[i]
        heap_create_and_sort(i, 0)


def add_vertex(v):
    added.add(v)
    not_added.discard(v)
    for i in nodes_arr[v]:
        if edges_arr[i][1] in not_added:
            edges.append(i)


def find_MST():
    v = 0
    final_sum = 0
    add_vertex(v)
    while not_added and edges:
        heapsort()
        e = edges[0]
        edges[0] = edges.pop()

        if edges_arr[e][1] in not_added:
            # max_spanning_tree.append(e)
            final_sum += edges_arr[e][2]
            add_vertex(edges_arr[e][1])

    if not_added:
        print('Oops! I did it again')
    else:
        print(final_sum)


nod, edg = (int(i) for i in input().split(' '))
e = []
edges_arr = dict()
nodes_arr = dict()
for i in range(nod):
    nodes_arr[i] = []

count = 0
for i in range(edg):
    start, end, w = (int(i) - 1 for i in input().split(' '))
    nodes_arr[start].append(count)
    nodes_arr[end].append(count + edg)
    edges_arr[count] = [start, end, w + 1]
    edges_arr[count + edg] = [end, start, w + 1]
    count += 1

# nod, edg = 6, 9
# edges_arr = {0: [0, 4, 6], 9: [4, 0, 6], 1: [0, 1, 2],
#              10: [1, 0, 2], 2: [1, 5, 7], 11: [5, 1, 7],
#              3: [5, 4, 8], 12: [4, 5, 8], 4: [4, 3, 4],
#              13: [3, 4, 4], 5: [3, 5, 3], 14: [5, 3, 3],
#              6: [5, 2, 1], 15: [2, 5, 1], 7: [2, 1, 5],
#              16: [1, 2, 5], 8: [2, 3, 9], 17: [3, 2, 9]}
#
# nodes_arr = {0: [0, 1], 1: [10, 2, 16], 2: [15, 7, 8], 3: [13, 5, 17], 4: [9, 12, 4], 5: [11, 3, 14, 6]}

# max_spanning_tree = []  # Рёбра, составляющие MST.
added = set()  # Множество вершин, уже добавленных в остов.
not_added = set(range(nod))  # Множество вершины, ещё не добавленных в остов.
edges = []  # Массив рёбер, исходящих из остовного дерева.

if edg == 0 and nod != 1:
    print('Oops! I did it again')
else:
    find_MST()
