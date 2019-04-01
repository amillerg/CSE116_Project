import unittest
from src.functions import demoFunctions


class UnitTesting(unittest.TestCase):

    def test1(self):
        bullet1 = demoFunctions.projectile(100, 100, 6, (0, 0, 0), -1)
        bullet2 = demoFunctions.projectile(600, 600, 6, (0, 0, 0), -1)

        bullet3 = demoFunctions.projectile(-.00001, 0, 6, (0, 0, 0), -1)
        bullet4 = demoFunctions.projectile(0.00001, 0, 6, (0, 0, 0), -1)

        bullet5 = demoFunctions.projectile(500.00001, 0, 6, (0, 0, 0), -1)
        bullet6 = demoFunctions.projectile(499.99999, 0, 6, (0, 0, 0), -1)

        bullet7 = demoFunctions.projectile(-100000000, 100, 6, (0, 0, 0), -1)
        bullet8 = demoFunctions.projectile(9999999999, 600, 6, (0, 0, 0), -1)

        self.assertTrue(demoFunctions.collisionWithWall(bullet1) == False)  # not collided
        self.assertTrue(demoFunctions.collisionWithWall(bullet2) == True)  # collided

        self.assertTrue(demoFunctions.collisionWithWall(bullet3) == True)  # collided
        self.assertTrue(demoFunctions.collisionWithWall(bullet4) == False)  # not collided

        self.assertTrue(demoFunctions.collisionWithWall(bullet5) == True)  # collided
        self.assertTrue(demoFunctions.collisionWithWall(bullet6) == False)  # not collided

        self.assertTrue(demoFunctions.collisionWithWall(bullet7) == True)  # collided
        self.assertTrue(demoFunctions.collisionWithWall(bullet8) == True)  # not collided

if __name__=="__main__":
    unittest.main()