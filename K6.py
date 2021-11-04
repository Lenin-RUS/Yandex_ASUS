функция relax(u, v):
    # Проверяем, не получился ли путь короче найденного ранее.
    если dist[v] > dist[u] + weight(u, v), то
        dist[v] = dist[u] + weight(u, v)
        previous[v] = u


функция get_min_dist_not_visited_vertex():
    # Находим ещё непосещённую вершину с минимальным расстоянием от s.
    current_minimum = inf
    current_minimum_vertex = null

    для каждой вершины v из graph.vertices:
        если (не visited[v]) И (dist[v] < current_minimum), то
            current_minimum = dist[v]
            current_minimum_vertex = v
    return current_minimum_vertex


функция Dijkstra(graph, s):
    для каждой вершины v из graph.vertices:
        dist[v] = inf         # Задаём расстояние по умолчанию.
        previous[v] = null      # Задаём предшественника для восстановления SPT.
        visited[v] = false    # Список статусов посещённости вершин.

    dist[s] = 0     # Расстояние от вершины до самой себя 0.

    пока существуют непосещённые вершины с расстоянием не равным бесконечности:
        u = get_min_dist_not_visited_vertex()

        visited[u] = true
        # из множества рёбер графа выбираем те, которые исходят из вершины u
        neighbours = graph.outgoing_edges(u)

        для каждого ребра (u, v) среди рёбер к соседним вершинам neighbours:
            relax(u, v)