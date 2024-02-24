import pygame
import random

weight = 800
height = 600

black = (0, 0, 0)
white = (255, 255, 255) 
red = (255, 0, 0)   
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
H_FA2F2F = (250, 47, 47)

class bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (5, 15))
        """pygame.draw.rect(self.image, red, self.image.get_rect(), 1)"""
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        speed = 10
        self.rect.y -= speed
        if self.rect.top < 0:
            self.kill()