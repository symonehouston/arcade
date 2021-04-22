import pygame, random, os, pickle

#April 1 - creating the shapes for the game. I used a youtube tutorial to help see how to code shapes and then
#drew out the different directions they could go. time = 1.5 hour(s)
#errors: keep getting an error about a tuple, and it took me awhile to find out what the problem was
#April 4 - i worked on a getting the grid to show up. i was trying to use surface to do that but kept running into problems.
#i switched my approch and redesigned the grid. time = 2.5 hour(s)
#April 8 - checked if the shapes touched and line break. time = 1 hour(s)
#April 9 - game over. time = 1 hour(s)
#April 15 - start initilize. time = .5 hour(s)
#April 18 - finish initilize and displaying the game. ran into sooo many BUGS :( time = 2.5 hours and counting -> 3 hours
#changed how i did the shapes to simply it. the new approach did not work with the way i did shapes at first. i tried changing
#the way the computer interpreted the figures but it didn't work time = .5 hour(s)
#errors i found and debugged:
#   -using the same function name as a variable, rotate
#   -was using the wrong number for drawing figure (made different files and tried changing different pieces) -> time = 2 hours
#April 19 - my pieces drop but now i have a problem getting them to rotate because the function is not being recognized.
#   - fixed rotation issue but now it does not work with the grid bounds
#   - having seperate if statements caused an issue (this took awhile to figure out because i changed none of my logic, just wrote it together)
#   time = 1.5 hours
#April 20 - pieces are showing and dropping properly. only the long piece acts weird
#   - score works
#   - started working on different background options
# time = 1 hour
#April 21
#   - finish backgrounds
#   - ensure whole arcade works
# time = 2.5 hours
#   - loading screen
#   - add messages for breaking lines (could not get this to work)
# time = 1.5 hours
#   - finish commenting
# time = .5 hour

#tutorials that were helpful: https://www.techwithtim.net/tutorials/game-development-with-python/tetris-pygame/tutorial-1/ and https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318


# FIND HIGH SCORE ##############################
score_dict = pickle.load(open("score_dict.p", "rb"))
tetris_high_score = score_dict['tetris']
# END FIND HIGH SCORE ##############################
####################################################

# https://freesound.org/people/ProjectsU012/sounds/341695/
button_sound = pygame.mixer.Sound(os.path.join('sounds', 'button.wav'))
font = pygame.font.SysFont("comicsansms", 24)
font1 = pygame.font.SysFont("comicsansms", 14)

