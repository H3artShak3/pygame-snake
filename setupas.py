import random

import pygame

screen_width = 512
screen_height = 512
logo = pygame.image.load("fabs/logo32x32.png")
back_list = ["fabs/back1.png", "fabs/back2.jpg", "fabs/back3.jpg", "fabs/back4.jpg"]
random_back = random.randint(0, 3)
background = pygame.image.load(back_list[random_back])
