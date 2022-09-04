import pygame
from draw import draw_grid, draw_text
from constants import Color, Particle

width, height = 800, 800
cell_size = 10
g_width, g_height = width // cell_size, height // cell_size
grid = [[Particle.EMPTY for _ in range(g_width)] for _ in range(g_height)]

current_slot = Particle.SAND
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

running = True
while running:
    pygame.draw.rect(display, Color.BLACK, (0, 0, width, height)) # clear

    # controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0: current_slot = 0
            elif event.key == pygame.K_1: current_slot = 1
            elif event.key == pygame.K_2: current_slot = 2
            elif event.key == pygame.K_3: current_slot = 3

    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        grid[y // cell_size][x // cell_size] = current_slot

    draw_grid(display, grid, cell_size)
    draw_text(display, 0, 0, "0 - REMOVE | 1 - WALL | 2 - SAND | 3 - WATER")
    pygame.display.update() # update window
    clock.tick(60) # 60 fps max
