import pygame
from pygame import mixer
import random
import time

# init pygame
pygame.init()

# define colors
white = (255, 255, 255)
green = (0, 100, 0)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
orange = (255, 165, 0)
aquamarine = (69, 139, 116)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)
gray = (38, 38, 38)

# display
width, height = 500, 500
bg = pygame.image.load('bg.png')

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snek Game")

clock = pygame.time.Clock()
snake_size = 10
snake_speed = 15
score = ()

# sound
mixer.music.load("bgm.wav")
mixer.music.play()

#fonts
message_font = pygame.font.SysFont('pixeboy', 60)
score_font = pygame.font.SysFont('pixeboy', 25)
title_font = pygame.font.SysFont('pixeboy', 35)
button_font = pygame.font.SysFont('pixeboy', 20)
game_font = pygame.font.SysFont('pixeboy', 60)


# start game menu
def text_objects(text, font):
    textSurface = button_font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, acolor, icolor, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(game_display, acolor, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "PLAY":
                game_instructions()
            elif action == "MENU":
                game_intro()
            elif action == "GO":
                mixer.music.load("bgm.wav")
                mixer.music.play(-1)
                game_modes()
            elif action == "TRAD":
                mixer.music.load("bgm.wav")
                mixer.music.play(-1)
                run_game()
            elif action == "BLEND":
                mixer.music.load("bgm.wav")
                mixer.music.play(-1)
                run_blend_game()
            elif action == "TUNNEL":
                mixer.music.load("bgm.wav")
                mixer.music.play(-1)
                run_tunnel_game()
            elif action == "REC":
                get_score_display()
            elif action == "RETURN":
                game_intro()
            elif action == "SCORES":
                display_scores()
            elif action == "BYE":
                pygame.quit()
                quit()

    else:
        pygame.draw.rect(game_display, icolor, (x, y, w, h))

    textobjfont = button_font.render('pixeboy', True, white)
    textSurf, textRect = text_objects(msg, textobjfont)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    game_display.blit(textSurf, textRect)


def game_intro():  # the initial display you can see
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(black)
        text = game_font.render("SNEK GAME ", True, white)
        game_display.blit(text, [120, 180])

        mouse = pygame.mouse.get_pos()
        # print (mouse)

        button("START", 190, 245, 120, 35, bright_green, white, "PLAY")
        button("LEADERBOARD", 190, 290, 120, 35, orange, white, "SCORES")
        button("QUIT", 190, 335, 120, 35, bright_red, white, "BYE")

        pygame.display.update()
        clock.tick(15)


def text_draw(text, font, color, x, y):
    font = font.render(text, True, color)
    game_display.blit(font, (x, y))


def game_modes():
    game_modes = True

    while game_modes:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(black)
        header_font = pygame.font.SysFont('pixeboy', 35)
        content_font = pygame.font.SysFont('pixeboy', 20)

        text_draw("CHOOSE A MODE", header_font, white, 150, 100)
        text_draw("The Traditional Snake Game", content_font, white, 155, 180)
        button("NORMAL MODE", 190, 200, 120, 35, bright_green, white, "TRAD")
        text_draw("BURP! Snek will blend in the background after eating!", content_font, white, 85, 255)
        button("BLEND MODE", 190, 275, 120, 35, orange, white, "BLEND")
        text_draw("WATCH OUT! Snek will tunnel to random places every 7 seconds", content_font, white, 50, 330)
        button("TUNNEL MODE", 190, 350, 120, 35, bright_red, white, "TUNNEL")
        text_draw("BSCS 2A - SEVILLENO, GABRIEL, MARMOLEJO, JUAYONG, VILLAR", button_font, gray, 33, 470)
        pygame.display.update()
        clock.tick(15)


def game_instructions():
    instructions = True

    while instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(black)
        header_font = pygame.font.SysFont('pixeboy', 35)
        content_font = pygame.font.SysFont('segoeuisymbol', 15)

        text_draw("HOW TO PLAY", header_font, white, 170, 100)
        text_draw("Use your keyboard's arrow keys to move.", content_font, white, 120, 130)
        text_draw("↑ - for up, ← - for left, → - for right, and ↓ - for down", content_font, white, 75, 150)

        text_draw("REMEMBER", header_font, white, 185, 200)
        text_draw("Do not hit the wall", content_font, white, 195, 230)
        text_draw("Do not eat your tail or body", content_font, white, 165, 250)
        text_draw("BSCS 2A - SEVILLENO, GABRIEL, MARMOLEJO, JUAYONG, VILLAR", button_font, gray, 33, 470)

        button("LET'S GO!", 190, 300, 120, 35, bright_green, white, "GO")

        pygame.display.update()
        clock.tick(15)


#misc functions
def print_score(score):
    text = score_font.render("Score: " + str(score), True, white)
    game_display.blit(text, [210, 50])

def print_title(text):
    text = title_font.render(text, True, white)
    game_display.blit(text, [180, 20])

def draw_snake(snake_size, snake_pixels):
    for pixels in snake_pixels:
        pygame.draw.rect(game_display, white, [pixels[0], pixels[1], snake_size, snake_size])

def run_game():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_lenght = 1

    target_x = round(random.randrange(50, width - snake_size) / 10.0) * 10
    target_y = round(random.randrange(50, height - snake_size) / 10.0) * 10

    while not game_over:

        while game_close:

            game_display.fill(black)
            game_over_message = message_font.render("GAME OVER!", True, red)
            game_display.blit(game_over_message, [170, 240])
            print_score(score)
            print_title("SNEK GAME")
            game_end()
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(black)
        game_display.blit(bg, (0,0))
        pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_lenght:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        draw_snake(snake_size, snake_pixels)
        print_score(snake_lenght - 1)
        print_title("SNEK GAME")
        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(50, width - snake_size) / 10.0) * 10
            target_y = round(random.randrange(50, height - snake_size) / 10.0) * 10
            snake_lenght += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


