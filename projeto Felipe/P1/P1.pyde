import random

from Vehicle import Vehicle
from Food import Food
from Mapa import Terreno
from flowField import flowField
from BFS import *

tileSize = 20;
scl = 3;

def setup():
    global v
    global f
    global mapa
    global flow
    size(720, 480)
    noStroke()
    colorMode(HSB)
    
    r1 = random.randint(0, width)
    r2 = random.randint(0, height)
    r3 = random.randint(0, width)
    r4 = random.randint(0, height)
    mapa = Terreno()
    flow = flowField(tileSize)
    v = Vehicle(r1, r2)
    f = Food(r3, r4)
    
def draw():
    #background(200)
    mapa.drawTerrain()
    
    if(round(v.location()[0]) == round(f.location()[0]) and round(v.location()[1]) == round(f.location()[1])):
        r1 = random.randint(0, width)
        r2 = random.randint(0, height)
        loc = PVector(r1,r2)
        f.update(r1, r2)
        f.comeu()

    v.arrive(f.location())
    #v.follow(flow, )

    f.display()        
    v.update()
    v.display()
    
    textSize(28)
    text("Pontuacao: ", 15, 40)
    text(str(f.comida), 170, 40)
    
