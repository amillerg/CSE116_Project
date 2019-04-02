import unittest
from src.functions import demoFunctions


class UnitTesting(unittest.TestCase):

    def test1(self): # different coordinates, player with 500 health is not hit
        p = demoFunctions.player(100, 100, 10, 30, 500, True)
        b = demoFunctions.projectile(50, 50, 6, (0, 0, 0), -1)
        demoFunctions.playerHit(b, p)

        self.assertTrue(p.health == 500)
        self.assertTrue(p.alive == True)

    def test2(self): # same coordinates, player with 500 health is hit once
        p = demoFunctions.player(100, 100, 10, 30, 500, True)
        b = demoFunctions.projectile(100, 100, 6, (0, 0, 0), -1)
        demoFunctions.playerHit(b, p)

        self.assertTrue(p.health == 400)
        self.assertTrue(p.alive == True)

    def test3(self): # same coordinates, player with 500 health is hit 4 times
        p = demoFunctions.player(300, 300, 10, 30, 500, True)
        b = demoFunctions.projectile(300, 300, 6, (0, 0, 0), -1)
        demoFunctions.playerHit(b, p)
        demoFunctions.playerHit(b, p)
        demoFunctions.playerHit(b, p)
        demoFunctions.playerHit(b, p)

        self.assertTrue(p.health == 100)
        self.assertTrue(p.alive == True)

    def test4(self): # same coordinates, player with 500 health is hit 5 times and is dead
        p = demoFunctions.player(123, 123, 10, 30, 500, True)
        b = demoFunctions.projectile(123, 123, 6, (0, 0, 0), -1)
        demoFunctions.playerHit(b, p)
        demoFunctions.playerHit(b, p)
        demoFunctions.playerHit(b, p)
        demoFunctions.playerHit(b, p)
        demoFunctions.playerHit(b, p)

        self.assertTrue(p.health == 0)
        self.assertTrue(p.alive == False)


if __name__=="__main__":
    unittest.main()







