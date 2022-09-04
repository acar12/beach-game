from constants import Particle

def update_particle(grid, x, y):
    cell = grid[y][x]
    if cell == Particle.SAND:
        if y != len(grid) - 1 and grid[y + 1][x] == Particle.EMPTY:
            grid[y][x] = Particle.EMPTY
            grid[y + 1][x] = Particle.SAND
            return (y + 1) * len(grid[0]) + x
