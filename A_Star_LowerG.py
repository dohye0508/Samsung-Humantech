from heapq import heappop, heappush
import DisplayGridWorld


def format_path_text(path, g_scores):
    """
    경로를 (노드) (누적 비용) → (다음 노드) (누적 비용) 형식의 텍스트로 변환합니다.
    """
    if not path or len(path) < 1:
        return "경로 없음"
    
    path_segments = []
    # 첫 번째 노드 (시작점)은 별도로 처리
    path_segments.append(f"({path[0][0]},{path[0][1]}) {g_scores.get(path[0], '?')}")
    
    # 두 번째 노드부터는 '→'와 함께 처리
    for i in range(1, len(path)):
        node = path[i]
        segment = f" → ({node[0]},{node[1]}) {g_scores.get(node, '?')}"
        path_segments.append(segment)
        
    return "".join(path_segments)


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
    all_explored_edges = []
    
    g_scores[start] = 0
    heappush(open_list, (0, 0, start, None))

    while open_list:
        cell = heappop(open_list)
        current_cost = cell[1]
        current_cell = cell[2]

        if current_cell == stop:
            path = []
            node = stop
            while node is not None:
                path.append(node)
                node = parents.get(node)
            path.reverse()
            
            # g_scores 딕셔너리를 format_path_text 함수로 전달
            path_text = format_path_text(path, g_scores)

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
                    total_cost=total_cost,
                    all_edges=all_explored_edges,
                    path_text=path_text
                )
            return path, closed_list, g_scores.get(stop, None)

        if current_cell in closed_list:
            continue

        closed_list.add(current_cell)

        for (u, v), cost in edge_costs.items():
            if u == current_cell and v not in closed_list:
                all_explored_edges.append((u, v))

                new_g_score = current_cost + cost

                if v in g_scores and g_scores[v] < new_g_score:
                    parent = parents[v]
                else:
                    g_scores[v] = new_g_score
                    parents[v] = current_cell
                    parent = current_cell

                heappush(open_list, (g_scores[v], g_scores[v], v, parent))

    if display:
        DisplayGridWorld.displayGridWorld(
            grid_world,
            title,
            reverse,
            path=None,
            explored=closed_list,
            start=start,
            goal=stop,
            total_cost=None,
            all_edges=all_explored_edges,
            path_text="경로를 찾을 수 없습니다."
        )
    return None, closed_list, None