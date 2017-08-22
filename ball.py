import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.WIDTH / 2
        self.rect.centery = self.HEIGHT / 2
        self.speed = [3, 3]

    def update(self):
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= self.WIDTH or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        self.rect.move_ip(self.speed)
