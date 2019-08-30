import pygame
import os
import time
from .pointerTower import PointerTower
from .tower import Tower

class ArcherTowerLong(PointerTower):

    tower_imgs = [
        pygame.transform.scale(
            pygame.image.load(
                os.path.join("game_assets", "towers", "archertower_" + str(x + 1) + ".png")),
            (Tower.width, Tower.height)) for x in range(3)
    ]
    pointer_imgs = [
        pygame.transform.scale(
            pygame.image.load(
                os.path.join("game_assets", "towers", "archertower_pointer_" + str(x + 1) + ".png")),
            (PointerTower.pointer_width, PointerTower.pointer_height)) for x in range(1)
    ]

    def __init__(self, x, y):
        super().__init__(x, y)

        self.range = 600
        self.inRange = False  # is t he tower in range of at least one enemy
        self.timer = time.time()

        self.damage = 1

    def draw(self, win):
        super().draw(win)
        pygame.draw.circle(win, (0, 255, 0), (self.x, self.y), self.range, 4)

    def attack(self, enemies):
        """
        Attacks an enemy in the enemy list, modifies the list
        :param enemies: list of enemies
        :return: none
        """
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            if enemy.dying < 0:
                x = enemy.x
                y = enemy.y

                dsq = (self.x-x)**2 + (self.y-y)**2
                if dsq < self.range**2:
                    self.inRange = True
                    enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda e: (self.point_x-e.x)**2 + (self.point_y-e.y)**2)
        if len(enemy_closest) > 0:
            self.point_at((enemy_closest[0].x-enemy_closest[0].offset[0],
                           enemy_closest[0].y-enemy_closest[0].offset[1]))
            if time.time() - self.timer >= 0.5:
                self.timer = time.time()
                enemy_closest[0].hit(self.damage)
