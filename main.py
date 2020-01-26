import pygame
from random import randrange
from random import choice
from digits import *

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
pink = (234, 136, 234)
gray = (128, 128, 128)

# Initialize the game
pygame.init()

# Create the screen
screen_dim_x = 1000
screen_dim_y = 900
screen = pygame.display.set_mode((screen_dim_x, screen_dim_y))
pygame.display.set_caption("PySnake")

# Initial snake position
snake_x_init = randrange(250, 750, 50)  # former 100 and 900
snake_y_init = randrange(200, 500, 50)  # former 100 and 650

# Initial snake movement direction
snake_vel_dir = choice(['x', 'y'])
snake_vel = choice([-50, 50])

# Snake velocity after direction change
snake_vel_pos = 50
snake_vel_neg = -50

# Snake position
snake_x = []
snake_y = []
snake_x.append(snake_x_init)
snake_y.append(snake_y_init)

# Eaten bait counter
count = 0

# Frame dimensions
frame_x = 950
frame_y = 700
frame_width_lr = 25
frame_width_ud = frame_x - 50
frame_height_lr = frame_y
frame_height_ud = 25

# Inner canvas dimensions
canvas_x = frame_x - 50
canvas_y = frame_y - 50


# Draw the snake
def draw_snake(snake_x, snake_y):
    pygame.draw.rect(screen, pink, (snake_x, snake_y, 50, 50))


def draw_frame(frame_x, frame_y):
    #pygame.draw.rect(screen, gray, (25, 25, frame_x, frame_y))
    pygame.draw.rect(screen, gray, (25, 25, frame_width_lr, frame_height_lr))
    pygame.draw.rect(screen, gray, (frame_x, 25, frame_width_lr, frame_height_lr))
    pygame.draw.rect(screen, gray, (50, 25, frame_width_ud, frame_height_ud))
    pygame.draw.rect(screen, gray, (50, frame_y, frame_width_ud, frame_height_ud))


def draw_brim():
    pygame.draw.rect(screen, white, (0, 0, frame_width_lr, frame_height_lr + 50))
    pygame.draw.rect(screen, white, (frame_x + 25, 0, frame_width_lr, frame_height_lr + 50))
    pygame.draw.rect(screen, white, (25, 0, frame_width_ud + 50, frame_height_ud))
    pygame.draw.rect(screen, white, (25, frame_y + 25, frame_width_ud + 50, frame_height_ud))


# def draw_one(digit_x, digit_y):
#     pygame.draw.rect(screen, black, (digit_x, digit_y, 25, 125))


# Draw the bait
bait_x_size = 50
bait_y_size = 50

snake_x_bait = snake_x_init
snake_y_bait = snake_y_init

turn_index = 0


def bait_pos(snake_x_bait, snake_y_bait):
    bait_x_values = list(range(100, 900, 50))
    bait_y_values = list(range(100, 650, 50))
    bait_x_values.remove(snake_x_bait)
    bait_y_values.remove(snake_y_bait)

    bait_x_pos = choice(bait_x_values)
    bait_y_pos = choice(bait_y_values)

    return bait_x_pos, bait_y_pos


def draw_bait(bait_x_pos, bait_y_pos, bait_x_size, bait_y_size):
    pygame.draw.rect(screen, black, (bait_x_pos, bait_y_pos, bait_x_size, bait_y_size))


# Initial bait position
bait_x = bait_pos(snake_x_init, snake_y_init)[0]
bait_y = bait_pos(snake_x_init, snake_y_init)[1]

# Direction lists
turn_vel_dir_list = []
turn_vel_list = []
turn_vel_dir_list.append(snake_vel_dir)
turn_vel_list.append(snake_vel)

# Number of times the loop ran
cycle_count = 0

# Memory if key was pressed
key_down = False

