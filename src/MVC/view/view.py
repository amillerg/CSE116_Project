import pygame
import MVC.model.model as model
import MVC.controller.controller as controller

pygame.init()

win = pygame.display.set_mode((700, 700))

pygame.display.set_caption("Space Shooters")

bg = pygame.image.load('images/Night Sky copy.jpg')
char = pygame.image.load('images/spaceship.gif')

clock = pygame.time.Clock()


def redrawGameWindow():
    win.blit(bg, (0, 0))
    win.blit(char, (ship.x, ship.y))

    for bullet in ship.bullets:
        bullet.draw(win)

    pygame.display.update()


# mainloop
ship = model.player(300, 410, 64, 64)
run = True


while run:
    clock.tick(60)  # FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in ship.bullets:

        if bullet.x < 700 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            ship.bullets.pop(ship.bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        controller.space_pressed(ship)

    if keys[pygame.K_a] and ship.x > ship.vel:
        controller.left_pressed(ship)

    if keys[pygame.K_d]and ship.x < ship.ScreenWidth - ship.width - ship.vel:
        controller.right_pressed(ship)

    if keys[pygame.K_w] and ship.y > ship.vel:
        controller.up_pressed(ship)

    if keys[pygame.K_s] and ship.y < ship.ScreenWidth - ship.height:
        controller.down_pressed(ship)

    redrawGameWindow()

pygame.quit()
