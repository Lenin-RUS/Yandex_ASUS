seq_1 = input()
seq_2 = input()

# seq_1 = 'innokentiy'
# seq_2 = 'innnokkentia'

x = len(seq_1) + 1
y = len(seq_2) + 1

result = [[0 for _ in range(y)] for _ in range(x)]

for i in range(x):
    result[i][0] = i
for j in range(y):
    result[0][j] = j

for i in range(1, x):
    for j in range(1, y):
        if seq_1[i - 1] == seq_2[j - 1]:
            result[i][j] = min(result[i - 1][j] + 1, result[i - 1][j - 1], result[i][j - 1] + 1)
        else:
            result[i][j] = min(result[i - 1][j] + 1, result[i - 1][j - 1] + 1, result[i][j - 1] + 1)

r = (result[-1][-1])
print(r)
