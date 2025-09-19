from heapq import heappop, heappush  # binary heap for open-list
import ConstructPath
import DisplayGridWorld


def manhattan_distance(a, b):  # heuristic function
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(grid_world, start, stop, display=False, reverse=False):
    if reverse:
        title = "Reverse A Star LowerG"
        start, stop = stop, start
    else:
        title = "A Star LowerG"

    size = len(grid_world) - 1
    open_list = []
    complete_closed_list = []
    closed_list = set()
    g_scores = {}
    parents = {}
    heappush(open_list, (0, 0, start, None))  # f, g, cell, parent

    while open_list:
        # Move to the best cell
        cell = heappop(open_list)
        previous_cost = cell[1]
        current_cell = cell[2]

        if current_cell == stop:
            complete_closed_list.append(cell)

            path = ConstructPath.construct_path_from_dict(parents, stop, start)

            # goal이 path에 포함되지 않았다면 추가
            if path[-1] != stop:
                path.append(stop)

            if display:
                DisplayGridWorld.displayGridWorld(
                    grid_world,
                    title,
                    reverse,
                    path=path,
                    explored=closed_list,
                    start=start,
                    goal=stop
                )
                return path, closed_list
            else:
                return path, closed_list


        if current_cell in closed_list:
            continue  # ignore cells already evaluated

        complete_closed_list.append(cell)
        closed_list.add(current_cell)

        # calculate f score for each valid neighbor
        x = current_cell[0]
        y = current_cell[1]

        if y > 0 and grid_world[x][y - 1] != 2 and (x, y - 1) not in closed_list:
            left = (x, y - 1)
            new_g_score = previous_cost + 1

            if left in g_scores and g_scores[(x, y - 1)] < new_g_score:
                parent = parents[left]
            else:
                g_scores[left] = new_g_score
                parents[left] = current_cell
                parent = current_cell

            f_score = manhattan_distance(left, stop) + g_scores[left]
            heappush(open_list, (f_score, g_scores[left], left, parent))

        if x > 0 and grid_world[x - 1][y] != 2 and (x - 1, y) not in closed_list:
            up = (x - 1, y)
            new_g_score = previous_cost + 1

            if up in g_scores and g_scores[(x - 1, y)] < new_g_score:
                parent = parents[up]
            else:
                g_scores[up] = new_g_score
                parents[up] = current_cell
                parent = current_cell

            f_score = manhattan_distance(up, stop) + g_scores[up]
            heappush(open_list, (f_score, g_scores[up], up, parent))

        if y < size and grid_world[x][y + 1] != 2 and (x, y + 1) not in closed_list:
            right = (x, y + 1)
            new_g_score = previous_cost + 1

            if right in g_scores and g_scores[(x, y + 1)] < new_g_score:
                parent = parents[right]
            else:
                g_scores[right] = new_g_score
                parents[right] = current_cell
                parent = current_cell

            f_score = manhattan_distance(right, stop) + g_scores[right]
            heappush(open_list, (f_score, g_scores[right], right, parent))

        if x < size and grid_world[x + 1][y] != 2 and (x + 1, y) not in closed_list:
            down = (x + 1, y)
            new_g_score = previous_cost + 1

            if down in g_scores and g_scores[(x + 1, y)] < new_g_score:
                parent = parents[down]
            else:
                g_scores[down] = new_g_score
                parents[down] = current_cell
                parent = current_cell

            f_score = manhattan_distance(down, stop) + g_scores[down]
            heappush(open_list, (f_score, g_scores[down], down, parent))

    # 경로가 없는 경우
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
    return [], []
