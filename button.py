class Button:
    def __init__(self, x, y, img, name):
        self.name = name
        self.img = img
        self.center_x = x
        self.center_y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()

        self.x = self.center_x - self.width/2
        self.y = self.center_y - self.height/2

    def click(self, pos):
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height

    def do_click(self):
        """
        Placeholder function that will be overwritten by individual buttons' functionality.
        :return: None
        """
        pass

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def set_pos(self, x, y):
        """
        Changes the x-position of the center of the button to a new value
        :param x: Int
        :param y: Int
        :return: None
        """
        self.center_x = x
        self.center_y = y
        self.x = self.center_x - self.width/2
        self.y = self.center_y - self.height / 2


class StateButton(Button):
    def __init__(self, x, y, img, name, off_img):
        super().__init__(x, y, img, name)
        self.imgs = {True: img, False: off_img}
        self.on = True

    def do_click(self):
        """
        Switches off to on or on to off, and changes the sprite image between on/off states. Should be called as a
        super().do_click() in subclasses to run before the "real" click execution code of a StateButton subclass.
        :return: None
        """
        self.on = not self.on
        self.img = self.imgs[self.on]
        # do the rest of the clicking code
