value = int(input())
_ = input()
noms = set([int(i) for i in input().split(' ')])
noms = list(noms)
noms.sort(reverse=True)
notes = 0
for i in noms:
    if value == 0:
        break
    elif value >= i:
        notes += value // i
        value = value % i
    elif value < noms[-1]:
        notes = -1
        break

print(notes)
