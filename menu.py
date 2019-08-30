import pygame
import os
from button import Button


class Menu:
    img = None

    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = self.center_x - self.width/2
        self.y = self.center_y + self.height/2

        self.item_names = []
        self.buttons = []
        self.items = len(self.item_names)

    def click(self, pos):
        """
        Returns True if (x, y) is within the bounds of the tower
        :param pos (Int, Int)
        :return: Bool
        """
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[0] <= self.y + self.height

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        subwin = win.subsurface(self.img.get_rect(topleft=(self.x, self.y)))
        for b in self.buttons:
            b.draw(subwin)

    def add_button(self, img, name):
        """
        Incomplete method that should be extended by the subclass in order to arrange the buttons.
        :param img: Surface
        :param name: String
        :return: None
        """
        self.items += 1
        new_button = Button(x=0, y=0, img=img, name=name)
        self.buttons.append(new_button)
        self.item_names.append(new_button.name)
        # something done in a subclass

    def pass_click(self, pos):
        """
        Passes the mouse click along to each of its buttons to see if any of them are triggered by it, and if so,
        then do whatever needs to be done.
        :param pos: (Int, Int)
        :return: None
        """
        for b in self.buttons:
            if b.click(b, pos):
                b.do_click()


class HorizontalMenu(Menu):
    def __int__(self, x, y):
        super().__init__(x, y)

    def add_button(self, img, name):
        """
        Adds a button to the list of buttons and then repositions all buttons to be evenly spaced HORIZONTALLY
        :param img: Surface
        :param name: String
        :return: None
        """
        super().add_button(img, name)
        inc_x = self.width / (self.items + 1)
        # update the x-position of each button in our list
        for b in enumerate(self.buttons, 1):
            b[1].set_pos(x=inc_x*b[0], y=self.height/2)


class VerticalMenu(Menu):
    def __int__(self, x, y):
        super().__init__(x, y)

    def add_button(self, img, name):
        """
        Adds a button to the list of buttons and then repositions all buttons to be evenly spaced VERTICALLY
        :param img: Surface
        :param name: String
        :return: None
        """
        super().add_button(img, name)
        inc_y = self.height / (self.items + 1)
        # update the position of each button in our list
        for b in enumerate(self.buttons, 1):
            b[1].set_pos(x=self.width/2, y=inc_y * b[0])


class archerTowerMenu(HorizontalMenu):
    img = pygame.transform.scale(
                pygame.image.load(os.path.join("game_assets", "menu_bg.png")),
                (300, 64))
    btn_plus = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets", "button_plus.png")),
                    (64, 48))
    btn_sell = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets", "button_money.png")),
                    (64, 48))
    btn_info = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets", "button_info.png")),
                    (64, 48))

    def __init__(self, x, y):
        super().__init__(x, y)
        for name, btn in {"plus": self.btn_plus, "sell": self.btn_sell, "info": self.btn_info}.items():
            self.add_button(img=btn, name=name)


