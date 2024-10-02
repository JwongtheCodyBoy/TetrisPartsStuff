import pygame
import sys
from copy import deepcopy
from random import choice 

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

tetrominos = [[pygame.Rect(x + WIDTH // 2, y +1, 1, 1) for x, y in block_pos] for block_pos in tetrominos_pos]
tetromino_rect = pygame.Rect(0,0, TILE -2, TILE -2)

tetromino = deepcopy(choice(tetrominos))  
feild = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]         

anim_count, anim_speed, anim_limit = 0, 60, 2000        # NEW CODE HERE


def check_borders():
    if tetromino[i].x < 0 or tetromino[i].x > WIDTH-1:
        return False
    elif tetromino[i].y > HEIGHT -1 or feild[tetromino[i].y][tetromino[i].x]:
        return False
    return True

tetrominos = [[pygame.Rect(x + WIDTH // 2, y +1, 1, 1) for x, y in block_pos] for block_pos in tetrominos_pos]
tetromino_rect = pygame.Rect(0,0, TILE -2, TILE -2)

tetromino = deepcopy(tetrominos[0])     # MODIFED CODE HERE

while True:
    screen.fill(pygame.Color("black"))

    dir_x = 0       # NEW CODE HERE
    rotate = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # NEW CODE HERE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dir_x = -1
            elif event.key == pygame.K_RIGHT:
                dir_x = 1
            elif event.key == pygame.K_DOWN:
                anim_limit = 100
            elif event.key == pygame.K_UP:      
                rotate = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                    anim_limit = 2000

    tetromino_old = deepcopy(tetromino)
    for i in range(4):
        tetromino[i].x += dir_x
        if not check_borders():
            tetromino = deepcopy(tetromino_old)
            break
        
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        tetromino_old = deepcopy(tetromino)
        for i in range(4):
            tetromino[i].y += 1
            if not check_borders():
                for i in range(4):
                    feild[tetromino_old[i].y][tetromino_old[i].x] = pygame.Color('white')
                tetromino = deepcopy(choice(tetrominos))
                break
    
    center = tetromino[0]
    tetromino_old = deepcopy(tetromino)
    if rotate:
        for i in range(4):
            x = tetromino[i].y - center.y
            y = tetromino[i].x - center.x
            tetromino[i].x = center.x - x
            tetromino[i].y = center.y + y
            if not check_borders():
                tetromino = deepcopy(tetromino_old)
                break
    
    [pygame.draw.rect(screen, (40,40,40), i_rect, 1) for i_rect in GRID]
    
    for i in range(4):
        tetromino_rect.x = tetromino[i].x * TILE
        tetromino_rect.y = tetromino[i].y * TILE
        pygame.draw.rect(screen, pygame.Color("white"), tetromino_rect)
        
    for y, row in enumerate(feild):
        for x, col in enumerate(row):
            if col:
                tetromino_rect.x, tetromino_rect.y = x * TILE, y * TILE
                pygame.draw.rect(screen, col, tetromino_rect)    
    
    line = HEIGHT - 1
    for row in range(HEIGHT - 1, -1, -1):
        count = 0
        for i in range(WIDTH):
            if feild[row][i]:
                count += 1
            feild[line][i] = feild[row][i]
        if count < WIDTH:
            line -= 1
    
    pygame.display.update()
    CLOCK.tick(60)