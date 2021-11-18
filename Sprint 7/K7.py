n = int(input())
seq_1=[int(i) for i in input().split(' ')]
m = int(input())
seq_2=[int(i) for i in input().split(' ')]


# n = 5
# seq_1 = [4, 9, 2, 4, 6]
# m = 7
# seq_2 = [9, 4, 0, 0, 2, 8, 4]

field = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if seq_2[i - 1] == seq_1[j - 1]:
            field[i][j] = field[i - 1][j - 1] + 1
        else:
            field[i][j] = max(field[i][j - 1], field[i - 1][j])
#
# for i in field:
#     print(*i)

j = n
i = m
l = []
seq_1_index = []
seq_2_index = []
while field[i][j] != 0:
    if seq_1[j - 1] == seq_2[i - 1]:
        l.append(seq_1[j - 1])
        seq_1_index.append(j)
        seq_2_index.append(i)
        i -= 1
        j -= 1
    else:
        if field[i][j] == field[i][j - 1]:
            j -= 1
        elif field[i][j] == field[i - 1][j]:
            i -= 1

# l.reverse()
seq_1_index.reverse()
seq_2_index.reverse()
print(field[-1][-1])
print(*seq_1_index)
print(*seq_2_index)
# seq_1_index = []
# seq_2_index = []
# i = 1
# j = 1
# k = 1
# while k < len(l):
#     while seq_1[i] != l[k]:
#         i += 1
#     seq_1_index.append(i)
#     while seq_2[j] != l[k]:
#         j += 1
#     seq_2_index.append(j)
#     k += 1

# print(*l, sep='')
# pass
