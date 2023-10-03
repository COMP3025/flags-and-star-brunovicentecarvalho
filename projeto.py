import sys

import pygame
from pygame.locals import QUIT
import math

def draw_star(surface, x, y, size, color):
    outer_points = []
    inner_points = []

    for i in range(5):
        angle = math.radians(18 + i * 72)
        
        outer_x = x + size * math.cos(angle)
        outer_y = y - size * math.sin(angle)
        outer_points.append((outer_x, outer_y))

        inner_angle = math.radians(54 + i * 72)
        inner_x = x + (size / 2) * math.cos(inner_angle)
        inner_y = y - (size / 2) * math.sin(inner_angle)
        inner_points.append((inner_x, inner_y))

    points = []
    for i in range(5):
        points.append(outer_points[i])
        points.append(inner_points[i])

    pygame.draw.polygon(surface, color, points)

azul = (0, 168, 255)
amarelo = (252, 209, 22)
vermelho = (206, 17, 38)

# Dimensões da tela
largura = 600
altura = 400

pygame.init()
tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Bandeira do Congo!')
while True:
   tela.fill(azul)
   pygame.draw.line(tela,vermelho,(680,0),(0,360),80)
   pygame.draw.line(tela,amarelo,(600,90),(0,410),20)
   pygame.draw.line(tela,amarelo,(600,0),(0,310),20) 
   draw_star(tela, 100, 100, 65, amarelo)
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   pygame.display.update()
