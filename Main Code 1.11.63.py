import math
import random
import pygame
from pygame import mixer

white = (255,255,255)
black = (0,0,0)
brightgreen = (121, 175, 127)
green = (92, 145, 101)
gold = (255,215,0)
orange = (255,165,0)
salmon = (250,128,114)
salmon_light = (255,160,122)
lower_black = (36,30,42)
upper_black = (96,122,126)


# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
bg = pygame.image.load('Main background.png')
background = pygame.transform.scale(bg, (800, 600))

info_background = pygame.image.load('info background.png')
info_back = pygame.transform.scale(info_background , (800,600))

intro_background = pygame.image.load('intro background.png')
intro_back = pygame.transform.scale(intro_background , (800,600))

#In game background start with 2,3,4,5,6
bg2 = pygame.image.load('Main background2.png')
background2 = pygame.transform.scale(bg2, (800, 600))

bg3 = pygame.image.load('Main background3.png')
background3 = pygame.transform.scale(bg3, (800, 600))

bg4 = pygame.image.load('Main background4.png')
background4 = pygame.transform.scale(bg4, (800, 600))

bg5 = pygame.image.load('Main background5.png')
background5 = pygame.transform.scale(bg5, (800, 600))

bg6 = pygame.image.load('Main background6.png')
background6 = pygame.transform.scale(bg6, (800, 600))

# Game Developer
background_dev = pygame.image.load('game developer.png')
bg_dv = pygame.transform.scale(background , (800,600))


#Play song in the intro and info loops
mixer.music.load("bongo song.mp3")
mixer.music.play(-1)


#FPS
clock = pygame.time.Clock()
FPS = 120

# Caption and Icon
pygame.display.set_caption("Bunky The Cat")
icon = pygame.image.load('cat app icon.png')
pygame.display.set_icon(icon)

# Player
player_Img1 = pygame.image.load('cat icon.png')
player1 = pygame.transform.scale(player_Img1, (175, 175))
player_Img2 = pygame.image.load('cat icon2.png')
player2 = pygame.transform.scale(player_Img2, (160, 160))
player_Img3 = pygame.image.load('cat icon3.png')
player3 = pygame.transform.scale(player_Img3, (140, 140))
#player_Img4 = pygame.image.load('cat icon4.png')
#player4 = pygame.transform.scale(player_Img4, (150, 150))

playerX = 370
playerY = 360
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 10

for i in range(num_of_enemies):
    enemy_Img = pygame.image.load('bone enemy.png')
    enemyImg.append(pygame.transform.scale(enemy_Img, (75, 75)))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)


# Bullet

bullet_Img = pygame.image.load('heart bullet.png')
bulletImg = pygame.transform.scale(bullet_Img, (125, 75))

#bullet kratong
bullet_kratong = pygame.image.load('kratong.png')
bullet_Img_Kratong = pygame.transform.scale(bullet_kratong , (75,75))

bulletX = 370
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('8-BIT WONDER.TTF', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('8-BIT WONDER.TTF', 60)

def game_over_text():
    
    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.mixer.music.pause()

        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (150, 200))

        button("PLAY AGAIN",160,300,220,60,salmon,salmon_light,game_loop)
        button("MAIN MENU",450,300,220,60,salmon,salmon_light,game_intro)
        pygame.display.update()



def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 50:
        return True
    else:
        return False

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def paused():

    pygame.mixer.music.pause()
    font = pygame.font.Font ("8-BIT WONDER.TTF", 30)
    largeText = pygame.font.Font("8-BIT WONDER.TTF",60)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = (400,300)
    screen.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    unpause()


        pygame.display.update()
        clock.tick(15)         
        
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False



def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(intro_back, (0,0))
        #largeText = pygame.font.Font('8-BIT WONDER.TTF', 60) #change to SysFont
        #TextSurf, TextRect = text_objects("Bunky The Cat", largeText)
        #TextRect.center = (410,200)
        #screen.blit(TextSurf, TextRect)     
        
        button("START",325,320,150,60,green,brightgreen,game_loop)
        button("INFO",325,395,150,60,green,brightgreen,game_info)
        button("QUIT",325,470,150,60,green,brightgreen,quit_game)
        pygame.display.update()
        clock.tick(15)
        
def game_info():

    info = True

    while info:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(info_back,(0,0))

        button("BACK",325,435,150,60,green,brightgreen,game_intro)
        pygame.display.update()
        
def quit_game():
    pygame.quit()
    quit()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font('8-BIT WONDER.TTF',20) #----- change from freesansbold.ttf to None
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def button_game(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font('8-BIT WONDER.TTF',10) #----- change from freesansbold.ttf to None
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)


