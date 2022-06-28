import pygame
import sys
import math

pygame.init()

screen = pygame.display.set_mode((500, 500))
width, height = screen.get_size()

background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
pygame.display.set_caption("My game")
sw = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            sw = not (sw)
    if sw:
        screen.blit(background, (0, 0))
        pygame.draw.circle(background, (0, 0, 225), (250, 250), 30, 0)
        pygame.draw.rect(background, (0, 255, 0), [270, 130, 60, 40], 5)
        pygame.draw.ellipse(background, (0, 255, 0), [270, 130, 60, 40], 5)
        pygame.draw.line(background, (0, 255, 0), (288, 140), (60, 40), 3)
        pygame.draw.polygon(background, (100, 200, 45),
                            [[100, 100], [0, 200], [200, 200]], 0)
        pygame.draw.arc(background, (255, 10, 0), [100, 100, 100, 50],
                        math.radians(180), math.radians(0), 2)
        pygame.draw.circle(background, (0, 0, 225), (25, 250), 30, 0)
        pygame.draw.rect(background, (0, 255, 0), [270, 130, 60, 40], 5)
        pygame.draw.ellipse(background, (0, 255, 0), [260, 120, 60, 40], 5)
        pygame.draw.line(background, (0, 255, 0), (288, 140), (60, 40), 3)
        pygame.draw.polygon(background, (100, 200, 45),
                            [[100, 100], [0, 200], [200, 200]], 0)
        pygame.draw.arc(background, (255, 10, 0), [100, 100, 100, 50],
                        math.radians(180), math.radians(0), 2)
    else:
        background.fill((255, 255, 255))
        screen.blit(background, (0, 0))
    pygame.display.update()  #畫圈 畫布物件 顏色 中心位置 填滿
