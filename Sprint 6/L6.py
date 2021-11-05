v = [int(i) for i in input().split(' ')]
all_edges = v[0] * (v[0] - 1) / 2

if v[1] < all_edges:
    print('NO')
else:
    c = set()
    for i in range(v[1]):
        e = [int(i) - 1 for i in input().split(' ')]
        if e[0] > e[1]:
            elem = str(e[0]) + '_' + str(e[1])
            c.add(elem)
        elif e[0] < e[1]:
            elem = str(e[1]) + '_' + str(e[0])
            c.add(elem)

    if len(c) == all_edges:
        print('YES')
    else:
        print('NO')
