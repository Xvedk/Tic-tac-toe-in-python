import pygame as pg
import sys
import time

# Define global variables
XO = 'x'
winner = None
draw = None
width = 400
height = 400
white = (255, 255, 255)
line_color = (0, 0, 0)
board = [[''] * 3 for _ in range(3)]

# Initialize pygame
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe")

# Load and scale images
initiating_window = pg.transform.scale(pg.image.load("modified_cover.png"), (width, height + 100))
x_img = pg.transform.scale(pg.image.load("X_modified.png"), (80, 80))
o_img = pg.transform.scale(pg.image.load("o_modified.png"), (80, 80))

def game_initiating_window():
    screen.blit(initiating_window, (0, 0))
    pg.display.update()
    time.sleep(3)
    screen.fill(white)
    for i in range(1, 3):
        pg.draw.line(screen, line_color, (0, i * height // 3), (width, i * height // 3), 7)
        pg.draw.line(screen, line_color, (i * width // 3, 0), (i * width // 3, height), 7)
    draw_status()

def draw_status():
    global draw
    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won !"
    if draw:
        message = "Game Draw !"
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()

def check_win():
    global board, winner, draw
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != '':
            winner = board[row][0]
            pg.draw.line(screen, (250, 0, 0), (0, (row + 1) * height // 3 - height // 6),
                         (width, (row + 1) * height // 3 - height // 6), 4)
            break
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            winner = board[0][col]
            pg.draw.line(screen, (250, 0, 0), ((col + 1) * width // 3 - width // 6, 0),
                         ((col + 1) * width // 3 - width // 6, height), 4)
            break
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        winner = board[0][0]
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        winner = board[0][2]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)
    if all(all(row) for row in board) and winner is None:
        draw = True
    draw_status()

def drawXO(row, col):
    global board, XO
    x_y_coordinates = [(90, 90), (210, 90), (330, 90), (90, 210), (210, 210), (330, 210), (90, 330), (210, 330), (330, 330)]
    if board[row-1][col-1] == '' and not (winner or draw):
        board[row-1][col-1] = XO
        screen.blit(x_img if XO == 'x' else o_img, x_y_coordinates[(row - 1) * 3 + col - 1])
        XO = 'o' if XO == 'x' else 'x'
        pg.display.update()

def reset_game():
    global board, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_initiating_window()
    winner = None
    board = [[''] * 3 for _ in range(3)]

game_initiating_window()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            user_click()
            if winner or draw:
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)

