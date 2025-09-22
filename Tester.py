import A_Star_LowerG
import A_Star_HigherG
import copy
import time
from GenerateGridWorld import generate_mazes

size = 20  # int(input("격자 크기를 입력하세요 (예: 20): "))
num = 1    # int(input("생성할 미로 개수를 입력하세요 (예: 1): "))

# =====================
# 미로 생성
all_mazes, start, stop, edge_costs = generate_mazes(num_of_mazes=num, size_of_square_maze=size)

# 미로 선택 (기본: 첫 번째 미로)
x = 0
current_maze = all_mazes[x]
copy_of_current_maze = copy.deepcopy(current_maze)
backward_maze = copy.deepcopy(current_maze)
backward_maze2 = copy.deepcopy(current_maze)
adaptive_maze = copy.deepcopy(current_maze)

# =====================
# LowerG (그래프 기반 다익스트라)
# =====================
lowerg_time = time.time()
path, explored_cells, total_cost = A_Star_LowerG.a_star_search(
    current_maze, start[x], stop[x], edge_costs, True
)
lowerg_end = time.time()