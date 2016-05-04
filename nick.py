#-------------------------------------------------------------------------------
#---[ Imports ]-----------------------------------------------------------------
#-------------------------------------------------------------------------------
import pygame
import sys
import glob

from pygame.locals import*
shooter = pygame.image.load('shooter.png')
bulletpew = pygame.image.load('bullet.png')

pygame.init()
game = True
## ---[ main ]------------------------------------------------------------------
#  This function runs the entire screen and contains the main while loop
#

       # Initialize Pygame

           # Create window
background = pygame.image.load('space.jpg')

background_size = background.get_size()
background_rect = background.get_rect()
screen = pygame.display.set_mode(background_size)
w,h = background_size
x1 = 0
y1 = 0

x2 = 0
y2 = -h

           # Set the window caption
pygame.display.set_caption('Space Shooter')



## ---[ The python script starts here! ]----------------------------------------
# Run the script

   
if game == True:
   
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    x = 10
    y = 10
    bullet = False
    bullet_speed = 80
    bx = 0
    by = 0

    # Set the height and width of the screen
     
    pygame.display.set_caption("fml")
     
    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    background = pygame.image.load('space.jpg')

    background_size = background.get_size()
    background_rect = background.get_rect()
    screen = pygame.display.set_mode(background_size)
    w,h = background_size
    x1 = 0
    y1 = 0

    x2 = 0
    y2 = -h

    class player:
        def __init__(self):
            self.x = 757
            self.y = 10
            self.ani_speed_init=10
            self.ani_speed=self.ani_speed_init
            self.ani = glob.glob("sprite_*.png")
            self.ani.sort()
            self.ani_pos=0
            self.ani_max = len(self.ani)-1
            self.img = pygame.image.load(self.ani[0])
            self.update(0)
            
        def update(self, pos):
            if pos != 0:
                self.ani_speed-=1
                self.x+=pos
                if self.ani_speed == 0:
                    self.img = pygame.image.load(self.ani[self.ani_pos])
                    self.ani_speed = self.ani_speed_init
                    if self.ani_pos == self.ani_max:
                        self.ani_pos = 0
                    else:
                        self.ani_pos+=1
            screen.blit(self.img,(self.x,self.y))    

    player1 = player()
    pos = 0        

    # Loop as long as done == False
    while not done:
     
        screen.blit(background,background_rect)
        y2 += 1
        y1 += 1
        screen.blit(background,(x1,y1))
        screen.blit(background,(x2,y2))
        if y1 > h:
            y1 = -h
        if y2 > h:
            y2 = -h    
        
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == KEYDOWN and event.key == K_UP:
                pos = -1
            elif event.type == KEYUP and event.key == K_UP:
                pos = 0
            elif event.type == KEYDOWN and event.key == K_DOWN:
                pos = 1
            elif event.type == KEYUP and event.key == K_DOWN:
                pos = 0
                

     

        # All drawing code happens after the for loop and but
        # inside the main while not done loop.
     
        # Clear the screen and set the screen background
        player1.update(pos)
        # Select the font to use, size, bold, italics
        font = pygame.font.SysFont('Calibri', 25, True, False)
     
        # Render the text. "True" means anti-aliased text.
        # Black is the color. This creates an image of the
        # letters, but does not put it on the screen

        #Controls
        keys = pygame.key.get_pressed()

        #Log last
        last_x = x
        last_y = y

        if keys[pygame.K_w]:
            y -= 8
        if keys[pygame.K_s]:
            y += 8
        if keys[pygame.K_SPACE]:
            bullet = True
            bx = x
            by = y


        if y <= 10:
            y = 10
        if y >= 567:
            y = 567

     
        # Put the image of the text on the screen at 250x250

        #Shooter
        screen.blit(shooter,[10,y])

        ###Hitboxes
        hero_hb = pygame.Rect(x, y, 50, 50)

        if bullet == True:
            screen.blit(bulletpew,[bx,by])
            bx += bullet_speed

        ###Hit Test

        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()
     
        # This limits the while loop to a max of 60 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(60)
     
    # Be IDLE friendly
    pygame.quit()


    #---[ END OF FILE ]-------------------------------------------------------------
