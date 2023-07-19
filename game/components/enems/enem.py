import pygame
import random
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH

class Enem(Sprite):
    ENEM_WIDTH = 40
    ENEM_HEIGHT = 60
    Y_POS = 2
    X_POS_RANGE = [20, 120, 220, 320, 420, 520, 620, 720, 820, 920]
    SPEED_ON_Y = 5
    SPEED_ON_X = 5
    MOVES = { 0: 'left', 1: 'right' }

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.ENEM_WIDTH, self.ENEM_HEIGHT))
        self.rect = self.image.get_rect(midtop = (random.choice(self.X_POS_RANGE), self.Y_POS))
        self.direction = self.MOVES[random.randint(0, 1)]
        self.movement_count = 0
        self.moves_before_change = random.randint(20, 60)

    def update(self, enems):
        self.rect.y += self.SPEED_ON_Y

        if self.direction == self.MOVES[0]:
            self.rect.x -= self.SPEED_ON_X
        elif self.direction == self.MOVES[1]:
            self.rect.x += self.SPEED_ON_X

        self.handle_direction()

        if self.rect.top > SCREEN_HEIGHT:
            enems.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_direction(self):
        self.movement_count += 1

        if (self.movement_count >= self.moves_before_change and self.direction == self.MOVES[1]) or self.rect.right >= SCREEN_WIDTH:
            self.direction = self.MOVES[0]
        elif self.movement_count >= self.moves_before_change and self.direction == self.MOVES[0] or self.rect.left <= 0:
            self.direction = self.MOVES[1]
        
        if (self.movement_count >= self.moves_before_change):
            self.movement_count = 0
