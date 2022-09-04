from random import choice
from constants import Particle

def update_particle(grid, x, y):
    cell = grid[y][x]
    if cell == Particle.SAND or cell == Particle.WATER:
        if y != len(grid) - 1:
            if grid[y + 1][x] == Particle.EMPTY:
                grid[y][x] = Particle.EMPTY
                grid[y + 1][x] = cell
                return (y + 1) * len(grid[0]) + x
            
            left = x != len(grid[0]) - 1 and grid[y + 1][x + 1] == Particle.EMPTY
            right = x != 0 and grid[y + 1][x - 1] == Particle.EMPTY
            
            if left and right:
                x_choice = choice((-1, 1))
                grid[y][x] = Particle.EMPTY
                grid[y + 1][x + x_choice] = cell
                return (y + 1) * len(grid[0]) + x + x_choice
            elif left:
                grid[y][x] = Particle.EMPTY
                grid[y + 1][x + 1] = cell
                return (y + 1) * len(grid[0]) + x + 1
            elif right:
                grid[y][x] = Particle.EMPTY
                grid[y + 1][x - 1] = cell
                return (y + 1) * len(grid[0]) + x - 1
    if cell == Particle.WATER:
        left = x != 0 and grid[y][x - 1] == Particle.EMPTY
        right = x != len(grid[0]) - 1 and grid[y][x + 1] == Particle.EMPTY

        if left and right:
            x_choice = choice((-1, 1))
            grid[y][x] = Particle.EMPTY
            grid[y][x + x_choice] = cell
            return y * len(grid[0]) + x + x_choice
        elif right:
            grid[y][x] = Particle.EMPTY
            grid[y][x + 1] = cell
            return y * len(grid[0]) + x + 1
        elif left:
            grid[y][x] = Particle.EMPTY
            grid[y][x - 1] = cell
            return y * len(grid[0]) + x - 1
