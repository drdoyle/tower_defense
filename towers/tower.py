import pygame


class Tower:
    """
    Abstract class for towers to set up inheritance
    """
    width = 64
    height = 64

    # <editor-fold desc="These class lists are included to make the code look prettier,
    # each subclass should have its own class list">
    tower_imgs = []

    base_damage = 0
    base_range = 0
    damage_list = []
    range_list = []

    upgrade_costs = [0]  # always have 0 at the end to signal that it can't be upgraded any further
    sell_price = []
    buy_price = []
    # </editor-fold>

    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y
        self.offset = (self.width / 2, self.height / 2)
        self.x = self.center_x - self.offset[0]
        self.y = self.center_y - self.offset[1]

        self.level = 0
        self.selected = False
        self.menu = None
        self.to_delete = False

        self.damage = self.base_damage
        self.range = self.base_range
        self.img = self.tower_imgs[self.level]

    def draw(self, win):
        """
        Draws the tower to the window
        :param win: Surface
        :return: None
        """
        win.blit(self.img, (self.x, self.y))
        if self.selected is True:
            # draw range indicator
            pygame.draw.circle(win, (0, 255, 0), (self.center_x, self.center_y), self.range, 4)
            # draw menus
            # for m in self.menu:
            #     m.draw()

    def click(self, pos):
        """
        Returns True if tower has been clicked on.
        :param pos: (Int, Int)
        :return: bool
        """
        return self.x + self.width >= pos[0] >= self.x and self.y + self.height >= pos[1] >= self.y

    def sell(self):
        """
        Call to sell the tower, returns the sell price. Flags the tower for deletion during the next cleanup step.
        :return:
        """
        self.to_delete = True
        return self.sell_price[self.level]

    def upgrade(self):
        """
        Upgrades the tower for a given cost; overwritten by subclasses
        :return:
        """
        return NotImplementedError  # should never return this, included to catch if we forgot to override

    def get_upgrade_cost(self):
        """
        Returns the upgrade cost. Returns -1 if it can't upgrade further
        :return: Int
        """
        return self.upgrade_costs[self.level]

    def get_sell_price(self):
        """
        Returns the sell cost. Returns -1 if at base level.
        :return: int
        """

        return self.sell_price[self.level]

    def move(self):
        pass

    def set_range(self, new_range):  # TODO: is this method necessary?
        """
        Setter for the range of the tower, primarily used in self.upgrade()
        :param new_range: Int
        :return: None
        """
        if new_range <= 0:
            raise ValueError("Variable new_range must be positive.")
        self.range = new_range

    def change_range(self, range_boost):
        """
        Changer for the range of the tower, to allow for things like support towers which passively
        boost the range of towers around them. Negative range_boosts decrease the range.
        :param range_boost: Int
        :return: None
        """
        self.range = max(0, self.range + range_boost)  # caps the range from below so it never becomes negative

    def change_damage(self, dmg_boost):
        """
        Changer for the damage of the tower, to allow for support towers. Negative boosts decrease damage.
        :param dmg_boost: Int
        :return: None
        """
        self.damage = max(0, self.damage + dmg_boost)

    def upgrade(self):
        """
        Applies all of the changes to the tower associated with going up a level
        :return:
        """
        self.level += 1
        self.change_damage(self.damage_list[self.level])
        self.change_range(self.range_list[self.level])
        self.img = self.tower_imgs[self.level]