import pygame
import random

pygame.init()

#The six lines below are defining the six colors we'll be using in our game.
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
paleRed=(200,0,0)
green = (0,255,0)
paleGreen= (34,177,76)
blue = (0,0,255)
yellow= (200,200,0)
paleYellow=(255,255,0)

#Have defined two different shades of red yellow and green to change the color of a button when you place your cursor at it, so that when your cursor is ON THE button, the button will become a lighter version of its original color.
displayWidth = 600
displayHeight = 600

# Loading the image for the head of the snake
head = pygame.image.load("head.png")

#runs a clock while the game is being executed; it enables to define frames per second for the game.
framePerSecond = pygame.time.Clock() 

screenDisplay = pygame.display.set_mode((displayWidth,displayHeight))

#Sets the title of the window that pops up when you open the game.
pygame.display.set_caption("Snake") 

#the size of the red boxes and the increase in the length snake per box
pixelSize = 10

# initial moving direstion of snake
movingDirection = "east" 

#creating three fonts of different sizes
font1 = pygame.font.SysFont(None, 30)
font2 = pygame.font.SysFont(None, 50)
font3 = pygame.font.SysFont(None, 80)


#function for snake making
def snakeMaking(pixelSize, makeSnakeList):					
        
# rotating the head of the image according to the direction

	if movingDirection == "east":
		head1 = pygame.transform.rotate(head, 270)
	elif movingDirection == "south":
		head1 = pygame.transform.rotate(head, 180)
	elif movingDirection == "west":
		head1 = pygame.transform.rotate(head, 90)
	elif movingDirection == "north":
		head1 = pygame.transform.rotate(head, 0)

        #bliting the snake on to the screen
	screenDisplay.blit(head1, (makeSnakeList[len(makeSnakeList)-1][0], makeSnakeList[len(makeSnakeList)-1][1]))	

	#for each box in the snake list, drawing a rectangle to make the snake
	for [X,Y] in makeSnakeList[:-1]:
		pygame.draw.rect(screenDisplay,blue,[X,Y,pixelSize,pixelSize]) 


# defining the function for displaying a message on the screen, y determines the displacement of the message form the center, and capacity determines the font
def messageOnScreen(message, color, y = 0, capacity= 0): 

	# according to the capacity given, selecting the font from the above created fonts
	if capacity == 1:
		surfaceOfText = font1.render(message, True, color)
	elif capacity == 2:
		surfaceOfText = font2.render(message, True, color)
	elif capacity == 3:
		surfaceOfText = font3.render(message, True, color)

        #creating a rectangle of the above font
	rectText = surfaceOfText.get_rect()
	
        #centering the rectangle created above
	rectText.center = (displayWidth/2, displayHeight/2-y)

        #bliting the text on to the rectangle which appears on the screen
	screenDisplay.blit(surfaceOfText,rectText)

# creating a finction for the different types in the game
def types():
        
	types = True
	global mode
	while types:
		screenDisplay.fill(white)
		messageOnScreen("Press C for classic mode: ", blue, 20, 1)
		messageOnScreen("Press M for modern/cave mode: ", blue, -20, 1)
		pygame.display.update()
		for event in pygame.event.get():
                        # quits the game if the users quits it
			if event.type == pygame.QUIT:				
				pygame.quit()
				quit()
			#checks for the pressing of the key
			elif(event.type == pygame.KEYDOWN):
                                # if c is pressed the mode is classic
				if(event.key == pygame.K_c): 			
					mode = "classic"
					types = False
				# if m is pressed the mode is modern/cave
				elif(event.key == pygame.K_m):			
					mode = "modern"
					types = False