#shapes list
shapes =[[1, 5, 9, 13], [4, 5, 6, 7]],[[4, 5, 9, 10], [2, 6, 5, 9]],[[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],[[6, 7, 9, 10], [1, 5, 6, 10]],[[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],[[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],[[1, 2, 5, 6]],

#user messages
m1 = "Great job!"
m2 = "You're doing good"
m3 = "Are things stacking up?"
message = [m1,m2,m3]

#assign colors to the shape. i looked up the rgb values for the shapes on rapidtables.com
sColor = [(50,0,50), (50,0,50), (100,0,45), (0,0,139), (0,100,0), (255,255,0), (0,191,255), (255,0,0), (255,105,180)]

#class for Piece. time = 15 minutes
class Pieces(object):
    x = 0 #########################################
    y = 0 #########################################

    global shapes

    #initilize the piece with attributes
    def __init__(self, x, y):
        self.x = x #x-coordinate
        self.y = y #y-coordinate
        self.shape = random.randint(0, len(shapes) - 1) #changed it to just shapes !
        self.rotateS = 0 #handles the case where you choose a different version of one shape
        self.color = random.randint(1, len(sColor) - 1)

    #rotate shape
    def rotation(self):
        #have to make sure the number does not go over length of the
        inBound = len(shapes[self.shape])
        #change rotation
        self.rotateS = (self.rotateS + 1) % inBound

    #show the piece
    def displayImage(self):
        return shapes[self.shape][self.rotateS]

#Tetris class: defines the game
class Tetris:
    global sayM
    width = 0
    height = 0
    status = "play"
    grid = []
    x = 100
    y = 60
    shapesPresent = None
    figure = None
    score = 0
    level = 2
    zoom = 20

    #initialize the game
    def __init__(self, height, width):
        score = 0
        self.height = height
        self.width = width
        self.grid = []
        self.status = "play"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.grid.append(new_line)

    def startSpot(self):
        self.figure = Pieces(3, 0)

    def breakL(self):
        numLines = 0
        sayM = True
        for row in range(1, self.height):
            zeros = 0
            for col in range(self.width):
                if self.grid[row][col] == 0:
                    zeros += 1
            if zeros == 0:
                numLines += 1
                for x in range(row, 1, -1):
                    for y in range(self.width):
                        self.grid[x][y] = self.grid[x - 1][y]
        self.score += numLines ** 2

    #need to check if a figure is out of bounds or touching something else
    #time = .5 hour(s)
    #originally i added a top but then realized i didn't need it
    #my research also made me realize i have to account for color values
    def isTouching(self):
        touch = False #need to return a boolean
        for i in range(4):
            for n in range(4):
                if i * 4 + n in self.figure.displayImage():
                    #account for left and right and down
                    if self.figure.x + n < 0 or self.figure.x + n > self.width - 1 or self.figure.y + i > self.height - 1 or self.grid[self.figure.y + i][self.figure.x + n] > 0:
                        touch = True
        return touch

    def stopMoving(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.displayImage():
                    self.grid[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.breakL()
        self.startSpot()
        if self.isTouching():
            game.status = "gameover"

    #### all movement functions########
    def down(self):
        self.figure.y += 1
        if self.isTouching():
            self.figure.y -= 1
            self.stopMoving()

    def rotate(self):
        temp = self.figure.rotateS
        self.figure.rotation()
        if self.isTouching():
            self.figure.rotateS= temp

    #complete - left, right
    def leftRight(self, move):
        old_x = self.figure.x
        self.figure.x += move
        if self.isTouching():
            self.figure.x = old_x

    #duplicate down
    def moreDown(self):
        while not self.isTouching():
            self.figure.y += 1
        self.figure.y -= 1
        self.stopMoving()

#class to make background
class Background(pygame.sprite.Sprite):
    # Initialize
    def __init__(self):
        super(Background, self).__init__()
        self.img_load = pygame.image.load(os.path.join('images', tet))
        self.surf = pygame.transform.scale2x(self.img_load)
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = (0, 0)

#starts the game
pygame.init()
#dimensions of game
size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")

#BACKGROUND CHOICES
# Opening loop skin
pickB = True
while pickB:
    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Display text
    text = font.render('Pick your background', True, (255, 255, 255))
    screen.blit(text, (400 / 2 - text.get_rect().width / 2,
                       500 / 2 - text.get_rect().height / 2))

    option_text = font1.render('1 - mario, 2 - minecraft, 3 - smash, 4 - cream', True, (255, 255, 255))
    screen.blit(option_text, (400 / 2 - option_text.get_rect().width / 2,
                             500 / 2 - option_text.get_rect().height / 2 + text.get_rect().height))

    # Event for loop
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == KEYDOWN:

            # Check what key is pressed
            if event.key == K_1:
                tet = 'mario.jpeg'
                pickB = False
                button_sound.play()

            if event.key == K_2:
                tet = 'minecraft.jpeg'
                pickB = False
                button_sound.play()

            if event.key == K_3:
                tet = 'smash.png'
                pickB = False
                button_sound.play()

            if event.key == K_4:
                tet = 'cream.jpeg'
                pickB = False
                button_sound.play()

    # Update display
    pygame.display.flip()

tet_bg = Background()


go = False
down = False
clock = pygame.time.Clock()
game = Tetris(20, 10)
counter = 0
first = 1

while not go:
    if game.figure is None:
        game.startSpot()
    counter += 1
    if counter > 100000:
        counter = 0

    if counter % (25 // game.level // 2) == 0 or down:
        if game.status == "play":
            game.down()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_LEFT:
                game.leftRight(-1)
            if event.key == pygame.K_RIGHT:
                game.leftRight(1)
            if event.key == pygame.K_SPACE:
                game.moreDown()
            if event.key == pygame.K_ESCAPE:
                go = True


    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                down = False

    #make background appear
    screen.blit(tet_bg.surf, tet_bg.rect)

    #make grid appear
    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, (128, 128, 128), [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.grid[i][j] > 0:
                pygame.draw.rect(screen, sColor[game.grid[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    #print piece
    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                temp = i * 4 + j
                if temp in game.figure.displayImage():
                    pygame.draw.rect(screen, sColor[game.figure.color],
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom * (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

    #write score
    text = font.render("Score: " + str(game.score), True, (0, 0, 0))

    #Display text
    first += 1
    if first > 150 and first < 400:
        nice = font.render(message[0], True, (0, 0, 0))
        screen.blit(nice, [200,15])

    if first > 400:
        nice = font1.render(message[1], True, (0, 0, 0))
        screen.blit(nice, [200,20])

    #show score
    screen.blit(text, [15, 15])

    #stop game
    if game.status == "gameover":
        go = True

    pygame.display.flip()
    clock.tick(25)

# FINAL SCREEN ##############################

# New high score if player beats current high score
if game.score > tetris_high_score:
    tetris_high_score = game.score

#end screen that reports high score
if game.status == "gameover":
    screen.fill((0, 0, 0))

    # Define and display text
    text = font.render('GAME OVER', True, (255, 0, 0))
    screen.blit(text, (400 / 2 - (text.get_rect().width) / 2,
                    500 / 2 - (text.get_rect().height) / 2))

    number_text = font.render(str('Score: ' + str(game.score)), True, (255, 0, 0))
    screen.blit(number_text, (400 / 2 - number_text.get_rect().width / 2,
                            500 / 2 - number_text.get_rect().height / 2 + text.get_rect().height))

    hs_text = font.render('High Score: '+str(tetris_high_score), True, (255, 0, 0))
    screen.blit(hs_text, (400 / 2 - hs_text.get_rect().width / 2,
                        500 / 2 - hs_text.get_rect().height / 2 + 2 * text.get_rect().height))

    # Update display
    pygame.display.flip()

    # Wait 5 seconds then end
    pygame.time.delay(5000)



