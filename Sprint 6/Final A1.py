def edge_add(key):
    index = len(edges)
    edges.append(key)
    sift_up(index)

def sift_up(index):
    if index == 1:
        return edges
    else:
        parent_index = index // 2
        if edges_arr[edges[parent_index]][2] < edges_arr[edges[index]][2]:
            edges[parent_index], edges[index] = edges[index], edges[parent_index]
            sift_up(parent_index)

def pop_max():
    result = edges[1]
    edges[1] = edges[-1]
    edges.pop()
    sift_down(1)
    return result

def sift_down(index):
    left = 2 * index
    right = 2 * index + 1
    if len(edges) <= left:
        return None
    if (right < len(edges)) and (edges_arr[edges[left]][2]  < edges_arr[edges[right]][2]):
        index_largest = right
    else:
        index_largest = left

    if edges_arr[edges[index]][2] < edges_arr[edges[index_largest]][2]:
        edges[index], edges[index_largest] = edges[index_largest], edges[index]
        sift_down(index_largest)

def add_vertex(v):
    added.add(v)
    not_added.discard(v)
    # edges.update(set(filter(lambda x: (edges_arr[x][0] == v and edges_arr[x][1] in not_added), edges_arr)))

    for i in nodes_arr[v]:
        if edges_arr[i][1] in not_added:
            edge_add(i)

def find_MST():
    v = 0
    final_sum = 0
    add_vertex(v)
    while not_added and edges:
        e = pop_max()
        if edges_arr[e][1] in not_added:
            max_spanning_tree.append(e)
            final_sum += edges_arr[e][2]
            add_vertex(edges_arr[e][1])

    if not_added:
        print('Oops! I did it again')
    else:
        print(final_sum)


# nod, edg = (int(i) for i in input().split(' '))
# e = []
# edges_arr = dict()
# nodes_arr = dict()
# for i in range(nod):
#     nodes_arr[i] = []
#
# count = 0
# for i in range(edg):
#     start, end, w = (int(i) - 1 for i in input().split(' '))
#     nodes_arr[start].append(count)
#     nodes_arr[end].append(count+edg)
#     edges_arr[count] = [start, end, w + 1]
#     edges_arr[count + edg] = [end, start, w + 1]
#     count += 1


nod, edg = 6, 9
edges_arr = {0: [0, 4, 6], 9: [4, 0, 6], 1: [0, 1, 2],
             10: [1, 0, 2], 2: [1, 5, 7], 11: [5, 1, 7],
             3: [5, 4, 8], 12: [4, 5, 8], 4: [4, 3, 4],
             13: [3, 4, 4], 5: [3, 5, 3], 14: [5, 3, 3],
             6: [5, 2, 1], 15: [2, 5, 1], 7: [2, 1, 5],
             16: [1, 2, 5], 8: [2, 3, 9], 17: [3, 2, 9]}

nodes_arr = {0: [0, 1], 1: [10, 2, 16], 2: [15, 7, 8], 3: [13, 5, 17], 4: [9, 12, 4], 5: [11, 3, 14, 6]}

max_spanning_tree = []  # Рёбра, составляющие MST.
added = set()  # Множество вершин, уже добавленных в остов.
not_added = set(range(nod))  # Множество вершины, ещё не добавленных в остов.
edges = [-1]  # Массив рёбер, исходящих из остовного дерева.

find_MST()