def run_blend_game():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_x = round(random.randrange(50, width - snake_size) / 10.0) * 10
    target_y = round(random.randrange(50, height - snake_size) / 10.0) * 10

    transparency_duration = 10  # in seconds
    time_since_last_target = 0

    while not game_over:

        while game_close:

            game_display.fill(black)
            game_over_message = message_font.render("GAME OVER!", True, red)
            game_display.blit(game_over_message, [170, 240])
            print_score(snake_length - 1)
            text = title_font.render("SNEK GAME: BLEND MODE", True, white)
            game_display.blit(text, [100, 20])
            game_end2()
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(black)
        game_display.blit(bg, (0, 0))
        pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        if time_since_last_target >= transparency_duration:
            draw_snake(snake_size, snake_pixels)
        else:
            # draw a transparent snake using a Surface with per-pixel alpha
            transparent_surface = pygame.Surface((snake_size, snake_size), pygame.SRCALPHA)
            transparent_surface.fill((000, 000, 000, 000))
            for pixel in snake_pixels:
                game_display.blit(transparent_surface, pixel)

        time_since_last_target += 1

        text = title_font.render("SNEK GAME: BLEND MODE", True, white)
        game_display.blit(text, [100, 20])
        print_score(snake_length - 1)
        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(50, width - snake_size) / 10.0) * 10
            target_y = round(random.randrange(50, height - snake_size) / 10.0) * 10
            snake_length += 1
            time_since_last_target = 0

        clock.tick(snake_speed)

    pygame.quit()
    quit()