def levels():
	global FPS
	level = True
	while level:
		screenDisplay.fill(white)
		#displaying various messages on the screen according to the function defined above
		messageOnScreen("Press 1 for Level 1:", red, 100, 1)
		messageOnScreen("Press 2 for Level 2:", red, 50, 1)
		messageOnScreen("Press 3 for Level 3:", red, 0, 1)
		messageOnScreen("Press 4 for Level 4:", red, -50, 1)
		messageOnScreen("Press 5 for Level 5:", red, -100, 1)


		pygame.display.update()
		for event in pygame.event.get():	        #running the loop for every event in the game
			if event.type == pygame.QUIT:	        #checking if the event calls for quiting the game
				pygame.quit()			#if it does call for quit, program quits
				quit()
			if(event.type == pygame.KEYDOWN):
				if(event.key == pygame.K_1):    #sets the frame rate to 10 if the user is playing at level 1; so the snakes very slowly
					FPS = 10
					level = False
				elif(event.key == pygame.K_2):  #sets the frame rate to 15 for level 2; so the movement of the snake on the screen is relatively faster
					FPS = 15
					level = False
				elif(event.key == pygame.K_3):  #sets the frame rate to 20 if the user opts for level 3; movement of the snake is faster than the earlier two levels.
					FPS = 20
					level = False
				elif(event.key == pygame.K_4):  #sets the frame rate to 25 for level 4; so the movement of the snake on the screen is relatively faster
					FPS = 25
					level = False
				elif(event.key == pygame.K_5):  #sets the frame rate to 30 if the user goes for maximum difficulty; the snake will move VERY quickly on the screen and the game would be harder to play.
					FPS = 30
					level = False

	framePerSecond.tick(10)



#for the start screen display
def startScreen():					

	flag = True
	while flag:
		for event in pygame.event.get():						#running the loop for every event in the game
			if event.type == pygame.QUIT:						#checking if the event calls for quiting the game
				pygame.quit()							#if it does call for quit, program quits
				quit()
			elif event.type == pygame.KEYDOWN:					#checking whether a key is pressed down	
				if event.key == pygame.K_q:					#checking if the key pressed is q, if it is quits the gameOver
					pygame.quit()
					quit()
				if(event.key == pygame.K_c):					#checking whether the key pressed is c, if it is, continues on to the game
					levels()
					types()
					mainGame()
					flag = False
					
		screenDisplay.fill(white)							#filling the screen with white color
		
		#displaying various messages on the screen according to the function defined above 
		messageOnScreen("Welcome to Snake", blue, 100, 3)
		messageOnScreen("This is a simple snake game.", black, 30, 1)
		messageOnScreen("Eat the red boxes and you get longer. ", black, -10, 1)
		messageOnScreen("Press C to continue or Q to quit", red, -90, 1 )
	
		pygame.display.update()

		
