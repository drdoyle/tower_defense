import pygame


class Button:
    def __init__(self, x, y, img, name):
        self.name = name
        self.img = img
        self.center_x = x
        self.center_y = y
        self.width = self.img.get_width()
        self.height = self.height.get_width()

        self.x = self.center_x - self.width/2
        self.y = self.center_y - self.height/2

    def click(self, pos):
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height

    def do_click(self):
        """
        Placeholder function that will be overwritten by individual buttons' functionality.
        :return: None
        """
        return NotImplementedError

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def set_pos(self, x, y):
        """
        Changes the x-position of the center of the button to a new value
        :param x: Int
        :return: None
        """
        self.center_x = x
        self.center_y = y
        self.x = self.center_x - self.width/2
        self.y = self.center_y - self.height / 2


class Menu:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0

        self.item_names = []
        self.buttons = []
        self.imgs = []
        self.items = len(self.item_names)

    def click(self, pos):
        """
        Returns True if (x, y) is within the bounds of the tower
        :param pos (Int, Int)
        :return: Bool
        """
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[0] <= self.y + self.height

    def draw(self, win):
        for b in self.buttons:
            b.draw(win)

    def add_button(self, img, name):
        self.items += 1
        new_button = Button(x=0, y=0, img=img, name=name)
        self.buttons.append(new_button)
        # something done in a subclass

    def get_clicked(self, pos):
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
        inc_x = self.width / self.items
        # update the x-position of each button in our list
        for b in enumerate(self.buttons):
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
        inc_y = self.height / self.items
        # update the position of each button in our list
        for b in enumerate(self.buttons):
            b[1].set_pos(x=self.width/2, y=inc_y * b[0])