def run_tunnel_game():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_x = round(random.randrange(50, width - snake_size) / 10.0) * 10
    target_y = round(random.randrange(50, height - snake_size) / 10.0) * 10

    last_spawn_time = time.time()
    score = 0

    while not game_over:

        while game_close:

            game_display.fill(black)
            game_over_message = message_font.render("GAME OVER!", True, red)
            game_display.blit(game_over_message, [170, 240])
            print_score(score)
            text = title_font.render("SNEK GAME: TUNNEL MODE", True, white)
            game_display.blit(text, [100, 20])
            game_end2()
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(black)
        game_display.blit(bg, (0, 0))
        pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        draw_snake(snake_size, snake_pixels)
        print_score(score)
        text = title_font.render("SNEK GAME: TUNNEL MODE", True, white)
        game_display.blit(text, [100, 20])
        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(50, width - snake_size) / 10.0) * 10
            target_y = round(random.randrange(50, height - snake_size) / 10.0) * 10
            snake_length += 1
            score += 1

        # Spawn snake in a new location every 5 seconds
        if time.time() - last_spawn_time >= 5:
            x = round(random.randrange(50, width - snake_size) / 10.0) * 10
            y = round(random.randrange(50, height - snake_size) / 10.0) * 10
            last_spawn_time = time.time()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

#gameover screen
def game_end():
    end = True

    mixer.music.load("gameend.wav")
    mixer.music.play()
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(black)
        text = message_font.render("GAME OVER", True, red)
        game_display.blit(text, [130, 170])

        mouse = pygame.mouse.get_pos()
        button("RESTART", 190, 225, 120, 35, bright_green, white, "PLAY")
        button("RECORD SCORE", 190, 270, 120, 35, orange, white, "REC")
        button("QUIT", 190, 360, 120, 35, bright_red, white, "BYE")
        button("LEADERBOARD", 190, 315, 120, 35, orange, white, "SCORES")
        pygame.display.update()
        clock.tick(15)

#gameover screen v2
def game_end2():
    end = True

    mixer.music.load("gameend.wav")
    mixer.music.play()
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(black)
        text = message_font.render("GAME OVER", True, red)
        game_display.blit(text, [130, 170])

        mouse = pygame.mouse.get_pos()
        button("RESTART", 190, 225, 120, 35, bright_green, white, "PLAY")
        button("QUIT", 190, 270, 120, 35, bright_red, white, "BYE")
        pygame.display.update()
        clock.tick(15)

#Record Score Screen
def get_score(width, height):
    score = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    score = score[:-1]
                elif event.key == pygame.K_RETURN:
                    return score
                else:
                    score += event.unicode
        game_display.fill((0, 0, 0))
        text = button_font.render(f'Enter your score then press [enter]: {score}', True, (255, 255, 255))
        text_rect = text.get_rect(center=(255, 255))
        game_display.blit(text, text_rect)
        pygame.display.flip()

def get_score_display():
    score = get_score(320, 220)
    write_score(score)

    text = button_font.render("Successfully recorded.", True, white)
    text_rect = text.get_rect(center=(255, 255))

    game_display.fill(black)
    game_display.blit(text, text_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        mouse = pygame.mouse.get_pos()
        button("BACK", 205, 450, 120, 35, bright_green, white, "MENU")
        pygame.display.update()
        clock.tick(15)


#writing score to scores.txt file
def write_score(score):
    with open('scores.txt', 'a') as file:
        file.write(f'{score}\n')

#to read scores from scores.txt file
def read_scores():
    scores = []
    with open('scores.txt', 'r') as file:
        for line in file:
            scores.append(int(line.strip()))
    scores.sort(reverse=True)
    return scores

#leaderboard screen
def display_scores():
    scores = read_scores()
    game_display.fill(black)

    text = title_font.render("LEADERBOARD", True, white)
    game_display.blit(text, [160, 50])

    y = 150

    for score in scores:
        text = score_font.render(f'Score: {score}', True, white)
        text_rect = text.get_rect(center=(game_display.get_width() / 2, y))
        game_display.blit(text, text_rect)
        y += 30
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        mouse = pygame.mouse.get_pos()
        button("BACK", 190, 410, 120, 35, bright_green, white, "MENU")
        pygame.display.update()
        clock.tick(15)


game_intro()