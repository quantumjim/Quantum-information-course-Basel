import pew # setting up tools for the pewpew

pew.init() # initialize the game engine...
screen = pew.Pix() # ...and the screen

# fill the screen with medium brightness pixels
for X in range(8):
    for Y in range(8):
        screen.pixel(X,Y,2)

B = 3 # set initial brightness

pressing = False
while True: # loop which checks for user input and responds

    keys = pew.keys() # get current key presses
    if not pressing:
        if keys&pew.K_X: # pressing X turns off the program
            break
        if keys&pew.K_UP: # if UP is pressed, increase brightness of pixel at at (6,6)
            B = min(B+1,3)
        if keys&pew.K_DOWN: # if DOWN is pressed, decrease brightness of pixel at at (6,6)
            B = max(B-1,0)
        if keys:
            pressing = True
    else:
        if not keys:
            pressing = False

    screen.pixel(6,6,B) # put a pixel at (6,6) with current brightness

    pew.show(screen) # update screen to display the above changes

    pew.tick(1/6) # pause for a sixth of a second