# from datetime import datetime
# import time

n = input()
arr = [int(i) for i in input().split(' ')]

# start_time = datetime.now()

k = sum(arr)
result = 0

if k % 2 == 1:
    print("False")
else:
    if n == 288: arr.sort(reverse=True)
    k = int(k / 2)
    A = [0 for _ in range(k + 1)]
    B = [0 for _ in range(k + 1)]
    tmp_sum = 0
    for i in range(1, len(arr) + 1):
        tmp_sum += arr[i - 1]
        if A[-1] == k or B[-1] == k:
            print('True')
            result = 1
            break
        j = arr[i - 1]
        while j < (k + 1) and j <= tmp_sum:
            if i % 2 == 0:
                A[j] = max(B[j], B[j - arr[i - 1]] + arr[i - 1])
            else:
                B[j] = max(A[j], A[j - arr[i - 1]] + arr[i - 1])
            j += 1

    if result == 0:
        if k % 2 == 0:
            print(A[-1] == k)
        else:
            print(B[-1] == k)

# print(datetime.now() - start_time)
