# _ = input()
# arr = [int(i) for i in input().split(' ')]
arr = [3, 1, 1, 2, 2, 1]
k = sum(arr)
if k % 2 == 1:
    print("False")
else:
    k = int(k / 2)
    result = [[1 for _ in range(len(arr) + 1)] for _ in range(k + 1)]
    for i in range(1, k + 1):
        result[i][0] = 0
        for j in range(1, len(arr) + 1):

            if i - arr[j - 1] >= 0:
                result[i][j] = (result[i][j - 1] or result[i - arr[j - 1]][j - 1])
            else:
                result[i][j] = result[i][j - 1]
    # for i in result:
    #     print(*i)
    print(result[-1][-1] == 1)
