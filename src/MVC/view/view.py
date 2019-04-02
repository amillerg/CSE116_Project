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

full_heart = pygame.image.load('images/fullHeart.png')

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
    pygame.draw.rect(win, bar_color, [0, 0, width/5, height], 0)
    pygame.draw.rect(win, bar_color, [width*(4/5), 0, width, height], 0)
    win.blit(full_heart, ( (width*(4/5)+20), 50))


    placing = 1
    xPlacing = 5
    xUser = 70
    xKills = 120
    xDeaths = 170
    y = 60

    '''for object in List:
        create_text(str(placing, "images/Helvetica.ttf", 10, (255, 255, 255)))
        placing = placing + 1
        
        win.blit(placing, (xPlacing, y))

        user = create_text(object.user, "images/Helvetica.ttf", 10, (255, 255, 255))
        win.blit(user, (xUser, y))
                 
        kills = create_text(object.kills, "images/Helvetica.ttf", 10, (255, 255, 255))
        win.blit(kills, (xKills, y))
        
        deaths = create_text(object.deaths, "images/Helvetica.ttf", 10, (255, 255, 255))
        win.blit(deaths, (xDeaths, y))
        
        y + 30 
        '''




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
        if bullet.x < (width *(4/5)) and bullet.x > (width/5):
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
    if keys[pygame.K_d] and ship.x >= width/ 5 and (ship.x <= (width*(4/5))):
        controller.right_pressed(ship)

    #  and ship.y > ship.vel
    if keys[pygame.K_w] and ship.y >= 0 and ship.y <= height:
        controller.up_pressed(ship)

    #  and ship.y < ship.ScreenWidth - ship.height
    if keys[pygame.K_s] and ship.y >= 0 and ship.y <= height:
        controller.down_pressed(ship)

    redrawGameWindow()

pygame.quit()
