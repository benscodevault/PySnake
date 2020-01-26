import pygame

dx = 75
dy = 750

pixel_height = 25
pixel_width = 25

digit_elem_coord = [
    [[dx, dy], [dx, dy + 25], [dx, dy + 50], [dx, dy + 75], [dx, dy + 100], [dx - 25, dy + 100], [dx - 50, dy + 100],
     [dx - 50, dy + 75], [dx - 50, dy + 50], [dx - 50, dy + 25], [dx - 50, dy], [dx - 25, dy]],

    [[dx, dy], [dx, dy + 25], [dx, dy + 50], [dx, dy + 75], [dx, dy + 100]],

    [[dx - 50, dy], [dx - 25, dy], [dx, dy], [dx, dy + 25], [dx, dy + 50], [dx - 25, dy + 50], [dx - 50, dy + 50],
     [dx - 50, dy + 75], [dx - 50, dy + 100], [dx - 25, dy + 100], [dx, dy + 100]],

    [[dx - 50, dy], [dx - 25, dy], [dx, dy], [dx, dy + 25], [dx, dy + 50], [dx, dy + 75], [dx, dy + 100],
     [dx - 50, dy + 50], [dx - 25, dy + 50], [dx - 50, dy + 100], [dx - 25, dy + 100]],

    [[dx - 50, dy], [dx - 50, dy + 25], [dx - 50, dy + 50], [dx - 25, dy + 50], [dx, dy], [dx, dy + 25], [dx, dy + 50],
     [dx, dy + 75], [dx, dy + 100]],

    [[dx, dy], [dx - 25, dy], [dx - 50, dy], [dx - 50, dy + 25], [dx - 50, dy + 50], [dx - 25, dy + 50], [dx, dy + 50],
     [dx, dy + 75], [dx, dy + 100], [dx - 25, dy + 100], [dx - 50, dy + 100]],

    [[dx, dy], [dx - 25, dy], [dx - 50, dy], [dx - 50, dy + 25], [dx - 50, dy + 50], [dx - 50, dy + 75],
     [dx - 50, dy + 100], [dx - 25, dy + 100], [dx, dy + 100], [dx, dy + 75], [dx, dy + 50], [dx - 25, dy + 50]],

    [[dx - 50, dy], [dx - 25, dy], [dx, dy], [dx, dy + 25], [dx, dy + 50], [dx, dy + 75], [dx, dy + 100]],

    [[dx, dy], [dx, dy + 25], [dx, dy + 50], [dx, dy + 75], [dx, dy + 100], [dx - 25, dy + 100], [dx - 50, dy + 100],
     [dx - 50, dy + 75], [dx - 50, dy + 50], [dx - 50, dy + 25], [dx - 50, dy], [dx - 25, dy], [dx - 25, dy + 50]],

    [[dx, dy], [dx, dy + 25], [dx, dy + 50], [dx, dy + 75], [dx, dy + 100], [dx - 25, dy + 100], [dx - 50, dy + 100],
     [dx - 50, dy + 50], [dx - 50, dy + 25], [dx - 50, dy], [dx - 25, dy], [dx - 25, dy + 50]]]


def draw_score(count, screen, black):
    if count < 10:
        # def draw_digit(screen, black, digit):
        for i in range(0, len(digit_elem_coord[count])):
            pygame.draw.rect(screen, black, (tuple(digit_elem_coord[count][i]) + (pixel_height, pixel_width)))
    elif count < 100:
        ten = count // 10
        one = count % 10
        for i in range(0, len(digit_elem_coord[ten])):
            pygame.draw.rect(screen, black, (tuple(digit_elem_coord[ten][i]) + (pixel_height, pixel_width)))

        for i in range(0, len(digit_elem_coord[one])):
            pygame.draw.rect(screen, black, (
                    tuple([(e[0] + 100, e[1]) for e in digit_elem_coord[one]][i]) + (pixel_height, pixel_width)))
