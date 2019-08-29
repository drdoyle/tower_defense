import pygame
import os
from .enemy import Enemy

class En_2(Enemy):



    def __init__(self, speed):
        super().__init__(speed=speed)
        self.max_health = 3
        self.health = self.max_health
        self.imgs = [
            pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_assets", "enemies", "2", "2_enemies_1_run_" + str(x) + ".png")),
                (64, 64)) for x in range(4)
        ]
