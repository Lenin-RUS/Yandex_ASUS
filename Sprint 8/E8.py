rita = input()
# rita = 'kukareku'
i = int(input())
gift = []
for j in range(i):
    k = [l for l in input().split(' ')]
    gift.append([int(k[1]), k[0]])

# gift=[[2, 'queue'], [0, 'deque'], [7, 'stack']]

gift.sort()
rez = ''
pos = 0
for i in gift:
    rez += rita[pos:i[0]]
    pos = i[0]
    rez += i[1]
rez += rita[pos:]
print(rez)
