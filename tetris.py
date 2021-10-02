import pygame
import time

class Game():
    def __init__(self):
        pygame.init()
        self.GameEnd = False
        self.display = pygame.display.set_mode((640 ,480))
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.z = 0
        self.x = 0
        self.y = -0 

    def start(self):
            self.timing = time.time()
            self.Matrix = Matrix(35,10)
            

    def search(self, x, y):# поиск клетки с определенными коордитами
        test = 0
        for g in self.Matrix.matrix:
            
            if g.x_real == x and g.y_real == y:
                test = 1
                #self.index = self.Matrix.matrix.index(g)
                if test == 1: 
                    return self.Matrix.matrix.index(g)
                else:
                    return None

    def motion(self):
        self.figure = L() # фигура должна выбираться случайно
        '''val = self.figure.figure_search(self.x, self.y)
        for cell in val:
            if cell != None:
                self.Matrix.matrix[cell].on(self.Matrix.matrix[cell]) 
        if time.time() - self.timing > 0.3:
            self.timing = time.time()
            for cell in val:
                if cell != None:
                    self.Matrix.matrix[cell].off(self.Matrix.matrix[cell])
            self.y += 1  '''  




        self.val1 = self.figure.figure_search(self.x, self.y)
        for cell in self.val1:
            if cell != None:
                self.Matrix.matrix[cell].on(self.Matrix.matrix[cell])
                if self.Matrix.matrix[cell].down == 0:
                    self.z = 1 
        if time.time() - self.timing > 0.3:
            self.timing = time.time()
            self.y += 1
            self.val2 = self.figure.figure_search(self.x, self.y)    
            for cell in self.val2:
                if cell != None:
                    self.Matrix.matrix[cell].on(self.Matrix.matrix[cell])
            time.sleep(0.2)
            for cell in self.val1:
                if cell != None:
                    self.Matrix.matrix[cell].off(self.Matrix.matrix[cell])
                   

    def run(self):
        self.start()
        while self.GameEnd == False:
            pygame.display.update()
            Game.motion()
            #print(str(self.Matrix.matrix[self.search(1,2)].value))
            #self.Matrix.matrix[].off(self.Matrix.matrix[self.search(1,2)])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        print("left")
                    elif event.key == pygame.K_RIGHT:
                        print("right")

                if event.type == pygame.QUIT:
                    self.GameEnd = True

            self.clock.tick(self.FPS)

class Matrix():
    def __init__(self, x, y):
        self.matrix = []
        for i in range(0, 20):
                for j in range(0, 10):
                    self.matrix.append(Cell(j*1, i*1, j*20+x, i*20+y))
        for h in self.matrix:
            h.off(h)
            if h.y == 20:
                h.down = 0

class Cell():
    def __init__(self, x, y, x_1, y_1):
        self.side = 20
        self.value = 0
        self.right = 1
        self.left = 1
        self.down = 1
        self.x_real = x
        self.y_real = y
        self.x = x_1
        self.y = y_1 

    def on(self, g):
        self.value = 1
        pygame.draw.rect(Game.display, (255, 255, 255),(g.x, g.y, 20, 20))

    def off(self, g):
        self.value = 0
        pygame.draw.rect(Game.display, (25, 25, 25),(g.x, g.y, 20, 20))

class L():
    def figure_search(self, x, y):
        return [Game.search(x, y), Game.search(x, y+1), Game.search(x, y+2), Game.search(x+1, y+2)]

class Weight():
    def __init__(self):
        self.array = []

    def in_array(self):
        self.array.append(Game.figure.index_list)

    def on_array(self):
        for i in self.array[-1]:
            Game.matrix[i].on(Game.matrix[i])
            Game.matrix[i - 10].down = 0
            Game.search(Game.matrix[i].x - 20, Game.matrix[i].y)
            if Game.test == 1:
                Game.matrix[Game.index].right = 0
            Game.search(Game.matrix[i].x + 20, Game.matrix[i].y)
            if Game.test == 1:
                Game.matrix[Game.index].left = 0
            


Game = Game()
Weight = Weight()
Game.run()  