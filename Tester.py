import A_Star_LowerG
import A_Star_HigherG
import Adaptive_A_Star
import copy
import time
from GenerateGridWorld import generate_mazes

# =====================
# 사용자 입력 받기
# =====================
size = 20  # int(input("격자 크기를 입력하세요 (예: 20): "))
num = 1    # int(input("생성할 미로 개수를 입력하세요 (예: 1): "))

# =====================
# 미로 생성
# =====================
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

print("총 비용 =", total_cost)
print("경로 =", path)

# =====================
# HigherG (그대로 A* 격자형)
# =====================
start_time = time.time()
path2, explored_cells2 = A_Star_HigherG.a_star_search(copy_of_current_maze, start[x], stop[x], True)
end_time = time.time()

# =====================
# Reverse LowerG (edge_costs 포함)
# =====================
reverse_lowerg_time = time.time()
reverse_path, reverse_explored, reverse_cost = A_Star_LowerG.a_star_search(
    backward_maze, start[x], stop[x], edge_costs, True, True
)
reverse_reverse_lowerg_end = time.time()

# =====================
# Reverse HigherG (그대로 A* 격자형)
# =====================
reverse_higherG = time.time()
reverse_path2, reverse_explored2 = A_Star_HigherG.a_star_search(backward_maze2, start[x], stop[x], True, True)
reverse_higherG_end = time.time()

# =====================
# Adaptive A* (그대로, 아직 CSV 반영 안 됨)
# =====================
adap_start = time.time()
# d, p 변수는 네 코드에 맞게 넣어야 함
adaptive_path, adaptive_explored = Adaptive_A_Star.a_star_search(
    adaptive_maze, start[x], stop[x], d, p, 3, True
)
adap_end = time.time()

# =====================
# 출력
# =====================
print("Start = ", start[0])
print("Stop = ", stop[0])
print("Length of LowerG path =", len(path))
print("Length of HigherG path=", len(path2))
print("Length of reverse LowerG path =", len(reverse_path))
print("Length of reverse HigherG path=", len(reverse_path2))
print("Length of Adaptive HigherG path=", len(adaptive_path))
print("Number of explored cells LowerG =", len(explored_cells))
print("Number of explored cells HigherG =", len(explored_cells2))
print("Number of explored cells reverse LowerG =", len(reverse_explored))
print("Number of explored cells reverse HigherG =", len(reverse_explored2))
print("Number of explored cells Adaptive A* =", len(adaptive_explored))
print("Lower G total cost        ", total_cost)
print("Reverse Lower G total cost", reverse_cost)
print("Lower G A* time           ", lowerg_end - lowerg_time)
print("Higher G A* time          ", end_time - start_time)
print("Adaptive A* time          ", adap_end - adap_start)
print("Reverse Lower G A* time   ", reverse_reverse_lowerg_end - reverse_lowerg_time)
print("Reverse Higher G A* time  ", reverse_higherG_end - reverse_higherG)
