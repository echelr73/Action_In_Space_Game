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


class enemy(pygame.sprite.Sprite):
    def __init__(self,speed):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 25))
        """pygame.draw.rect(self.image, red, self.image.get_rect(), 1)"""
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0,weight - self.rect.width),
                                         random.randint(0, 100 - self.rect.height))

        self.velocity_x = random.randint(1, speed)
        self.velocity_y = random.randint(1, speed)

    def update(self):
        self.rect.x -= self.velocity_x
        self.rect.y += self.velocity_y

        if self.rect.left < 0:
            self.velocity_x -= 1

        if self.rect.bottom > height:
            self.velocity_y -= 1

        if self.rect.top < 0:
            self.velocity_y += 1
        
        if self.rect.right > weight:
            self.velocity_x += 1
        
               
