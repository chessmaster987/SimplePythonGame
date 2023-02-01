import pygame
import random

# initialize pygame
pygame.init()

# game window size
width = 1200
height = 720

# create game window
screen = pygame.display.set_mode((width, height))

# player square
square_x = width // 2
square_y = height // 2
square_size = 50
square_speed = 1

# list to store circles
circles = []

# generate random circles  
for i in range(5):
    x = random.randint(0, width - 50)
    y = random.randint(0, height - 50)
    r = random.randint(20, 50)
    circles.append([x, y, r, 0, 0, random.randint(1, 5)])

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= square_speed
    if keys[pygame.K_RIGHT]:
        square_x += square_speed
    if keys[pygame.K_UP]:
        square_y -= square_speed
    if keys[pygame.K_DOWN]:
        square_y += square_speed

    # make the square wrap around the screen
    if square_x >= width:
        square_x = 0
    if square_x < 0:
        square_x = width - square_size
    if square_y >= height:
        square_y = 0
    if square_y < 0:
        square_y = height - square_size

    # fill screen with color
    screen.fill((255, 255, 255))

    # draw square
    pygame.draw.rect(screen, (0, 0, 0), (square_x, square_y, square_size, square_size))

    # update and draw circles
    for i, (x, y, r, dx, dy, dr) in enumerate(circles):
        x += dx
        y += dy
        r += dr
        if x + 2 * r >= width or x <= 0:
            dx = -dx
        if y + 2 * r >= height or y <= 0:
            dy = -dy
        if r >= 50 or r <= 20:
            dr = -dr
        circles[i] = [x, y, r, dx, dy, dr]
        pygame.draw.circle(screen, (255, 0, 0), (x + r, y + r), r, 0)

    # check collision with circles
    for x, y, r, _, _, _ in circles:
        if (square_x < x + 2 * r) and (square_x + square_size > x) and (square_y < y + 2 * r) and (square_y + square_size > y):
            running = False

    # update screen
    pygame.display.update()

# quit pygame
pygame.quit()
