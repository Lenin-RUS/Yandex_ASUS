N, M = (int(i) for i in input().split(' '))
Edges = []
for i in range(M):
    start, end = (int(i)-1 for i in input().split(' '))
    Edges.append([start, end])


Color = [0] * (N + 1)
IsBipartite = True
def DFS(start):
    for u in V[start]:
        if Color[u] == 0:
            Color[u] = 3 - Color[start]
            DFS(u)
        else if Color[u] == Color[start]:
            IsBipartite = False
for i in range(1, n + 1):
    if Color[i] == 0:
        Color[i] = 1
        DFS(i)