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
        for col in range(BOARD_ROWS):
            if check_board[row][col] == 0:
                return False
    return True

def check_win(player, check_board=board):
    #vertical win check
    for col in range(BOARD_COLS):
        if check_board[0][col] == player and check_board[1][col] == player and check_board[2][col] == player:
            draw_vertical_winning_line(col,player)
            return True

    #horizontal win check
    for row in range(BOARD_ROWS):
        if check_board[row][0] == player and check_board[row][1] == player and check_board[row][2] == player:
            draw_horizontal_winning_line(row,player)
            return True

    #asc diagonal win check
    if check_board[2][0] == player and check_board[1][1] == player and check_board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    #desc diagonal win check
    if check_board[0][0] == player and check_board[1][1] == player and check_board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


def minimax(board, depth, is_maximizing):
    if check_win(2, board):
        return 1
    elif check_win(1, board):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -np.inf
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    board[row][col] = 2
                    score = minimax(board, depth + 1, False)
                    board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = np.inf
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    board[row][col] = 1
                    score = minimax(board, depth + 1, True)
                    board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score


def best_move():
    best_score = -np.inf
    move = None
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
    if move != (-1, -1):
                    mark_square(move[0], move[1], 2)
                    return True
    return False




 