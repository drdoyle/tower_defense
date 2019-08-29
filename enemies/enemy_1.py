import pygame
import os
from .enemy import Enemy

class En_1(Enemy):

    imgs = [
        pygame.transform.scale(
            pygame.image.load(
                os.path.join("game_assets", "enemies", "1", "1_enemies_1_run_" + str(x) + ".png")),
            (64, 64)) for x in range(4)
    ]

    def __init__(self, speed):
        super().__init__(speed=speed)
        self.max_health = 1
        self.health = self.max_health

