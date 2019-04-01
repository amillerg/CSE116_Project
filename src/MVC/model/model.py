import pygame
# import MVC.view as view
# import MVC.controller as controller


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 14
        self.ScreenWidth = 700
        self.hitbox = (self.x + 20, self.y, 70, 70)
        self.bullets = []

    def draw(self, win):
        self.hitbox = (self.x + 20, self.y, 64, 64)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class projectile(object):
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.vel = 20 * direction

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

