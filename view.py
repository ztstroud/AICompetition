import pygame, sys
from level import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((640,480))

images = {
    "hex": pygame.image.load("images/hex.png"),
    "hex_water": pygame.image.load("images/hex_water.png"),
    
    "hex_blue": pygame.image.load("images/hex_blue.png"),
    "hex_green": pygame.image.load("images/hex_green.png"),
    "hex_orange": pygame.image.load("images/hex_orange.png"),
    "hex_purple": pygame.image.load("images/hex_purple.png"),
    "hex_red": pygame.image.load("images/hex_red.png"),
    "hex_yellow": pygame.image.load("images/hex_yellow.png"),

    "peasant": pygame.image.load("images/peasant.png"),
    "spearman": pygame.image.load("images/spearman.png"),
    "knight": pygame.image.load("images/knight.png"),
    "baron": pygame.image.load("images/baron.png"),

    "capital": pygame.image.load("images/capital.png"),
    "farm": pygame.image.load("images/farm.png"),
    "tower": pygame.image.load("images/tower.png"),
    "magictower": pygame.image.load("images/magictower.png"),

    "pine": pygame.image.load("images/pine.png"),
    "palm": pygame.image.load("images/palm.png"),
    "grave": pygame.image.load("images/grave.png")
}

hexMapping = {
    -1: "hex_water",
    0:  "hex",
    1:  "hex_blue",
    2:  "hex_green",
    3:  "hex_orange",
    4:  "hex_purple",
    5:  "hex_red",
    6:  "hex_yellow"
}

level = Level.fromFile("levels/test_level.txt")

while True:
    msElapsed = clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((32, 32, 32))

    for y in range(level.height):
        for x in range(level.width):
            tile = level.getTile((x, y))

            screen.blit(images[hexMapping[tile.owner]], (x * 25, y * 32 + (x % 2) * 16))

            if tile.unit.type != UnitType.NONE:
                screen.blit(images[tile.unit.type.value], (x * 25, y * 32 + (x % 2) * 16))

    pygame.display.update()
