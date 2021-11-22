_ = input()
arr = [int(i) for i in input().split(' ')]
# arr = [1,5,7,1]
k = sum(arr)
result = 0

if k % 2 == 1:
    print("False")
else:
    arr.sort(reverse=True)
    k = int(k / 2)
    A = [0 for _ in range(k + 1)]
    B = [0 for _ in range(k + 1)]

    for i in range(1, len(arr) + 1):
        if A[-1] == k or B[-1] == k:
            print('True')
            result = 1
            break

        for j in range(arr[i - 1], k + 1):
            if i % 2 == 0:
                A[j] = max(B[j], B[j - arr[i - 1]] + arr[i - 1])
            else:
                B[j] = max(A[j], A[j - arr[i - 1]] + arr[i - 1])
    if result == 0:
        if k % 2 == 0:
            print(A[-1] == 1)
        else:
            print(B[-1] == 1)
