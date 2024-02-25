# Import necessary modules
from asyncio import events
from enemy import enemy
from bullet import bullet
import pygame
import random
import time

# Define global variables
weight = 800
height = 600
life = 3
level = 1
kills = 0

fps = 120

# Define fonts and colors
font_console = pygame.font.match_font("consolas")
font_times = pygame.font.match_font("times")
font_arial = pygame.font.match_font("arial")
font_courier = pygame.font.match_font("courier")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
H_FA2F2F = (250, 47, 47)

# Player class
class player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Load player image
        self.image = pygame.image.load("player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 70))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.cadency = 300
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        # Update player position according to pressed keys
        speed = 8
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += speed
        if keys[pygame.K_SPACE]:
            # Control shooting cadence
            now = pygame.time.get_ticks()
            if now - self.last_shot > self.cadency:
                self.last_shot = now
                self.shoot()
        # Restrict player position within the screen
        if self.rect.right >= weight:
            self.rect.right = weight
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
    
    def shoot(self):
        # Method for player shooting
        bullet_ = bullet(self.rect.centerx, self.rect.centery - 40)
        bullets.add(bullet_)
        laser_sound.play()

# Initialization class
class init():
    pygame.init()

# Load sounds and adjust volume
laser_sound = pygame.mixer.Sound("laser.wav")
laser_sound.set_volume(0.5)
kill_sound = pygame.mixer.Sound("point.wav")
crash_sound = pygame.mixer.Sound("crash.wav")
finish_sound = pygame.mixer.Sound("finish.wav")

ambient_sound = pygame.mixer.Sound("background_sound.mp3")

# Play background sound in loop and adjust volume
ambient_sound.play(-1)
ambient_sound.set_volume(0.4)

# Screen configuration
screen = pygame.display.set_mode((weight, height))
background = pygame.transform.scale(pygame.image.load("background.jpg").convert(),(1000, 600))
pygame.display.set_caption("Space Invaders")

# Initialize game clock
clock = pygame.time.Clock()

# Create player
player1 = player(weight/2, height-125)
players = pygame.sprite.Group()
players.add(player1)
bullets = pygame.sprite.Group()

# Function to make enemies appear
def enemy_appear(speed):
    enemy_ = enemy(speed)
    enemys.add(enemy_)

# Function to render text
def text_objects(text, font, screen, color, x, y,size):
    font_Text = pygame.font.Font(font, size)
    textSurface = font_Text.render(text, True, color)
    screen.blit(textSurface, (x, y))

# Function to handle game over
def game_over():
    finish_sound.play()
    text_objects("Game Over", font_console, screen, red, (weight - 400) // 2, (height - 100) // 2, 100)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()

# Group of enemies
enemys = pygame.sprite.Group()

# Main game loop
running = True
while running:
    clock.tick(fps)
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Show game information on screen
    text_objects("Life: " + str(life), font_arial, screen, white, 10, 10, 20)
    text_objects("Level: " + str(level), font_arial, screen, white, 10, 30, 20)
    text_objects("Kills: " + str(kills), font_arial, screen, white, 10, 50, 20)

    # Update and draw elements on screen
    players.draw(screen)
    player1.update()
    bullets.draw(screen)
    bullets.update()
    enemys.draw(screen)
    enemys.update()
    
    # Generate enemies according to the level
    if level == 1:
        if len(enemys) < 1:
            enemy_appear(5)
    if level == 2:
        if len(enemys) < 2:
            for i in range(2):
                enemy_appear(10)
    if level == 3:
        if len(enemys) < 5:
            for i in range(5):
                enemy_appear(10)
    if level == 4:
        if len(enemys) < 10:
            for i in range(10):
                enemy_appear(10)
    
    # Detect collisions between bullets and enemies
    for bullet_ in bullets:
        collisions = pygame.sprite.spritecollide(bullet_, enemys, True)
        for enemy_ in collisions:
            kill_sound.play()
            bullet_.kill()
            kills += 1
    
    # Detect collisions between enemies and player
    for enemy_ in enemys:
        if enemy_.rect.colliderect(player1.rect):
            crash_sound.play()
            enemy_.kill()
            life -= 1
        if life == 0:
            game_over()
            running = False
    
    # Increase level and adjust shooting cadence based on the number of enemies eliminated
    if kills == 10:
        level = 2
        player1.cadency = 200
    if kills == 20:
        level = 3
        player1.cadency = 100
    if kills == 40:
        level = 4
        player1.cadency = 50

    pygame.display.flip()
