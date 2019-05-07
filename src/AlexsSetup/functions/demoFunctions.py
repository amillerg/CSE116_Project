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


def fireBullet(Player, BulletList):
    if len(BulletList) < 3:
        BulletList.append(projectile(round(Player.x + Player.width // 2), round(Player.y + Player.height // 2), 6, (0, 255, 50), 1))






