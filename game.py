"""
Responsible for running the game, transitioning between menus
"""

import pygame
import os
from pygame.constants import *  # import constants like QUIT or K_W
from enemies.enemy_1 import En_1
from enemies.enemy_2 import En_2


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
        self.towers = []
        self.lives = STARTING_LIVES
        self.money = STARTING_MONEY

        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clock = pygame.time.Clock()

        self.clicks = []  # debugging list

        self.entities = []  # one list to iterate over for drawing and updating
        self.entities.append(self.enemies)
        self.entities.append(self.towers)


    def run(self):
        running = True
        self.clock.tick(60)

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

                pos = pygame.mouse.get_pos()

                if event.type == MOUSEBUTTONDOWN:
                    self.clicks.append(pos)

            to_del = []
            for en in self.enemies:
                en.move()
                if en.x < - en.width or en.y < -en.height or en.x > self.width + en.width or en.y > self.height + en.height:
                    to_del.append(en)

            for d in to_del:
                self.enemies.remove(d)

            self.draw()
        print(self.clicks)

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))
        # for p in self.clicks:  #
        #     pygame.draw.circle(self.win, (255, 0, 0), (p[0], p[1]), 5, 0)


        for en in self.enemies:
            en.draw(self.win)
            # en.draw_path(self.win)  # debugging function to investigate paths
        pygame.display.update()


game = Game()
game.run()
