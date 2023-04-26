import pygame
import random
import time


#init pygame
pygame.init()

#define colors
white = (255, 255, 255)
black = (0,100,0) #green ito atm
red = (255, 0, 0)
orange = (255, 165, 0)

width, height = 500, 500


game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Glaiza forever!")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('pixeboy', 40)
score_font = pygame.font.SysFont('pixeboy', 25)
title_font = pygame.font.SysFont('pixeboy', 35)


def print_score(score):
    text = score_font.render("Score: " + str(score), True, white)
    game_display.blit(text, [210,50])

def print_title():
    text = title_font.render("SNEK GAME ", True, white)
    game_display.blit(text, [180,20]) 

def display_image():
    image = pygame.image.load("ufo.png")
    game_display.blit(image, [50,10])

def draw_snake (snake_size, snake_pixels):
    for pixels in snake_pixels: 
        pygame.draw.rect(game_display, white, [pixels[0], pixels[1], snake_size, snake_size])

def run_game():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed= 0
    y_speed = 0

    snake_pixels = []
    snake_lenght = 1

    target_x = round(random.randrange(50, width-snake_size) / 10.0) *10
    target_y = round(random.randrange(50, height-snake_size) / 10.0) *10

    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("GAME OVER!", True, red)
            game_display.blit(game_over_message, [170, 240])
            print_score(snake_lenght - 1)
            print_title()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

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

        if x>= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(black)
        pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_lenght:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        display_image()
        print_title()
        draw_snake(snake_size, snake_pixels)
        print_score(snake_lenght - 1)
        print_title()

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(50, width-snake_size) / 10.0) *10
            target_y = round(random.randrange(50, height-snake_size) / 10.0) *10
            snake_lenght += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

run_game()
            
        

                
            
                
