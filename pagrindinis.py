import random

import pygame

from setupas import logo, background, screen_width, screen_height
from game_ui import ivesti_username, game_over


def game(username, logo, background, screen_width, screen_height):
    pygame.init()
    score = 0
    multiplier = 1
    game_speed = 300
    game_amplifier = 1

    pygame.display.set_icon(logo)
    pygame.display.set_caption("Snake")

    screen = pygame.display.set_mode((screen_width, screen_height))

    screen.blit(background, (0, 0))

    grid = pygame.image.load("fabs/grid.png")  # naudojamas laukas 20x20
    grid.set_alpha(100)
    screen.blit(grid, (45, 45))

    grid_border = pygame.image.load("fabs/grid_border.png")
    screen.blit(grid_border, (45, 45))

    score_pane = pygame.image.load("fabs/score.png")
    screen.blit(score_pane, (345, 10))

    arial_font = pygame.font.SysFont("arial", 25)
    scoreline = arial_font.render(str(score), False, (0, 0, 0))
    screen.blit(scoreline, (427, 12))
    snake_pos_x = 10
    snake_pos_y = 10
    snake_body_pos = []
    snake_direction = 1  # (1 - viršus, 2 - apačia, 3 - LEFT, 4 - RIGHT)
    snake_body = pygame.image.load("fabs/body.png")
    screen.blit(snake_body, (snake_pos_x * 21 + 47, snake_pos_y * 21 + 47))

    eat_pos_x = random.randint(0, 19)
    eat_pos_y = random.randint(0, 19)
    while snake_pos_x == eat_pos_x or snake_pos_y == eat_pos_y:
        eat_pos_x = random.randint(0, 19)
        eat_pos_y = random.randint(0, 19)
    eat = pygame.image.load("fabs/eat.png")
    screen.blit(eat, (eat_pos_x * 21 + 47, eat_pos_y * 21 + 47))

    pygame.display.flip()

    running = True

    while running:

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and snake_direction != 1:
                    snake_direction = 2
                elif event.key == pygame.K_UP and snake_direction != 2:
                    snake_direction = 1
                elif event.key == pygame.K_LEFT and snake_direction != 4:
                    snake_direction = 3
                elif event.key == pygame.K_RIGHT and snake_direction != 3:
                    snake_direction = 4

        pygame.time.delay(game_speed)
        if int(score / 100) == game_amplifier and score > 0:
            game_speed -= 20
            multiplier += 0.2
            score += 5
            game_amplifier += 1

        for elem in snake_body_pos:
            if snake_body_pos.index(elem) == 0:
                snake_body_pos.append([snake_pos_x, snake_pos_y])
                snake_body_pos.pop(0)

        if snake_pos_x == eat_pos_x and snake_pos_y == eat_pos_y:
            score += 10 * multiplier
            snake_body_pos.append([eat_pos_x, eat_pos_y])

            while snake_pos_x == eat_pos_x and snake_pos_y == eat_pos_y and ([eat_pos_x, eat_pos_y] in snake_body_pos):
                eat_pos_x = random.randint(0, 19)
                eat_pos_y = random.randint(0, 19)

        if snake_direction == 1:
            snake_pos_y = snake_pos_y - 1
        elif snake_direction == 2:
            snake_pos_y = snake_pos_y + 1
        elif snake_direction == 3:
            snake_pos_x = snake_pos_x - 1
        elif snake_direction == 4:
            snake_pos_x = snake_pos_x + 1

        if snake_pos_y == -1 or snake_pos_y == 20 or ([snake_pos_x, snake_pos_y] in snake_body_pos):
            running = False
            game_over(score, username, logo, background, screen_width, screen_height)
        if snake_pos_x == -1 or snake_pos_x == 20:
            running = False
            game_over(score, username, logo, background, screen_width, screen_height)

        screen.blit(background, (0, 0))
        screen.blit(score_pane, (345, 10))
        scoreline = arial_font.render(str(int(score)), False, (0, 0, 0))
        screen.blit(scoreline, (427, 10))
        screen.blit(grid, (45, 45))
        screen.blit(grid_border, (45, 45))
        screen.blit(eat, (eat_pos_x * 21 + 47, eat_pos_y * 21 + 47))

        for elem in snake_body_pos:
            screen.blit(snake_body, (elem[0] * 21 + 47, elem[1] * 21 + 47))
        screen.blit(snake_body, (snake_pos_x * 21 + 47, snake_pos_y * 21 + 47))
        pygame.display.flip()


ivesti_username(logo, background, screen_width, screen_height)
