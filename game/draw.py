import pygame
from constants import Color, Particle

def draw(display, grid, cell_size):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            color_mapping = {Particle.EMPTY: Color.BLACK, Particle.WALL: Color.GRAY, Particle.SAND: Color.BEIGE, Particle.WATER: Color.BLUE}
            color = color_mapping[cell]
            pygame.draw.rect(display, color, (x * cell_size, y * cell_size, cell_size, cell_size))
