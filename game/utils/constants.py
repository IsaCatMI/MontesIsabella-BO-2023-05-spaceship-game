import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship1.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

SHIELD1 = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield1.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

GO = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))

EP = pygame.image.load(os.path.join(IMG_DIR, "Other/explosion.png"))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
SHIELD_1_TYPE = 'shield1'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship1.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
IMPROVED = pygame.image.load(os.path.join(IMG_DIR, 'Spaceship/improved.png'))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))

FONT_STYLE = 'freesansbold.ttf'