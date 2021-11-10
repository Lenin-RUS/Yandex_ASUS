i = int(input())
F = [0, 1]
MOD = 10**9 + 7
for _ in range(i):
    F.append((F[-1] + F[-2])%MOD)
print(F[-1])
