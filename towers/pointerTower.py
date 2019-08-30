import pygame

from math import degrees, atan2
from .tower import Tower


class PointerTower(Tower):
    pointer_width = 32
    pointer_height = pointer_width * 2  # to keep proportionate scaling of sprite

    # <editor-fold desc="Class variable that should be overwritten by subclass, included for prettiness">
    pointer_imgs = []
    # </editor-fold>

    def __init__(self, x, y):
        super().__init__(x, y)
        self.point_x = self.x
        self.point_y = self.y - self.offset[1] + 10  # plus 10 is arbitrary
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
        """
        Draws the tower by calling the super().draw function, and then draws
        the pointer on top of the tower, rotated by self.angle degrees.

        :param win: Surface
        :return: None
        """
        super().draw(win)

        self.pointer_count += 1
        if self.pointer_count >= len(self.pointer_imgs)*10:
            self.pointer_count = 0
        point_img = self.pointer_imgs[self.pointer_count // 10]

        point_img = pygame.transform.rotate(point_img, self.angle)
        pi_topleft = point_img.get_rect(center=(self.point_x, self.point_y)).topleft
        win.blit(point_img,  pi_topleft)
