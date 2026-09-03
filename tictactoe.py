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
        pygame.draw.line(screen, color, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        pygame.draw.line(screen, color, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)

#Drawing figure
def draw_figures(color=WHITE):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]==1:
                pygame.draw.circle(screen, color, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, color, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4), (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4), CROSS_WIDTH)
                pygame.draw.line(screen, color, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4), (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4), CROSS_WIDTH)

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


def draw_desc_diagonal(player):
    color = RED if player == 1 else GREEN
    pygame.draw.line(screen, color, (0, 0), (WIDTH, HEIGHT), LINE_WIDTH)


def draw_horizontal_winning_line(row, player):
    color = RED if player == 1 else GREEN
    y = row * SQUARE_SIZE + SQUARE_SIZE // 2
    pygame.draw.line(screen, color, (0, y), (WIDTH, y), LINE_WIDTH)


def draw_vertical_winning_line(col, player):
    color = RED if player == 1 else GREEN
    x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    pygame.draw.line(screen, color, (x, 0), (x, HEIGHT), LINE_WIDTH)


def draw_asc_diagonal(player):
    color = RED if player == 1 else GREEN
    pygame.draw.line(screen, color, (0, HEIGHT), (WIDTH, 0), LINE_WIDTH)


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



def restart():
    screen.fill(BLACK)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0



draw_lines()

player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and player == 1:
            mouseX, mouseY = event.pos
            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                elif is_board_full():
                    game_over = True
                else:
                    player = 2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False

    # AI move happens once per frame, outside the event loop
    if player == 2 and not game_over:
        best_move()
        if check_win(2):
            game_over = True
        elif is_board_full():
            game_over = True
        else:
            player = 1

    if not game_over:
        screen.fill(BLACK)
        draw_lines()
        draw_figures()
    else:
        screen.fill(BLACK)
        draw_lines()
        draw_figures()
        font = pygame.font.Font(None, 36)
        if check_win(1):
            text = font.render("Player 1 wins!", True, GREEN)
        elif check_win(2):
            text = font.render("Player 2 wins!", True, RED)
        else:
            text = font.render("It's a draw!", True, GRAY)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    pygame.display.update()



 