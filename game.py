"""
Responsible for running the game, transitioning between menus
"""

import pygame
import os
import time
import random
from pygame.constants import *  # import constants like QUIT or K_W
from enemies.enemy_1 import En_1
from enemies.enemy_2 import En_2
from towers.archerTower import ArcherTowerLong


# New defined constants to change aspects of the game
WIN_W = 1280
WIN_H = 800
STARTING_LIVES = 10
STARTING_MONEY = 0

class Game:

    def __init__(self):
        self.width = WIN_W
        self.height = WIN_H
        self.win = pygame.display.set_mode((self.width, self.height))

        # list of entities
        self.enemies = [En_1(speed=2), En_2(speed=1)]  # TODO: create maploader that generates spawns
        self.towers = [ArcherTowerLong(x=1000, y=200)]
        self.lives = STARTING_LIVES
        self.money = STARTING_MONEY

        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clock = pygame.time.Clock()
        self.timer = time.time()

    def run(self):
        running = True
        self.clock.tick(60)

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

                pos = pygame.mouse.get_pos()

                if event.type == MOUSEBUTTONDOWN:
                    pass

            # if time.time() - self.timer >= 1.50:
            #      self.enemies.append(random.choice((En_2(speed=2), En_2(speed=2.5))))
            #      self.timer = time.time()

            to_del = []

            for tow in self.towers:
                tow.attack(self.enemies)

            for en in self.enemies:
                en.move()
                if en.x < - en.width \
                        or en.y < -en.height \
                        or en.x > self.width + en.width \
                        or en.y > self.height + en.height\
                        or en.to_delete is True:
                    to_del.append(en)

            for d in to_del:
                self.enemies.remove(d)

            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))

        entlist = [item for list_ in [self.towers, self.enemies] for item in list_]
        for ent in sorted(entlist, key=lambda e: e.x):
            ent.draw(self.win)

        pygame.display.update()


game = Game()
game.run()
