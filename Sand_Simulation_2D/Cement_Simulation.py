import pygame
import random
import numpy as np

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sand Simulation")
WHITE = (255, 255, 255)
SAND = (128, 128, 128)
#cement gray color-145, 117, 103
#sand yellow color-128, 128, 128
T = 16

class Grid:
    def __init__(self):
        self.grid = np.zeros((WIDTH * 2, HEIGHT + T))
        self.position = []

    def addSand(self, pointX, pointY):
        if pointX >= 0 and pointX <= WIDTH and pointY >= 0 and pointY <= HEIGHT:
            if self.grid[pointX][pointY] == 0:
                self.grid[pointX][pointY] = 1
                self.position.append((pointX, pointY))

    def update_position(self):
        new_position = []
        for points in self.position:
            listpoints = list(points)

            if points[1] >= HEIGHT - T:
                new_position.append(points)

            elif self.grid[points[0]][points[1] + T] == 0:
                self.grid[points[0]][points[1]] = 0
                self.grid[points[0]][points[1] + T] = 1
                listpoints[1] += T
                new_position.append(tuple(listpoints))

            else:
                left = self.grid[points[0] - T][points[1] + T]
                right = self.grid[points[0] + T][points[1] + T]

                if left == 0 and right == 0:
                    a = random.choice([-1, 1])
                elif left == 0:
                    a = -1
                elif right == 0:
                    a = 1
                else:
                    a = 0

                if a != 0:
                    self.grid[points[0]][points[1]] = 0
                    self.grid[points[0] + a * T][points[1] + T] = 1
                    listpoints[0] += a * T
                    listpoints[1] += T
                    new_position.append(tuple(listpoints))
                else:
                    new_position.append(points)

        self.position = new_position

    def draw(self, win):
        for points in self.position:
            pygame.draw.rect(win, SAND, (points[0], points[1], T, T), 0)

def main():
    run = True
    sand_dropping = False  # Flag to track if left mouse button is held down
    sandbox = Grid()

    while run:
        pygame.time.delay(10)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                sand_dropping = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left mouse button released
                sand_dropping = False

        # Continuously add sand while left mouse button is held down
        if sand_dropping:
            pos = pygame.mouse.get_pos()
            sandbox.addSand(pos[0] - pos[0] % T, pos[1] - pos[1] % T)

        sandbox.update_position()
        sandbox.draw(WIN)

        pygame.display.update()

    pygame.quit()

main()
