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
#     nodes_arr[end].append(count+edg)
#     edges_arr[count] = [start, end, w+1]
#     edges_arr[count+edg] = [end, start, w+1]
#     count+=1

nod, edg = 6, 9
edges_arr = {0: [0, 4, 6], 9: [4, 0, 6], 1: [0, 1, 2],
             10: [1, 0, 2], 2: [1, 5, 7], 11: [5, 1, 7],
             3: [5, 4, 8], 12: [4, 5, 8], 4: [4, 3, 4],
             13: [3, 4, 4], 5: [3, 5, 3], 14: [5, 3, 3],
             6: [5, 2, 1], 15: [2, 5, 1], 7: [2, 1, 5],
             16: [1, 2, 5], 8: [2, 3, 9], 17: [3, 2, 9]}
nodes_arr = {0: [0, 1], 1: [10, 2, 16], 2: [15, 7, 8], 3: [13, 5, 17], 4: [9, 12, 4], 5: [11, 3, 14, 6]}

added = set()  # Множество вершин, уже добавленных в остов.
not_added = set(range(nod))  # Множество вершины, ещё не добавленных в остов.
edges = set()  # Массив рёбер, исходящих из остовного дерева.

