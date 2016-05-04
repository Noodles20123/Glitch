import pygame
 
# initialize game engine
pygame.init()

# set screen width/height and caption
size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')

# initialize clock. used later in the loop.
clock = pygame.time.Clock()

#Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
#player Variables
x = 10
y = 10
  
# Loop until the user clicks close button
done = False
while done == False:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    # write game logic here
    
    # clear the screen before drawing
    screen.fill((255, 255, 255)) 
    # write draw code here
    screen.blit.rect()
    
    pygame.display.update()
    # run at 20 fps
    clock.tick(20)
 
# close the window and quit
pygame.quit()