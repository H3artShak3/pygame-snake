import pygame
import pygame_gui

import pagrindinis
from models import get_stats, stats_add



def ivesti_username(logo, background, screen_width, screen_height):
    pygame.init()
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode((screen_width, screen_height))

    screen.blit(background, (0, 0))

    manager = pygame_gui.UIManager((screen_width, screen_height))
    text_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect(((screen_width / 2 - 150), (screen_height / 2 - 95)), (300, 50)), manager=manager,
        object_id='#main_text_entry')
    get_name_game_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(((screen_width / 2 - 100), (screen_height / 2 - 35)), (200, 50)),
        text='Patvirtinti username',
        manager=manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == get_name_game_button:
                    meniu(text_input.get_text(), logo, background, screen_width, screen_height)
                    is_running = False

            manager.process_events(event)

        manager.update(time_delta)

        screen.blit(background, (0, 0))
        manager.draw_ui(screen)

        pygame.display.update()


def meniu(username, logo, background, screen_width, screen_height):
    pygame.init()

    pygame.display.set_icon(logo)
    pygame.display.set_caption("Snake")

    screen = pygame.display.set_mode((screen_width, screen_height))

    screen.blit(background, (0, 0))

    manager = pygame_gui.UIManager((screen_width, screen_height))

    new_game_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(((screen_width / 2 - 100), (screen_height / 2 - 35)), (200, 50)),
        text='Pradėti naują žaidimą',
        manager=manager)
    stats_game_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(((screen_width / 2 - 100), (screen_height / 2 + 25)), (200, 50)),
        text='Parodyti statistiką',
        manager=manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == new_game_button:
                    pagrindinis.game(username, logo, background, screen_width, screen_height)
                    is_running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == stats_game_button:
                    stats_show(username, logo, background, screen_width, screen_height)
                    is_running = False
            manager.process_events(event)

        manager.update(time_delta)

        screen.blit(background, (0, 0))
        manager.draw_ui(screen)

        pygame.display.update()


def game_over(score, username, logo, background, screen_width, screen_height):
    pygame.init()

    pygame.display.set_icon(logo)
    pygame.display.set_caption("Snake")

    screen = pygame.display.set_mode((screen_width, screen_height))

    screen.blit(background, (0, 0))

    manager = pygame_gui.UIManager((screen_width, screen_height))
    font = pygame.font.Font('freesansbold.ttf', 32)

    tekstas = f"Vartotojo vardas: {username}\n Pasiektas skaičius: {int(score)}"
    text = font.render(tekstas, True, (0, 0, 128))

    text_rect = text.get_rect()
    text_rect.center = (screen_width / 2, screen_height / 2 - 150)
    screen.blit(text, text_rect)
    main_menu_game_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(((screen_width / 2 - 150), (screen_height / 2 - 35)), (300, 50)),
        text='Grįžti į pagrindinį meniu',
        manager=manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == main_menu_game_button:
                    stats_add(score, username)
                    meniu(username, logo, background, screen_width, screen_height)
                    is_running = False

            manager.process_events(event)

        manager.update(time_delta)

        screen.blit(background, (0, 0))
        screen.blit(text, text_rect)
        manager.draw_ui(screen)

        pygame.display.update()


def stats_show(username, logo, background, screen_width, screen_height):
    pygame.init()

    pygame.display.set_icon(logo)
    pygame.display.set_caption("Snake")

    screen = pygame.display.set_mode((screen_width, screen_height))

    screen.blit(background, (0, 0))

    manager = pygame_gui.UIManager((screen_width, screen_height))

    top_10 = get_stats()
    font = pygame.font.Font('freesansbold.ttf', 26)

    tekstas = "Username--Score--Date\n"
    i = 1
    for elem in top_10:
        tekstas = tekstas + str(i) + ") " + str(elem.user_name) + '   ' + str(elem.score) + '   ' + str(
            elem.data) + ';\n'
        i += 1

    text = font.render(tekstas, True, (0, 0, 128))

    text_rect = text.get_rect()
    text_rect.center = (screen_width / 2, screen_height / 2)
    screen.blit(text, text_rect)
    main_menu_game_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(((screen_width / 2 - 150), (screen_height - 60)), (300, 50)),
        text='Grįžti į pagrindinį meniu',
        manager=manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == main_menu_game_button:
                    meniu(username, logo, background, screen_width, screen_height)
                    is_running = False
            manager.process_events(event)

        manager.update(time_delta)

        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(40, 70, 440, 360))
        screen.blit(text, text_rect)
        manager.draw_ui(screen)

        pygame.display.update()
