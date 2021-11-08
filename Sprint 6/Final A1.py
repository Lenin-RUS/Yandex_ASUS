N, M = (int(i) for i in input().split(' '))
Edges = []
for i in range(M):
    start, end, weight = (int(i)-1 for i in input().split(' '))
    Edges.append([weight+1, start, end])

Edges.sort(reverse=True)
Comp = [i for i in range(N)]
Ans = 0
for weight, start, end in Edges:
    if Comp[start] != Comp[end]:
        Ans += weight
        a = Comp[start]
        b = Comp[end]
        for i in range(N):
            if Comp[i] == b:
                Comp[i] = a
if M == 0 and N != 1:
    print('Oops! I did it again')
else:
    if len(set(Comp)) > 1:
        print('Oops! I did it again')
    else:
        print(Ans)