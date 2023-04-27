import pygame
from pygame import mixer
import random
import time


#init pygame
pygame.init()

#define colors
white = (255, 255, 255)
greent = (0,100,0) #green ito atm
black = (0,0,0) #green ito atm
red = (200, 0, 0)
green = (0, 200, 0)
orange = (255, 165, 0)
aquamarine = (69,139,116)

bright_green = (0, 255, 0)
bright_red = (255, 0, 0)

width, height = 500, 500

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Glaiza forever!")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

#sound
mixer.music.load("tetris.wav")
mixer.music.play()

message_font = pygame.font.SysFont('pixeboy', 60)
score_font = pygame.font.SysFont('pixeboy', 25)
title_font = pygame.font.SysFont('pixeboy', 35)
button_font = pygame.font.SysFont('pixeboy', 20)
game_font = pygame.font.SysFont('pixeboy', 60)

#start game menu

def text_objects (text, font):
    textSurface = button_font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button (msg, x, y, w, h, acolor, icolor, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse [0] > x and y + h > mouse[1] > y:   
        pygame.draw.rect (game_display, acolor, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "PLAY":
               
                mixer.music.load("tetris.wav")
                mixer.music.play(-1)
                run_game()
            elif action == "BYE":
                mixer.music.load("click.wav")
                mixer.music.play()
                pygame.quit()
                quit()
    else:
        pygame.draw.rect (game_display, icolor, (x, y, w, h))
    
    textobjfont = button_font.render ('pixeboy', True, white)
    textSurf, textRect = text_objects(msg, textobjfont)
    textRect.center = ((x + (w/2)), (y + (h/2)))    
    game_display.blit(textSurf, textRect)
    
def game_intro (): #the initial display you can see
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
                
        game_display.fill(black)
        text = game_font.render("SNEK GAME ", True, white)
        game_display.blit(text, [140,180])

        mouse = pygame.mouse.get_pos()
        #print (mouse)
        
        button ("START", 205, 245, 100, 35, bright_green, white, "PLAY")
        button ("QUIT", 205, 290, 100, 35, bright_red, white, "BYE")
        
        pygame.display.update()
        clock.tick(15) 


def game_end (): #the initial display you can see
    intro = True
    
    mixer.music.load("gameend.wav")
    mixer.music.play()
    while intro:
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
        
        game_display.fill(black)
        text = message_font.render("GAME OVER", True, red)
        game_display.blit(text, [140,180])
        
        mouse = pygame.mouse.get_pos()
        #print (mouse)
        

        button ("RESTART", 205, 245, 100, 35, bright_green, white, "PLAY")
        button ("QUIT", 205, 290, 100, 35, bright_red, white, "BYE")
        
        pygame.display.update()
        clock.tick(15)   

#sound def


#start menu code ends here

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
            game_end()
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
    
game_intro()
run_game()
