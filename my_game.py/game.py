import pygame
import random

pygame.init()

screen_width = 1090
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))

player = pygame.image.load("player.jpg")
prize = pygame.image.load("prize.jpg")
enemy1 = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("image.png")

player_height = player.get_height()
player_width = player.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

print("The height of the player image is: " + str(player_height))
print("The width of the player image is: " + str(player_width))

playerXPosition = 100
playerYPosition = 50

prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)

enemy1XPosition = screen_width
enemy1YPosition = random.randint(0, screen_height - enemy1_height)

enemy2XPosition = screen_width
enemy2YPosition = random.randint(0, screen_height - enemy2_height)

enemy3XPosition = screen_width
enemy3YPosition = random.randint(0, screen_height - enemy2_height)


keyUp = False
keyDown = False

while 1:
    
    screen.fill(0)
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
                
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
                
                
    if keyUp == True:
        if playerYPosition > 0:
            playerYPosition -=1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:
            playerYPosition += 1
            
    playerBox = pygame.Rect(player.get_rect())
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition


    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition
    
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy1XPosition
    
    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition
    
    if playerBox.colliderect(enemy1):
        print("You lose!")
    elif playerBox.colliderect(enemy2):
        print("You lose!")
    elif playerBox.colliderect(enemy3):
        print("You lose")

        pygame.quit()
        exit(0)
            
    if playerXPosition == prize_width:
        print("You win")
        
    pygame.quit()
    exit(0)
    
    enemy1XPosition -= 0.15
    enemy2XPosition -= 0.15
    enemy3XPosition -= 0.15