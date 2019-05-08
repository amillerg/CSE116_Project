import MVC.model.model as model
import pygame
# import MVC.controller as controller


def mouse_pressed(ship, mouse_location):
    if len(ship.bullets) < 3:
        ship.bullets.append(
            model.projectile(
                round(ship.x + ship.width // 2),
                round(ship.y + ship.height // 2),
                6, 1, mouse_location))


def left_pressed(ship):
        ship.x -= ship.vel


def right_pressed(ship):
        ship.x += ship.vel


def up_pressed(ship):
        ship.y -= ship.vel


def down_pressed(ship):
        ship.y += ship.vel





