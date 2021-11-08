nod, edg = 6, 9
edges_arr = {0: [0, 4, 6], 9: [4, 0, 6], 1: [0, 1, 2],
             10: [1, 0, 2], 2: [1, 5, 7], 11: [5, 1, 7],
             3: [5, 4, 8], 12: [4, 5, 8], 4: [4, 3, 4],
             13: [3, 4, 4], 5: [3, 5, 3], 14: [5, 3, 3],
             6: [5, 2, 1], 15: [2, 5, 1], 7: [2, 1, 5],
             16: [1, 2, 5], 8: [2, 3, 9], 17: [3, 2, 9]}

nodes_arr = {0: [0, 1], 1: [10, 2, 16], 2: [15, 7, 8], 3: [13, 5, 17], 4: [9, 12, 4], 5: [11, 3, 14, 6]}

edges=[0,1,2,3]

def heap_create_and_sort(heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and edges_arr[edges[left_child]][2] > edges_arr[edges[largest]][2]:
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

heapsort()
print(edges)
for i in edges:
    print(edges_arr[i][2], end=' ')