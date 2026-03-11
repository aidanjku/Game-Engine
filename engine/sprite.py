import pygame

class Sprite:
    def __init__(self, x, y, w, h, color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.vx = 0
        self.vy = 0

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)