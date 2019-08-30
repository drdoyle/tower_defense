import pygame


class Projectile:

    # <editor-fold desc="Class variables to prettify and be overwritten by subclasses">
    proj_imgs = []
    speed = 1
    # </editor-fold>
    length = 32
    width = 16

    def __init__(self, start, target):
        '''
        Creates a projectile at position start that moves towards target.
        :param start: (Int, Int)
        :param target: Enemy
        '''
        self.center_x, self.center_y = start
        self.tar_x = target.x
        self.tar_y = target.y

        self.offset = (self.x, self.y - self.width / 2)  # offset to the middle of the side
        self.x = self.center_x - self.offset[0]
        self.y = self.center_y - self.offset[1]

        self.flip_x = False
        self.flip_y = False  # likely static, included for completeness
        self.animation_count = 0

    def move(self):
        """
        Updates the position of the projectile by stepping it towards the target according to its speed.
        Based on the enemy.draw() function, but using a set target rather than a path.
        :return: None
        """
        dirn = [self.tar_x - self.center_x, self.tar_y - self.center_y]  # basic vector
        dist_to_tar = dirn[0] ** 2 + dirn[1] ** 2  # squared distance for normalization

        dirn = [dirn[0] * abs(dirn[0]) / dist_to_tar, dirn[1] * abs(dirn[1]) / dist_to_tar]  # squared norm
        change_x = self.speed * dirn[0]
        change_y = self.speed * dirn[1]
        self.flip_x = change_x < 0
        # self.flip_y = change_y < 0  # included but never implemented, self.flip_y is always False
        self.update_pos(change_x, change_y)

    def update_pos(self, dx, dy):
        """
        Changes self.(x,y) and self.center_(x,y) by (dx,dy), both in place.
        :param dx: Float
        :param dy: Float
        :return: None
        """
        self.x += dx
        self.y += dy
        self.center_x = self.x + self.offset[0]
        self.center_y = self.y + self.offset[1]

    def draw(self, win):
        self.animation_count += 1
        if self.animation_count >= len(self.proj_imgs)*10:
            self.animation_count = 0
        img = self.proj_imgs[self.animation_count // 10]

        win.blit(pygame.transform.flip(img, self.flip_x, self.flip_y),
                 (self.x - self.offset[0], self.y - self.offset[1]))
