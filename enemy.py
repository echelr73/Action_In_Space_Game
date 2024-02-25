import pygame
import random

# Screen dimensions
weight = 800
height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255) 
red = (255, 0, 0)   
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
H_FA2F2F = (250, 47, 47)

class enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        # Load and scale enemy image
        self.image = pygame.image.load("enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 25))
        # Uncomment line below to draw a red rectangle around the enemy for visualization
        """pygame.draw.rect(self.image, red, self.image.get_rect(), 1)"""
        self.rect = self.image.get_rect()
        # Randomize initial position within screen boundaries
        self.rect.center = (random.randint(0, weight - self.rect.width),
                            random.randint(0, 100 - self.rect.height))

        # Set random velocities within specified speed limit
        self.velocity_x = random.randint(1, speed)
        self.velocity_y = random.randint(1, speed)

    def update(self):
        # Move the enemy horizontally and vertically
        self.rect.x -= self.velocity_x
        self.rect.y += self.velocity_y

        # Adjust velocities if enemy hits screen boundaries
        if self.rect.left < 0:
            self.velocity_x -= 1

        if self.rect.bottom > height:
            self.velocity_y -= 1

        if self.rect.top < 0:
            self.velocity_y += 1
        
        if self.rect.right > weight:
            self.velocity_x += 1
