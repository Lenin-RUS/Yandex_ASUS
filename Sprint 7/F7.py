n, k = (int (i) for i in input().split(' '))
F = [1]
MOD = 10**9 + 7
for _ in range(k-1):
    F.append((sum(F))%MOD)

for _ in range(k, n):
    F.append((sum(F[-k:]))%MOD)

print(F[-1])