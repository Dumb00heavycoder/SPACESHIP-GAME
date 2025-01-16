import pygame 
import time 
import random 

#setting resolution
WIDTH, HEIGHT = 1280 , 600
#i personally like this resolution and i use it in most of my games
WIN = pygame.display.set_mode((WIDTH,  HEIGHT))

#displaying the name of the game
pygame.display.set_caption("Space Invaders")

#variables for my player's coordinates
PLAYER_WIDTH = 25
PLAYER_HEIGHT = 40
PLAYER_VELOCITY = 3

#here i am creating a variable to hold my background image
BG = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH,HEIGHT))
#i used pygame.transform.scale to scale my image from (0,0) coordinates to the maximum resolution, i did this because the real imagae's size is much smaller and it was not fitting in



#creating a function to put the background
def draw(player):
    WIN.blit(BG, (0,0))
    #(0,0) are the height and widht coordinate and not mentioning anything after that means the program will fill display with background till my final coordinates which are (1280,600)
    
    #drawing the player
    pygame.draw.rect(WIN, "red", player )


    pygame.display.update()
    #this update function is used to update the screen everytime i make a change in the draw function



#i am creating a function to keep my game displayed on the screen in a constant loop 
def main():
    run = True 
    
    #here i set my player as a rectangle with its coordinates
    player = pygame.Rect(640, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
                break
        #setting up keys for my player , velocity here represents the amount of frames being added or reduced to the players position
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_d]:
            player.x += PLAYER_VELOCITY


        draw(player)
        #calling the draw function
    pygame.quit()

if __name__ == "__main__":
    main()