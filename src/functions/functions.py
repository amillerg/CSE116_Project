import pygame
pygame.init()

win = pygame.display.set_mode((700, 700))

pygame.display.set_caption("Space Shooters")

bg = pygame.image.load('')  # background image
char = pygame.image.load('')  # character sprite

clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 14
        self.ScreenWidth = 700
        self.hitbox = (self.x +20, self.y, 70, 70)

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



def redrawGameWindow():
    win.blit(bg, (0,0))
    win.blit(char, (ship.x, ship.y))
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()

#mainloop
ship = player(300, 410, 64, 64)
bullets = []
run = True

while run:
    clock.tick(60)  # FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:

        if bullet.x < 700 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if len(bullets) < 3:
            bullets.append(projectile(round(ship.x + ship.width // 2), round(ship.y + ship.height // 2), 6, (0, 255, 50), 1))

    if keys[pygame.K_LEFT] and ship.x > ship.vel:
        ship.x -= ship.vel
    if keys[pygame.K_RIGHT]and ship.x < ship.ScreenWidth - ship.width - ship.vel:
        ship.x += ship.vel
    if keys[pygame.K_UP] and ship.y > ship.vel:
        ship.y -= ship.vel
    if keys[pygame.K_DOWN] and ship.y < ship.ScreenWidth - ship.height:
        ship.y += ship.vel

    redrawGameWindow()

pygame.quit()





















