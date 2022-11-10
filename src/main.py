import math
import pygame
import random
from pygame import mixer

from src.modules.events.keys_event import PLAYER_EVENT, REST_EVENT, SCREEN_EVENT

# Initialize the pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('src/assets/images/icon.png')
pygame.display.set_icon(icon)


def load_image(directory: str = ''):
    return pygame.image.load(directory)


background = load_image('src/assets/images/backgrounds/space-background.jpg')

player = {
    "img": load_image('src/assets/images/ships/spaceship/Spaceship_Green64.gif'),
    "x": 370,
    "y": 480,
    "x_change": 0.0,
    "y_change": 0.0
}

enemy = {
    "img": load_image('src/assets/images/enemies/enemy.png'),
    "x": random.randint(0, 600),
    "y": random.randint(50, 150),
    "x_change": 0.3,
    "y_change": 40.0
}

num_enemies = 3
enemies = []
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

for i in range(num_enemies):
    enemies.append(enemy)
    enemy_img.append(enemy["img"])
    enemy_x.append(random.randint(0, 600))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(enemy["x_change"])
    enemy_y_change.append(enemy["y_change"])

print(enemy_x)

bullet = {
    "img": load_image('src/assets/images/bullets/black_shoot.png'),
    "x": 0,
    "y": 480,
    "x_change": 2,
    "y_change": 10.0,
    "state": "ready",
    "sound": mixer.Sound('src/assets/sounds/effects/laser.wav')
}

text: dict = {
    "score": 0,
    "font": pygame.font.Font('src/assets/fonts/contrast.ttf', 32),
    "x": 10,
    "y": 10
}

mixer.music.load('src/assets/sounds/background_music/background.wav')
mixer.music.play(-1)


def game_over_text():
    game_over = text['font'].render(f"Game Over:{text['score']}", True, (255, 255, 255))
    screen.blit(game_over, (200, 250))


def show_score(x, y):
    score_render = text['font'].render("Score:" + str(text['score']), True, (255, 255, 255))
    screen.blit(score_render, (x, y))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    a = math.pow(enemy_x - bullet_x, 2)
    b = math.pow(enemy_y - bullet_y, 2)
    distance = math.sqrt(a) + math.sqrt(b)
    return True if distance < 30 else False


def display_entity(entity_image, cords: tuple):
    screen.blit(entity_image, cords)


def fire_bullet(x, y):
    bullet["state"] = "fire"
    screen.blit(bullet["img"], (x + 12, y + 8))


def main():
    # Game Loop
    running: bool = True
    while running:
        # RGB Red, Green, Blue
        # screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        for event in pygame.event.get():

            running = SCREEN_EVENT.get(event.type, True)

            # if keystroke is presses check whatever its right or left
            if event.type == pygame.KEYDOWN:
                player["x_change"] = PLAYER_EVENT.get(event.key, 0)

                if event.key == pygame.K_x:
                    bullet["x"] = player["x"]
                    bullet["y"] = player["y"]
                    bullet["sound"].play()
                    fire_bullet(bullet["x"], bullet["y"])

            if event.type == pygame.KEYUP:
                player["x_change"] = REST_EVENT.get(event.key, 0)

                if event.key == pygame.K_c:
                    player["x_change"] = 0

        player["x"] += player["x_change"]

        # Ship limit
        if player["x"] <= 0:
            player["x"] = 0

        if player["x"] >= 740:
            player["x"] = 740

        # Enemy Movement
        for h in range(num_enemies):
            enemy_x[h] += enemy_x_change[i]

            if enemy_x[h] <= 0:
                enemy_x_change[i] = 0.3
                enemy_y[h] += enemy_y_change[h]

            if enemy_x[h] >= 740:
                enemy_x_change[h] = -0.3
                enemy_y[i] += enemy_y_change[h]

            collision = is_collision(enemy_x[h], enemy_y[h], bullet["x"], bullet["x"])
            if collision:
                BULLET_SOUND = mixer.Sound('src/assets/sounds/effects/explosion.wav')
                BULLET_SOUND.play()
                bullet["y"] = 300
                bullet["state"] = "ready"
                text["score"] += 1
                enemy_x[h] = random.randint(0, 600)
                enemy_y[h] = random.randint(70, 150)

            if enemy_y[h] > 450:
                for u in range(num_enemies):
                    enemy_y[u] = 2000
                    game_over_text()
                # break

            # Spawn the ENEMY
            display_entity(enemy.get("img"), (enemy_x[h], enemy_y[h]))

        # Bullet Movement
        if bullet["y"] <= 0:
            bullet["y"] = 480
            bullet["state"] = "ready"

        if bullet["state"] == "fire":
            fire_bullet(bullet["x"],
                        bullet["y"])
            bullet["y"] -= bullet["y_change"]

        # Spawn the player
        display_entity(player.get("img"), (player["x"], player["y"]))

        show_score(text["x"], text["y"])
        pygame.display.update()


if __name__ == "__main__":
    main()
