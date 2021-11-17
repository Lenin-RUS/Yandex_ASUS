n, s = (int(i) for i in input().split(' '))
w = [int(i) for i in input().split(' ')]
# n, s = 5, 15
# w = [3, 8, 1, 2, 5]

w.sort(reverse=True)
A = [0 for _ in range(s + 1)]
B = [0 for _ in range(s + 1)]

result = 0
for i in range(1, n + 1):
    if A[-1] == s or B[-1] == s:
        print(s)
        result = 1
        break

    for j in range(w[i - 1], s + 1):
        if i % 2 == 0:
            A[j] = max(B[j], B[j - w[i - 1]] + w[i - 1])
        else:
            B[j] = max(A[j], A[j - w[i - 1]] + w[i - 1])

if result == 0:
    if n % 2 == 0:
        print(A[-1])
    else:
        print(B[-1])

# print(result)