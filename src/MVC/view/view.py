import pygame
import MVC.model.model as model
import MVC.controller.controller as controller
import MVC.view.ex_leaderboard as ex_lb
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

full_heart = pygame.image.load('images/fullHeart.png')
empty_heart = pygame.image.load('images/EmptyHeartWhite.png')
coin = pygame.image.load('images/Coin.png')

ship = model.player(width/2, height/2, char_width, char_height, "Jesse")

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
health = create_text("Health", "images/Helvetica.ttf", 26, (255, 255, 255))
wallet = create_text("Wallet", "images/Helvetica.ttf", 26, (255, 255, 255))

store = create_text("Store", "images/Helvetica.ttf", 26, (255, 255, 255))
buylife = create_text("Buy Life      200 c", "images/Helvetica.ttf", 22, (255,255,255))

placingTitle = create_text("Placing", "images/Helvetica.ttf", 14, (255, 255, 255))
userTitle = create_text("User", "images/Helvetica.ttf", 14, (255, 255, 255))
killTitle = create_text("Kills", "images/Helvetica.ttf", 14, (255, 255, 255))
deathsTitle = create_text("Deaths", "images/Helvetica.ttf", 14, (255, 255, 255))
name_tag = create_text(ship.username, "images/Helvetica.ttf", 10, (255, 255, 255))


def redrawGameWindow():
    win.blit(bg, (0, 0))
    win.blit(char, (ship.x, ship.y))
    win.blit(name_tag, (ship.x + 20, ship.y - 10))
    pygame.draw.rect(win, bar_color, [0, 0, width/5, height], 0)
    pygame.draw.rect(win, bar_color, [width*(4/5), 0, width, height], 0)

    for bullet in ship.bullets:
        bullet.draw(win)

    if ship.health == 3:
        win.blit(full_heart, ( (width*(4/5)+40), 75))
        win.blit(full_heart, ((width * (4 / 5) + 90), 75))
        win.blit(full_heart, ((width * (4 / 5) + 140), 75))

    if ship.health == 2:
        win.blit(full_heart, ((width * (4 / 5) + 40), 75))
        win.blit(full_heart, ((width * (4 / 5) + 90), 75))
        win.blit(empty_heart, ((width * (4 / 5) + 140), 75))

    if ship.health == 1:
        win.blit(full_heart, ((width * (4 / 5) + 40), 75))
        win.blit(empty_heart, ((width * (4 / 5) + 90), 75))
        win.blit(empty_heart, ((width * (4 / 5) + 140), 75))

    #if mousePressed:
        #pygame.draw.line(win, (0, 255, 0), line[0], line[1])

    win.blit(leaderboard, (45, 30))
    win.blit(health, (1045,30))
    win.blit(wallet, (1045, 180))
    pygame.draw.line(win, (11, 68, 160), ((width*(4/5)), 155), (1200, 155), 2)
    pygame.draw.line(win, (11, 68, 160), ((width * (4 / 5)), 300), (1200, 300), 2)

    user_coins = create_text(str(ship.coins) + " c", "images/Helvetica.ttf", 26, (255, 255, 255))
    win.blit(user_coins, (1045, 240))
    win.blit(store, (1045, 320))
    win.blit(buylife, (1000, 370))

    win.blit(placingTitle, (5, 80))
    win.blit(userTitle, (70, 80))
    win.blit(killTitle, (160, 80))
    win.blit(deathsTitle, (190, 80))

# ----------------------------------------------------------------------^

    placing = 1
    xPlacing = 10
    xUser = 50
    xKills = 160
    xDeaths = 210
    y = 110

    for object in ex_lb.ship_list:
        place = create_text(str(placing), "images/Helvetica.ttf", 14, (255, 255, 255))
        placing = placing + 1
        
        win.blit(place, (xPlacing, y))

        user = create_text(object.username, "images/Helvetica.ttf", 14, (255, 255, 255))
        win.blit(user, (xUser, y))
                 
        kills = create_text(str(object.kills), "images/Helvetica.ttf", 14, (255, 255, 255))
        win.blit(kills, (xKills, y))
        
        deaths = create_text(str(object.deaths), "images/Helvetica.ttf", 14, (255, 255, 255))
        win.blit(deaths, (xDeaths, y))
        
        y = y + 50

    pygame.display.update()



# mainloop

run = True

list_of_ships = [ship]

time = 0
while run:
    clock.tick(60)  # FPS
    # print(time)
    time += 1
    if (time == 100):
        ship.health = 2

    if time == 200:
        ship.health = 1

    #mousePressed = False
    #line = [(round(ship.x + ship.width // 2), round(ship.y + ship.height // 2)), pygame.mouse.get_pos()]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in ship.bullets:
        if bullet.x < (width *(4/5)- 2*bullet.radius) and bullet.x > (width/5 + 2*bullet.radius):
            bullet.y += bullet.angle_bullet
            bullet.x += bullet.vel
        else:
            ship.bullets.pop(ship.bullets.index(bullet))


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        controller.mouse_pressed(ship, pygame.mouse.get_pos())

    if keys[pygame.K_a] and (ship.x - width/5) > ship.vel:
        controller.left_pressed(ship)

    if keys[pygame.K_d] and (ship.x + width/5) < width - ship.width - ship.vel:
        controller.right_pressed(ship)

    if keys[pygame.K_w] and ship.y > ship.vel:
        controller.up_pressed(ship)

    if keys[pygame.K_s] and ship.y < height - ship.height:
        controller.down_pressed(ship)

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        print(type(mouse))
        if mouse[0]<((4/5)*width) and mouse[0] > (width/5):
            #mousePressed = True
            controller.mouse_pressed(ship, mouse)
        if model.buy_life(mouse):
            model.buy_a_life(ship)




    redrawGameWindow()

pygame.quit()
