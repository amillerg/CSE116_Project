import MVC.model.model as model
import pygame
# import MVC.controller as controller

def setEvent(keys,ship,width,height):
    if keys[pygame.K_SPACE]:
        model.mouse_pressed(ship, pygame.mouse.get_pos())

    if keys[pygame.K_a] and (ship.x - width/5) > ship.vel:
        model.left_pressed(ship)

    if keys[pygame.K_d] and (ship.x + width/5) < width - ship.width - ship.vel:
        model.right_pressed(ship)

    if keys[pygame.K_w] and ship.y > ship.vel:
        model.up_pressed(ship)

    if keys[pygame.K_s] and ship.y < height - ship.height:
        model.down_pressed(ship)