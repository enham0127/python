import pygame
import sys
import math

pygame.init()

screen = pygame.display.set_mode((500, 500))
width, height = screen.get_size()
BLACK = (0, 0, 0)
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
pygame.display.set_caption("My game")
sw = False
typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render('Start', True, BLACK)
tit_w = title.get_width()
tit_h = title.get_height()


def display_font(win):
    win.blit(title, (0, 0))


def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = pos[0] > x_min and pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


while True:
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 0, 0, tit_w, tit_h):
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
        display_font(screen)
    pygame.display.update()  #畫圈 畫布物件 顏色 中心位置 填滿