def mainGame():

        
        
	#using global variable movingDirection in the function
        global movingDirection
	
	#generating random X and Y coordinates for the apples/redboxes
        appleX = round(random.randrange(0, displayWidth - pixelSize)/10.0)*10.0
        appleY = round(random.randrange(0, displayHeight - pixelSize)/10.0)*10.0
	
	#making intial list of snake empty and length of snake equal to zero
        makeSnakeList = []
        SnakeLength = 0
	
	#calculating center coordinates of the screen
        X = displayWidth/2
        Y = displayHeight/2
	
	#initalizing the change in X equal to 10 and Y equal to zero so the snake moves along X direction
        changeX = 10
        changeY = 0

        runningGame = True #Making this true so the loop  will run as long as it is true
        gameOver = False   #game will be over when this is true
        while runningGame:
                while gameOver==True:
                        screenDisplay.fill(white)
			
			#displaying various messages on the screen according to the function defined above
                        messageOnScreen("Game Over. ", red, 100, 3)
                        messageOnScreen("Your score was: " + str(SnakeLength), black, 0, 2)
                        messageOnScreen("Press C to continue or Q to quit.", black, -100, 1)

                        pygame.display.update()

                        for event in pygame.event.get():		#running the loop for every event in the game
                                if (event.type == pygame.QUIT ):	#checking if the event calls for quiting the game, if it does then quits the loop by changing the variables to False
                                        runningGame = False
                                        gameOver = False
                                elif(event.type == pygame.KEYDOWN):	#checks for the pressing of a key
                                        if(event.key == pygame.K_q):	#if the key is q, then the program quits the loop by changing the variables to False
                                                gameOver = False
                                                runningGame = False
                                        elif(event.key == pygame.K_c):
                                                levels()		#if the user chooses to continue it calls the levels functions, types function and then the mainGame
                                                types()
                                                mainGame()

                for event in pygame.event.get():			#checking if the user wants to quit
                        if (event.type == pygame.QUIT ):
                                runningGame = False

                        if (event.type == pygame.KEYDOWN):		#checks if a key is pressed
                                
			#doesn't allow the user to move in the backward direction
                                if movingDirection == "west" and event.key == pygame.K_RIGHT:
                                        break
                                elif movingDirection == "east" and event.key == pygame.K_LEFT:
                                        break
                                elif movingDirection == "north" and event.key == pygame.K_DOWN:
                                        break
                                elif movingDirection == "south" and event.key == pygame.K_UP:
                                        break
                                elif (event.key == pygame.K_LEFT):  #if the user hits the left arrow key, it sets the direction of the snake to west(left), and changes the x-coordinate of the snake by 10 every second, and doesn't change it's y-cordinate so the snake only moves horizontally.
                                        movingDirection = "west"
                                        changeX = -pixelSize
                                        changeY = 0
                                elif (event.key == pygame.K_RIGHT): #same as the last used elif, except this time the snake moves right, so the change in x-coordinate of the snake is positive.
                                        movingDirection = "east"
                                        changeX = pixelSize
                                        changeY = 0
                                elif (event.key == pygame.K_UP):    #For up, there's a negative change in y-coordinate of the snake only, and no change in it's x-coordinate so that the snake moves vertically upwards.
                                        movingDirection = "north"
                                        changeY = -pixelSize
                                        changeX = 0
                                elif (event.key == pygame.K_DOWN):  #For up, there's a positive change in y-coordinate of the snake only, and no change in it's x-coordinate so that the snake moves vertically downwards.
                                        movingDirection = "south"
                                        changeY = pixelSize
                                        changeX = 0
                if mode== "modern":                         # if the mode is modern then the game is over if the snake touches the boundary

                        if (X >= displayWidth or X <= 0 or Y >= displayHeight or Y <= 0): #X here is the x-coordinate of the left top of the snake at any given instant, and y is it's y-coordinate. This condition ensures that when the snake hits a boundary, the game ends.

                                gameOver = True                                           #ends the game if either of that happens. First one for right boundary, second statement for left boundary, third one for upper boundary and fourth one for lower boundary.

                elif mode == "classic":                                                   # if the mode is modern then the snake somes out of the other side after touching the corners

                        if X > displayWidth:
                                X = 0 - pixelSize
                        elif X + pixelSize < 0:
                                X = displayWidth
                        elif Y > displayHeight:
                                Y = 0 - pixelSize
                        elif Y + pixelSize < 0:
                                Y =  displayHeight

		#the change in the coordinates is added in the respective X or Y
                X += changeX
                Y += changeY

                screenDisplay.fill(white)

                # creating the red box
                pygame.draw.rect(screenDisplay, red, [appleX, appleY, pixelSize, pixelSize])

                headOfSnake = []				#first an empty list
		
		#appending X and Y in to the list
                headOfSnake.append(X)
                headOfSnake.append(Y)
                makeSnakeList.append(headOfSnake)     # then appending this list into the original list made for the making of snake
                snakeMaking(pixelSize, makeSnakeList) # calling the function that was made for the making of snake

                if len(makeSnakeList) > SnakeLength:
                        del makeSnakeList[0]

                # checking for each block in the list of snake
                for eachBlock in makeSnakeList[:len(makeSnakeList)-1]:
                        # if the snake cuts itself at any point the game is over
                        if(eachBlock == headOfSnake):
                                gameOver = True

                pygame.display.update()

                # if the snake's coordinates conincides with the red box's then other random X and Y coordinates are generated for a new red box
                if X == appleX and Y == appleY:
                        appleX = round(random.randrange(0, displayWidth - pixelSize)/10.0) * 10.0
                        appleY = round(random.randrange(0, displayHeight - pixelSize)/10.0) * 10.0
                        SnakeLength += 1				#adding one to the length each time the snake eats a red box
			
                # writing score
                score = font1.render("Score: " +str(SnakeLength), True, blue)
		
                #bliting the score on to the top left corner of the screen
                screenDisplay.blit(score, [0,0])
                pygame.display.update()

                #moving the screen according to the frames given per second
                framePerSecond.tick(FPS)					

        #quits the game if comes out of the loop
        pygame.quit()
        quit()

#displays the main screen
startScreen()
mainGame()
