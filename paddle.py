import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/platform.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = (self.WIDTH / 2, self.HEIGHT - 20)
        self.speed = [0, 0]

    def update(self, event):
        if event.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-10, 0]
        elif event.key == pygame.K_RIGHT and self.rect.right < self.WIDTH:
            self.speed = [10, 0]
        else:
            self.speed = [0, 0]
        self.rect.move_ip(self.speed)
