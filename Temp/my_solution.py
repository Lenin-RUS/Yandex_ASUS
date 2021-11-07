nod, edg = (int(i) for i in input().split(' '))
e = []

edges_arr = dict()
nodes_arr = dict()

for i in range(nod):
    nodes_arr[i]=[]

count = 0
for i in range(edg):
    start, end, w = (int(i)-1 for i in input().split(' '))
    nodes_arr[start].append(count)
    nodes_arr[end].append(count)
    edges_arr[count] = [start, end, w+1]
    edges_arr[count+edg] = [end, start, w+1]
    count+=1

pass