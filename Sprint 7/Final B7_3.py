_ = input()
arr = [int(i) for i in input().split(' ')]
# arr = [1, 3, 1, 2, 2, 1]
k = sum(arr)
if k % 2 == 1:
    print("False")
else:
    k = int(k / 2)
    # result = [[1 for _ in range(len(arr) + 1)] for _ in range(k + 1)]
    A = [1 for _ in range(k + 1)]
    B = [0 for _ in range(k + 1)]
    B[0] = 1
    for i in range(1, k + 1):
        for j in range(1, len(arr) + 1):
            if j % 2 == 1:
                if i - arr[j - 1] >= 0:
                    A[i] = (B[i] or B[i - arr[j - 1]])
                else:
                    A[i] = B[i]
            else:
                if i - arr[j - 1] >= 0:
                    B[i] = (A[i] or A[i - arr[j - 1]])
                else:
                    B[i] = A[i]
    print((A[-1] or B[-1]) == 1)
