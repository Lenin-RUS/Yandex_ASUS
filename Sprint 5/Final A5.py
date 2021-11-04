'''
ID 55258457
Мда..... все оказалось гораздо проще....


1. Делаем массив из игроков [-очков, штраф, имя] и отправляем его в функцию сортировки кучи
2. На первом этапе - создаем из массива игроков бинарную кучу по заданной позиции массива.
3. Сортируем кучу и переставляем в массиве игроком по убыванию.
4. Выводим игроков на печать.
'''


def heap_create_and_sort(players, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and players[left_child] > players[largest]:
        largest = left_child

    if right_child < heap_size and players[right_child] > players[largest]:
        largest = right_child

    if largest != root_index:
        players[root_index], players[largest] = players[largest], players[root_index]
        heap_create_and_sort(players, heap_size, largest)


def heapsort(players):
    n = len(players)
    for i in range(n, -1, -1):  # Тут мы создаем бинарную кучу
        heap_create_and_sort(players, n, i)
    for i in range(n - 1, -1, -1):
        players[i], players[0] = players[0], players[i]
        heap_create_and_sort(players, i, 0)
    return players


n = int(input())
players = []
for j in range(n):
    a = [inp for inp in input().split(' ')]
    players.append([-int(a[1]), int(a[2]), a[0]])

# players = [['tima', -9, 100], ['tima', -9, 200], ['tima', -9, 100], ['tima', -9, 200], ['tima', -9, 100], ['tima', -9, -2000]]
players = heapsort(players)
for player in players:
    print(player[2])
