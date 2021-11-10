empty = int(input())
heap = int(input())
heaps = []
for i in range(heap):
    price, w = (int(i) for i in input().split(' '))
    heaps.append([price, w])
heaps.sort(reverse=True)
answer = 0
i = 0
while empty > 0 and i < heap:
    w = min(empty, heaps[i][1])
    empty -= w
    answer += heaps[i][0] * w
    i += 1

print(answer)