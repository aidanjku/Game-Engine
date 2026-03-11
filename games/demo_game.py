import pygame
from engine.game import Game
from engine.sprite import Sprite
from engine.physics import apply_gravity, collide

def run_demo():
    game = Game()

    player = Sprite(100, 100, 40, 40, color=(0, 200, 255))
    platform = Sprite(0, 550, 800, 50, color=(100, 255, 100))

    game.add_object(player)
    game.add_object(platform)

    def player_update():
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.vx = -5
        elif keys[pygame.K_RIGHT]:
            player.vx = 5
        else:
            player.vx = 0

        player.rect.x += player.vx
        apply_gravity(player)
        collide(player, [platform])

    player.update = player_update

    game.run()