class Stack():
    def __init__(self):
        self.values = []
        self.colors = dict()

    def pop(self):
        return self.values.pop()

    def push(self, value):
        self.values.append(value)

    def is_empty(self):
        return len(self.values)


def DFS(start_vertex):
    stack = Stack()
    stack.push(start_vertex)
    if not start_vertex in stack.colors:
        stack.colors[start_vertex] = 'white'

    while stack.is_empty():
        v = stack.pop()
        if stack.colors[v] == 'white':
            stack.colors[v] = 'gray'
            stack.push(v)

            if v in graph:
                for w in graph[v]:
                    if not w in stack.colors:
                        stack.colors[w] = 'white'

                    if stack.colors[w] == 'white':
                        stack.push(w)
                    else:
                        stack.colors[v] == 'gray'
            stack.colors[v] = 'black'
            print(v, end=' ')


v = [int(i) for i in input().split(' ')]
e = []
graph = dict()
for i in range(v[1]):
    e = [int(i) for i in input().split(' ')]
    if e[0] in graph:
        graph[e[0]].append(e[1])
    else:
        graph[e[0]] = [e[1]]

    if e[1] in graph:
        graph[e[1]].append(e[0])
    else:
        graph[e[1]] = [e[0]]
start_vertex = int(input())

#
# graph = {3: [4, 2], 2: [3, 1], 4: [3, 1], 1: [4, 2]}
# start_vertex=3

for i in graph:
    graph[i] = sorted(graph[i], reverse=True)

DFS(start_vertex)

# print(graph)
