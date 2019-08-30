import pygame
import os
from .pointerTower import PointerTower
from .attackTower import AttackTower
from .tower import Tower


class ArcherTowerLong(AttackTower):

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

    base_damage = 1
    base_range = 200
    damage_list = [0, 2, 3]
    range_list = [0, 200, 200]
    upgrade_costs = [100, 300, 0]  # 0 at the end to signal that it can't be upgraded any further

    def __init__(self, x, y):
        super().__init__(x, y)
