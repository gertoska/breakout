import sys  # exit()
import time  # sleep()
import pygame

ANCHO = 640
ALTO = 480
blue_color = (0, 0, 64)
white_color = (255, 255, 255)

pygame.init()


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2
        self.speed = [3, 3]

    def update(self):
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        self.rect.move_ip(self.speed)


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/platform.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = (ANCHO / 2, ALTO - 20)
        self.speed = [0, 0]

    def update(self, event):
        if event.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-10, 0]
        elif event.key == pygame.K_RIGHT and self.rect.right < ANCHO:
            self.speed = [10, 0]
        else:
            self.speed = [0, 0]
        self.rect.move_ip(self.speed)


class Brick(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/brick.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = position


class Wall(pygame.sprite.Group):
    def __init__(self, numberOfBricks):
        pygame.sprite.Group.__init__(self)

        pos_x = 0
        pos_y = 20
        for i in range(numberOfBricks):
            brick = Brick((pos_x, pos_y))
            self.add(brick)
            pos_x += brick.rect.width
            if pos_x >= ANCHO:
                pos_x = 0
                pos_y += brick.rect.height


def game_over():
    font = pygame.font.SysFont('Arial', 72)
    text = font.render('Game over :(', True, white_color)
    text_rect = text.get_rect()
    text_rect.center = [ANCHO / 2, ALTO / 2]
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(3)
    sys.exit()


def show_score():
    font = pygame.font.SysFont('Consolas', 20)
    text = font.render(str(score).zfill(5), True, white_color)
    text_rect = text.get_rect()
    text_rect.topleft = [0, 0]
    screen.blit(text, text_rect)


def show_lives():
    font = pygame.font.SysFont('Consolas', 20)
    string = "Lives: " + str(lives).zfill(2)
    text = font.render(string, True, white_color)
    text_rect = text.get_rect()
    text_rect.topright = [ANCHO, 0]
    screen.blit(text, text_rect)


screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Breakout')
clock = pygame.time.Clock()
pygame.key.set_repeat(30)

ball = Ball()
paddle = Paddle()
wall = Wall(50)
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
            if waiting == True and event.key == pygame.K_SPACE:
                waiting = False
                if ball.rect.centerx < ANCHO / 2:
                    ball.speed = [3, -3]
                else:
                    ball.speed = [-3, -3]

    if waiting:
        ball.rect.midbottom = paddle.rect.midtop
    else:
        ball.update()

    if pygame.sprite.collide_rect(ball, paddle):
        ball.speed[1] = -ball.speed[1]

    list = pygame.sprite.spritecollide(ball, wall, False)
    if list:
        brick = list[0]
        cx = ball.rect.centerx
        if cx < brick.rect.left or cx > brick.rect.right:
            ball.speed[0] = -ball.speed[0]
        else:
            ball.speed[1] = -ball.speed[1]
        wall.remove(brick)
        score += 10

    if ball.rect.top > ALTO:
        lives -= 1
        waiting = True

    screen.fill(blue_color)
    show_score()
    show_lives()

    screen.blit(ball.image, ball.rect)
    screen.blit(paddle.image, paddle.rect)
    wall.draw(screen)
    pygame.display.flip()

    if lives <= 0:
        game_over()
