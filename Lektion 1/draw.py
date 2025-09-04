import pygame

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

pygame.draw.line(screen, (150, 0, 150), (100, 380), (540, 380)) # Draw a black line
pygame.draw.line(screen, (70, 60, 100), (100, 380), (100, 100)) # wall 1
pygame.draw.line(screen, (100, 100, 100), (100, 100), (320, 50) ) # Roof 1
pygame.draw.line(screen, (0, 0, 200), (320, 50), (540, 100) ) # Roof 2
pygame.draw.line(screen, (200, 0, 0), (540, 380), (540, 100) )# Wall 2
pygame.draw.line(screen, (0, 200, 0), (50, 382), (600, 382) ) #ground
pygame.draw.circle(screen, (0, 0, 200), (200, 200), radius= 50, width=1) 

# Draw the ground
# Draw the bottom of the house
# Draw two walls
# Draw the roof

# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears