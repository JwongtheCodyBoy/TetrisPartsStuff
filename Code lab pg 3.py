import pygame
import sys
from copy import deepcopy

WIDTH, HEIGHT = 10, 20;
TILE = 45;
GAME_RES = (WIDTH * TILE, HEIGHT * TILE)

CLOCK = pygame.time.Clock()
GRID = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(WIDTH) for y in range(HEIGHT)]

pygame.init()
screen = pygame.display.set_mode(GAME_RES)
pygame.display.set_caption("Tetris")

tetrominos_pos = [[(-1,-1),(-2,-1),(0,-1),(1,-1)], # I
              [(0,-1),(-1,-1),(-1,0),(0,0)], # O
              [(0,0),(-1,-1),(0,-1),(1,0)], # Z
              [(0,0),(-1,0),(0,-1),(1,-1)], # S
              [(0,0),(-1,0),(1,0),(1,-1)], # L
              [(0,0),(-1,-1),(-1,0),(1,0)], # J
              [(0,0),(-1,0),(1,0),(0,-1)]] # T

tetrominos = [[pygame.Rect(x + WIDTH // 2, y +1, 1, 1) for x, y in block_pos] for block_pos in tetrominos_pos]
tetromino_rect = pygame.Rect(0,0, TILE -2, TILE -2)

tetromino = tetrominos[0]

while True:
    screen.fill(pygame.Color("black"))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    [pygame.draw.rect(screen, (40,40,40), i_rect, 1) for i_rect in GRID]
    
    for i in range(4):
        tetromino_rect.x = tetromino[i].x * TILE
        tetromino_rect.y = tetromino[i].y * TILE
        pygame.draw.rect(screen, pygame.Color("white"), tetromino_rect)
        
    pygame.display.update()
    CLOCK.tick(60)