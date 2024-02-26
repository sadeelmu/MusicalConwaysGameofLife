import pygame
import numpy as np
import time

WIDTH, HEIGHT = 1000, 780
RESOLUTION = 20
COLS, ROWS = WIDTH // RESOLUTION, HEIGHT // RESOLUTION

def create_grid():
    return np.random.randint(2, size=(COLS, ROWS))

def count_neighbors(grid, x, y):
    return np.sum(grid[x-1:x+2, y-1:y+2]) - grid[x, y]

def next_gen(grid):
    next_grid = np.zeros((COLS, ROWS), dtype=int)
    for i in range(COLS):
        for j in range(ROWS):
            state = grid[i, j]
            neighbors = count_neighbors(grid, i, j)
            if state == 1 and (neighbors < 2 or neighbors > 3):
                next_grid[i, j] = 0
            elif state == 0 and neighbors == 3:
                next_grid[i, j] = 1
            else:
                next_grid[i, j] = state
    return next_grid

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")

    pygame.mixer.init()
    sound = pygame.mixer.Sound("met.mp3")

    grid = create_grid()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grid = next_gen(grid)
        sound.play()

        #draw the grid
        screen.fill((0, 0, 0))
        for i in range(COLS):
            for j in range(ROWS):
                color = (255, 255, 255) if grid[i, j] == 1 else (0, 0, 0)
                pygame.draw.rect(screen, color, (i * RESOLUTION, j * RESOLUTION, RESOLUTION-1, RESOLUTION-1))

        pygame.display.flip()

        time.sleep(0.1)

    pygame.quit()

if __name__ == "__main__":
    main()
