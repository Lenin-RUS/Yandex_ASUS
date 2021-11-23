# n, s = (int(i) for i in input().split(' '))
# w = [int(i) for i in input().split(' ')]
n, s = 4, 14
w = [1, 5, 7, 1]
# w.sort(reverse=True)
A = [[0 for _ in range(s + 1)] for _ in range(n + 1)]

tmp_sum = 0
for i in range(1, n + 1):
    tmp_sum += w[i - 1]
    j = w[i - 1]
    while j < (s + 1) and j <= tmp_sum:
        A[i][j] = max(A[i - 1][j], (A[i - 1][j - w[i - 1]] + w[i - 1]))
        j += 1

print(A)
print(A[n][s])
