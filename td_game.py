import pygame
import sys

# Constants
from pygame.constants import *
from player import Player

WIN_WIDTH = 800
WIN_HEIGHT = 600
BACKGROUND_COLOR = (0, 255, 255)

pygame.init()


class Game:
    def __init__(self):
        pygame.display.set_caption("TD Game Demo")

        self.clock = pygame.time.Clock()
        self.last_tick = pygame.time.get_ticks()
        self.screen_res = (WIN_WIDTH, WIN_HEIGHT)

        self.font = pygame.font.SysFont("Impact", 55)
        self.screen = pygame.display.set_mode(self.screen_res, pygame.HWSURFACE, 32)

        # load all the sprites into their bins
        self.entities = pygame.sprite.Group()
        self.solids = pygame.sprite.Group()
        self.player = Player(game=self, pos=(50, 50))

        self.entities.add(self.solids)
        self.entities.add(self.player)

        self.clock.tick()

        # define self.variables that will be set later
        self.ttime = None
        self.mpos = None
        self.keys_pressed = None

        while True:
            self.update()

    def update(self):
        self.event_loop()

        self.tick()
        self.draw()
        pygame.display.update()

    def tick(self):
        self.ttime = self.clock.tick()
        self.mpos = pygame.mouse.get_pos()
        self.keys_pressed = pygame.key.get_pressed()

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.player.update(self.ttime/1000.)

        for e in self.entities:
            e.image.blit(self.screen, (e.left, e.top))

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_w:
                    self.player.jump()
                if event.key == K_a:
                    self.player.go_left():
                if event.key == K_d:
                    self.player.go_right():
                if event.key == K_s:
                    self.player.duck():



# class Block(Game, pygame.Surface):
#
#     def __init__(self, color: tuple, width: int, height: int):
#         self.image = pygame.Surface([width, height])
#         self.image.fill(color)
#
#         self.rect = self.image.get_rect()
#
#     def update(self):
#         self.image.blit(dest=screen)

if __name__ == "__main__":
    Game()
