# DisplayGridWorld.py
# draw grid world as points and connecting lines

import pygame


def displayGridWorld(
    maze,
    title,
    reverse=False,
    path=None,
    explored=None,
    start=None,
    goal=None,
    total_cost=None
):
    # define colors
    black = (0, 0, 0)        # background
    white = (255, 255, 255)  # free cell
    green = (0, 255, 0)      # start
    red = (255, 0, 0)        # goal
    blue = (0, 0, 255)       # explored cells
    orange = (255, 153, 0)   # shortest path
    yellow = (255, 255, 0)

    # window size
    size = [850, 850]
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

        # background
        screen.fill(black)

        # draw grid outlines
        for row in range(rows):
            for col in range(cols):
                rect = pygame.Rect(
                    (margin + width) * col + margin,
                    (margin + height) * row + margin + vertical_padding,
                    width, height
                )
                pygame.draw.rect(screen, white, rect, 1)

        # draw all free cells as white points
        for row in range(rows):
            for col in range(cols):
                if maze[row][col] != 2:  # not a wall
                    cx = (margin + width) * col + margin + width // 2
                    cy = (margin + height) * row + margin + height // 2 + vertical_padding
                    pygame.draw.circle(screen, white, (cx, cy), 5)

        # draw explored cells as yellow points
        if explored:
            for (x, y) in explored:
                cx = (margin + width) * y + margin + width // 2
                cy = (margin + height) * x + margin + height // 2 + vertical_padding
                pygame.draw.circle(screen, yellow, (cx, cy), 5)

        # draw shortest path as orange line
        if path and len(path) > 1:
            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                cx1 = (margin + width) * y1 + margin + width // 2
                cy1 = (margin + height) * x1 + margin + height // 2 + vertical_padding
                cx2 = (margin + width) * y2 + margin + width // 2
                cy2 = (margin + height) * x2 + margin + height // 2 + vertical_padding
                pygame.draw.line(screen, orange, (cx1, cy1), (cx2, cy2), 3)

        # draw start & goal
        if start:
            sx = (margin + width) * start[1] + margin + width // 2
            sy = (margin + height) * start[0] + margin + height // 2 + vertical_padding
            pygame.draw.circle(screen, green, (sx, sy), 6)

        if goal:
            gx = (margin + width) * goal[1] + margin + width // 2
            gy = (margin + height) * goal[0] + margin + height // 2 + vertical_padding
            pygame.draw.circle(screen, red, (gx, gy), 6)

        # draw info text (총 비용 & 경로 길이)
        font = pygame.font.SysFont("Arial", 24)
        info_text = f"Path length: {len(path)-1 if path else 0}   Cost: {total_cost if total_cost is not None else '?'}"
        text_surface = font.render(info_text, True, white)
        screen.blit(text_surface, (20, 20))

        # refresh
        clock.tick(20)
        pygame.display.flip()

    pygame.quit()
