import pygame
import os
from .enemy import Enemy

class En_2(Enemy):

    imgs = [
        pygame.transform.scale(
            pygame.image.load(
                os.path.join("game_assets", "enemies", "2", "2_enemies_1_run_" + str(x) + ".png")),
            (64, 64)) for x in range(6)
        ]

    def __init__(self, speed):
        super().__init__(speed=speed)
