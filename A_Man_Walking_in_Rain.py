import pygame
import random
import sys
pygame.init()
WIDTH = 800
HEIGHT = 600
GROUND_Y = int(HEIGHT * 0.75)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RAIN_COLOR = (100, 100, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A Man Walking in Rain")
clock = pygame.time.Clock()
ldisp = 0
def draw_man_and_umbrella(x, ldisp):
    pygame.draw.circle(screen, BLACK, (x, GROUND_Y - 90), 10)
    pygame.draw.line(screen, BLACK, (x, GROUND_Y - 80), (x, GROUND_Y - 30), 2)
    pygame.draw.line(screen, BLACK, (x, GROUND_Y - 70), (x + 10, GROUND_Y - 60), 2)
    pygame.draw.line(screen, BLACK, (x, GROUND_Y - 65), (x + 10, GROUND_Y - 55), 2)
    pygame.draw.line(screen, BLACK, (x + 10, GROUND_Y - 60), (x + 20, GROUND_Y - 70), 2)
    pygame.draw.line(screen, BLACK, (x + 10, GROUND_Y - 55), (x + 20, GROUND_Y - 70), 2)
    pygame.draw.line(screen, BLACK, (x, GROUND_Y - 30), (x + ldisp, GROUND_Y), 2)
    pygame.draw.line(screen, BLACK, (x, GROUND_Y - 30), (x - ldisp, GROUND_Y), 2)
    pygame.draw.arc(screen, BLACK, (x + 20 - 40, GROUND_Y - 120 - 40, 80, 80), 0, 3.1416, 2)
    pygame.draw.line(screen, BLACK, (x + 20, GROUND_Y - 120), (x + 20, GROUND_Y - 70), 2)
def rain(x):
    for _ in range(400):
        rx = random.randint(0, WIDTH)
        ry = random.randint(0, HEIGHT)
        if ry < GROUND_Y - 4:
            # Block rain hitting umbrella area
            if ry < GROUND_Y - 120 or (rx < x - 20 or rx > x + 60):
                pygame.draw.line(screen, RAIN_COLOR, (rx, ry), (rx, ry + 4))
def main():
    x = 0
    ldisp = 0
    while True:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.draw.line(screen, BLACK, (0, GROUND_Y), (WIDTH, GROUND_Y), 2)
        rain(x)
        ldisp = (ldisp + 2) % 20
        draw_man_and_umbrella(x, ldisp)
        x = (x + 2) % WIDTH
        pygame.display.flip()
        clock.tick(30)
if __name__ == "__main__":
    main()
