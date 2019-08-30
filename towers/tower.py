import pygame
from math import atan2, degrees

class Tower:
    """
    Abstract class for towers to set up inheritance
    """
    width = 64
    height = 64

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.offset = (self.width / 2, self.height / 2)

        self.range = 100

        self.sell_price = [0, 0, 0]
        self.buy_price = [0, 0, 0]
        self.level = 0
        self.selected = False
        self.menu = None

    def draw(self, win):
        """
        Draws the tower to the window
        :param win: Surface
        :return: None
        """
        win.blit(self.tower_imgs[self.level], (self.x - self.offset[0], self.y - self.offset[1]))

    def click(self, x_c, y_c):
        """
        Returns True if tower has been clicked on, if tower was clicked on selects tower
        :param x_c: float
        :param y_c: float
        :return: bool
        """
        if x_c <= self.x + self.width and x >= self.x:
            if y_c <= self.y + self.height and y_c >= self.y:
                return True
        return False

    def sell(self):
        """
        Call to sell the tower, returns the sell price.
        :return:
        """
        return self.sell_price[self.level]

    def upgrade(self):
        """
        Upgrades the tower for a given cost
        :return:
        """
        pass

    def get_upgrade_cost(self):
        """
        Returns the upgrade cost. Returns -1 if it can't upgrade further
        :return:
        """

    def get_sell_price(self):
        """
        Returns the sell cost. Returns -1 if at base level.
        :return: int
        """
        try:
            price = self.sell_price[self.level]
        except IndexError:
            return -1
        else:
            return price

    def move(self):
        pass

    def set_range(self, newrange):
        """
        Setter for the range of the tower.
        :param newrange: int
        :return: None
        """
        self.range = newrange
