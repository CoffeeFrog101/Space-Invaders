import pygame
import random
import math
from pygame import mixer
#intilize the pygame
pygame.init()
# creates a screen                 w    h
screen = pygame.display.set_mode((800,600))

#background and music
background = pygame.image.load('space-galaxy-background.png')
mixer.music.load("background sound.wav")
mixer.music.play(-1)
#title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('outer-space-alien.png')
pygame.display.set_icon(icon)

#player
playerimg = pygame.image.load('ship 2.png')
playerx = 350
playery = 470
playerx_change = 0

#Enemey

enemy_img = pygame.image.load('ufo.png')
enemyX = random.randint(0,735)
enemyY = random.randint(50,150)
enemyX_change = 2
enemyY_change = 40

#Bullet

#ready - you cant see the bullet on the screen
#
bullet_img = pygame.image.load('bullet.png')
bulletX = 0
bulletY=470
bulletX_change = 0
bulletY_change = 10
bullet_state ="ready"
#score
score_amount = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
testY = 10





def show_score(x,y):
    score = font.render("Score : " + str(score_amount),True,(255,255,255))#color white
    screen.blit( score, (x, y) )
#draw the player
def player(x,y):
    screen.blit(playerimg, (x,y))
def enemy(x,y):
    screen.blit(enemy_img, (x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 32,y + 10))

def iscollsion(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2)+ math.pow(enemyY-bulletY,2))
    if distance < 27:
        return True
    else:
        return False

#Game loop makes the game running infinitly
running = True
while running:
    # RGB = Red Green Blue
    screen.fill( (0, 0, 0) )
    #background image
    screen.blit(background,(0, 0))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    # if key pressed check if its right or left


      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              playerx_change = -2
          if event.key == pygame.K_RIGHT:
              playerx_change = 2
          if event.key == pygame.K_SPACE:

             if bullet_state == "ready":
                 bullet_Sound = mixer.Sound( "laser gun.wav" )
                 bullet_Sound.play()

                 bulletX = playerx
                 fire_bullet(bulletX,bulletY)

      if event.type == pygame.KEYUP:
           if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               playerx_change = 0



#checking spaceship boundries so that is doesnt go out of bounds
    playerx += playerx_change

    if playerx <=0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
# enemy movments




    enemyX += enemyX_change
    if enemyX <= 0:
            enemyX_change= 2
            enemyY += enemyY_change
    elif enemyX >= 736:
           enemyX_change = -2
           enemyY += enemyY_change




    # bullet movment
    if bulletY <= 0:
        bulletY = 470
        bullet_state = "ready"


    if bullet_state == "fire":
        fire_bullet(bulletX ,bulletY)
        bulletY -= bulletY_change

        # collision
    collision = iscollsion( enemyX, enemyY, bulletX, bulletY )
    if collision:
          impact_Sound = mixer.Sound( "impact sound.wav" )
          impact_Sound.play()
          bulletY = 470
          bullet_state = "ready"
          score_amount += 1
          print( score_amount )
          # will restart the poition of the alien
          enemyX = random.randint( 0, 735 )
          enemyY = random.randint( 50, 150 )



    player(playerx,playery)
    show_score(textX,testY)
    enemy( enemyX, enemyY )
    pygame.display.update()

