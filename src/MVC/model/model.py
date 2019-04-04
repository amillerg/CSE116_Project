import pygame
# import MVC.view as view
# import MVC.controller as controller

# player gets 5 coins per kill
# player needs 50 coins to buy a life
# as they buy more lives, cost per life will go up 20%

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 14
        self.ScreenWidth = 1200
        self.hitbox = (self.x + 20, self.y, 70, 70)
        self.bullets = []
        self.coins = 0
        self.kills = 0
        self.deaths = 0
        self.username = ""

    def draw(self, win):
        self.hitbox = (self.x + 20, self.y, 64, 64)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class projectile(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 40
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius - 1)

"""
class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing


def collisionWithWall(myBullet): # detects if a bullet collides with the window boundaries
    if ((myBullet.x < 500) and (myBullet.x > 0)):
        return False
    else:
        return True




class player(object):
    def __init__(self, x, y, width, height, health, alive):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 14
        self.health = health
        self.alive = alive

def playerHit(b, p):  # subtracts 100 from player health each time this function is called
    if (b.x == p.x) and (b.y == p.y):
        p.health -= 100
    if p.health <= 0:
        p.health = 0
        p.alive = False




bullets = []
bullets2 = []
Player = player(100, 100, 64, 64, 300, True)
for bullet in bullets:

    if collisionWithWall(bullet) is False:
        bullet.x += bullet.vel
    else:
        bullets.pop(bullets.index(bullet))
        bullets2.append(bullet)


def fireBullet():
    if len(BulletList) < 3:
        BulletList.append(projectile(round(Player.x + Player.width // 2), round(Player.y + Player.height // 2), 6, (0, 255, 50), 1))


"""