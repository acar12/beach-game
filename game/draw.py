import pygame
from constants import Color, Particle

pygame.font.init()
font = pygame.font.SysFont("Arial", 12, bold=True)

def draw_grid(display, grid, cell_size):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            color_mapping = {Particle.EMPTY: Color.BLACK, Particle.WALL: Color.GRAY, Particle.SAND: Color.BEIGE, Particle.WATER: Color.BLUE}
            color = color_mapping[cell]
            pygame.draw.rect(display, color, (x * cell_size, y * cell_size, cell_size, cell_size))

def draw_text(display, x, y, text):
    text_surface = font.render(text, True, Color.WHITE)
    display.blit(text_surface, (x, y))
