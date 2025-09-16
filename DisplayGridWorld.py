# used to draw grid worlds
import pygame


def displayGridWorld(maze, title, reverse=False):
    # define colors
    black = (0, 0, 0)  # blocked
    white = (255, 255, 255)  # unblocked
    green = (0, 255, 0)  # start
    red = (255, 0, 0)  # end
    blue = (0, 0, 255)  # explored cells
    orange = (255, 153, 0)  # shortest path

    # set width and height of window
    size = [850, 850]
    screen = pygame.display.set_mode(size)

    # set rows, cols from maze
    rows = len(maze)
    cols = len(maze[0])
    margin = 1

    # 가로 칸 기준으로 정사각형 칸 크기 계산
    width = (size[0] // cols) - margin
    height = width  # 정사각형 유지

    # 실제 그려질 전체 높이
    total_grid_height = rows * (height + margin)
    # 위/아래 검은 패딩 계산
    vertical_padding = (size[1] - total_grid_height) // 2

    # initialize the game engine
    pygame.init()
    pygame.display.set_caption(title)

    # Loop until user closes the window
    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():  # user did something
            if event.type == pygame.QUIT:  # user clicked close
                done = True

        # all event processing

        # code to draw
        screen.fill(black)

        # draw the grid
        for row in range(len(maze)):
            for column in range(len(maze[0])):
                if maze[row][column] == 1:
                    color = white
                elif maze[row][column] == 2:
                    color = black
                elif maze[row][column] == 5:
                    if reverse:
                        color = red
                    else:
                        color = green
                elif maze[row][column] == 10:
                    if reverse:
                        color = green
                    else:
                        color = red
                elif maze[row][column] == 7:
                    color = blue  # explored cells
                else:
                    color = orange  # shortest path

                # Y좌표에 vertical_padding 추가해서 위아래 패딩 적용
                pygame.draw.rect(screen, color, [
                    (margin + width) * column + margin,
                    (margin + height) * row + margin + vertical_padding,
                    width, height
                ])

        # 20 frames per second
        clock.tick(20)
        pygame.display.flip()

    pygame.quit()
