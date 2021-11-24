n = int(input())
A = [int(i) for i in input().split(' ')]
m = int(input())
B = [int(i) for i in input().split(' ')]
A = [A[i + 1] - A[i] for i in range(n - 1)]
B = [B[i + 1] - B[i] for i in range(m - 1)]

# n=9
# m=2
# A=[6, -8, 1, 3, 5, -1, -8, 6]
# B=[6]

i = 0
j = 0
match = []
while i < n - 1:
    if n - i >= m and A[i:i+(m-1)] == B:
        match.append(i + 1)
    i += 1

print(*match)
