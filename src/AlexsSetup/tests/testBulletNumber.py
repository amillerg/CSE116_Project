import unittest
from AlexsSetup.functions import demoFunctions


class UnitTesting(unittest.TestCase):

    def test1(self):  # No bullets on screen, one additional bullet fired
        bullets = []
        bullets2 = []

        Player = demoFunctions.player(100, 100, 64, 64, 300, True)
        for bullet in bullets:

            if demoFunctions.collisionWithWall(bullet) is False:
                bullet.x += bullet.vel
                bullets2.append(bullet)

        demoFunctions.fireBullet(Player, bullets2)  # one bullet is fired

        self.assertTrue(len(bullets2) == 1)




    def test2(self):  # 2 bullets on screen, 1 additional bullet fired
        bullet1 = demoFunctions.projectile(100, 100, 6, (0, 0, 0), -1)  # on screen
        bullet2 = demoFunctions.projectile(200, 200, 6, (0, 0, 0), -1)  # on screen
        bullets = [bullet1, bullet2]

        bullets2 = []

        Player = demoFunctions.player(100, 100, 64, 64, 300, True)
        for bullet in bullets:

            if demoFunctions.collisionWithWall(bullet2) is False:
                bullet.x += bullet.vel
                bullets2.append(bullet)

        demoFunctions.fireBullet(Player, bullets2)  # one bullet is fired

        self.assertTrue(len(bullets2) == 3)





    def test3(self):  # 2 bullets on screen, 2 bullets off screen, one additional bullet fired
        bullet1 = demoFunctions.projectile(100, 100, 6, (0, 0, 0), -1)  # on screen
        bullet2 = demoFunctions.projectile(200, 200, 6, (0, 0, 0), -1)  # on screen
        bullet3 = demoFunctions.projectile(600, 600, 6, (0, 0, 0), -1)  # off screen
        bullet4 = demoFunctions.projectile(501, 501, 6, (0, 0, 0), -1)  # off screen
        bullets = [bullet1, bullet2, bullet3, bullet4]
        bullets2 = []

        Player = demoFunctions.player(100, 100, 64, 64, 300, True)

        for bullet in bullets:

            if demoFunctions.collisionWithWall(bullet) is False:
                bullet.x += bullet.vel
                bullets2.append(bullet)

        demoFunctions.fireBullet(Player, bullets2)  # one bullet is fired

        self.assertTrue(len(bullets2) == 3)





    def test4(self):  # 0 bullets on screen, 6 bullets off screen, 2 bullets fired
        bullet1 = demoFunctions.projectile(673, 100, 6, (0, 0, 0), -1)  # off screen
        bullet2 = demoFunctions.projectile(891, -42, 6, (0, 0, 0), -1)  # off screen
        bullet3 = demoFunctions.projectile(-1000, 1, 6, (0, 0, 0), -1)  # off screen
        bullet4 = demoFunctions.projectile(1234, 5678, 6, (0, 0, 0), -1)  # off screen
        bullet5 = demoFunctions.projectile(-20.93248, -500.23, 6, (0, 0, 0), -1)  # off screen
        bullet6 = demoFunctions.projectile(673, 100, 6, (0, 0, 0), -1)  # off screen
        bullets = [bullet1, bullet2, bullet3, bullet4, bullet5, bullet6]
        bullets2 = []

        Player = demoFunctions.player(100, 100, 64, 64, 300, True)
        for bullet in bullets:

            if demoFunctions.collisionWithWall(bullet) is False:
                bullet.x += bullet.vel
                bullets2.append(bullet)

        demoFunctions.fireBullet(Player, bullets2)  # one bullet is fired
        demoFunctions.fireBullet(Player, bullets2)  # one bullet is fired

        self.assertTrue(len(bullets2) == 2)





if __name__=="__main__":
    unittest.main()







