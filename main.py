import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1000,625))
pygame.display.set_caption("Theory of Fromage")
font = pygame.font.Font(None, 40) # use default font

doExit = False

clock = pygame.time.Clock()

GameMap =[
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
          ]

# position variables
playerx = 20
playery = 300


#velocity variables
playerxVel = 0
playeryVel = 0

#variable to check for ground collision
isGrounded = False

#variables for which direction the player is going
xDirection = 1
yDirection = 1




while not doExit:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True

    # game logic goes here --------------------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if isGrounded == True:
            playeryVel -= 5
            
    if playerxVel > -7.5:#checks if velocity is lower than a certain value to limit top speed
        if keys[pygame.K_a]:#left
            if isGrounded == True:
                playerxVel -= .50
            elif isGrounded == False:
                playerxVel -= .30

    if playerxVel < 7.5:#right
        if keys[pygame.K_d]:
            if isGrounded == True:
                playerxVel += .5
            elif isGrounded == False:
                playerxVel += .3
        
    if isGrounded == False: #checks if s key is pressed in the air allowing a fast fall
        if keys[pygame.K_s]:
            playeryVel -= -0.8
    #direction variables for collision
    if playeryVel > 0:
        yDirection = 1
    elif playeryVel < 0:
        yDirection = 2
    if playerxVel > 0:
        xDirection = 1
    elif playerxVel < 0:
        xDirection = 2



    #gravity
    if isGrounded == False:
        playeryVel += .1
    #friction
    if isGrounded == True:
        playerxVel * 0.2

    #collisions plural
        
    # VERTICAL RELATED collision################################
    if GameMap[int((playery+25)/25)][int((playerx+25)/25)] == 1:#checks if the players position divided by 25 is a 1 in the array, if the player is on a block
        if yDirection == 1: #if going down
            playeryVel = 0 #vertical velocity is 0
            isGrounded = True
        else:
            isGrounded = False
        
    if GameMap[int((playery+25)/25)][int((playerx)/25)] == 0: #constant check to see if the player is in the air
        isGrounded = False

        
    if GameMap[int((playery)/25)][int((playerx+12)/25)] == 1: #checks for collision under a block
        playeryVel = 0 #resets y velocity
        playeryVel += 3.8 #moves player back down
    ###########################################################
    # Horizontal collision checks##############################
    if GameMap[int((playery+10)/25)][int((playerx)/25)] == 1: #collision checks towards the left
        if xDirection == 2:
            playerxVel = 0

    if GameMap[int((playery+10)/25)][int((playerx+25)/25)] == 1: #collision checks towards the right
        if xDirection == 1:
            playerxVel = 0
            
    #falling through the ground check
    if playery + 30 > 625:
        isGrounded = True
        playery = 625 - 30
    
    #going off the sides check
    if playerx + 25 > 970:
        playerxVel = -2
    if playerx < 0:
        playerxVel = 2
    # END collision CHECKS ######################################################################    
    
    playery += playeryVel
    playerx += playerxVel

    # render section will go here---------------------
    screen.fill((0,0,0)) # wipe screen
    
    for i in range (25):
        for j in range (40):
            if GameMap[i][j] == 1:
                pygame.draw.rect(screen, (255,130,130), (j*25,i*25,25,25))
    
    pygame.draw.rect(screen, (255,255,255), (playerx, playery, 25, 25))
    # update the screen
    pygame.display.flip()

# end game LOOP-------------------------------------

pygame.quit()
