arr = [i for i in input().split(' ')]
# arr=['one', 'two', 'three']
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=' ')
