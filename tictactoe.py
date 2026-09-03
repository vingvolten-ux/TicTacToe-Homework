#Used to give us the exit
import sys

import pygame
import numpy as np

#helps with handling geometry
pygame.init()

#colors
WHITE = (255,255,255)
GRAY = (180,180,180)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

#Propotions & sizes
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

#Screens
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tic Tac Toe AI')
screen.fill(BLACK)

#Board
board = np.zeros((BOARD_ROWS, BOARD_COLS))

#Drawing lines
def draw_lines(color=WHITE):
    for i in range(1,BOARD_ROWS):
        pygame.draw.line(screen, color, start_pos: (0, SQUARE_SIZE * i), end_pos: (WIDTH,SQUARE_SIZE * i),LINE_WIDTH)
        pygame.draw.line(screen, color, start_pos: (SQUARE_SIZE * i, 0), end_pos: (SQUARE_SIZE * i, HEIGHT),LINE_WIDTH)

#Drawing figure
def draw_figures(coler=WHITE):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]==1:
                pygame.draw.circle(screen,color, center: (int(col * SQUARE_SIZE + SQUARE_SIZE // 2),int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, start_pos:(col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4), end_pos: (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4))
                pygame.draw.line(screen, start_pos:(col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE +3 * SQUARE_SIZE // 4), end_pos: (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE +  SQUARE_SIZE //4))

def mark_square(row,col,player):
    board[row][col] = player


def available_square(row,col):
    return board[row][col] == 0


def is_board_full(check_board=board):
    for row in range(BOARD_ROWS):
        for col in range
                