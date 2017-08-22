import pygame

from brick import Brick


class Wall(pygame.sprite.Group):
    def __init__(self, number_of_bricks, width):
        pygame.sprite.Group.__init__(self)
        pos_x = 20
        pos_y = 70
        for i in range(number_of_bricks):
            color = 'orange'
            if i >= 45:
                color = 'yellow'
            brick = Brick((pos_x, pos_y), color)
            self.add(brick)
            pos_x += brick.rect.width
            i += 1
            if i == 15 or i == 30:
                pos_x = 20
                pos_y += brick.rect.height
            if i == 45:
                pos_x = 100
                pos_y += brick.rect.height
            if i == 56:
                pos_x = 140
                pos_y += brick.rect.height
