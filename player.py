import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, game, pos, width = 25, height = 50):
        """

        :type pos: tuple of ints
        """
        self.game = game
        pygame.sprite.Sprite.__init__(self)

        self.left, self.top = pos
        self.right = self.left + width
        self.bottom = self.top + height


        self.image = pygame.Surface([width,height])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(topleft=(pos[0], pos[1]))

        # define self constants for behavior use later
        self.can_jump = False
        self.max_jump = 100
        self.vy = 0
        self.dy = 0
        self.falling = False




    def jump(self):
        if self.can_jump:
            self.dy = self.max_jump


    def go_left(self):
        pass

    def go_right(self):
        pass

    def duck(self):
        pass

    def update(self):
        if