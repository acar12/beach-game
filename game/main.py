import pygame
from constants import Color

width, height = 800, 800
display = pygame.display.set_mode((width, height))

def draw():
    pass

running = True
while running:
    pygame.draw.rect(display, Color.BLACK, (0, 0, width, height))
    draw()
    pygame.display.update()