import pygame
import sys

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((640,480))

hex = pygame.image.load("hex.png")

while True:
    msElapsed = clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((32, 32, 32))

    for y in range(10):
        for x in range(10):
            screen.blit(hex, (x * 25, y * 32 + (x % 2) * 16))

    pygame.display.update()
