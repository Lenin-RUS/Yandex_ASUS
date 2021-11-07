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




edges_arr = {0: [0, 4, 6], 9: [4, 0, 6], 1: [0, 1, 2],
             10: [1, 0, 2], 2: [1, 5, 7], 11: [5, 1, 7],
             3: [5, 4, 8], 12: [4, 5, 8], 4: [4, 3, 4],
             13: [3, 4, 4], 5: [3, 5, 3], 14: [5, 3, 3],
             6: [5, 2, 1], 15: [2, 5, 1], 7: [2, 1, 5],
             16: [1, 2, 5], 8: [2, 3, 9], 17: [3, 2, 9]}

edges=[-1]
for i in range(10):
    edge_add(i)
print(edges)

print(edges)
for i in edges[1:]:
    print(edges_arr[i][2], end=' ')
print()

print(edges_arr[pop_max()][2])
