import pygame


class Brick(pygame.sprite.Sprite):
    def __init__(self, position, color):
        pygame.sprite.Sprite.__init__(self)
        if color == 'orange':
            self.image = pygame.image.load('images/brick_orange.png')
        else:
            self.image = pygame.image.load('images/brick_yellow.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = position
