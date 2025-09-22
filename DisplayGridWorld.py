# DisplayGridWorld.py
# draw grid world as points and connecting lines

import pygame


def displayGridWorld(
    maze,
    title,
    reverse=False,
    path=None,
    explored=None,
    all_edges=None,
    start=None,
    goal=None,
    total_cost=None,
    path_text=None # 새롭게 추가된 매개변수
):
    # define colors
    black = (0, 0, 0)
    white = (245, 245, 245)
    green = (102, 176, 78)
    red = (214, 82, 82)
    blue = (0, 0, 255)
    orange = (255, 100, 0)
    yellow = (226, 123, 95)
    gray = (170, 170, 187)
    common_gray = (220, 220, 220)
    light_gray = (237, 237, 237)
    
    # window size
    size = [850, 850]
    node_size = 5
    screen = pygame.display.set_mode(size)

    # grid size
    rows = len(maze)
    cols = len(maze[0])
    margin = 1

    # square cell
    width = (size[0] // cols) - margin
    height = width

    # vertical padding (중앙 정렬)
    total_grid_height = rows * (height + margin)
    vertical_padding = (size[1] - total_grid_height) // 2

    # pygame init
    pygame.init()
    pygame.display.set_caption(title)
    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(light_gray)

        # Draw grid outlines
        for row in range(rows):
            for col in range(cols):
                rect = pygame.Rect(
                    (margin + width) * col + margin,
                    (margin + height) * row + margin + vertical_padding,
                    width, height
                )
                pygame.draw.rect(screen, common_gray, rect, 5)
        
        # Draw all explored edges (gray lines)
        if all_edges:
            for ((x1, y1), (x2, y2)) in all_edges:
                cx1 = (margin + width) * y1 + margin + width // 2
                cy1 = (margin + height) * x1 + margin + height // 2 + vertical_padding
                cx2 = (margin + width) * y2 + margin + width // 2
                cy2 = (margin + height) * x2 + margin + height // 2 + vertical_padding
                pygame.draw.line(screen, gray, (cx1, cy1), (cx2, cy2), 3)

        # Draw shortest path (black line)
        if path and len(path) > 1:
            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                cx1 = (margin + width) * y1 + margin + width // 2
                cy1 = (margin + height) * x1 + margin + height // 2 + vertical_padding
                cx2 = (margin + width) * y2 + margin + width // 2
                cy2 = (margin + height) * x2 + margin + height // 2 + vertical_padding
                pygame.draw.line(screen, black, (cx1, cy1), (cx2, cy2), 3)

        # Draw all nodes (circles)
        for row in range(rows):
            for col in range(cols):
                if maze[row][col] != 2:
                    cx = (margin + width) * col + margin + width // 2
                    cy = (margin + height) * row + margin + height // 2 + vertical_padding
                    pygame.draw.circle(screen, black, (cx, cy), node_size*1.1+2)
        
        if explored:
            for (x, y) in explored:
                cx = (margin + width) * y + margin + width // 2
                cy = (margin + height) * x + margin + height // 2 + vertical_padding
                pygame.draw.circle(screen, white, (cx, cy), node_size)

        if start:
            sx = (margin + width) * start[1] + margin + width // 2
            sy = (margin + height) * start[0] + margin + height // 2 + vertical_padding
            pygame.draw.circle(screen, green, (sx, sy), node_size)

        if goal:
            gx = (margin + width) * goal[1] + margin + width // 2
            gy = (margin + height) * goal[0] + margin + height // 2 + vertical_padding
            pygame.draw.circle(screen, red, (gx, gy), node_size)

        # Draw info text and path text
        font = pygame.font.SysFont("Arial", 24)
        info_text = f"Path length: {len(path)-1 if path else 0}   Cost: {total_cost if total_cost is not None else '?'}"
        text_surface = font.render(info_text, True, black)
        screen.blit(text_surface, (20, 20))

        # 경로 텍스트 렌더링
        if path_text:
            text_font = pygame.font.SysFont("Arial", 18)
            wrapped_text = ""
            current_line = ""
            for segment in path_text.split():
                if text_font.size(current_line + segment)[0] < size[0] - 40:
                    current_line += segment + " "
                else:
                    wrapped_text += current_line + "\n"
                    current_line = segment + " "
            wrapped_text += current_line

            y_pos = total_grid_height + vertical_padding + 30
            for line in wrapped_text.split("\n"):
                line_surface = text_font.render(line, True, black)
                screen.blit(line_surface, (20, y_pos))
                y_pos += 25

        clock.tick(20)
        pygame.display.flip()

    pygame.quit()