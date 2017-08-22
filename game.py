import sys  # exit()
import time  # sleep()
import pygame

from ball import Ball
from paddle import Paddle
from wall import Wall

width = 640
height = 480
white_color = (255, 255, 255)

pygame.init()


def game_over():
    font = pygame.font.SysFont('Arial', 72)
    text = font.render('Game over :(', True, white_color)
    text_rect = text.get_rect()
    text_rect.center = [width / 2, height / 2]
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(3)
    sys.exit()


def show_score():
    font_score = pygame.font.SysFont('Consolas', 20)
    text_score = font_score.render(str(score).zfill(5), True, white_color)
    text_score_rect = text_score.get_rect()
    text_score_rect.topleft = [32, 30]

    font_title = pygame.font.SysFont('Consolas', 25)
    text_title = font_title.render('SCORE', True, white_color)
    text_title_rect = text_title.get_rect()
    text_title_rect.topleft = [10, 10]

    screen.blit(text_score, text_score_rect)
    screen.blit(text_title, text_title_rect)


def show_lives():

    font = pygame.font.SysFont('Consolas', 25)
    text = font.render(str(lives).zfill(2), True, white_color)
    text_rect = text.get_rect()
    text_rect.topleft = [width - 60, 15]

    heart = pygame.image.load('images/heart.png')
    heart_rect = heart.get_rect()
    heart_rect.topright = [width - 10, 10]

    screen.blit(text, text_rect)
    screen.blit(heart, heart_rect)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Breakout')
clock = pygame.time.Clock()
pygame.key.set_repeat(30)

ball = Ball(width, height)
paddle = Paddle(width, height)
wall = Wall(65, width)
score = 0
lives = 3
waiting = True

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            paddle.update(event)
            if waiting and event.key == pygame.K_SPACE:
                waiting = False
                if ball.rect.centerx < width / 2:
                    ball.speed = [3, -3]
                else:
                    ball.speed = [-3, -3]

    if waiting:
        ball.rect.midbottom = paddle.rect.midtop
    else:
        ball.update()

    if pygame.sprite.collide_rect(ball, paddle):
        ball.speed[1] = -ball.speed[1]

    collided_list = pygame.sprite.spritecollide(ball, wall, False)
    if collided_list:
        brick = collided_list[0]
        cx = ball.rect.centerx
        if cx < brick.rect.left or cx > brick.rect.right:
            ball.speed[0] = -ball.speed[0]
        else:
            ball.speed[1] = -ball.speed[1]
        wall.remove(brick)
        score += 10

    if ball.rect.top > height:
        lives -= 1
        waiting = True

    image = pygame.image.load('images/bg.png')
    screen.blit(image, image.get_rect())
    show_score()
    show_lives()

    screen.blit(ball.image, ball.rect)
    screen.blit(paddle.image, paddle.rect)
    wall.draw(screen)
    pygame.display.flip()

    if lives <= 0:
        game_over()
