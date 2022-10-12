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
    "x_change": 0,
    "y_change": 0
}

enemy = {
    "img": load_image('assets/images/enemies/space-invader-icon.png'),
    "x": random.randint(0, 600),
    "y": random.randint(50, 150),
    "x_change": 0.3,
    "y_change": 0
}

xLimit = {
    0: 0,
    740: 740
}

yLimit = {
    0: 0,
    540: 540
}


def player_screen(x, y):
    screen.blit(player["img"], (x, y))


def enemy_screen(x, y):
    screen.blit(enemy["img"], (x, y))


# Game Loop
running: bool = True
while running:
    # RGB Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is presses check whatever its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player["x_change"] = -0.3
            if event.key == pygame.K_RIGHT:
                player["x_change"] = 0.3
            if event.key == pygame.K_UP:
                player["y_change"] = -0.3
            if event.key == pygame.K_DOWN:
                player["y_change"] = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player["x_change"] = 0
                player["y_change"] = 0

    player["x"] += player["x_change"]
    player["y"] += player["y_change"]

    if player["x"] <= 0:
        player["x"] = 0
    elif player["x"] >= 740:
        player["x"] = 740
    if player["y"] <= 0:
        player["y"] = 0
    elif player["y"] >= 540:
        player["y"] = 540

    enemy_screen(enemy["x"], enemy["y"])
    player_screen(player["x"], player["y"])

    pygame.display.update()