def game_loop():

    global pause
    global bullet_state
    playerX = 370
    playerY = 360
    playerX_change = 0
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 10
    bulletX = 370
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"
    textX = 10
    testY = 10
    score_value = 0

    # Sound

    pygame.mixer.music.load("Wii.mp3")
    pygame.mixer.music.play(-1)


    for i in range(num_of_enemies):
        enemy_Img = pygame.image.load('bone enemy.png')
        enemyImg.append(pygame.transform.scale(enemy_Img, (75, 75)))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(4)
        enemyY_change.append(40)

    running = True
    while running:

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))
        # Background Image
        if score_value < 50:
            screen.blit(background, (0, 0))
        elif 50 <= score_value < 100:
            screen.blit(background2, (0,0))
        elif 100 <= score_value < 150:
            screen.blit(background3, (0,0))
        elif 150 <= score_value < 190:
            screen.blit(background4, (0,0))
        else:
            screen.blit(background6, (0,0))

        

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                running = False
                score = False

            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -3

                if event.key == pygame.K_RIGHT:
                    playerX_change = 3
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        #bulletSound = mixer.Sound("laser.wav")
                        #bulletSound.play()
                        # Get the current x cordinate of the spaceship
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)

                if event.key == pygame.K_p:
                    pause = True
                    paused()

                if event.key == pygame.K_l:
                    game_loy()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0



        # 5 = 5 + -0.1 -> 5 = 5 - 0.1
        # 5 = 5 + 0.1

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 680:
            playerX = 680

        button_game("MAIN MENU",450,550,150,35,lower_black,upper_black,game_intro)
        button_game("QUIT",620,550,140,35,lower_black,upper_black,quit_game)


       # Enemy Movement + speed
        for i in range(num_of_enemies):

            # Game Over
            if enemyY[i] > 330:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            if score_value <= 30:

                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 1
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -1    
                    enemyY[i] += enemyY_change[i]

            elif 30 < score_value <= 70:
                
                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 1.5
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -1.5      
                    enemyY[i] += enemyY_change[i]

            elif 70 < score_value <= 100:

                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 2
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -2        
                    enemyY[i] += enemyY_change[i]

            elif 100 < score_value <= 130:

                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 2.5
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -2.5       
                    enemyY[i] += enemyY_change[i]

            elif 130 < score_value <= 160:

                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 3
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -3      
                    enemyY[i] += enemyY_change[i]

            elif 160 < score_value <= 190:

                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 3.5
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -3.5    
                    enemyY[i] += enemyY_change[i]

            elif 190 < score_value :

                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 4
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -4    
                    enemyY[i] += enemyY_change[i]

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                #explosionSound = mixer.Sound("coin sound.wav")
                #explosionSound.play()
                bulletY = 370
                bullet_state = "ready"
                score_value += 1         
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)


        # Bullet Movement
        if bulletY <= 0:
            bulletY = 360
            bullet_state = "ready"

        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change


        #player(playerX, playerY)
        #show_score(textX, testY)

        if score_value <= 50:
            screen.blit(player1 , (playerX,playerY))
        elif 50 < score_value <= 100:
             screen.blit(player2 , (playerX,playerY))
        elif 100 < score_value <= 150:
            screen.blit(player3 , (playerX,playerY))
        else:
            screen.blit(player2 , (playerX,playerY))


        score = font.render("Score " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (10, 10))

        pygame.display.update()

def game_loy():

    global pause
    global bullet_state
    playerX = 370
    playerY = 360
    playerX_change = 0
    bulletX = 370
    bulletY = 460
    bulletX_change = 0.3
    bulletY_change = 0.1
    bullet_state = "ready"
    textX = 10
    testY = 10


    # Sound

    pygame.mixer.music.load("loy.mp3")
    pygame.mixer.music.play(-1)

    for i in range(num_of_enemies):
        enemy_Img = pygame.image.load('bone enemy.png')
        enemyImg.append(pygame.transform.scale(enemy_Img, (75, 75)))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(4)
        enemyY_change.append(40)

    running = True
    while running:

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))
        # Background Image

        screen.blit(background5, (0, 0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                running = False
                score = False

            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -3

                if event.key == pygame.K_RIGHT:
                    playerX_change = 3
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        #bulletSound = mixer.Sound("laser.wav")
                        #bulletSound.play()
                        # Get the current x cordinate of the spaceship
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)


                if event.key == pygame.K_b:
                    game_intro()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0



        # 5 = 5 + -0.1 -> 5 = 5 - 0.1
        # 5 = 5 + 0.1

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 130:
            playerX = 130


        # Bullet Movement
        if bulletX <= 0:
            bulletX = 360
            bullet_state = "ready"

        if bullet_state is "fire":
            screen.blit(bullet_Img_Kratong, (bulletX + 100, bulletY - 20))
            bulletX += bulletX_change


        #player(playerX, playerY)
        #show_score(textX, testY)

        
        screen.blit(player1 , (playerX,playerY))

        pygame.display.update()

game_intro()
game_loop()
game_loy()
pygame.quit()
quit()
