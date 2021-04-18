import pygame, random

#determine the size of the screen. time = 10 minutes
WIDTH = 800
HEIGHT = 700
blockW = 300
blockH = 600
blockS = 30

top_left_x = (WIDTH - HEIGHT) // 2
top_left_y = blockW - blockH

#April 1 - creating the shapes for the game. I used a youtube tutorial to help see how to code shapes and then
#drew out the different directions they could go. time = 1.5 hour(s)
#errors: keep getting an error about a tuple, and it took me awhile to find out what the problem was
#April 4 - i worked on a getting the grid to show up. i was trying to use surface to do that but kept running into problems.
#i switched my approch and redesigned the grid. time = 2.5 hour(s)
#April 8 - checked if the shapes touched and line break. time = 1 hour(s)
#April 9 - game over. time = 1 hour(s)
#April 15 - start initilize. time = .5 hour(s)
#April 18 - finish initilize and displaying the game. ran into sooo many BUGS :( time = 2.5 hours and counting

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

S = [['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....'],
      ['.....',
      '......',
      '..00..',
      '.00...',
      '......']]
#shapes list
shapes = [I,L,J,O,Z,T,S]

#assign colors to the shape. i looked up the rgb values for the shapes on rapidtables.com
sColor = [(211,211,211), (0,0,139), (50,205,50), (255,255,0), (0,191,255), (255,0,0), (255,105,180)]

#class for Piece. time = 15 minutes
class Pieces(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = random.randint(0, len(shapes) - 1) #changed it to just shapes !
        self.rotate = 0 #handles the case where you choose a different version of one shape
        self.color = random.randint(0, len(sColor) - 1)

    def rotation(self):
        #have to make sure the number does not go over length of the
        inBound = len(self.shapes[self.type])
        #change rotation
        self.rotate = (self.rotate + 1) % inBound

    def displayImage(self):
        return shapes[self.shape][self.rotate]

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
        self.height = HEIGHT
        self.width = WIDTH
        self.grid = []
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(1) #used 1 because my figures are 0
            self.grid.append(new_line)

    def startSpot(self):
        self.figure = Pieces(top_left_x, 0)

    def breakL():
        numLines = 0
        for row in range(1, self.height):
            zeros = 0
            for col in range(self.width):
                if self.field[row][col] == 0:
                    zeros += 1
            if zeros == 0:
                numLines += 1
                for x in range(row, 1, -1):
                    for y in range(self.width):
                        self.field[x][y] = self.field[x - 1][y]

    #need to check if a figure is out of bounds or touching something else
    #time = .5 hour(s)
    #originally i added a top but then realized i didn't need it
    #my research also made me realize i have to account for color values
    def isTouching(self):
        touch = False #need to return a boolean
        for i in range(4):
            for n in range(4):
                if i * 4 + n in self.figure.image():
                    #account for left and right
                    if self.figure.x + n < 0:
                        touch = True
                    if self.figure.x + n > self.width - 1:
                        touch = True
                    #only have to account for going down
                    if i + self.figure.n > self.height - 1:
                       touch = True
                    #checking if a color is there
                    if self.grid[self.figure.y + i][self.figure.x + n] == 0:
                        touch = True
        return touch

    def stopMoving(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
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

    #complete - left, right


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
        if game.state == "play":
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
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
            if event.key == pygame.K_SPACE:
                game.go_space()
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
                if temp in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color],
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

