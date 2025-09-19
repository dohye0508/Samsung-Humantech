from heapq import heappop, heappush  # binary heap for open-list
import DisplayGridWorld


def a_star_search(grid_world, start, stop, edge_costs, display=False, reverse=False):
    """
    Graph-based Dijkstra (edge_costs 이용)
    모양은 격자(grid_world)를 그대로 쓰되,
    실제 탐색은 edge_costs 딕셔너리로만 수행.
    """

    if reverse:
        title = "Reverse Dijkstra (LowerG)"
        start, stop = stop, start
    else:
        title = "Dijkstra (LowerG)"

    open_list = []
    closed_list = set()
    g_scores = {}
    parents = {}

    # 시작점 초기화
    g_scores[start] = 0
    heappush(open_list, (0, 0, start, None))  # (f, g, node, parent)

    while open_list:
        cell = heappop(open_list)
        current_cost = cell[1]
        current_cell = cell[2]

        if current_cell == stop:
            # 경로 재구성
            path = []
            node = stop
            while node is not None:
                path.append(node)
                node = parents.get(node)
            path.reverse()

            if display:
                total_cost = g_scores.get(stop, None)
                DisplayGridWorld.displayGridWorld(
                    grid_world,
                    title,
                    reverse,
                    path=path,
                    explored=closed_list,
                    start=start,
                    goal=stop,
                    total_cost=total_cost
                )
            return path, closed_list, g_scores.get(stop, None)

        if current_cell in closed_list:
            continue

        closed_list.add(current_cell)

        # edge_costs 기반으로만 이웃 탐색
        for (u, v), cost in edge_costs.items():
            if u == current_cell and v not in closed_list:
                new_g_score = current_cost + cost

                if v in g_scores and g_scores[v] < new_g_score:
                    parent = parents[v]
                else:
                    g_scores[v] = new_g_score
                    parents[v] = current_cell
                    parent = current_cell

                # f=g로 (Dijkstra)
                heappush(open_list, (g_scores[v], g_scores[v], v, parent))

    # 도달 불가
    if display:
        DisplayGridWorld.displayGridWorld(
            grid_world,
            title,
            reverse,
            path=[],
            explored=closed_list,
            start=start,
            goal=stop
        )
    return [], closed_list, None
