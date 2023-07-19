import pygame
from game.components.enems.enem import Enem

class EnemManager:
    def __init__(self):
        self.enems = []

    def update (self):
        self.add_enem()

        for enemy in self.enems:
            enemy.update(self.enems)

    def draw(self, screen):
        for enem in self.enems:
            enem.draw(screen)

    def add_enem(self):
        if len(self.enems) < 1:
            enem = Enem()
            self.enems.append(enem)