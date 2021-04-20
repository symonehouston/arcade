import pygame, random

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

#shapes list
shapes =[[1, 5, 9, 13], [4, 5, 6, 7]],[[4, 5, 9, 10], [2, 6, 5, 9]],[[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],[[6, 7, 9, 10], [1, 5, 6, 10]],[[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],[[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],[[1, 2, 5, 6]],

#assign colors to the shape. i looked up the rgb values for the shapes on rapidtables.com
sColor = [(211,211,211), (0,0,139), (50,205,50), (255,255,0), (0,191,255), (255,0,0), (255,105,180)]

#class for Piece. time = 15 minutes
class Pieces(object):
    x = 0 #########################################
    y = 0 #########################################

    #initilize the piece with attributes
    def __init__(self, x, y):
        self.x = x #x-coordinate
        self.y = y #y-coordinate
        self.shape = random.randint(0, len(shapes) - 1) #changed it to just shapes !
        self.rotateS = 0 #handles the case where you choose a different version of one shape
        self.color = random.randint(0, len(sColor) - 1)

    #rotate shape
    def rotation(self):
        #have to make sure the number does not go over length of the
        inBound = len(self.shapes[self.shape])
        #change rotation
        self.rotateS = (self.rotateS + 1) % inBound

    #show the piece
    def displayImage(self):
        return shapes[self.shape][self.rotateS]

class Tetris:
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

    def __init__(self, height, width):
        score = 0
        self.height = height
        self.width = width
        self.grid = []
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.grid.append(new_line)

    def startSpot(self):
        self.figure = Pieces(5, 0)

    def breakL(self):
        numLines = 0
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

    #need to check if a figure is out of bounds or touching something else
    #time = .5 hour(s)
    #originally i added a top but then realized i didn't need it
    #my research also made me realize i have to account for color values
    def isTouching(self):
        touch = False #need to return a boolean
        for i in range(4):
            for n in range(4):
                if i * 4 + n in self.figure.displayImage():
                    #account for left and right
                    if self.figure.x + n < 0:
                        touch = True
                    if self.figure.x + n > self.width - 1:
                        touch = True
                    #only have to account for going down
                    if i + self.figure.y > self.height - 1:
                       touch = True
                    #checking if a color is there
                    if self.grid[self.figure.y + i][self.figure.x + n] > 0: # my logic was weong with the new button
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
        self.freeze()

pygame.init()

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tetris")

# Loop until the user clicks the close button.
go = False
down = False
clock = pygame.time.Clock()
game = Tetris(20, 10)
counter = 0

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
                game.__init__(20, 10)

    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                down = False

    screen.fill((255, 255, 255))

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, (128, 128, 128), [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.grid[i][j] > 0:
                pygame.draw.rect(screen, sColor[game.grid[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                temp = i * 4 + j
                if temp in game.figure.displayImage():
                    pygame.draw.rect(screen, sColor[game.figure.color],
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom * (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

    font = pygame.font.SysFont('timesnewroman', 25, True, False)
    font1 = pygame.font.SysFont('timesnewroman', 65, True, False)
    text = font.render("Score: " + str(game.score), True, (0, 0, 0))
    gameEnd = font1.render("Game Over", True, (0, 0, 55))
    gameEscape = font1.render("Press ESC", True, (0, 0, 55))

    screen.blit(text, [0, 0])
    if game.status == "gameover":
        screen.blit(gameEnd, [20, 200])
        screen.blit(gameEscape, [25, 265])

    pygame.display.flip()
    clock.tick(25)

pygame.quit()

