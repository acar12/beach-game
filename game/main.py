import pygame
from draw import draw_grid
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

    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        grid[y // cell_size][x // cell_size] = current_slot

    draw_grid(display, grid, cell_size)
    pygame.display.update() # update window
    clock.tick(60) # 60 fps max