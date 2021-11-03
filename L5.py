a = [-1]
def sift_down(heap, index):
    left = 2 * index
    right = 2 * index + 1
    a[0] = index
    if len(heap) <= left:
        return a[0]
    if (right < len(heap)) and (heap[left] < heap[right]):
        index_largest = right
    else:
        index_largest = left

    if heap[index] < heap[index_largest]:
        heap[index], heap[index_largest] = heap[index_largest], heap[index]
        sift_down(heap, index_largest)

    return a[0]

sample = [-1, 90, 70, 50]
sample[1]-=1
print(sift_down(sample, 1))
sample[3]-=1
print(sift_down(sample, 3))
sample[2]-=1
print(sift_down(sample, 2))
sample[1]-=25
print(sift_down(sample, 1))

# 3
# 90 70 50
# 6
# 1 1
# 3 1
# 2 1
# 1 25
# 1 40
# 1 60