button_already_pushed = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if key_down == False:
            print(event)
            if event.type == pygame.KEYDOWN:
                # turn_index = 0
                # turn_vel_dir = snake_vel_dir
                # turn_vel = snake_vel
                # key_down = True
                # button_already_pushed = False
                if event.key == pygame.K_RIGHT and turn_vel_dir_list[-1] != 'x':
                    # snake_vel_dir = 'x'
                    # snake_vel = snake_vel_pos
                    turn_vel_dir_list.append('x')
                    turn_vel_list.append(snake_vel_pos)
                    key_down = True
                # if event.key == pygame.K_RIGHT and turn_vel_dir_list[-1] == 'x':
                #     key_down = False
                if event.key == pygame.K_DOWN and turn_vel_dir_list[-1] != 'y':
                    # snake_vel_dir = 'y'
                    # snake_vel = snake_vel_pos
                    turn_vel_dir_list.append('y')
                    turn_vel_list.append(snake_vel_pos)
                    key_down = True
                # if event.key == pygame.K_DOWN and turn_vel_dir_list[-1] == 'y':
                #     key_down = False
                if event.key == pygame.K_LEFT and turn_vel_dir_list[-1] != 'x':
                    # snake_vel_dir = 'x'
                    # snake_vel = snake_vel_neg
                    turn_vel_dir_list.append('x')
                    turn_vel_list.append(snake_vel_neg)
                    key_down = True
                # if event.key == pygame.K_LEFT and turn_vel_dir_list[-1] == 'x':
                #     key_down = False
                if event.key == pygame.K_UP and turn_vel_dir_list[-1] != 'y':
                    # snake_vel_dir = 'y'
                    # snake_vel = snake_vel_neg
                    turn_vel_dir_list.append('y')
                    turn_vel_list.append(snake_vel_neg)
                    key_down = True
            # if event.key == pygame.K_UP and turn_vel_dir_list[-1] == 'y':
            #     key_down = False

    if key_down is False:
        if cycle_count > 0:
            turn_vel_dir_list.append(turn_vel_dir_list[-1])
            turn_vel_list.append(turn_vel_list[-1])

    key_down = False

    pygame.time.Clock().tick(30)

    screen.fill((255, 255, 255))

    # draw_frame(frame_x, frame_y)
    # draw_inner_canvas(canvas_x, canvas_y)
    # draw_nine(screen, black, 75, 750)
    #draw_digit(screen, black, 9)

    draw_bait(bait_x, bait_y, bait_x_size, bait_y_size)

    for i in range(1, len(snake_x) + 1):
        # print('Snake X: ', snake_x[i - 1], i)
        # print('Snake Y: ', snake_y[i - 1], i)
        if turn_vel_dir_list[-i] == 'x':
            snake_x[i - 1] += turn_vel_list[-i]
        else:
            snake_y[i - 1] += turn_vel_list[-i]

    len_snake = len(list(zip(snake_x, snake_y)))
    number_single_snake_elements = len(list(set(zip(snake_x, snake_y))))

    if number_single_snake_elements < len_snake:
        running = False
    if any(i < 50 for i in snake_x) or any(i > 900 for i in snake_x):
        running = False
    if any(i < 50 for i in snake_y) or any(i > 650 for i in snake_y):
        running = False

    for i in range(0, len(snake_x)):
        draw_snake(snake_x[i], snake_y[i])

    draw_brim()
    draw_frame(frame_x, frame_y)

    # for i in range(0, len(snake_x)):
    #     if i <= turn_index:
    #         if snake_vel_dir == 'x':
    #             snake_x[i] += snake_vel
    #         else:
    #             snake_y[i] += snake_vel
    #     else:
    #         if turn_vel_dir == 'x':
    #             snake_x[i] += turn_vel
    #         else:
    #             snake_y[i] += turn_vel

    print(turn_vel_dir_list)
    print(turn_vel_list)
    print(cycle_count)
    # print(snake_x)
    # print(snake_y)

    # for i in range(1, len(snake_x) + 1):
    #     # print('Snake X: ', snake_x[i - 1], i)
    #     # print('Snake Y: ', snake_y[i - 1], i)
    #     if turn_vel_dir_list[-i] == 'x':
    #         snake_x[i - 1] += turn_vel_list[-i]
    #     else:
    #         snake_y[i - 1] += turn_vel_list[-i]

    turn_index += 1

    # if turn_index > len(snake_x):
    #     turn_index = len(snake_x)
    # print(turn_index)

    if snake_x[0] == bait_x and snake_y[0] == bait_y:
        count += 1
        # print('Snake ate the bait! - ', count)

        bait_x = bait_pos(snake_x[0], snake_y[0])[0]
        bait_y = bait_pos(snake_x[0], snake_y[0])[1]

        if turn_vel_dir_list[-count] == 'x':
            snake_x.append(snake_x[-1] - turn_vel_list[-count])
            snake_y.append(snake_y[-1])
        else:
            snake_x.append(snake_x[-1])
            snake_y.append(snake_y[-1] - turn_vel_list[-count])

    cycle_count += 1

    draw_score(count, screen, black)

    if len(turn_vel_dir_list) > len(snake_x):
        turn_vel_dir_list.pop(0)
        turn_vel_list.pop(0)

    pygame.display.update()
