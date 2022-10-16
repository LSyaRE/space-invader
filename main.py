import math

import pygame
import random

# Initialize the pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('./assets/images/icon.png')
pygame.display.set_icon(icon)


def load_image(directory: str = ''):
    return pygame.image.load(directory)


player = {
    "img": load_image('assets/images/ships/spaceship/Spaceship_Green64.gif'),
    "x": 370,
    "y": 480,
    "x_change": 0.0,
    "y_change": 0.0
}

enemy = {
    "img": load_image('assets/images/enemies/enemy.png'),
    "x": random.randint(0, 600),
    "y": random.randint(50, 150),
    "x_change": 0.3,
    "y_change": 40.0
}

bullet = {
    "img": load_image('assets/images/bullets/black_shoot.png'),
    "x": 0,
    "y": 480,
    "x_change": 0.3,
    "y_change": 10.0,
    "state": "ready"
}

keys = {
    pygame.K_LEFT,
    pygame.K_RIGHT,
    pygame.K_UP,
    pygame.K_DOWN
}

background = load_image('assets/images/backgrounds/space-background.jpg')

xLimit = {
    0: 0,
    740: 740
}

yLimit = {
    0: 0,
    540: 540
}

score = 0

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    return False if distance < 27 else True


def player_screen(x, y):
    screen.blit(player["img"], (x, y))


def enemy_screen(x, y):
    screen.blit(enemy["img"], (x, y))


def fire_bullet(x, y):
    bullet["state"] = "fire"
    screen.blit(bullet["img"], (x + 16, y + 10))


# Game Loop
running: bool = True
while running:
    # RGB Red, Green, Blue
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is presses check whatever its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player["x_change"] = -0.4
            if event.key == pygame.K_RIGHT:
                player["x_change"] = 0.4
            if event.key == pygame.K_UP:
                player["y_change"] = -0.4
            if event.key == pygame.K_DOWN:
                player["y_change"] = 0.4
            if event.key == pygame.K_x:
                bullet["x"] = player["x"]
                bullet["y"] = player["y"]
                fire_bullet(bullet["x"],
                            bullet["y"])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player["x_change"] = -0.03
            if event.key == pygame.K_RIGHT:
                player["x_change"] = 0.03
            if event.key == pygame.K_UP:
                player["y_change"] = -0.03
            if event.key == pygame.K_DOWN:
                player["y_change"] = 0.03
            if event.key == pygame.K_c:
                player["x_change"] = 0
                player["y_change"] = 0

    player["x"] += player["x_change"]
    player["y"] += player["y_change"]

    enemy["x"] += enemy["x_change"]

    #Ship limit
    if player["x"] <= 0:
        player["x"] = 0
        player["y_change"] = 0

    elif player["x"] >= 740:
        player["x"] = 740
        player["y_change"] = 0

    if player["y"] <= 0:
        player["y"] = 0

    elif player["y"] >= 540:
        player["y"] = 540

    if enemy["x"] <= 0:
        enemy["x_change"] = 0.3
        enemy["y"] += enemy["y_change"]

    elif enemy["x"] >= 740:
        enemy["x_change"] = -0.3
        enemy["y"] += enemy["y_change"]

    if bullet["y"] <= 0:
        bullet["y"] = 480
        bullet["state"] = "ready"

    if bullet["state"] == "fire":
        fire_bullet(bullet["x"],
                    bullet["y"])
        bullet["y"] -= bullet["y_change"]


    collision = is_collision(enemy["x"],enemy["y"],bullet["x"],bullet["x"])
    if collision:
        bullet["y"] = 480
        bullet["state"]= "ready"
        score += 1
        enemy["x"] =random.randint(0,800)
        enemy["y"] = random.randint(50,150)


    #Spawn the player
    enemy_screen(enemy["x"],
                 enemy["y"])

    player_screen(player["x"],
                  player["y"])

    pygame.display.update()
