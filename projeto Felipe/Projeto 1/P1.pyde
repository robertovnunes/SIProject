import random

from Vehicle import Vehicle
from Food import Food

tileSize = 20;
scl = 0.1;

def setup():
    global v
    global f
    size(720, 480)
    noStroke()
    colorMode(HSB)
    drawTerrain()
    
    v = Vehicle(width / 2, height / 2)
    f = Food(width / 2, height / 2)
    
def draw():
    #background(200)
    drawTerrain()
    
    if(round(v.location()[0]) == round(f.location()[0]) and round(v.location()[1]) == round(f.location()[1])):
        r1 = random.randint(0, width)
        r2 = random.randint(0, height)
        loc = PVector(r1,r2)
        f.update(r1, r2)
        f.comeu()

    v.arrive(PVector(f.location()[0],f.location()[1]))
    print(PVector(f.location()[0],f.location()[1]))
    print(PVector(v.location()[0],v.location()[1]))

    f.display()        
    v.update()
    v.display()
    
    textSize(28)
    text("Pontuacao: ", 15, 40)
    text(str(f.comida - 1), 170, 40)
    
def drawTerrain():
    for i in range (width/tileSize):
        for j in range (height/tileSize):
            fill(getColor(i, j))
            rect(i * tileSize, j * tileSize, tileSize, tileSize)

def getColor (x,y):
    v = noise(x * scl, y * scl)
    if v < 0.25:
        #azul
        return color(155, 255, 255)
    elif v < 0.5:
        #laranja
        return color(30, 255, 255)
    elif v < 0.9:
        #verde
        return color(66, 255, 255)
    else:
        #preto
        return color(0, 0, 0)
