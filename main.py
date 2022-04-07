import pygame
from pygame.locals import *

# Initialize game
pygame.init()
clock = pygame.time.Clock()
screen_surface = pygame.display.set_mode((1500, 1000))

# Colors
black = 0, 0, 0
white = 255, 255, 255
green = 154, 205, 50
red = 255, 0, 0
yellow = 255, 255, 0
pink = 255, 153, 153
blue = 0, 0, 255

# Background surface
background = pygame.Surface(screen_surface.get_size())
background.fill(black)

# Surface where the red square is moving
surf_square_select = pygame.Surface(screen_surface.get_size())
surf_square_select.set_colorkey((0, 0, 0))

# Red square positions
square_red_x, square_red_y = 100, 100

# Function that creates the map
def creating_map(connector_to_process):
    not_empty = 0
    square_x, square_y = 100, 100
    der = 255, 0, 0
    welloy = 255, 255, 0
    orange = 255, 165, 0
    for y in connector_to_process:
        square_x = 100
        for x in y:
            pygame.draw.rect(background, blue, (square_x, square_y, 100, 100), 0)
            square_x += 100
            if x == 1 or x == 2:
                not_empty += 1
                if count == 42:
                    while True:
                        for t in pygame.event.get():
                            if t.type == QUIT:
                                quit()

                        font = pygame.font.Font('ARCADECLASSIC.TTF', 64)

                        text = font.render('No    one    has    won', True, orange)

                        background.blit(text, (100, 800))
                        screen_surface.blit(background, (0, 0))
                        pygame.display.update()
                if x == 1:
                    pygame.draw.circle(background, der, (square_x - 50, square_y + 50), 47.5)

                else:
                    pygame.draw.circle(background, welloy, (square_x - 50, square_y + 50), 47.5)
            else:
                pygame.draw.circle(background, black, (square_x - 50, square_y + 50), 47.5)

        square_y += 100


# Function that checks if 4 coins are in a row (right, down, down-right, down-left)
def check_4win(ye, num):
    mHeight = len(ye)
    mWidth = len(ye[0])

    for y in range(mHeight):
        for x in range(mWidth - 3):
            if ye[y][x] == num and ye[y][x + 1] == num and ye[y][x + 2] == num and ye[y][x + 3] == num:
                return True

    for x in range(mWidth):
        for y in range(mHeight - 3):
            if ye[y][x] == num and ye[y + 1][x] == num and ye[y + 2][x] == num and ye[y + 3][x] == num:
                return True

    for x in range(mWidth - 3):
        for y in range(mHeight - 3):
            if ye[y][x] == num and ye[y + 1][x + 1] == num and ye[y + 2][x + 2] == num and ye[y + 3][x + 3] == num:
                return True

    for x in range(mWidth):
        for y in range(mHeight - 3):
            if x >= 0:
                if ye[y][x] == num and ye[y + 1][x - 1] == num and ye[y + 2][x - 2] == num and ye[y + 3][x - 3] == num:
                    return True


def turn_player(posx, posy, matrix):  # Put the coin at the right place and check if someone won
    global alternate, count, check
    n = 6
    while True:  # Check each time if you can put your coin there
        n -= 1
        x = int(posx / 100) - 1
        y = int(posy / 100) - 1 + n
        chose = alternate % 2

        if y < 0:
            pygame.display.set_caption("You can't put your coin there!")
            alternate -= 1
            break

        if matrix[y][x] == 0:
            pygame.display.set_caption("")
            if chose == 1:
                count = 1
                matrix[y][x] += 2
            else:
                count = 0
                matrix[y][x] += 1
            creating_map(matrix)
            if check_4win(matrix, matrix[y][x]):
                while True:
                    for evnt in pygame.event.get():
                        if evnt.type == QUIT:
                            quit()

                    key = pygame.key.get_pressed()
                    font = pygame.font.Font('ARCADECLASSIC.TTF', 64)

                    if chose == 1:
                        text = font.render('Yellow   Player    Won!', True, yellow)
                    else:
                        text = font.render('Red   Player    Won!', True, red)

                    if key[K_RETURN]:
                        check = 0
                        break

                    text2 = font.render('Press   ENTER  to  restart', True, yellow)
                    background.blit(text2, (700, 700))
                    background.blit(text, (100, 800))
                    screen_surface.blit(background, (0, 0))
                    pygame.display.update()
            break
        else:
            pass

while True:
    alternate = 0
    count = 0
    check = 1
    screen_surface.fill(black)
    matrix = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    background.fill(black)
    creating_map(matrix)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()

        key = pygame.key.get_pressed()
        font = pygame.font.Font('ARCADECLASSIC.TTF', 54)
        text = font.render('Who   wants   to   begin', True, blue)
        text2 = font.render('Press  R  if  red  player  wants  to  begin', True, red)
        text3 = font.render('Press  y  if  yellow  player  wants to begin', True, yellow)

        if key[K_r]:
            alternate += 1
            count += 1
            break

        if key[K_y]:
            break

        screen_surface.blit(text, (240, 100))
        screen_surface.blit(text2, (0, 200))
        screen_surface.blit(text3, (0, 300))
        pygame.display.flip()

    # Game loop
    while True:
        # If the player wants to quit, no error will be shown
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()

        key = pygame.key.get_pressed()  # Pygame module for inputs

        rectangle = pygame.Rect(square_red_x, square_red_y, 100, 100)  # Dedicate a location for the square

        surf_square_select.fill((0, 0, 0, 0))  # Erase the old square (only hiding it with a black screen)

        if key[K_RIGHT]:  # Change position of the red square (right movement)
            square_red_x += 100
            if square_red_x == 800:
                square_red_x = 100

        if key[K_LEFT]:  # Change position of the red square (left movement)
            square_red_x -= 100
            if square_red_x == 0:
                square_red_x = 700

        if key[K_r] and count == 1 and check > 5:  # Check if it's the turn of the red player
            alternate += 1
            turn_player(square_red_x, square_red_y, matrix)

        if key[K_y] and count == 0 and check > 5:  # Check if it's the turn of the yellow player
            alternate += 1
            turn_player(square_red_x, square_red_y, matrix)

        if check == 0:
            break
        check += 1

        pygame.draw.rect(surf_square_select, red, rectangle, 7)  # Draw the red square depending on rectangle

        screen_surface.blit(background, (0, 0))
        screen_surface.blit(surf_square_select, (0, 0))
        clock.tick(10)  # Setting game speed (FPS)
        pygame.display.flip()


