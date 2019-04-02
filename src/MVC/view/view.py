import pygame
import MVC.model.model as model
import MVC.controller.controller as controller

pygame.init()

height = 600
width = 1200

bar_color = (206, 57, 16)

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Space Shooters")

bg = pygame.image.load('images/Night Sky copy.jpg')

char = pygame.image.load('images/spaceship.gif')
char_width = char.get_size()[0]
char_height = char.get_size()[1]

clock = pygame.time.Clock()



_cached_text = {}
def create_text(text, ourFont, size, color):
    global _cached_text
    key = '|'.join(map(str, (ourFont, size, color, text)))
    image = _cached_text.get(key, None)
    if image == None:
        font = pygame.font.Font(ourFont, size)
        image = font.render(text, True, color)
        _cached_text[key] = image
    return image


leaderboard = create_text("Leaderboard", "images/Helvetica.ttf", 26, (255, 255, 255))

placingTitle = create_text("Placing", "images/Helvetica.ttf", 14, (255, 255, 255))
userTitle = create_text("User", "images/Helvetica.ttf", 14, (255, 255, 255))
killTitle = create_text("Kills", "images/Helvetica.ttf", 14, (255, 255, 255))
deathsTitle = create_text("Deaths", "images/Helvetica.ttf", 14, (255, 255, 255))



def redrawGameWindow():
    win.blit(bg, (0, 0))
    win.blit(char, (ship.x, ship.y))
    pygame.draw.rect(win, bar_color, [0, 0, width/6, height], 0)
    pygame.draw.rect(win, bar_color, [width*(5/6), 0, width, height], 0)

    """for object in List:
        create_text("1st", "images/Helvetica.ttf", 10, (255, 255, 255))
        create_text(object.user, "images/Helvetica.ttf", 10, (255, 255, 255))
        create_text(object.kills, "images/Helvetica.ttf", 10, (255, 255, 255))
        create_text(object.deagh, "images/Helvetica.ttf", 10, (255, 255, 255))

"""

    win.blit(leaderboard, (25,30))
    win.blit(placingTitle, (5, 60))
    win.blit(userTitle, (70, 60))
    win.blit(killTitle, (120, 60))
    win.blit(deathsTitle, (170, 60))

    for bullet in ship.bullets:
        bullet.draw(win)

    pygame.display.update()




# mainloop
ship = model.player(width/2, height/2, char_width, char_height)
run = True

list_of_ships = [ship]

while run:
    clock.tick(60)  # FPS



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in ship.bullets:
        if bullet.x < (width *(5/6)) and bullet.x > (width/6):
            bullet.x += bullet.vel
        else:
            ship.bullets.pop(ship.bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        controller.space_pressed(ship)

    # and ship.x > ship.vel
    if keys[pygame.K_a]:
        controller.left_pressed(ship)

    # and ship.x < ship.ScreenWidth - ship.width - ship.vel
    if keys[pygame.K_d] and ship.x >= width/ 6 and (ship.x <= (width*(5/6))):
        controller.right_pressed(ship)

    #  and ship.y > ship.vel
    if keys[pygame.K_w] and ship.y >= 0 and ship.y <= height:
        controller.up_pressed(ship)

    #  and ship.y < ship.ScreenWidth - ship.height
    if keys[pygame.K_s] and ship.y >= 0 and ship.y <= height:
        controller.down_pressed(ship)

    redrawGameWindow()

pygame.quit()
