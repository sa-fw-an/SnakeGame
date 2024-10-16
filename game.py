import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (80, 213, 50)
blue = (50, 153, 213)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game Using Pygame')

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    snake_block = 10

    speed = 10

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    score = 0


    while not game_over:

        while game_close:
            game_re(score)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and (x1_change == 0): 
                    x1_change = -snake_block
                    y1_change = 0
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and (x1_change == 0): 
                    x1_change = snake_block
                    y1_change = 0
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and (y1_change == 0):  
                    y1_change = -snake_block
                    x1_change = 0
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and (y1_change == 0):  
                    y1_change = snake_block
                    x1_change = 0


        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True


        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        for segment in snake_list:
            pygame.draw.rect(dis, bright_green, [segment[0], segment[1], snake_block, snake_block])


        score_font = pygame.font.SysFont("comicsansms", 25)
        value = score_font.render("Your Score: " + str(score), True, yellow)
        dis.blit(value, [0, 0])


        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score += 10


        pygame.time.Clock().tick(speed)

    quit_game()

def button(msg, x, y, w, h, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(dis, active_color, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(dis, inactive_color, (x, y, w, h))

    small_font = pygame.font.SysFont("comicsansms", 20)
    text = small_font.render(msg, True, black)
    text_rect = text.get_rect(center=(x + w / 2, y + h / 2))
    dis.blit(text, text_rect)


def quit_game():
    pygame.quit()
    quit()


def play_again():
    gameLoop()


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        dis.fill(black)
        us = pygame.font.SysFont("comicsansms", 15)
        val = us.render("By :Safwan Sayeed" ,True, white)
        dis.blit(val, [0, 0])
        large_font = pygame.font.SysFont("comicsansms", 60)
        intro_text = large_font.render("Snake Game", True, white)
        dis.blit(intro_text, (dis_width / 2 - intro_text.get_width() / 2, dis_height / 4))

        button("Start", 150, 450, 150, 50, green, bright_green, play_again)
        button("Quit", 550, 450, 150, 50, red, bright_red, quit_game)

        pygame.display.update()
        pygame.time.Clock().tick(20)


def game_re(sc):
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        dis.fill(black)
        us = pygame.font.SysFont("comicsansms", 15)
        val = us.render("By :Safwan Sayeed" ,True, white)
        dis.blit(val, [0, 0])
        large_font = pygame.font.SysFont("comicsansms", 60)
        intro_text = large_font.render("You Lost !!!", True, bright_red)
        dis.blit(intro_text, (dis_width / 2 - intro_text.get_width() / 2, dis_height / 4))
        score_font = pygame.font.SysFont("comicsansms", 25)
        score_msg = score_font.render("Your Score: " + str(sc), True, yellow)
        dis.blit(score_msg, [dis_width / 2 - intro_text.get_width() / 4, dis_height / 2])

        button("Play Again", 150, 450, 150, 50, green, bright_green, play_again)
        button("Quit", 550, 450, 150, 50, red, bright_red, quit_game)

        pygame.display.update()
        pygame.time.Clock().tick(20)

game_intro()
