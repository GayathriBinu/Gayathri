#Recall, graphics coordinate system at top left corner, (0,0)

# Import pygame module 
import pygame 

# telling pygame module we want to use the following objects 

from pygame import Color, Rect, draw, display 

# Variable to be used as a parameter for display.set_mode(), the brackets are needed
SCREEN_SIZE = (500, 500)

# Initialize pygame module, should be done at the start of the program 
pygame.init()

# Create a display surface 
gameDisplay = display.set_mode(SCREEN_SIZE)

# Create background color of the sky
# covers the entire surface with the color selected 
# do this before any draw command
# see "Pygame library.html" in hapara for more colors 
gameDisplay.fill(Color('lightgreen'))

# draws rectangle on the surface 
# Usage: Rect(left, top, width, height)
draw.rect(gameDisplay, Color('lightblue'), Rect(100, 200, 300, 200))

# draw a triangle in the surface for a roof 
# Usage: draw.polygon(Surface, Color(name), [pointlist])
draw.polygon(gameDisplay, Color('yellow'), [(100, 200), (400, 200), (250, 50)])

# draw green grass on the surface
draw.rect(gameDisplay, Color('black'), Rect(0, 400, 500, 100))

# draw sun on the surface
# Usage: draw.circle(Surface, Color(name), (left, top), radius)
draw.circle(gameDisplay, Color('red'), (50, 50), 50)

# show the graphics on the screen 
# updates the contents of the surface 
display.flip()

# add to the end of program
# In order for user to see image, and program with a prompt for the user and expectation of input
# Prompt ensures that pygame window remains visible until the user ends the program
# we don't need to save the input
input('Press enter to exit')
