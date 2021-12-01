'''
ID 59618093
1. Слова словаря превращаем в граф по принципу: начало ребра = номер входа слова в длинное слово, окончание ребра = начало ребра + длинна слова
2. Далее перебираем в ширину все узлы нашего графа из стартовой точки 0
3. Если у узла есть ребро, которое заканчивается в точке окончания длинного слова (номер окончания ребра = равен длинне слова), то мы нашли то, что искали.
Корректность решения - у нас непрерыная цепочка слов (граф), длинна которой = длинне основного слова
Сложность алгоритма - динна главного слова * количество слов в словаре О(n*m)

'''



from collections import deque


def ins_count(a, b):
    r = a.find(b)
    while r != -1:
        if r in graph:
            graph[r].append(r + len(b))
        else:
            graph[r] = [r + len(b)]
        r = a.find(b, r + 1)


def bfs():
    rezult = 'NO'
    while len(planned) > 0 and rezult == 'NO':
        u = planned.pop()  # Возьмём вершину из очереди.
        if u in graph:
            for v in graph[u]:
                if v == len(a):
                    rezult = 'YES'
                    break
                if color[v] == 'white':  # Серые и чёрные вершины уже
                    color[v] = 'gray'
                    planned.append(v)  # Запланируем посещение вершины.
            color[u] = 'black'  # Теперь вершина считается обработанной.
    return rezult


a = input()
n = int(input())
graph = dict()
color = ['white'] * (len(a) + 1)


for i in range(n):
    ins_count(a, input())

planned = deque()
planned.append(0)
color[0] = 'gray'


print(bfs())
