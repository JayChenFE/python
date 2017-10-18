import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("12-1 blue window")

screen.fill((0, 0, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
