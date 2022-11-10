import pygame

SCREEN_EVENT = {
    pygame.QUIT: False
}

PLAYER_EVENT = {
    pygame.K_UP: -0.4,
    pygame.K_RIGHT: 0.4,
    pygame.K_LEFT: -0.4,
    pygame.K_DOWN: 0.4,
    pygame.K_c: 0,

}

REST_EVENT = {
    pygame.K_UP: -0.03,
    pygame.K_RIGHT: 0.03,
    pygame.K_LEFT: -0.03,
    pygame.K_DOWN: 0.03,
}

PLAYER_COLLISION_EVENT = {
    0: 0,
    740: 740
}
