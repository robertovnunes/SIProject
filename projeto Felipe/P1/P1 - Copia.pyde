import random

from Vehicle import *
from Food import *
#from flowField import flowField

class Cell():
    # A cell object knows about its location in the grid 
    # it also knows of its size with the variables x,y,w,h.
    def __init__(self, tempX, tempY, tempW, tempH, tempAngle):
        self.x = tempX
        self.y = tempY
        self.w = tempW
        self.h = tempH
        self.angle = tempAngle
    
    # Oscillation means increase angle
    def oscillate(self):
        self.angle += 0.02;
        
    def display(self):
        stroke(255)
        # Color calculated using sine wave
        fill(127+127*sin(self.angle))
        rect(self.x,self.y,self.w,self.h)

def setup():
    global v
    global f
    global mapa
    global col
    global row
    global weight
    #global flow
    size(720, 480)
    col = width/12
    row = height/12
    print(col, row)
    v = Vehicle(width / 2, height / 2)
    f = Food(width / 2, height / 2)
    mapa = makeGrid()
    for i in xrange(col):
        for j in xrange(row):
            mapa[i][j] = Cell(i*12,j*12,12,12,i+j)
    #drawPoints(mapa)
    #flow = flowField(12)
    
def makeGrid():
    global mapa, col, row
    mapa = []
    xoff = 0.0
    for i in xrange(col):
        # give each new row an empty list
        yoff = 0.0
        mapa.append([])
        for j in xrange(row):
        # Create an empty list for each row
            n = map(noise(xoff,yoff), 0, 1, 0, TWO_PI)
            weight = random.randint(0, 3)
            mapa[i].append(PVector(cos(n), sin(n), weight))
            yoff = yoff + 0.1
                
        xoff = xoff + 0.1
            
    return mapa
        

def draw():
    background(200)
    if(round(v.location()[0]) == round(f.location()[0]) and round(v.location()[1]) == round(f.location()[1])):
        r1 = random.randint(0, width)
        r2 = random.randint(0, height)
        loc = PVector(r1,r2)
        f.update(r1, r2)
        f.comeu()
    v.arrive(f.posicao)
    #v.follow(flow, f.posicao)
    #print(PVector(f.location()[0],f.location()[1]))
    #print(PVector(v.location()[0],v.location()[1]))
    for i in xrange(col):
        for j in xrange(row):
            # Oscillate and display each object
            mapa[i][j].oscillate()
            mapa[i][j].display()
    f.display()        
    v.update()
    v.display()
    
    textSize(28)
    text("Pontuacao: ", 15, 40)
    text(str(f.comida - 1), 170, 40)
    
 
