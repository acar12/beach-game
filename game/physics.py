from random import choice
from helper import turn_coords_to_i
from constants import Particle

def update_particle(grid, x, y):
    cell = grid[y][x]
    if cell == Particle.SAND or cell == Particle.WATER:
        if y != len(grid) - 1:
            if grid[y + 1][x] == Particle.EMPTY:
                grid[y][x] = Particle.EMPTY
                grid[y + 1][x] = cell
                return turn_coords_to_i(grid, x, y + 1)
            
            left = x != len(grid[0]) - 1 and grid[y + 1][x + 1] == Particle.EMPTY
            right = x != 0 and grid[y + 1][x - 1] == Particle.EMPTY
            
            if left and right:
                x_choice = choice((-1, 1))
                grid[y][x] = Particle.EMPTY
                grid[y + 1][x + x_choice] = cell
                return turn_coords_to_i(grid, x + x_choice, y + 1)
            elif left:
                grid[y][x] = Particle.EMPTY
                grid[y + 1][x + 1] = cell
                return turn_coords_to_i(grid, x + 1, y + 1)
            elif right:
                grid[y][x] = Particle.EMPTY
                grid[y + 1][x - 1] = cell
                return turn_coords_to_i(grid, x - 1, y + 1)
    if cell == Particle.WATER:
        left = x != 0 and grid[y][x - 1] == Particle.EMPTY
        right = x != len(grid[0]) - 1 and grid[y][x + 1] == Particle.EMPTY

        if left and right:
            x_choice = choice((-1, 1))
            grid[y][x] = Particle.EMPTY
            grid[y][x + x_choice] = cell
            return turn_coords_to_i(grid, x + x_choice, y)
        elif right:
            grid[y][x] = Particle.EMPTY
            grid[y][x + 1] = cell
            return turn_coords_to_i(grid, x + 1, y)
        elif left:
            grid[y][x] = Particle.EMPTY
            grid[y][x - 1] = cell
            return turn_coords_to_i(grid, x - 1, y)
