from .pointerTower import PointerTower
import time

class AttackTower(PointerTower):

    def __int__(self, x, y):
        super().__init__(x, y)
        self.timer = time.time()
        self.inRange = False

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
        else:
            self.point_at((self.point_x, self.point_y - 1))
