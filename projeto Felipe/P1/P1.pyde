import random

from Vehicle import Vehicle
from Food import Food

tileSize = 20;
scl = 0.1;

class Cell():
    # A cell object knows about its location in the grid 
    # it also knows of its size with the variables x,y,w,h.
    def __init__(self, tempX, tempY, tempW, tempH, tempCusto):
        self.x = tempX
        self.y = tempY
        self.w = tempW
        self.h = tempH
        self.custo = tempCusto

def drawTerrain():
    mapa = []
    for i in range (width/tileSize):
        mapa.append([])
        for j in range (height/tileSize):
            fill(getColor(i,j)[0])
            rect(i * tileSize, j * tileSize, tileSize, tileSize)
            if getColor(i,j)[1] < 0.3:
                #verde: grama com custo 0
                mapa[i].append(Cell(i*tileSize,j*tileSize,tileSize,tileSize, 0))
            elif getColor(i,j)[1] < 0.5:
                #laranja: areia com custo 1
                mapa[i].append(Cell(i*tileSize,j*tileSize,tileSize,tileSize, 1))
            elif getColor(i,j)[1] < 0.7:
                #azul: agua com custo 2
                mapa[i].append(Cell(i*tileSize,j*tileSize,tileSize,tileSize, 2))
            else:
                #preto
                mapa[i].append(Cell(i*tileSize,j*tileSize,tileSize,tileSize, 3))
            #print(mapa[i][j].x, mapa[i][j].y)
    return mapa

def getColor (x,y):
    v = noise(x * scl, y * scl)
    if v < 0.3:
        #azul
        return (color(155, 255, 255), v)
    elif v < 0.5:
        #verde
        return (color(66, 255, 255), v)
    elif v < 0.7:
        #laranja
        return (color(30, 255, 255), v)
    else:
        #preto
        return (color(0, 0, 0), v)
    
def setup():
    global v
    global f
    global mapa
    size(720, 480)
    noStroke()
    colorMode(HSB)
    
    r1 = random.randint(0, width)
    r2 = random.randint(0, height)
    r3 = random.randint(0, width)
    r4 = random.randint(0, height)
    
    v = Vehicle(r1, r2)
    f = Food(r3, r4)
    
def draw():
    #background(200)
    mapa = drawTerrain()
    
    if(round(v.location()[0]) == round(f.location()[0]) and round(v.location()[1]) == round(f.location()[1])):
        r1 = random.randint(0, width)
        r2 = random.randint(0, height)
        loc = PVector(r1,r2)
        f.update(r1, r2)
        f.comeu()

    v.arrive(f.location())


    f.display()        
    v.update()
    v.display()
    
    textSize(28)
    text("Pontuacao: ", 15, 40)
    text(str(f.comida), 170, 40)
    
