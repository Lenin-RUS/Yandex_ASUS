n, m = (int(i) for i in input().split(' '))
field = [0 for _ in range(n)]
for i in range(n - 1, -1, -1):
    field[i] = [int(i) for i in input()]

path = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == j == 0:
            path[i][j] = field[0][0]
        else:
            if i == 0:
                path[i][j] = field[i][j] + path[i][j - 1]
            elif j == 0:
                path[i][j] = field[i][j] + path[i - 1][j]
            else:
                path[i][j] = field[i][j] + max(path[i - 1][j], path[i][j - 1])



# n, m = 5, 5
# path = [[0, 0, 0, 0, 1], [1, 2, 3, 4, 4], [2, 2, 3, 5, 6], [3, 3, 3, 6, 7], [4, 5, 5, 7, 8]]
#
# for i in path:
#     print(*i)
#
print(path[-1][-1])

j = m - 1
i = n - 1
l = []
while j > 0 or i > 0:
    if j == 0:
        l.append('U')
        i -= 1
    elif i == 0:
        l.append('R')
        j -= 1
    elif path[i - 1][j] < path[i][j - 1]:
        l.append('R')
        j -= 1
    else:
        l.append('U')
        i -= 1
l.reverse()
print(*l, sep='')
pass
