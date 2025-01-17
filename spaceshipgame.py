#I created this game with the help of a tutorial video by tech with tim.
#this project took me 4 hours to complete and overall i learned alot about pygame and basic gaming concepts 
import pygame 
import time 
import random 
pygame.font.init()

#setting resolution
WIDTH, HEIGHT = 1280 , 600
#i personally like this resolution and i use it in most of my games
WIN = pygame.display.set_mode((WIDTH,  HEIGHT))

#displaying the name of the game
pygame.display.set_caption("Space Invaders")

#variables for my player's coordinates
PLAYER_WIDTH = 25
PLAYER_HEIGHT = 40
PLAYER_VELOCITY = 5

#variables for my projectiles coordinates 
PROJECTILE_WIDTH = 10
PROJECTIE_HEIGHT = 17
PROJECTILE_VELOCITY = 3
#here i am creating a variable to hold my background image
BG = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH,HEIGHT))
#i used pygame.transform.scale to scale my image from (0,0) coordinates to the maximum resolution, i did this because the real imagae's size is much smaller and it was not fitting in

#creating a font variable which will hold my font, here i am using comicsans font which is in my computer. further is the size which i choose to be 30 
FONT = pygame.font.SysFont("comicsans", 30)

#creating a function to put the background
def draw(player, elapsed_time, projectiles):
    WIN.blit(BG, (0,0))
    #(0,0) are the height and widht coordinate and not mentioning anything after that means the program will fill display with background till my final coordinates which are (1280,600)
    
    #here i make a variable time text which holds the text for showing my time, first i render the font and then i use f which allows me to set TIME text in which i store the rounded off time, 1 is for anti aliasing and white is text colour
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "White")
    WIN.blit(time_text, (10,10))
    #here i set the time text with its coordinates to be (10,10)
    #drawing the player
    pygame.draw.rect(WIN, "red", player )
    
    #here we draw our projectiles
    for projectile in projectiles:
        pygame.draw.rect(WIN, "white", projectile)

    pygame.display.update()
    #this update function is used to update the screen everytime i make a change in the draw function

    



#i am creating a function to keep my game displayed on the screen in a constant loop 
def main():
    run = True 
    
    #here i set my player as a rectangle with its coordinates
    player = pygame.Rect(640, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock = pygame.time.Clock()
    #setting up clock variable which will hold the time function from pygame
    
    start_time = time.time()
    #time.time will give us current time which will be used when game starts
    elapsed_time = 0


    projectile_add_increment = 2000
    #setting 2000 milliseconds as the time when a new projectile is added to the screen
    projectile_count = 0
    #count progression for our projectile

    #this array stores projectiles
    projectiles = []
    hit = False
       
   
    while run:
        
        projectile_count += clock.tick(60)
        #this keeps the track of projectiles and keeps adding to the count with time
        #clock.tick(60)
        #60 is the maximum number of frames per second, this will delay the while look such that it will only run 60 times per second. this will slow down the speed of the game and clock it at a playable time
        
        elapsed_time = time.time() - start_time
        #current time minus the starting time will give us the time elapsed since we started the play
       
        if projectile_count > projectile_add_increment:
            #creating a loop which only runs when projectile counts is more then the mili seconds that means every 2000 seconds projectile counts increases and this loops runs
            for _ in range(5): # we are generating 5 projectiles here
                #this is for randomly spawning projectile x from 0 x coordinate and a width with the particular equation
                projectile_x = random.randint(0, WIDTH - PROJECTILE_WIDTH )
                projectile = pygame.Rect(projectile_x, -PROJECTIE_HEIGHT, PROJECTILE_WIDTH, PROJECTIE_HEIGHT)
                #here we set projectile as a rectangle which starts at the position projectile x and then we set projectile height negative so that we slowly see it appear and enter the screen then we set the height and width
                projectiles.append(projectile)
                #we add this projectile to our projectile list
            projectile_add_increment = max(200, projectile_add_increment - 50)
            #everytime this runs -50 mili seconds is done and generation of projectiles get faster and faster until it reacahes to 200 mili seconds which is where the game gets fastest, it starts from 2000 then 1950 then 1900 then 1850 and keeps the generation of 5 projectiles get faster and faster and faster 
            projectile_count = 0 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
                break
        #setting up keys for my player , velocity here represents the amount of frames being added or reduced to the players position
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_VELOCITY >= 0:
        #setting up a as moving left    #in our and condition we are asking this if statement to only run if player's current x position - player velocity is greater than equal to 0. if it goes to -1 then dont run this if statement. this prevents the player from going outside the game
            player.x -= PLAYER_VELOCITY
            #player's position - velocity (measured in pixels) = the position we desire 
        if keys[pygame.K_d] and player.x + PLAYER_VELOCITY + PLAYER_WIDTH <= WIDTH:
            #same as the above one but the only differece is i have added player width here too which will not allow the player to surpass the width of the screen which is the final x coordinate
            player.x += PLAYER_VELOCITY
        
        for projectile in projectiles[:]:
        # for loop is created for projectiles and we loop it in a list which runs it again and again
            projectile.y += PROJECTILE_VELOCITY
            #projectile's y position is added with projectiles velocity to move it forward
            if projectile.y > HEIGHT:
            #this if statement runs when projectiles y position is greater than height of the display of the game. if this happens then the projectile is simply removed and rendering stops 
                projectiles.remove(projectile)
            #this is another possibility where if projectile collides with player the also the rendering stop and hit variable turns true and we break out of the loop
            elif projectile.y + PROJECTIE_HEIGHT >= player.y and projectile.colliderect(player):
                projectiles.remove(projectile)
                hit = True
                break

        #here we make a screen which we get after the hit 
        if hit:
            # here u can add the scoreboard and everything 
            #this is where we make the text
            lost_text = FONT.render("YOU LOST!, GET BETTER", 1, "red")
            #this is where we set size of the font and set it on our screen, remember this equation it can be used in all of ur games
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            #here we update the display
            pygame.display.update()
            #this freezes the game for 4 seconds so u can see the screen
            pygame.time.delay(4000)
            break


        draw(player, elapsed_time, projectiles)
        #calling the draw function
    pygame.quit()

if __name__ == "__main__":
    main()

