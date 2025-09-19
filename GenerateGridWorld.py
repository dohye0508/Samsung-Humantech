import csv

def generate_mazes(num_of_mazes=1, size_of_square_maze=None, csv_file="sample.csv"):
    points = set()
    edges = []
    edge_costs = {}

    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))

        # 시작점과 끝점은 첫 번째 행 기준
        first_row = reader[0]
        start = [(int(first_row["x1"]), int(first_row["y1"]))]
        stop = [(int(first_row["x2"]), int(first_row["y2"]))]

        # 나머지 행 처리
        for row in reader:
            x1, y1, x2, y2 = map(int, [row["x1"], row["y1"], row["x2"], row["y2"]])
            c1, c2 = map(int, [row["cost1"], row["cost2"]])
            points.add((x1, y1))
            points.add((x2, y2))
            edges.append(((x1, y1), (x2, y2), c1, c2))
            edge_costs[((x1, y1), (x2, y2))] = c1
            edge_costs[((x2, y2), (x1, y1))] = c2

    # 맵 크기 계산
    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)
    rows, cols = max_x + 1, max_y + 1

    # 벽(2)로 초기화
    maze = [[2 for _ in range(cols)] for _ in range(rows)]
    for (x, y) in points:
        maze[x][y] = 1

    return [maze], start, stop, edge_costs
