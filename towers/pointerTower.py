import pygame

from math import degrees, atan2
from .tower import Tower


class PointerTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.pointer_imgs = []
        self.pointer_width = 32
        self.pointer_height = 32
        self.point_x = self.x - self.pointer_width / 2
        self.point_y = self.y - self.pointer_height / 2 - self.offset[0]
        self.angle = 0
        self.pointer_count = 0

    def point_at(self, pos):
        """
        Aims the pointer at the top of the tower at its target. Updates self.angle
        :param pos: tuple of ints
        :return: None
        """
        self.angle = degrees(atan2(-pos[1] + self.point_y,
                                   pos[0] - self.point_x)) - 90

    def draw(self, win):
        super().draw(win)

        self.pointer_count += 1
        if self.pointer_count >= len(self.pointer_imgs)*10:
            self.pointer_count = 0
        point_img = self.pointer_imgs[self.pointer_count // 10]

        win.blit(pygame.transform.rotate(point_img, self.angle),
                 (self.point_x, self.point_y))