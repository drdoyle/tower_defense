import pygame
from pygame.constants import *
from math import sqrt


base_path = [(-10, 122),
             (639, 119), (649, 330), (872, 326), (868, 124), (1125, 130),
             (1132, 617), (326, 621), (332, 291), (22, 284),
             (-100, 287)  # last point is off the screen
             ]
path_threshold = 2

BASE_HEALTH = 1


class Enemy:
    imgs = []

    def __init__(self, speed, width=64, height=64):
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = BASE_HEALTH
        self.path = base_path  # list of nodes / checkpoints for enemy to move to
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.offset = (self.width / 2, self.height / 2)
        self.img = None
        self.speed = speed
        self.path_pos = 0  # starting at the beginning of the path

        self.flip_x = False
        self.flip_y = False

        # self.x0, self.x1, self.y0, self.y1 = (0, 0, 0, 0)
        #
        # self.move_counter = 0
        # self.mdist = 0

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        self.animation_count += 1
        if (self.animation_count // 10) >= len(self.imgs):
            self.animation_count = 0
        self.img = self.imgs[self.animation_count // 10]

        win.blit(pygame.transform.flip(self.img, self.flip_x, self.flip_y),
                 (self.x - self.offset[0], self.y - self.offset[1]))


    def collide(self, x_check, y_check):
        """
        Returns if position has hit enemy
        :param x_check: int
        :param y_check: int
        :return: Bool
        """
        if x_check <= self.x + self.width and x_check > self.x:
            if y_check <= self.y + self.height and y_check >= self.y:
                return True
        return False

    def move(self):
        """
        Move enemy
        :return: None
        """
        tar_x, tar_y = self.path[self.path_pos + 1]

        dirn = [tar_x - self.x, tar_y - self.y]  # basic vector
        dist_to_path = dirn[0]**2 + dirn[1]**2  # squared distance

        dirn = [dirn[0]*abs(dirn[0]) / dist_to_path, dirn[1]*abs(dirn[1]) / dist_to_path]  # squared norm
        change_x = self.speed * dirn[0]
        change_y = self.speed * dirn[1]
        self.flip_x = change_x < 0
        # self.flip_y = change_y < 0  # included but never implemented, self.flip_y is always False
        self.x += change_x
        self.y += change_y

        if dirn[0] >= 0 and dirn[1] >= 0:  # moving down-right
            if self.x > tar_x or self.y > tar_y:
                self.path_pos += 1
        elif dirn[0] <= 0 and dirn[1] >= 0:  # moving down-left
            if self.x < tar_x or self.y > tar_y:
                self.path_pos += 1
        elif dirn[0] >= 0 and dirn[1] <= 0:  # moving up-right
            if self.x > tar_x or self.y < tar_y:
                self.path_pos += 1
        elif dirn[0] <= 0 and dirn[1] <= 0:  # moving up-left
            if self.x < tar_x or self.y < tar_y:
                self.path_pos += 1

    # def move_slope(self):
    #     """
    #     New move function that linearly interpolates between path points
    #     :return:
    #     """
    #
    #     if self.move_counter <= 0:
    #         self.set_moveslope()
    #
    #     self.x = self.x1 - (self.x1-self.x0)/self.mdist * self.move_counter
    #     self.y = self.y1 - (self.y1-self.y0)/self.mdist * self.move_counter
    #     self.move_counter -= 1
    #
    # def set_moveslope(self):
    #     self.path_pos += 1
    #     self.x0, self.y0 = self.path[self.path_pos - 1]
    #     self.x1, self.y1 = self.path[self.path_pos]
    #     self.mdist = sqrt((self.x1 - self.x0) ** 2 + (self.y1 - self.y0) ** 2)
    #     self.move_counter = self.mdist / self.speed
    #     self.path_pos += 1

    def hit(self):
        """
        Removes one health from the enemy/self.
        Returns True if enemy has no remaining health, else False
        :return: Bool
        """
        self.health -= 1
        if self.health <= 0:
            return True
        return False

    def draw_path(self, win):
        """
        Debugging function that displays all the points for the enemy
        :return: None
        """
        for p in self.path:
            pygame.draw.circle(win, (255, 0, 0), (p[0], p[1]), 5, 0)
