import pygame
import operator
# import MVC.view as view
# import MVC.controller as controller

# player gets 5 coins per kill
# player needs 50 coins to buy a life
# as they buy more lives, cost per life will go up 20%

class player(object):
    def __init__(self, x, y, width, height, username):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 14
        self.ScreenWidth = 1200
        self.hitbox = (self.x + 20, self.y, 70, 70)
        self.bullets = []
        self.coins = 1000
        self.kills = 0
        self.deaths = 0
        self.health = 3
        self.username = username

    def draw(self, win):
        self.hitbox = (self.x + 20, self.y, 64, 64)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class projectile(object):
    def __init__(self, x, y, radius, direction, mouselocation):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (0, 255, 0)
        self.direction = direction
        self.vel = 10 * direction
        self.mouselocation = mouselocation
        self.angle_bullet = round(angle_bullet(self, x, y))
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

def angle_bullet(bullet, x, y):
    xdistance = bullet.mouselocation[0] - x
    ydistance = bullet.mouselocation[1] - y
    answer = (bullet.vel*ydistance)/xdistance
    if xdistance<0:
        bullet.vel *= -1
        answer = answer *-1
    return answer

def buy_life(mouse):
    x = mouse[0]
    y = mouse[1]
    return x<1150and x>1000 and y>350 and y<420


def buy_a_life(ship):
    if ship.health ==3:
        pass
    else:
        ship.health= ship.health + 1
        ship.coins -= 200

def topPlayers(playerList):
    top = {}  # dictionary of players and their kill to death ratios
    ratio = 0
    leaders = []  # list of top players
    for i in playerList:
        ratio = (i.kills / i.deaths)
        top[i] = ratio
    sorted_top = sorted(top.items(), key=operator.itemgetter(1))  # sorts the dictionary from least to greatest k/d ratio and makes a new list
    sorted_top.reverse() # reverses the list of sorted players
    for x in sorted_top:
        leaders.append(x[0])
    return leaders # returns list of players from first place to last based on kill/death ratio



def mouse_pressed(ship, mouse_location):
    if len(ship.bullets) < 3:
        ship.bullets.append(
            projectile(
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




