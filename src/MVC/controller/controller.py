import MVC.model.model as model
# import MVC.controller as controller


def space_pressed(ship):
    if len(ship.bullets) < 3:
        ship.bullets.append(
            model.projectile(round(ship.x + ship.width // 2), round(ship.y + ship.height // 2), 6, (0, 255, 0), 1))


def left_pressed(ship):
        ship.x -= ship.vel


def right_pressed(ship):
        ship.x += ship.vel


def up_pressed(ship):
        ship.y -= ship.vel


def down_pressed(ship):
        ship.y += ship.vel





